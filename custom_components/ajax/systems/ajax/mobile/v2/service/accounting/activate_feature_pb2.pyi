from systems.ajax.api.mobile.v2.common.accounting import feature_on_target_pb2 as _feature_on_target_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateFeatureRequest(_message.Message):
    __slots__ = ("feature_id", "reseller_id", "feature_target_id")
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    RESELLER_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    feature_id: str
    reseller_id: str
    feature_target_id: str
    def __init__(self, feature_id: _Optional[str] = ..., reseller_id: _Optional[str] = ..., feature_target_id: _Optional[str] = ...) -> None: ...

class ActivateFeatureResponse(_message.Message):
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
    success: ActivateFeatureResponse.Success
    failure: ActivateFeatureResponse.Failure
    def __init__(self, success: _Optional[_Union[ActivateFeatureResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ActivateFeatureResponse.Failure, _Mapping]] = ...) -> None: ...
