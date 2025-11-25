"""Siren device handler for Ajax HomeSiren series.

Handles:
- HomeSiren
- StreetSiren
- StreetSiren DoubleDeck
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


class SirenHandler(AjaxDeviceHandler):
    """Handler for Ajax HomeSiren sirens."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for sirens."""
        sensors = []

        # Note: "armed_in_night_mode" is now a switch, not a binary sensor

        # Tamper / Couvercle
        sensors.append(
            {
                "key": "tamper",
                "translation_key": "tamper",
                "device_class": BinarySensorDeviceClass.TAMPER,
                "icon": "mdi:lock-open-alert",
                "value_fn": lambda: self.device.attributes.get("tampered", False),
                "enabled_by_default": True,
            }
        )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for sirens."""
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

        # Alarm volume level (sirenVolumeLevel from API)
        if "siren_volume_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "alarm_volume_level",
                    "translation_key": "alarm_volume_level",
                    "icon": "mdi:volume-high",
                    "value_fn": lambda: self._format_volume(self.device.attributes.get("siren_volume_level")),
                    "enabled_by_default": True,
                }
            )

        # Beep volume level
        if "beep_volume_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "beep_volume_level",
                    "translation_key": "beep_volume_level",
                    "icon": "mdi:volume-medium",
                    "value_fn": lambda: self._format_volume(self.device.attributes.get("beep_volume_level")),
                    "enabled_by_default": True,
                }
            )

        # Alarm duration
        if "alarm_duration" in self.device.attributes:
            sensors.append(
                {
                    "key": "alarm_duration",
                    "translation_key": "alarm_duration",
                    "icon": "mdi:timer-outline",
                    "value_fn": lambda: self._format_duration(self.device.attributes.get("alarm_duration")),
                    "enabled_by_default": True,
                }
            )

        # Note: LED indication is now a switch (switch.sirene_clignoter_quand_arme)

        return sensors

    def _format_volume(self, volume: str | None) -> str | None:
        """Format volume level to French."""
        if volume is None:
            return None
        volume_map = {
            "OFF": "Désactivé",
            "QUIET": "Silencieux",
            "NORMAL": "Normal",
            "LOUD": "Fort",
            "VERY_LOUD": "Très fort",
        }
        return volume_map.get(volume, volume)

    def _format_duration(self, duration: int | str | None) -> str | None:
        """Format alarm duration to French."""
        if duration is None:
            return None
        # If it's a number (seconds), convert to minutes
        if isinstance(duration, (int, float)):
            minutes = int(duration) // 60
            if minutes == 0:
                return f"{int(duration)} secondes"
            return f"{minutes} minutes"
        # If it's a string like "3_MINUTES", "180_SECONDS", etc.
        duration_map = {
            "1_MINUTE": "1 minute",
            "2_MINUTES": "2 minutes",
            "3_MINUTES": "3 minutes",
            "5_MINUTES": "5 minutes",
            "10_MINUTES": "10 minutes",
            "15_MINUTES": "15 minutes",
            "CONTINUOUS": "Continue",
        }
        return duration_map.get(str(duration), str(duration))

    def get_switches(self) -> list[dict]:
        """Return switch entities for sirens."""
        switches = []

        # Night Mode switch
        switches.append(
            {
                "key": "night_mode",
                "translation_key": "night_mode",
                "name": "Armé en mode nuit",
                "icon": "mdi:weather-night",
                "value_fn": lambda: self.device.attributes.get("night_mode_arm", False),
                "api_key": "nightModeArm",
                "enabled_by_default": True,
            }
        )

        # Beep on arm/disarm
        switches.append(
            {
                "key": "beep_on_arm",
                "translation_key": "beep_on_arm",
                "name": "Bip lors armement/désarmement",
                "icon": "mdi:volume-high",
                "value_fn": lambda: self.device.attributes.get("beep_on_arm_disarm", False),
                "api_key": "beepOnArmDisarm",
                "enabled_by_default": True,
            }
        )

        # Beep on delay
        switches.append(
            {
                "key": "beep_on_delay",
                "translation_key": "beep_on_delay",
                "name": "Bip pendant délai",
                "icon": "mdi:timer-sand",
                "value_fn": lambda: self.device.attributes.get("beep_on_delay", False),
                "api_key": "beepOnDelay",
                "enabled_by_default": True,
            }
        )

        # Blink while armed (LED)
        switches.append(
            {
                "key": "blink_while_armed",
                "translation_key": "blink_while_armed",
                "name": "Clignoter quand armé",
                "icon": "mdi:led-on",
                "value_fn": lambda: self._get_blink_state(),
                "api_key": "v2sirenIndicatorLightMode",
                "api_value_on": "BLINK_WHILE_ARMED",
                "api_value_off": "DISABLED",
                "api_extra": {"blinkWhileArmed": True},
                "api_extra_off": {"blinkWhileArmed": False},
                "enabled_by_default": True,
            }
        )

        # Chimes enabled
        switches.append(
            {
                "key": "chimes",
                "translation_key": "chimes",
                "name": "Carillons",
                "icon": "mdi:bell-ring",
                "value_fn": lambda: self.device.attributes.get("chimes_enabled", False),
                "api_key": "chimesEnabled",
                "enabled_by_default": True,
            }
        )

        return switches

    def _get_blink_state(self) -> bool:
        """Get the blink while armed state."""
        led = self.device.attributes.get("led_indication")
        if isinstance(led, bool):
            return led
        if isinstance(led, str):
            return led == "BLINK_WHILE_ARMED"
        return self.device.attributes.get("blink_while_armed", False)
