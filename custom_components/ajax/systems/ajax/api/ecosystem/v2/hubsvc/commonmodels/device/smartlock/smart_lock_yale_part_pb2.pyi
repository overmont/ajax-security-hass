from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_chimes_pb2 as _device_chimes_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import patch_type_pb2 as _patch_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockYalePart(_message.Message):
    __slots__ = ("model_type", "hw_version", "keyboard_status", "secure_mode", "door_bell_device_chimes", "loudness", "language", "alarm_mode", "user_code_blocking", "fw_version")
    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[SmartLockYalePart.ModelType]
        MODEL_TYPE_DOORMAN_L3S: _ClassVar[SmartLockYalePart.ModelType]
        MODEL_TYPE_DOORMAN_V2N: _ClassVar[SmartLockYalePart.ModelType]
    MODEL_TYPE_UNSPECIFIED: SmartLockYalePart.ModelType
    MODEL_TYPE_DOORMAN_L3S: SmartLockYalePart.ModelType
    MODEL_TYPE_DOORMAN_V2N: SmartLockYalePart.ModelType
    class KeyboardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEYBOARD_STATUS_UNSPECIFIED: _ClassVar[SmartLockYalePart.KeyboardStatus]
        KEYBOARD_STATUS_UNLOCKED: _ClassVar[SmartLockYalePart.KeyboardStatus]
        KEYBOARD_STATUS_LOCKED: _ClassVar[SmartLockYalePart.KeyboardStatus]
    KEYBOARD_STATUS_UNSPECIFIED: SmartLockYalePart.KeyboardStatus
    KEYBOARD_STATUS_UNLOCKED: SmartLockYalePart.KeyboardStatus
    KEYBOARD_STATUS_LOCKED: SmartLockYalePart.KeyboardStatus
    class SecureMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURE_MODE_UNSPECIFIED: _ClassVar[SmartLockYalePart.SecureMode]
        SECURE_MODE_DISABLED: _ClassVar[SmartLockYalePart.SecureMode]
        SECURE_MODE_ENABLED: _ClassVar[SmartLockYalePart.SecureMode]
    SECURE_MODE_UNSPECIFIED: SmartLockYalePart.SecureMode
    SECURE_MODE_DISABLED: SmartLockYalePart.SecureMode
    SECURE_MODE_ENABLED: SmartLockYalePart.SecureMode
    class Loudness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOUDNESS_UNSPECIFIED: _ClassVar[SmartLockYalePart.Loudness]
        LOUDNESS_LOW: _ClassVar[SmartLockYalePart.Loudness]
        LOUDNESS_MEDIUM: _ClassVar[SmartLockYalePart.Loudness]
        LOUDNESS_MAX: _ClassVar[SmartLockYalePart.Loudness]
    LOUDNESS_UNSPECIFIED: SmartLockYalePart.Loudness
    LOUDNESS_LOW: SmartLockYalePart.Loudness
    LOUDNESS_MEDIUM: SmartLockYalePart.Loudness
    LOUDNESS_MAX: SmartLockYalePart.Loudness
    class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LANGUAGE_UNSPECIFIED: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_ARABIC: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_ENGLISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_FRENCH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_SPANISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_DANISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_NORWEGIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_SWEDISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_FINNISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_RUSSIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_CHINESE: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_DUTCH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_GERMAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_GREEK: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_ITALIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_POLISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_PORTUGUESE: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_TURKISH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_CZECH: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_SLOVAK: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_BULGARIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_HUNGARIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_ROMANIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_BELORUSSIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_UKRAINIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_ESTONIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_LITHUANIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_LATVIAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_KOREAN: _ClassVar[SmartLockYalePart.Language]
        LANGUAGE_JAPANESE: _ClassVar[SmartLockYalePart.Language]
    LANGUAGE_UNSPECIFIED: SmartLockYalePart.Language
    LANGUAGE_ARABIC: SmartLockYalePart.Language
    LANGUAGE_ENGLISH: SmartLockYalePart.Language
    LANGUAGE_FRENCH: SmartLockYalePart.Language
    LANGUAGE_SPANISH: SmartLockYalePart.Language
    LANGUAGE_DANISH: SmartLockYalePart.Language
    LANGUAGE_NORWEGIAN: SmartLockYalePart.Language
    LANGUAGE_SWEDISH: SmartLockYalePart.Language
    LANGUAGE_FINNISH: SmartLockYalePart.Language
    LANGUAGE_RUSSIAN: SmartLockYalePart.Language
    LANGUAGE_CHINESE: SmartLockYalePart.Language
    LANGUAGE_DUTCH: SmartLockYalePart.Language
    LANGUAGE_GERMAN: SmartLockYalePart.Language
    LANGUAGE_GREEK: SmartLockYalePart.Language
    LANGUAGE_ITALIAN: SmartLockYalePart.Language
    LANGUAGE_POLISH: SmartLockYalePart.Language
    LANGUAGE_PORTUGUESE: SmartLockYalePart.Language
    LANGUAGE_TURKISH: SmartLockYalePart.Language
    LANGUAGE_CZECH: SmartLockYalePart.Language
    LANGUAGE_SLOVAK: SmartLockYalePart.Language
    LANGUAGE_BULGARIAN: SmartLockYalePart.Language
    LANGUAGE_HUNGARIAN: SmartLockYalePart.Language
    LANGUAGE_ROMANIAN: SmartLockYalePart.Language
    LANGUAGE_BELORUSSIAN: SmartLockYalePart.Language
    LANGUAGE_UKRAINIAN: SmartLockYalePart.Language
    LANGUAGE_ESTONIAN: SmartLockYalePart.Language
    LANGUAGE_LITHUANIAN: SmartLockYalePart.Language
    LANGUAGE_LATVIAN: SmartLockYalePart.Language
    LANGUAGE_KOREAN: SmartLockYalePart.Language
    LANGUAGE_JAPANESE: SmartLockYalePart.Language
    class AlarmMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_MODE_UNSPECIFIED: _ClassVar[SmartLockYalePart.AlarmMode]
        ALARM_MODE_DISABLED: _ClassVar[SmartLockYalePart.AlarmMode]
        ALARM_MODE_HOME_MODE: _ClassVar[SmartLockYalePart.AlarmMode]
        ALARM_MODE_AWAY_MODE: _ClassVar[SmartLockYalePart.AlarmMode]
    ALARM_MODE_UNSPECIFIED: SmartLockYalePart.AlarmMode
    ALARM_MODE_DISABLED: SmartLockYalePart.AlarmMode
    ALARM_MODE_HOME_MODE: SmartLockYalePart.AlarmMode
    ALARM_MODE_AWAY_MODE: SmartLockYalePart.AlarmMode
    class UserCodeBlocking(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_CODE_BLOCKING_UNSPECIFIED: _ClassVar[SmartLockYalePart.UserCodeBlocking]
        USER_CODE_BLOCKING_DISABLED: _ClassVar[SmartLockYalePart.UserCodeBlocking]
        USER_CODE_BLOCKING_ENABLED: _ClassVar[SmartLockYalePart.UserCodeBlocking]
    USER_CODE_BLOCKING_UNSPECIFIED: SmartLockYalePart.UserCodeBlocking
    USER_CODE_BLOCKING_DISABLED: SmartLockYalePart.UserCodeBlocking
    USER_CODE_BLOCKING_ENABLED: SmartLockYalePart.UserCodeBlocking
    class DoorBellDeviceChimes(_message.Message):
        __slots__ = ("chimes_triggers", "chimes_sound")
        class DoorBellChimesTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DOOR_BELL_CHIMES_TRIGGER_UNSPECIFIED: _ClassVar[SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger]
            DOOR_BELL_CHIMES_TRIGGER_BUTTON: _ClassVar[SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger]
        DOOR_BELL_CHIMES_TRIGGER_UNSPECIFIED: SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger
        DOOR_BELL_CHIMES_TRIGGER_BUTTON: SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger
        CHIMES_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        CHIMES_SOUND_FIELD_NUMBER: _ClassVar[int]
        chimes_triggers: _containers.RepeatedScalarFieldContainer[SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger]
        chimes_sound: _device_chimes_pb2.DeviceChimes.Sound
        def __init__(self, chimes_triggers: _Optional[_Iterable[_Union[SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger, str]]] = ..., chimes_sound: _Optional[_Union[_device_chimes_pb2.DeviceChimes.Sound, str]] = ...) -> None: ...
    class SmartLockYalePartSettings(_message.Message):
        __slots__ = ("door_bell_device_chimes", "loudness", "language", "alarm_mode", "user_code_blocking")
        class DoorBellDeviceChimesSettings(_message.Message):
            __slots__ = ("chimes_triggers", "chimes_sound")
            class DoorBellChimesTriggerPatch(_message.Message):
                __slots__ = ("patch_type", "chimes_trigger")
                PATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
                CHIMES_TRIGGER_FIELD_NUMBER: _ClassVar[int]
                patch_type: _patch_type_pb2.PatchType
                chimes_trigger: SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger
                def __init__(self, patch_type: _Optional[_Union[_patch_type_pb2.PatchType, str]] = ..., chimes_trigger: _Optional[_Union[SmartLockYalePart.DoorBellDeviceChimes.DoorBellChimesTrigger, str]] = ...) -> None: ...
            CHIMES_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
            CHIMES_SOUND_FIELD_NUMBER: _ClassVar[int]
            chimes_triggers: _containers.RepeatedCompositeFieldContainer[SmartLockYalePart.SmartLockYalePartSettings.DoorBellDeviceChimesSettings.DoorBellChimesTriggerPatch]
            chimes_sound: _device_chimes_pb2.DeviceChimes.Sound
            def __init__(self, chimes_triggers: _Optional[_Iterable[_Union[SmartLockYalePart.SmartLockYalePartSettings.DoorBellDeviceChimesSettings.DoorBellChimesTriggerPatch, _Mapping]]] = ..., chimes_sound: _Optional[_Union[_device_chimes_pb2.DeviceChimes.Sound, str]] = ...) -> None: ...
        DOOR_BELL_DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
        LOUDNESS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        ALARM_MODE_FIELD_NUMBER: _ClassVar[int]
        USER_CODE_BLOCKING_FIELD_NUMBER: _ClassVar[int]
        door_bell_device_chimes: SmartLockYalePart.SmartLockYalePartSettings.DoorBellDeviceChimesSettings
        loudness: SmartLockYalePart.Loudness
        language: SmartLockYalePart.Language
        alarm_mode: SmartLockYalePart.AlarmMode
        user_code_blocking: SmartLockYalePart.UserCodeBlocking
        def __init__(self, door_bell_device_chimes: _Optional[_Union[SmartLockYalePart.SmartLockYalePartSettings.DoorBellDeviceChimesSettings, _Mapping]] = ..., loudness: _Optional[_Union[SmartLockYalePart.Loudness, str]] = ..., language: _Optional[_Union[SmartLockYalePart.Language, str]] = ..., alarm_mode: _Optional[_Union[SmartLockYalePart.AlarmMode, str]] = ..., user_code_blocking: _Optional[_Union[SmartLockYalePart.UserCodeBlocking, str]] = ...) -> None: ...
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    SECURE_MODE_FIELD_NUMBER: _ClassVar[int]
    DOOR_BELL_DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
    LOUDNESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ALARM_MODE_FIELD_NUMBER: _ClassVar[int]
    USER_CODE_BLOCKING_FIELD_NUMBER: _ClassVar[int]
    FW_VERSION_FIELD_NUMBER: _ClassVar[int]
    model_type: SmartLockYalePart.ModelType
    hw_version: str
    keyboard_status: SmartLockYalePart.KeyboardStatus
    secure_mode: SmartLockYalePart.SecureMode
    door_bell_device_chimes: SmartLockYalePart.DoorBellDeviceChimes
    loudness: SmartLockYalePart.Loudness
    language: SmartLockYalePart.Language
    alarm_mode: SmartLockYalePart.AlarmMode
    user_code_blocking: SmartLockYalePart.UserCodeBlocking
    fw_version: str
    def __init__(self, model_type: _Optional[_Union[SmartLockYalePart.ModelType, str]] = ..., hw_version: _Optional[str] = ..., keyboard_status: _Optional[_Union[SmartLockYalePart.KeyboardStatus, str]] = ..., secure_mode: _Optional[_Union[SmartLockYalePart.SecureMode, str]] = ..., door_bell_device_chimes: _Optional[_Union[SmartLockYalePart.DoorBellDeviceChimes, _Mapping]] = ..., loudness: _Optional[_Union[SmartLockYalePart.Loudness, str]] = ..., language: _Optional[_Union[SmartLockYalePart.Language, str]] = ..., alarm_mode: _Optional[_Union[SmartLockYalePart.AlarmMode, str]] = ..., user_code_blocking: _Optional[_Union[SmartLockYalePart.UserCodeBlocking, str]] = ..., fw_version: _Optional[str] = ...) -> None: ...
