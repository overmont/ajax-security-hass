from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreetSiren(_message.Message):
    __slots__ = ("common_part", "alarm_duration", "beep_on_arm_disarm", "beep_on_arm_disarm_v2", "blink_while_armed", "alert_if_moved", "siren_volume_level", "externally_powered", "buzzer_state", "beep_on_delay", "beep_on_delay_v2", "beep_volume_level", "associated_group_id", "chimes_enabled", "post_alarm_indication_enabled", "subtype")
    class ArmedLightIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARMED_LIGHT_INDICATION_INFO: _ClassVar[StreetSiren.ArmedLightIndication]
        OFF_ARMED_LIGHT_INDICATION: _ClassVar[StreetSiren.ArmedLightIndication]
        BLINK_ARMED_LIGHT_INDICATION: _ClassVar[StreetSiren.ArmedLightIndication]
        CONSTANT_ON_ARMED_LIGHT_INDICATION: _ClassVar[StreetSiren.ArmedLightIndication]
    NO_ARMED_LIGHT_INDICATION_INFO: StreetSiren.ArmedLightIndication
    OFF_ARMED_LIGHT_INDICATION: StreetSiren.ArmedLightIndication
    BLINK_ARMED_LIGHT_INDICATION: StreetSiren.ArmedLightIndication
    CONSTANT_ON_ARMED_LIGHT_INDICATION: StreetSiren.ArmedLightIndication
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_BUZZER_STATE_INFO: _ClassVar[StreetSiren.BuzzerState]
        OFF_BUZZER_STATE: _ClassVar[StreetSiren.BuzzerState]
        ON_BUZZER_STATE: _ClassVar[StreetSiren.BuzzerState]
        WAIT_START_BUZZER_STATE: _ClassVar[StreetSiren.BuzzerState]
        WAIT_STOP_BUZZER_STATE: _ClassVar[StreetSiren.BuzzerState]
    NOT_BUZZER_STATE_INFO: StreetSiren.BuzzerState
    OFF_BUZZER_STATE: StreetSiren.BuzzerState
    ON_BUZZER_STATE: StreetSiren.BuzzerState
    WAIT_START_BUZZER_STATE: StreetSiren.BuzzerState
    WAIT_STOP_BUZZER_STATE: StreetSiren.BuzzerState
    class SirenVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_VOLUME_LEVEL_INFO: _ClassVar[StreetSiren.SirenVolumeLevel]
        VERY_LOUD_SIREN_VOLUME_LEVEL: _ClassVar[StreetSiren.SirenVolumeLevel]
        LOUD_SIREN_VOLUME_LEVEL: _ClassVar[StreetSiren.SirenVolumeLevel]
        QUIET_SIREN_VOLUME_LEVEL: _ClassVar[StreetSiren.SirenVolumeLevel]
        DISABLED_SIREN_VOLUME_LEVEL: _ClassVar[StreetSiren.SirenVolumeLevel]
    NO_SIREN_VOLUME_LEVEL_INFO: StreetSiren.SirenVolumeLevel
    VERY_LOUD_SIREN_VOLUME_LEVEL: StreetSiren.SirenVolumeLevel
    LOUD_SIREN_VOLUME_LEVEL: StreetSiren.SirenVolumeLevel
    QUIET_SIREN_VOLUME_LEVEL: StreetSiren.SirenVolumeLevel
    DISABLED_SIREN_VOLUME_LEVEL: StreetSiren.SirenVolumeLevel
    class BeepVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_VOLUME_LEVEL_INFO: _ClassVar[StreetSiren.BeepVolumeLevel]
        VERY_LOUD_BEEP_VOLUME_LEVEL: _ClassVar[StreetSiren.BeepVolumeLevel]
        LOUD_BEEP_VOLUME_LEVEL: _ClassVar[StreetSiren.BeepVolumeLevel]
        QUIET_BEEP_VOLUME_LEVEL: _ClassVar[StreetSiren.BeepVolumeLevel]
    NO_BEEP_VOLUME_LEVEL_INFO: StreetSiren.BeepVolumeLevel
    VERY_LOUD_BEEP_VOLUME_LEVEL: StreetSiren.BeepVolumeLevel
    LOUD_BEEP_VOLUME_LEVEL: StreetSiren.BeepVolumeLevel
    QUIET_BEEP_VOLUME_LEVEL: StreetSiren.BeepVolumeLevel
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[StreetSiren.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[StreetSiren.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[StreetSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[StreetSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[StreetSiren.BeepOnArmDisarm]
    NO_BEEP_ON_ARM_DISARM_INFO: StreetSiren.BeepOnArmDisarm
    BEEP_ON_ARM: StreetSiren.BeepOnArmDisarm
    BEEP_ON_DISARM: StreetSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: StreetSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: StreetSiren.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[StreetSiren.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[StreetSiren.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[StreetSiren.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[StreetSiren.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[StreetSiren.BeepOnDelay]
    NO_BEEP_ON_DELAY_INFO: StreetSiren.BeepOnDelay
    BEEP_ON_ARM_DELAY: StreetSiren.BeepOnDelay
    BEEP_ON_DISARM_DELAY: StreetSiren.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: StreetSiren.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: StreetSiren.BeepOnDelay
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[StreetSiren.Subtype]
    NO_SUBTYPE: StreetSiren.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_V2_FIELD_NUMBER: _ClassVar[int]
    BLINK_WHILE_ARMED_FIELD_NUMBER: _ClassVar[int]
    ALERT_IF_MOVED_FIELD_NUMBER: _ClassVar[int]
    SIREN_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    BUZZER_STATE_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_V2_FIELD_NUMBER: _ClassVar[int]
    BEEP_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHIMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    alarm_duration: int
    beep_on_arm_disarm: bool
    beep_on_arm_disarm_v2: _containers.RepeatedScalarFieldContainer[StreetSiren.BeepOnArmDisarm]
    blink_while_armed: StreetSiren.ArmedLightIndication
    alert_if_moved: bool
    siren_volume_level: StreetSiren.SirenVolumeLevel
    externally_powered: _wrappers_pb2.BoolValue
    buzzer_state: StreetSiren.BuzzerState
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[StreetSiren.BeepOnDelay]
    beep_volume_level: StreetSiren.BeepVolumeLevel
    associated_group_id: str
    chimes_enabled: bool
    post_alarm_indication_enabled: bool
    subtype: StreetSiren.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., alarm_duration: _Optional[int] = ..., beep_on_arm_disarm: bool = ..., beep_on_arm_disarm_v2: _Optional[_Iterable[_Union[StreetSiren.BeepOnArmDisarm, str]]] = ..., blink_while_armed: _Optional[_Union[StreetSiren.ArmedLightIndication, str]] = ..., alert_if_moved: bool = ..., siren_volume_level: _Optional[_Union[StreetSiren.SirenVolumeLevel, str]] = ..., externally_powered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., buzzer_state: _Optional[_Union[StreetSiren.BuzzerState, str]] = ..., beep_on_delay: bool = ..., beep_on_delay_v2: _Optional[_Iterable[_Union[StreetSiren.BeepOnDelay, str]]] = ..., beep_volume_level: _Optional[_Union[StreetSiren.BeepVolumeLevel, str]] = ..., associated_group_id: _Optional[str] = ..., chimes_enabled: bool = ..., post_alarm_indication_enabled: bool = ..., subtype: _Optional[_Union[StreetSiren.Subtype, str]] = ...) -> None: ...
