from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_ROLE_UNSPECIFIED: _ClassVar[UserRole]
    USER_ROLE_USER: _ClassVar[UserRole]
    USER_ROLE_PRO: _ClassVar[UserRole]
USER_ROLE_UNSPECIFIED: UserRole
USER_ROLE_USER: UserRole
USER_ROLE_PRO: UserRole
