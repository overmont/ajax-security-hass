from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import source_type_pb2 as _source_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import video_edge_type_pb2 as _video_edge_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "room_hex_id", "room_name", "device_color", "video_edge_type", "image_info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.VideoNotificationSourceType
    id: str
    name: str
    room_hex_id: str
    room_name: str
    device_color: _device_color_pb2.DeviceColor
    video_edge_type: _video_edge_type_pb2.VideoEdgeType
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(self, type: _Optional[_Union[_source_type_pb2.VideoNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., room_hex_id: _Optional[str] = ..., room_name: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., video_edge_type: _Optional[_Union[_video_edge_type_pb2.VideoEdgeType, str]] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ...) -> None: ...
