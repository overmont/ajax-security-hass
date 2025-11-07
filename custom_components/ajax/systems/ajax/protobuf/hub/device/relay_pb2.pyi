from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Relay(_message.Message):
    __slots__ = ("common_part", "switch_state", "actions_on_arming", "contact_normal_state", "lockup_relay_mode", "voltage_milli_volts", "lockup_relay_time_seconds", "subtype")
    class ContactNormalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_CONTACT_NORMAL_STATE_INFO: _ClassVar[Relay.ContactNormalState]
        NO: _ClassVar[Relay.ContactNormalState]
        NC: _ClassVar[Relay.ContactNormalState]
    NOT_CONTACT_NORMAL_STATE_INFO: Relay.ContactNormalState
    NO: Relay.ContactNormalState
    NC: Relay.ContactNormalState
    class LockupRelayMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_LOCKUP_RELAY_MODE_INFO: _ClassVar[Relay.LockupRelayMode]
        BISTABLE: _ClassVar[Relay.LockupRelayMode]
        IMPULSE: _ClassVar[Relay.LockupRelayMode]
    NO_LOCKUP_RELAY_MODE_INFO: Relay.LockupRelayMode
    BISTABLE: Relay.LockupRelayMode
    IMPULSE: Relay.LockupRelayMode
    class SwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFF_TOO_LOW_VOLTAGE: _ClassVar[Relay.SwitchState]
        OFF_HIGH_VOLTAGE: _ClassVar[Relay.SwitchState]
        CONTACT_HANG: _ClassVar[Relay.SwitchState]
        OFF_HIGH_TEMPERATURE: _ClassVar[Relay.SwitchState]
        SWITCHED_OFF: _ClassVar[Relay.SwitchState]
    OFF_TOO_LOW_VOLTAGE: Relay.SwitchState
    OFF_HIGH_VOLTAGE: Relay.SwitchState
    CONTACT_HANG: Relay.SwitchState
    OFF_HIGH_TEMPERATURE: Relay.SwitchState
    SWITCHED_OFF: Relay.SwitchState
    class ArmActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARM_ACTIONS_INFO: _ClassVar[Relay.ArmActions]
        ARM_SWITCH_ON: _ClassVar[Relay.ArmActions]
        ARM_SWITCH_OFF: _ClassVar[Relay.ArmActions]
        DISARM_SWITCH_ON: _ClassVar[Relay.ArmActions]
        DISARM_SWITCH_OFF: _ClassVar[Relay.ArmActions]
    NO_ARM_ACTIONS_INFO: Relay.ArmActions
    ARM_SWITCH_ON: Relay.ArmActions
    ARM_SWITCH_OFF: Relay.ArmActions
    DISARM_SWITCH_ON: Relay.ArmActions
    DISARM_SWITCH_OFF: Relay.ArmActions
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[Relay.Subtype]
    NO_SUBTYPE: Relay.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SWITCH_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_ON_ARMING_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NORMAL_STATE_FIELD_NUMBER: _ClassVar[int]
    LOCKUP_RELAY_MODE_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_MILLI_VOLTS_FIELD_NUMBER: _ClassVar[int]
    LOCKUP_RELAY_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    switch_state: _containers.RepeatedScalarFieldContainer[Relay.SwitchState]
    actions_on_arming: _containers.RepeatedScalarFieldContainer[Relay.ArmActions]
    contact_normal_state: Relay.ContactNormalState
    lockup_relay_mode: Relay.LockupRelayMode
    voltage_milli_volts: _wrappers_pb2.Int32Value
    lockup_relay_time_seconds: int
    subtype: Relay.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., switch_state: _Optional[_Iterable[_Union[Relay.SwitchState, str]]] = ..., actions_on_arming: _Optional[_Iterable[_Union[Relay.ArmActions, str]]] = ..., contact_normal_state: _Optional[_Union[Relay.ContactNormalState, str]] = ..., lockup_relay_mode: _Optional[_Union[Relay.LockupRelayMode, str]] = ..., voltage_milli_volts: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., lockup_relay_time_seconds: _Optional[int] = ..., subtype: _Optional[_Union[Relay.Subtype, str]] = ...) -> None: ...
