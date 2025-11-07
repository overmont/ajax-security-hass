from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupPermissions(_message.Message):
    __slots__ = ("group_id", "group_permission")
    class GroupPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GROUP_PERMISSION_UNSPECIFIED: _ClassVar[GroupPermissions.GroupPermission]
        GROUP_PERMISSION_ENABLED: _ClassVar[GroupPermissions.GroupPermission]
        GROUP_PERMISSION_DISABLED: _ClassVar[GroupPermissions.GroupPermission]
    GROUP_PERMISSION_UNSPECIFIED: GroupPermissions.GroupPermission
    GROUP_PERMISSION_ENABLED: GroupPermissions.GroupPermission
    GROUP_PERMISSION_DISABLED: GroupPermissions.GroupPermission
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    group_permission: GroupPermissions.GroupPermission
    def __init__(self, group_id: _Optional[str] = ..., group_permission: _Optional[_Union[GroupPermissions.GroupPermission, str]] = ...) -> None: ...
