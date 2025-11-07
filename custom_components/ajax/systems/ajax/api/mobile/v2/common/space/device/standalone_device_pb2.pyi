from systems.ajax.api.mobile.v2.common.space.device import hub_pb2 as _hub_pb2
from systems.ajax.api.mobile.v2.common.space.device import passive_hub_pb2 as _passive_hub_pb2
from systems.ajax.api.mobile.v2.common.space.device import smart_lock_device_pb2 as _smart_lock_device_pb2
from systems.ajax.api.mobile.v2.common.space.device import video_edge_pb2 as _video_edge_pb2
from systems.ajax.api.mobile.v2.common.space.device import vaelsys_camera_pb2 as _vaelsys_camera_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StandaloneDevice(_message.Message):
    __slots__ = ("hub", "video_edge", "passive_hub", "smart_lock", "vaelsys_camera", "sorting_key")
    HUB_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_HUB_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    VAELSYS_CAMERA_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    hub: _hub_pb2.Hub
    video_edge: _video_edge_pb2.VideoEdge
    passive_hub: _passive_hub_pb2.PassiveHub
    smart_lock: _smart_lock_device_pb2.SmartLockDevice
    vaelsys_camera: _vaelsys_camera_pb2.VaelsysCamera
    sorting_key: str
    def __init__(self, hub: _Optional[_Union[_hub_pb2.Hub, _Mapping]] = ..., video_edge: _Optional[_Union[_video_edge_pb2.VideoEdge, _Mapping]] = ..., passive_hub: _Optional[_Union[_passive_hub_pb2.PassiveHub, _Mapping]] = ..., smart_lock: _Optional[_Union[_smart_lock_device_pb2.SmartLockDevice, _Mapping]] = ..., vaelsys_camera: _Optional[_Union[_vaelsys_camera_pb2.VaelsysCamera, _Mapping]] = ..., sorting_key: _Optional[str] = ...) -> None: ...
