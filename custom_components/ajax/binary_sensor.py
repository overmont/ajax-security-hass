"""Ajax binary sensor platform.

This module creates binary sensors for Ajax security devices:
- Motion detectors
- Door/window contacts
- Smoke detectors
- Flood detectors
- Glass break detectors
- System problems (malfunctions)
"""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import AjaxDataCoordinator
from .models import DeviceType

_LOGGER = logging.getLogger(__name__)

# Mapping from Ajax DeviceType to BinarySensorDeviceClass
DEVICE_TYPE_MAP = {
    DeviceType.MOTION_DETECTOR: BinarySensorDeviceClass.MOTION,
    DeviceType.DOOR_CONTACT: BinarySensorDeviceClass.DOOR,
    DeviceType.SMOKE_DETECTOR: BinarySensorDeviceClass.SMOKE,
    DeviceType.FLOOD_DETECTOR: BinarySensorDeviceClass.MOISTURE,
    DeviceType.GLASS_BREAK: BinarySensorDeviceClass.VIBRATION,
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Ajax binary sensors from a config entry."""
    coordinator: AjaxDataCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[BinarySensorEntity] = []

    if not coordinator.account:
        _LOGGER.warning("No Ajax account found, no binary sensors created")
        return

    # Create space-level binary sensors (system problems)
    for space_id, space in coordinator.account.spaces.items():
        # Add "System Problems" binary sensor for the space
        entities.append(
            AjaxSystemProblemsSensor(coordinator, entry, space_id)
        )
        _LOGGER.debug("Created system problems sensor for space '%s'", space.name)
        _LOGGER.debug("Space '%s' has %d devices with malfunctions",
                     space.name, len(space.get_devices_with_malfunctions()))

    # Create device-level binary sensors for each supported device
    for space_id, space in coordinator.account.spaces.items():
        for device_id, device in space.devices.items():
            # For Hubs, create tamper and power binary sensors
            if device.type == DeviceType.HUB:
                # Tamper sensor (cover open/closed)
                if "tampered" in device.attributes:
                    entities.append(
                        AjaxHubTamperSensor(coordinator, entry, space_id, device_id)
                    )
                    _LOGGER.debug("Created tamper sensor for Hub '%s'", device.name)

                # External power sensor
                if "externally_powered" in device.attributes:
                    entities.append(
                        AjaxHubPowerSensor(coordinator, entry, space_id, device_id)
                    )
                    _LOGGER.debug("Created power sensor for Hub '%s'", device.name)

                continue  # Don't create regular binary sensor for hubs

            # Skip if device type not supported as binary sensor
            if device.type not in DEVICE_TYPE_MAP:
                _LOGGER.debug(
                    "Skipping device '%s' (type: %s) - not a binary sensor",
                    device.name,
                    device.type.value,
                )
                continue

            entities.append(
                AjaxDeviceBinarySensor(coordinator, entry, space_id, device_id)
            )
            _LOGGER.debug(
                "Created binary sensor for device '%s' (type: %s)",
                device.name,
                device.type.value,
            )

    if entities:
        async_add_entities(entities)
        _LOGGER.info("Added %d Ajax binary sensor(s)", len(entities))
    else:
        _LOGGER.info("No Ajax binary sensors to create")


# ==============================================================================
# Space-level Binary Sensors
# ==============================================================================


class AjaxSystemProblemsSensor(CoordinatorEntity[AjaxDataCoordinator], BinarySensorEntity):
    """Binary sensor indicating if there are system problems (malfunctions)."""

    _attr_device_class = BinarySensorDeviceClass.PROBLEM

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
    ) -> None:
        """Initialize the system problems sensor."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._entry = entry

        # Get initial space data
        space = coordinator.get_space(space_id)
        space_name = space.name if space else "Unknown"

        # Set entity attributes - use translation_key
        self._attr_has_entity_name = True
        self._attr_translation_key = "system_problems"
        self._attr_unique_id = f"{entry.entry_id}_{space_id}_problems"
        self._attr_icon = "mdi:alert-circle"

    @property
    def is_on(self) -> bool:
        """Return true if there are problems."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return False

        # Check if any device has malfunctions
        devices_with_problems = space.get_devices_with_malfunctions()
        return len(devices_with_problems) > 0

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        devices_with_problems = space.get_devices_with_malfunctions()

        attributes = {
            "space_id": space.id,
            "space_name": space.name,
            "total_malfunctions": sum(d.malfunctions for d in devices_with_problems),
            "devices_with_problems": len(devices_with_problems),
        }

        # List devices with problems with detailed analysis
        if devices_with_problems:
            problem_details = []
            for device in devices_with_problems:
                device_info = {
                    "device_id": device.id,
                    "device_name": device.name,
                    "device_type": device.type.value,
                    "malfunctions_count": device.malfunctions,
                    "online": device.online,
                    "bypassed": device.bypassed,
                    "room_name": self.coordinator.get_room(self._space_id, device.room_id).name
                    if device.room_id and self.coordinator.get_room(self._space_id, device.room_id)
                    else None,
                }

                # Add specific problem indicators as structured data
                problems_detected = []

                # Check SIM status for hubs
                if device.type.value == "hub" and "sim_status" in device.attributes:
                    sim_status = device.attributes.get("sim_status", "")
                    sim_slots_used = device.attributes.get("sim_slots_used", 0)
                    sim_slots_total = device.attributes.get("sim_slots_total", 0)
                    if sim_slots_used < sim_slots_total:
                        problems_detected.append({
                            "type": "sim_missing",
                            "status": sim_status,
                            "slots_used": sim_slots_used,
                            "slots_total": sim_slots_total,
                        })

                # Check battery
                if device.is_low_battery:
                    problems_detected.append({
                        "type": "low_battery",
                        "level": device.battery_level,
                    })

                # Check signal
                if device.signal_strength is not None and device.signal_strength < 30:
                    problems_detected.append({
                        "type": "weak_signal",
                        "strength": device.signal_strength,
                    })

                # Check offline status
                if not device.online:
                    problems_detected.append({"type": "offline"})

                # If we detected specific problems, add them
                if problems_detected:
                    device_info["problems"] = problems_detected
                else:
                    # If no specific problem detected but malfunctions reported
                    device_info["problems"] = [{"type": "unknown", "count": device.malfunctions}]

                problem_details.append(device_info)

            attributes["problem_devices"] = problem_details

        return attributes

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        return {
            "identifiers": {(DOMAIN, self._space_id)},
            "name": f"Ajax Hub - {space.name}",
            "manufacturer": "Ajax Systems",
            "model": "Security Hub",
        }


# ==============================================================================
# Device-level Binary Sensors
# ==============================================================================


class AjaxDeviceBinarySensor(CoordinatorEntity[AjaxDataCoordinator], BinarySensorEntity):
    """Representation of an Ajax device binary sensor (motion, door, smoke, etc.)."""

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id
        self._entry = entry

        # Get initial device data
        device = coordinator.get_device(space_id, device_id)
        if not device:
            _LOGGER.error("Device %s not found in space %s", device_id, space_id)
            return

        # Set device class based on device type
        if device.type in DEVICE_TYPE_MAP:
            self._attr_device_class = DEVICE_TYPE_MAP[device.type]
        else:
            self._attr_device_class = None

        # Set entity attributes - device name is used as-is
        # Binary sensors for devices don't need translation_key since they represent physical devices
        self._attr_name = f"{device.name}"
        self._attr_unique_id = f"{entry.entry_id}_{device_id}_binary"

    @property
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return None

        # Check device states for triggers
        # Ajax devices report states like "ACTIVATED", "TRIGGERED", etc.
        for state in device.states:
            state_lower = str(state).lower()
            if any(
                keyword in state_lower
                for keyword in ["activated", "triggered", "detected", "open", "alarm"]
            ):
                return True

        return False

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return False

        # Binary sensor is unavailable if device is offline
        return device.online

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        attributes = {
            "device_id": device.id,
            "device_type": device.type.value,
            "space_id": device.space_id,
            "hub_id": device.hub_id,
            "online": device.online,
            "bypassed": device.bypassed,
            "malfunctions": device.malfunctions,
            "states": device.states,
        }

        # Add room information if available
        if device.room_id:
            room = self.coordinator.get_room(self._space_id, device.room_id)
            if room:
                attributes["room_id"] = room.id
                attributes["room_name"] = room.name

        # Add battery info if available
        if device.has_battery:
            attributes["battery_level"] = device.battery_level
            attributes["battery_state"] = device.battery_state
            attributes["is_low_battery"] = device.is_low_battery

        # Add signal strength if available
        if device.signal_strength is not None:
            attributes["signal_strength"] = device.signal_strength

        return attributes

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": f"Ajax {device.name}",
            "manufacturer": "Ajax Systems",
            "model": device.type.value.replace("_", " ").title(),
            "via_device": (DOMAIN, self._space_id),
            "sw_version": device.firmware_version,
            "hw_version": device.hardware_version,
        }


# ==============================================================================
# Hub-specific Binary Sensors
# ==============================================================================


class AjaxHubTamperSensor(CoordinatorEntity[AjaxDataCoordinator], BinarySensorEntity):
    """Binary sensor for Hub tamper status (cover open/closed)."""

    _attr_device_class = BinarySensorDeviceClass.TAMPER

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the tamper sensor."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id
        self._entry = entry

        # Set entity attributes - use translation_key
        self._attr_has_entity_name = True
        self._attr_translation_key = "tamper"
        self._attr_unique_id = f"{entry.entry_id}_{device_id}_tamper"
        self._attr_icon = "mdi:shield-alert"
        self._attr_entity_category = "diagnostic"

    @property
    def is_on(self) -> bool | None:
        """Return true if tampered (cover opened)."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return None

        return device.attributes.get("tampered", False)

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._space_id, self._device_id)
        return device is not None and device.online

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": f"Ajax {device.name}",
            "manufacturer": "Ajax Systems",
            "model": device.type.value.replace("_", " ").title(),
            "via_device": (DOMAIN, self._space_id),
            "sw_version": device.firmware_version,
            "hw_version": device.hardware_version,
        }


class AjaxHubPowerSensor(CoordinatorEntity[AjaxDataCoordinator], BinarySensorEntity):
    """Binary sensor for Hub external power status."""

    _attr_device_class = BinarySensorDeviceClass.PLUG

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the power sensor."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id
        self._entry = entry

        # Set entity attributes - use translation_key
        self._attr_has_entity_name = True
        self._attr_translation_key = "external_power"
        self._attr_unique_id = f"{entry.entry_id}_{device_id}_external_power"
        self._attr_icon = "mdi:power-plug"
        self._attr_entity_category = "diagnostic"

    @property
    def is_on(self) -> bool | None:
        """Return true if externally powered."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return None

        return device.attributes.get("externally_powered", False)

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._space_id, self._device_id)
        return device is not None and device.online

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": f"Ajax {device.name}",
            "manufacturer": "Ajax Systems",
            "model": device.type.value.replace("_", " ").title(),
            "via_device": (DOMAIN, self._space_id),
            "sw_version": device.firmware_version,
            "hw_version": device.hardware_version,
        }
