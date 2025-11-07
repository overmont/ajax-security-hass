from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_fire_zone_pb2 as _device_fire_zone_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonEn54Part(_message.Message):
    __slots__ = ("device_temperature", "fire_zone", "device_tamper_status", "description_malfunctions", "disablement_state")
    class DescriptionMalfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESCRIPTION_MALFUNCTION_BIT_MASK_UNSPECIFIED: _ClassVar[CommonEn54Part.DescriptionMalfunction]
        DESCRIPTION_MALFUNCTION_BIT_MASK_CAMERA_DUSTY: _ClassVar[CommonEn54Part.DescriptionMalfunction]
        DESCRIPTION_MALFUNCTION_BIT_MASK_SMOKE_FAULT: _ClassVar[CommonEn54Part.DescriptionMalfunction]
        DESCRIPTION_MALFUNCTION_BIT_MASK_TEMP_FAULT: _ClassVar[CommonEn54Part.DescriptionMalfunction]
        DESCRIPTION_MALFUNCTION_BIT_MASK_SOUNDER_FAULT: _ClassVar[CommonEn54Part.DescriptionMalfunction]
        DESCRIPTION_MALFUNCTION_BIT_MASK_VAD_FAULT: _ClassVar[CommonEn54Part.DescriptionMalfunction]
    DESCRIPTION_MALFUNCTION_BIT_MASK_UNSPECIFIED: CommonEn54Part.DescriptionMalfunction
    DESCRIPTION_MALFUNCTION_BIT_MASK_CAMERA_DUSTY: CommonEn54Part.DescriptionMalfunction
    DESCRIPTION_MALFUNCTION_BIT_MASK_SMOKE_FAULT: CommonEn54Part.DescriptionMalfunction
    DESCRIPTION_MALFUNCTION_BIT_MASK_TEMP_FAULT: CommonEn54Part.DescriptionMalfunction
    DESCRIPTION_MALFUNCTION_BIT_MASK_SOUNDER_FAULT: CommonEn54Part.DescriptionMalfunction
    DESCRIPTION_MALFUNCTION_BIT_MASK_VAD_FAULT: CommonEn54Part.DescriptionMalfunction
    class DisablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISABLEMENT_STATE_UNSPECIFIED: _ClassVar[CommonEn54Part.DisablementState]
        DISABLEMENT_STATE_SMOKE_DETECTOR: _ClassVar[CommonEn54Part.DisablementState]
        DISABLEMENT_STATE_HEAT_TEMP_DETECTOR: _ClassVar[CommonEn54Part.DisablementState]
        DISABLEMENT_STATE_SOUNDER: _ClassVar[CommonEn54Part.DisablementState]
        DISABLEMENT_STATE_VAD: _ClassVar[CommonEn54Part.DisablementState]
    DISABLEMENT_STATE_UNSPECIFIED: CommonEn54Part.DisablementState
    DISABLEMENT_STATE_SMOKE_DETECTOR: CommonEn54Part.DisablementState
    DISABLEMENT_STATE_HEAT_TEMP_DETECTOR: CommonEn54Part.DisablementState
    DISABLEMENT_STATE_SOUNDER: CommonEn54Part.DisablementState
    DISABLEMENT_STATE_VAD: CommonEn54Part.DisablementState
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    device_temperature: _device_temperature_pb2.DeviceTemperature
    fire_zone: _device_fire_zone_pb2.FireZoneDeviceRepresentation
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    description_malfunctions: _containers.RepeatedScalarFieldContainer[CommonEn54Part.DescriptionMalfunction]
    disablement_state: _containers.RepeatedScalarFieldContainer[CommonEn54Part.DisablementState]
    def __init__(self, device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., fire_zone: _Optional[_Union[_device_fire_zone_pb2.FireZoneDeviceRepresentation, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., description_malfunctions: _Optional[_Iterable[_Union[CommonEn54Part.DescriptionMalfunction, str]]] = ..., disablement_state: _Optional[_Iterable[_Union[CommonEn54Part.DisablementState, str]]] = ...) -> None: ...

class CommonEn54SounderPart(_message.Message):
    __slots__ = ("alarm_status_sounder", "sounder_volume")
    class SounderVolume(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOUNDER_VOLUME_UNSPECIFIED: _ClassVar[CommonEn54SounderPart.SounderVolume]
        SOUNDER_VOLUME_LOW: _ClassVar[CommonEn54SounderPart.SounderVolume]
        SOUNDER_VOLUME_MEDIUM: _ClassVar[CommonEn54SounderPart.SounderVolume]
        SOUNDER_VOLUME_HIGH: _ClassVar[CommonEn54SounderPart.SounderVolume]
    SOUNDER_VOLUME_UNSPECIFIED: CommonEn54SounderPart.SounderVolume
    SOUNDER_VOLUME_LOW: CommonEn54SounderPart.SounderVolume
    SOUNDER_VOLUME_MEDIUM: CommonEn54SounderPart.SounderVolume
    SOUNDER_VOLUME_HIGH: CommonEn54SounderPart.SounderVolume
    class AlarmStatusSounder(_message.Message):
        __slots__ = ("sounder_alarm_state", "sounder_pattern", "sounder_sync_state", "sounder_silence_state")
        class SounderAlarmState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOUNDER_ALARM_STATE_UNSPECIFIED: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState]
            SOUNDER_ALARM_STATE_INACTIVE: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState]
            SOUNDER_ALARM_STATE_ACTIVE: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState]
        SOUNDER_ALARM_STATE_UNSPECIFIED: CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState
        SOUNDER_ALARM_STATE_INACTIVE: CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState
        SOUNDER_ALARM_STATE_ACTIVE: CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState
        class SounderSyncState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOUNDER_SYNC_STATE_UNSPECIFIED: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState]
            SOUNDER_SYNC_STATE_OUT_OF_SYNC: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState]
            SOUNDER_SYNC_STATE_SYNCHRONIZED: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState]
        SOUNDER_SYNC_STATE_UNSPECIFIED: CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState
        SOUNDER_SYNC_STATE_OUT_OF_SYNC: CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState
        SOUNDER_SYNC_STATE_SYNCHRONIZED: CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState
        class SounderSilenceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOUNDER_SILENCE_STATE_UNSPECIFIED: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState]
            SOUNDER_SILENCE_STATE_NOT_ACTIVE: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState]
            SOUNDER_SILENCE_STATE_ACTIVE: _ClassVar[CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState]
        SOUNDER_SILENCE_STATE_UNSPECIFIED: CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState
        SOUNDER_SILENCE_STATE_NOT_ACTIVE: CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState
        SOUNDER_SILENCE_STATE_ACTIVE: CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState
        SOUNDER_ALARM_STATE_FIELD_NUMBER: _ClassVar[int]
        SOUNDER_PATTERN_FIELD_NUMBER: _ClassVar[int]
        SOUNDER_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
        SOUNDER_SILENCE_STATE_FIELD_NUMBER: _ClassVar[int]
        sounder_alarm_state: CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState
        sounder_pattern: int
        sounder_sync_state: CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState
        sounder_silence_state: CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState
        def __init__(self, sounder_alarm_state: _Optional[_Union[CommonEn54SounderPart.AlarmStatusSounder.SounderAlarmState, str]] = ..., sounder_pattern: _Optional[int] = ..., sounder_sync_state: _Optional[_Union[CommonEn54SounderPart.AlarmStatusSounder.SounderSyncState, str]] = ..., sounder_silence_state: _Optional[_Union[CommonEn54SounderPart.AlarmStatusSounder.SounderSilenceState, str]] = ...) -> None: ...
    ALARM_STATUS_SOUNDER_FIELD_NUMBER: _ClassVar[int]
    SOUNDER_VOLUME_FIELD_NUMBER: _ClassVar[int]
    alarm_status_sounder: CommonEn54SounderPart.AlarmStatusSounder
    sounder_volume: CommonEn54SounderPart.SounderVolume
    def __init__(self, alarm_status_sounder: _Optional[_Union[CommonEn54SounderPart.AlarmStatusSounder, _Mapping]] = ..., sounder_volume: _Optional[_Union[CommonEn54SounderPart.SounderVolume, str]] = ...) -> None: ...

