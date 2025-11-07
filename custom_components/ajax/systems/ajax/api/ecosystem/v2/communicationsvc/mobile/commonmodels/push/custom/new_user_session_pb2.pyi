from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NewUserSession(_message.Message):
    __slots__ = ("sessionId", "client_os", "device_model", "last_connection_ip")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_IP_FIELD_NUMBER: _ClassVar[int]
    sessionId: int
    client_os: str
    device_model: str
    last_connection_ip: str
    def __init__(self, sessionId: _Optional[int] = ..., client_os: _Optional[str] = ..., device_model: _Optional[str] = ..., last_connection_ip: _Optional[str] = ...) -> None: ...
