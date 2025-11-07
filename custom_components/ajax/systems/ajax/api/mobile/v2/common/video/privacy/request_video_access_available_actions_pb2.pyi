from systems.ajax.api.mobile.v2.common.video.privacy import channel_permission_pb2 as _channel_permission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestVideoAccessAvailableActions(_message.Message):
    __slots__ = ("can_request_video_access", "available_channel_permissions")
    CAN_REQUEST_VIDEO_ACCESS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_CHANNEL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    can_request_video_access: bool
    available_channel_permissions: _containers.RepeatedScalarFieldContainer[_channel_permission_pb2.ChannelPermission]
    def __init__(self, can_request_video_access: bool = ..., available_channel_permissions: _Optional[_Iterable[_Union[_channel_permission_pb2.ChannelPermission, str]]] = ...) -> None: ...
