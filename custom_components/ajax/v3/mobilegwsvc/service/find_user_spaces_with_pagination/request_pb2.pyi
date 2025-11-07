from systems.ajax.api.mobile.v2.common import pagination_pb2 as _pagination_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindUserSpacesWithPaginationRequest(_message.Message):
    __slots__ = ("limit", "pagination", "search_phrase")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PHRASE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    pagination: _pagination_pb2.Pagination
    search_phrase: str
    def __init__(self, limit: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ..., search_phrase: _Optional[str] = ...) -> None: ...
