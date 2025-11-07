from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge import video_edge_pb2 as _video_edge_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelSourceSettings(_message.Message):
    __slots__ = ("nvr_source_settings",)
    NVR_SOURCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    nvr_source_settings: NvrSourceSettings
    def __init__(self, nvr_source_settings: _Optional[_Union[NvrSourceSettings, _Mapping]] = ...) -> None: ...

class NvrSourceSettings(_message.Message):
    __slots__ = ("video_edge_id", "channel_id", "video_edge_name", "video_edge_connection_state", "record_mode", "record_policy", "storage_devices", "channel_states", "media_device_id")
    class StorageDevice(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STATES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    video_edge_name: str
    video_edge_connection_state: _video_edge_pb2.ConnectionState
    record_mode: _archive_pb2.RecordMode
    record_policy: _archive_pb2.RecordPolicy
    storage_devices: _containers.RepeatedCompositeFieldContainer[NvrSourceSettings.StorageDevice]
    channel_states: _containers.RepeatedScalarFieldContainer[_channel_pb2.ChannelState]
    media_device_id: str
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., video_edge_name: _Optional[str] = ..., video_edge_connection_state: _Optional[_Union[_video_edge_pb2.ConnectionState, str]] = ..., record_mode: _Optional[_Union[_archive_pb2.RecordMode, str]] = ..., record_policy: _Optional[_Union[_archive_pb2.RecordPolicy, str]] = ..., storage_devices: _Optional[_Iterable[_Union[NvrSourceSettings.StorageDevice, _Mapping]]] = ..., channel_states: _Optional[_Iterable[_Union[_channel_pb2.ChannelState, str]]] = ..., media_device_id: _Optional[str] = ...) -> None: ...