class CommonEn54VadPart(_message.Message):
    __slots__ = ("alarm_status_vad",)
    class AlarmStatusVad(_message.Message):
        __slots__ = ("vad_alarm_state", "vad_patterns", "vad_sync_state", "vad_silence_state")
        class VadAlarmState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VAD_ALARM_STATE_UNSPECIFIED: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadAlarmState]
            VAD_ALARM_STATE_INACTIVE: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadAlarmState]
            VAD_ALARM_STATE_ACTIVE: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadAlarmState]
        VAD_ALARM_STATE_UNSPECIFIED: CommonEn54VadPart.AlarmStatusVad.VadAlarmState
        VAD_ALARM_STATE_INACTIVE: CommonEn54VadPart.AlarmStatusVad.VadAlarmState
        VAD_ALARM_STATE_ACTIVE: CommonEn54VadPart.AlarmStatusVad.VadAlarmState
        class VadSyncState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VAD_SYNC_STATE_UNSPECIFIED: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSyncState]
            VAD_SYNC_STATE_OUT_OF_SYNC: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSyncState]
            VAD_SYNC_STATE_SYNCHRONIZED: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSyncState]
        VAD_SYNC_STATE_UNSPECIFIED: CommonEn54VadPart.AlarmStatusVad.VadSyncState
        VAD_SYNC_STATE_OUT_OF_SYNC: CommonEn54VadPart.AlarmStatusVad.VadSyncState
        VAD_SYNC_STATE_SYNCHRONIZED: CommonEn54VadPart.AlarmStatusVad.VadSyncState
        class VadSilenceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VAD_SILENCE_STATE_UNSPECIFIED: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSilenceState]
            VAD_SILENCE_STATE_NOT_ACTIVE: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSilenceState]
            VAD_SILENCE_STATE_ACTIVE: _ClassVar[CommonEn54VadPart.AlarmStatusVad.VadSilenceState]
        VAD_SILENCE_STATE_UNSPECIFIED: CommonEn54VadPart.AlarmStatusVad.VadSilenceState
        VAD_SILENCE_STATE_NOT_ACTIVE: CommonEn54VadPart.AlarmStatusVad.VadSilenceState
        VAD_SILENCE_STATE_ACTIVE: CommonEn54VadPart.AlarmStatusVad.VadSilenceState
        VAD_ALARM_STATE_FIELD_NUMBER: _ClassVar[int]
        VAD_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        VAD_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
        VAD_SILENCE_STATE_FIELD_NUMBER: _ClassVar[int]
        vad_alarm_state: CommonEn54VadPart.AlarmStatusVad.VadAlarmState
        vad_patterns: int
        vad_sync_state: CommonEn54VadPart.AlarmStatusVad.VadSyncState
        vad_silence_state: CommonEn54VadPart.AlarmStatusVad.VadSilenceState
        def __init__(self, vad_alarm_state: _Optional[_Union[CommonEn54VadPart.AlarmStatusVad.VadAlarmState, str]] = ..., vad_patterns: _Optional[int] = ..., vad_sync_state: _Optional[_Union[CommonEn54VadPart.AlarmStatusVad.VadSyncState, str]] = ..., vad_silence_state: _Optional[_Union[CommonEn54VadPart.AlarmStatusVad.VadSilenceState, str]] = ...) -> None: ...
    ALARM_STATUS_VAD_FIELD_NUMBER: _ClassVar[int]
    alarm_status_vad: CommonEn54VadPart.AlarmStatusVad
    def __init__(self, alarm_status_vad: _Optional[_Union[CommonEn54VadPart.AlarmStatusVad, _Mapping]] = ...) -> None: ...

