from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SelfTestStatus(_message.Message):
    __slots__ = ("defected_sensors",)
    class DefectedSensor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFECTED_SENSOR_UNSPECIFIED: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_ACCELEROMETER: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_MAGNETOMETER: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_REED: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_PIR: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_MICROWAVE: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_MASKING: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_SEISMIC: _ClassVar[SelfTestStatus.DefectedSensor]
        DEFECTED_SENSOR_BATTERY: _ClassVar[SelfTestStatus.DefectedSensor]
    DEFECTED_SENSOR_UNSPECIFIED: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_ACCELEROMETER: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_MAGNETOMETER: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_REED: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_PIR: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_MICROWAVE: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_MASKING: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_SEISMIC: SelfTestStatus.DefectedSensor
    DEFECTED_SENSOR_BATTERY: SelfTestStatus.DefectedSensor
    DEFECTED_SENSORS_FIELD_NUMBER: _ClassVar[int]
    defected_sensors: _containers.RepeatedScalarFieldContainer[SelfTestStatus.DefectedSensor]
    def __init__(self, defected_sensors: _Optional[_Iterable[_Union[SelfTestStatus.DefectedSensor, str]]] = ...) -> None: ...
