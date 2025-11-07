from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSpaceIntegrationCredentialsRequest(_message.Message):
    __slots__ = ("credentials_id",)
    CREDENTIALS_ID_FIELD_NUMBER: _ClassVar[int]
    credentials_id: str
    def __init__(self, credentials_id: _Optional[str] = ...) -> None: ...
