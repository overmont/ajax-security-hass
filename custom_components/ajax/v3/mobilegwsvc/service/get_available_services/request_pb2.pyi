from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableServicesRequest(_message.Message):
    __slots__ = ("feature_target_id", "feature_target")
    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    feature_target_id: str
    feature_target: _feature_target_pb2.FeatureTarget
    def __init__(self, feature_target_id: _Optional[str] = ..., feature_target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ...) -> None: ...
