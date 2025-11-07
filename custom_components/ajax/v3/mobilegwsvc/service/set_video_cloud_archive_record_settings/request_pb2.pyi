from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from v3.mobilegwsvc.commonmodels.video import duration_option_pb2 as _duration_option_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoCloudArchiveRecordSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "record_mode", "record_policy", "recording_duration", "cooldown_interval")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    RECORDING_DURATION_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    record_mode: _archive_pb2.RecordMode
    record_policy: _archive_pb2.RecordPolicy
    recording_duration: _duration_option_pb2.DurationOption
    cooldown_interval: _duration_option_pb2.DurationOption
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., record_mode: _Optional[_Union[_archive_pb2.RecordMode, str]] = ..., record_policy: _Optional[_Union[_archive_pb2.RecordPolicy, str]] = ..., recording_duration: _Optional[_Union[_duration_option_pb2.DurationOption, str]] = ..., cooldown_interval: _Optional[_Union[_duration_option_pb2.DurationOption, str]] = ...) -> None: ...
