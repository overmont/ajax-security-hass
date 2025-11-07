from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_transmission_power_mode_pb2 as _device_transmission_power_mode_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSetDeviceTransmissionPowerModeRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "mode")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    mode: _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., mode: _Optional[_Union[_device_transmission_power_mode_pb2.DeviceTransmissionPowerMode, str]] = ...) -> None: ...
