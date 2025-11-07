from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_color_pb2 as _device_color_pb2
from systems.ajax.api.mobile.v2.common.hub import hub_box_type_pb2 as _hub_box_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubBoxAppearance(_message.Message):
    __slots__ = ("box_color", "box_type")
    BOX_COLOR_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    box_color: _device_color_pb2.DeviceColor
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(self, box_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ...) -> None: ...
