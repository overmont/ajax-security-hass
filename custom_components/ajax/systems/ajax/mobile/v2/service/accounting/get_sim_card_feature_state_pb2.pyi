from systems.ajax.api.mobile.v2.common.accounting import feature_on_target_pb2 as _feature_on_target_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSimCardFeatureStateRequest(_message.Message):
    __slots__ = ("hub_id",)
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    def __init__(self, hub_id: _Optional[str] = ...) -> None: ...

class GetSimCardFeatureStateResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("feature",)
        FEATURE_FIELD_NUMBER: _ClassVar[int]
        feature: _feature_on_target_pb2.FeatureOnTarget
        def __init__(self, feature: _Optional[_Union[_feature_on_target_pb2.FeatureOnTarget, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetSimCardFeatureStateResponse.Success
    failure: GetSimCardFeatureStateResponse.Failure
    def __init__(self, success: _Optional[_Union[GetSimCardFeatureStateResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetSimCardFeatureStateResponse.Failure, _Mapping]] = ...) -> None: ...
