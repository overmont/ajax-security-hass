from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_type_pb2 as _hub_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubInfo(_message.Message):
    __slots__ = ("color", "device_label", "box_type", "hub_type")
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    HUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    hub_type: _hub_type_pb2.HubType
    def __init__(self, color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ..., hub_type: _Optional[_Union[_hub_type_pb2.HubType, str]] = ...) -> None: ...
