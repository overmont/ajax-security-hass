from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeypadCombi(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "access_profiles", "star_button_function", "password", "force_disarm_password", "block_on_multiple_password_failures", "time_to_block_on_multiple_password_failures_minutes", "blocked", "allow_fast_arming", "brightness_level", "volume_level", "associated_group_id", "password_hash", "password_hash_duress", "arm_inversion", "nfc_enabled", "beep_on_delay", "beep_on_delay_v2", "siren_events_volume", "act_on_arming", "act_on_arming_v2", "time_to_act_seconds", "siren_alarm_volume", "chimes_enabled", "count_protect", "buzzer_state", "siren_associated_group_id", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[KeypadCombi.SirenTrigger]
        SECURITY_BUTTON: _ClassVar[KeypadCombi.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: KeypadCombi.SirenTrigger
    SECURITY_BUTTON: KeypadCombi.SirenTrigger
    class StarButtonFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STAR_BUTTON_FUNCTION_INFO: _ClassVar[KeypadCombi.StarButtonFunction]
        DISABLED: _ClassVar[KeypadCombi.StarButtonFunction]
        PANIC: _ClassVar[KeypadCombi.StarButtonFunction]
        MUTE_FIRE_ALARM: _ClassVar[KeypadCombi.StarButtonFunction]
    NO_STAR_BUTTON_FUNCTION_INFO: KeypadCombi.StarButtonFunction
    DISABLED: KeypadCombi.StarButtonFunction
    PANIC: KeypadCombi.StarButtonFunction
    MUTE_FIRE_ALARM: KeypadCombi.StarButtonFunction
    class AccessProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACCESS_PROFILE_INFO: _ClassVar[KeypadCombi.AccessProfile]
        KEYBOARD_PASSWORD: _ClassVar[KeypadCombi.AccessProfile]
        USER_PASSWORD: _ClassVar[KeypadCombi.AccessProfile]
    NO_ACCESS_PROFILE_INFO: KeypadCombi.AccessProfile
    KEYBOARD_PASSWORD: KeypadCombi.AccessProfile
    USER_PASSWORD: KeypadCombi.AccessProfile
    class SirenAlarmVolume(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_ALARM_VOLUME: _ClassVar[KeypadCombi.SirenAlarmVolume]
        DISABLED_ALARM_VOLUME: _ClassVar[KeypadCombi.SirenAlarmVolume]
        MIN_ALARM_VOLUME: _ClassVar[KeypadCombi.SirenAlarmVolume]
        AVG_ALARM_VOLUME: _ClassVar[KeypadCombi.SirenAlarmVolume]
        MAX_ALARM_VOLUME: _ClassVar[KeypadCombi.SirenAlarmVolume]
    NO_SIREN_ALARM_VOLUME: KeypadCombi.SirenAlarmVolume
    DISABLED_ALARM_VOLUME: KeypadCombi.SirenAlarmVolume
    MIN_ALARM_VOLUME: KeypadCombi.SirenAlarmVolume
    AVG_ALARM_VOLUME: KeypadCombi.SirenAlarmVolume
    MAX_ALARM_VOLUME: KeypadCombi.SirenAlarmVolume
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_BUZZER_STATE_INFO: _ClassVar[KeypadCombi.BuzzerState]
        OFF_BUZZER_STATE: _ClassVar[KeypadCombi.BuzzerState]
        ON_BUZZER_STATE: _ClassVar[KeypadCombi.BuzzerState]
        WAIT_STOP_BUZZER_STATE: _ClassVar[KeypadCombi.BuzzerState]
        WAIT_START_BUZZER_STATE: _ClassVar[KeypadCombi.BuzzerState]
    NOT_BUZZER_STATE_INFO: KeypadCombi.BuzzerState
    OFF_BUZZER_STATE: KeypadCombi.BuzzerState
    ON_BUZZER_STATE: KeypadCombi.BuzzerState
    WAIT_STOP_BUZZER_STATE: KeypadCombi.BuzzerState
    WAIT_START_BUZZER_STATE: KeypadCombi.BuzzerState
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[KeypadCombi.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[KeypadCombi.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[KeypadCombi.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[KeypadCombi.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[KeypadCombi.BeepOnArmDisarm]
    NO_BEEP_ON_ARM_DISARM_INFO: KeypadCombi.BeepOnArmDisarm
    BEEP_ON_ARM: KeypadCombi.BeepOnArmDisarm
    BEEP_ON_DISARM: KeypadCombi.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: KeypadCombi.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: KeypadCombi.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[KeypadCombi.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[KeypadCombi.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[KeypadCombi.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[KeypadCombi.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[KeypadCombi.BeepOnDelay]
    NO_BEEP_ON_DELAY_INFO: KeypadCombi.BeepOnDelay
    BEEP_ON_ARM_DELAY: KeypadCombi.BeepOnDelay
    BEEP_ON_DISARM_DELAY: KeypadCombi.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: KeypadCombi.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: KeypadCombi.BeepOnDelay
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[KeypadCombi.Subtype]
    NO_SUBTYPE: KeypadCombi.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROFILES_FIELD_NUMBER: _ClassVar[int]
    STAR_BUTTON_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    FORCE_DISARM_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ON_MULTIPLE_PASSWORD_FAILURES_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_BLOCK_ON_MULTIPLE_PASSWORD_FAILURES_MINUTES_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FAST_ARMING_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_DURESS_FIELD_NUMBER: _ClassVar[int]
    ARM_INVERSION_FIELD_NUMBER: _ClassVar[int]
    NFC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_V2_FIELD_NUMBER: _ClassVar[int]
    SIREN_EVENTS_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ACT_ON_ARMING_FIELD_NUMBER: _ClassVar[int]
    ACT_ON_ARMING_V2_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_ACT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SIREN_ALARM_VOLUME_FIELD_NUMBER: _ClassVar[int]
    CHIMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COUNT_PROTECT_FIELD_NUMBER: _ClassVar[int]
    BUZZER_STATE_FIELD_NUMBER: _ClassVar[int]
    SIREN_ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[KeypadCombi.SirenTrigger]
    access_profiles: _containers.RepeatedScalarFieldContainer[KeypadCombi.AccessProfile]
    star_button_function: KeypadCombi.StarButtonFunction
    password: str
    force_disarm_password: str
    block_on_multiple_password_failures: bool
    time_to_block_on_multiple_password_failures_minutes: int
    blocked: _wrappers_pb2.BoolValue
    allow_fast_arming: bool
    brightness_level: int
    volume_level: int
    associated_group_id: str
    password_hash: str
    password_hash_duress: str
    arm_inversion: bool
    nfc_enabled: bool
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[KeypadCombi.BeepOnDelay]
    siren_events_volume: int
    act_on_arming: bool
    act_on_arming_v2: _containers.RepeatedScalarFieldContainer[KeypadCombi.BeepOnArmDisarm]
    time_to_act_seconds: int
    siren_alarm_volume: KeypadCombi.SirenAlarmVolume
    chimes_enabled: bool
    count_protect: int
    buzzer_state: KeypadCombi.BuzzerState
    siren_associated_group_id: str
    subtype: KeypadCombi.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[KeypadCombi.SirenTrigger, str]]] = ..., access_profiles: _Optional[_Iterable[_Union[KeypadCombi.AccessProfile, str]]] = ..., star_button_function: _Optional[_Union[KeypadCombi.StarButtonFunction, str]] = ..., password: _Optional[str] = ..., force_disarm_password: _Optional[str] = ..., block_on_multiple_password_failures: bool = ..., time_to_block_on_multiple_password_failures_minutes: _Optional[int] = ..., blocked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., allow_fast_arming: bool = ..., brightness_level: _Optional[int] = ..., volume_level: _Optional[int] = ..., associated_group_id: _Optional[str] = ..., password_hash: _Optional[str] = ..., password_hash_duress: _Optional[str] = ..., arm_inversion: bool = ..., nfc_enabled: bool = ..., beep_on_delay: bool = ..., beep_on_delay_v2: _Optional[_Iterable[_Union[KeypadCombi.BeepOnDelay, str]]] = ..., siren_events_volume: _Optional[int] = ..., act_on_arming: bool = ..., act_on_arming_v2: _Optional[_Iterable[_Union[KeypadCombi.BeepOnArmDisarm, str]]] = ..., time_to_act_seconds: _Optional[int] = ..., siren_alarm_volume: _Optional[_Union[KeypadCombi.SirenAlarmVolume, str]] = ..., chimes_enabled: bool = ..., count_protect: _Optional[int] = ..., buzzer_state: _Optional[_Union[KeypadCombi.BuzzerState, str]] = ..., siren_associated_group_id: _Optional[str] = ..., subtype: _Optional[_Union[KeypadCombi.Subtype, str]] = ...) -> None: ...
