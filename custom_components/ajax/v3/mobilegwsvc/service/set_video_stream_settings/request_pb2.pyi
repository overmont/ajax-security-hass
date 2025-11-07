from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_settings_pb2 as _media_device_settings_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoStreamSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "main_settings", "sub_settings")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    main_settings: _media_device_settings_pb2.VideoSettings.Stream
    sub_settings: _media_device_settings_pb2.VideoSettings.Stream
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., main_settings: _Optional[_Union[_media_device_settings_pb2.VideoSettings.Stream, _Mapping]] = ..., sub_settings: _Optional[_Union[_media_device_settings_pb2.VideoSettings.Stream, _Mapping]] = ...) -> None: ...
