from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtectCurtain(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "sensitivity", "always_active", "pet_immunity", "antimasking", "masked", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtectCurtain.SirenTrigger]
        MOTION: _ClassVar[MotionProtectCurtain.SirenTrigger]
        ANTIMASKING: _ClassVar[MotionProtectCurtain.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: MotionProtectCurtain.SirenTrigger
    MOTION: MotionProtectCurtain.SirenTrigger
    ANTIMASKING: MotionProtectCurtain.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtectCurtain.Subtype]
    NO_SUBTYPE: MotionProtectCurtain.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PET_IMMUNITY_FIELD_NUMBER: _ClassVar[int]
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    MASKED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[MotionProtectCurtain.SirenTrigger]
    sensitivity: int
    always_active: bool
    pet_immunity: bool
    antimasking: bool
    masked: _wrappers_pb2.BoolValue
    subtype: MotionProtectCurtain.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[MotionProtectCurtain.SirenTrigger, str]]] = ..., sensitivity: _Optional[int] = ..., always_active: bool = ..., pet_immunity: bool = ..., antimasking: bool = ..., masked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., subtype: _Optional[_Union[MotionProtectCurtain.Subtype, str]] = ...) -> None: ...
