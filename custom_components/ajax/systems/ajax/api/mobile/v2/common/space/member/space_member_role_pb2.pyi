from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMemberRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_MEMBER_ROLE_UNSPECIFIED: _ClassVar[SpaceMemberRole]
    SPACE_MEMBER_ROLE_USER: _ClassVar[SpaceMemberRole]
    SPACE_MEMBER_ROLE_ADMIN: _ClassVar[SpaceMemberRole]
    SPACE_MEMBER_ROLE_PRO: _ClassVar[SpaceMemberRole]
    SPACE_MEMBER_ROLE_COMPANY: _ClassVar[SpaceMemberRole]
SPACE_MEMBER_ROLE_UNSPECIFIED: SpaceMemberRole
SPACE_MEMBER_ROLE_USER: SpaceMemberRole
SPACE_MEMBER_ROLE_ADMIN: SpaceMemberRole
SPACE_MEMBER_ROLE_PRO: SpaceMemberRole
SPACE_MEMBER_ROLE_COMPANY: SpaceMemberRole
