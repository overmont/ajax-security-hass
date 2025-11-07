from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreTargetResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "dealer_not_found", "subscription_plan_not_found", "illegal_state", "target_not_found", "dealer_did_not_suspend_target")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_PLAN_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        TARGET_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_DID_NOT_SUSPEND_TARGET_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        subscription_plan_not_found: _response_pb2.Error
        illegal_state: _response_pb2.Error
        target_not_found: _response_pb2.Error
        dealer_did_not_suspend_target: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., subscription_plan_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., target_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_did_not_suspend_target: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RestoreTargetResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[RestoreTargetResponse.Failure, _Mapping]] = ...) -> None: ...
