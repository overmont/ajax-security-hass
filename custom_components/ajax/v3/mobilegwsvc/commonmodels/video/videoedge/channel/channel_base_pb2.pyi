from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import cloud_archive_pb2 as _cloud_archive_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelBase(_message.Message):
    __slots__ = ("id", "device_info", "info", "state", "record_mode", "record_policy", "zombie", "cloud_archive", "smart_backlight_trigger_settings")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    ZOMBIE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    SMART_BACKLIGHT_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_info: _channel_pb2.MediaDeviceInfo
    info: _channel_pb2.ChannelInfo
    state: _containers.RepeatedScalarFieldContainer[_channel_pb2.ChannelState]
    record_mode: _archive_pb2.RecordMode
    record_policy: _archive_pb2.RecordPolicy
    zombie: bool
    cloud_archive: _cloud_archive_pb2.CloudArchive
    smart_backlight_trigger_settings: _channel_pb2.SmartBacklightTriggerSettings
    def __init__(self, id: _Optional[str] = ..., device_info: _Optional[_Union[_channel_pb2.MediaDeviceInfo, _Mapping]] = ..., info: _Optional[_Union[_channel_pb2.ChannelInfo, _Mapping]] = ..., state: _Optional[_Iterable[_Union[_channel_pb2.ChannelState, str]]] = ..., record_mode: _Optional[_Union[_archive_pb2.RecordMode, str]] = ..., record_policy: _Optional[_Union[_archive_pb2.RecordPolicy, str]] = ..., zombie: bool = ..., cloud_archive: _Optional[_Union[_cloud_archive_pb2.CloudArchive, _Mapping]] = ..., smart_backlight_trigger_settings: _Optional[_Union[_channel_pb2.SmartBacklightTriggerSettings, _Mapping]] = ...) -> None: ...
