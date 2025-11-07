from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_STATE_UNSPECIFIED: _ClassVar[ServiceState]
    SERVICE_STATE_REQUIRED: _ClassVar[ServiceState]
    SERVICE_STATE_ACTIVE: _ClassVar[ServiceState]
    SERVICE_STATE_SUSPENDED: _ClassVar[ServiceState]
    SERVICE_STATE_AVAILABLE: _ClassVar[ServiceState]
    SERVICE_STATE_NOT_AVAILABLE: _ClassVar[ServiceState]
SERVICE_STATE_UNSPECIFIED: ServiceState
SERVICE_STATE_REQUIRED: ServiceState
SERVICE_STATE_ACTIVE: ServiceState
SERVICE_STATE_SUSPENDED: ServiceState
SERVICE_STATE_AVAILABLE: ServiceState
SERVICE_STATE_NOT_AVAILABLE: ServiceState
