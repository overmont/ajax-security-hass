"""Ajax REST API client based on official PDF documentation."""
from __future__ import annotations

import asyncio
import hashlib
import logging
from typing import Any

import aiohttp

from .const import (
    AJAX_REST_API_BASE_URL,
    AJAX_REST_API_TIMEOUT,
)

_LOGGER = logging.getLogger(__name__)


class AjaxRestApiError(Exception):
    """Base exception for Ajax REST API errors."""


class AjaxRestAuthError(AjaxRestApiError):
    """Authentication error."""


class AjaxRest2FARequiredError(AjaxRestApiError):
    """2FA is required."""

    def __init__(self, request_id: str):
        """Initialize 2FA error with request ID."""
        super().__init__("Two-factor authentication required")
        self.request_id = request_id


class AjaxRestApi:
    """Ajax REST API client.

    Authentication as User (from PDF page 4-5):
    - First login via Credentials: E-mail + SHA256(password)
    - Generate a temporary token
    - Use this token for subsequent API calls
    """

    def __init__(
        self,
        api_key: str,
        email: str,
        password: str,
        password_is_hashed: bool = False,
    ):
        """Initialize the API client.

        Args:
            api_key: API Key provided by Ajax Systems
            email: User email address
            password: User password (plain or SHA256 hashed)
            password_is_hashed: True if password is already SHA256 hashed
        """
        self.api_key = api_key
        self.email = email

        # Hash password if not already hashed
        if password_is_hashed:
            self.password_hash = password
        else:
            self.password_hash = hashlib.sha256(password.encode()).hexdigest()

        self.session: aiohttp.ClientSession | None = None
        self.session_token: str | None = None  # Session token (15 min TTL)
        self.refresh_token: str | None = None  # Refresh token (7 days TTL)
        self.user_id: str | None = None  # User ID from login

        # Base headers with API key
        self._base_headers = {
            "X-Api-Key": api_key,
            "Content-Type": "application/json",
        }

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def close(self):
        """Close the session."""
        if self.session and not self.session.closed:
            await self.session.close()

    async def async_login(self) -> str:
        """Login with email and SHA256(password) to get session token.

        According to Swagger API 1.130.0:
        - Authenticates with email + SHA256(password)
        - Returns sessionToken (15 min TTL), refreshToken (7 days TTL), and userId
        - POST body: {"login": email, "passwordHash": hash}

        Returns:
            Session token string

        Raises:
            AjaxRest2FARequiredError: If 2FA is required
            AjaxRestAuthError: If authentication fails
            AjaxRestApiError: For other API errors
        """
        _LOGGER.debug("Logging in with email: %s", self.email)

        session = await self._get_session()
        url = f"{AJAX_REST_API_BASE_URL}/login"

        # Login request body according to Swagger
        payload = {
            "login": self.email,
            "passwordHash": self.password_hash,
        }

        try:
            async with session.post(
                url,
                headers=self._base_headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=AJAX_REST_API_TIMEOUT),
            ) as response:
                _LOGGER.debug("Login response status: %s", response.status)

                if response.status == 401:
                    raise AjaxRestAuthError("Invalid email or password")
                elif response.status == 403:
                    # 2FA required
                    result = await response.json()
                    request_id = result.get("requestId", "")
                    _LOGGER.info("2FA required, request_id: %s", request_id)
                    raise AjaxRest2FARequiredError(request_id)

                response.raise_for_status()
                result = await response.json()

                # Extract tokens from response (Swagger format)
                self.session_token = result.get("sessionToken")
                self.refresh_token = result.get("refreshToken")
                self.user_id = result.get("userId")

                if not self.session_token:
                    raise AjaxRestApiError("No sessionToken in login response")

                _LOGGER.info(
                    "Login successful, session token obtained (userId: %s)",
                    self.user_id
                )
                return self.session_token

        except aiohttp.ClientError as err:
            _LOGGER.error("Login request failed: %s", err)
            raise AjaxRestApiError(f"Login failed: {err}") from err
        except asyncio.TimeoutError as err:
            _LOGGER.error("Login request timeout")
            raise AjaxRestApiError("Login timeout") from err

    async def async_verify_2fa(self, request_id: str, code: str) -> str:
        """Verify 2FA code and get temporary token.

        Args:
            request_id: Request ID from login response
            code: 6-digit 2FA code

        Returns:
            Temporary token string

        Raises:
            AjaxRestAuthError: If 2FA verification fails
            AjaxRestApiError: For other API errors
        """
        _LOGGER.debug("Verifying 2FA code")

        session = await self._get_session()
        url = f"{AJAX_REST_API_BASE_URL}/login/2fa"

        headers = {
            **self._base_headers,
            "X-Request-Id": request_id,
            "X-2FA-Code": code,
        }

        try:
            async with session.post(
                url,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=AJAX_REST_API_TIMEOUT),
            ) as response:
                if response.status == 401:
                    raise AjaxRestAuthError("Invalid 2FA code")

                response.raise_for_status()
                result = await response.json()

                # 2FA returns sessionToken like normal login
                self.session_token = result.get("sessionToken")
                if not self.session_token:
                    raise AjaxRestApiError("No sessionToken in 2FA response")

                _LOGGER.info("2FA verification successful")
                return self.session_token

        except aiohttp.ClientError as err:
            _LOGGER.error("2FA verification failed: %s", err)
            raise AjaxRestApiError(f"2FA verification failed: {err}") from err
        except asyncio.TimeoutError as err:
            _LOGGER.error("2FA verification timeout")
            raise AjaxRestApiError("2FA verification timeout") from err

    async def async_refresh_token(self) -> str:
        """Refresh session token using refresh token.

        According to Swagger API 1.130.0:
        - Uses refreshToken to get a new sessionToken without re-authenticating
        - Extends session without requiring email/password
        - POST body: {"refreshToken": refresh_token, "userId": user_id}

        Returns:
            New session token string

        Raises:
            AjaxRestAuthError: If refresh token is invalid or expired
            AjaxRestApiError: For other API errors
        """
        if not self.refresh_token or not self.user_id:
            raise AjaxRestApiError(
                "No refresh token available. Call async_login() first."
            )

        _LOGGER.debug("Refreshing session token for user: %s", self.user_id)

        session = await self._get_session()
        url = f"{AJAX_REST_API_BASE_URL}/refresh"

        # Refresh request body according to Swagger
        payload = {
            "refreshToken": self.refresh_token,
            "userId": self.user_id,
        }

        try:
            async with session.post(
                url,
                headers=self._base_headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=AJAX_REST_API_TIMEOUT),
            ) as response:
                _LOGGER.debug("Refresh response status: %s", response.status)

                if response.status == 401:
                    raise AjaxRestAuthError("Refresh token expired or invalid")

                response.raise_for_status()
                result = await response.json()

                # Extract new tokens from response
                self.session_token = result.get("sessionToken")
                self.refresh_token = result.get("refreshToken")
                # userId should remain the same

                if not self.session_token:
                    raise AjaxRestApiError("No sessionToken in refresh response")

                _LOGGER.info(
                    "Session token refreshed successfully (userId: %s)",
                    self.user_id
                )
                return self.session_token

        except aiohttp.ClientError as err:
            _LOGGER.error("Token refresh request failed: %s", err)
            raise AjaxRestApiError(f"Token refresh failed: {err}") from err
        except asyncio.TimeoutError as err:
            _LOGGER.error("Token refresh request timeout")
            raise AjaxRestApiError("Token refresh timeout") from err

    async def _request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, Any] | None = None,
        _retry_on_auth_error: bool = True,
    ) -> Any:
        """Make API request with session token.

        Automatically renews the token if it expires (401 error).

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            data: Optional JSON data for POST/PUT requests
            _retry_on_auth_error: Internal flag to prevent infinite retry loop

        Returns:
            API response as dict

        Raises:
            AjaxRestAuthError: If authentication fails
            AjaxRestApiError: For other API errors
        """
        if not self.session_token:
            raise AjaxRestApiError("Not logged in. Call async_login() first.")

        url = f"{AJAX_REST_API_BASE_URL}/{endpoint}"
        session = await self._get_session()

        # Headers with session token (Swagger spec)
        headers = {
            **self._base_headers,
            "X-Session-Token": self.session_token,
        }

        _LOGGER.debug("Making %s request to %s", method, endpoint)

        try:
            async with session.request(
                method,
                url,
                headers=headers,
                json=data,
                timeout=aiohttp.ClientTimeout(total=AJAX_REST_API_TIMEOUT),
            ) as response:
                _LOGGER.debug(
                    "Response from %s: status=%s", endpoint, response.status
                )

                if response.status == 401:
                    if _retry_on_auth_error:
                        # Token expired, try to refresh it first
                        _LOGGER.warning(
                            "Token expired (401), attempting token refresh"
                        )
                        try:
                            # Try refresh token first (faster, no password needed)
                            await self.async_refresh_token()
                            _LOGGER.info("Token refreshed successfully, retrying request")
                            # Retry the request with the new token (only once)
                            return await self._request(
                                method, endpoint, data, _retry_on_auth_error=False
                            )
                        except AjaxRestAuthError:
                            # Refresh token expired or invalid, fallback to full login
                            _LOGGER.warning(
                                "Refresh token failed, falling back to full login"
                            )
                            try:
                                await self.async_login()
                                _LOGGER.info("Full login successful, retrying request")
                                return await self._request(
                                    method, endpoint, data, _retry_on_auth_error=False
                                )
                            except Exception as err:
                                _LOGGER.error("Failed to renew token: %s", err)
                                raise AjaxRestAuthError("Token renewal failed") from err
                        except Exception as err:
                            _LOGGER.error("Token refresh failed: %s", err)
                            raise AjaxRestAuthError("Token refresh failed") from err
                    else:
                        # Already retried once, give up
                        _LOGGER.error("Authentication failed after token renewal")
                        raise AjaxRestAuthError("Invalid or expired token")
                elif response.status == 403:
                    _LOGGER.error(
                        "Access denied (403) - Insufficient permissions"
                    )
                    raise AjaxRestAuthError("Access denied")

                response.raise_for_status()
                result = await response.json()
                _LOGGER.debug("Successfully received data from %s", endpoint)
                return result

        except aiohttp.ClientError as err:
            _LOGGER.error("API request to %s failed: %s", endpoint, err)
            raise AjaxRestApiError(f"API request failed: {err}") from err
        except asyncio.TimeoutError as err:
            _LOGGER.error("API request to %s timed out after %ss", endpoint, AJAX_REST_API_TIMEOUT)
            raise AjaxRestApiError("API request timeout") from err

    # User methods
    async def async_get_account(self) -> dict[str, Any]:
        """Get current user account information.

        Returns:
            User account dictionary with phone, firstName, language, etc.
        """
        return await self._request("GET", "user")

    # Hub methods
    async def async_get_hubs(self) -> list[dict[str, Any]]:
        """Get all hubs.

        Returns:
            List of hub dictionaries
        """
        if not self.user_id:
            raise AjaxRestApiError("No user_id available. Call async_login() first.")
        return await self._request("GET", f"user/{self.user_id}/hubs")

    async def async_get_hub(self, hub_id: str) -> dict[str, Any]:
        """Get hub details.

        Args:
            hub_id: Hub ID

        Returns:
            Hub details dictionary
        """
        if not self.user_id:
            raise AjaxRestApiError("No user_id available. Call async_login() first.")
        return await self._request("GET", f"user/{self.user_id}/hubs/{hub_id}")

    async def async_get_hub_mode(self, hub_id: str) -> dict[str, Any]:
        """Get hub alarm mode.

        Args:
            hub_id: Hub ID

        Returns:
            Hub mode dictionary
        """
        return await self._request("GET", f"hubs/{hub_id}/mode")

    async def async_set_hub_mode(self, hub_id: str, mode: str) -> dict[str, Any]:
        """Set hub alarm mode.

        Args:
            hub_id: Hub ID
            mode: Alarm mode (full, partial_1, night, disarmed)

        Returns:
            Updated hub mode
        """
        return await self._request("POST", f"hubs/{hub_id}/mode", {"mode": mode})

    # Device methods
    async def async_get_devices(self, hub_id: str) -> list[dict[str, Any]]:
        """Get all devices for a specific hub.

        Args:
            hub_id: Hub ID

        Returns:
            List of device dictionaries
        """
        return await self._request("GET", f"user/{self.user_id}/hubs/{hub_id}/devices")

    async def async_get_device(self, hub_id: str, device_id: str) -> dict[str, Any]:
        """Get device details.

        Args:
            hub_id: Hub ID
            device_id: Device ID

        Returns:
            Device details dictionary
        """
        return await self._request("GET", f"user/{self.user_id}/hubs/{hub_id}/devices/{device_id}")

    async def async_get_device_state(self, device_id: str) -> dict[str, Any]:
        """Get device state.

        Args:
            device_id: Device ID

        Returns:
            Device state dictionary
        """
        return await self._request("GET", f"devices/{device_id}/state")

    # Relay methods
    async def async_set_relay_state(self, device_id: str, state: bool) -> dict[str, Any]:
        """Set relay state (on/off).

        Args:
            device_id: Relay device ID
            state: True for on, False for off

        Returns:
            Updated relay state
        """
        return await self._request(
            "POST",
            f"devices/{device_id}/control",
            {"state": "on" if state else "off"}
        )

    async def async_pulse_relay(self, device_id: str, duration: int = 1) -> dict[str, Any]:
        """Trigger relay pulse (for gates, doors, etc.).

        Args:
            device_id: Relay device ID
            duration: Pulse duration in seconds

        Returns:
            Relay response
        """
        return await self._request(
            "POST",
            f"devices/{device_id}/control",
            {"action": "pulse", "duration": duration}
        )

    # Socket methods
    async def async_set_socket_state(self, device_id: str, state: bool) -> dict[str, Any]:
        """Set socket state (on/off).

        Args:
            device_id: Socket device ID
            state: True for on, False for off

        Returns:
            Updated socket state
        """
        return await self._request(
            "POST",
            f"devices/{device_id}/control",
            {"state": "on" if state else "off"}
        )

    async def async_get_socket_power(self, device_id: str) -> dict[str, Any]:
        """Get socket power consumption.

        Args:
            device_id: Socket device ID

        Returns:
            Power consumption data
        """
        return await self._request("GET", f"devices/{device_id}/power")

    # Camera methods
    async def async_get_cameras(self) -> list[dict[str, Any]]:
        """Get all cameras.

        Returns:
            List of camera dictionaries
        """
        return await self._request("GET", "cameras")

    async def async_get_camera(self, camera_id: str) -> dict[str, Any]:
        """Get camera details.

        Args:
            camera_id: Camera ID

        Returns:
            Camera details dictionary
        """
        return await self._request("GET", f"cameras/{camera_id}")

    async def async_get_camera_snapshot(self, camera_id: str) -> bytes:
        """Get camera snapshot.

        Args:
            camera_id: Camera ID

        Returns:
            Snapshot image data as bytes
        """
        url = f"{AJAX_REST_API_BASE_URL}/cameras/{camera_id}/snapshot"
        session = await self._get_session()

        headers = {
            **self._base_headers,
            "X-Session-Token": self.session_token,
        }

        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.read()

    async def async_get_camera_stream_url(self, camera_id: str) -> str:
        """Get camera stream URL.

        Args:
            camera_id: Camera ID

        Returns:
            Stream URL string
        """
        data = await self._request("GET", f"cameras/{camera_id}/stream")
        return data.get("url", "")

    # Light/Button methods
    async def async_set_light_state(
        self,
        device_id: str,
        state: bool,
        brightness: int | None = None,
    ) -> dict[str, Any]:
        """Set light state.

        Args:
            device_id: Light device ID
            state: True for on, False for off
            brightness: Optional brightness (0-100)

        Returns:
            Updated light state
        """
        payload = {"state": "on" if state else "off"}
        if brightness is not None:
            payload["brightness"] = brightness
        return await self._request("POST", f"devices/{device_id}/control", payload)

    # Automation methods
    async def async_get_automations(self, hub_id: str) -> list[dict[str, Any]]:
        """Get hub automations/scenarios.

        Args:
            hub_id: Hub ID

        Returns:
            List of automation dictionaries
        """
        return await self._request("GET", f"hubs/{hub_id}/automations")

    async def async_trigger_automation(
        self,
        hub_id: str,
        automation_id: str,
    ) -> dict[str, Any]:
        """Trigger automation/scenario.

        Args:
            hub_id: Hub ID
            automation_id: Automation ID

        Returns:
            Automation trigger response
        """
        return await self._request(
            "POST",
            f"hubs/{hub_id}/automations/{automation_id}/trigger"
        )

    # Events methods
    async def async_get_events(self, hub_id: str, limit: int = 100) -> list[dict[str, Any]]:
        """Get hub events history.

        Args:
            hub_id: Hub ID
            limit: Maximum number of events to return

        Returns:
            List of event dictionaries
        """
        return await self._request("GET", f"hubs/{hub_id}/events?limit={limit}")

    # NVR methods
    async def async_get_nvr_status(self, nvr_id: str) -> dict[str, Any]:
        """Get NVR status.

        Args:
            nvr_id: NVR device ID

        Returns:
            NVR status dictionary
        """
        return await self._request("GET", f"devices/{nvr_id}/status")

    async def async_get_nvr_recordings(
        self,
        nvr_id: str,
        camera_id: str,
        start: str,
        end: str,
    ) -> list[dict[str, Any]]:
        """Get NVR recordings for a camera.

        Args:
            nvr_id: NVR device ID
            camera_id: Camera ID
            start: Start time (ISO format)
            end: End time (ISO format)

        Returns:
            List of recording dictionaries
        """
        return await self._request(
            "GET",
            f"devices/{nvr_id}/recordings?cameraId={camera_id}&start={start}&end={end}"
        )
