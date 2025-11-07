from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSubscriptionManagementUrlResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("subscription_management_url", "request_id")
        SUBSCRIPTION_MANAGEMENT_URL_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        subscription_management_url: str
        request_id: str
        def __init__(self, subscription_management_url: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "available_service_not_found")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        available_service_not_found: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., available_service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetSubscriptionManagementUrlResponse.Success
    failure: GetSubscriptionManagementUrlResponse.Failure
    def __init__(self, success: _Optional[_Union[GetSubscriptionManagementUrlResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetSubscriptionManagementUrlResponse.Failure, _Mapping]] = ...) -> None: ...
