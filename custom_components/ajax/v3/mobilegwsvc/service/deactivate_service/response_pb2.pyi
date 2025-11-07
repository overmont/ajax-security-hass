from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeactivateServiceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "service_not_found", "dealer_not_found", "deactivate_failed")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEACTIVATE_FAILED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        service_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        deactivate_failed: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., deactivate_failed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DeactivateServiceResponse.Success
    failure: DeactivateServiceResponse.Failure
    def __init__(self, success: _Optional[_Union[DeactivateServiceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[DeactivateServiceResponse.Failure, _Mapping]] = ...) -> None: ...
