from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteScheduledAccessRequest(_message.Message):
    __slots__ = ("id", "hub_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    hub_id: str
    def __init__(self, id: _Optional[int] = ..., hub_id: _Optional[str] = ...) -> None: ...
