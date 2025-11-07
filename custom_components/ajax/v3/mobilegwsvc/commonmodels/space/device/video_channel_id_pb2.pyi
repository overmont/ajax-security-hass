from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoChannelId(_message.Message):
    __slots__ = ("video_edge_id", "channel_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...
