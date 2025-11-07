from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BatteryChargedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_CHARGED_STATE_UNSPECIFIED: _ClassVar[BatteryChargedState]
    BATTERY_CHARGED_STATE_LOW_CHARGED: _ClassVar[BatteryChargedState]
    BATTERY_CHARGED_STATE_FULL_CHARGED: _ClassVar[BatteryChargedState]
BATTERY_CHARGED_STATE_UNSPECIFIED: BatteryChargedState
BATTERY_CHARGED_STATE_LOW_CHARGED: BatteryChargedState
BATTERY_CHARGED_STATE_FULL_CHARGED: BatteryChargedState
