from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RtspSettings(_message.Message):
    __slots__ = ("http_port",)
    HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    http_port: int
    def __init__(self, http_port: _Optional[int] = ...) -> None: ...
