from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageUrls(_message.Message):
    __slots__ = ("small", "medium", "big", "base_path")
    SMALL_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    BIG_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    small: str
    medium: str
    big: str
    base_path: str
    def __init__(self, small: _Optional[str] = ..., medium: _Optional[str] = ..., big: _Optional[str] = ..., base_path: _Optional[str] = ...) -> None: ...
