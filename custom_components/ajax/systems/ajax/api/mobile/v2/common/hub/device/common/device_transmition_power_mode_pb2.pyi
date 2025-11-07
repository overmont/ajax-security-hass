from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTransmitionPowerMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TRANSMITION_POWER_MODE_UNSPECIFIED: _ClassVar[DeviceTransmitionPowerMode]
    DEVICE_TRANSMITION_POWER_MODE_AUTO: _ClassVar[DeviceTransmitionPowerMode]
    DEVICE_TRANSMITION_POWER_MODE_FIX: _ClassVar[DeviceTransmitionPowerMode]
    DEVICE_TRANSMITION_POWER_MODE_RESERVED: _ClassVar[DeviceTransmitionPowerMode]
    DEVICE_TRANSMITION_POWER_MODE_MAX: _ClassVar[DeviceTransmitionPowerMode]
DEVICE_TRANSMITION_POWER_MODE_UNSPECIFIED: DeviceTransmitionPowerMode
DEVICE_TRANSMITION_POWER_MODE_AUTO: DeviceTransmitionPowerMode
DEVICE_TRANSMITION_POWER_MODE_FIX: DeviceTransmitionPowerMode
DEVICE_TRANSMITION_POWER_MODE_RESERVED: DeviceTransmitionPowerMode
DEVICE_TRANSMITION_POWER_MODE_MAX: DeviceTransmitionPowerMode
