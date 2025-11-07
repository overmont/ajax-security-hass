from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import sensitivity_pb2 as _sensitivity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensitivityPart(_message.Message):
    __slots__ = ("sensitivity", "capabilities")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[SensitivityPart.Capability]
        CAPABILITY_INSERT_SENSITIVITY: _ClassVar[SensitivityPart.Capability]
    CAPABILITY_UNSPECIFIED: SensitivityPart.Capability
    CAPABILITY_INSERT_SENSITIVITY: SensitivityPart.Capability
    class SensitivitySettings(_message.Message):
        __slots__ = ("sensitivity",)
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        sensitivity: _sensitivity_pb2.Sensitivity
        def __init__(self, sensitivity: _Optional[_Union[_sensitivity_pb2.Sensitivity, str]] = ...) -> None: ...
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    sensitivity: _sensitivity_pb2.Sensitivity
    capabilities: _containers.RepeatedScalarFieldContainer[SensitivityPart.Capability]
    def __init__(self, sensitivity: _Optional[_Union[_sensitivity_pb2.Sensitivity, str]] = ..., capabilities: _Optional[_Iterable[_Union[SensitivityPart.Capability, str]]] = ...) -> None: ...
