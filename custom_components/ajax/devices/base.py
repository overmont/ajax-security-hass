"""Base device handler for Ajax devices.

This module defines the base class that all device-specific handlers inherit from.
Each handler knows which Home Assistant entities (sensors, binary sensors, switches, etc.)
should be created for that specific device type.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.helpers.entity import Entity

    from ..models import AjaxDevice


class AjaxDeviceHandler(ABC):
    """Base class for Ajax device type handlers.

    Each device type (MotionProtect, DoorProtect, etc.) has its own handler
    that defines which entities should be created for that device.
    """

    def __init__(self, device: AjaxDevice) -> None:
        """Initialize the device handler.

        Args:
            device: The Ajax device data model
        """
        self.device = device

    @abstractmethod
    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entity descriptions for this device.

        Returns:
            List of dicts with keys:
                - key: Unique key for the sensor
                - name: Display name
                - device_class: BinarySensorDeviceClass
                - value_fn: Function to get the value from device
                - icon: Optional icon
                - enabled_by_default: Whether enabled by default
        """
        return []

    @abstractmethod
    def get_sensors(self) -> list[dict]:
        """Return sensor entity descriptions for this device.

        Returns:
            List of dicts with keys:
                - key: Unique key for the sensor
                - name: Display name
                - device_class: SensorDeviceClass
                - native_unit_of_measurement: Optional unit
                - state_class: Optional SensorStateClass
                - value_fn: Function to get the value from device
                - icon: Optional icon
                - enabled_by_default: Whether enabled by default
        """
        return []

    def get_switches(self) -> list[dict]:
        """Return switch entity descriptions for this device.

        Returns:
            List of dicts with keys:
                - key: Unique key for the switch
                - name: Display name
                - value_fn: Function to get the state from device
                - turn_on_fn: Function to turn on
                - turn_off_fn: Function to turn off
                - icon: Optional icon
                - enabled_by_default: Whether enabled by default
        """
        return []

    def get_buttons(self) -> list[dict]:
        """Return button entity descriptions for this device.

        Returns:
            List of dicts with keys:
                - key: Unique key for the button
                - name: Display name
                - press_fn: Function to press the button
                - icon: Optional icon
                - enabled_by_default: Whether enabled by default
        """
        return []

    def get_alarm_control_panels(self) -> list[dict]:
        """Return alarm control panel descriptions for this device.

        Usually only the Hub device creates an alarm control panel.

        Returns:
            List of dicts with alarm panel configuration
        """
        return []
