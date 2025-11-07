from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScanVideoEdgeWifiRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ...) -> None: ...
