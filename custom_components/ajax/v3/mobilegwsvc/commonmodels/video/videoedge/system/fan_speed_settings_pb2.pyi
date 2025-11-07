from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FanSpeedSettings(_message.Message):
    __slots__ = ("auto", "manual")
    class FanSpeedSettingsAutoMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class FanSpeedSettingsManualMode(_message.Message):
        __slots__ = ("preset",)
        class FanSpeedSettingsManualPreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FAN_SPEED_SETTINGS_MANUAL_PRESET_UNSPECIFIED: _ClassVar[FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset]
            FAN_SPEED_SETTINGS_MANUAL_PRESET_LOW: _ClassVar[FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset]
            FAN_SPEED_SETTINGS_MANUAL_PRESET_MEDIUM: _ClassVar[FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset]
            FAN_SPEED_SETTINGS_MANUAL_PRESET_HIGH: _ClassVar[FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset]
        FAN_SPEED_SETTINGS_MANUAL_PRESET_UNSPECIFIED: FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset
        FAN_SPEED_SETTINGS_MANUAL_PRESET_LOW: FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset
        FAN_SPEED_SETTINGS_MANUAL_PRESET_MEDIUM: FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset
        FAN_SPEED_SETTINGS_MANUAL_PRESET_HIGH: FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset
        PRESET_FIELD_NUMBER: _ClassVar[int]
        preset: FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset
        def __init__(self, preset: _Optional[_Union[FanSpeedSettings.FanSpeedSettingsManualMode.FanSpeedSettingsManualPreset, str]] = ...) -> None: ...
    AUTO_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    auto: FanSpeedSettings.FanSpeedSettingsAutoMode
    manual: FanSpeedSettings.FanSpeedSettingsManualMode
    def __init__(self, auto: _Optional[_Union[FanSpeedSettings.FanSpeedSettingsAutoMode, _Mapping]] = ..., manual: _Optional[_Union[FanSpeedSettings.FanSpeedSettingsManualMode, _Mapping]] = ...) -> None: ...
