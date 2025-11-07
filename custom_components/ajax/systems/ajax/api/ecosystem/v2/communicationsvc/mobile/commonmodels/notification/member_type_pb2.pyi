from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MemberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_TYPE_UNSPECIFIED: _ClassVar[MemberType]
    MEMBER_TYPE_USER: _ClassVar[MemberType]
    MEMBER_TYPE_PRO: _ClassVar[MemberType]
    MEMBER_TYPE_COMPANY: _ClassVar[MemberType]
MEMBER_TYPE_UNSPECIFIED: MemberType
MEMBER_TYPE_USER: MemberType
MEMBER_TYPE_PRO: MemberType
MEMBER_TYPE_COMPANY: MemberType
