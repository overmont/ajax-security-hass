from systems.ajax.api.mobile.v2.common.accounting import feature_target_info_pb2 as _feature_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModifySubscriptionTargetsRequest(_message.Message):
    __slots__ = ("subscription_id", "updated_targets_list")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TARGETS_LIST_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    updated_targets_list: _containers.RepeatedCompositeFieldContainer[_feature_target_info_pb2.FeatureTargetInfo]
    def __init__(self, subscription_id: _Optional[str] = ..., updated_targets_list: _Optional[_Iterable[_Union[_feature_target_info_pb2.FeatureTargetInfo, _Mapping]]] = ...) -> None: ...
