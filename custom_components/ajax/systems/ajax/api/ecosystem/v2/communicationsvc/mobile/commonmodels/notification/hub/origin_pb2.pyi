from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_type_pb2 as _hub_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubOrigin(_message.Message):
    __slots__ = ("hex_id", "name", "color", "type", "label", "box_type")
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    name: str
    color: _device_color_pb2.DeviceColor
    type: _hub_type_pb2.HubType
    label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(self, hex_id: _Optional[str] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., type: _Optional[_Union[_hub_type_pb2.HubType, str]] = ..., label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ...) -> None: ...
