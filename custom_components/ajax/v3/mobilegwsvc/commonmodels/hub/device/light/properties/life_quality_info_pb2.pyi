from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeQualityInfo(_message.Message):
    __slots__ = ("actual_temperature", "actual_humidity", "actual_co2", "hardware_malfunctions", "temperature_statuses", "humidity_statuses", "co2_statuses")
    class HardwareMalfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARDWARE_MALFUNCTION_UNSPECIFIED: _ClassVar[LifeQualityInfo.HardwareMalfunction]
        HARDWARE_MALFUNCTION_TEMPERATURE_SENSOR: _ClassVar[LifeQualityInfo.HardwareMalfunction]
        HARDWARE_MALFUNCTION_HUMIDITY_SENSOR: _ClassVar[LifeQualityInfo.HardwareMalfunction]
        HARDWARE_MALFUNCTION_CO2_SENSOR: _ClassVar[LifeQualityInfo.HardwareMalfunction]
    HARDWARE_MALFUNCTION_UNSPECIFIED: LifeQualityInfo.HardwareMalfunction
    HARDWARE_MALFUNCTION_TEMPERATURE_SENSOR: LifeQualityInfo.HardwareMalfunction
    HARDWARE_MALFUNCTION_HUMIDITY_SENSOR: LifeQualityInfo.HardwareMalfunction
    HARDWARE_MALFUNCTION_CO2_SENSOR: LifeQualityInfo.HardwareMalfunction
    class TemperatureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEMPERATURE_STATUS_UNSPECIFIED: _ClassVar[LifeQualityInfo.TemperatureStatus]
        TEMPERATURE_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[LifeQualityInfo.TemperatureStatus]
        TEMPERATURE_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[LifeQualityInfo.TemperatureStatus]
        TEMPERATURE_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[LifeQualityInfo.TemperatureStatus]
    TEMPERATURE_STATUS_UNSPECIFIED: LifeQualityInfo.TemperatureStatus
    TEMPERATURE_STATUS_OUT_OF_LOWER_THRESHOLD: LifeQualityInfo.TemperatureStatus
    TEMPERATURE_STATUS_OUT_OF_HIGHER_THRESHOLD: LifeQualityInfo.TemperatureStatus
    TEMPERATURE_STATUS_OUT_OF_PASSPORT_RANGE: LifeQualityInfo.TemperatureStatus
    class HumidityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HUMIDITY_STATUS_UNSPECIFIED: _ClassVar[LifeQualityInfo.HumidityStatus]
        HUMIDITY_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[LifeQualityInfo.HumidityStatus]
        HUMIDITY_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[LifeQualityInfo.HumidityStatus]
        HUMIDITY_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[LifeQualityInfo.HumidityStatus]
    HUMIDITY_STATUS_UNSPECIFIED: LifeQualityInfo.HumidityStatus
    HUMIDITY_STATUS_OUT_OF_LOWER_THRESHOLD: LifeQualityInfo.HumidityStatus
    HUMIDITY_STATUS_OUT_OF_HIGHER_THRESHOLD: LifeQualityInfo.HumidityStatus
    HUMIDITY_STATUS_OUT_OF_PASSPORT_RANGE: LifeQualityInfo.HumidityStatus
    class Co2Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CO2_STATUS_UNSPECIFIED: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_LIGHTLY_POLLUTED: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_MODERATE_POLLUTED: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_HEAVY_POLLUTED: _ClassVar[LifeQualityInfo.Co2Status]
        CO2_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[LifeQualityInfo.Co2Status]
    CO2_STATUS_UNSPECIFIED: LifeQualityInfo.Co2Status
    CO2_STATUS_OUT_OF_LOWER_THRESHOLD: LifeQualityInfo.Co2Status
    CO2_STATUS_OUT_OF_HIGHER_THRESHOLD: LifeQualityInfo.Co2Status
    CO2_STATUS_LIGHTLY_POLLUTED: LifeQualityInfo.Co2Status
    CO2_STATUS_MODERATE_POLLUTED: LifeQualityInfo.Co2Status
    CO2_STATUS_HEAVY_POLLUTED: LifeQualityInfo.Co2Status
    CO2_STATUS_OUT_OF_PASSPORT_RANGE: LifeQualityInfo.Co2Status
    ACTUAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_CO2_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_STATUSES_FIELD_NUMBER: _ClassVar[int]
    CO2_STATUSES_FIELD_NUMBER: _ClassVar[int]
    actual_temperature: float
    actual_humidity: float
    actual_co2: int
    hardware_malfunctions: _containers.RepeatedScalarFieldContainer[LifeQualityInfo.HardwareMalfunction]
    temperature_statuses: _containers.RepeatedScalarFieldContainer[LifeQualityInfo.TemperatureStatus]
    humidity_statuses: _containers.RepeatedScalarFieldContainer[LifeQualityInfo.HumidityStatus]
    co2_statuses: _containers.RepeatedScalarFieldContainer[LifeQualityInfo.Co2Status]
    def __init__(self, actual_temperature: _Optional[float] = ..., actual_humidity: _Optional[float] = ..., actual_co2: _Optional[int] = ..., hardware_malfunctions: _Optional[_Iterable[_Union[LifeQualityInfo.HardwareMalfunction, str]]] = ..., temperature_statuses: _Optional[_Iterable[_Union[LifeQualityInfo.TemperatureStatus, str]]] = ..., humidity_statuses: _Optional[_Iterable[_Union[LifeQualityInfo.HumidityStatus, str]]] = ..., co2_statuses: _Optional[_Iterable[_Union[LifeQualityInfo.Co2Status, str]]] = ...) -> None: ...
