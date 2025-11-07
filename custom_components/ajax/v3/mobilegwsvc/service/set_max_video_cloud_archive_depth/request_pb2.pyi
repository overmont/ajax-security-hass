from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video import duration_option_pb2 as _duration_option_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMaxVideoCloudArchiveDepthRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "max_cloud_archive_depth")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_CLOUD_ARCHIVE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    max_cloud_archive_depth: _duration_option_pb2.DurationOption
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., max_cloud_archive_depth: _Optional[_Union[_duration_option_pb2.DurationOption, str]] = ...) -> None: ...
