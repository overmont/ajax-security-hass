from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupPermissions(_message.Message):
    __slots__ = ("group_id", "permissions")
    class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_PERMISSION_INFO: _ClassVar[GroupPermissions.Permission]
        ARM: _ClassVar[GroupPermissions.Permission]
        DISARM: _ClassVar[GroupPermissions.Permission]
    NO_PERMISSION_INFO: GroupPermissions.Permission
    ARM: GroupPermissions.Permission
    DISARM: GroupPermissions.Permission
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    permissions: _containers.RepeatedScalarFieldContainer[GroupPermissions.Permission]
    def __init__(self, group_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[GroupPermissions.Permission, str]]] = ...) -> None: ...
