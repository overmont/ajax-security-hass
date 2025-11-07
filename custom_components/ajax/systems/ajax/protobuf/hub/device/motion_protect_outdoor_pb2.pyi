from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtectOutdoor(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "sensitivity", "always_active", "antimasking", "masked", "externally_powered", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtectOutdoor.SirenTrigger]
        MOTION: _ClassVar[MotionProtectOutdoor.SirenTrigger]
        ANTIMASKING: _ClassVar[MotionProtectOutdoor.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: MotionProtectOutdoor.SirenTrigger
    MOTION: MotionProtectOutdoor.SirenTrigger
    ANTIMASKING: MotionProtectOutdoor.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtectOutdoor.Subtype]
    NO_SUBTYPE: MotionProtectOutdoor.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    MASKED_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[MotionProtectOutdoor.SirenTrigger]
    sensitivity: int
    always_active: bool
    antimasking: bool
    masked: _wrappers_pb2.BoolValue
    externally_powered: _wrappers_pb2.BoolValue
    subtype: MotionProtectOutdoor.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[MotionProtectOutdoor.SirenTrigger, str]]] = ..., sensitivity: _Optional[int] = ..., always_active: bool = ..., antimasking: bool = ..., masked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., externally_powered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., subtype: _Optional[_Union[MotionProtectOutdoor.Subtype, str]] = ...) -> None: ...
