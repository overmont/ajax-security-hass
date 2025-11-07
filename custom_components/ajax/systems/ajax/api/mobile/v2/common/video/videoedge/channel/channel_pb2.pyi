from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import calendar_pb2 as _calendar_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import cloud_archive_pb2 as _cloud_archive_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.spacesettings import channel_space_settings_pb2 as _channel_space_settings_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CS_NONE: _ClassVar[ChannelState]
    ONLINE: _ClassVar[ChannelState]
    RECORDING: _ClassVar[ChannelState]
    HAVE_ARCHIVE: _ClassVar[ChannelState]
    HAVE_DETECTION: _ClassVar[ChannelState]
    HAVE_MOTION: _ClassVar[ChannelState]
    HAVE_SOUND: _ClassVar[ChannelState]
    HAVE_ALARM: _ClassVar[ChannelState]
    HAVE_OBJECTS: _ClassVar[ChannelState]
    FLICKERING: _ClassVar[ChannelState]
    HAVE_PIR_MOTION: _ClassVar[ChannelState]
    HAVE_RING: _ClassVar[ChannelState]
CS_NONE: ChannelState
ONLINE: ChannelState
RECORDING: ChannelState
HAVE_ARCHIVE: ChannelState
HAVE_DETECTION: ChannelState
HAVE_MOTION: ChannelState
HAVE_SOUND: ChannelState
HAVE_ALARM: ChannelState
HAVE_OBJECTS: ChannelState
FLICKERING: ChannelState
HAVE_PIR_MOTION: ChannelState
HAVE_RING: ChannelState

class Channel(_message.Message):
    __slots__ = ("guid", "device_info", "info", "state", "record_mode", "channel_preview", "calendar", "record_policy", "zombie", "cloud_archive", "smart_backlight_trigger_settings", "room_id", "group_id", "space_settings", "source_aliases")
    GUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    ZOMBIE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    SMART_BACKLIGHT_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ALIASES_FIELD_NUMBER: _ClassVar[int]
    guid: str
    device_info: MediaDeviceInfo
    info: ChannelInfo
    state: _containers.RepeatedScalarFieldContainer[ChannelState]
    record_mode: _archive_pb2.RecordMode
    channel_preview: ChannelPreview
    calendar: _calendar_pb2.Calendar
    record_policy: _archive_pb2.RecordPolicy
    zombie: bool
    cloud_archive: _cloud_archive_pb2.CloudArchive
    smart_backlight_trigger_settings: SmartBacklightTriggerSettings
    room_id: str
    group_id: str
    space_settings: _channel_space_settings_pb2.ChannelSpaceSettings
    source_aliases: SourceAliases
    def __init__(self, guid: _Optional[str] = ..., device_info: _Optional[_Union[MediaDeviceInfo, _Mapping]] = ..., info: _Optional[_Union[ChannelInfo, _Mapping]] = ..., state: _Optional[_Iterable[_Union[ChannelState, str]]] = ..., record_mode: _Optional[_Union[_archive_pb2.RecordMode, str]] = ..., channel_preview: _Optional[_Union[ChannelPreview, _Mapping]] = ..., calendar: _Optional[_Union[_calendar_pb2.Calendar, _Mapping]] = ..., record_policy: _Optional[_Union[_archive_pb2.RecordPolicy, str]] = ..., zombie: bool = ..., cloud_archive: _Optional[_Union[_cloud_archive_pb2.CloudArchive, _Mapping]] = ..., smart_backlight_trigger_settings: _Optional[_Union[SmartBacklightTriggerSettings, _Mapping]] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., space_settings: _Optional[_Union[_channel_space_settings_pb2.ChannelSpaceSettings, _Mapping]] = ..., source_aliases: _Optional[_Union[SourceAliases, _Mapping]] = ...) -> None: ...

class MediaDeviceInfo(_message.Message):
    __slots__ = ("media_device_guid", "channel_id")
    MEDIA_DEVICE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    media_device_guid: str
    channel_id: str
    def __init__(self, media_device_guid: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ChannelInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ChannelPreview(_message.Message):
    __slots__ = ("image_url", "created_at")
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, image_url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SourceAliases(_message.Message):
    __slots__ = ("sources",)
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[VideoSource]
    def __init__(self, sources: _Optional[_Iterable[_Union[VideoSource, _Mapping]]] = ...) -> None: ...

class VideoSource(_message.Message):
    __slots__ = ("primary_source", "nvr_source", "cloud_archive_source")
    PRIMARY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NVR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    primary_source: PrimarySource
    nvr_source: NvrSource
    cloud_archive_source: CloudArchiveSource
    def __init__(self, primary_source: _Optional[_Union[PrimarySource, _Mapping]] = ..., nvr_source: _Optional[_Union[NvrSource, _Mapping]] = ..., cloud_archive_source: _Optional[_Union[CloudArchiveSource, _Mapping]] = ...) -> None: ...

class PrimarySource(_message.Message):
    __slots__ = ("video_edge_id", "channel_id", "type", "color")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    type: _about_pb2.About.Type
    color: _about_pb2.About.Color
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., type: _Optional[_Union[_about_pb2.About.Type, str]] = ..., color: _Optional[_Union[_about_pb2.About.Color, str]] = ...) -> None: ...

class NvrSource(_message.Message):
    __slots__ = ("video_edge_id", "channel_id", "type")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    type: _about_pb2.About.Type
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., type: _Optional[_Union[_about_pb2.About.Type, str]] = ...) -> None: ...

class CloudArchiveSource(_message.Message):
    __slots__ = ("video_edge_id", "channel_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class SmartBacklightTriggerTypeSettings(_message.Message):
    __slots__ = ("enabled", "motion", "object")
    class Motion(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Object(_message.Message):
        __slots__ = ("object_class",)
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        object_class: _types_pb2.ObjectClass
        def __init__(self, object_class: _Optional[_Union[_types_pb2.ObjectClass, str]] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    motion: SmartBacklightTriggerTypeSettings.Motion
    object: SmartBacklightTriggerTypeSettings.Object
    def __init__(self, enabled: bool = ..., motion: _Optional[_Union[SmartBacklightTriggerTypeSettings.Motion, _Mapping]] = ..., object: _Optional[_Union[SmartBacklightTriggerTypeSettings.Object, _Mapping]] = ...) -> None: ...

class SmartBacklightTriggerSettings(_message.Message):
    __slots__ = ("smart_backlight_trigger_types",)
    SMART_BACKLIGHT_TRIGGER_TYPES_FIELD_NUMBER: _ClassVar[int]
    smart_backlight_trigger_types: _containers.RepeatedCompositeFieldContainer[SmartBacklightTriggerTypeSettings]
    def __init__(self, smart_backlight_trigger_types: _Optional[_Iterable[_Union[SmartBacklightTriggerTypeSettings, _Mapping]]] = ...) -> None: ...
