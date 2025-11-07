from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_type_pb2 as _source_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("type", "hex_id", "name", "room_name", "room_id", "device_color")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.HubNotificationSourceType
    hex_id: str
    name: str
    room_name: str
    room_id: str
    device_color: _device_color_pb2.DeviceColor
    def __init__(self, type: _Optional[_Union[_source_type_pb2.HubNotificationSourceType, str]] = ..., hex_id: _Optional[str] = ..., name: _Optional[str] = ..., room_name: _Optional[str] = ..., room_id: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ...) -> None: ...
