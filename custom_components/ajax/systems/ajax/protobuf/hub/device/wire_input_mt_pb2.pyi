from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WireInputMt(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "external_contact_mode", "external_contact_alarm_mode", "external_contact_state", "external_contact_broken", "input_type", "reaction_time", "assigned_mtr", "input_resistance", "fact_resistance", "custom_alarm", "alwaysActive", "external_contact_scenario_bits", "chime_triggers", "chime_signal", "subtype")
    class ExternalContactMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_MODE_INFO: _ClassVar[WireInputMt.ExternalContactMode]
        DISABLED: _ClassVar[WireInputMt.ExternalContactMode]
        NORMALLY_OPEN: _ClassVar[WireInputMt.ExternalContactMode]
        NORMALLY_CLOSED: _ClassVar[WireInputMt.ExternalContactMode]
        NORMALLY_CLOSED_R: _ClassVar[WireInputMt.ExternalContactMode]
        NORMALLY_OPEN_R: _ClassVar[WireInputMt.ExternalContactMode]
    NO_EXTERNAL_CONTACT_MODE_INFO: WireInputMt.ExternalContactMode
    DISABLED: WireInputMt.ExternalContactMode
    NORMALLY_OPEN: WireInputMt.ExternalContactMode
    NORMALLY_CLOSED: WireInputMt.ExternalContactMode
    NORMALLY_CLOSED_R: WireInputMt.ExternalContactMode
    NORMALLY_OPEN_R: WireInputMt.ExternalContactMode
    class ExternalContactAlarmMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: _ClassVar[WireInputMt.ExternalContactAlarmMode]
        BISTABLE: _ClassVar[WireInputMt.ExternalContactAlarmMode]
        IMPULSE: _ClassVar[WireInputMt.ExternalContactAlarmMode]
    NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: WireInputMt.ExternalContactAlarmMode
    BISTABLE: WireInputMt.ExternalContactAlarmMode
    IMPULSE: WireInputMt.ExternalContactAlarmMode
    class ExternalContactState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_STATE: _ClassVar[WireInputMt.ExternalContactState]
        CONTACT_DISRUPTED: _ClassVar[WireInputMt.ExternalContactState]
        CONTACT_NORMAL: _ClassVar[WireInputMt.ExternalContactState]
        CONTACT_NOT_AVAILABLE: _ClassVar[WireInputMt.ExternalContactState]
    NO_EXTERNAL_CONTACT_STATE: WireInputMt.ExternalContactState
    CONTACT_DISRUPTED: WireInputMt.ExternalContactState
    CONTACT_NORMAL: WireInputMt.ExternalContactState
    CONTACT_NOT_AVAILABLE: WireInputMt.ExternalContactState
    class ExternalContactDisruptionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_DISRUPTION_STATE: _ClassVar[WireInputMt.ExternalContactDisruptionState]
        CONTACT_DISRUPTION_NORMAL: _ClassVar[WireInputMt.ExternalContactDisruptionState]
        CONTACT_DISRUPTION_BROKEN: _ClassVar[WireInputMt.ExternalContactDisruptionState]
        CONTACT_DISRUPTION_NOT_AVAILABLE: _ClassVar[WireInputMt.ExternalContactDisruptionState]
    NO_EXTERNAL_CONTACT_DISRUPTION_STATE: WireInputMt.ExternalContactDisruptionState
    CONTACT_DISRUPTION_NORMAL: WireInputMt.ExternalContactDisruptionState
    CONTACT_DISRUPTION_BROKEN: WireInputMt.ExternalContactDisruptionState
    CONTACT_DISRUPTION_NOT_AVAILABLE: WireInputMt.ExternalContactDisruptionState
    class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_INPUT_TYPE: _ClassVar[WireInputMt.InputType]
        DEVICE: _ClassVar[WireInputMt.InputType]
        TAMPER: _ClassVar[WireInputMt.InputType]
    NO_INPUT_TYPE: WireInputMt.InputType
    DEVICE: WireInputMt.InputType
    TAMPER: WireInputMt.InputType
    class ReactionTimeMillis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_REACTION_TIME: _ClassVar[WireInputMt.ReactionTimeMillis]
        _20: _ClassVar[WireInputMt.ReactionTimeMillis]
        _100: _ClassVar[WireInputMt.ReactionTimeMillis]
        _1000: _ClassVar[WireInputMt.ReactionTimeMillis]
    NO_REACTION_TIME: WireInputMt.ReactionTimeMillis
    _20: WireInputMt.ReactionTimeMillis
    _100: WireInputMt.ReactionTimeMillis
    _1000: WireInputMt.ReactionTimeMillis
    class CustomAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CUSTOM_ALARM_TYPE: _ClassVar[WireInputMt.CustomAlarmType]
        BURGLARY: _ClassVar[WireInputMt.CustomAlarmType]
        FIRE: _ClassVar[WireInputMt.CustomAlarmType]
        MEDICAL: _ClassVar[WireInputMt.CustomAlarmType]
        PANIC: _ClassVar[WireInputMt.CustomAlarmType]
        GAS: _ClassVar[WireInputMt.CustomAlarmType]
    NO_CUSTOM_ALARM_TYPE: WireInputMt.CustomAlarmType
    BURGLARY: WireInputMt.CustomAlarmType
    FIRE: WireInputMt.CustomAlarmType
    MEDICAL: WireInputMt.CustomAlarmType
    PANIC: WireInputMt.CustomAlarmType
    GAS: WireInputMt.CustomAlarmType
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[WireInputMt.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[WireInputMt.SirenTrigger]
        SHORT_CIRCUIT: _ClassVar[WireInputMt.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: WireInputMt.SirenTrigger
    EXTRA_CONTACT: WireInputMt.SirenTrigger
    SHORT_CIRCUIT: WireInputMt.SirenTrigger
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[WireInputMt.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[WireInputMt.ChimeTrigger]
    NO_CHIME_TRIGGER_INFO: WireInputMt.ChimeTrigger
    CHIME_EXTRA_CONTACT: WireInputMt.ChimeTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[WireInputMt.Subtype]
    NO_SUBTYPE: WireInputMt.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALARM_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_STATE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_BROKEN_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_MTR_FIELD_NUMBER: _ClassVar[int]
    INPUT_RESISTANCE_FIELD_NUMBER: _ClassVar[int]
    FACT_RESISTANCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_FIELD_NUMBER: _ClassVar[int]
    ALWAYSACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_SCENARIO_BITS_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[WireInputMt.SirenTrigger]
    external_contact_mode: WireInputMt.ExternalContactMode
    external_contact_alarm_mode: WireInputMt.ExternalContactAlarmMode
    external_contact_state: WireInputMt.ExternalContactState
    external_contact_broken: WireInputMt.ExternalContactDisruptionState
    input_type: WireInputMt.InputType
    reaction_time: WireInputMt.ReactionTimeMillis
    assigned_mtr: _wrappers_pb2.Int32Value
    input_resistance: int
    fact_resistance: int
    custom_alarm: WireInputMt.CustomAlarmType
    alwaysActive: bool
    external_contact_scenario_bits: int
    chime_triggers: _containers.RepeatedScalarFieldContainer[WireInputMt.ChimeTrigger]
    chime_signal: int
    subtype: WireInputMt.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[WireInputMt.SirenTrigger, str]]] = ..., external_contact_mode: _Optional[_Union[WireInputMt.ExternalContactMode, str]] = ..., external_contact_alarm_mode: _Optional[_Union[WireInputMt.ExternalContactAlarmMode, str]] = ..., external_contact_state: _Optional[_Union[WireInputMt.ExternalContactState, str]] = ..., external_contact_broken: _Optional[_Union[WireInputMt.ExternalContactDisruptionState, str]] = ..., input_type: _Optional[_Union[WireInputMt.InputType, str]] = ..., reaction_time: _Optional[_Union[WireInputMt.ReactionTimeMillis, str]] = ..., assigned_mtr: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., input_resistance: _Optional[int] = ..., fact_resistance: _Optional[int] = ..., custom_alarm: _Optional[_Union[WireInputMt.CustomAlarmType, str]] = ..., alwaysActive: bool = ..., external_contact_scenario_bits: _Optional[int] = ..., chime_triggers: _Optional[_Iterable[_Union[WireInputMt.ChimeTrigger, str]]] = ..., chime_signal: _Optional[int] = ..., subtype: _Optional[_Union[WireInputMt.Subtype, str]] = ...) -> None: ...
