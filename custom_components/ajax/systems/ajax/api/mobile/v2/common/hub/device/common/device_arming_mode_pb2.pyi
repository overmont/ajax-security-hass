from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceArmingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_ARMING_MODE_UNSPECIFIED: _ClassVar[DeviceArmingMode]
    DEVICE_ARMING_MODE_NORMAL: _ClassVar[DeviceArmingMode]
    DEVICE_ARMING_MODE_ENTRY_EXIT: _ClassVar[DeviceArmingMode]
    DEVICE_ARMING_MODE_FOLLOWER: _ClassVar[DeviceArmingMode]
DEVICE_ARMING_MODE_UNSPECIFIED: DeviceArmingMode
DEVICE_ARMING_MODE_NORMAL: DeviceArmingMode
DEVICE_ARMING_MODE_ENTRY_EXIT: DeviceArmingMode
DEVICE_ARMING_MODE_FOLLOWER: DeviceArmingMode
