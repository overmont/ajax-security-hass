from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalUserPermissions(_message.Message):
    __slots__ = ("admin", "operator")
    class LocalUserChannelPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_USER_CHANNEL_PERMISSION_UNSPECIFIED: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
        LOCAL_USER_CHANNEL_PERMISSION_VIEW_LIVE_STREAM: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
        LOCAL_USER_CHANNEL_PERMISSION_VIEW_ARCHIVE: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
        LOCAL_USER_CHANNEL_PERMISSION_PTZ: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
        LOCAL_USER_CHANNEL_PERMISSION_SOUND: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
        LOCAL_USER_CHANNEL_PERMISSION_EXPORT_ARCHIVE: _ClassVar[LocalUserPermissions.LocalUserChannelPermission]
    LOCAL_USER_CHANNEL_PERMISSION_UNSPECIFIED: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_VIEW_LIVE_STREAM: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_VIEW_ARCHIVE: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_PTZ: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_SOUND: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_EXPORT_ARCHIVE: LocalUserPermissions.LocalUserChannelPermission
    class LocalUserAdminRole(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class LocalUserOperatorRole(_message.Message):
        __slots__ = ("channel_ids", "channel_permissions")
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        channel_permissions: _containers.RepeatedScalarFieldContainer[LocalUserPermissions.LocalUserChannelPermission]
        def __init__(self, channel_ids: _Optional[_Iterable[str]] = ..., channel_permissions: _Optional[_Iterable[_Union[LocalUserPermissions.LocalUserChannelPermission, str]]] = ...) -> None: ...
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    admin: LocalUserPermissions.LocalUserAdminRole
    operator: LocalUserPermissions.LocalUserOperatorRole
    def __init__(self, admin: _Optional[_Union[LocalUserPermissions.LocalUserAdminRole, _Mapping]] = ..., operator: _Optional[_Union[LocalUserPermissions.LocalUserOperatorRole, _Mapping]] = ...) -> None: ...
