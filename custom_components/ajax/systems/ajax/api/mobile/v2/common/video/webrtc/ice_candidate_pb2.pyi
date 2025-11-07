from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IceCandidate(_message.Message):
    __slots__ = ("sdp_mid", "sdp_mline_index", "sdp")
    SDP_MID_FIELD_NUMBER: _ClassVar[int]
    SDP_MLINE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp_mid: str
    sdp_mline_index: int
    sdp: str
    def __init__(self, sdp_mid: _Optional[str] = ..., sdp_mline_index: _Optional[int] = ..., sdp: _Optional[str] = ...) -> None: ...
