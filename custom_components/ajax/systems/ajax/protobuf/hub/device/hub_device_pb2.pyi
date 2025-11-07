from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from systems.ajax.protobuf.common import decimal_pb2 as _decimal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubDevice(_message.Message):
    __slots__ = ("id", "name", "noise_level", "connection_status", "state", "state_with_groups", "debug_log_state", "panic_siren_on_panic_button", "limits", "groups_enabled", "firmware", "ethernet", "arm_prevention_mode", "tampered", "panic_siren_on_any_tamper", "battery", "hardware_versions", "warnings", "fire_alarm", "wifi", "gsm", "cms", "color", "image_id", "image_num", "image_urls", "active_channels", "ping_period_seconds", "offline_alarm_seconds", "led_brightness_level", "subtype", "jeweller", "externally_powered", "connection_test_in_progress", "malfunctions", "blocked_by_service_provider", "connection_lost_as_malfunction", "alarm_as_malfunction_when_arming", "auto_bypass_timer_minutes", "auto_bypass_counter", "hub_address", "time_zone", "alarm_verification", "restore_required", "alarm_happened", "arm_preventions_to_check", "report_alarm_restore", "report_panic_alarm_restore", "tamper_alarm_confirmation", "confirmed_alarm_on_delayed_devices", "alarm_confirmation_hu_devices_pd6662", "verification_timeout_hu", "interconnection", "postAlarmIndicationRule", "lost_fibra_counter", "chimes_status", "channel_connectivity_notification_active", "channel_offline_alarm_delay_seconds", "photo_on_demand_mode", "default_camera_permission", "default_photo_on_demand_permission", "default_user_camera_permission", "default_user_photo_on_demand_permission", "max_power_test_state", "bus_status", "scan_status", "privacy_officer_options", "geofence", "two_stage_arming_progress_status", "two_stage_arming")
    class DebugLogState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEBUG_LOG_STATE_INFO: _ClassVar[HubDevice.DebugLogState]
        NO_LOGS: _ClassVar[HubDevice.DebugLogState]
        ETHERNET_ONLY: _ClassVar[HubDevice.DebugLogState]
        WIFI_ONLY: _ClassVar[HubDevice.DebugLogState]
        ETHERNET_OR_WIFI: _ClassVar[HubDevice.DebugLogState]
    NO_DEBUG_LOG_STATE_INFO: HubDevice.DebugLogState
    NO_LOGS: HubDevice.DebugLogState
    ETHERNET_ONLY: HubDevice.DebugLogState
    WIFI_ONLY: HubDevice.DebugLogState
    ETHERNET_OR_WIFI: HubDevice.DebugLogState
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE_INFO: _ClassVar[HubDevice.State]
        DISARMED: _ClassVar[HubDevice.State]
        ARMED: _ClassVar[HubDevice.State]
        NIGHT_MODE: _ClassVar[HubDevice.State]
    NO_STATE_INFO: HubDevice.State
    DISARMED: HubDevice.State
    ARMED: HubDevice.State
    NIGHT_MODE: HubDevice.State
    class StateWithGroups(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE_WITH_GROUPS_INFO: _ClassVar[HubDevice.StateWithGroups]
        ARMED_NIGHT_MODE_ON: _ClassVar[HubDevice.StateWithGroups]
        ARMED_NIGHT_MODE_OFF: _ClassVar[HubDevice.StateWithGroups]
        DISARMED_NIGHT_MODE_ON: _ClassVar[HubDevice.StateWithGroups]
        DISARMED_NIGHT_MODE_OFF: _ClassVar[HubDevice.StateWithGroups]
        PARTIALLY_ARMED_NIGHT_MODE_ON: _ClassVar[HubDevice.StateWithGroups]
        PARTIALLY_ARMED_NIGHT_MODE_OFF: _ClassVar[HubDevice.StateWithGroups]
    NO_STATE_WITH_GROUPS_INFO: HubDevice.StateWithGroups
    ARMED_NIGHT_MODE_ON: HubDevice.StateWithGroups
    ARMED_NIGHT_MODE_OFF: HubDevice.StateWithGroups
    DISARMED_NIGHT_MODE_ON: HubDevice.StateWithGroups
    DISARMED_NIGHT_MODE_OFF: HubDevice.StateWithGroups
    PARTIALLY_ARMED_NIGHT_MODE_ON: HubDevice.StateWithGroups
    PARTIALLY_ARMED_NIGHT_MODE_OFF: HubDevice.StateWithGroups
    class ArmPreventionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARM_PREVENTION_MODE_INFO: _ClassVar[HubDevice.ArmPreventionMode]
        IGNORE_WARNINGS: _ClassVar[HubDevice.ArmPreventionMode]
        ALERT_USER: _ClassVar[HubDevice.ArmPreventionMode]
        PREVENT_ARMING: _ClassVar[HubDevice.ArmPreventionMode]
    NO_ARM_PREVENTION_MODE_INFO: HubDevice.ArmPreventionMode
    IGNORE_WARNINGS: HubDevice.ArmPreventionMode
    ALERT_USER: HubDevice.ArmPreventionMode
    PREVENT_ARMING: HubDevice.ArmPreventionMode
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_COLOR_INFO: _ClassVar[HubDevice.Color]
        WHITE: _ClassVar[HubDevice.Color]
        BLACK: _ClassVar[HubDevice.Color]
        WHITE_LABEL_WHITE: _ClassVar[HubDevice.Color]
        WHITE_LABEL_BLACK: _ClassVar[HubDevice.Color]
    NO_COLOR_INFO: HubDevice.Color
    WHITE: HubDevice.Color
    BLACK: HubDevice.Color
    WHITE_LABEL_WHITE: HubDevice.Color
    WHITE_LABEL_BLACK: HubDevice.Color
    class BatteryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BATTERY_STATE_INFO: _ClassVar[HubDevice.BatteryState]
        DISCHARGED: _ClassVar[HubDevice.BatteryState]
        CHARGED: _ClassVar[HubDevice.BatteryState]
        MALFUNCTION: _ClassVar[HubDevice.BatteryState]
        CHARGING: _ClassVar[HubDevice.BatteryState]
    NO_BATTERY_STATE_INFO: HubDevice.BatteryState
    DISCHARGED: HubDevice.BatteryState
    CHARGED: HubDevice.BatteryState
    MALFUNCTION: HubDevice.BatteryState
    CHARGING: HubDevice.BatteryState
    class ActiveChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACTIVE_CHANNEL_INFO: _ClassVar[HubDevice.ActiveChannel]
        ETHERNET: _ClassVar[HubDevice.ActiveChannel]
        WIFI: _ClassVar[HubDevice.ActiveChannel]
        GSM: _ClassVar[HubDevice.ActiveChannel]
    NO_ACTIVE_CHANNEL_INFO: HubDevice.ActiveChannel
    ETHERNET: HubDevice.ActiveChannel
    WIFI: HubDevice.ActiveChannel
    GSM: HubDevice.ActiveChannel
    class Malfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_MALFUNCTION_INFO: _ClassVar[HubDevice.Malfunction]
        CABLE_BREAK_ISSUE: _ClassVar[HubDevice.Malfunction]
        VOLTAGE_INSTABILITY: _ClassVar[HubDevice.Malfunction]
        SIREN_VOLUME_TEST_REQUIRED: _ClassVar[HubDevice.Malfunction]
        CO_SENSOR_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[HubDevice.Malfunction]
        SMOKE_DETECTOR_CAMERA_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[HubDevice.Malfunction]
        ACCELEROMETER_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        BAD_INPUT_RESISTANCE: _ClassVar[HubDevice.Malfunction]
        MODEM_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        WIFI_CONNECTION_FAIL: _ClassVar[HubDevice.Malfunction]
        BATTERY_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        BATTERY_CHARGE_ERROR: _ClassVar[HubDevice.Malfunction]
        SOFTWARE_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
        FLASH_MALFUNCTION: _ClassVar[HubDevice.Malfunction]
    NO_MALFUNCTION_INFO: HubDevice.Malfunction
    CABLE_BREAK_ISSUE: HubDevice.Malfunction
    VOLTAGE_INSTABILITY: HubDevice.Malfunction
    SIREN_VOLUME_TEST_REQUIRED: HubDevice.Malfunction
    CO_SENSOR_MALFUNCTION: HubDevice.Malfunction
    CO_SENSOR_LEVEL_EXCEEDED: HubDevice.Malfunction
    SMOKE_DETECTOR_CAMERA_MALFUNCTION: HubDevice.Malfunction
    MICROWAVE_SENSOR_CALIBRATION_ERROR: HubDevice.Malfunction
    ACCELEROMETER_MALFUNCTION: HubDevice.Malfunction
    BAD_INPUT_RESISTANCE: HubDevice.Malfunction
    MODEM_MALFUNCTION: HubDevice.Malfunction
    WIFI_CONNECTION_FAIL: HubDevice.Malfunction
    BATTERY_MALFUNCTION: HubDevice.Malfunction
    BATTERY_CHARGE_ERROR: HubDevice.Malfunction
    SOFTWARE_MALFUNCTION: HubDevice.Malfunction
    FLASH_MALFUNCTION: HubDevice.Malfunction
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE_INFO: _ClassVar[HubDevice.Subtype]
        HUB: _ClassVar[HubDevice.Subtype]
        HUB_PLUS: _ClassVar[HubDevice.Subtype]
        YAVIR: _ClassVar[HubDevice.Subtype]
        YAVIR_PLUS: _ClassVar[HubDevice.Subtype]
        HUB_2: _ClassVar[HubDevice.Subtype]
        HUB_2_PLUS: _ClassVar[HubDevice.Subtype]
        HUB_3: _ClassVar[HubDevice.Subtype]
        HUB_FIBRA: _ClassVar[HubDevice.Subtype]
        HUB_2_4G: _ClassVar[HubDevice.Subtype]
    NO_SUBTYPE_INFO: HubDevice.Subtype
    HUB: HubDevice.Subtype
    HUB_PLUS: HubDevice.Subtype
    YAVIR: HubDevice.Subtype
    YAVIR_PLUS: HubDevice.Subtype
    HUB_2: HubDevice.Subtype
    HUB_2_PLUS: HubDevice.Subtype
    HUB_3: HubDevice.Subtype
    HUB_FIBRA: HubDevice.Subtype
    HUB_2_4G: HubDevice.Subtype
    class TwoStageArmingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TWO_STORAGE_ARMING_STATUS: _ClassVar[HubDevice.TwoStageArmingStatus]
        NONE: _ClassVar[HubDevice.TwoStageArmingStatus]
        APP_EXIT_TIMER_IN_PROGRESS: _ClassVar[HubDevice.TwoStageArmingStatus]
        SECOND_STAGE_TIMER_IN_PROGRESS: _ClassVar[HubDevice.TwoStageArmingStatus]
        ARMING_INCOMPLETE: _ClassVar[HubDevice.TwoStageArmingStatus]
        FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS: _ClassVar[HubDevice.TwoStageArmingStatus]
    NO_TWO_STORAGE_ARMING_STATUS: HubDevice.TwoStageArmingStatus
    NONE: HubDevice.TwoStageArmingStatus
    APP_EXIT_TIMER_IN_PROGRESS: HubDevice.TwoStageArmingStatus
    SECOND_STAGE_TIMER_IN_PROGRESS: HubDevice.TwoStageArmingStatus
    ARMING_INCOMPLETE: HubDevice.TwoStageArmingStatus
    FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS: HubDevice.TwoStageArmingStatus
    class PostAlarmIndicationRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ALARM_INDICATION_RULE: _ClassVar[HubDevice.PostAlarmIndicationRule]
        UNCONFIRMED_ALARM: _ClassVar[HubDevice.PostAlarmIndicationRule]
        CONFIRMED_ALARM: _ClassVar[HubDevice.PostAlarmIndicationRule]
        TEMPER_ALARM: _ClassVar[HubDevice.PostAlarmIndicationRule]
    NO_ALARM_INDICATION_RULE: HubDevice.PostAlarmIndicationRule
    UNCONFIRMED_ALARM: HubDevice.PostAlarmIndicationRule
    CONFIRMED_ALARM: HubDevice.PostAlarmIndicationRule
    TEMPER_ALARM: HubDevice.PostAlarmIndicationRule
    class ReportAlarmRestore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_REPORT_ALARM_RESTORE_INFO: _ClassVar[HubDevice.ReportAlarmRestore]
        ON_RECOVERY: _ClassVar[HubDevice.ReportAlarmRestore]
        ON_DISARM: _ClassVar[HubDevice.ReportAlarmRestore]
    NO_REPORT_ALARM_RESTORE_INFO: HubDevice.ReportAlarmRestore
    ON_RECOVERY: HubDevice.ReportAlarmRestore
    ON_DISARM: HubDevice.ReportAlarmRestore
    class ReportPanicAlarmRestore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_REPORT_PANIC_ALARM_RESTORE_INFO: _ClassVar[HubDevice.ReportPanicAlarmRestore]
        OFF: _ClassVar[HubDevice.ReportPanicAlarmRestore]
        ON: _ClassVar[HubDevice.ReportPanicAlarmRestore]
    NO_REPORT_PANIC_ALARM_RESTORE_INFO: HubDevice.ReportPanicAlarmRestore
    OFF: HubDevice.ReportPanicAlarmRestore
    ON: HubDevice.ReportPanicAlarmRestore
    class AlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ALARM_TYPE_INFO: _ClassVar[HubDevice.AlarmType]
        CONFIRMED_ALARMS: _ClassVar[HubDevice.AlarmType]
        CONFIRMED_HU_ALARMS: _ClassVar[HubDevice.AlarmType]
        UNCONFIRMED_ALARMS: _ClassVar[HubDevice.AlarmType]
        UNCONFIRMED_HU_ALARMS: _ClassVar[HubDevice.AlarmType]
        TAMPER_ACTIVATION: _ClassVar[HubDevice.AlarmType]
    NO_ALARM_TYPE_INFO: HubDevice.AlarmType
    CONFIRMED_ALARMS: HubDevice.AlarmType
    CONFIRMED_HU_ALARMS: HubDevice.AlarmType
    UNCONFIRMED_ALARMS: HubDevice.AlarmType
    UNCONFIRMED_HU_ALARMS: HubDevice.AlarmType
    TAMPER_ACTIVATION: HubDevice.AlarmType
    class InterconnectState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_INTERCONNECT_STATE: _ClassVar[HubDevice.InterconnectState]
        DISABLED: _ClassVar[HubDevice.InterconnectState]
        DELAYED: _ClassVar[HubDevice.InterconnectState]
        MUTED_BY_USER: _ClassVar[HubDevice.InterconnectState]
        STARTED: _ClassVar[HubDevice.InterconnectState]
    NO_INTERCONNECT_STATE: HubDevice.InterconnectState
    DISABLED: HubDevice.InterconnectState
    DELAYED: HubDevice.InterconnectState
    MUTED_BY_USER: HubDevice.InterconnectState
    STARTED: HubDevice.InterconnectState
    class ArmPreventionCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARM_PREVENTION_CONDITION: _ClassVar[HubDevice.ArmPreventionCondition]
        LOW_BATTERY_CHARGE: _ClassVar[HubDevice.ArmPreventionCondition]
        NO_EXTERNAL_POWER: _ClassVar[HubDevice.ArmPreventionCondition]
        TAMPERED: _ClassVar[HubDevice.ArmPreventionCondition]
        HIGH_NOISE_LEVEL: _ClassVar[HubDevice.ArmPreventionCondition]
        NO_SERVER_CONNECTION: _ClassVar[HubDevice.ArmPreventionCondition]
        NO_CMS_CONNECTION: _ClassVar[HubDevice.ArmPreventionCondition]
    NO_ARM_PREVENTION_CONDITION: HubDevice.ArmPreventionCondition
    LOW_BATTERY_CHARGE: HubDevice.ArmPreventionCondition
    NO_EXTERNAL_POWER: HubDevice.ArmPreventionCondition
    TAMPERED: HubDevice.ArmPreventionCondition
    HIGH_NOISE_LEVEL: HubDevice.ArmPreventionCondition
    NO_SERVER_CONNECTION: HubDevice.ArmPreventionCondition
    NO_CMS_CONNECTION: HubDevice.ArmPreventionCondition
    class InterconnectMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_INTERCONNECT_MODE_INFO: _ClassVar[HubDevice.InterconnectMode]
        MULTI_APARTMENT: _ClassVar[HubDevice.InterconnectMode]
    NO_INTERCONNECT_MODE_INFO: HubDevice.InterconnectMode
    MULTI_APARTMENT: HubDevice.InterconnectMode
    class ChimesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIMES_STATUS_INFO: _ClassVar[HubDevice.ChimesStatus]
        CHIMES_ENABLED: _ClassVar[HubDevice.ChimesStatus]
        SIRENS_READY: _ClassVar[HubDevice.ChimesStatus]
        TRIGGERS_READY: _ClassVar[HubDevice.ChimesStatus]
    NO_CHIMES_STATUS_INFO: HubDevice.ChimesStatus
    CHIMES_ENABLED: HubDevice.ChimesStatus
    SIRENS_READY: HubDevice.ChimesStatus
    TRIGGERS_READY: HubDevice.ChimesStatus
    class DefaultCameraPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEFAULT_CAMERA_PERMISSION_INFO: _ClassVar[HubDevice.DefaultCameraPermission]
        CAMERA_PERMISSION_DISABLED: _ClassVar[HubDevice.DefaultCameraPermission]
        CAMERA_PERMISSION_ENABLED: _ClassVar[HubDevice.DefaultCameraPermission]
    NO_DEFAULT_CAMERA_PERMISSION_INFO: HubDevice.DefaultCameraPermission
    CAMERA_PERMISSION_DISABLED: HubDevice.DefaultCameraPermission
    CAMERA_PERMISSION_ENABLED: HubDevice.DefaultCameraPermission
    class DefaultPhotoOnDemandPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEFAULT_PHOTO_ON_DEMAND_PERMISSION_INFO: _ClassVar[HubDevice.DefaultPhotoOnDemandPermission]
        PHOTO_ON_DEMAND_PERMISSION_DISABLED: _ClassVar[HubDevice.DefaultPhotoOnDemandPermission]
        PHOTO_ON_DEMAND_PERMISSION_ENABLED: _ClassVar[HubDevice.DefaultPhotoOnDemandPermission]
        PHOTO_ON_DEMAND_PERMISSION_ENABLED_ON_ARM: _ClassVar[HubDevice.DefaultPhotoOnDemandPermission]
    NO_DEFAULT_PHOTO_ON_DEMAND_PERMISSION_INFO: HubDevice.DefaultPhotoOnDemandPermission
    PHOTO_ON_DEMAND_PERMISSION_DISABLED: HubDevice.DefaultPhotoOnDemandPermission
    PHOTO_ON_DEMAND_PERMISSION_ENABLED: HubDevice.DefaultPhotoOnDemandPermission
    PHOTO_ON_DEMAND_PERMISSION_ENABLED_ON_ARM: HubDevice.DefaultPhotoOnDemandPermission
    class DefaultUserCameraPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEFAULT_USER_CAMERA_PERMISSION_INFO: _ClassVar[HubDevice.DefaultUserCameraPermission]
        USER_CAMERA_PERMISSION_DISABLED: _ClassVar[HubDevice.DefaultUserCameraPermission]
        USER_CAMERA_PERMISSION_ENABLED: _ClassVar[HubDevice.DefaultUserCameraPermission]
    NO_DEFAULT_USER_CAMERA_PERMISSION_INFO: HubDevice.DefaultUserCameraPermission
    USER_CAMERA_PERMISSION_DISABLED: HubDevice.DefaultUserCameraPermission
    USER_CAMERA_PERMISSION_ENABLED: HubDevice.DefaultUserCameraPermission
    class DefaultUserPhotoOnDemandPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEFAULT_USER_PHOTO_ON_DEMAND_PERMISSION_INFO: _ClassVar[HubDevice.DefaultUserPhotoOnDemandPermission]
        USER_PHOTO_ON_DEMAND_PERMISSION_DISABLED: _ClassVar[HubDevice.DefaultUserPhotoOnDemandPermission]
        USER_PHOTO_ON_DEMAND_PERMISSION_ENABLED: _ClassVar[HubDevice.DefaultUserPhotoOnDemandPermission]
        USER_PHOTO_ON_DEMAND_PERMISSION_ENABLED_ON_ARM: _ClassVar[HubDevice.DefaultUserPhotoOnDemandPermission]
    NO_DEFAULT_USER_PHOTO_ON_DEMAND_PERMISSION_INFO: HubDevice.DefaultUserPhotoOnDemandPermission
    USER_PHOTO_ON_DEMAND_PERMISSION_DISABLED: HubDevice.DefaultUserPhotoOnDemandPermission
    USER_PHOTO_ON_DEMAND_PERMISSION_ENABLED: HubDevice.DefaultUserPhotoOnDemandPermission
    USER_PHOTO_ON_DEMAND_PERMISSION_ENABLED_ON_ARM: HubDevice.DefaultUserPhotoOnDemandPermission
    class PhotoOnDemandMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_PHOTO_ON_DEMAND_MODE_INFO: _ClassVar[HubDevice.PhotoOnDemandMode]
        PHOTO_ON_DEMAND_USER: _ClassVar[HubDevice.PhotoOnDemandMode]
        PHOTO_ON_DEMAND_SCENARIO: _ClassVar[HubDevice.PhotoOnDemandMode]
    NO_PHOTO_ON_DEMAND_MODE_INFO: HubDevice.PhotoOnDemandMode
    PHOTO_ON_DEMAND_USER: HubDevice.PhotoOnDemandMode
    PHOTO_ON_DEMAND_SCENARIO: HubDevice.PhotoOnDemandMode
    class PrivacyOfficerOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_PRIVACY_OFFICER_OPTION_INFO: _ClassVar[HubDevice.PrivacyOfficerOption]
        ACCESS_TO_SLOW_POD_ALLOWED: _ClassVar[HubDevice.PrivacyOfficerOption]
        ACCESS_TO_CAMERA_PRIVACY_SETTINGS_ALLOWED: _ClassVar[HubDevice.PrivacyOfficerOption]
    NO_PRIVACY_OFFICER_OPTION_INFO: HubDevice.PrivacyOfficerOption
    ACCESS_TO_SLOW_POD_ALLOWED: HubDevice.PrivacyOfficerOption
    ACCESS_TO_CAMERA_PRIVACY_SETTINGS_ALLOWED: HubDevice.PrivacyOfficerOption
    class MaxPowerTestState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_MAX_POWER_TEST_STATE_INFO: _ClassVar[HubDevice.MaxPowerTestState]
        TEST_NOT_STARTED: _ClassVar[HubDevice.MaxPowerTestState]
        TEST_IN_PROGRESS: _ClassVar[HubDevice.MaxPowerTestState]
        TEST_FINISHED_SUCCESSFULLY: _ClassVar[HubDevice.MaxPowerTestState]
        TEST_FINISHED_WITH_SC: _ClassVar[HubDevice.MaxPowerTestState]
    NO_MAX_POWER_TEST_STATE_INFO: HubDevice.MaxPowerTestState
    TEST_NOT_STARTED: HubDevice.MaxPowerTestState
    TEST_IN_PROGRESS: HubDevice.MaxPowerTestState
    TEST_FINISHED_SUCCESSFULLY: HubDevice.MaxPowerTestState
    TEST_FINISHED_WITH_SC: HubDevice.MaxPowerTestState
    class BusState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BUS_STATE: _ClassVar[HubDevice.BusState]
        POWERED_ON: _ClassVar[HubDevice.BusState]
        SHORT_CIRCUIT_PRESENT: _ClassVar[HubDevice.BusState]
    NO_BUS_STATE: HubDevice.BusState
    POWERED_ON: HubDevice.BusState
    SHORT_CIRCUIT_PRESENT: HubDevice.BusState
    class ScanStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SCAN_STATUS_INFO: _ClassVar[HubDevice.ScanStatus]
        SCAN_NOT_STARTED: _ClassVar[HubDevice.ScanStatus]
        SCAN_STARTED: _ClassVar[HubDevice.ScanStatus]
        DEVICES_FOUND: _ClassVar[HubDevice.ScanStatus]
    NO_SCAN_STATUS_INFO: HubDevice.ScanStatus
    SCAN_NOT_STARTED: HubDevice.ScanStatus
    SCAN_STARTED: HubDevice.ScanStatus
    DEVICES_FOUND: HubDevice.ScanStatus
    class NoiseLevel(_message.Message):
        __slots__ = ("high", "avg_value_channel1", "avg_value_channel2", "avg_value_data_channel")
        HIGH_FIELD_NUMBER: _ClassVar[int]
        AVG_VALUE_CHANNEL1_FIELD_NUMBER: _ClassVar[int]
        AVG_VALUE_CHANNEL2_FIELD_NUMBER: _ClassVar[int]
        AVG_VALUE_DATA_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        high: _wrappers_pb2.BoolValue
        avg_value_channel1: _wrappers_pb2.Int32Value
        avg_value_channel2: _wrappers_pb2.Int32Value
        avg_value_data_channel: _wrappers_pb2.Int32Value
        def __init__(self, high: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., avg_value_channel1: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., avg_value_channel2: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., avg_value_data_channel: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    class Limits(_message.Message):
        __slots__ = ("users", "sensors", "rooms", "cameras", "groups")
        USERS_FIELD_NUMBER: _ClassVar[int]
        SENSORS_FIELD_NUMBER: _ClassVar[int]
        ROOMS_FIELD_NUMBER: _ClassVar[int]
        CAMERAS_FIELD_NUMBER: _ClassVar[int]
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        users: _wrappers_pb2.Int32Value
        sensors: _wrappers_pb2.Int32Value
        rooms: _wrappers_pb2.Int32Value
        cameras: _wrappers_pb2.Int32Value
        groups: _wrappers_pb2.Int32Value
        def __init__(self, users: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., sensors: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., rooms: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., cameras: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., groups: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    class Firmware(_message.Message):
        __slots__ = ("version", "new_version_available", "auto_update_enabled", "latest_available_version", "rr")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NEW_VERSION_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        AUTO_UPDATE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LATEST_AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
        RR_FIELD_NUMBER: _ClassVar[int]
        version: str
        new_version_available: _wrappers_pb2.BoolValue
        auto_update_enabled: bool
        latest_available_version: str
        rr: str
        def __init__(self, version: _Optional[str] = ..., new_version_available: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., auto_update_enabled: bool = ..., latest_available_version: _Optional[str] = ..., rr: _Optional[str] = ...) -> None: ...
    class Ethernet(_message.Message):
        __slots__ = ("dhcp", "ip", "mask", "gate", "dns", "enabled")
        DHCP_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        dhcp: bool
        ip: str
        mask: str
        gate: str
        dns: str
        enabled: bool
        def __init__(self, dhcp: bool = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ..., enabled: bool = ...) -> None: ...
    class Battery(_message.Message):
        __slots__ = ("charge_level_percentage", "state")
        CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        charge_level_percentage: _wrappers_pb2.Int32Value
        state: HubDevice.BatteryState
        def __init__(self, charge_level_percentage: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., state: _Optional[_Union[HubDevice.BatteryState, str]] = ...) -> None: ...
    class HardwareVersions(_message.Message):
        __slots__ = ("modem", "wifi", "ethernet", "flash", "cpu", "pcb", "rfm", "zwave")
        MODEM_FIELD_NUMBER: _ClassVar[int]
        WIFI_FIELD_NUMBER: _ClassVar[int]
        ETHERNET_FIELD_NUMBER: _ClassVar[int]
        FLASH_FIELD_NUMBER: _ClassVar[int]
        CPU_FIELD_NUMBER: _ClassVar[int]
        PCB_FIELD_NUMBER: _ClassVar[int]
        RFM_FIELD_NUMBER: _ClassVar[int]
        ZWAVE_FIELD_NUMBER: _ClassVar[int]
        modem: int
        wifi: int
        ethernet: int
        flash: int
        cpu: int
        pcb: int
        rfm: int
        zwave: int
        def __init__(self, modem: _Optional[int] = ..., wifi: _Optional[int] = ..., ethernet: _Optional[int] = ..., flash: _Optional[int] = ..., cpu: _Optional[int] = ..., pcb: _Optional[int] = ..., rfm: _Optional[int] = ..., zwave: _Optional[int] = ...) -> None: ...
    class Warnings(_message.Message):
        __slots__ = ("hub", "all_devices")
        HUB_FIELD_NUMBER: _ClassVar[int]
        ALL_DEVICES_FIELD_NUMBER: _ClassVar[int]
        hub: _wrappers_pb2.Int32Value
        all_devices: _wrappers_pb2.Int32Value
        def __init__(self, hub: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., all_devices: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    class FireAlarm(_message.Message):
        __slots__ = ("trigger_on_all_sensors", "double_impulses")
        TRIGGER_ON_ALL_SENSORS_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_IMPULSES_FIELD_NUMBER: _ClassVar[int]
        trigger_on_all_sensors: bool
        double_impulses: bool
        def __init__(self, trigger_on_all_sensors: bool = ..., double_impulses: bool = ...) -> None: ...
    class Wifi(_message.Message):
        __slots__ = ("security_protocol", "signal_level", "ssid", "password", "channel", "ip", "mask", "gate", "dns", "dhcp", "enabled")
        class SecurityProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SECURITY_PROTOCOL_INFO: _ClassVar[HubDevice.Wifi.SecurityProtocol]
            NONE: _ClassVar[HubDevice.Wifi.SecurityProtocol]
            WEP: _ClassVar[HubDevice.Wifi.SecurityProtocol]
            WPA: _ClassVar[HubDevice.Wifi.SecurityProtocol]
            WPA2: _ClassVar[HubDevice.Wifi.SecurityProtocol]
            WPA_WPA2: _ClassVar[HubDevice.Wifi.SecurityProtocol]
        NO_SECURITY_PROTOCOL_INFO: HubDevice.Wifi.SecurityProtocol
        NONE: HubDevice.Wifi.SecurityProtocol
        WEP: HubDevice.Wifi.SecurityProtocol
        WPA: HubDevice.Wifi.SecurityProtocol
        WPA2: HubDevice.Wifi.SecurityProtocol
        WPA_WPA2: HubDevice.Wifi.SecurityProtocol
        class SignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SIGNAL_LEVEL_INFO: _ClassVar[HubDevice.Wifi.SignalLevel]
            NO_SIGNAL: _ClassVar[HubDevice.Wifi.SignalLevel]
            WEAK: _ClassVar[HubDevice.Wifi.SignalLevel]
            NORMAL: _ClassVar[HubDevice.Wifi.SignalLevel]
            STRONG: _ClassVar[HubDevice.Wifi.SignalLevel]
        NO_SIGNAL_LEVEL_INFO: HubDevice.Wifi.SignalLevel
        NO_SIGNAL: HubDevice.Wifi.SignalLevel
        WEAK: HubDevice.Wifi.SignalLevel
        NORMAL: HubDevice.Wifi.SignalLevel
        STRONG: HubDevice.Wifi.SignalLevel
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        SSID_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        DHCP_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        security_protocol: HubDevice.Wifi.SecurityProtocol
        signal_level: HubDevice.Wifi.SignalLevel
        ssid: str
        password: str
        channel: int
        ip: str
        mask: str
        gate: str
        dns: str
        dhcp: bool
        enabled: bool
        def __init__(self, security_protocol: _Optional[_Union[HubDevice.Wifi.SecurityProtocol, str]] = ..., signal_level: _Optional[_Union[HubDevice.Wifi.SignalLevel, str]] = ..., ssid: _Optional[str] = ..., password: _Optional[str] = ..., channel: _Optional[int] = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ..., dhcp: bool = ..., enabled: bool = ...) -> None: ...
    class Gsm(_message.Message):
        __slots__ = ("disable_icmp_before_connecting", "gprs_enabled", "virtual_operator_allowed", "roaming_enabled", "sim_card_state", "network_status", "signal_level", "active_sim_card", "sim_card1", "sim_card2")
        class SimCardState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SIM_CARD_STATE_INFO: _ClassVar[HubDevice.Gsm.SimCardState]
            OK: _ClassVar[HubDevice.Gsm.SimCardState]
            MISSING: _ClassVar[HubDevice.Gsm.SimCardState]
            MALFUNCTION: _ClassVar[HubDevice.Gsm.SimCardState]
            LOCKED: _ClassVar[HubDevice.Gsm.SimCardState]
            UNKNOWN: _ClassVar[HubDevice.Gsm.SimCardState]
        NO_SIM_CARD_STATE_INFO: HubDevice.Gsm.SimCardState
        OK: HubDevice.Gsm.SimCardState
        MISSING: HubDevice.Gsm.SimCardState
        MALFUNCTION: HubDevice.Gsm.SimCardState
        LOCKED: HubDevice.Gsm.SimCardState
        UNKNOWN: HubDevice.Gsm.SimCardState
        class SignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SIGNAL_LEVEL_INFO: _ClassVar[HubDevice.Gsm.SignalLevel]
            NO_SIGNAL: _ClassVar[HubDevice.Gsm.SignalLevel]
            WEAK: _ClassVar[HubDevice.Gsm.SignalLevel]
            NORMAL: _ClassVar[HubDevice.Gsm.SignalLevel]
            STRONG: _ClassVar[HubDevice.Gsm.SignalLevel]
        NO_SIGNAL_LEVEL_INFO: HubDevice.Gsm.SignalLevel
        NO_SIGNAL: HubDevice.Gsm.SignalLevel
        WEAK: HubDevice.Gsm.SignalLevel
        NORMAL: HubDevice.Gsm.SignalLevel
        STRONG: HubDevice.Gsm.SignalLevel
        class NetworkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_NETWORK_STATUS_INFO: _ClassVar[HubDevice.Gsm.NetworkStatus]
            GSM: _ClassVar[HubDevice.Gsm.NetworkStatus]
            _2G: _ClassVar[HubDevice.Gsm.NetworkStatus]
            _3G: _ClassVar[HubDevice.Gsm.NetworkStatus]
            _4G: _ClassVar[HubDevice.Gsm.NetworkStatus]
        NO_NETWORK_STATUS_INFO: HubDevice.Gsm.NetworkStatus
        GSM: HubDevice.Gsm.NetworkStatus
        _2G: HubDevice.Gsm.NetworkStatus
        _3G: HubDevice.Gsm.NetworkStatus
        _4G: HubDevice.Gsm.NetworkStatus
        class SimCard1(_message.Message):
            __slots__ = ("number", "apn", "username", "password", "balance_number", "traffic_tx_kb", "traffic_rx_kb", "last_traffic_reset_timestamp")
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            APN_FIELD_NUMBER: _ClassVar[int]
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            TRAFFIC_TX_KB_FIELD_NUMBER: _ClassVar[int]
            TRAFFIC_RX_KB_FIELD_NUMBER: _ClassVar[int]
            LAST_TRAFFIC_RESET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            number: str
            apn: str
            username: str
            password: str
            balance_number: str
            traffic_tx_kb: _wrappers_pb2.Int32Value
            traffic_rx_kb: _wrappers_pb2.Int32Value
            last_traffic_reset_timestamp: _wrappers_pb2.Int32Value
            def __init__(self, number: _Optional[str] = ..., apn: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., balance_number: _Optional[str] = ..., traffic_tx_kb: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., traffic_rx_kb: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., last_traffic_reset_timestamp: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        class SimCard2(_message.Message):
            __slots__ = ("number", "apn", "username", "password", "balance_number", "traffic_tx_kb", "traffic_rx_kb", "last_traffic_reset_timestamp")
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            APN_FIELD_NUMBER: _ClassVar[int]
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            TRAFFIC_TX_KB_FIELD_NUMBER: _ClassVar[int]
            TRAFFIC_RX_KB_FIELD_NUMBER: _ClassVar[int]
            LAST_TRAFFIC_RESET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            number: str
            apn: str
            username: str
            password: str
            balance_number: str
            traffic_tx_kb: _wrappers_pb2.Int32Value
            traffic_rx_kb: _wrappers_pb2.Int32Value
            last_traffic_reset_timestamp: _wrappers_pb2.Int32Value
            def __init__(self, number: _Optional[str] = ..., apn: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., balance_number: _Optional[str] = ..., traffic_tx_kb: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., traffic_rx_kb: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., last_traffic_reset_timestamp: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        DISABLE_ICMP_BEFORE_CONNECTING_FIELD_NUMBER: _ClassVar[int]
        GPRS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_OPERATOR_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        ROAMING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_STATE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_STATUS_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_SIM_CARD_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD1_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD2_FIELD_NUMBER: _ClassVar[int]
        disable_icmp_before_connecting: bool
        gprs_enabled: bool
        virtual_operator_allowed: bool
        roaming_enabled: bool
        sim_card_state: HubDevice.Gsm.SimCardState
        network_status: HubDevice.Gsm.NetworkStatus
        signal_level: HubDevice.Gsm.SignalLevel
        active_sim_card: int
        sim_card1: HubDevice.Gsm.SimCard1
        sim_card2: HubDevice.Gsm.SimCard2
        def __init__(self, disable_icmp_before_connecting: bool = ..., gprs_enabled: bool = ..., virtual_operator_allowed: bool = ..., roaming_enabled: bool = ..., sim_card_state: _Optional[_Union[HubDevice.Gsm.SimCardState, str]] = ..., network_status: _Optional[_Union[HubDevice.Gsm.NetworkStatus, str]] = ..., signal_level: _Optional[_Union[HubDevice.Gsm.SignalLevel, str]] = ..., active_sim_card: _Optional[int] = ..., sim_card1: _Optional[_Union[HubDevice.Gsm.SimCard1, _Mapping]] = ..., sim_card2: _Optional[_Union[HubDevice.Gsm.SimCard2, _Mapping]] = ...) -> None: ...
    class Cms(_message.Message):
        __slots__ = ("address", "port", "address_reserve", "port_reserve", "active_channels", "ping_period_seconds", "gprs_enabled", "ethernet_enabled", "wifi_enabled", "protocol", "connection_mode", "sia_account_number", "sia_encryption_key", "sia_encryption_type", "send_panic_button_location")
        class ActiveChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ACTIVE_CHANNEL_INFO: _ClassVar[HubDevice.Cms.ActiveChannel]
            ETHERNET: _ClassVar[HubDevice.Cms.ActiveChannel]
            WIFI: _ClassVar[HubDevice.Cms.ActiveChannel]
            GSM: _ClassVar[HubDevice.Cms.ActiveChannel]
        NO_ACTIVE_CHANNEL_INFO: HubDevice.Cms.ActiveChannel
        ETHERNET: HubDevice.Cms.ActiveChannel
        WIFI: HubDevice.Cms.ActiveChannel
        GSM: HubDevice.Cms.ActiveChannel
        class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_CMS_PROTOCOL_INFO: _ClassVar[HubDevice.Cms.Protocol]
            CID: _ClassVar[HubDevice.Cms.Protocol]
            SIA: _ClassVar[HubDevice.Cms.Protocol]
        NO_CMS_PROTOCOL_INFO: HubDevice.Cms.Protocol
        CID: HubDevice.Cms.Protocol
        SIA: HubDevice.Cms.Protocol
        class ConnectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_CMS_CONNECTION_MODE_INFO: _ClassVar[HubDevice.Cms.ConnectionMode]
            ALWAYS_UP: _ClassVar[HubDevice.Cms.ConnectionMode]
            ON_DEMAND: _ClassVar[HubDevice.Cms.ConnectionMode]
        NO_CMS_CONNECTION_MODE_INFO: HubDevice.Cms.ConnectionMode
        ALWAYS_UP: HubDevice.Cms.ConnectionMode
        ON_DEMAND: HubDevice.Cms.ConnectionMode
        class SiaEncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SIA_ENCRYPTION_TYPE_INFO: _ClassVar[HubDevice.Cms.SiaEncryptionType]
            OFF: _ClassVar[HubDevice.Cms.SiaEncryptionType]
            AES128: _ClassVar[HubDevice.Cms.SiaEncryptionType]
            AES256: _ClassVar[HubDevice.Cms.SiaEncryptionType]
        NO_SIA_ENCRYPTION_TYPE_INFO: HubDevice.Cms.SiaEncryptionType
        OFF: HubDevice.Cms.SiaEncryptionType
        AES128: HubDevice.Cms.SiaEncryptionType
        AES256: HubDevice.Cms.SiaEncryptionType
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_RESERVE_FIELD_NUMBER: _ClassVar[int]
        PORT_RESERVE_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        PING_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
        GPRS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ETHERNET_ENABLED_FIELD_NUMBER: _ClassVar[int]
        WIFI_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_MODE_FIELD_NUMBER: _ClassVar[int]
        SIA_ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SIA_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        SIA_ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        SEND_PANIC_BUTTON_LOCATION_FIELD_NUMBER: _ClassVar[int]
        address: str
        port: int
        address_reserve: str
        port_reserve: int
        active_channels: _containers.RepeatedScalarFieldContainer[HubDevice.Cms.ActiveChannel]
        ping_period_seconds: int
        gprs_enabled: bool
        ethernet_enabled: bool
        wifi_enabled: bool
        protocol: HubDevice.Cms.Protocol
        connection_mode: HubDevice.Cms.ConnectionMode
        sia_account_number: str
        sia_encryption_key: str
        sia_encryption_type: HubDevice.Cms.SiaEncryptionType
        send_panic_button_location: bool
        def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., address_reserve: _Optional[str] = ..., port_reserve: _Optional[int] = ..., active_channels: _Optional[_Iterable[_Union[HubDevice.Cms.ActiveChannel, str]]] = ..., ping_period_seconds: _Optional[int] = ..., gprs_enabled: bool = ..., ethernet_enabled: bool = ..., wifi_enabled: bool = ..., protocol: _Optional[_Union[HubDevice.Cms.Protocol, str]] = ..., connection_mode: _Optional[_Union[HubDevice.Cms.ConnectionMode, str]] = ..., sia_account_number: _Optional[str] = ..., sia_encryption_key: _Optional[str] = ..., sia_encryption_type: _Optional[_Union[HubDevice.Cms.SiaEncryptionType, str]] = ..., send_panic_button_location: bool = ...) -> None: ...
    class Jeweller(_message.Message):
        __slots__ = ("lost_heartbeats_threshold", "detector_ping_interval_seconds")
        LOST_HEARTBEATS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        DETECTOR_PING_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
        lost_heartbeats_threshold: int
        detector_ping_interval_seconds: int
        def __init__(self, lost_heartbeats_threshold: _Optional[int] = ..., detector_ping_interval_seconds: _Optional[int] = ...) -> None: ...
    class Address(_message.Message):
        __slots__ = ("country_code", "loc_state", "locality", "address", "comment", "latitude", "longitude")
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        LOC_STATE_FIELD_NUMBER: _ClassVar[int]
        LOCALITY_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        country_code: str
        loc_state: str
        locality: str
        address: str
        comment: str
        latitude: _decimal_pb2.Decimal
        longitude: _decimal_pb2.Decimal
        def __init__(self, country_code: _Optional[str] = ..., loc_state: _Optional[str] = ..., locality: _Optional[str] = ..., address: _Optional[str] = ..., comment: _Optional[str] = ..., latitude: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., longitude: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...
    class AlarmVerification(_message.Message):
        __slots__ = ("verification_enabled", "verification_timeout")
        VERIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        VERIFICATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        verification_enabled: bool
        verification_timeout: int
        def __init__(self, verification_enabled: bool = ..., verification_timeout: _Optional[int] = ...) -> None: ...
    class Interconnection(_message.Message):
        __slots__ = ("interconnect_delay_timeout", "interconnect_delay_expiration_unix_time", "interconnect_state", "interconnect_modes")
        INTERCONNECT_DELAY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        INTERCONNECT_DELAY_EXPIRATION_UNIX_TIME_FIELD_NUMBER: _ClassVar[int]
        INTERCONNECT_STATE_FIELD_NUMBER: _ClassVar[int]
        INTERCONNECT_MODES_FIELD_NUMBER: _ClassVar[int]
        interconnect_delay_timeout: int
        interconnect_delay_expiration_unix_time: int
        interconnect_state: HubDevice.InterconnectState
        interconnect_modes: _containers.RepeatedScalarFieldContainer[HubDevice.InterconnectMode]
        def __init__(self, interconnect_delay_timeout: _Optional[int] = ..., interconnect_delay_expiration_unix_time: _Optional[int] = ..., interconnect_state: _Optional[_Union[HubDevice.InterconnectState, str]] = ..., interconnect_modes: _Optional[_Iterable[_Union[HubDevice.InterconnectMode, str]]] = ...) -> None: ...
    class GeoFence(_message.Message):
        __slots__ = ("radius_meters", "coordinates")
        class GeoFenceCoordinates(_message.Message):
            __slots__ = ("latitude", "longitude")
            LATITUDE_FIELD_NUMBER: _ClassVar[int]
            LONGITUDE_FIELD_NUMBER: _ClassVar[int]
            latitude: _decimal_pb2.Decimal
            longitude: _decimal_pb2.Decimal
            def __init__(self, latitude: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., longitude: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...
        RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
        COORDINATES_FIELD_NUMBER: _ClassVar[int]
        radius_meters: int
        coordinates: HubDevice.GeoFence.GeoFenceCoordinates
        def __init__(self, radius_meters: _Optional[int] = ..., coordinates: _Optional[_Union[HubDevice.GeoFence.GeoFenceCoordinates, _Mapping]] = ...) -> None: ...
    class TwoStageArming(_message.Message):
        __slots__ = ("two_stage_arming_state", "application_triggered_arming", "device_triggered_arming", "exit_timer_expiration_unix_time", "remote_notification_delay", "disarming_by_keypad")
        TWO_STAGE_ARMING_STATE_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_TRIGGERED_ARMING_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TRIGGERED_ARMING_FIELD_NUMBER: _ClassVar[int]
        EXIT_TIMER_EXPIRATION_UNIX_TIME_FIELD_NUMBER: _ClassVar[int]
        REMOTE_NOTIFICATION_DELAY_FIELD_NUMBER: _ClassVar[int]
        DISARMING_BY_KEYPAD_FIELD_NUMBER: _ClassVar[int]
        two_stage_arming_state: bool
        application_triggered_arming: HubDevice.ApplicationTriggeredArming
        device_triggered_arming: HubDevice.DeviceTriggeredArming
        exit_timer_expiration_unix_time: int
        remote_notification_delay: int
        disarming_by_keypad: bool
        def __init__(self, two_stage_arming_state: bool = ..., application_triggered_arming: _Optional[_Union[HubDevice.ApplicationTriggeredArming, _Mapping]] = ..., device_triggered_arming: _Optional[_Union[HubDevice.DeviceTriggeredArming, _Mapping]] = ..., exit_timer_expiration_unix_time: _Optional[int] = ..., remote_notification_delay: _Optional[int] = ..., disarming_by_keypad: bool = ...) -> None: ...
    class ApplicationTriggeredArming(_message.Message):
        __slots__ = ("app_exit_timer",)
        APP_EXIT_TIMER_FIELD_NUMBER: _ClassVar[int]
        app_exit_timer: int
        def __init__(self, app_exit_timer: _Optional[int] = ...) -> None: ...
    class DeviceTriggeredArming(_message.Message):
        __slots__ = ("second_stage_exit_timer", "final_door_bounce_timer")
        SECOND_STAGE_EXIT_TIMER_FIELD_NUMBER: _ClassVar[int]
        FINAL_DOOR_BOUNCE_TIMER_FIELD_NUMBER: _ClassVar[int]
        second_stage_exit_timer: int
        final_door_bounce_timer: int
        def __init__(self, second_stage_exit_timer: _Optional[int] = ..., final_door_bounce_timer: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOISE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_WITH_GROUPS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_LOG_STATE_FIELD_NUMBER: _ClassVar[int]
    PANIC_SIREN_ON_PANIC_BUTTON_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    ARM_PREVENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    TAMPERED_FIELD_NUMBER: _ClassVar[int]
    PANIC_SIREN_ON_ANY_TAMPER_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    GSM_FIELD_NUMBER: _ClassVar[int]
    CMS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_NUM_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    PING_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_ALARM_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    JEWELLER_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TEST_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_BY_SERVICE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_LOST_AS_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    ALARM_AS_MALFUNCTION_WHEN_ARMING_FIELD_NUMBER: _ClassVar[int]
    AUTO_BYPASS_TIMER_MINUTES_FIELD_NUMBER: _ClassVar[int]
    AUTO_BYPASS_COUNTER_FIELD_NUMBER: _ClassVar[int]
    HUB_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    RESTORE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ALARM_HAPPENED_FIELD_NUMBER: _ClassVar[int]
    ARM_PREVENTIONS_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    REPORT_ALARM_RESTORE_FIELD_NUMBER: _ClassVar[int]
    REPORT_PANIC_ALARM_RESTORE_FIELD_NUMBER: _ClassVar[int]
    TAMPER_ALARM_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_ALARM_ON_DELAYED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    ALARM_CONFIRMATION_HU_DEVICES_PD6662_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TIMEOUT_HU_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECTION_FIELD_NUMBER: _ClassVar[int]
    POSTALARMINDICATIONRULE_FIELD_NUMBER: _ClassVar[int]
    LOST_FIBRA_COUNTER_FIELD_NUMBER: _ClassVar[int]
    CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_CONNECTIVITY_NOTIFICATION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OFFLINE_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CAMERA_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PHOTO_ON_DEMAND_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USER_CAMERA_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USER_PHOTO_ON_DEMAND_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    MAX_POWER_TEST_STATE_FIELD_NUMBER: _ClassVar[int]
    BUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    SCAN_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OFFICER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GEOFENCE_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_PROGRESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    noise_level: HubDevice.NoiseLevel
    connection_status: _wrappers_pb2.BoolValue
    state: HubDevice.State
    state_with_groups: HubDevice.StateWithGroups
    debug_log_state: HubDevice.DebugLogState
    panic_siren_on_panic_button: bool
    limits: HubDevice.Limits
    groups_enabled: bool
    firmware: HubDevice.Firmware
    ethernet: HubDevice.Ethernet
    arm_prevention_mode: HubDevice.ArmPreventionMode
    tampered: _wrappers_pb2.BoolValue
    panic_siren_on_any_tamper: bool
    battery: HubDevice.Battery
    hardware_versions: HubDevice.HardwareVersions
    warnings: HubDevice.Warnings
    fire_alarm: HubDevice.FireAlarm
    wifi: HubDevice.Wifi
    gsm: HubDevice.Gsm
    cms: HubDevice.Cms
    color: HubDevice.Color
    image_id: str
    image_num: int
    image_urls: _image_urls_pb2.ImageUrls
    active_channels: _containers.RepeatedScalarFieldContainer[HubDevice.ActiveChannel]
    ping_period_seconds: int
    offline_alarm_seconds: int
    led_brightness_level: int
    subtype: HubDevice.Subtype
    jeweller: HubDevice.Jeweller
    externally_powered: _wrappers_pb2.BoolValue
    connection_test_in_progress: _wrappers_pb2.BoolValue
    malfunctions: _containers.RepeatedScalarFieldContainer[HubDevice.Malfunction]
    blocked_by_service_provider: _wrappers_pb2.BoolValue
    connection_lost_as_malfunction: bool
    alarm_as_malfunction_when_arming: bool
    auto_bypass_timer_minutes: int
    auto_bypass_counter: int
    hub_address: HubDevice.Address
    time_zone: str
    alarm_verification: HubDevice.AlarmVerification
    restore_required: _containers.RepeatedScalarFieldContainer[HubDevice.AlarmType]
    alarm_happened: _containers.RepeatedScalarFieldContainer[HubDevice.AlarmType]
    arm_preventions_to_check: _containers.RepeatedScalarFieldContainer[HubDevice.ArmPreventionCondition]
    report_alarm_restore: HubDevice.ReportAlarmRestore
    report_panic_alarm_restore: HubDevice.ReportPanicAlarmRestore
    tamper_alarm_confirmation: int
    confirmed_alarm_on_delayed_devices: int
    alarm_confirmation_hu_devices_pd6662: int
    verification_timeout_hu: int
    interconnection: HubDevice.Interconnection
    postAlarmIndicationRule: _containers.RepeatedScalarFieldContainer[HubDevice.PostAlarmIndicationRule]
    lost_fibra_counter: int
    chimes_status: _containers.RepeatedScalarFieldContainer[HubDevice.ChimesStatus]
    channel_connectivity_notification_active: _containers.RepeatedScalarFieldContainer[HubDevice.ActiveChannel]
    channel_offline_alarm_delay_seconds: int
    photo_on_demand_mode: _containers.RepeatedScalarFieldContainer[HubDevice.PhotoOnDemandMode]
    default_camera_permission: HubDevice.DefaultCameraPermission
    default_photo_on_demand_permission: HubDevice.DefaultPhotoOnDemandPermission
    default_user_camera_permission: HubDevice.DefaultUserCameraPermission
    default_user_photo_on_demand_permission: HubDevice.DefaultUserPhotoOnDemandPermission
    max_power_test_state: HubDevice.MaxPowerTestState
    bus_status: _containers.RepeatedScalarFieldContainer[HubDevice.BusState]
    scan_status: HubDevice.ScanStatus
    privacy_officer_options: _containers.RepeatedScalarFieldContainer[HubDevice.PrivacyOfficerOption]
    geofence: HubDevice.GeoFence
    two_stage_arming_progress_status: HubDevice.TwoStageArmingStatus
    two_stage_arming: HubDevice.TwoStageArming
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., noise_level: _Optional[_Union[HubDevice.NoiseLevel, _Mapping]] = ..., connection_status: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., state: _Optional[_Union[HubDevice.State, str]] = ..., state_with_groups: _Optional[_Union[HubDevice.StateWithGroups, str]] = ..., debug_log_state: _Optional[_Union[HubDevice.DebugLogState, str]] = ..., panic_siren_on_panic_button: bool = ..., limits: _Optional[_Union[HubDevice.Limits, _Mapping]] = ..., groups_enabled: bool = ..., firmware: _Optional[_Union[HubDevice.Firmware, _Mapping]] = ..., ethernet: _Optional[_Union[HubDevice.Ethernet, _Mapping]] = ..., arm_prevention_mode: _Optional[_Union[HubDevice.ArmPreventionMode, str]] = ..., tampered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., panic_siren_on_any_tamper: bool = ..., battery: _Optional[_Union[HubDevice.Battery, _Mapping]] = ..., hardware_versions: _Optional[_Union[HubDevice.HardwareVersions, _Mapping]] = ..., warnings: _Optional[_Union[HubDevice.Warnings, _Mapping]] = ..., fire_alarm: _Optional[_Union[HubDevice.FireAlarm, _Mapping]] = ..., wifi: _Optional[_Union[HubDevice.Wifi, _Mapping]] = ..., gsm: _Optional[_Union[HubDevice.Gsm, _Mapping]] = ..., cms: _Optional[_Union[HubDevice.Cms, _Mapping]] = ..., color: _Optional[_Union[HubDevice.Color, str]] = ..., image_id: _Optional[str] = ..., image_num: _Optional[int] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., active_channels: _Optional[_Iterable[_Union[HubDevice.ActiveChannel, str]]] = ..., ping_period_seconds: _Optional[int] = ..., offline_alarm_seconds: _Optional[int] = ..., led_brightness_level: _Optional[int] = ..., subtype: _Optional[_Union[HubDevice.Subtype, str]] = ..., jeweller: _Optional[_Union[HubDevice.Jeweller, _Mapping]] = ..., externally_powered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., connection_test_in_progress: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., malfunctions: _Optional[_Iterable[_Union[HubDevice.Malfunction, str]]] = ..., blocked_by_service_provider: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., connection_lost_as_malfunction: bool = ..., alarm_as_malfunction_when_arming: bool = ..., auto_bypass_timer_minutes: _Optional[int] = ..., auto_bypass_counter: _Optional[int] = ..., hub_address: _Optional[_Union[HubDevice.Address, _Mapping]] = ..., time_zone: _Optional[str] = ..., alarm_verification: _Optional[_Union[HubDevice.AlarmVerification, _Mapping]] = ..., restore_required: _Optional[_Iterable[_Union[HubDevice.AlarmType, str]]] = ..., alarm_happened: _Optional[_Iterable[_Union[HubDevice.AlarmType, str]]] = ..., arm_preventions_to_check: _Optional[_Iterable[_Union[HubDevice.ArmPreventionCondition, str]]] = ..., report_alarm_restore: _Optional[_Union[HubDevice.ReportAlarmRestore, str]] = ..., report_panic_alarm_restore: _Optional[_Union[HubDevice.ReportPanicAlarmRestore, str]] = ..., tamper_alarm_confirmation: _Optional[int] = ..., confirmed_alarm_on_delayed_devices: _Optional[int] = ..., alarm_confirmation_hu_devices_pd6662: _Optional[int] = ..., verification_timeout_hu: _Optional[int] = ..., interconnection: _Optional[_Union[HubDevice.Interconnection, _Mapping]] = ..., postAlarmIndicationRule: _Optional[_Iterable[_Union[HubDevice.PostAlarmIndicationRule, str]]] = ..., lost_fibra_counter: _Optional[int] = ..., chimes_status: _Optional[_Iterable[_Union[HubDevice.ChimesStatus, str]]] = ..., channel_connectivity_notification_active: _Optional[_Iterable[_Union[HubDevice.ActiveChannel, str]]] = ..., channel_offline_alarm_delay_seconds: _Optional[int] = ..., photo_on_demand_mode: _Optional[_Iterable[_Union[HubDevice.PhotoOnDemandMode, str]]] = ..., default_camera_permission: _Optional[_Union[HubDevice.DefaultCameraPermission, str]] = ..., default_photo_on_demand_permission: _Optional[_Union[HubDevice.DefaultPhotoOnDemandPermission, str]] = ..., default_user_camera_permission: _Optional[_Union[HubDevice.DefaultUserCameraPermission, str]] = ..., default_user_photo_on_demand_permission: _Optional[_Union[HubDevice.DefaultUserPhotoOnDemandPermission, str]] = ..., max_power_test_state: _Optional[_Union[HubDevice.MaxPowerTestState, str]] = ..., bus_status: _Optional[_Iterable[_Union[HubDevice.BusState, str]]] = ..., scan_status: _Optional[_Union[HubDevice.ScanStatus, str]] = ..., privacy_officer_options: _Optional[_Iterable[_Union[HubDevice.PrivacyOfficerOption, str]]] = ..., geofence: _Optional[_Union[HubDevice.GeoFence, _Mapping]] = ..., two_stage_arming_progress_status: _Optional[_Union[HubDevice.TwoStageArmingStatus, str]] = ..., two_stage_arming: _Optional[_Union[HubDevice.TwoStageArming, _Mapping]] = ...) -> None: ...
