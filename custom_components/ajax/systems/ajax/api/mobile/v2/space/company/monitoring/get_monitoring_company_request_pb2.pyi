from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.company import space_monitoring_company_pb2 as _space_monitoring_company_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMonitoringCompanyRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    def __init__(self, company_hex_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class GetMonitoringCompanyResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("company",)
        COMPANY_FIELD_NUMBER: _ClassVar[int]
        company: _space_monitoring_company_pb2.SpaceMonitoringCompany
        def __init__(self, company: _Optional[_Union[_space_monitoring_company_pb2.SpaceMonitoringCompany, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetMonitoringCompanyResponse.Success
    failure: GetMonitoringCompanyResponse.Failure
    def __init__(self, success: _Optional[_Union[GetMonitoringCompanyResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetMonitoringCompanyResponse.Failure, _Mapping]] = ...) -> None: ...
