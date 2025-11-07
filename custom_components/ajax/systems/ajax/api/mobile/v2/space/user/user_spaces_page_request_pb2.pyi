from systems.ajax.api.mobile.v2.common.space import space_profile_pb2 as _space_profile_pb2
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2
from systems.ajax.api.mobile.v2.common import pagination_pb2 as _pagination_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
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

class FindUserSpacesWithPaginationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("spaces", "pagination")
        SPACES_FIELD_NUMBER: _ClassVar[int]
        PAGINATION_FIELD_NUMBER: _ClassVar[int]
        spaces: _containers.RepeatedCompositeFieldContainer[_space_lite_pb2.LiteSpace]
        pagination: _pagination_pb2.Pagination
        def __init__(self, spaces: _Optional[_Iterable[_Union[_space_lite_pb2.LiteSpace, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindUserSpacesWithPaginationResponse.Success
    failure: FindUserSpacesWithPaginationResponse.Failure
    def __init__(self, success: _Optional[_Union[FindUserSpacesWithPaginationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindUserSpacesWithPaginationResponse.Failure, _Mapping]] = ...) -> None: ...
