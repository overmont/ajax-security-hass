"""Ajax API client."""
from __future__ import annotations

import hashlib
import logging
from typing import Any

import grpc

from .const import (
    API_BASE_URL,
    API_PORT,
    DEFAULT_DEVICE_MODEL,
    DEFAULT_VERSION,
    DEFAULT_OS,
    DEFAULT_APP_LABEL,
    DEFAULT_DEVICE_TYPE,
)

# Import generated protobuf stubs
from custom_components.ajax.v3.mobilegwsvc.service.login_by_password import (
    endpoint_pb2_grpc as login_pb2_grpc,
    request_pb2 as login_request_pb2,
    response_pb2 as login_response_pb2,
)
from custom_components.ajax.v3.mobilegwsvc.service.find_user_spaces_with_pagination import (
    endpoint_pb2_grpc as spaces_pb2_grpc,
    request_pb2 as spaces_request_pb2,
    response_pb2 as spaces_response_pb2,
)
from custom_components.ajax.v3.mobilegwsvc.service.stream_light_devices import (
    endpoint_pb2_grpc as light_devices_pb2_grpc,
    request_pb2 as light_devices_request_pb2,
    response_pb2 as light_devices_response_pb2,
)
from custom_components.ajax.v3.mobilegwsvc.commonmodels.type import user_role_pb2

# Import space security service
from custom_components.ajax.systems.ajax.api.mobile.v2.space.security import (
    space_security_endpoints_pb2_grpc,
    arm_request_pb2,
    disarm_request_pb2,
    arm_to_night_mode_request_pb2,
)
from custom_components.ajax.systems.ajax.api.mobile.v2.common.space import space_locator_pb2

_LOGGER = logging.getLogger(__name__)


class AjaxApiError(Exception):
    """Base exception for Ajax API errors."""


class AjaxAuthError(AjaxApiError):
    """Exception for authentication errors."""


