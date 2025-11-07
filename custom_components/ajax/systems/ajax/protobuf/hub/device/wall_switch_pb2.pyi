from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WallSwitch(_message.Message):
    __slots__ = ("common_part", "switch_state", "actions_on_arming", "voltage_protection_enabled", "current_protection_enabled", "power_consumed_watts_per_hour", "current_milli_ampers", "voltage_volts", "contact_normal_state", "lockup_relay_mode", "lockup_relay_time_seconds", "subtype")
    class ContactNormalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_CONTACT_NORMAL_STATE_INFO: _ClassVar[WallSwitch.ContactNormalState]
        NO: _ClassVar[WallSwitch.ContactNormalState]
        NC: _ClassVar[WallSwitch.ContactNormalState]
    NOT_CONTACT_NORMAL_STATE_INFO: WallSwitch.ContactNormalState
    NO: WallSwitch.ContactNormalState
    NC: WallSwitch.ContactNormalState
    class LockupRelayMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_LOCKUP_RELAY_MODE_INFO: _ClassVar[WallSwitch.LockupRelayMode]
        BISTABLE: _ClassVar[WallSwitch.LockupRelayMode]
        IMPULSE: _ClassVar[WallSwitch.LockupRelayMode]
    NO_LOCKUP_RELAY_MODE_INFO: WallSwitch.LockupRelayMode
    BISTABLE: WallSwitch.LockupRelayMode
    IMPULSE: WallSwitch.LockupRelayMode
    class SwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFF_TOO_LOW_VOLTAGE: _ClassVar[WallSwitch.SwitchState]
        OFF_HIGH_VOLTAGE: _ClassVar[WallSwitch.SwitchState]
        OFF_HIGH_CURRENT: _ClassVar[WallSwitch.SwitchState]
        OFF_SHORT_CIRCUIT: _ClassVar[WallSwitch.SwitchState]
        CONTACT_HANG: _ClassVar[WallSwitch.SwitchState]
        OFF_HIGH_TEMPERATURE: _ClassVar[WallSwitch.SwitchState]
        SWITCHED_OFF: _ClassVar[WallSwitch.SwitchState]
    OFF_TOO_LOW_VOLTAGE: WallSwitch.SwitchState
    OFF_HIGH_VOLTAGE: WallSwitch.SwitchState
    OFF_HIGH_CURRENT: WallSwitch.SwitchState
    OFF_SHORT_CIRCUIT: WallSwitch.SwitchState
    CONTACT_HANG: WallSwitch.SwitchState
    OFF_HIGH_TEMPERATURE: WallSwitch.SwitchState
    SWITCHED_OFF: WallSwitch.SwitchState
    class ArmActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARM_ACTIONS_INFO: _ClassVar[WallSwitch.ArmActions]
        ARM_SWITCH_ON: _ClassVar[WallSwitch.ArmActions]
        ARM_SWITCH_OFF: _ClassVar[WallSwitch.ArmActions]
        DISARM_SWITCH_ON: _ClassVar[WallSwitch.ArmActions]
        DISARM_SWITCH_OFF: _ClassVar[WallSwitch.ArmActions]
    NO_ARM_ACTIONS_INFO: WallSwitch.ArmActions
    ARM_SWITCH_ON: WallSwitch.ArmActions
    ARM_SWITCH_OFF: WallSwitch.ArmActions
    DISARM_SWITCH_ON: WallSwitch.ArmActions
    DISARM_SWITCH_OFF: WallSwitch.ArmActions
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[WallSwitch.Subtype]
    NO_SUBTYPE: WallSwitch.Subtype
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
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    switch_state: _containers.RepeatedScalarFieldContainer[WallSwitch.SwitchState]
    actions_on_arming: _containers.RepeatedScalarFieldContainer[WallSwitch.ArmActions]
    voltage_protection_enabled: bool
    current_protection_enabled: bool
    power_consumed_watts_per_hour: _wrappers_pb2.Int32Value
    current_milli_ampers: _wrappers_pb2.Int32Value
    voltage_volts: _wrappers_pb2.Int32Value
    contact_normal_state: WallSwitch.ContactNormalState
    lockup_relay_mode: WallSwitch.LockupRelayMode
    lockup_relay_time_seconds: int
    subtype: WallSwitch.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., switch_state: _Optional[_Iterable[_Union[WallSwitch.SwitchState, str]]] = ..., actions_on_arming: _Optional[_Iterable[_Union[WallSwitch.ArmActions, str]]] = ..., voltage_protection_enabled: bool = ..., current_protection_enabled: bool = ..., power_consumed_watts_per_hour: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., current_milli_ampers: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., voltage_volts: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., contact_normal_state: _Optional[_Union[WallSwitch.ContactNormalState, str]] = ..., lockup_relay_mode: _Optional[_Union[WallSwitch.LockupRelayMode, str]] = ..., lockup_relay_time_seconds: _Optional[int] = ..., subtype: _Optional[_Union[WallSwitch.Subtype, str]] = ...) -> None: ...
