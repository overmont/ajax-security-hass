from systems.ajax.api.mobile.v2.common.video.privacy import permanent_channel_permissions_pb2 as _permanent_channel_permissions_pb2
from systems.ajax.api.mobile.v2.common.video.privacy import temporary_channel_permissions_pb2 as _temporary_channel_permissions_pb2
from systems.ajax.api.mobile.v2.common.video.privacy import channel_permission_pb2 as _channel_permission_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelPermissions(_message.Message):
    __slots__ = ("channel_id", "active", "granted")
    class ActiveChannelPermissions(_message.Message):
        __slots__ = ("permissions",)
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        permissions: _containers.RepeatedScalarFieldContainer[_channel_permission_pb2.ChannelPermission]
        def __init__(self, permissions: _Optional[_Iterable[_Union[_channel_permission_pb2.ChannelPermission, str]]] = ...) -> None: ...
    class GrantedChannelPermissions(_message.Message):
        __slots__ = ("permanent", "temporary", "merged")
        PERMANENT_FIELD_NUMBER: _ClassVar[int]
        TEMPORARY_FIELD_NUMBER: _ClassVar[int]
        MERGED_FIELD_NUMBER: _ClassVar[int]
        permanent: _permanent_channel_permissions_pb2.PermanentChannelPermissions
        temporary: _temporary_channel_permissions_pb2.TemporaryChannelPermissions
        merged: ChannelPermissions.MergedGrantedChannelPermissions
        def __init__(self, permanent: _Optional[_Union[_permanent_channel_permissions_pb2.PermanentChannelPermissions, _Mapping]] = ..., temporary: _Optional[_Union[_temporary_channel_permissions_pb2.TemporaryChannelPermissions, _Mapping]] = ..., merged: _Optional[_Union[ChannelPermissions.MergedGrantedChannelPermissions, _Mapping]] = ...) -> None: ...
    class MergedGrantedChannelPermissions(_message.Message):
        __slots__ = ("permissions", "type", "expire_at")
        class ChannelPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTIVE_CHANNEL_PERMISSION_TYPE_UNSPECIFIED: _ClassVar[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType]
            ACTIVE_CHANNEL_PERMISSION_TYPE_ALWAYS: _ClassVar[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType]
            ACTIVE_CHANNEL_PERMISSION_TYPE_WHEN_ARMED: _ClassVar[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType]
            ACTIVE_CHANNEL_PERMISSION_TYPE_AFTER_ALARM: _ClassVar[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType]
            ACTIVE_CHANNEL_PERMISSION_TYPE_TEMPORARY: _ClassVar[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType]
        ACTIVE_CHANNEL_PERMISSION_TYPE_UNSPECIFIED: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        ACTIVE_CHANNEL_PERMISSION_TYPE_ALWAYS: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        ACTIVE_CHANNEL_PERMISSION_TYPE_WHEN_ARMED: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        ACTIVE_CHANNEL_PERMISSION_TYPE_AFTER_ALARM: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        ACTIVE_CHANNEL_PERMISSION_TYPE_TEMPORARY: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
        permissions: _containers.RepeatedScalarFieldContainer[_channel_permission_pb2.ChannelPermission]
        type: ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType
        expire_at: _timestamp_pb2.Timestamp
        def __init__(self, permissions: _Optional[_Iterable[_Union[_channel_permission_pb2.ChannelPermission, str]]] = ..., type: _Optional[_Union[ChannelPermissions.MergedGrantedChannelPermissions.ChannelPermissionType, str]] = ..., expire_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    GRANTED_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    active: ChannelPermissions.ActiveChannelPermissions
    granted: ChannelPermissions.GrantedChannelPermissions
    def __init__(self, channel_id: _Optional[str] = ..., active: _Optional[_Union[ChannelPermissions.ActiveChannelPermissions, _Mapping]] = ..., granted: _Optional[_Union[ChannelPermissions.GrantedChannelPermissions, _Mapping]] = ...) -> None: ...