class AjaxApi:
    """Ajax API client using gRPC."""

    def __init__(
        self,
        email: str,
        password: str,
        device_id: str,
        device_model: str = DEFAULT_DEVICE_MODEL,
    ) -> None:
        """Initialize the Ajax API client."""
        self.email = email
        self.password = password
        self.device_id = device_id
        self.device_model = device_model

        self.session_token: bytes | None = None
        self.user_id: str | None = None
        self.user_name: str | None = None

        # Create gRPC channel
        credentials = grpc.ssl_channel_credentials()
        self.channel = grpc.aio.secure_channel(
            f"{API_BASE_URL}:{API_PORT}",
            credentials,
        )

    def _get_metadata(self, include_auth: bool = False) -> list[tuple[str, str]]:
        """Get gRPC metadata headers."""
        metadata = [
            ("user-agent", "grpc-java-okhttp/1.75.0"),
            ("content-type", "application/grpc"),
            ("client-device-id", self.device_id),
            ("client-device-model", self.device_model),
            ("client-version-major", DEFAULT_VERSION),
            ("client-os", DEFAULT_OS),
            ("application-label", DEFAULT_APP_LABEL),
            ("client-device-type", DEFAULT_DEVICE_TYPE),
        ]

        if include_auth and self.session_token:
            metadata.extend([
                ("client-session-token", self.session_token.hex()),
                ("a911-user-id", self.user_id or ""),
                ("client-user-login", self.email),
                ("client-user-role", "USER"),
            ])

        return metadata

    async def async_login(self) -> dict[str, Any]:
        """Login to Ajax and get session token."""
        try:
            # Hash password with SHA256
            password_hash = hashlib.sha256(self.password.encode()).hexdigest()

            _LOGGER.debug("Attempting to login with email: %s", self.email)

            # Create login request
            request = login_request_pb2.LoginByPasswordRequest(
                email=self.email,
                password_sha256_hash=password_hash,
                user_role=user_role_pb2.USER_ROLE_USER,
            )

            # Create stub and call login service
            stub = login_pb2_grpc.LoginByPasswordServiceStub(self.channel)
            response = await stub.execute(request, metadata=self._get_metadata())

            # Check response type
            if response.HasField("success"):
                # Extract session token and user info
                self.session_token = response.success.session_token

                account = response.success.lite_account
                if account:
                    self.user_id = account.user_hex_id
                    # Build full name from first_name and last_name
                    name_parts = []
                    if account.first_name:
                        name_parts.append(account.first_name)
                    if account.last_name:
                        name_parts.append(account.last_name)
                    self.user_name = " ".join(name_parts) if name_parts else account.email
                else:
                    self.user_id = None
                    self.user_name = self.email

                _LOGGER.info("Successfully logged in as %s (ID: %s)", self.user_name, self.user_id)

                return {
                    "session_token": self.session_token.hex(),
                    "user_id": self.user_id,
                    "user_name": self.user_name,
                }
            elif response.HasField("failure"):
                # Handle various failure cases
                failure = response.failure
                if failure.HasField("invalid_credentials"):
                    raise AjaxAuthError("Invalid email or password")
                elif failure.HasField("account_not_confirmed"):
                    raise AjaxAuthError("Account not confirmed")
                elif failure.HasField("account_locked"):
                    raise AjaxAuthError("Account is locked")
                elif failure.HasField("two_fa_required"):
                    raise AjaxAuthError("Two-factor authentication required (not yet supported)")
                else:
                    raise AjaxAuthError("Login failed: Unknown error")
            else:
                raise AjaxApiError("Invalid login response")

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error during login: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Invalid credentials") from err
            raise AjaxApiError(f"gRPC error: {err}") from err
        except (AjaxAuthError, AjaxApiError):
            raise
        except Exception as err:
            _LOGGER.exception("Unexpected error during login")
            raise AjaxApiError(f"Login failed: {err}") from err

    async def async_get_account(self) -> dict[str, Any]:
        """Get account information."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated. Call async_login() first.")

        # Return cached info from login
        return {
            "user_hex_id": self.user_id,
            "name": self.user_name,
            "email": self.email,
        }

    async def async_get_spaces(self) -> list[dict[str, Any]]:
        """Get list of user spaces (hubs/systems)."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated. Call async_login() first.")

        try:
            # Create request for finding user spaces
            # Structure: limit (int), pagination (token), search_phrase (str)
            request = spaces_request_pb2.FindUserSpacesWithPaginationRequest(
                limit=100,  # Get up to 100 spaces
                search_phrase="",  # No search filter
            )

            # Create stub and call service
            stub = spaces_pb2_grpc.FindUserSpacesWithPaginationServiceStub(self.channel)
            response = await stub.execute(
                request, metadata=self._get_metadata(include_auth=True)
            )

            spaces = []
            if response.HasField("success"):
                for space in response.success.spaces:
                    space_data = {
                        "id": space.id if hasattr(space, "id") else "",
                        "name": space.profile.name if hasattr(space, "profile") and hasattr(space.profile, "name") else "Unknown",
                    }

                    # Add hub_id if available
                    if hasattr(space, "hub_id") and space.hub_id:
                        space_data["hub_id"] = space.hub_id

                    spaces.append(space_data)

                _LOGGER.info("Found %d spaces", len(spaces))
                return spaces
            elif response.HasField("failure"):
                _LOGGER.error("Failed to get spaces: %s", response.failure)
                raise AjaxApiError("Failed to get spaces")
            else:
                _LOGGER.warning("Empty response when getting spaces")
                return []

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error getting spaces: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Session expired") from err
            raise AjaxApiError(f"gRPC error: {err}") from err
        except (AjaxAuthError, AjaxApiError):
            raise
        except Exception as err:
            _LOGGER.exception("Unexpected error getting spaces")
            raise AjaxApiError(f"Failed to get spaces: {err}") from err

    async def async_get_devices(self, space_id: str) -> list[dict[str, Any]]:
        """Get list of devices for a given space."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated. Call async_login() first.")

        try:
            _LOGGER.debug("Fetching devices for space_id: %s", space_id)

            # Create request for streaming light devices
            request = light_devices_request_pb2.StreamLightDevicesRequest(
                space_id=space_id
            )

            # Create stub and call service (streaming response)
            stub = light_devices_pb2_grpc.StreamLightDevicesServiceStub(self.channel)
            response_stream = stub.execute(
                request, metadata=self._get_metadata(include_auth=True)
            )

            devices = []
            response_count = 0

            # Read the stream - first message should be a snapshot
            async for response in response_stream:
                response_count += 1
                _LOGGER.debug("Received response #%d from device stream", response_count)

                if response.HasField("success"):
                    if response.success.HasField("snapshot"):
                        snapshot = response.success.snapshot
                        _LOGGER.info(
                            "Received device snapshot with %d light_devices",
                            len(snapshot.light_devices)
                        )

                        # Process snapshot with all devices
                        for idx, light_device in enumerate(snapshot.light_devices):
                            _LOGGER.debug("Processing light_device #%d", idx + 1)
                            device_data = self._parse_light_device(light_device)
                            if device_data:
                                devices.append(device_data)
                            else:
                                _LOGGER.debug("light_device #%d returned no data (unsupported type or parsing error)", idx + 1)

                        # After receiving snapshot, we can break (updates would follow in real streaming)
                        _LOGGER.debug("Snapshot processed, stopping stream")
                        break
                    elif response.success.HasField("updates"):
                        _LOGGER.debug("Received updates (skipping)")
                        # Skip updates for now - we only need initial snapshot
                        continue
                elif response.HasField("failure"):
                    _LOGGER.error("Failed to get devices: %s", response.failure)
                    raise AjaxApiError("Failed to get devices")
                else:
                    _LOGGER.warning("Unknown response type received")

            _LOGGER.info("Found %d devices in space %s", len(devices), space_id)
            return devices

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error getting devices: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Session expired") from err
            raise AjaxApiError(f"gRPC error: {err}") from err
        except (AjaxAuthError, AjaxApiError):
            raise
        except Exception as err:
            _LOGGER.exception("Unexpected error getting devices")
            raise AjaxApiError(f"Failed to get devices: {err}") from err

    def _parse_light_device(self, light_device) -> dict[str, Any] | None:
        """Parse a LightDevice protobuf message to a dict."""
        try:
            _LOGGER.debug("Parsing LightDevice: %s", light_device)

            # LightDevice can be a hub_device, video_edge, video_edge_channel, or smart_lock
            if light_device.HasField("hub_device"):
                hub_dev = light_device.hub_device
                _LOGGER.debug("Found hub_device")

                if not hub_dev.HasField("common_device"):
                    _LOGGER.warning("hub_device has no common_device field")
                    return None

                common = hub_dev.common_device
                profile = common.profile

                object_type_str = self._get_device_type(common.object_type)

                _LOGGER.info(
                    "Device found - Name: '%s', Type: '%s', ID: %s",
                    profile.name,
                    object_type_str,
                    profile.id
                )

                device_data = {
                    "id": profile.id,
                    "name": profile.name,
                    "type": object_type_str,
                    "hub_id": common.hub_id,
                    "room_id": profile.room_id if profile.room_id else None,
                    "group_id": profile.group_id if profile.group_id else None,
                    "malfunctions": profile.malfunctions,
                    "bypassed": profile.bypassed,
                    "states": [str(state) for state in profile.states],
                    "online": True,  # TODO: Parse status to determine online state
                }

                # Add device color, label, and marketing ID
                if hasattr(profile, "device_color"):
                    device_data["device_color"] = str(profile.device_color).split("_")[-1]
                if hasattr(profile, "device_label"):
                    device_data["device_label"] = str(profile.device_label).split("_")[-1]
                if hasattr(profile, "device_marketing_id"):
                    device_data["device_marketing_id"] = profile.device_marketing_id

                # Parse statuses for battery, SIM, firmware, etc.
                device_data["battery_level"] = None
                device_data["battery_state"] = None
                device_data["firmware_version"] = None
                device_data["hardware_version"] = None

                # Store complex attributes separately
                attributes = {}

                # Track SIM cards status (for dual-SIM hubs)
                sim_cards = []

                for status in profile.statuses:
                    try:
                        if status.HasField("battery"):
                            device_data["battery_level"] = status.battery.charge_level_percentage
                            device_data["battery_state"] = str(status.battery.battery_state).split("_")[-1]
                        elif status.HasField("sim_status"):
                            # Log the full SIM status structure
                            _LOGGER.debug("Raw SIM status object: %s", status.sim_status)

                            # Parse individual SIM card status
                            # The enum value might be something like "SIM_CARD_STATUS_MISSING" or just the number
                            sim_status_raw = str(status.sim_status.sim_card_status)
                            _LOGGER.debug("Raw SIM status string: %s", sim_status_raw)

                            # Extract just the status name (e.g., "MISSING" from "SIM_CARD_STATUS_MISSING")
                            if "SIM_CARD_STATUS_" in sim_status_raw:
                                sim_status_str = sim_status_raw.split("SIM_CARD_STATUS_")[-1]
                            else:
                                sim_status_str = sim_status_raw

                            sim_info = {
                                "status": sim_status_str,
                                "installed": sim_status_str not in ["MISSING", "NOT_INSTALLED", "2"],
                            }

                            # Check if there's a slot number or if this is aggregated data
                            if hasattr(status.sim_status, "slot"):
                                sim_info["slot"] = status.sim_status.slot

                            sim_cards.append(sim_info)
                            _LOGGER.info("Found SIM card slot: status='%s', installed=%s", sim_status_str, sim_info["installed"])
                    except ValueError as e:
                        # Some status fields may not exist on all devices
                        _LOGGER.debug("Error parsing status: %s", e)
                        pass

                    # Check for firmware/hardware without HasField (safer)
                    try:
                        if hasattr(status, "firmware") and status.firmware:
                            if hasattr(status.firmware, "version"):
                                device_data["firmware_version"] = status.firmware.version
                    except (AttributeError, ValueError):
                        pass

                    try:
                        if hasattr(status, "hardware") and status.hardware:
                            if hasattr(status.hardware, "version"):
                                device_data["hardware_version"] = status.hardware.version
                    except (AttributeError, ValueError):
                        pass

                # Process SIM cards status
                if sim_cards:
                    installed_count = sum(1 for sim in sim_cards if sim["installed"])

                    # Detect total SIM slots based on device type
                    # Hub 2 Plus and Hub 2 (4G) have 2 SIM slots
                    device_type_lower = object_type_str.lower()
                    if "hub" in device_type_lower and ("plus" in device_type_lower or "4g" in device_type_lower or "two" in device_type_lower):
                        expected_slots = 2
                    else:
                        expected_slots = len(sim_cards)

                    # If we only got 1 status but expect 2 slots, it means both are empty/missing
                    if len(sim_cards) == 1 and sim_cards[0]["status"] == "MISSING" and expected_slots == 2:
                        total_slots = 2
                        installed_count = 0
                        _LOGGER.info("Hub has 2 SIM slots, both empty (API returned single MISSING status)")
                    else:
                        total_slots = max(len(sim_cards), expected_slots)

                    attributes["sim_status"] = f"{installed_count}/{total_slots}"
                    attributes["sim_cards"] = sim_cards
                    attributes["sim_slots_total"] = total_slots
                    attributes["sim_slots_used"] = installed_count
                    _LOGGER.info("SIM status: %d/%d slots used (device type: %s)", installed_count, total_slots, object_type_str)

                # Add attributes dict if we have any
                if attributes:
                    device_data["attributes"] = attributes

                _LOGGER.debug("Parsed device data: %s", device_data)
                return device_data

            elif light_device.HasField("video_edge"):
                _LOGGER.debug("Found video_edge device (not yet implemented)")
                return None
            elif light_device.HasField("video_edge_channel"):
                _LOGGER.debug("Found video_edge_channel device (not yet implemented)")
                return None
            elif light_device.HasField("smart_lock"):
                _LOGGER.debug("Found smart_lock device (not yet implemented)")
                return None
            else:
                _LOGGER.warning("Unknown LightDevice type: %s", light_device)
                return None

        except Exception as err:
            _LOGGER.exception("Failed to parse light device: %s", err)
            return None

    def _get_device_type(self, object_type) -> str:
        """Convert protobuf ObjectType to string."""
        # Map object type enum to friendly names
        # For now, return the string representation
        return str(object_type).split(".")[-1].lower() if object_type else "unknown"

    async def async_arm(self, space_id: str) -> None:
        """Arm the security system."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated")

        try:
            _LOGGER.info("Arming space: %s", space_id)

            # Create space locator
            space_locator = space_locator_pb2.SpaceLocator(space_id=space_id)

            # Create arm request
            request = arm_request_pb2.ArmSpaceRequest(
                space_locator=space_locator,
                ignore_alarms=False,
            )

            # Create stub and call service
            stub = space_security_endpoints_pb2_grpc.SpaceSecurityServiceStub(self.channel)
            response = await stub.arm(request, metadata=self._get_metadata(include_auth=True))

            # Check response
            if response.HasField("success"):
                _LOGGER.info("Successfully armed space %s", space_id)
            elif response.HasField("failure"):
                failure = response.failure
                error_msg = "Unknown error"

                if failure.HasField("hub_offline"):
                    error_msg = "Hub is offline"
                elif failure.HasField("hub_busy"):
                    error_msg = "Hub is busy"
                elif failure.HasField("hub_detected_malfunctions"):
                    error_msg = "Hub detected malfunctions"
                elif failure.HasField("permission_denied"):
                    error_msg = "Permission denied"
                elif failure.HasField("already_in_the_requested_security_state"):
                    error_msg = "Already armed"
                elif failure.HasField("space_locked"):
                    error_msg = "Space is locked"

                _LOGGER.error("Failed to arm space: %s", error_msg)
                raise AjaxApiError(f"Failed to arm: {error_msg}")

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error arming system: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Session expired") from err
            raise AjaxApiError(f"gRPC error: {err}") from err

    async def async_disarm(self, space_id: str) -> None:
        """Disarm the security system."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated")

        try:
            _LOGGER.info("Disarming space: %s", space_id)

            # Create space locator
            space_locator = space_locator_pb2.SpaceLocator(space_id=space_id)

            # Create disarm request
            request = disarm_request_pb2.DisarmSpaceRequest(
                space_locator=space_locator,
            )

            # Create stub and call service
            stub = space_security_endpoints_pb2_grpc.SpaceSecurityServiceStub(self.channel)
            response = await stub.disarm(request, metadata=self._get_metadata(include_auth=True))

            # Check response
            if response.HasField("success"):
                _LOGGER.info("Successfully disarmed space %s", space_id)
            elif response.HasField("failure"):
                failure = response.failure
                error_msg = "Unknown error"

                if failure.HasField("hub_offline"):
                    error_msg = "Hub is offline"
                elif failure.HasField("hub_busy"):
                    error_msg = "Hub is busy"
                elif failure.HasField("permission_denied"):
                    error_msg = "Permission denied"
                elif failure.HasField("already_in_the_requested_security_state"):
                    error_msg = "Already disarmed"
                elif failure.HasField("space_locked"):
                    error_msg = "Space is locked"

                _LOGGER.error("Failed to disarm space: %s", error_msg)
                raise AjaxApiError(f"Failed to disarm: {error_msg}")

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error disarming system: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Session expired") from err
            raise AjaxApiError(f"gRPC error: {err}") from err

    async def async_arm_night_mode(self, space_id: str) -> None:
        """Activate night mode."""
        if not self.session_token:
            raise AjaxAuthError("Not authenticated")

        try:
            _LOGGER.info("Arming space to night mode: %s", space_id)

            # Create space locator
            space_locator = space_locator_pb2.SpaceLocator(space_id=space_id)

            # Create arm to night mode request
            request = arm_to_night_mode_request_pb2.ArmSpaceToNightModeRequest(
                space_locator=space_locator,
                ignore_alarms=False,
            )

            # Create stub and call service
            stub = space_security_endpoints_pb2_grpc.SpaceSecurityServiceStub(self.channel)
            response = await stub.armToNightMode(request, metadata=self._get_metadata(include_auth=True))

            # Check response
            if response.HasField("success"):
                _LOGGER.info("Successfully armed space %s to night mode", space_id)
            elif response.HasField("failure"):
                failure = response.failure
                error_msg = "Unknown error"

                if failure.HasField("hub_offline"):
                    error_msg = "Hub is offline"
                elif failure.HasField("hub_busy"):
                    error_msg = "Hub is busy"
                elif failure.HasField("hub_detected_malfunctions"):
                    error_msg = "Hub detected malfunctions"
                elif failure.HasField("permission_denied"):
                    error_msg = "Permission denied"
                elif failure.HasField("already_in_the_requested_security_state"):
                    error_msg = "Already in night mode"
                elif failure.HasField("space_locked"):
                    error_msg = "Space is locked"

                _LOGGER.error("Failed to arm space to night mode: %s", error_msg)
                raise AjaxApiError(f"Failed to activate night mode: {error_msg}")

        except grpc.RpcError as err:
            _LOGGER.error("gRPC error activating night mode: %s", err)
            if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise AjaxAuthError("Session expired") from err
            raise AjaxApiError(f"gRPC error: {err}") from err

    async def close(self) -> None:
        """Close the gRPC channel."""
        if self.channel:
            await self.channel.close()
