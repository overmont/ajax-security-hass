from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import video_edge_type_pb2 as _video_edge_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeInSpaceInfo(_message.Message):
    __slots__ = ("id", "name", "type", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _video_edge_type_pb2.VideoEdgeType
    color: _device_color_pb2.DeviceColor
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_video_edge_type_pb2.VideoEdgeType, str]] = ..., color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ...) -> None: ...
