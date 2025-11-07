from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtect(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "sensitivity", "always_active", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtect.SirenTrigger]
        MOTION: _ClassVar[MotionProtect.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: MotionProtect.SirenTrigger
    MOTION: MotionProtect.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtect.Subtype]
    NO_SUBTYPE: MotionProtect.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[MotionProtect.SirenTrigger]
    sensitivity: int
    always_active: bool
    subtype: MotionProtect.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[MotionProtect.SirenTrigger, str]]] = ..., sensitivity: _Optional[int] = ..., always_active: bool = ..., subtype: _Optional[_Union[MotionProtect.Subtype, str]] = ...) -> None: ...
