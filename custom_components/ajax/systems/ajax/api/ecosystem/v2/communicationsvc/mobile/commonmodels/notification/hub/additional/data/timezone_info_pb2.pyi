from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimezoneInfo(_message.Message):
    __slots__ = ("new_timezone",)
    NEW_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    new_timezone: str
    def __init__(self, new_timezone: _Optional[str] = ...) -> None: ...
