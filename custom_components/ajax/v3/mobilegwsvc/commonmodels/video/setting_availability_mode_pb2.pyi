from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SettingAvailabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETTING_AVAILABILITY_MODE_UNSPECIFIED: _ClassVar[SettingAvailabilityMode]
    SETTING_AVAILABILITY_MODE_AVAILABLE: _ClassVar[SettingAvailabilityMode]
    SETTING_AVAILABILITY_MODE_UNAVAILABLE: _ClassVar[SettingAvailabilityMode]
    SETTING_AVAILABILITY_MODE_LOCKED: _ClassVar[SettingAvailabilityMode]
SETTING_AVAILABILITY_MODE_UNSPECIFIED: SettingAvailabilityMode
SETTING_AVAILABILITY_MODE_AVAILABLE: SettingAvailabilityMode
SETTING_AVAILABILITY_MODE_UNAVAILABLE: SettingAvailabilityMode
SETTING_AVAILABILITY_MODE_LOCKED: SettingAvailabilityMode
