from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_type_pb2 as _video_notification_type_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoNotificationAlertSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "type", "line_crossing_rule_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    type: _video_notification_type_pb2.VideoNotificationType
    line_crossing_rule_id: int
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., type: _Optional[_Union[_video_notification_type_pb2.VideoNotificationType, str]] = ..., line_crossing_rule_id: _Optional[int] = ...) -> None: ...
