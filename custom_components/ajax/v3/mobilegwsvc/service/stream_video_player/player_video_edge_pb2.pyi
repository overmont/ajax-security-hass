from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import app_settings_pb2 as _app_settings_pb2
from v3.mobilegwsvc.service.stream_video_player import player_channel_pb2 as _player_channel_pb2
from v3.mobilegwsvc.service.stream_video_player import player_detector_pb2 as _player_detector_pb2
from v3.mobilegwsvc.service.stream_video_player import player_storage_device_pb2 as _player_storage_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerVideoEdge(_message.Message):
    __slots__ = ("id", "channels", "detectors", "storage_devices", "timezone_id", "app_settings")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    channels: _containers.RepeatedCompositeFieldContainer[_player_channel_pb2.PlayerChannel]
    detectors: _containers.RepeatedCompositeFieldContainer[_player_detector_pb2.PlayerDetector]
    storage_devices: _containers.RepeatedCompositeFieldContainer[_player_storage_device_pb2.PlayerStorageDevice]
    timezone_id: str
    app_settings: _app_settings_pb2.AppSettings
    def __init__(self, id: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[_player_channel_pb2.PlayerChannel, _Mapping]]] = ..., detectors: _Optional[_Iterable[_Union[_player_detector_pb2.PlayerDetector, _Mapping]]] = ..., storage_devices: _Optional[_Iterable[_Union[_player_storage_device_pb2.PlayerStorageDevice, _Mapping]]] = ..., timezone_id: _Optional[str] = ..., app_settings: _Optional[_Union[_app_settings_pb2.AppSettings, _Mapping]] = ...) -> None: ...
