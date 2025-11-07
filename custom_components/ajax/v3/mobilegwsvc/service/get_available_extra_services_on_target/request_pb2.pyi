from systems.ajax.api.mobile.v2.common.accounting import feature_target_info_pb2 as _feature_target_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableExtraServicesOnTargetRequest(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: _feature_target_info_pb2.FeatureTargetInfo
    def __init__(self, target: _Optional[_Union[_feature_target_info_pb2.FeatureTargetInfo, _Mapping]] = ...) -> None: ...
