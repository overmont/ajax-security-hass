from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SessionDescription(_message.Message):
    __slots__ = ("type", "sdp")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    type: str
    sdp: str
    def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ...) -> None: ...
