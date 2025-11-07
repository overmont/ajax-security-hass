from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from v3.mobilegwsvc.commonmodels.accounting import hub_additional_info_pb2 as _hub_additional_info_pb2
from v3.mobilegwsvc.commonmodels.accounting import video_edge_additional_info_pb2 as _video_edge_additional_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnrichedTargetInfo(_message.Message):
    __slots__ = ("target_id", "target", "name", "room_name", "hub_additional_info", "video_edge_additional_info")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    HUB_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    target: _feature_target_pb2.FeatureTarget
    name: str
    room_name: str
    hub_additional_info: _hub_additional_info_pb2.HubAdditionalInfo
    video_edge_additional_info: _video_edge_additional_info_pb2.VideoEdgeAdditionalInfo
    def __init__(self, target_id: _Optional[str] = ..., target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ..., name: _Optional[str] = ..., room_name: _Optional[str] = ..., hub_additional_info: _Optional[_Union[_hub_additional_info_pb2.HubAdditionalInfo, _Mapping]] = ..., video_edge_additional_info: _Optional[_Union[_video_edge_additional_info_pb2.VideoEdgeAdditionalInfo, _Mapping]] = ...) -> None: ...
