from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSiren(_message.Message):
    __slots__ = ("common_part", "alarm_duration", "beep_on_arm_disarm", "beep_on_arm_disarm_v2", "blink_while_armed", "siren_volume_level", "buzzer_state", "beep_on_delay", "beep_on_delay_v2", "beep_volume_level", "associated_group_id", "chimes_enabled", "post_alarm_indication_enabled", "subtype")
    class ArmedLightIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARMED_LIGHT_INDICATION_INFO: _ClassVar[HomeSiren.ArmedLightIndication]
        OFF_ARMED_LIGHT_INDICATION: _ClassVar[HomeSiren.ArmedLightIndication]
        BLINK_ARMED_LIGHT_INDICATION: _ClassVar[HomeSiren.ArmedLightIndication]
        CONSTANT_ON_ARMED_LIGHT_INDICATION: _ClassVar[HomeSiren.ArmedLightIndication]
    NO_ARMED_LIGHT_INDICATION_INFO: HomeSiren.ArmedLightIndication
    OFF_ARMED_LIGHT_INDICATION: HomeSiren.ArmedLightIndication
    BLINK_ARMED_LIGHT_INDICATION: HomeSiren.ArmedLightIndication
    CONSTANT_ON_ARMED_LIGHT_INDICATION: HomeSiren.ArmedLightIndication
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_BUZZER_STATE_INFO: _ClassVar[HomeSiren.BuzzerState]
        OFF_BUZZER_STATE: _ClassVar[HomeSiren.BuzzerState]
        ON_BUZZER_STATE: _ClassVar[HomeSiren.BuzzerState]
        WAIT_START_BUZZER_STATE: _ClassVar[HomeSiren.BuzzerState]
        WAIT_STOP_BUZZER_STATE: _ClassVar[HomeSiren.BuzzerState]
    NOT_BUZZER_STATE_INFO: HomeSiren.BuzzerState
    OFF_BUZZER_STATE: HomeSiren.BuzzerState
    ON_BUZZER_STATE: HomeSiren.BuzzerState
    WAIT_START_BUZZER_STATE: HomeSiren.BuzzerState
    WAIT_STOP_BUZZER_STATE: HomeSiren.BuzzerState
    class SirenVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_VOLUME_LEVEL_INFO: _ClassVar[HomeSiren.SirenVolumeLevel]
        VERY_LOUD_SIREN_VOLUME_LEVEL: _ClassVar[HomeSiren.SirenVolumeLevel]
        LOUD_SIREN_VOLUME_LEVEL: _ClassVar[HomeSiren.SirenVolumeLevel]
        QUIET_SIREN_VOLUME_LEVEL: _ClassVar[HomeSiren.SirenVolumeLevel]
        DISABLED_SIREN_VOLUME_LEVEL: _ClassVar[HomeSiren.SirenVolumeLevel]
    NO_SIREN_VOLUME_LEVEL_INFO: HomeSiren.SirenVolumeLevel
    VERY_LOUD_SIREN_VOLUME_LEVEL: HomeSiren.SirenVolumeLevel
    LOUD_SIREN_VOLUME_LEVEL: HomeSiren.SirenVolumeLevel
    QUIET_SIREN_VOLUME_LEVEL: HomeSiren.SirenVolumeLevel
    DISABLED_SIREN_VOLUME_LEVEL: HomeSiren.SirenVolumeLevel
    class BeepVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_VOLUME_LEVEL_INFO: _ClassVar[HomeSiren.BeepVolumeLevel]
        VERY_LOUD_BEEP_VOLUME_LEVEL: _ClassVar[HomeSiren.BeepVolumeLevel]
        LOUD_BEEP_VOLUME_LEVEL: _ClassVar[HomeSiren.BeepVolumeLevel]
        QUIET_BEEP_VOLUME_LEVEL: _ClassVar[HomeSiren.BeepVolumeLevel]
    NO_BEEP_VOLUME_LEVEL_INFO: HomeSiren.BeepVolumeLevel
    VERY_LOUD_BEEP_VOLUME_LEVEL: HomeSiren.BeepVolumeLevel
    LOUD_BEEP_VOLUME_LEVEL: HomeSiren.BeepVolumeLevel
    QUIET_BEEP_VOLUME_LEVEL: HomeSiren.BeepVolumeLevel
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[HomeSiren.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[HomeSiren.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[HomeSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[HomeSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[HomeSiren.BeepOnArmDisarm]
    NO_BEEP_ON_ARM_DISARM_INFO: HomeSiren.BeepOnArmDisarm
    BEEP_ON_ARM: HomeSiren.BeepOnArmDisarm
    BEEP_ON_DISARM: HomeSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: HomeSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: HomeSiren.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[HomeSiren.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[HomeSiren.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[HomeSiren.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[HomeSiren.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[HomeSiren.BeepOnDelay]
    NO_BEEP_ON_DELAY_INFO: HomeSiren.BeepOnDelay
    BEEP_ON_ARM_DELAY: HomeSiren.BeepOnDelay
    BEEP_ON_DISARM_DELAY: HomeSiren.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: HomeSiren.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: HomeSiren.BeepOnDelay
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[HomeSiren.Subtype]
    NO_SUBTYPE: HomeSiren.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_V2_FIELD_NUMBER: _ClassVar[int]
    BLINK_WHILE_ARMED_FIELD_NUMBER: _ClassVar[int]
    SIREN_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
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
    beep_on_arm_disarm_v2: _containers.RepeatedScalarFieldContainer[HomeSiren.BeepOnArmDisarm]
    blink_while_armed: HomeSiren.ArmedLightIndication
    siren_volume_level: HomeSiren.SirenVolumeLevel
    buzzer_state: HomeSiren.BuzzerState
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[HomeSiren.BeepOnDelay]
    beep_volume_level: HomeSiren.BeepVolumeLevel
    associated_group_id: str
    chimes_enabled: bool
    post_alarm_indication_enabled: bool
    subtype: HomeSiren.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., alarm_duration: _Optional[int] = ..., beep_on_arm_disarm: bool = ..., beep_on_arm_disarm_v2: _Optional[_Iterable[_Union[HomeSiren.BeepOnArmDisarm, str]]] = ..., blink_while_armed: _Optional[_Union[HomeSiren.ArmedLightIndication, str]] = ..., siren_volume_level: _Optional[_Union[HomeSiren.SirenVolumeLevel, str]] = ..., buzzer_state: _Optional[_Union[HomeSiren.BuzzerState, str]] = ..., beep_on_delay: bool = ..., beep_on_delay_v2: _Optional[_Iterable[_Union[HomeSiren.BeepOnDelay, str]]] = ..., beep_volume_level: _Optional[_Union[HomeSiren.BeepVolumeLevel, str]] = ..., associated_group_id: _Optional[str] = ..., chimes_enabled: bool = ..., post_alarm_indication_enabled: bool = ..., subtype: _Optional[_Union[HomeSiren.Subtype, str]] = ...) -> None: ...
