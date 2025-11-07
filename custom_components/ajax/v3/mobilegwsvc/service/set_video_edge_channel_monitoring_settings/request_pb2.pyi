from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel import video_monitoring_state_pb2 as _video_monitoring_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeChannelMonitoringSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "zone_number", "monitoring_state")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    zone_number: str
    monitoring_state: _video_monitoring_state_pb2.VideoMonitoringState
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., zone_number: _Optional[str] = ..., monitoring_state: _Optional[_Union[_video_monitoring_state_pb2.VideoMonitoringState, str]] = ...) -> None: ...
