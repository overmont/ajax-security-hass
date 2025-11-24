"""Relay handler for Ajax Relay devices.

Handles:
- Relay (relay module for gates, garage doors, locks)
- WallSwitch (in relay mode)

Features:
- ON/OFF control
- Pulse mode (temporary activation for gates/doors)
- Power monitoring
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
    UnitOfTime,
)

from .base import AjaxDeviceHandler


class RelayHandler(AjaxDeviceHandler):
    """Handler for Ajax Relay devices."""

    def get_switches(self) -> list[dict]:
        """Return switch entities for relay control."""
        return [
            {
                "key": "relay",
                "translation_key": "relay",
                "value_fn": lambda: self.device.attributes.get("state") == "on",
                "turn_on_fn": self._async_turn_on,
                "turn_off_fn": self._async_turn_off,
                "icon": "mdi:electric-switch",
                "enabled_by_default": True,
            }
        ]

    def get_buttons(self) -> list[dict]:
        """Return button entities for relay control."""
        buttons = [
            {
                "key": "pulse",
                "translation_key": "pulse",
                "press_fn": self._async_pulse,
                "icon": "mdi:gesture-tap-button",
                "enabled_by_default": True,
            }
        ]
        return buttons

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for relay."""
        sensors = [
            {
                "key": "problem",
                "translation_key": "problem",
                "device_class": BinarySensorDeviceClass.PROBLEM,
                "value_fn": lambda: bool(self.device.malfunctions),
                "enabled_by_default": True,
            }
        ]

        # Connection status
        sensors.append(
            {
                "key": "connection",
                "translation_key": "connection",
                "device_class": BinarySensorDeviceClass.CONNECTIVITY,
                "value_fn": lambda: self.device.online,
                "enabled_by_default": True,
            }
        )

        # External power status (if available)
        if "external_power" in self.device.attributes:
            sensors.append(
                {
                    "key": "external_power",
                    "translation_key": "external_power",
                    "device_class": BinarySensorDeviceClass.POWER,
                    "value_fn": lambda: self.device.attributes.get("external_power", False),
                    "enabled_by_default": True,
                }
            )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for relay monitoring."""
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
                    "icon": "mdi:wifi",
                    "enabled_by_default": False,
                }
            )

        # Pulse duration (configuration)
        if "pulse_duration" in self.device.attributes:
            sensors.append(
                {
                    "key": "pulse_duration",
                    "translation_key": "pulse_duration",
                    "native_unit_of_measurement": UnitOfTime.SECONDS,
                    "value_fn": lambda: self.device.attributes.get("pulse_duration", 1),
                    "icon": "mdi:timer",
                    "enabled_by_default": False,
                }
            )

        return sensors

    async def _async_turn_on(self) -> None:
        """Turn the relay on."""
        await self.device.coordinator.api.async_set_relay_state(
            self.device.device_id, True
        )
        await self.device.coordinator.async_request_refresh()

    async def _async_turn_off(self) -> None:
        """Turn the relay off."""
        await self.device.coordinator.api.async_set_relay_state(
            self.device.device_id, False
        )
        await self.device.coordinator.async_request_refresh()

    async def _async_pulse(self) -> None:
        """Trigger relay pulse (for gates, garage doors).

        Default duration is 1 second, can be configured via pulse_duration attribute.
        """
        duration = self.device.attributes.get("pulse_duration", 1)
        await self.device.coordinator.api.async_pulse_relay(
            self.device.device_id, duration
        )
        # Pulse triggers automatically, no need to refresh immediately
