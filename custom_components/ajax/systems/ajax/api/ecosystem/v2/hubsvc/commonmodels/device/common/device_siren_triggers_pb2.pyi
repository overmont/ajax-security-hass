from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import patch_type_pb2 as _patch_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SirenTriggers(_message.Message):
    __slots__ = ("settings", "siren_trigger_capabilities")
    class Trigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_UNSPECIFIED: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TAMPER: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_REED: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_EXTRA: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_EXTRA2: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_EXTRA3: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_MOTION: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_GLASS: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TEMPERATURE: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TEMPERATURE_DIFF: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SMOKE: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_CO: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_LEAK: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_ACCEL: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TILT: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SECURITY_BUTTON: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SHOCK: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SHORT_CIRCUIT: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SHUTTER_ALARM: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SHUTTER_ONLINE: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_ANTIMASKING: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TEMP_WARNING: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_TEMP_CRITICAL: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_FLAME_DETECTED: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_MOTION_LEFT_PIR: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_MOTION_RIGHT_PIR: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_ANTIMASKING_LEFT_PIR: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_ANTIMASKING_RIGHT_PIR: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_CCO: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_FIRE_ALARM: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_MEDICAL_ALARM: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_CSMOKE: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_SEISMIC: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_CASE_BREAK: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_OVERHEAT: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_ENTRY_DELAY: _ClassVar[SirenTriggers.Trigger]
        TRIGGER_POWER_SUPPLY_SHORTED_OUT: _ClassVar[SirenTriggers.Trigger]
    TRIGGER_UNSPECIFIED: SirenTriggers.Trigger
    TRIGGER_TAMPER: SirenTriggers.Trigger
    TRIGGER_REED: SirenTriggers.Trigger
    TRIGGER_EXTRA: SirenTriggers.Trigger
    TRIGGER_EXTRA2: SirenTriggers.Trigger
    TRIGGER_EXTRA3: SirenTriggers.Trigger
    TRIGGER_MOTION: SirenTriggers.Trigger
    TRIGGER_GLASS: SirenTriggers.Trigger
    TRIGGER_TEMPERATURE: SirenTriggers.Trigger
    TRIGGER_TEMPERATURE_DIFF: SirenTriggers.Trigger
    TRIGGER_SMOKE: SirenTriggers.Trigger
    TRIGGER_CO: SirenTriggers.Trigger
    TRIGGER_LEAK: SirenTriggers.Trigger
    TRIGGER_ACCEL: SirenTriggers.Trigger
    TRIGGER_TILT: SirenTriggers.Trigger
    TRIGGER_SECURITY_BUTTON: SirenTriggers.Trigger
    TRIGGER_SHOCK: SirenTriggers.Trigger
    TRIGGER_SHORT_CIRCUIT: SirenTriggers.Trigger
    TRIGGER_SHUTTER_ALARM: SirenTriggers.Trigger
    TRIGGER_SHUTTER_ONLINE: SirenTriggers.Trigger
    TRIGGER_ANTIMASKING: SirenTriggers.Trigger
    TRIGGER_TEMP_WARNING: SirenTriggers.Trigger
    TRIGGER_TEMP_CRITICAL: SirenTriggers.Trigger
    TRIGGER_FLAME_DETECTED: SirenTriggers.Trigger
    TRIGGER_MOTION_LEFT_PIR: SirenTriggers.Trigger
    TRIGGER_MOTION_RIGHT_PIR: SirenTriggers.Trigger
    TRIGGER_ANTIMASKING_LEFT_PIR: SirenTriggers.Trigger
    TRIGGER_ANTIMASKING_RIGHT_PIR: SirenTriggers.Trigger
    TRIGGER_CCO: SirenTriggers.Trigger
    TRIGGER_FIRE_ALARM: SirenTriggers.Trigger
    TRIGGER_MEDICAL_ALARM: SirenTriggers.Trigger
    TRIGGER_CSMOKE: SirenTriggers.Trigger
    TRIGGER_SEISMIC: SirenTriggers.Trigger
    TRIGGER_CASE_BREAK: SirenTriggers.Trigger
    TRIGGER_OVERHEAT: SirenTriggers.Trigger
    TRIGGER_ENTRY_DELAY: SirenTriggers.Trigger
    TRIGGER_POWER_SUPPLY_SHORTED_OUT: SirenTriggers.Trigger
    class SirenTriggerSettings(_message.Message):
        __slots__ = ("siren_triggers",)
        SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        siren_triggers: _containers.RepeatedCompositeFieldContainer[SirenTriggers.SirenTriggerPatch]
        def __init__(self, siren_triggers: _Optional[_Iterable[_Union[SirenTriggers.SirenTriggerPatch, _Mapping]]] = ...) -> None: ...
    class SirenTriggerPatch(_message.Message):
        __slots__ = ("type", "trigger")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        type: _patch_type_pb2.PatchType
        trigger: SirenTriggers.Trigger
        def __init__(self, type: _Optional[_Union[_patch_type_pb2.PatchType, str]] = ..., trigger: _Optional[_Union[SirenTriggers.Trigger, str]] = ...) -> None: ...
    class EnabledSirenTriggers(_message.Message):
        __slots__ = ("enabled_triggers",)
        ENABLED_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        enabled_triggers: _containers.RepeatedScalarFieldContainer[SirenTriggers.Trigger]
        def __init__(self, enabled_triggers: _Optional[_Iterable[_Union[SirenTriggers.Trigger, str]]] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    settings: SirenTriggers.EnabledSirenTriggers
    siren_trigger_capabilities: _containers.RepeatedScalarFieldContainer[SirenTriggers.Trigger]
    def __init__(self, settings: _Optional[_Union[SirenTriggers.EnabledSirenTriggers, _Mapping]] = ..., siren_trigger_capabilities: _Optional[_Iterable[_Union[SirenTriggers.Trigger, str]]] = ...) -> None: ...