class CommonEn54HeatPart(_message.Message):
    __slots__ = ("temp_alarm", "temp_high_diff_alarm", "heat_sensor_mode", "heat_sensor_fixed_temp")
    class TempAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEMP_ALARM_UNSPECIFIED: _ClassVar[CommonEn54HeatPart.TempAlarm]
        TEMP_ALARM_NOT_DETECTED: _ClassVar[CommonEn54HeatPart.TempAlarm]
        TEMP_ALARM_DETECTED: _ClassVar[CommonEn54HeatPart.TempAlarm]
    TEMP_ALARM_UNSPECIFIED: CommonEn54HeatPart.TempAlarm
    TEMP_ALARM_NOT_DETECTED: CommonEn54HeatPart.TempAlarm
    TEMP_ALARM_DETECTED: CommonEn54HeatPart.TempAlarm
    class TempHighDiffAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEMP_HIGH_DIFF_ALARM_UNSPECIFIED: _ClassVar[CommonEn54HeatPart.TempHighDiffAlarm]
        TEMP_HIGH_DIFF_ALARM_NOT_DETECTED: _ClassVar[CommonEn54HeatPart.TempHighDiffAlarm]
        TEMP_HIGH_DIFF_ALARM_DETECTED: _ClassVar[CommonEn54HeatPart.TempHighDiffAlarm]
    TEMP_HIGH_DIFF_ALARM_UNSPECIFIED: CommonEn54HeatPart.TempHighDiffAlarm
    TEMP_HIGH_DIFF_ALARM_NOT_DETECTED: CommonEn54HeatPart.TempHighDiffAlarm
    TEMP_HIGH_DIFF_ALARM_DETECTED: CommonEn54HeatPart.TempHighDiffAlarm
    class HeatSensorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEAT_SENSOR_MODE_UNSPECIFIED: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_A1R: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_A1: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_A1S: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_B: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_BR: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_BS: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_C: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_CR: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_CS: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
        HEAT_SENSOR_MODE_FIXED_TEMP: _ClassVar[CommonEn54HeatPart.HeatSensorMode]
    HEAT_SENSOR_MODE_UNSPECIFIED: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_A1R: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_A1: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_A1S: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_B: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_BR: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_BS: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_C: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_CR: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_CS: CommonEn54HeatPart.HeatSensorMode
    HEAT_SENSOR_MODE_FIXED_TEMP: CommonEn54HeatPart.HeatSensorMode
    TEMP_ALARM_FIELD_NUMBER: _ClassVar[int]
    TEMP_HIGH_DIFF_ALARM_FIELD_NUMBER: _ClassVar[int]
    HEAT_SENSOR_MODE_FIELD_NUMBER: _ClassVar[int]
    HEAT_SENSOR_FIXED_TEMP_FIELD_NUMBER: _ClassVar[int]
    temp_alarm: CommonEn54HeatPart.TempAlarm
    temp_high_diff_alarm: CommonEn54HeatPart.TempHighDiffAlarm
    heat_sensor_mode: CommonEn54HeatPart.HeatSensorMode
    heat_sensor_fixed_temp: int
    def __init__(self, temp_alarm: _Optional[_Union[CommonEn54HeatPart.TempAlarm, str]] = ..., temp_high_diff_alarm: _Optional[_Union[CommonEn54HeatPart.TempHighDiffAlarm, str]] = ..., heat_sensor_mode: _Optional[_Union[CommonEn54HeatPart.HeatSensorMode, str]] = ..., heat_sensor_fixed_temp: _Optional[int] = ...) -> None: ...

