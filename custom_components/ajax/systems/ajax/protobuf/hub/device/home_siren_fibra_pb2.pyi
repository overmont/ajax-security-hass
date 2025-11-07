from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from systems.ajax.protobuf.hub.device import common_fibra_pb2 as _common_fibra_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSirenFibra(_message.Message):
    __slots__ = ("common_part", "common_fibra_part", "alarm_duration", "beep_on_arm_disarm", "beep_on_arm_disarm_v2", "blink_while_armed", "siren_volume_level", "buzzer_state", "beep_on_delay", "beep_on_delay_v2", "beep_volume_level", "associated_group_id", "chimes_enabled", "post_alarm_indication_enabled", "subtype")
    class ArmedLightIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARMED_LIGHT_INDICATION_INFO: _ClassVar[HomeSirenFibra.ArmedLightIndication]
        OFF_ARMED_LIGHT_INDICATION: _ClassVar[HomeSirenFibra.ArmedLightIndication]
        BLINK_ARMED_LIGHT_INDICATION: _ClassVar[HomeSirenFibra.ArmedLightIndication]
        CONSTANT_ON_ARMED_LIGHT_INDICATION: _ClassVar[HomeSirenFibra.ArmedLightIndication]
    NO_ARMED_LIGHT_INDICATION_INFO: HomeSirenFibra.ArmedLightIndication
    OFF_ARMED_LIGHT_INDICATION: HomeSirenFibra.ArmedLightIndication
    BLINK_ARMED_LIGHT_INDICATION: HomeSirenFibra.ArmedLightIndication
    CONSTANT_ON_ARMED_LIGHT_INDICATION: HomeSirenFibra.ArmedLightIndication
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_BUZZER_STATE_INFO: _ClassVar[HomeSirenFibra.BuzzerState]
        OFF_BUZZER_STATE: _ClassVar[HomeSirenFibra.BuzzerState]
        ON_BUZZER_STATE: _ClassVar[HomeSirenFibra.BuzzerState]
        WAIT_START_BUZZER_STATE: _ClassVar[HomeSirenFibra.BuzzerState]
        WAIT_STOP_BUZZER_STATE: _ClassVar[HomeSirenFibra.BuzzerState]
    NOT_BUZZER_STATE_INFO: HomeSirenFibra.BuzzerState
    OFF_BUZZER_STATE: HomeSirenFibra.BuzzerState
    ON_BUZZER_STATE: HomeSirenFibra.BuzzerState
    WAIT_START_BUZZER_STATE: HomeSirenFibra.BuzzerState
    WAIT_STOP_BUZZER_STATE: HomeSirenFibra.BuzzerState
    class SirenVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_VOLUME_LEVEL_INFO: _ClassVar[HomeSirenFibra.SirenVolumeLevel]
        VERY_LOUD_SIREN_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.SirenVolumeLevel]
        LOUD_SIREN_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.SirenVolumeLevel]
        QUIET_SIREN_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.SirenVolumeLevel]
        DISABLED_SIREN_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.SirenVolumeLevel]
    NO_SIREN_VOLUME_LEVEL_INFO: HomeSirenFibra.SirenVolumeLevel
    VERY_LOUD_SIREN_VOLUME_LEVEL: HomeSirenFibra.SirenVolumeLevel
    LOUD_SIREN_VOLUME_LEVEL: HomeSirenFibra.SirenVolumeLevel
    QUIET_SIREN_VOLUME_LEVEL: HomeSirenFibra.SirenVolumeLevel
    DISABLED_SIREN_VOLUME_LEVEL: HomeSirenFibra.SirenVolumeLevel
    class BeepVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_VOLUME_LEVEL_INFO: _ClassVar[HomeSirenFibra.BeepVolumeLevel]
        VERY_LOUD_BEEP_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.BeepVolumeLevel]
        LOUD_BEEP_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.BeepVolumeLevel]
        QUIET_BEEP_VOLUME_LEVEL: _ClassVar[HomeSirenFibra.BeepVolumeLevel]
    NO_BEEP_VOLUME_LEVEL_INFO: HomeSirenFibra.BeepVolumeLevel
    VERY_LOUD_BEEP_VOLUME_LEVEL: HomeSirenFibra.BeepVolumeLevel
    LOUD_BEEP_VOLUME_LEVEL: HomeSirenFibra.BeepVolumeLevel
    QUIET_BEEP_VOLUME_LEVEL: HomeSirenFibra.BeepVolumeLevel
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[HomeSirenFibra.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[HomeSirenFibra.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[HomeSirenFibra.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[HomeSirenFibra.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[HomeSirenFibra.BeepOnArmDisarm]
    NO_BEEP_ON_ARM_DISARM_INFO: HomeSirenFibra.BeepOnArmDisarm
    BEEP_ON_ARM: HomeSirenFibra.BeepOnArmDisarm
    BEEP_ON_DISARM: HomeSirenFibra.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: HomeSirenFibra.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: HomeSirenFibra.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[HomeSirenFibra.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[HomeSirenFibra.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[HomeSirenFibra.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[HomeSirenFibra.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[HomeSirenFibra.BeepOnDelay]
    NO_BEEP_ON_DELAY_INFO: HomeSirenFibra.BeepOnDelay
    BEEP_ON_ARM_DELAY: HomeSirenFibra.BeepOnDelay
    BEEP_ON_DISARM_DELAY: HomeSirenFibra.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: HomeSirenFibra.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: HomeSirenFibra.BeepOnDelay
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[HomeSirenFibra.Subtype]
    NO_SUBTYPE: HomeSirenFibra.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
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
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    alarm_duration: int
    beep_on_arm_disarm: bool
    beep_on_arm_disarm_v2: _containers.RepeatedScalarFieldContainer[HomeSirenFibra.BeepOnArmDisarm]
    blink_while_armed: HomeSirenFibra.ArmedLightIndication
    siren_volume_level: HomeSirenFibra.SirenVolumeLevel
    buzzer_state: HomeSirenFibra.BuzzerState
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[HomeSirenFibra.BeepOnDelay]
    beep_volume_level: HomeSirenFibra.BeepVolumeLevel
    associated_group_id: str
    chimes_enabled: bool
    post_alarm_indication_enabled: bool
    subtype: HomeSirenFibra.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., common_fibra_part: _Optional[_Union[_common_fibra_pb2.CommonFibraPart, _Mapping]] = ..., alarm_duration: _Optional[int] = ..., beep_on_arm_disarm: bool = ..., beep_on_arm_disarm_v2: _Optional[_Iterable[_Union[HomeSirenFibra.BeepOnArmDisarm, str]]] = ..., blink_while_armed: _Optional[_Union[HomeSirenFibra.ArmedLightIndication, str]] = ..., siren_volume_level: _Optional[_Union[HomeSirenFibra.SirenVolumeLevel, str]] = ..., buzzer_state: _Optional[_Union[HomeSirenFibra.BuzzerState, str]] = ..., beep_on_delay: bool = ..., beep_on_delay_v2: _Optional[_Iterable[_Union[HomeSirenFibra.BeepOnDelay, str]]] = ..., beep_volume_level: _Optional[_Union[HomeSirenFibra.BeepVolumeLevel, str]] = ..., associated_group_id: _Optional[str] = ..., chimes_enabled: bool = ..., post_alarm_indication_enabled: bool = ..., subtype: _Optional[_Union[HomeSirenFibra.Subtype, str]] = ...) -> None: ...
