from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MalfunctionInfo(_message.Message):
    __slots__ = ("malfunction_info",)
    class MalfunctionCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_MALFUNCTION_INFO: _ClassVar[MalfunctionInfo.MalfunctionCase]
        CABLE_BREAK_ISSUE: _ClassVar[MalfunctionInfo.MalfunctionCase]
        VOLTAGE_INSTABILITY: _ClassVar[MalfunctionInfo.MalfunctionCase]
        SIREN_VOLUME_TEST_REQUIRED: _ClassVar[MalfunctionInfo.MalfunctionCase]
        CO_SENSOR_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[MalfunctionInfo.MalfunctionCase]
        SMOKE_DETECTOR_CAMERA_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[MalfunctionInfo.MalfunctionCase]
        ACCELEROMETER_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BAD_INPUT_RESISTANCE: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BAD_TEMPERATURE: _ClassVar[MalfunctionInfo.MalfunctionCase]
        END_OF_LIFE: _ClassVar[MalfunctionInfo.MalfunctionCase]
        CHARGER_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BATTERY_HARDWARE_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        MEMORY_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        WATCHDOG_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BATTERY_LOAD_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        MODEM_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        WIFI_CONNECTION_FAIL: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BATTERY_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        BATTERY_CHARGE_ERROR: _ClassVar[MalfunctionInfo.MalfunctionCase]
        SOFTWARE_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        FLASH_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
        HARDWARE_MALFUNCTION: _ClassVar[MalfunctionInfo.MalfunctionCase]
    NO_MALFUNCTION_INFO: MalfunctionInfo.MalfunctionCase
    CABLE_BREAK_ISSUE: MalfunctionInfo.MalfunctionCase
    VOLTAGE_INSTABILITY: MalfunctionInfo.MalfunctionCase
    SIREN_VOLUME_TEST_REQUIRED: MalfunctionInfo.MalfunctionCase
    CO_SENSOR_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    CO_SENSOR_LEVEL_EXCEEDED: MalfunctionInfo.MalfunctionCase
    SMOKE_DETECTOR_CAMERA_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    MICROWAVE_SENSOR_CALIBRATION_ERROR: MalfunctionInfo.MalfunctionCase
    ACCELEROMETER_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    BAD_INPUT_RESISTANCE: MalfunctionInfo.MalfunctionCase
    BAD_TEMPERATURE: MalfunctionInfo.MalfunctionCase
    END_OF_LIFE: MalfunctionInfo.MalfunctionCase
    CHARGER_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    BATTERY_HARDWARE_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    MEMORY_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    WATCHDOG_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    BATTERY_LOAD_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    MODEM_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    WIFI_CONNECTION_FAIL: MalfunctionInfo.MalfunctionCase
    BATTERY_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    BATTERY_CHARGE_ERROR: MalfunctionInfo.MalfunctionCase
    SOFTWARE_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    FLASH_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    HARDWARE_MALFUNCTION: MalfunctionInfo.MalfunctionCase
    MALFUNCTION_INFO_FIELD_NUMBER: _ClassVar[int]
    malfunction_info: MalfunctionInfo.MalfunctionCase
    def __init__(self, malfunction_info: _Optional[_Union[MalfunctionInfo.MalfunctionCase, str]] = ...) -> None: ...