class CommonEn54SmokePart(_message.Message):
    __slots__ = ("smoke_alarm", "steam_alarm", "steam_detector_status")
    class SmokeAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SMOKE_ALARM_UNSPECIFIED: _ClassVar[CommonEn54SmokePart.SmokeAlarm]
        SMOKE_ALARM_NOT_DETECTED: _ClassVar[CommonEn54SmokePart.SmokeAlarm]
        SMOKE_ALARM_DETECTED: _ClassVar[CommonEn54SmokePart.SmokeAlarm]
    SMOKE_ALARM_UNSPECIFIED: CommonEn54SmokePart.SmokeAlarm
    SMOKE_ALARM_NOT_DETECTED: CommonEn54SmokePart.SmokeAlarm
    SMOKE_ALARM_DETECTED: CommonEn54SmokePart.SmokeAlarm
    class SteamAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STEAM_ALARM_UNSPECIFIED: _ClassVar[CommonEn54SmokePart.SteamAlarm]
        STEAM_ALARM_NOT_DETECTED: _ClassVar[CommonEn54SmokePart.SteamAlarm]
        STEAM_ALARM_DETECTED: _ClassVar[CommonEn54SmokePart.SteamAlarm]
    STEAM_ALARM_UNSPECIFIED: CommonEn54SmokePart.SteamAlarm
    STEAM_ALARM_NOT_DETECTED: CommonEn54SmokePart.SteamAlarm
    STEAM_ALARM_DETECTED: CommonEn54SmokePart.SteamAlarm
    class SteamDetectorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STEAM_DETECTOR_STATUS_UNSPECIFIED: _ClassVar[CommonEn54SmokePart.SteamDetectorStatus]
        STEAM_DETECTOR_STATUS_DISABLED: _ClassVar[CommonEn54SmokePart.SteamDetectorStatus]
        STEAM_DETECTOR_STATUS_ENABLED: _ClassVar[CommonEn54SmokePart.SteamDetectorStatus]
    STEAM_DETECTOR_STATUS_UNSPECIFIED: CommonEn54SmokePart.SteamDetectorStatus
    STEAM_DETECTOR_STATUS_DISABLED: CommonEn54SmokePart.SteamDetectorStatus
    STEAM_DETECTOR_STATUS_ENABLED: CommonEn54SmokePart.SteamDetectorStatus
    SMOKE_ALARM_FIELD_NUMBER: _ClassVar[int]
    STEAM_ALARM_FIELD_NUMBER: _ClassVar[int]
    STEAM_DETECTOR_STATUS_FIELD_NUMBER: _ClassVar[int]
    smoke_alarm: CommonEn54SmokePart.SmokeAlarm
    steam_alarm: CommonEn54SmokePart.SteamAlarm
    steam_detector_status: CommonEn54SmokePart.SteamDetectorStatus
    def __init__(self, smoke_alarm: _Optional[_Union[CommonEn54SmokePart.SmokeAlarm, str]] = ..., steam_alarm: _Optional[_Union[CommonEn54SmokePart.SteamAlarm, str]] = ..., steam_detector_status: _Optional[_Union[CommonEn54SmokePart.SteamDetectorStatus, str]] = ...) -> None: ...

