from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareVersion(_message.Message):
    __slots__ = ("major", "minor", "extra")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    extra: str
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., extra: _Optional[str] = ...) -> None: ...
