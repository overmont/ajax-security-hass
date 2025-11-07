from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTransmissionPowerMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TRANSMISSION_POWER_MODE_UNSPECIFIED: _ClassVar[DeviceTransmissionPowerMode]
    DEVICE_TRANSMISSION_POWER_MODE_AUTO: _ClassVar[DeviceTransmissionPowerMode]
    DEVICE_TRANSMISSION_POWER_MODE_FIX: _ClassVar[DeviceTransmissionPowerMode]
    DEVICE_TRANSMISSION_POWER_MODE_MAX: _ClassVar[DeviceTransmissionPowerMode]
DEVICE_TRANSMISSION_POWER_MODE_UNSPECIFIED: DeviceTransmissionPowerMode
DEVICE_TRANSMISSION_POWER_MODE_AUTO: DeviceTransmissionPowerMode
DEVICE_TRANSMISSION_POWER_MODE_FIX: DeviceTransmissionPowerMode
DEVICE_TRANSMISSION_POWER_MODE_MAX: DeviceTransmissionPowerMode
