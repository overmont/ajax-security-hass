from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_appearance_pb2 as _device_appearance_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import custom_alarm_type_pb2 as _custom_alarm_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import yavir_access_control_type_pb2 as _yavir_access_control_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubDeviceViewSource(_message.Message):
    __slots__ = ("device_type", "device_hex_id", "name", "device_color", "device_label", "yavir_access_control_type", "custom_alarm_type", "device_appearance_type", "room_hex_id", "room_name")
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    YAVIR_ACCESS_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    device_type: _object_type_pb2.ObjectType
    device_hex_id: str
    name: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    yavir_access_control_type: _yavir_access_control_type_pb2.YavirAccessControlType
    custom_alarm_type: _custom_alarm_type_pb2.CustomAlarmType
    device_appearance_type: _device_appearance_pb2.DeviceAppearance.DeviceAppearanceType
    room_hex_id: str
    room_name: str
    def __init__(self, device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., device_hex_id: _Optional[str] = ..., name: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., yavir_access_control_type: _Optional[_Union[_yavir_access_control_type_pb2.YavirAccessControlType, str]] = ..., custom_alarm_type: _Optional[_Union[_custom_alarm_type_pb2.CustomAlarmType, str]] = ..., device_appearance_type: _Optional[_Union[_device_appearance_pb2.DeviceAppearance.DeviceAppearanceType, str]] = ..., room_hex_id: _Optional[str] = ..., room_name: _Optional[str] = ...) -> None: ...
