from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceSignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_SIGNAL_LEVEL_UNSPECIFIED: _ClassVar[DeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_NO_SIGNAL: _ClassVar[DeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_WEAK: _ClassVar[DeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_NORMAL: _ClassVar[DeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_STRONG: _ClassVar[DeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_DISCONNECTED: _ClassVar[DeviceSignalLevel]
DEVICE_SIGNAL_LEVEL_UNSPECIFIED: DeviceSignalLevel
DEVICE_SIGNAL_LEVEL_NO_SIGNAL: DeviceSignalLevel
DEVICE_SIGNAL_LEVEL_WEAK: DeviceSignalLevel
DEVICE_SIGNAL_LEVEL_NORMAL: DeviceSignalLevel
DEVICE_SIGNAL_LEVEL_STRONG: DeviceSignalLevel
DEVICE_SIGNAL_LEVEL_DISCONNECTED: DeviceSignalLevel
