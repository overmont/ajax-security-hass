from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ("resolution", "url")
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    resolution: str
    url: str
    def __init__(self, resolution: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
