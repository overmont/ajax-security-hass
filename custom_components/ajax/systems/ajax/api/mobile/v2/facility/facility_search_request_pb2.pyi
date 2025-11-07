from v1.facility import facility_pb2 as _facility_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacilitySearchRequest(_message.Message):
    __slots__ = ("search_phrase", "limit", "offset")
    SEARCH_PHRASE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_phrase: str
    limit: int
    offset: int
    def __init__(self, search_phrase: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class FacilitySearchResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("facilities", "offset", "counter")
        FACILITIES_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        COUNTER_FIELD_NUMBER: _ClassVar[int]
        facilities: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility]
        offset: int
        counter: int
        def __init__(self, facilities: _Optional[_Iterable[_Union[_facility_pb2.Facility, _Mapping]]] = ..., offset: _Optional[int] = ..., counter: _Optional[int] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FacilitySearchResponse.Success
    failure: FacilitySearchResponse.Failure
    def __init__(self, success: _Optional[_Union[FacilitySearchResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FacilitySearchResponse.Failure, _Mapping]] = ...) -> None: ...
