from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_sensor_settings_pb2 as _device_sensor_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FastTamperPart(_message.Message):
    __slots__ = ("fast_tamper_settings", "capabilities")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[FastTamperPart.Capability]
        CAPABILITY_FAST_TAMPER: _ClassVar[FastTamperPart.Capability]
    CAPABILITY_UNSPECIFIED: FastTamperPart.Capability
    CAPABILITY_FAST_TAMPER: FastTamperPart.Capability
    FAST_TAMPER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    fast_tamper_settings: _device_sensor_settings_pb2.FastTamperSettings
    capabilities: _containers.RepeatedScalarFieldContainer[FastTamperPart.Capability]
    def __init__(self, fast_tamper_settings: _Optional[_Union[_device_sensor_settings_pb2.FastTamperSettings, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[FastTamperPart.Capability, str]]] = ...) -> None: ...
