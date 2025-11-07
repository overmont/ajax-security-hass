from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTamperStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_TAMPER_STATUS_UNSPECIFIED: _ClassVar[DeviceTamperStatus]
    DEVICE_TAMPER_STATUS_NOT_TAMPERED: _ClassVar[DeviceTamperStatus]
    DEVICE_TAMPER_STATUS_TAMPERED: _ClassVar[DeviceTamperStatus]
DEVICE_TAMPER_STATUS_UNSPECIFIED: DeviceTamperStatus
DEVICE_TAMPER_STATUS_NOT_TAMPERED: DeviceTamperStatus
DEVICE_TAMPER_STATUS_TAMPERED: DeviceTamperStatus
