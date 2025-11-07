from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginTokenRequest(_message.Message):
    __slots__ = ("login", "token", "machine_id")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    login: str
    token: str
    machine_id: str
    def __init__(self, login: _Optional[str] = ..., token: _Optional[str] = ..., machine_id: _Optional[str] = ...) -> None: ...
