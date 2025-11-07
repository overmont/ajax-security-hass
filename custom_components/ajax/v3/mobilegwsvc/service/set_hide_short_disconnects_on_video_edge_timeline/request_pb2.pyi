from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import app_settings_pb2 as _app_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetHideShortDisconnectsOnVideoEdgeTimelineRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "hide_short_disconnects_on_timeline")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    hide_short_disconnects_on_timeline: _app_settings_pb2.HideShortDisconnectsOnTimeline
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., hide_short_disconnects_on_timeline: _Optional[_Union[_app_settings_pb2.HideShortDisconnectsOnTimeline, str]] = ...) -> None: ...
