from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorProtect(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "reed_closed", "extra_contact_closed", "always_active", "extra_contact_aware", "reed_contact_aware", "chime_triggers", "chime_signal", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[DoorProtect.SirenTrigger]
        REED: _ClassVar[DoorProtect.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[DoorProtect.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: DoorProtect.SirenTrigger
    REED: DoorProtect.SirenTrigger
    EXTRA_CONTACT: DoorProtect.SirenTrigger
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[DoorProtect.ChimeTrigger]
        CHIME_REED: _ClassVar[DoorProtect.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[DoorProtect.ChimeTrigger]
    NO_CHIME_TRIGGER_INFO: DoorProtect.ChimeTrigger
    CHIME_REED: DoorProtect.ChimeTrigger
    CHIME_EXTRA_CONTACT: DoorProtect.ChimeTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[DoorProtect.Subtype]
    NO_SUBTYPE: DoorProtect.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    REED_CLOSED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_CLOSED_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_AWARE_FIELD_NUMBER: _ClassVar[int]
    REED_CONTACT_AWARE_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[DoorProtect.SirenTrigger]
    reed_closed: _wrappers_pb2.BoolValue
    extra_contact_closed: _wrappers_pb2.BoolValue
    always_active: bool
    extra_contact_aware: bool
    reed_contact_aware: bool
    chime_triggers: _containers.RepeatedScalarFieldContainer[DoorProtect.ChimeTrigger]
    chime_signal: int
    subtype: DoorProtect.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[DoorProtect.SirenTrigger, str]]] = ..., reed_closed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., extra_contact_closed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., always_active: bool = ..., extra_contact_aware: bool = ..., reed_contact_aware: bool = ..., chime_triggers: _Optional[_Iterable[_Union[DoorProtect.ChimeTrigger, str]]] = ..., chime_signal: _Optional[int] = ..., subtype: _Optional[_Union[DoorProtect.Subtype, str]] = ...) -> None: ...
