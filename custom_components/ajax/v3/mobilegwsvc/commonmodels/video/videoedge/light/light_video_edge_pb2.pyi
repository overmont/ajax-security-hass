from v3.mobilegwsvc.commonmodels.space.device.light import light_device_profile_pb2 as _light_device_profile_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from v3.mobilegwsvc.commonmodels.space.device.light.properties import subscription_state_pb2 as _subscription_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightVideoEdge(_message.Message):
    __slots__ = ("profile", "spread_properties", "video_edge_properties")
    class SpreadProperties(_message.Message):
        __slots__ = ("id", "sort_index", "channels", "subscription_state")
        class Channels(_message.Message):
            __slots__ = ("total_count", "online_count")
            TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
            ONLINE_COUNT_FIELD_NUMBER: _ClassVar[int]
            total_count: int
            online_count: int
            def __init__(self, total_count: _Optional[int] = ..., online_count: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        SORT_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_STATE_FIELD_NUMBER: _ClassVar[int]
        id: str
        sort_index: int
        channels: LightVideoEdge.SpreadProperties.Channels
        subscription_state: _subscription_state_pb2.SubscriptionState
        def __init__(self, id: _Optional[str] = ..., sort_index: _Optional[int] = ..., channels: _Optional[_Union[LightVideoEdge.SpreadProperties.Channels, _Mapping]] = ..., subscription_state: _Optional[_Union[_subscription_state_pb2.SubscriptionState, _Mapping]] = ...) -> None: ...
    class VideoEdgeProperties(_message.Message):
        __slots__ = ("video_edge_type", "channels_number")
        VIDEO_EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_NUMBER_FIELD_NUMBER: _ClassVar[int]
        video_edge_type: _about_pb2.About.Type
        channels_number: int
        def __init__(self, video_edge_type: _Optional[_Union[_about_pb2.About.Type, str]] = ..., channels_number: _Optional[int] = ...) -> None: ...
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    profile: _light_device_profile_pb2.LightDeviceProfile
    spread_properties: _containers.RepeatedCompositeFieldContainer[LightVideoEdge.SpreadProperties]
    video_edge_properties: LightVideoEdge.VideoEdgeProperties
    def __init__(self, profile: _Optional[_Union[_light_device_profile_pb2.LightDeviceProfile, _Mapping]] = ..., spread_properties: _Optional[_Iterable[_Union[LightVideoEdge.SpreadProperties, _Mapping]]] = ..., video_edge_properties: _Optional[_Union[LightVideoEdge.VideoEdgeProperties, _Mapping]] = ...) -> None: ...

class LightVideoEdgeChannel(_message.Message):
    __slots__ = ("profile", "video_edge_channel_properties", "spread_properties")
    class VideoEdgeChannelProperties(_message.Message):
        __slots__ = ("video_edge_type", "source_aliases", "backup_channel_properties", "video_edge_id")
        VIDEO_EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ALIASES_FIELD_NUMBER: _ClassVar[int]
        BACKUP_CHANNEL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        video_edge_type: _about_pb2.About.Type
        source_aliases: _channel_pb2.SourceAliases
        backup_channel_properties: LightVideoEdgeChannel.BackupChannelProperties
        video_edge_id: str
        def __init__(self, video_edge_type: _Optional[_Union[_about_pb2.About.Type, str]] = ..., source_aliases: _Optional[_Union[_channel_pb2.SourceAliases, _Mapping]] = ..., backup_channel_properties: _Optional[_Union[LightVideoEdgeChannel.BackupChannelProperties, _Mapping]] = ..., video_edge_id: _Optional[str] = ...) -> None: ...
    class BackupChannelProperties(_message.Message):
        __slots__ = ("hub_id",)
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        def __init__(self, hub_id: _Optional[str] = ...) -> None: ...
    class SpreadProperties(_message.Message):
        __slots__ = ("id", "sort_index", "subscription_state")
        ID_FIELD_NUMBER: _ClassVar[int]
        SORT_INDEX_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_STATE_FIELD_NUMBER: _ClassVar[int]
        id: str
        sort_index: int
        subscription_state: _subscription_state_pb2.SubscriptionState
        def __init__(self, id: _Optional[str] = ..., sort_index: _Optional[int] = ..., subscription_state: _Optional[_Union[_subscription_state_pb2.SubscriptionState, _Mapping]] = ...) -> None: ...
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    profile: _light_device_profile_pb2.LightDeviceProfile
    video_edge_channel_properties: LightVideoEdgeChannel.VideoEdgeChannelProperties
    spread_properties: _containers.RepeatedCompositeFieldContainer[LightVideoEdgeChannel.SpreadProperties]
    def __init__(self, profile: _Optional[_Union[_light_device_profile_pb2.LightDeviceProfile, _Mapping]] = ..., video_edge_channel_properties: _Optional[_Union[LightVideoEdgeChannel.VideoEdgeChannelProperties, _Mapping]] = ..., spread_properties: _Optional[_Iterable[_Union[LightVideoEdgeChannel.SpreadProperties, _Mapping]]] = ...) -> None: ...
