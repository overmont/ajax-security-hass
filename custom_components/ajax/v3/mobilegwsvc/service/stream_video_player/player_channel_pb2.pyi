from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_capabilities_pb2 as _media_device_capabilities_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import cloud_archive_pb2 as _cloud_archive_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerChannel(_message.Message):
    __slots__ = ("id", "device_info", "audio_output_settings", "video_capabilities", "video_settings", "audio_settings", "cloud_archive")
    class AudioOutputSettings(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AudioSettings(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class VideoCapabilities(_message.Message):
        __slots__ = ("ptz",)
        PTZ_FIELD_NUMBER: _ClassVar[int]
        ptz: _media_device_capabilities_pb2.VideoCapabilities.Ptz
        def __init__(self, ptz: _Optional[_Union[_media_device_capabilities_pb2.VideoCapabilities.Ptz, _Mapping]] = ...) -> None: ...
    class VideoSettings(_message.Message):
        __slots__ = ("main_resolution",)
        MAIN_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        main_resolution: _types_pb2.VideoResolution
        def __init__(self, main_resolution: _Optional[_Union[_types_pb2.VideoResolution, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_info: _channel_pb2.MediaDeviceInfo
    audio_output_settings: PlayerChannel.AudioOutputSettings
    video_capabilities: PlayerChannel.VideoCapabilities
    video_settings: PlayerChannel.VideoSettings
    audio_settings: PlayerChannel.AudioSettings
    cloud_archive: _cloud_archive_pb2.CloudArchive
    def __init__(self, id: _Optional[str] = ..., device_info: _Optional[_Union[_channel_pb2.MediaDeviceInfo, _Mapping]] = ..., audio_output_settings: _Optional[_Union[PlayerChannel.AudioOutputSettings, _Mapping]] = ..., video_capabilities: _Optional[_Union[PlayerChannel.VideoCapabilities, _Mapping]] = ..., video_settings: _Optional[_Union[PlayerChannel.VideoSettings, _Mapping]] = ..., audio_settings: _Optional[_Union[PlayerChannel.AudioSettings, _Mapping]] = ..., cloud_archive: _Optional[_Union[_cloud_archive_pb2.CloudArchive, _Mapping]] = ...) -> None: ...
