from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from v1.facility import facility_pb2 as _facility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JoinSpaceByCompanyRequest(_message.Message):
    __slots__ = ("hub_qr",)
    HUB_QR_FIELD_NUMBER: _ClassVar[int]
    hub_qr: str
    def __init__(self, hub_qr: _Optional[str] = ...) -> None: ...

class JoinSpaceByCompanyResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("facility",)
        FACILITY_FIELD_NUMBER: _ClassVar[int]
        facility: _facility_pb2.Facility
        def __init__(self, facility: _Optional[_Union[_facility_pb2.Facility, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("hub_error",)
        class HubError(_message.Message):
            __slots__ = ("bad_request", "space_not_found", "hub_not_found", "hub_qr_code_invalid", "hub_claim_error", "space_armed", "hub_claim_forbidden_by_company_error", "hub_offline")
            BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
            SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
            SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_FORBIDDEN_BY_COMPANY_ERROR_FIELD_NUMBER: _ClassVar[int]
            HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
            bad_request: _response_pb2.DefaultError
            space_not_found: _response_pb2.DefaultError
            hub_not_found: _response_pb2.DefaultError
            hub_qr_code_invalid: _response_pb2.DefaultError
            hub_claim_error: _response_pb2.DefaultError
            space_armed: _response_pb2.DefaultError
            hub_claim_forbidden_by_company_error: _response_pb2.DefaultError
            hub_offline: _response_pb2.DefaultError
            def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_qr_code_invalid: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_claim_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_claim_forbidden_by_company_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        hub_error: JoinSpaceByCompanyResponse.Failure.HubError
        def __init__(self, hub_error: _Optional[_Union[JoinSpaceByCompanyResponse.Failure.HubError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: JoinSpaceByCompanyResponse.Success
    failure: JoinSpaceByCompanyResponse.Failure
    def __init__(self, success: _Optional[_Union[JoinSpaceByCompanyResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[JoinSpaceByCompanyResponse.Failure, _Mapping]] = ...) -> None: ...
