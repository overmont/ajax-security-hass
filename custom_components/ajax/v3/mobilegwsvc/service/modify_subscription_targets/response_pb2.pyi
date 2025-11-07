from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModifySubscriptionTargetsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("unknown_target_type",)
        UNKNOWN_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
        unknown_target_type: _response_pb2.Error
        def __init__(self, unknown_target_type: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ModifySubscriptionTargetsResponse.Success
    failure: ModifySubscriptionTargetsResponse.Failure
    def __init__(self, success: _Optional[_Union[ModifySubscriptionTargetsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ModifySubscriptionTargetsResponse.Failure, _Mapping]] = ...) -> None: ...
