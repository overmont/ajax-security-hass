from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeactivateServiceSubscriptionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "subscription_not_found", "permission_denied", "illegal_state")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        subscription_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        illegal_state: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., subscription_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DeactivateServiceSubscriptionResponse.Success
    failure: DeactivateServiceSubscriptionResponse.Failure
    def __init__(self, success: _Optional[_Union[DeactivateServiceSubscriptionResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[DeactivateServiceSubscriptionResponse.Failure, _Mapping]] = ...) -> None: ...
