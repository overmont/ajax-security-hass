from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveFragmentInfo(_message.Message):
    __slots__ = ("fragment_id", "ts", "duration")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    fragment_id: int
    ts: int
    duration: int
    def __init__(self, fragment_id: _Optional[int] = ..., ts: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...
