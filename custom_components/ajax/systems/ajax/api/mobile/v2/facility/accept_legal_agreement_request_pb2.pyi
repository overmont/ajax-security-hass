from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptLegalAgreementRequest(_message.Message):
    __slots__ = ("facility_id", "agreement_version")
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    agreement_version: str
    def __init__(self, facility_id: _Optional[str] = ..., agreement_version: _Optional[str] = ...) -> None: ...

class AcceptLegalAgreementResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "facility_not_found", "permission_denied", "already_processed")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        FACILITY_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ALREADY_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        facility_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        already_processed: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., facility_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., already_processed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: AcceptLegalAgreementResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[AcceptLegalAgreementResponse.Failure, _Mapping]] = ...) -> None: ...
