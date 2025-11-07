from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TemperatureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE_STATUS_UNSPECIFIED: _ClassVar[TemperatureStatus]
    TEMPERATURE_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[TemperatureStatus]
    TEMPERATURE_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[TemperatureStatus]
    TEMPERATURE_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[TemperatureStatus]

class HumidityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUMIDITY_STATUS_UNSPECIFIED: _ClassVar[HumidityStatus]
    HUMIDITY_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[HumidityStatus]
    HUMIDITY_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[HumidityStatus]
    HUMIDITY_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[HumidityStatus]

class Co2Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CO2_STATUS_UNSPECIFIED: _ClassVar[Co2Status]
    CO2_STATUS_OUT_OF_LOWER_THRESHOLD: _ClassVar[Co2Status]
    CO2_STATUS_OUT_OF_HIGHER_THRESHOLD: _ClassVar[Co2Status]
    CO2_STATUS_LIGHTLY_POLLUTED: _ClassVar[Co2Status]
    CO2_STATUS_MODERATE_POLLUTED: _ClassVar[Co2Status]
    CO2_STATUS_HEAVY_POLLUTED: _ClassVar[Co2Status]
    CO2_STATUS_OUT_OF_PASSPORT_RANGE: _ClassVar[Co2Status]

class HardwareMalfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARDWARE_MALFUNCTION_UNSPECIFIED: _ClassVar[HardwareMalfunction]
    HARDWARE_MALFUNCTION_TEMPERATURE_AND_HUMIDITY_SENSOR: _ClassVar[HardwareMalfunction]
    HARDWARE_MALFUNCTION_CO2_SENSOR: _ClassVar[HardwareMalfunction]
TEMPERATURE_STATUS_UNSPECIFIED: TemperatureStatus
TEMPERATURE_STATUS_OUT_OF_LOWER_THRESHOLD: TemperatureStatus
TEMPERATURE_STATUS_OUT_OF_HIGHER_THRESHOLD: TemperatureStatus
TEMPERATURE_STATUS_OUT_OF_PASSPORT_RANGE: TemperatureStatus
HUMIDITY_STATUS_UNSPECIFIED: HumidityStatus
HUMIDITY_STATUS_OUT_OF_LOWER_THRESHOLD: HumidityStatus
HUMIDITY_STATUS_OUT_OF_HIGHER_THRESHOLD: HumidityStatus
HUMIDITY_STATUS_OUT_OF_PASSPORT_RANGE: HumidityStatus
CO2_STATUS_UNSPECIFIED: Co2Status
CO2_STATUS_OUT_OF_LOWER_THRESHOLD: Co2Status
CO2_STATUS_OUT_OF_HIGHER_THRESHOLD: Co2Status
CO2_STATUS_LIGHTLY_POLLUTED: Co2Status
CO2_STATUS_MODERATE_POLLUTED: Co2Status
CO2_STATUS_HEAVY_POLLUTED: Co2Status
CO2_STATUS_OUT_OF_PASSPORT_RANGE: Co2Status
HARDWARE_MALFUNCTION_UNSPECIFIED: HardwareMalfunction
HARDWARE_MALFUNCTION_TEMPERATURE_AND_HUMIDITY_SENSOR: HardwareMalfunction
HARDWARE_MALFUNCTION_CO2_SENSOR: HardwareMalfunction
