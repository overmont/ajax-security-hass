from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_color_pb2 as _hub_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_type_pb2 as _hub_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubInSpaceInfo(_message.Message):
    __slots__ = ("id", "name", "type", "color", "device_label", "box_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _hub_type_pb2.HubType
    color: _hub_color_pb2.HubColor
    device_label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_hub_type_pb2.HubType, str]] = ..., color: _Optional[_Union[_hub_color_pb2.HubColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ...) -> None: ...
