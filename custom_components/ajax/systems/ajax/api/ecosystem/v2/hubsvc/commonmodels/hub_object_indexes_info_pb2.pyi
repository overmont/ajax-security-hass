from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubObjectIndexesInfo(_message.Message):
    __slots__ = ("range",)
    class Range(_message.Message):
        __slots__ = ("min_index", "max_index")
        MIN_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_INDEX_FIELD_NUMBER: _ClassVar[int]
        min_index: int
        max_index: int
        def __init__(self, min_index: _Optional[int] = ..., max_index: _Optional[int] = ...) -> None: ...
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: HubObjectIndexesInfo.Range
    def __init__(self, range: _Optional[_Union[HubObjectIndexesInfo.Range, _Mapping]] = ...) -> None: ...
