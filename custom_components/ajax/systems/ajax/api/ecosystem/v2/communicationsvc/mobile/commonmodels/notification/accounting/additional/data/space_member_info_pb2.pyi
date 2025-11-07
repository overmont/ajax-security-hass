from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMemberInfo(_message.Message):
    __slots__ = ("space_member_id", "name")
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    space_member_id: str
    name: str
    def __init__(self, space_member_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
