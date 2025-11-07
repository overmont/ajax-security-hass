from systems.ajax.api.mobile.v2.common.accounting import feature_target_info_pb2 as _feature_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSubscriptionManagementUrlRequest(_message.Message):
    __slots__ = ("service_group_id", "feature_target_infos", "redirect_link")
    SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_LINK_FIELD_NUMBER: _ClassVar[int]
    service_group_id: str
    feature_target_infos: _containers.RepeatedCompositeFieldContainer[_feature_target_info_pb2.FeatureTargetInfo]
    redirect_link: str
    def __init__(self, service_group_id: _Optional[str] = ..., feature_target_infos: _Optional[_Iterable[_Union[_feature_target_info_pb2.FeatureTargetInfo, _Mapping]]] = ..., redirect_link: _Optional[str] = ...) -> None: ...
