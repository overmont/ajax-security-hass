from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonDevicePart(_message.Message):
    __slots__ = ("id", "temperature", "signal_level", "tampered", "battery_charge_level_percentage", "name", "room_id", "online", "issues_count", "state", "device_transmission_power_mode", "night_mode_arm", "malfunctions", "assigned_extender", "color", "cms_device_index", "battery_ok", "group_id", "battery_charge_volt", "arm_delay_seconds", "alarm_delay_seconds", "apply_delays_to_night_mode", "firmware_version", "verifies_alarm", "bypass_mode", "is_bypass_mode", "device_alarm_logic_type", "indicator_light_mode", "perimeter_arm_delay_seconds", "perimeter_alarm_delay_seconds", "estimated_arming_state", "migration_state")
    class DeviceColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_COLOR_INFO: _ClassVar[CommonDevicePart.DeviceColor]
        WHITE: _ClassVar[CommonDevicePart.DeviceColor]
        BLACK: _ClassVar[CommonDevicePart.DeviceColor]
        WHITE_LABEL_WHITE: _ClassVar[CommonDevicePart.DeviceColor]
        WHITE_LABEL_BLACK: _ClassVar[CommonDevicePart.DeviceColor]
    NO_COLOR_INFO: CommonDevicePart.DeviceColor
    WHITE: CommonDevicePart.DeviceColor
    BLACK: CommonDevicePart.DeviceColor
    WHITE_LABEL_WHITE: CommonDevicePart.DeviceColor
    WHITE_LABEL_BLACK: CommonDevicePart.DeviceColor
    class DeviceSignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIGNAL_LEVEL_INFO: _ClassVar[CommonDevicePart.DeviceSignalLevel]
        NO_SIGNAL: _ClassVar[CommonDevicePart.DeviceSignalLevel]
        WEAK: _ClassVar[CommonDevicePart.DeviceSignalLevel]
        NORMAL: _ClassVar[CommonDevicePart.DeviceSignalLevel]
        STRONG: _ClassVar[CommonDevicePart.DeviceSignalLevel]
    NO_SIGNAL_LEVEL_INFO: CommonDevicePart.DeviceSignalLevel
    NO_SIGNAL: CommonDevicePart.DeviceSignalLevel
    WEAK: CommonDevicePart.DeviceSignalLevel
    NORMAL: CommonDevicePart.DeviceSignalLevel
    STRONG: CommonDevicePart.DeviceSignalLevel
    class DeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_STATE_INFO: _ClassVar[CommonDevicePart.DeviceState]
        PASSIVE: _ClassVar[CommonDevicePart.DeviceState]
        ACTIVE: _ClassVar[CommonDevicePart.DeviceState]
        DETECTION_AREA_TEST: _ClassVar[CommonDevicePart.DeviceState]
        RADIO_CONNECTION_TEST: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_RADIO_CONNECTION_TEST_START: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_RADIO_CONNECTION_TEST_END: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_DETECTION_AREA_TEST_START: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_DETECTION_AREA_TEST_END: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_REGISTRATION: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_RADIO_CHANNEL_TEST_START: _ClassVar[CommonDevicePart.DeviceState]
        RADIO_CHANNEL_TEST: _ClassVar[CommonDevicePart.DeviceState]
        WAIT_RADIO_CHANNEL_TEST_END: _ClassVar[CommonDevicePart.DeviceState]
    NO_DEVICE_STATE_INFO: CommonDevicePart.DeviceState
    PASSIVE: CommonDevicePart.DeviceState
    ACTIVE: CommonDevicePart.DeviceState
    DETECTION_AREA_TEST: CommonDevicePart.DeviceState
    RADIO_CONNECTION_TEST: CommonDevicePart.DeviceState
    WAIT_RADIO_CONNECTION_TEST_START: CommonDevicePart.DeviceState
    WAIT_RADIO_CONNECTION_TEST_END: CommonDevicePart.DeviceState
    WAIT_DETECTION_AREA_TEST_START: CommonDevicePart.DeviceState
    WAIT_DETECTION_AREA_TEST_END: CommonDevicePart.DeviceState
    WAIT_REGISTRATION: CommonDevicePart.DeviceState
    WAIT_RADIO_CHANNEL_TEST_START: CommonDevicePart.DeviceState
    RADIO_CHANNEL_TEST: CommonDevicePart.DeviceState
    WAIT_RADIO_CHANNEL_TEST_END: CommonDevicePart.DeviceState
    class DeviceMalfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_MALFUNCTION_INFO: _ClassVar[CommonDevicePart.DeviceMalfunction]
        CABLE_BREAK_ISSUE: _ClassVar[CommonDevicePart.DeviceMalfunction]
        VOLTAGE_INSTABILITY: _ClassVar[CommonDevicePart.DeviceMalfunction]
        SIREN_VOLUME_TEST_REQUIRED: _ClassVar[CommonDevicePart.DeviceMalfunction]
        CO_SENSOR_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[CommonDevicePart.DeviceMalfunction]
        SMOKE_DETECTOR_CAMERA_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[CommonDevicePart.DeviceMalfunction]
        ACCELEROMETER_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        BAD_INPUT_RESISTANCE: _ClassVar[CommonDevicePart.DeviceMalfunction]
        MODEM_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        WIFI_CONNECTION_FAIL: _ClassVar[CommonDevicePart.DeviceMalfunction]
        BATTERY_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        BATTERY_CHARGE_ERROR: _ClassVar[CommonDevicePart.DeviceMalfunction]
        SOFTWARE_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
        FLASH_MALFUNCTION: _ClassVar[CommonDevicePart.DeviceMalfunction]
    NO_MALFUNCTION_INFO: CommonDevicePart.DeviceMalfunction
    CABLE_BREAK_ISSUE: CommonDevicePart.DeviceMalfunction
    VOLTAGE_INSTABILITY: CommonDevicePart.DeviceMalfunction
    SIREN_VOLUME_TEST_REQUIRED: CommonDevicePart.DeviceMalfunction
    CO_SENSOR_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    CO_SENSOR_LEVEL_EXCEEDED: CommonDevicePart.DeviceMalfunction
    SMOKE_DETECTOR_CAMERA_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    MICROWAVE_SENSOR_CALIBRATION_ERROR: CommonDevicePart.DeviceMalfunction
    ACCELEROMETER_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    BAD_INPUT_RESISTANCE: CommonDevicePart.DeviceMalfunction
    MODEM_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    WIFI_CONNECTION_FAIL: CommonDevicePart.DeviceMalfunction
    BATTERY_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    BATTERY_CHARGE_ERROR: CommonDevicePart.DeviceMalfunction
    SOFTWARE_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    FLASH_MALFUNCTION: CommonDevicePart.DeviceMalfunction
    class BypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BYPASS_MODE_INFO: _ClassVar[CommonDevicePart.BypassMode]
        ENGINEER_BYPASS_OFF: _ClassVar[CommonDevicePart.BypassMode]
        ENGINEER_BYPASS_ON: _ClassVar[CommonDevicePart.BypassMode]
        TAMPER_BYPASS_ON: _ClassVar[CommonDevicePart.BypassMode]
    NO_BYPASS_MODE_INFO: CommonDevicePart.BypassMode
    ENGINEER_BYPASS_OFF: CommonDevicePart.BypassMode
    ENGINEER_BYPASS_ON: CommonDevicePart.BypassMode
    TAMPER_BYPASS_ON: CommonDevicePart.BypassMode
    class IsBypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_IN_BYPASS_MODE: _ClassVar[CommonDevicePart.IsBypassMode]
        ENABLED_ENGINEER_BYPASS: _ClassVar[CommonDevicePart.IsBypassMode]
        ENABLED_TAMPER_BYPASS: _ClassVar[CommonDevicePart.IsBypassMode]
        AUTO_BYPASS_BY_COUNT: _ClassVar[CommonDevicePart.IsBypassMode]
        AUTO_BYPASS_BY_ACTIVE: _ClassVar[CommonDevicePart.IsBypassMode]
    NO_IN_BYPASS_MODE: CommonDevicePart.IsBypassMode
    ENABLED_ENGINEER_BYPASS: CommonDevicePart.IsBypassMode
    ENABLED_TAMPER_BYPASS: CommonDevicePart.IsBypassMode
    AUTO_BYPASS_BY_COUNT: CommonDevicePart.IsBypassMode
    AUTO_BYPASS_BY_ACTIVE: CommonDevicePart.IsBypassMode
    class DeviceAlarmLogicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_ALARM_LOGIC_TYPE: _ClassVar[CommonDevicePart.DeviceAlarmLogicType]
        NONE: _ClassVar[CommonDevicePart.DeviceAlarmLogicType]
        ARMING_COMPLETION_DEVICE: _ClassVar[CommonDevicePart.DeviceAlarmLogicType]
        ENTRY_ROUTE: _ClassVar[CommonDevicePart.DeviceAlarmLogicType]
    NO_DEVICE_ALARM_LOGIC_TYPE: CommonDevicePart.DeviceAlarmLogicType
    NONE: CommonDevicePart.DeviceAlarmLogicType
    ARMING_COMPLETION_DEVICE: CommonDevicePart.DeviceAlarmLogicType
    ENTRY_ROUTE: CommonDevicePart.DeviceAlarmLogicType
    class IndicatorLightMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_INDICATOR_LIGHT_MODE_INFO: _ClassVar[CommonDevicePart.IndicatorLightMode]
        DONT_BLINK_ON_ALARM: _ClassVar[CommonDevicePart.IndicatorLightMode]
        STANDARD: _ClassVar[CommonDevicePart.IndicatorLightMode]
    NO_INDICATOR_LIGHT_MODE_INFO: CommonDevicePart.IndicatorLightMode
    DONT_BLINK_ON_ALARM: CommonDevicePart.IndicatorLightMode
    STANDARD: CommonDevicePart.IndicatorLightMode
    class EstimatedArmingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ESTIMATED_ARMING_STATE_INFO: _ClassVar[CommonDevicePart.EstimatedArmingState]
        DISARMED: _ClassVar[CommonDevicePart.EstimatedArmingState]
        ARMED: _ClassVar[CommonDevicePart.EstimatedArmingState]
        N_A: _ClassVar[CommonDevicePart.EstimatedArmingState]
    NO_ESTIMATED_ARMING_STATE_INFO: CommonDevicePart.EstimatedArmingState
    DISARMED: CommonDevicePart.EstimatedArmingState
    ARMED: CommonDevicePart.EstimatedArmingState
    N_A: CommonDevicePart.EstimatedArmingState
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TAMPERED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ARM_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BATTERY_OK_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGE_VOLT_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    APPLY_DELAYS_TO_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERIFIES_ALARM_FIELD_NUMBER: _ClassVar[int]
    BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ALARM_LOGIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDICATOR_LIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ARMING_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    temperature: _wrappers_pb2.Int32Value
    signal_level: CommonDevicePart.DeviceSignalLevel
    tampered: _wrappers_pb2.BoolValue
    battery_charge_level_percentage: _wrappers_pb2.Int32Value
    name: _name_pb2.Name
    room_id: str
    online: _wrappers_pb2.BoolValue
    issues_count: _wrappers_pb2.Int32Value
    state: CommonDevicePart.DeviceState
    device_transmission_power_mode: int
    night_mode_arm: bool
    malfunctions: _containers.RepeatedScalarFieldContainer[CommonDevicePart.DeviceMalfunction]
    assigned_extender: int
    color: CommonDevicePart.DeviceColor
    cms_device_index: int
    battery_ok: _wrappers_pb2.BoolValue
    group_id: str
    battery_charge_volt: _wrappers_pb2.Int32Value
    arm_delay_seconds: int
    alarm_delay_seconds: int
    apply_delays_to_night_mode: bool
    firmware_version: str
    verifies_alarm: bool
    bypass_mode: CommonDevicePart.BypassMode
    is_bypass_mode: _containers.RepeatedScalarFieldContainer[CommonDevicePart.IsBypassMode]
    device_alarm_logic_type: CommonDevicePart.DeviceAlarmLogicType
    indicator_light_mode: CommonDevicePart.IndicatorLightMode
    perimeter_arm_delay_seconds: int
    perimeter_alarm_delay_seconds: int
    estimated_arming_state: CommonDevicePart.EstimatedArmingState
    migration_state: int
    def __init__(self, id: _Optional[str] = ..., temperature: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., signal_level: _Optional[_Union[CommonDevicePart.DeviceSignalLevel, str]] = ..., tampered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., battery_charge_level_percentage: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., room_id: _Optional[str] = ..., online: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., issues_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., state: _Optional[_Union[CommonDevicePart.DeviceState, str]] = ..., device_transmission_power_mode: _Optional[int] = ..., night_mode_arm: bool = ..., malfunctions: _Optional[_Iterable[_Union[CommonDevicePart.DeviceMalfunction, str]]] = ..., assigned_extender: _Optional[int] = ..., color: _Optional[_Union[CommonDevicePart.DeviceColor, str]] = ..., cms_device_index: _Optional[int] = ..., battery_ok: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., group_id: _Optional[str] = ..., battery_charge_volt: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., arm_delay_seconds: _Optional[int] = ..., alarm_delay_seconds: _Optional[int] = ..., apply_delays_to_night_mode: bool = ..., firmware_version: _Optional[str] = ..., verifies_alarm: bool = ..., bypass_mode: _Optional[_Union[CommonDevicePart.BypassMode, str]] = ..., is_bypass_mode: _Optional[_Iterable[_Union[CommonDevicePart.IsBypassMode, str]]] = ..., device_alarm_logic_type: _Optional[_Union[CommonDevicePart.DeviceAlarmLogicType, str]] = ..., indicator_light_mode: _Optional[_Union[CommonDevicePart.IndicatorLightMode, str]] = ..., perimeter_arm_delay_seconds: _Optional[int] = ..., perimeter_alarm_delay_seconds: _Optional[int] = ..., estimated_arming_state: _Optional[_Union[CommonDevicePart.EstimatedArmingState, str]] = ..., migration_state: _Optional[int] = ...) -> None: ...
