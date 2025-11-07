from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDeviceBypassRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "object_type", "bypass_type")
    class Bypass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BYPASS_UNSPECIFIED: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ENGINEERING_DISABLE: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ENGINEERING_SENSOR: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ENGINEERING_TAMPER: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ONE_TIME_DISABLE: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ONE_TIME_SENSOR: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
        BYPASS_ONE_TIME_TAMPER: _ClassVar[DeviceCommandDeviceBypassRequest.Bypass]
    BYPASS_UNSPECIFIED: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ENGINEERING_DISABLE: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ENGINEERING_SENSOR: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ENGINEERING_TAMPER: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ONE_TIME_DISABLE: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ONE_TIME_SENSOR: DeviceCommandDeviceBypassRequest.Bypass
    BYPASS_ONE_TIME_TAMPER: DeviceCommandDeviceBypassRequest.Bypass
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    bypass_type: DeviceCommandDeviceBypassRequest.Bypass
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., bypass_type: _Optional[_Union[DeviceCommandDeviceBypassRequest.Bypass, str]] = ...) -> None: ...
