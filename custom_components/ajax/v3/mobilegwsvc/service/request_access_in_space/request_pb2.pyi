from systems.ajax.api.mobile.v2.common.video.privacy import channel_permission_pb2 as _channel_permission_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel import channel_reference_pb2 as _channel_reference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestAccessInSpaceRequest(_message.Message):
    __slots__ = ("space_id", "space_permissions", "video_permissions")
    class TemporaryPermissionsDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEMPORARY_PERMISSIONS_DURATION_UNSPECIFIED: _ClassVar[RequestAccessInSpaceRequest.TemporaryPermissionsDuration]
        TEMPORARY_PERMISSIONS_DURATION_1_HOUR: _ClassVar[RequestAccessInSpaceRequest.TemporaryPermissionsDuration]
        TEMPORARY_PERMISSIONS_DURATION_2_HOURS: _ClassVar[RequestAccessInSpaceRequest.TemporaryPermissionsDuration]
        TEMPORARY_PERMISSIONS_DURATION_4_HOURS: _ClassVar[RequestAccessInSpaceRequest.TemporaryPermissionsDuration]
        TEMPORARY_PERMISSIONS_DURATION_8_HOURS: _ClassVar[RequestAccessInSpaceRequest.TemporaryPermissionsDuration]
    TEMPORARY_PERMISSIONS_DURATION_UNSPECIFIED: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
    TEMPORARY_PERMISSIONS_DURATION_1_HOUR: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
    TEMPORARY_PERMISSIONS_DURATION_2_HOURS: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
    TEMPORARY_PERMISSIONS_DURATION_4_HOURS: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
    TEMPORARY_PERMISSIONS_DURATION_8_HOURS: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
    class RequestedSpacePermissions(_message.Message):
        __slots__ = ("permanent", "temporary")
        class RequestedPermanentSpacePermissions(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class RequestedTemporarySpacePermissions(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
            def __init__(self, duration: _Optional[_Union[RequestAccessInSpaceRequest.TemporaryPermissionsDuration, str]] = ...) -> None: ...
        PERMANENT_FIELD_NUMBER: _ClassVar[int]
        TEMPORARY_FIELD_NUMBER: _ClassVar[int]
        permanent: RequestAccessInSpaceRequest.RequestedSpacePermissions.RequestedPermanentSpacePermissions
        temporary: RequestAccessInSpaceRequest.RequestedSpacePermissions.RequestedTemporarySpacePermissions
        def __init__(self, permanent: _Optional[_Union[RequestAccessInSpaceRequest.RequestedSpacePermissions.RequestedPermanentSpacePermissions, _Mapping]] = ..., temporary: _Optional[_Union[RequestAccessInSpaceRequest.RequestedSpacePermissions.RequestedTemporarySpacePermissions, _Mapping]] = ...) -> None: ...
    class RequestedVideoPermissions(_message.Message):
        __slots__ = ("channels", "permissions", "duration")
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        channels: _containers.RepeatedCompositeFieldContainer[_channel_reference_pb2.ChannelReference]
        permissions: _containers.RepeatedScalarFieldContainer[_channel_permission_pb2.ChannelPermission]
        duration: RequestAccessInSpaceRequest.TemporaryPermissionsDuration
        def __init__(self, channels: _Optional[_Iterable[_Union[_channel_reference_pb2.ChannelReference, _Mapping]]] = ..., permissions: _Optional[_Iterable[_Union[_channel_permission_pb2.ChannelPermission, str]]] = ..., duration: _Optional[_Union[RequestAccessInSpaceRequest.TemporaryPermissionsDuration, str]] = ...) -> None: ...
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    space_permissions: RequestAccessInSpaceRequest.RequestedSpacePermissions
    video_permissions: RequestAccessInSpaceRequest.RequestedVideoPermissions
    def __init__(self, space_id: _Optional[str] = ..., space_permissions: _Optional[_Union[RequestAccessInSpaceRequest.RequestedSpacePermissions, _Mapping]] = ..., video_permissions: _Optional[_Union[RequestAccessInSpaceRequest.RequestedVideoPermissions, _Mapping]] = ...) -> None: ...
