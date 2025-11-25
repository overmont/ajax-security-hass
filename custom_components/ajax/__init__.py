"""The Ajax Security System integration."""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv

from .api import AjaxRestApi, AjaxRestApiError, AjaxRestAuthError
from .const import (
    CONF_API_KEY,
    CONF_AWS_ACCESS_KEY_ID,
    CONF_AWS_SECRET_ACCESS_KEY,
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_QUEUE_NAME,
    DOMAIN,
)
from .coordinator import AjaxDataCoordinator

if TYPE_CHECKING:
    from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

# Service names
SERVICE_FORCE_ARM = "force_arm"
SERVICE_FORCE_ARM_NIGHT = "force_arm_night"
SERVICE_GENERATE_DEVICE_INFO = "generate_device_info"

PLATFORMS: list[Platform] = [
    Platform.ALARM_CONTROL_PANEL,
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.DEVICE_TRACKER,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Ajax Security System component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ajax Security System from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Get API credentials
    api_key = entry.data[CONF_API_KEY]
    email = entry.data[CONF_EMAIL]
    password_hash = entry.data[CONF_PASSWORD]  # Already hashed in config_flow

    # Get optional AWS SQS credentials (for real-time events)
    aws_access_key_id = entry.data.get(CONF_AWS_ACCESS_KEY_ID)
    aws_secret_access_key = entry.data.get(CONF_AWS_SECRET_ACCESS_KEY)
    queue_name = entry.data.get(CONF_QUEUE_NAME)

    # Create REST API instance
    # password_is_hashed=True because we store only SHA256 hash, never plain password
    api = AjaxRestApi(
        api_key=api_key,
        email=email,
        password=password_hash,
        password_is_hashed=True,  # Password is already SHA256 hash
    )

    try:
        # Login to get temporary token
        await api.async_login()
        _LOGGER.info("Successfully logged in to Ajax REST API")

        # Test API connection by getting hubs
        await api.async_get_hubs()
        _LOGGER.info("Successfully connected to Ajax REST API")

    except AjaxRestAuthError as err:
        _LOGGER.error("Authentication failed: %s", err)
        return False
    except AjaxRestApiError as err:
        _LOGGER.error("API error during setup: %s", err)
        raise ConfigEntryNotReady from err

    # Create coordinator
    # - REST polling: Baseline updates every 30s
    # - AWS SQS: Optional real-time events (if credentials provided)
    coordinator = AjaxDataCoordinator(
        hass,
        api,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        queue_name=queue_name,
    )

    # Store coordinator
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Set up platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register services
    await _async_setup_services(hass, coordinator)

    return True


async def _async_setup_services(
    hass: HomeAssistant, coordinator: AjaxDataCoordinator
) -> None:
    """Set up Ajax services."""

    async def handle_force_arm(call: ServiceCall) -> None:
        """Handle force arm service call."""
        entity_id = call.data.get("entity_id")
        _LOGGER.info("Force arming via service call (entity: %s)", entity_id)

        # Get the first hub from coordinator
        if coordinator.account and coordinator.account.spaces:
            for hub_id in coordinator.account.spaces:
                try:
                    await coordinator.api.async_arm(hub_id, ignore_problems=True)
                    await coordinator.async_request_refresh()
                    _LOGGER.info("Force armed hub %s", hub_id)
                except Exception as err:
                    _LOGGER.error("Failed to force arm hub %s: %s", hub_id, err)

    async def handle_force_arm_night(call: ServiceCall) -> None:
        """Handle force arm night mode service call."""
        entity_id = call.data.get("entity_id")
        _LOGGER.info("Force arming night mode via service call (entity: %s)", entity_id)

        if coordinator.account and coordinator.account.spaces:
            for hub_id in coordinator.account.spaces:
                try:
                    await coordinator.api.async_night_mode(hub_id, enabled=True)
                    await coordinator.async_request_refresh()
                    _LOGGER.info("Force armed night mode hub %s", hub_id)
                except Exception as err:
                    _LOGGER.error("Failed to force arm night mode hub %s: %s", hub_id, err)

    async def handle_generate_device_info(call: ServiceCall) -> None:
        """Handle generate device info service call."""
        _LOGGER.info("Generating device info report")

        device_info: dict[str, Any] = {
            "integration_version": "1.0.0",
            "device_types": {},
            "device_count": 0,
        }

        if coordinator.account:
            for space_id, space in coordinator.account.spaces.items():
                for device_id, device in space.devices.items():
                    device_type = device.device_type
                    if device_type not in device_info["device_types"]:
                        device_info["device_types"][device_type] = {
                            "count": 0,
                            "attributes": set(),
                            "firmware_versions": set(),
                        }

                    type_info = device_info["device_types"][device_type]
                    type_info["count"] += 1
                    type_info["attributes"].update(device.attributes.keys())

                    if "firmware_version" in device.attributes:
                        type_info["firmware_versions"].add(
                            device.attributes["firmware_version"]
                        )

                    device_info["device_count"] += 1

        # Convert sets to lists for JSON serialization
        for type_info in device_info["device_types"].values():
            type_info["attributes"] = sorted(type_info["attributes"])
            type_info["firmware_versions"] = sorted(type_info["firmware_versions"])

        # Write to file
        output_path = Path(hass.config.path("ajax_device_info.json"))
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(device_info, f, indent=2, default=str)

        _LOGGER.info("Device info written to %s", output_path)

        # Create persistent notification
        from homeassistant.components.persistent_notification import async_create

        async_create(
            hass,
            f"Device info report generated: {output_path}",
            title="Ajax Device Info",
            notification_id="ajax_device_info",
        )

    # Register services if not already registered
    if not hass.services.has_service(DOMAIN, SERVICE_FORCE_ARM):
        hass.services.async_register(
            DOMAIN,
            SERVICE_FORCE_ARM,
            handle_force_arm,
            schema=vol.Schema(
                {vol.Optional("entity_id"): cv.entity_ids}
            ),
        )

    if not hass.services.has_service(DOMAIN, SERVICE_FORCE_ARM_NIGHT):
        hass.services.async_register(
            DOMAIN,
            SERVICE_FORCE_ARM_NIGHT,
            handle_force_arm_night,
            schema=vol.Schema(
                {vol.Optional("entity_id"): cv.entity_ids}
            ),
        )

    if not hass.services.has_service(DOMAIN, SERVICE_GENERATE_DEVICE_INFO):
        hass.services.async_register(
            DOMAIN,
            SERVICE_GENERATE_DEVICE_INFO,
            handle_generate_device_info,
        )


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(
        entry, PLATFORMS
    ):
        coordinator: AjaxDataCoordinator = hass.data[DOMAIN].pop(entry.entry_id)

        # Shutdown coordinator (closes SQS manager, API connection, and all tasks)
        await coordinator.async_shutdown()

    return unload_ok
