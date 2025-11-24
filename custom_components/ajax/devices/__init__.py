"""Ajax device type handlers.

This module organizes device handlers by Ajax device type for easier maintenance
and extensibility. Each device type (MotionProtect, DoorProtect, FireProtect, etc.)
has its own module that defines which entities it should create.

Structure:
- base.py: Base device handler class
- motion_detector.py: MotionProtect, MotionProtect Plus, CombiProtect
- door_contact.py: DoorProtect, DoorProtect Plus
- smoke_detector.py: FireProtect, FireProtect Plus, FireProtect 2
- flood_detector.py: LeaksProtect
- socket.py: Socket, Relay, WallSwitch
- hub.py: Hub/Hub 2/Hub Plus with alarm control panel
- keypad.py: KeyPad, KeyPad Plus
- button.py: Button, DoubleButton, SpaceControl
- life_quality.py: LifeQuality air quality sensor
"""

from .base import AjaxDeviceHandler
from .door_contact import DoorContactHandler
from .flood_detector import FloodDetectorHandler
from .hub import HubHandler
from .light import LightHandler
from .motion_detector import MotionDetectorHandler
from .relay import RelayHandler
from .smoke_detector import SmokeDetectorHandler
from .socket import SocketHandler

__all__ = [
    "AjaxDeviceHandler",
    "DoorContactHandler",
    "FloodDetectorHandler",
    "HubHandler",
    "LightHandler",
    "MotionDetectorHandler",
    "RelayHandler",
    "SmokeDetectorHandler",
    "SocketHandler",
]
