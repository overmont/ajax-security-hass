from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveTzEntry(_message.Message):
    __slots__ = ("ts", "tz_offset")
    TS_FIELD_NUMBER: _ClassVar[int]
    TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ts: int
    tz_offset: int
    def __init__(self, ts: _Optional[int] = ..., tz_offset: _Optional[int] = ...) -> None: ...
