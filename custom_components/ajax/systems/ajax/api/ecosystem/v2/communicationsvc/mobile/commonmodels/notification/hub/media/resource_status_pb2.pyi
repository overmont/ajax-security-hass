from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_STATUS_UNSPECIFIED: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_IN_PROGRESS: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_READY: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_FAILED: _ClassVar[ResourceStatus]
RESOURCE_STATUS_UNSPECIFIED: ResourceStatus
RESOURCE_STATUS_IN_PROGRESS: ResourceStatus
RESOURCE_STATUS_READY: ResourceStatus
RESOURCE_STATUS_FAILED: ResourceStatus
