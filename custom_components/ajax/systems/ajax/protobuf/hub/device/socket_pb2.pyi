from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Socket(_message.Message):
    __slots__ = ("common_part", "switch_state", "actions_on_arming", "voltage_protection_enabled", "current_protection_enabled", "power_consumed_watts_per_hour", "current_milli_ampers", "voltage_volts", "contact_normal_state", "lockup_relay_mode", "lockup_relay_time_seconds", "indication_enabled", "indication_brightness", "subtype")
    class ContactNormalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_CONTACT_NORMAL_STATE_INFO: _ClassVar[Socket.ContactNormalState]
        NO: _ClassVar[Socket.ContactNormalState]
        NC: _ClassVar[Socket.ContactNormalState]
    NOT_CONTACT_NORMAL_STATE_INFO: Socket.ContactNormalState
    NO: Socket.ContactNormalState
    NC: Socket.ContactNormalState
    class LockupRelayMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_LOCKUP_RELAY_MODE_INFO: _ClassVar[Socket.LockupRelayMode]
        BISTABLE: _ClassVar[Socket.LockupRelayMode]
        IMPULSE: _ClassVar[Socket.LockupRelayMode]
    NO_LOCKUP_RELAY_MODE_INFO: Socket.LockupRelayMode
    BISTABLE: Socket.LockupRelayMode
    IMPULSE: Socket.LockupRelayMode
    class SwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFF_TOO_LOW_VOLTAGE: _ClassVar[Socket.SwitchState]
        OFF_HIGH_VOLTAGE: _ClassVar[Socket.SwitchState]
        OFF_HIGH_CURRENT: _ClassVar[Socket.SwitchState]
        OFF_SHORT_CIRCUIT: _ClassVar[Socket.SwitchState]
        CONTACT_HANG: _ClassVar[Socket.SwitchState]
        OFF_HIGH_TEMPERATURE: _ClassVar[Socket.SwitchState]
        SWITCHED_OFF: _ClassVar[Socket.SwitchState]
    OFF_TOO_LOW_VOLTAGE: Socket.SwitchState
    OFF_HIGH_VOLTAGE: Socket.SwitchState
    OFF_HIGH_CURRENT: Socket.SwitchState
    OFF_SHORT_CIRCUIT: Socket.SwitchState
    CONTACT_HANG: Socket.SwitchState
    OFF_HIGH_TEMPERATURE: Socket.SwitchState
    SWITCHED_OFF: Socket.SwitchState
    class ArmActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARM_ACTIONS_INFO: _ClassVar[Socket.ArmActions]
        ARM_SWITCH_ON: _ClassVar[Socket.ArmActions]
        ARM_SWITCH_OFF: _ClassVar[Socket.ArmActions]
        DISARM_SWITCH_ON: _ClassVar[Socket.ArmActions]
        DISARM_SWITCH_OFF: _ClassVar[Socket.ArmActions]
    NO_ARM_ACTIONS_INFO: Socket.ArmActions
    ARM_SWITCH_ON: Socket.ArmActions
    ARM_SWITCH_OFF: Socket.ArmActions
    DISARM_SWITCH_ON: Socket.ArmActions
    DISARM_SWITCH_OFF: Socket.ArmActions
    class IndicationBrightness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_INDICATION_BRIGHTNESS_INFO: _ClassVar[Socket.IndicationBrightness]
        MAX: _ClassVar[Socket.IndicationBrightness]
        MIN: _ClassVar[Socket.IndicationBrightness]
    NO_INDICATION_BRIGHTNESS_INFO: Socket.IndicationBrightness
    MAX: Socket.IndicationBrightness
    MIN: Socket.IndicationBrightness
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[Socket.Subtype]
    NO_SUBTYPE: Socket.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SWITCH_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_ON_ARMING_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWER_CONSUMED_WATTS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MILLI_AMPERS_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_VOLTS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NORMAL_STATE_FIELD_NUMBER: _ClassVar[int]
    LOCKUP_RELAY_MODE_FIELD_NUMBER: _ClassVar[int]
    LOCKUP_RELAY_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INDICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INDICATION_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    switch_state: _containers.RepeatedScalarFieldContainer[Socket.SwitchState]
    actions_on_arming: _containers.RepeatedScalarFieldContainer[Socket.ArmActions]
    voltage_protection_enabled: bool
    current_protection_enabled: bool
    power_consumed_watts_per_hour: _wrappers_pb2.Int32Value
    current_milli_ampers: _wrappers_pb2.Int32Value
    voltage_volts: _wrappers_pb2.Int32Value
    contact_normal_state: Socket.ContactNormalState
    lockup_relay_mode: Socket.LockupRelayMode
    lockup_relay_time_seconds: int
    indication_enabled: bool
    indication_brightness: Socket.IndicationBrightness
    subtype: Socket.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., switch_state: _Optional[_Iterable[_Union[Socket.SwitchState, str]]] = ..., actions_on_arming: _Optional[_Iterable[_Union[Socket.ArmActions, str]]] = ..., voltage_protection_enabled: bool = ..., current_protection_enabled: bool = ..., power_consumed_watts_per_hour: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., current_milli_ampers: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., voltage_volts: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., contact_normal_state: _Optional[_Union[Socket.ContactNormalState, str]] = ..., lockup_relay_mode: _Optional[_Union[Socket.LockupRelayMode, str]] = ..., lockup_relay_time_seconds: _Optional[int] = ..., indication_enabled: bool = ..., indication_brightness: _Optional[_Union[Socket.IndicationBrightness, str]] = ..., subtype: _Optional[_Union[Socket.Subtype, str]] = ...) -> None: ...
