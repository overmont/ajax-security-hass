"""Door/Window contact sensor handler for Ajax DoorProtect series.

Handles:
- DoorProtect
- DoorProtect Plus (with tilt sensor and temperature)
- Wired input modules with door contacts
"""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    UnitOfTemperature,
)

from .base import AjaxDeviceHandler


class DoorContactHandler(AjaxDeviceHandler):
    """Handler for Ajax DoorProtect door/window contact sensors."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for door contacts."""
        sensors = []

        # Main door sensor
        if "door_opened" in self.device.attributes:
            sensors.append(
                {
                    "key": "door",
                    "translation_key": "door",
                    "device_class": BinarySensorDeviceClass.DOOR,
                    "value_fn": lambda: self.device.attributes.get("door_opened", False),
                    "enabled_by_default": True,
                }
            )

        # External contact (for connecting wired sensors)
        if "external_contact_opened" in self.device.attributes:
            sensors.append(
                {
                    "key": "external_contact",
                    "translation_key": "external_contact",
                    "device_class": BinarySensorDeviceClass.DOOR,
                    "value_fn": lambda: self.device.attributes.get("external_contact_opened", False),
                    "enabled_by_default": True,
                }
            )

        # Always active mode
        sensors.append(
            {
                "key": "always_active",
                "translation_key": "always_active",
                "icon": "mdi:moon-waning-crescent",
                "value_fn": lambda: self.device.attributes.get("always_active", False),
                "enabled_by_default": True,
            }
        )

        # Armed in night mode
        sensors.append(
            {
                "key": "armed_in_night_mode",
                "translation_key": "armed_in_night_mode",
                "icon": "mdi:shield-moon",
                "value_fn": lambda: self.device.attributes.get("armed_in_night_mode", False),
                "enabled_by_default": True,
            }
        )

        # Problem detection
        sensors.append(
            {
                "key": "problem",
                "translation_key": "problem",
                "device_class": BinarySensorDeviceClass.PROBLEM,
                "value_fn": lambda: bool(self.device.malfunctions),
                "enabled_by_default": True,
            }
        )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for door contacts."""
        sensors = []

        # Battery level
        if "battery_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "battery",
                    "translation_key": "battery",
                    "device_class": SensorDeviceClass.BATTERY,
                    "native_unit_of_measurement": PERCENTAGE,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "value_fn": lambda: self.device.attributes.get("battery_level"),
                    "enabled_by_default": True,
                }
            )

        # Signal strength
        if "signal_strength" in self.device.attributes:
            sensors.append(
                {
                    "key": "signal_strength",
                    "translation_key": "signal_strength",
                    "device_class": SensorDeviceClass.SIGNAL_STRENGTH,
                    "native_unit_of_measurement": SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "value_fn": lambda: self.device.attributes.get("signal_strength"),
                    "enabled_by_default": True,
                }
            )

        # Temperature (DoorProtect Plus)
        if "temperature" in self.device.attributes:
            sensors.append(
                {
                    "key": "temperature",
                    "translation_key": "temperature",
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "native_unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "value_fn": lambda: self.device.attributes.get("temperature"),
                    "enabled_by_default": True,
                }
            )

        # Malfunctions
        if self.device.malfunctions:
            sensors.append(
                {
                    "key": "malfunctions",
                    "translation_key": "malfunctions",
                    "icon": "mdi:alert-circle",
                    "value_fn": lambda: ", ".join(self.device.malfunctions) if self.device.malfunctions else "None",
                    "enabled_by_default": True,
                }
            )

        # Firmware version
        if "firmware_version" in self.device.attributes:
            sensors.append(
                {
                    "key": "firmware_version",
                    "translation_key": "firmware_version",
                    "icon": "mdi:chip",
                    "value_fn": lambda: self.device.attributes.get("firmware_version"),
                    "enabled_by_default": False,
                }
            )

        return sensors
