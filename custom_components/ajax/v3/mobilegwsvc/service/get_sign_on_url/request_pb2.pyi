from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSignOnUrlRequest(_message.Message):
    __slots__ = ("email", "client_device_id", "relay_state")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RELAY_STATE_FIELD_NUMBER: _ClassVar[int]
    email: str
    client_device_id: str
    relay_state: str
    def __init__(self, email: _Optional[str] = ..., client_device_id: _Optional[str] = ..., relay_state: _Optional[str] = ...) -> None: ...
