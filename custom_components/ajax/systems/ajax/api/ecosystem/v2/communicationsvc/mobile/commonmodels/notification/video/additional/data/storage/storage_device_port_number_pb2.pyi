from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StorageDevicePortNumber(_message.Message):
    __slots__ = ("actual_number", "display_number")
    ACTUAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    actual_number: int
    display_number: int
    def __init__(self, actual_number: _Optional[int] = ..., display_number: _Optional[int] = ...) -> None: ...
