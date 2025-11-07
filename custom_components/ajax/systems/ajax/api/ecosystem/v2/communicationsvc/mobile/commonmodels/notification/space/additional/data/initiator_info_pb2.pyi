from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("initiator_id", "initiator_name")
    INITIATOR_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    initiator_id: str
    initiator_name: str
    def __init__(self, initiator_id: _Optional[str] = ..., initiator_name: _Optional[str] = ...) -> None: ...
