from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FollowedGroupIds(_message.Message):
    __slots__ = ("group_ids",)
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_ids: _Optional[_Iterable[str]] = ...) -> None: ...
