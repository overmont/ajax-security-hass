from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.company import space_monitoring_company_pb2 as _space_monitoring_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchMonitoringCompaniesRequest(_message.Message):
    __slots__ = ("email", "space_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    space_id: str
    def __init__(self, email: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class SearchMonitoringCompaniesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("companies",)
        COMPANIES_FIELD_NUMBER: _ClassVar[int]
        companies: _containers.RepeatedCompositeFieldContainer[_space_monitoring_company_pb2.SpaceMonitoringCompany]
        def __init__(self, companies: _Optional[_Iterable[_Union[_space_monitoring_company_pb2.SpaceMonitoringCompany, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SearchMonitoringCompaniesResponse.Success
    failure: SearchMonitoringCompaniesResponse.Failure
    def __init__(self, success: _Optional[_Union[SearchMonitoringCompaniesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SearchMonitoringCompaniesResponse.Failure, _Mapping]] = ...) -> None: ...
