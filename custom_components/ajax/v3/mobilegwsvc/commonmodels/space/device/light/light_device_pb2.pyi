from v3.mobilegwsvc.commonmodels.hub.device.light import light_hub_device_pb2 as _light_hub_device_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.light import light_video_edge_pb2 as _light_video_edge_pb2
from v3.mobilegwsvc.commonmodels.space.smartlock.light import light_smart_lock_pb2 as _light_smart_lock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightDevice(_message.Message):
    __slots__ = ("hub_device", "video_edge", "video_edge_channel", "smart_lock")
    HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    hub_device: _light_hub_device_pb2.LightHubDevice
    video_edge: _light_video_edge_pb2.LightVideoEdge
    video_edge_channel: _light_video_edge_pb2.LightVideoEdgeChannel
    smart_lock: _light_smart_lock_pb2.LightSmartLock
    def __init__(self, hub_device: _Optional[_Union[_light_hub_device_pb2.LightHubDevice, _Mapping]] = ..., video_edge: _Optional[_Union[_light_video_edge_pb2.LightVideoEdge, _Mapping]] = ..., video_edge_channel: _Optional[_Union[_light_video_edge_pb2.LightVideoEdgeChannel, _Mapping]] = ..., smart_lock: _Optional[_Union[_light_smart_lock_pb2.LightSmartLock, _Mapping]] = ...) -> None: ...