class CommonEn54AnnunciationTestPart(_message.Message):
    __slots__ = ("annunciation_test_state", "annunciation_test_endpoints")
    class AnnunciationTestState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANNUNCIATION_TEST_STATE_UNSPECIFIED: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestState]
        ANNUNCIATION_TEST_STATE_INACTIVE: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestState]
        ANNUNCIATION_TEST_STATE_STARTING: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestState]
        ANNUNCIATION_TEST_STATE_ACTIVE: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestState]
        ANNUNCIATION_TEST_STATE_FINISHING: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestState]
    ANNUNCIATION_TEST_STATE_UNSPECIFIED: CommonEn54AnnunciationTestPart.AnnunciationTestState
    ANNUNCIATION_TEST_STATE_INACTIVE: CommonEn54AnnunciationTestPart.AnnunciationTestState
    ANNUNCIATION_TEST_STATE_STARTING: CommonEn54AnnunciationTestPart.AnnunciationTestState
    ANNUNCIATION_TEST_STATE_ACTIVE: CommonEn54AnnunciationTestPart.AnnunciationTestState
    ANNUNCIATION_TEST_STATE_FINISHING: CommonEn54AnnunciationTestPart.AnnunciationTestState
    class AnnunciationTestEndPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANNUNCIATION_TEST_END_POINT_UNSPECIFIED: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint]
        ANNUNCIATION_TEST_END_POINT_SOUNDER_TEST: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint]
        ANNUNCIATION_TEST_END_POINT_VAD_TEST: _ClassVar[CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint]
    ANNUNCIATION_TEST_END_POINT_UNSPECIFIED: CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint
    ANNUNCIATION_TEST_END_POINT_SOUNDER_TEST: CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint
    ANNUNCIATION_TEST_END_POINT_VAD_TEST: CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint
    ANNUNCIATION_TEST_STATE_FIELD_NUMBER: _ClassVar[int]
    ANNUNCIATION_TEST_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    annunciation_test_state: CommonEn54AnnunciationTestPart.AnnunciationTestState
    annunciation_test_endpoints: _containers.RepeatedScalarFieldContainer[CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint]
    def __init__(self, annunciation_test_state: _Optional[_Union[CommonEn54AnnunciationTestPart.AnnunciationTestState, str]] = ..., annunciation_test_endpoints: _Optional[_Iterable[_Union[CommonEn54AnnunciationTestPart.AnnunciationTestEndPoint, str]]] = ...) -> None: ...
