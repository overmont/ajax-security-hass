from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTemperature(_message.Message):
    __slots__ = ("value", "is_extreme")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_EXTREME_FIELD_NUMBER: _ClassVar[int]
    value: int
    is_extreme: bool
    def __init__(self, value: _Optional[int] = ..., is_extreme: bool = ...) -> None: ...
