from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeLocalUserPasswordRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "name", "password")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    name: str
    password: str
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
