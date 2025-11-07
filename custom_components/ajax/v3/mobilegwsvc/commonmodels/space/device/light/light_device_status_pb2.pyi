from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_signal_level_pb2 as _device_signal_level_pb2
from v3.mobilegwsvc.commonmodels.hub.device.common import sim_card_status_pb2 as _sim_card_status_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import life_quality_status_pb2 as _life_quality_status_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceStatus(_message.Message):
    __slots__ = ("gsm_status", "signal_strength", "sim_status", "monitoring", "camera_view", "someone_has_camera_stream_access", "someone_can_make_photo", "battery", "always_active", "rex_connected", "delay_when_leaving", "armed_in_night_mode", "access_card_disabled", "smoke_detected", "co_level_detected", "high_temperature_detected", "external_contact_broken", "case_drilling_detected", "fire_alarm_fp", "external_contact_alert", "roller_shutter", "door_opened", "leak_detected", "nfc", "ble", "power_management", "motion_detected", "interconnect", "high_voltage", "low_voltage", "current_short_circuit", "high_current_protection", "contact_hang", "migration_in_process", "pd_compliance_warning", "sia_compliance_warning", "ul_not_compliant", "standard_compliance_warning", "chimes_enabled", "real_active", "privacy", "relay_stuck", "light_switch_through_pass", "arc_spark_detected", "high_diff_temperature_detected", "malfunction", "end_of_service_life", "high_frame_interconnect", "device_firmware_status", "anti_masking_alert", "interference_detected", "door_need_anti_masking", "switch_alarm_pressed", "temporary_deactivation_whole", "temporary_deactivation_tamper", "temporary_deactivation_alarms", "temporary_deactivation_timer", "one_time_deactivation_whole", "one_time_deactivation_tamper", "temporary_deactivation", "one_time_deactivation", "smart_lock", "line_supply_high_temperature", "bukhoor", "smart_bracket_unlocked", "device_installation_warning", "power_line_low", "life_quality", "temperature", "wire_input_status", "transmitter_status", "active_subscription", "water_stop_valve_stuck", "water_stop_prevention_warning", "en54_fault", "annunciation_test_active", "lid_opened", "storage_device", "wifi_signal_level_status", "onvif_user_auth_enabled", "en54_fire_buzzer_status", "fire_buzzer_active", "en54_vad_status", "en54_disablement", "arc_reporting_disabled", "walk_test_status")
    class CustomAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_ALARM_TYPE_UNSPECIFIED: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_INTRUSION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_FIRE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MEDICAL: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_PANIC: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_GAS: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_TAMPER: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MALFUNCTION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_LEAK: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_SERVICE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_KEY_ARM: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_GLASS_BREAK: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_LOW_TEMPERATURE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MASKING: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_DURESS_CODE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_VIBRATION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_BOLT_CONTACT: _ClassVar[LightDeviceStatus.CustomAlarmType]
    CUSTOM_ALARM_TYPE_UNSPECIFIED: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_INTRUSION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_FIRE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MEDICAL: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_PANIC: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_GAS: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_TAMPER: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MALFUNCTION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_LEAK: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_SERVICE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_KEY_ARM: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_GLASS_BREAK: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_LOW_TEMPERATURE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MASKING: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_DURESS_CODE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_VIBRATION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_BOLT_CONTACT: LightDeviceStatus.CustomAlarmType
    class WifiSignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIFI_SIGNAL_LEVEL_UNSPECIFIED: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_NO_SIGNAL: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_WEAK: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_NORMAL: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_STRONG: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_DISCONNECTED: _ClassVar[LightDeviceStatus.WifiSignalLevel]
    WIFI_SIGNAL_LEVEL_UNSPECIFIED: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_NO_SIGNAL: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_WEAK: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_NORMAL: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_STRONG: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_DISCONNECTED: LightDeviceStatus.WifiSignalLevel
    class StorageDevice(_message.Message):
        __slots__ = ("storage_device_type", "storage_device_status")
        class StorageDeviceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORAGE_DEVICE_STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceStatus]
            STORAGE_DEVICE_STATUS_OK: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceStatus]
            STORAGE_DEVICE_STATUS_WARNING: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceStatus]
            STORAGE_DEVICE_STATUS_ERROR: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceStatus]
            STORAGE_DEVICE_STATUS_UNAVAILABLE: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceStatus]
        STORAGE_DEVICE_STATUS_UNSPECIFIED: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_OK: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_WARNING: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_ERROR: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_UNAVAILABLE: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        class StorageDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORAGE_DEVICE_TYPE_UNSPECIFIED: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceType]
            STORAGE_DEVICE_TYPE_SD_CARD: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceType]
            STORAGE_DEVICE_TYPE_HARD_DRIVE: _ClassVar[LightDeviceStatus.StorageDevice.StorageDeviceType]
        STORAGE_DEVICE_TYPE_UNSPECIFIED: LightDeviceStatus.StorageDevice.StorageDeviceType
        STORAGE_DEVICE_TYPE_SD_CARD: LightDeviceStatus.StorageDevice.StorageDeviceType
        STORAGE_DEVICE_TYPE_HARD_DRIVE: LightDeviceStatus.StorageDevice.StorageDeviceType
        STORAGE_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
        storage_device_type: LightDeviceStatus.StorageDevice.StorageDeviceType
        storage_device_status: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        def __init__(self, storage_device_type: _Optional[_Union[LightDeviceStatus.StorageDevice.StorageDeviceType, str]] = ..., storage_device_status: _Optional[_Union[LightDeviceStatus.StorageDevice.StorageDeviceStatus, str]] = ...) -> None: ...
    class Simple(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SimStatus(_message.Message):
        __slots__ = ("sim_card_status",)
        SIM_CARD_STATUS_FIELD_NUMBER: _ClassVar[int]
        sim_card_status: _sim_card_status_pb2.SimCardStatus
        def __init__(self, sim_card_status: _Optional[_Union[_sim_card_status_pb2.SimCardStatus, str]] = ...) -> None: ...
    class Monitoring(_message.Message):
        __slots__ = ("cms_active",)
        CMS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        cms_active: bool
        def __init__(self, cms_active: bool = ...) -> None: ...
    class CameraView(_message.Message):
        __slots__ = ("has_access",)
        HAS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        has_access: bool
        def __init__(self, has_access: bool = ...) -> None: ...
    class SignalStrength(_message.Message):
        __slots__ = ("device_signal_level",)
        DEVICE_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        device_signal_level: _device_signal_level_pb2.DeviceSignalLevel
        def __init__(self, device_signal_level: _Optional[_Union[_device_signal_level_pb2.DeviceSignalLevel, str]] = ...) -> None: ...
    class Battery(_message.Message):
        __slots__ = ("battery_state", "charge_level_percentage", "is_without_charge")
        class BatteryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BATTERY_STATE_UNSPECIFIED: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_OK: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_ERROR: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_WARNING: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_ALERT: _ClassVar[LightDeviceStatus.Battery.BatteryState]
        BATTERY_STATE_UNSPECIFIED: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_OK: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_ERROR: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_WARNING: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_ALERT: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_FIELD_NUMBER: _ClassVar[int]
        CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        IS_WITHOUT_CHARGE_FIELD_NUMBER: _ClassVar[int]
        battery_state: LightDeviceStatus.Battery.BatteryState
        charge_level_percentage: int
        is_without_charge: bool
        def __init__(self, battery_state: _Optional[_Union[LightDeviceStatus.Battery.BatteryState, str]] = ..., charge_level_percentage: _Optional[int] = ..., is_without_charge: bool = ...) -> None: ...
    class Nfc(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class Ble(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class MotionDetected(_message.Message):
        __slots__ = ("detected_at",)
        DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
        detected_at: _timestamp_pb2.Timestamp
        def __init__(self, detected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Privacy(_message.Message):
        __slots__ = ("is_video_surveillance", "enabled")
        IS_VIDEO_SURVEILLANCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        is_video_surveillance: bool
        enabled: bool
        def __init__(self, is_video_surveillance: bool = ..., enabled: bool = ...) -> None: ...
    class GsmStatus(_message.Message):
        __slots__ = ("type", "status")
        class GsmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GSM_TYPE_UNSPECIFIED: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_2G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_3G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_4G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
        GSM_TYPE_UNSPECIFIED: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_2G: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_3G: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_4G: LightDeviceStatus.GsmStatus.GsmType
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.GsmStatus.Status]
            STATUS_DISCONNECTED: _ClassVar[LightDeviceStatus.GsmStatus.Status]
            STATUS_CONNECTED: _ClassVar[LightDeviceStatus.GsmStatus.Status]
        STATUS_UNSPECIFIED: LightDeviceStatus.GsmStatus.Status
        STATUS_DISCONNECTED: LightDeviceStatus.GsmStatus.Status
        STATUS_CONNECTED: LightDeviceStatus.GsmStatus.Status
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        type: LightDeviceStatus.GsmStatus.GsmType
        status: LightDeviceStatus.GsmStatus.Status
        def __init__(self, type: _Optional[_Union[LightDeviceStatus.GsmStatus.GsmType, str]] = ..., status: _Optional[_Union[LightDeviceStatus.GsmStatus.Status, str]] = ...) -> None: ...
    class DeviceFirmware(_message.Message):
        __slots__ = ("in_progress", "failed", "critical_firmware_available")
        IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        CRITICAL_FIRMWARE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        in_progress: LightDeviceStatus.Simple
        failed: LightDeviceStatus.Simple
        critical_firmware_available: LightDeviceStatus.Simple
        def __init__(self, in_progress: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., failed: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., critical_firmware_available: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ...) -> None: ...
    class SmartLock(_message.Message):
        __slots__ = ("in_progress", "failed")
        IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        in_progress: LightDeviceStatus.Simple
        failed: LightDeviceStatus.Simple
        def __init__(self, in_progress: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., failed: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ...) -> None: ...
    class LifeQualityStatus(_message.Message):
        __slots__ = ("actual_temperature", "actual_humidity", "actual_co2", "hardware_malfunctions", "temperature_statuses", "humidity_statuses", "co2_statuses")
        ACTUAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_CO2_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_STATUSES_FIELD_NUMBER: _ClassVar[int]
        HUMIDITY_STATUSES_FIELD_NUMBER: _ClassVar[int]
        CO2_STATUSES_FIELD_NUMBER: _ClassVar[int]
        actual_temperature: int
        actual_humidity: int
        actual_co2: int
        hardware_malfunctions: _containers.RepeatedScalarFieldContainer[_life_quality_status_pb2.HardwareMalfunction]
        temperature_statuses: _containers.RepeatedScalarFieldContainer[_life_quality_status_pb2.TemperatureStatus]
        humidity_statuses: _containers.RepeatedScalarFieldContainer[_life_quality_status_pb2.HumidityStatus]
        co2_statuses: _containers.RepeatedScalarFieldContainer[_life_quality_status_pb2.Co2Status]
        def __init__(self, actual_temperature: _Optional[int] = ..., actual_humidity: _Optional[int] = ..., actual_co2: _Optional[int] = ..., hardware_malfunctions: _Optional[_Iterable[_Union[_life_quality_status_pb2.HardwareMalfunction, str]]] = ..., temperature_statuses: _Optional[_Iterable[_Union[_life_quality_status_pb2.TemperatureStatus, str]]] = ..., humidity_statuses: _Optional[_Iterable[_Union[_life_quality_status_pb2.HumidityStatus, str]]] = ..., co2_statuses: _Optional[_Iterable[_Union[_life_quality_status_pb2.Co2Status, str]]] = ...) -> None: ...
    class ValueStatus(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class WireInputStatus(_message.Message):
        __slots__ = ("contact_index", "is_alert", "type")
        CONTACT_INDEX_FIELD_NUMBER: _ClassVar[int]
        IS_ALERT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        contact_index: int
        is_alert: bool
        type: LightDeviceStatus.CustomAlarmType
        def __init__(self, contact_index: _Optional[int] = ..., is_alert: bool = ..., type: _Optional[_Union[LightDeviceStatus.CustomAlarmType, str]] = ...) -> None: ...
    class TransmitterStatus(_message.Message):
        __slots__ = ("is_alert", "type")
        IS_ALERT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        is_alert: bool
        type: LightDeviceStatus.CustomAlarmType
        def __init__(self, is_alert: bool = ..., type: _Optional[_Union[LightDeviceStatus.CustomAlarmType, str]] = ...) -> None: ...
    class RexConnected(_message.Message):
        __slots__ = ("is_rex_online",)
        IS_REX_ONLINE_FIELD_NUMBER: _ClassVar[int]
        is_rex_online: bool
        def __init__(self, is_rex_online: bool = ...) -> None: ...
    class En54FireBuzzerStatus(_message.Message):
        __slots__ = ("status",)
        class BuzzerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BUZZER_STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus]
            BUZZER_STATUS_ACTIVE: _ClassVar[LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus]
            BUZZER_STATUS_SILENCED: _ClassVar[LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus]
            BUZZER_STATUS_INACTIVE: _ClassVar[LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus]
        BUZZER_STATUS_UNSPECIFIED: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_ACTIVE: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_SILENCED: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_INACTIVE: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        def __init__(self, status: _Optional[_Union[LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus, str]] = ...) -> None: ...
    class En54VadStatus(_message.Message):
        __slots__ = ("status",)
        class VadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VAD_STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_ACTIVE: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_SILENCED: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_INACTIVE: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
        VAD_STATUS_UNSPECIFIED: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_ACTIVE: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_SILENCED: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_INACTIVE: LightDeviceStatus.En54VadStatus.VadStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.En54VadStatus.VadStatus
        def __init__(self, status: _Optional[_Union[LightDeviceStatus.En54VadStatus.VadStatus, str]] = ...) -> None: ...
    class WalkTestStatus(_message.Message):
        __slots__ = ("status",)
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]
            STATUS_LAUNCH: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]
            STATUS_PROCESS: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]
        STATUS_UNSPECIFIED: LightDeviceStatus.WalkTestStatus.Status
        STATUS_LAUNCH: LightDeviceStatus.WalkTestStatus.Status
        STATUS_PROCESS: LightDeviceStatus.WalkTestStatus.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.WalkTestStatus.Status
        def __init__(self, status: _Optional[_Union[LightDeviceStatus.WalkTestStatus.Status, str]] = ...) -> None: ...
    class WifiSignalLevelStatus(_message.Message):
        __slots__ = ("wifi_signal_level",)
        WIFI_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        wifi_signal_level: LightDeviceStatus.WifiSignalLevel
        def __init__(self, wifi_signal_level: _Optional[_Union[LightDeviceStatus.WifiSignalLevel, str]] = ...) -> None: ...
    GSM_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    SIM_STATUS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    CAMERA_VIEW_FIELD_NUMBER: _ClassVar[int]
    SOMEONE_HAS_CAMERA_STREAM_ACCESS_FIELD_NUMBER: _ClassVar[int]
    SOMEONE_CAN_MAKE_PHOTO_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    REX_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DELAY_WHEN_LEAVING_FIELD_NUMBER: _ClassVar[int]
    ARMED_IN_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_BROKEN_FIELD_NUMBER: _ClassVar[int]
    CASE_DRILLING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_FP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALERT_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPENED_FIELD_NUMBER: _ClassVar[int]
    LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    NFC_FIELD_NUMBER: _ClassVar[int]
    BLE_FIELD_NUMBER: _ClassVar[int]
    POWER_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    HIGH_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    LOW_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    HIGH_CURRENT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CONTACT_HANG_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_IN_PROCESS_FIELD_NUMBER: _ClassVar[int]
    PD_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    SIA_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    UL_NOT_COMPLIANT_FIELD_NUMBER: _ClassVar[int]
    STANDARD_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    CHIMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REAL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_FIELD_NUMBER: _ClassVar[int]
    RELAY_STUCK_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SWITCH_THROUGH_PASS_FIELD_NUMBER: _ClassVar[int]
    ARC_SPARK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_DIFF_TEMPERATURE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    END_OF_SERVICE_LIFE_FIELD_NUMBER: _ClassVar[int]
    HIGH_FRAME_INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ANTI_MASKING_ALERT_FIELD_NUMBER: _ClassVar[int]
    INTERFERENCE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    DOOR_NEED_ANTI_MASKING_FIELD_NUMBER: _ClassVar[int]
    SWITCH_ALARM_PRESSED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_WHOLE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_TAMPER_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_ALARMS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_TIMER_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_WHOLE_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_TAMPER_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    LINE_SUPPLY_HIGH_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_FIELD_NUMBER: _ClassVar[int]
    SMART_BRACKET_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INSTALLATION_WARNING_FIELD_NUMBER: _ClassVar[int]
    POWER_LINE_LOW_FIELD_NUMBER: _ClassVar[int]
    LIFE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSMITTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WATER_STOP_VALVE_STUCK_FIELD_NUMBER: _ClassVar[int]
    WATER_STOP_PREVENTION_WARNING_FIELD_NUMBER: _ClassVar[int]
    EN54_FAULT_FIELD_NUMBER: _ClassVar[int]
    ANNUNCIATION_TEST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LID_OPENED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    WIFI_SIGNAL_LEVEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    ONVIF_USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_BUZZER_STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRE_BUZZER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EN54_VAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    EN54_DISABLEMENT_FIELD_NUMBER: _ClassVar[int]
    ARC_REPORTING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    gsm_status: LightDeviceStatus.GsmStatus
    signal_strength: LightDeviceStatus.SignalStrength
    sim_status: LightDeviceStatus.SimStatus
    monitoring: LightDeviceStatus.Monitoring
    camera_view: LightDeviceStatus.CameraView
    someone_has_camera_stream_access: LightDeviceStatus.Simple
    someone_can_make_photo: LightDeviceStatus.Simple
    battery: LightDeviceStatus.Battery
    always_active: LightDeviceStatus.Simple
    rex_connected: LightDeviceStatus.RexConnected
    delay_when_leaving: LightDeviceStatus.Simple
    armed_in_night_mode: LightDeviceStatus.Simple
    access_card_disabled: LightDeviceStatus.Simple
    smoke_detected: LightDeviceStatus.Simple
    co_level_detected: LightDeviceStatus.Simple
    high_temperature_detected: LightDeviceStatus.Simple
    external_contact_broken: LightDeviceStatus.Simple
    case_drilling_detected: LightDeviceStatus.Simple
    fire_alarm_fp: LightDeviceStatus.Simple
    external_contact_alert: LightDeviceStatus.Simple
    roller_shutter: LightDeviceStatus.Simple
    door_opened: LightDeviceStatus.Simple
    leak_detected: LightDeviceStatus.Simple
    nfc: LightDeviceStatus.Nfc
    ble: LightDeviceStatus.Ble
    power_management: LightDeviceStatus.Simple
    motion_detected: LightDeviceStatus.MotionDetected
    interconnect: LightDeviceStatus.Simple
    high_voltage: LightDeviceStatus.Simple
    low_voltage: LightDeviceStatus.Simple
    current_short_circuit: LightDeviceStatus.Simple
    high_current_protection: LightDeviceStatus.Simple
    contact_hang: LightDeviceStatus.Simple
    migration_in_process: LightDeviceStatus.Simple
    pd_compliance_warning: LightDeviceStatus.Simple
    sia_compliance_warning: LightDeviceStatus.Simple
    ul_not_compliant: LightDeviceStatus.Simple
    standard_compliance_warning: LightDeviceStatus.Simple
    chimes_enabled: LightDeviceStatus.Simple
    real_active: LightDeviceStatus.Simple
    privacy: LightDeviceStatus.Privacy
    relay_stuck: LightDeviceStatus.Simple
    light_switch_through_pass: LightDeviceStatus.Simple
    arc_spark_detected: LightDeviceStatus.Simple
    high_diff_temperature_detected: LightDeviceStatus.Simple
    malfunction: LightDeviceStatus.Simple
    end_of_service_life: LightDeviceStatus.Simple
    high_frame_interconnect: LightDeviceStatus.Simple
    device_firmware_status: LightDeviceStatus.DeviceFirmware
    anti_masking_alert: LightDeviceStatus.Simple
    interference_detected: LightDeviceStatus.Simple
    door_need_anti_masking: LightDeviceStatus.Simple
    switch_alarm_pressed: LightDeviceStatus.Simple
    temporary_deactivation_whole: LightDeviceStatus.Simple
    temporary_deactivation_tamper: LightDeviceStatus.Simple
    temporary_deactivation_alarms: LightDeviceStatus.Simple
    temporary_deactivation_timer: LightDeviceStatus.Simple
    one_time_deactivation_whole: LightDeviceStatus.Simple
    one_time_deactivation_tamper: LightDeviceStatus.Simple
    temporary_deactivation: LightDeviceStatus.Simple
    one_time_deactivation: LightDeviceStatus.Simple
    smart_lock: _smart_lock_pb2.SmartLockStatus.LockStatus
    line_supply_high_temperature: LightDeviceStatus.Simple
    bukhoor: LightDeviceStatus.Simple
    smart_bracket_unlocked: LightDeviceStatus.Simple
    device_installation_warning: LightDeviceStatus.Simple
    power_line_low: LightDeviceStatus.Simple
    life_quality: LightDeviceStatus.LifeQualityStatus
    temperature: LightDeviceStatus.ValueStatus
    wire_input_status: LightDeviceStatus.WireInputStatus
    transmitter_status: LightDeviceStatus.TransmitterStatus
    active_subscription: LightDeviceStatus.Simple
    water_stop_valve_stuck: LightDeviceStatus.Simple
    water_stop_prevention_warning: LightDeviceStatus.Simple
    en54_fault: LightDeviceStatus.Simple
    annunciation_test_active: LightDeviceStatus.Simple
    lid_opened: LightDeviceStatus.Simple
    storage_device: LightDeviceStatus.StorageDevice
    wifi_signal_level_status: LightDeviceStatus.WifiSignalLevelStatus
    onvif_user_auth_enabled: LightDeviceStatus.Simple
    en54_fire_buzzer_status: LightDeviceStatus.En54FireBuzzerStatus
    fire_buzzer_active: LightDeviceStatus.Simple
    en54_vad_status: LightDeviceStatus.En54VadStatus
    en54_disablement: LightDeviceStatus.Simple
    arc_reporting_disabled: LightDeviceStatus.Simple
    walk_test_status: LightDeviceStatus.WalkTestStatus
    def __init__(self, gsm_status: _Optional[_Union[LightDeviceStatus.GsmStatus, _Mapping]] = ..., signal_strength: _Optional[_Union[LightDeviceStatus.SignalStrength, _Mapping]] = ..., sim_status: _Optional[_Union[LightDeviceStatus.SimStatus, _Mapping]] = ..., monitoring: _Optional[_Union[LightDeviceStatus.Monitoring, _Mapping]] = ..., camera_view: _Optional[_Union[LightDeviceStatus.CameraView, _Mapping]] = ..., someone_has_camera_stream_access: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., someone_can_make_photo: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., battery: _Optional[_Union[LightDeviceStatus.Battery, _Mapping]] = ..., always_active: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., rex_connected: _Optional[_Union[LightDeviceStatus.RexConnected, _Mapping]] = ..., delay_when_leaving: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., armed_in_night_mode: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., access_card_disabled: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., smoke_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., co_level_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., high_temperature_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., external_contact_broken: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., case_drilling_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., fire_alarm_fp: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., external_contact_alert: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., roller_shutter: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., door_opened: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., leak_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., nfc: _Optional[_Union[LightDeviceStatus.Nfc, _Mapping]] = ..., ble: _Optional[_Union[LightDeviceStatus.Ble, _Mapping]] = ..., power_management: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., motion_detected: _Optional[_Union[LightDeviceStatus.MotionDetected, _Mapping]] = ..., interconnect: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., high_voltage: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., low_voltage: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., current_short_circuit: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., high_current_protection: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., contact_hang: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., migration_in_process: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., pd_compliance_warning: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., sia_compliance_warning: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., ul_not_compliant: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., standard_compliance_warning: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., chimes_enabled: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., real_active: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., privacy: _Optional[_Union[LightDeviceStatus.Privacy, _Mapping]] = ..., relay_stuck: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., light_switch_through_pass: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., arc_spark_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., high_diff_temperature_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., malfunction: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., end_of_service_life: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., high_frame_interconnect: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., device_firmware_status: _Optional[_Union[LightDeviceStatus.DeviceFirmware, _Mapping]] = ..., anti_masking_alert: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., interference_detected: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., door_need_anti_masking: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., switch_alarm_pressed: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., temporary_deactivation_whole: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., temporary_deactivation_tamper: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., temporary_deactivation_alarms: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., temporary_deactivation_timer: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., one_time_deactivation_whole: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., one_time_deactivation_tamper: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., temporary_deactivation: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., one_time_deactivation: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., smart_lock: _Optional[_Union[_smart_lock_pb2.SmartLockStatus.LockStatus, str]] = ..., line_supply_high_temperature: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., bukhoor: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., smart_bracket_unlocked: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., device_installation_warning: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., power_line_low: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., life_quality: _Optional[_Union[LightDeviceStatus.LifeQualityStatus, _Mapping]] = ..., temperature: _Optional[_Union[LightDeviceStatus.ValueStatus, _Mapping]] = ..., wire_input_status: _Optional[_Union[LightDeviceStatus.WireInputStatus, _Mapping]] = ..., transmitter_status: _Optional[_Union[LightDeviceStatus.TransmitterStatus, _Mapping]] = ..., active_subscription: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., water_stop_valve_stuck: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., water_stop_prevention_warning: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., en54_fault: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., annunciation_test_active: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., lid_opened: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., storage_device: _Optional[_Union[LightDeviceStatus.StorageDevice, _Mapping]] = ..., wifi_signal_level_status: _Optional[_Union[LightDeviceStatus.WifiSignalLevelStatus, _Mapping]] = ..., onvif_user_auth_enabled: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., en54_fire_buzzer_status: _Optional[_Union[LightDeviceStatus.En54FireBuzzerStatus, _Mapping]] = ..., fire_buzzer_active: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., en54_vad_status: _Optional[_Union[LightDeviceStatus.En54VadStatus, _Mapping]] = ..., en54_disablement: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., arc_reporting_disabled: _Optional[_Union[LightDeviceStatus.Simple, _Mapping]] = ..., walk_test_status: _Optional[_Union[LightDeviceStatus.WalkTestStatus, _Mapping]] = ...) -> None: ...
