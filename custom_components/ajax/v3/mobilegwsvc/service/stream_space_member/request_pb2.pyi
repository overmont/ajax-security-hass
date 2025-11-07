from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceMemberRequest(_message.Message):
    __slots__ = ("space_id", "space_member_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    space_member_id: str
    def __init__(self, space_id: _Optional[str] = ..., space_member_id: _Optional[str] = ...) -> None: ...
