from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.system import accelerometer_settings_pb2 as _accelerometer_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeAccelerometerSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "accelerometer_settings")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    accelerometer_settings: _accelerometer_settings_pb2.AccelerometerSettings
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., accelerometer_settings: _Optional[_Union[_accelerometer_settings_pb2.AccelerometerSettings, _Mapping]] = ...) -> None: ...
