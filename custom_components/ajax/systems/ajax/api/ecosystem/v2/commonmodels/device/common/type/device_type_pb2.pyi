from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.api.internal.v2.commonmodels.videoedge import video_edge_family_pb2 as _video_edge_family_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(_message.Message):
    __slots__ = ("hub_device_type", "video_edge_type", "video_channel_type", "smart_lock_type")
    HUB_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_device_type: HubDeviceType
    video_edge_type: VideoEdgeType
    video_channel_type: VideoChannelType
    smart_lock_type: SmartLockType
    def __init__(self, hub_device_type: _Optional[_Union[HubDeviceType, _Mapping]] = ..., video_edge_type: _Optional[_Union[VideoEdgeType, _Mapping]] = ..., video_channel_type: _Optional[_Union[VideoChannelType, _Mapping]] = ..., smart_lock_type: _Optional[_Union[SmartLockType, _Mapping]] = ...) -> None: ...

class HubDeviceType(_message.Message):
    __slots__ = ("object_type",)
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_type: _object_type_pb2.ObjectType
    def __init__(self, object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...

class VideoEdgeType(_message.Message):
    __slots__ = ("video_edge_family",)
    VIDEO_EDGE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    video_edge_family: _video_edge_family_pb2.VideoEdgeFamily
    def __init__(self, video_edge_family: _Optional[_Union[_video_edge_family_pb2.VideoEdgeFamily, str]] = ...) -> None: ...

class VideoChannelType(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockType(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
