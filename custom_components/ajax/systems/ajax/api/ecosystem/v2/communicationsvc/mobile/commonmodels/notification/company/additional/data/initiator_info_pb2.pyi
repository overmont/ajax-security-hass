from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("id", "name", "mail")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mail: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., mail: _Optional[str] = ...) -> None: ...
