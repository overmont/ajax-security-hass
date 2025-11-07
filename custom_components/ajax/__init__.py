"""The Ajax Security System integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform, CONF_EMAIL, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady

from .const import DOMAIN, CONF_DEVICE_ID
from .api import AjaxApi, AjaxApiError, AjaxAuthError
from .coordinator import AjaxDataCoordinator

_LOGGER = logging.getLogger(__name__)

# Define platforms
PLATFORMS: list[Platform] = [
    Platform.ALARM_CONTROL_PANEL,
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ajax from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Create API client
    api = AjaxApi(
        email=entry.data[CONF_EMAIL],
        password=entry.data[CONF_PASSWORD],
        device_id=entry.data.get(CONF_DEVICE_ID, "homeassistant"),
    )

    # Authenticate
    try:
        await api.async_login()
    except AjaxAuthError as err:
        raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
    except AjaxApiError as err:
        raise ConfigEntryNotReady(f"Failed to connect to Ajax API: {err}") from err

    # Create coordinator
    coordinator = AjaxDataCoordinator(hass, api)

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Forward setup to platforms
    if PLATFORMS:
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    _LOGGER.info(
        "Ajax integration loaded successfully for %s with %d spaces",
        coordinator.account.name if coordinator.account else "Unknown",
        len(coordinator.account.spaces) if coordinator.account else 0,
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if PLATFORMS:
        unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    else:
        unload_ok = True

    if unload_ok:
        coordinator: AjaxDataCoordinator = hass.data[DOMAIN].pop(entry.entry_id)
        await coordinator.async_shutdown()

    return unload_ok
