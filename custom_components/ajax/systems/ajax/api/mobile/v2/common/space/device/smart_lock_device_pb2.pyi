from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockDevice(_message.Message):
    __slots__ = ("id", "room_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    def __init__(self, id: _Optional[str] = ..., room_id: _Optional[str] = ...) -> None: ...
