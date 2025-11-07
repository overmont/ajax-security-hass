from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchServiceForSubscriptionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("new_subscription_id",)
        NEW_SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        new_subscription_id: str
        def __init__(self, new_subscription_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "service_not_found", "subscription_not_found", "reseller_not_found", "dealer_not_found", "linkage_suspended", "illegal_state")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        LINKAGE_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        service_not_found: _response_pb2.Error
        subscription_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        linkage_suspended: _response_pb2.Error
        illegal_state: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., subscription_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., reseller_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., linkage_suspended: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SwitchServiceForSubscriptionResponse.Success
    failure: SwitchServiceForSubscriptionResponse.Failure
    def __init__(self, success: _Optional[_Union[SwitchServiceForSubscriptionResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SwitchServiceForSubscriptionResponse.Failure, _Mapping]] = ...) -> None: ...
