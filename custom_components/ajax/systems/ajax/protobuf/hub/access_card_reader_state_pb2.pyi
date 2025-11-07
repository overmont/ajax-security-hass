from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCardReaderState(_message.Message):
    __slots__ = ("id", "timeout_seconds", "reader_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    READER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    timeout_seconds: int
    reader_active: bool
    def __init__(self, id: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., reader_active: bool = ...) -> None: ...
