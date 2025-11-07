from systems.ajax.api.mobile.v2.common.space.device import video_edge_channel_pb2 as _video_edge_channel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDeviceArmingPartRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_channel")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_channel: _video_edge_channel_pb2.VideoEdgeChannel
    def __init__(self, space_id: _Optional[str] = ..., video_edge_channel: _Optional[_Union[_video_edge_channel_pb2.VideoEdgeChannel, _Mapping]] = ...) -> None: ...
