"""Config flow for Ajax integration."""
from __future__ import annotations

import hashlib
import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv

from .api import AjaxRestApi, AjaxRestApiError, AjaxRestAuthError, AjaxRest2FARequiredError
from .const import (
    CONF_API_KEY,
    CONF_AWS_ACCESS_KEY_ID,
    CONF_AWS_SECRET_ACCESS_KEY,
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_QUEUE_NAME,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


class AjaxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Ajax Security Systems."""

    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self._api: AjaxRestApi | None = None
        self._user_input: dict[str, Any] = {}
        self._request_id: str | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step - API credentials."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Store user input for potential 2FA step
            self._user_input = user_input

            # Validate API credentials
            try:
                self._api = AjaxRestApi(
                    api_key=user_input[CONF_API_KEY],
                    email=user_input[CONF_EMAIL],
                    password=user_input[CONF_PASSWORD],
                )

                # Test API connection by logging in
                await self._api.async_login()

                # If login successful, try to get hubs to verify access
                await self._api.async_get_hubs()
                await self._api.close()

                # Hash password for secure storage (never store plain password!)
                password_hash = hashlib.sha256(
                    user_input[CONF_PASSWORD].encode()
                ).hexdigest()

                # Prepare entry data
                entry_data = {
                    CONF_API_KEY: user_input[CONF_API_KEY],
                    CONF_EMAIL: user_input[CONF_EMAIL],
                    CONF_PASSWORD: password_hash,  # Store ONLY the hash
                }

                # Add optional AWS SQS credentials if provided
                if user_input.get(CONF_AWS_ACCESS_KEY_ID):
                    entry_data[CONF_AWS_ACCESS_KEY_ID] = user_input[CONF_AWS_ACCESS_KEY_ID]
                if user_input.get(CONF_AWS_SECRET_ACCESS_KEY):
                    entry_data[CONF_AWS_SECRET_ACCESS_KEY] = user_input[CONF_AWS_SECRET_ACCESS_KEY]
                if user_input.get(CONF_QUEUE_NAME):
                    entry_data[CONF_QUEUE_NAME] = user_input[CONF_QUEUE_NAME]

                # Create entry
                return self.async_create_entry(
                    title=f"Ajax - {user_input[CONF_EMAIL]}",
                    data=entry_data,
                )

            except AjaxRest2FARequiredError as err:
                # 2FA is required, store request_id and show 2FA form
                _LOGGER.info("2FA required for login")
                self._request_id = err.request_id
                return await self.async_step_2fa()

            except AjaxRestAuthError:
                _LOGGER.error("Invalid API credentials")
                errors["base"] = "invalid_auth"
            except AjaxRestApiError as err:
                _LOGGER.error("Cannot connect to Ajax API: %s", err)
                errors["base"] = "cannot_connect"
            except Exception as err:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception: %s", err)
                errors["base"] = "unknown"

        # Show configuration form
        data_schema = vol.Schema(
            {
                vol.Required(CONF_API_KEY): str,
                vol.Required(CONF_EMAIL): str,
                vol.Required(CONF_PASSWORD): str,
                # AWS SQS credentials (optional - for real-time events)
                vol.Optional(CONF_AWS_ACCESS_KEY_ID): str,
                vol.Optional(CONF_AWS_SECRET_ACCESS_KEY): str,
                vol.Optional(CONF_QUEUE_NAME): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    async def async_step_2fa(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle 2FA verification step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            code = user_input.get("code", "").strip()

            try:
                # Verify 2FA code
                await self._api.async_verify_2fa(self._request_id, code)

                # 2FA successful, verify access
                await self._api.async_get_hubs()
                await self._api.close()

                # Hash password for secure storage (never store plain password!)
                password_hash = hashlib.sha256(
                    self._user_input[CONF_PASSWORD].encode()
                ).hexdigest()

                # Prepare entry data
                entry_data = {
                    CONF_API_KEY: self._user_input[CONF_API_KEY],
                    CONF_EMAIL: self._user_input[CONF_EMAIL],
                    CONF_PASSWORD: password_hash,  # Store ONLY the hash
                }

                # Add optional AWS SQS credentials if provided
                if self._user_input.get(CONF_AWS_ACCESS_KEY_ID):
                    entry_data[CONF_AWS_ACCESS_KEY_ID] = self._user_input[CONF_AWS_ACCESS_KEY_ID]
                if self._user_input.get(CONF_AWS_SECRET_ACCESS_KEY):
                    entry_data[CONF_AWS_SECRET_ACCESS_KEY] = self._user_input[CONF_AWS_SECRET_ACCESS_KEY]
                if self._user_input.get(CONF_QUEUE_NAME):
                    entry_data[CONF_QUEUE_NAME] = self._user_input[CONF_QUEUE_NAME]

                # Create entry
                return self.async_create_entry(
                    title=f"Ajax - {self._user_input[CONF_EMAIL]}",
                    data=entry_data,
                )

            except AjaxRestAuthError:
                _LOGGER.error("Invalid 2FA code")
                errors["base"] = "invalid_2fa"
            except AjaxRestApiError as err:
                _LOGGER.error("2FA verification failed: %s", err)
                errors["base"] = "cannot_connect"
            except Exception as err:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception during 2FA: %s", err)
                errors["base"] = "unknown"

        # Show 2FA form
        data_schema = vol.Schema(
            {
                vol.Required("code"): str,
            }
        )

        return self.async_show_form(
            step_id="2fa",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                "email": self._user_input.get(CONF_EMAIL, ""),
            },
        )
