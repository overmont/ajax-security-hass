from systems.ajax.api.mobile.v2.common.video.privacy import channel_permissions_pb2 as _channel_permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgePermissions(_message.Message):
    __slots__ = ("device_id", "channel_permissions")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    channel_permissions: _containers.RepeatedCompositeFieldContainer[_channel_permissions_pb2.ChannelPermissions]
    def __init__(self, device_id: _Optional[str] = ..., channel_permissions: _Optional[_Iterable[_Union[_channel_permissions_pb2.ChannelPermissions, _Mapping]]] = ...) -> None: ...
