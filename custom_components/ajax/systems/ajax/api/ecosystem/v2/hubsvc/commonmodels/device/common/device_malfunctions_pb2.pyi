from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceMalfunctions(_message.Message):
    __slots__ = ("malfunctions",)
    class Malfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALFUNCTION_UNSPECIFIED: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_CABLE_BREAK_ISSUE: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_VOLTAGE_INSTABILITY: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_SIREN_VOLUME_TEST_REQUIRED: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_CO_SENSOR_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_SENSOR_CAL_ERROR_1: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_ACCELEROMETER_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BAD_INPUT_RESISTANCE: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BAD_TEMPERATURE: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_END_OF_LIFE: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_HARDWARE_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_CHARGER_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_HARDWARE_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MEMORY_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_WATCHDOG_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_LOAD_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MODEM_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_WIFI_CONNECTION_FAIL: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_CHARGE_ERROR: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_SOFTWARE_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_FLASH_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MASKING_SENSOR_CALIBRATION_FAILED: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MASKING_SENSOR_BROKEN: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_PIR_SENSOR_BROKEN: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MICROWAVE_SENSOR_BROKEN: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_CAMERA_MODULE_MALFUNCTION: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_MAGNETOMETER_ERROR: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_FAILS_CHARGE_FULLY: _ClassVar[DeviceMalfunctions.Malfunction]
        MALFUNCTION_BATTERY_NOT_INSTALLED: _ClassVar[DeviceMalfunctions.Malfunction]
    MALFUNCTION_UNSPECIFIED: DeviceMalfunctions.Malfunction
    MALFUNCTION_CABLE_BREAK_ISSUE: DeviceMalfunctions.Malfunction
    MALFUNCTION_VOLTAGE_INSTABILITY: DeviceMalfunctions.Malfunction
    MALFUNCTION_SIREN_VOLUME_TEST_REQUIRED: DeviceMalfunctions.Malfunction
    MALFUNCTION_CO_SENSOR_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_CO_SENSOR_LEVEL_EXCEEDED: DeviceMalfunctions.Malfunction
    MALFUNCTION_SENSOR_CAL_ERROR_1: DeviceMalfunctions.Malfunction
    MALFUNCTION_MICROWAVE_SENSOR_CALIBRATION_ERROR: DeviceMalfunctions.Malfunction
    MALFUNCTION_ACCELEROMETER_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_BAD_INPUT_RESISTANCE: DeviceMalfunctions.Malfunction
    MALFUNCTION_BAD_TEMPERATURE: DeviceMalfunctions.Malfunction
    MALFUNCTION_END_OF_LIFE: DeviceMalfunctions.Malfunction
    MALFUNCTION_HARDWARE_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_CHARGER_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_HARDWARE_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_MEMORY_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_WATCHDOG_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_LOAD_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_MODEM_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_WIFI_CONNECTION_FAIL: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_CHARGE_ERROR: DeviceMalfunctions.Malfunction
    MALFUNCTION_SOFTWARE_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_FLASH_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_MASKING_SENSOR_CALIBRATION_FAILED: DeviceMalfunctions.Malfunction
    MALFUNCTION_MASKING_SENSOR_BROKEN: DeviceMalfunctions.Malfunction
    MALFUNCTION_PIR_SENSOR_BROKEN: DeviceMalfunctions.Malfunction
    MALFUNCTION_MICROWAVE_SENSOR_BROKEN: DeviceMalfunctions.Malfunction
    MALFUNCTION_CAMERA_MODULE_MALFUNCTION: DeviceMalfunctions.Malfunction
    MALFUNCTION_MAGNETOMETER_ERROR: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_FAILS_CHARGE_FULLY: DeviceMalfunctions.Malfunction
    MALFUNCTION_BATTERY_NOT_INSTALLED: DeviceMalfunctions.Malfunction
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    malfunctions: _containers.RepeatedScalarFieldContainer[DeviceMalfunctions.Malfunction]
    def __init__(self, malfunctions: _Optional[_Iterable[_Union[DeviceMalfunctions.Malfunction, str]]] = ...) -> None: ...
