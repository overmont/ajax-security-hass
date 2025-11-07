from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMemberPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_MEMBER_PERMISSION_TYPE_UNSPECIFIED: _ClassVar[SpaceMemberPermissionType]
    PARTIAL_PERMISSION: _ClassVar[SpaceMemberPermissionType]
    FULL_PERMISSIONS: _ClassVar[SpaceMemberPermissionType]
SPACE_MEMBER_PERMISSION_TYPE_UNSPECIFIED: SpaceMemberPermissionType
PARTIAL_PERMISSION: SpaceMemberPermissionType
FULL_PERMISSIONS: SpaceMemberPermissionType
