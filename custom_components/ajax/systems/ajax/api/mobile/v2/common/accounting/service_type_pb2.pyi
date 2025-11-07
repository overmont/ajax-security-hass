from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_TYPE_N0_INFO: _ClassVar[ServiceType]
    SERVICE_TYPE_DEALER: _ClassVar[ServiceType]
    SERVICE_TYPE_RESELLER: _ClassVar[ServiceType]
SERVICE_TYPE_N0_INFO: ServiceType
SERVICE_TYPE_DEALER: ServiceType
SERVICE_TYPE_RESELLER: ServiceType
