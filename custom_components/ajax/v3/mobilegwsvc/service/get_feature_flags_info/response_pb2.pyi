from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFeatureFlagsInfoResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("known_features",)
        class FeatureState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FEATURE_STATE_UNSPECIFIED: _ClassVar[GetFeatureFlagsInfoResponse.Success.FeatureState]
            FEATURE_STATE_DISABLED: _ClassVar[GetFeatureFlagsInfoResponse.Success.FeatureState]
            FEATURE_STATE_ENABLED: _ClassVar[GetFeatureFlagsInfoResponse.Success.FeatureState]
        FEATURE_STATE_UNSPECIFIED: GetFeatureFlagsInfoResponse.Success.FeatureState
        FEATURE_STATE_DISABLED: GetFeatureFlagsInfoResponse.Success.FeatureState
        FEATURE_STATE_ENABLED: GetFeatureFlagsInfoResponse.Success.FeatureState
        class FeatureInfo(_message.Message):
            __slots__ = ("feature_name", "feature_state")
            FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
            FEATURE_STATE_FIELD_NUMBER: _ClassVar[int]
            feature_name: str
            feature_state: GetFeatureFlagsInfoResponse.Success.FeatureState
            def __init__(self, feature_name: _Optional[str] = ..., feature_state: _Optional[_Union[GetFeatureFlagsInfoResponse.Success.FeatureState, str]] = ...) -> None: ...
        KNOWN_FEATURES_FIELD_NUMBER: _ClassVar[int]
        known_features: _containers.RepeatedCompositeFieldContainer[GetFeatureFlagsInfoResponse.Success.FeatureInfo]
        def __init__(self, known_features: _Optional[_Iterable[_Union[GetFeatureFlagsInfoResponse.Success.FeatureInfo, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetFeatureFlagsInfoResponse.Success
    failure: GetFeatureFlagsInfoResponse.Failure
    def __init__(self, success: _Optional[_Union[GetFeatureFlagsInfoResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetFeatureFlagsInfoResponse.Failure, _Mapping]] = ...) -> None: ...
