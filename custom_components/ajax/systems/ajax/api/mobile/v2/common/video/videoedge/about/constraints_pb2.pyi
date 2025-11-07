from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Constraints(_message.Message):
    __slots__ = ("channels_number",)
    CHANNELS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    channels_number: int
    def __init__(self, channels_number: _Optional[int] = ...) -> None: ...
