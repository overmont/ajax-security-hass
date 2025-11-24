"""Smoke detector handler for Ajax FireProtect series.

Handles:
- FireProtect (smoke detector)
- FireProtect Plus (smoke + CO + temperature)
- FireProtect 2 (smoke + CO + temperature + SirenControl)
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


class SmokeDetectorHandler(AjaxDeviceHandler):
    """Handler for Ajax FireProtect smoke detectors."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for smoke detectors."""
        sensors = [
            {
                "key": "smoke",
                "translation_key": "smoke",
                "device_class": BinarySensorDeviceClass.SMOKE,
                "value_fn": lambda: self.device.attributes.get("smoke_detected", False),
                "enabled_by_default": True,
            },
            {
                "key": "always_active",
                "translation_key": "always_active",
                "icon": "mdi:moon-waning-crescent",
                "value_fn": lambda: self.device.attributes.get("always_active", False),
                "enabled_by_default": True,
            },
            {
                "key": "armed_in_night_mode",
                "translation_key": "armed_in_night_mode",
                "icon": "mdi:shield-moon",
                "value_fn": lambda: self.device.attributes.get("armed_in_night_mode", False),
                "enabled_by_default": True,
            },
            {
                "key": "problem",
                "translation_key": "problem",
                "device_class": BinarySensorDeviceClass.PROBLEM,
                "value_fn": lambda: bool(self.device.malfunctions),
                "enabled_by_default": True,
            },
        ]

        # CO detector (FireProtect Plus, FireProtect 2)
        if "co_detected" in self.device.attributes:
            sensors.append(
                {
                    "key": "gas",
                    "translation_key": "gas",
                    "device_class": BinarySensorDeviceClass.GAS,
                    "value_fn": lambda: self.device.attributes.get("co_detected", False),
                    "enabled_by_default": True,
                }
            )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for smoke detectors."""
        sensors = []

        # Battery level (for battery-powered models)
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

        # Temperature (FireProtect Plus, FireProtect 2)
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

        # CO level (FireProtect Plus, FireProtect 2)
        if "co_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "co_level",
                    "translation_key": "co_level",
                    "device_class": SensorDeviceClass.CO,
                    "native_unit_of_measurement": "ppm",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "value_fn": lambda: self.device.attributes.get("co_level"),
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
