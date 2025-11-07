from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceId(_message.Message):
    __slots__ = ("hub_light_device_id", "video_edge_id", "video_edge_channel_reference", "smart_lock_id")
    class HubLightDeviceId(_message.Message):
        __slots__ = ("device_id", "hub_id")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        hub_id: str
        def __init__(self, device_id: _Optional[str] = ..., hub_id: _Optional[str] = ...) -> None: ...
    class VideoEdgeId(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class VideoEdgeChannelReference(_message.Message):
        __slots__ = ("video_edge_id", "channel_id")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_id: str
        def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...
    class SmartLockId(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    HUB_LIGHT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    hub_light_device_id: LightDeviceId.HubLightDeviceId
    video_edge_id: LightDeviceId.VideoEdgeId
    video_edge_channel_reference: LightDeviceId.VideoEdgeChannelReference
    smart_lock_id: LightDeviceId.SmartLockId
    def __init__(self, hub_light_device_id: _Optional[_Union[LightDeviceId.HubLightDeviceId, _Mapping]] = ..., video_edge_id: _Optional[_Union[LightDeviceId.VideoEdgeId, _Mapping]] = ..., video_edge_channel_reference: _Optional[_Union[LightDeviceId.VideoEdgeChannelReference, _Mapping]] = ..., smart_lock_id: _Optional[_Union[LightDeviceId.SmartLockId, _Mapping]] = ...) -> None: ...
