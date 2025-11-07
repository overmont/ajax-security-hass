from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshSmartLocksRequest(_message.Message):
    __slots__ = ("space_id", "smart_lock_ids")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, space_id: _Optional[str] = ..., smart_lock_ids: _Optional[_Iterable[str]] = ...) -> None: ...
