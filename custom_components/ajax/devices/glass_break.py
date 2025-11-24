"""Glass break detector handler for Ajax GlassProtect series.

Handles:
- GlassProtect
"""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfTemperature,
)

from .base import AjaxDeviceHandler


class GlassBreakHandler(AjaxDeviceHandler):
    """Handler for Ajax GlassProtect glass break detectors."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for glass break detectors."""
        sensors = []

        # Main glass break sensor
        sensors.append(
            {
                "key": "glass_break",
                "translation_key": "glass_break",
                "device_class": BinarySensorDeviceClass.SAFETY,
                "icon": "mdi:glass-fragile",
                "value_fn": lambda: self.device.attributes.get("glass_break_detected", False),
                "enabled_by_default": True,
            }
        )

        # External contact (for connecting wired sensors)
        # Only create if extraContactAware is True (feature enabled on device)
        if self.device.attributes.get("extra_contact_aware", False):
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

        # Tamper / Couvercle
        sensors.append(
            {
                "key": "tamper",
                "translation_key": "tamper",
                "device_class": BinarySensorDeviceClass.TAMPER,
                "value_fn": lambda: self.device.attributes.get("tampered", False),
                "enabled_by_default": True,
            }
        )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for glass break detectors."""
        sensors = []

        # Battery level
        sensors.append(
            {
                "key": "battery",
                "translation_key": "battery",
                "device_class": SensorDeviceClass.BATTERY,
                "native_unit_of_measurement": PERCENTAGE,
                "state_class": SensorStateClass.MEASUREMENT,
                "value_fn": lambda: self.device.battery_level if self.device.battery_level is not None else None,
                "enabled_by_default": True,
            }
        )

        # Signal strength
        sensors.append(
            {
                "key": "signal_strength",
                "translation_key": "signal_strength",
                "icon": "mdi:signal",
                "native_unit_of_measurement": PERCENTAGE,
                "state_class": SensorStateClass.MEASUREMENT,
                "value_fn": lambda: self.device.signal_strength if self.device.signal_strength is not None else None,
                "enabled_by_default": True,
            }
        )

        # Temperature
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

        # Sensitivity
        if "sensitivity" in self.device.attributes:
            sensors.append(
                {
                    "key": "sensitivity",
                    "translation_key": "sensitivity",
                    "icon": "mdi:tune",
                    "value_fn": lambda: self.device.attributes.get("sensitivity"),
                    "enabled_by_default": True,
                }
            )

        return sensors
