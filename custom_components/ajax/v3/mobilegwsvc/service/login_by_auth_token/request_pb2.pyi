from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByAuthTokenRequest(_message.Message):
    __slots__ = ("session_token",)
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    session_token: bytes
    def __init__(self, session_token: _Optional[bytes] = ...) -> None: ...
