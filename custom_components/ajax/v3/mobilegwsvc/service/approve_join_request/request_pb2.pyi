from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveJoinByQrRequest(_message.Message):
    __slots__ = ("request_id", "space_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    space_id: str
    def __init__(self, request_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...
