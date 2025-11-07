from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_type_pb2 as _video_notification_type_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeDetectorsEnabledByNotificationTypesRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "notification_types")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    notification_types: _containers.RepeatedScalarFieldContainer[_video_notification_type_pb2.VideoNotificationType]
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., notification_types: _Optional[_Iterable[_Union[_video_notification_type_pb2.VideoNotificationType, str]]] = ...) -> None: ...
