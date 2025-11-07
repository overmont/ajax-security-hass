from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFramesMedia(_message.Message):
    __slots__ = ("frames",)
    class VideoFrameMedia(_message.Message):
        __slots__ = ("url", "timestamp")
        URL_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        url: str
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, url: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[VideoFramesMedia.VideoFrameMedia]
    def __init__(self, frames: _Optional[_Iterable[_Union[VideoFramesMedia.VideoFrameMedia, _Mapping]]] = ...) -> None: ...
