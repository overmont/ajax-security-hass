from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableFollowedGroupsRequest(_message.Message):
    __slots__ = ("group_id", "space_id")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    space_id: str
    def __init__(self, group_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...
