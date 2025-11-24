"""Motion detector device handler for Ajax MotionProtect series.

Handles:
- MotionProtect
- MotionProtect Plus (with microwave sensor)
- MotionProtect Outdoor (with dual motion detection)
- CombiProtect (motion + glass break)
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


class MotionDetectorHandler(AjaxDeviceHandler):
    """Handler for Ajax MotionProtect motion detectors."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for motion detectors."""
        sensors = [
            {
                "key": "motion",
                "translation_key": "motion",
                "device_class": BinarySensorDeviceClass.MOTION,
                "value_fn": lambda: self.device.attributes.get("motion_detected", False),
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

        # CombiProtect also has glass break detection
        if "glass_break_detected" in self.device.attributes:
            sensors.append(
                {
                    "key": "glass_break",
                    "translation_key": "glass_break",
                    "device_class": BinarySensorDeviceClass.VIBRATION,
                    "value_fn": lambda: self.device.attributes.get("glass_break_detected", False),
                    "enabled_by_default": True,
                }
            )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for motion detectors."""
        sensors = []

        # Battery level (all MotionProtect devices are battery-powered)
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

        # Signal strength (Jeweller radio)
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

        # Temperature (MotionProtect Plus has temperature sensor)
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

        # Malfunctions list
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

        # Noise level (MotionProtect Plus with microwave sensor)
        if "noise_level_avg" in self.device.attributes:
            sensors.append(
                {
                    "key": "noise_level_avg",
                    "translation_key": "noise_level_avg",
                    "icon": "mdi:waveform",
                    "value_fn": lambda: self.device.attributes.get("noise_level_avg"),
                    "enabled_by_default": False,
                }
            )

        return sensors
