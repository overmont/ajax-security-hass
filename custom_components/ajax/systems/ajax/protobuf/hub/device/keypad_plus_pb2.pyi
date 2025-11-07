from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeypadPlus(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "access_profiles", "star_button_function", "password", "force_disarm_password", "block_on_multiple_password_failures", "time_to_block_on_multiple_password_failures_minutes", "blocked", "allow_fast_arming", "brightness_level", "volume_level", "associated_group_id", "password_hash", "password_hash_duress", "arm_inversion", "nfc_enabled", "ble_enabled", "ble_sensitivity", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[KeypadPlus.SirenTrigger]
        SECURITY_BUTTON: _ClassVar[KeypadPlus.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: KeypadPlus.SirenTrigger
    SECURITY_BUTTON: KeypadPlus.SirenTrigger
    class StarButtonFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STAR_BUTTON_FUNCTION_INFO: _ClassVar[KeypadPlus.StarButtonFunction]
        DISABLED: _ClassVar[KeypadPlus.StarButtonFunction]
        PANIC: _ClassVar[KeypadPlus.StarButtonFunction]
        MUTE_FIRE_ALARM: _ClassVar[KeypadPlus.StarButtonFunction]
    NO_STAR_BUTTON_FUNCTION_INFO: KeypadPlus.StarButtonFunction
    DISABLED: KeypadPlus.StarButtonFunction
    PANIC: KeypadPlus.StarButtonFunction
    MUTE_FIRE_ALARM: KeypadPlus.StarButtonFunction
    class AccessProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACCESS_PROFILE_INFO: _ClassVar[KeypadPlus.AccessProfile]
        KEYBOARD_PASSWORD: _ClassVar[KeypadPlus.AccessProfile]
        USER_PASSWORD: _ClassVar[KeypadPlus.AccessProfile]
    NO_ACCESS_PROFILE_INFO: KeypadPlus.AccessProfile
    KEYBOARD_PASSWORD: KeypadPlus.AccessProfile
    USER_PASSWORD: KeypadPlus.AccessProfile
    class BleSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BLE_SENSITIVITY: _ClassVar[KeypadPlus.BleSensitivity]
        WELL_BELLOW_AVERAGE: _ClassVar[KeypadPlus.BleSensitivity]
        BELLOW_AVERAGE: _ClassVar[KeypadPlus.BleSensitivity]
        AVERAGE: _ClassVar[KeypadPlus.BleSensitivity]
        ABOVE_AVERAGE: _ClassVar[KeypadPlus.BleSensitivity]
        WELL_ABOVE_AVERAGE: _ClassVar[KeypadPlus.BleSensitivity]
    NO_BLE_SENSITIVITY: KeypadPlus.BleSensitivity
    WELL_BELLOW_AVERAGE: KeypadPlus.BleSensitivity
    BELLOW_AVERAGE: KeypadPlus.BleSensitivity
    AVERAGE: KeypadPlus.BleSensitivity
    ABOVE_AVERAGE: KeypadPlus.BleSensitivity
    WELL_ABOVE_AVERAGE: KeypadPlus.BleSensitivity
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[KeypadPlus.Subtype]
        S_PLUS: _ClassVar[KeypadPlus.Subtype]
    NO_SUBTYPE: KeypadPlus.Subtype
    S_PLUS: KeypadPlus.Subtype
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
    BLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLE_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[KeypadPlus.SirenTrigger]
    access_profiles: _containers.RepeatedScalarFieldContainer[KeypadPlus.AccessProfile]
    star_button_function: KeypadPlus.StarButtonFunction
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
    ble_enabled: bool
    ble_sensitivity: KeypadPlus.BleSensitivity
    subtype: KeypadPlus.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[KeypadPlus.SirenTrigger, str]]] = ..., access_profiles: _Optional[_Iterable[_Union[KeypadPlus.AccessProfile, str]]] = ..., star_button_function: _Optional[_Union[KeypadPlus.StarButtonFunction, str]] = ..., password: _Optional[str] = ..., force_disarm_password: _Optional[str] = ..., block_on_multiple_password_failures: bool = ..., time_to_block_on_multiple_password_failures_minutes: _Optional[int] = ..., blocked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., allow_fast_arming: bool = ..., brightness_level: _Optional[int] = ..., volume_level: _Optional[int] = ..., associated_group_id: _Optional[str] = ..., password_hash: _Optional[str] = ..., password_hash_duress: _Optional[str] = ..., arm_inversion: bool = ..., nfc_enabled: bool = ..., ble_enabled: bool = ..., ble_sensitivity: _Optional[_Union[KeypadPlus.BleSensitivity, str]] = ..., subtype: _Optional[_Union[KeypadPlus.Subtype, str]] = ...) -> None: ...
