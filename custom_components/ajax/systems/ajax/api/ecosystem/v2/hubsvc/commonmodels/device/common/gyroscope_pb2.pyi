from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gyroscope(_message.Message):
    __slots__ = ("capabilities", "accelerometer_sensitivity", "alert_if_moved", "accelerometer_sensitivity_capabilities", "magnetometer_sensitivity", "magnetometer_sensitivity_capabilities")
    class AlertIfMoved(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALERT_IF_MOVED_UNSPECIFIED: _ClassVar[Gyroscope.AlertIfMoved]
        ALERT_IF_MOVED_ENABLED: _ClassVar[Gyroscope.AlertIfMoved]
        ALERT_IF_MOVED_DISABLED: _ClassVar[Gyroscope.AlertIfMoved]
    ALERT_IF_MOVED_UNSPECIFIED: Gyroscope.AlertIfMoved
    ALERT_IF_MOVED_ENABLED: Gyroscope.AlertIfMoved
    ALERT_IF_MOVED_DISABLED: Gyroscope.AlertIfMoved
    class AccelSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCEL_SENSITIVITY_UNSPECIFIED: _ClassVar[Gyroscope.AccelSensitivity]
        ACCEL_SENSITIVITY_LOW: _ClassVar[Gyroscope.AccelSensitivity]
        ACCEL_SENSITIVITY_NORMAL: _ClassVar[Gyroscope.AccelSensitivity]
        ACCEL_SENSITIVITY_HIGH: _ClassVar[Gyroscope.AccelSensitivity]
    ACCEL_SENSITIVITY_UNSPECIFIED: Gyroscope.AccelSensitivity
    ACCEL_SENSITIVITY_LOW: Gyroscope.AccelSensitivity
    ACCEL_SENSITIVITY_NORMAL: Gyroscope.AccelSensitivity
    ACCEL_SENSITIVITY_HIGH: Gyroscope.AccelSensitivity
    class MagnetometerSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MAGNETOMETER_SENSITIVITY_UNSPECIFIED: _ClassVar[Gyroscope.MagnetometerSensitivity]
        MAGNETOMETER_SENSITIVITY_LOW: _ClassVar[Gyroscope.MagnetometerSensitivity]
        MAGNETOMETER_SENSITIVITY_NORMAL: _ClassVar[Gyroscope.MagnetometerSensitivity]
    MAGNETOMETER_SENSITIVITY_UNSPECIFIED: Gyroscope.MagnetometerSensitivity
    MAGNETOMETER_SENSITIVITY_LOW: Gyroscope.MagnetometerSensitivity
    MAGNETOMETER_SENSITIVITY_NORMAL: Gyroscope.MagnetometerSensitivity
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[Gyroscope.Capability]
        CAPABILITY_ACCELEROMETER_SENSITIVITY: _ClassVar[Gyroscope.Capability]
        CAPABILITY_MAGNETIC_SENSOR_SENSITIVITY: _ClassVar[Gyroscope.Capability]
    CAPABILITY_UNSPECIFIED: Gyroscope.Capability
    CAPABILITY_ACCELEROMETER_SENSITIVITY: Gyroscope.Capability
    CAPABILITY_MAGNETIC_SENSOR_SENSITIVITY: Gyroscope.Capability
    class GyroscopeSensorSettings(_message.Message):
        __slots__ = ("alert_if_moved", "accelerometer_sensitivity", "magnetometer_sensitivity")
        ALERT_IF_MOVED_FIELD_NUMBER: _ClassVar[int]
        ACCELEROMETER_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        MAGNETOMETER_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        alert_if_moved: Gyroscope.AlertIfMoved
        accelerometer_sensitivity: Gyroscope.AccelSensitivity
        magnetometer_sensitivity: Gyroscope.MagnetometerSensitivity
        def __init__(self, alert_if_moved: _Optional[_Union[Gyroscope.AlertIfMoved, str]] = ..., accelerometer_sensitivity: _Optional[_Union[Gyroscope.AccelSensitivity, str]] = ..., magnetometer_sensitivity: _Optional[_Union[Gyroscope.MagnetometerSensitivity, str]] = ...) -> None: ...
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALERT_IF_MOVED_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_SENSITIVITY_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    MAGNETOMETER_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    MAGNETOMETER_SENSITIVITY_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedScalarFieldContainer[Gyroscope.Capability]
    accelerometer_sensitivity: Gyroscope.AccelSensitivity
    alert_if_moved: Gyroscope.AlertIfMoved
    accelerometer_sensitivity_capabilities: _containers.RepeatedScalarFieldContainer[Gyroscope.AccelSensitivity]
    magnetometer_sensitivity: Gyroscope.MagnetometerSensitivity
    magnetometer_sensitivity_capabilities: _containers.RepeatedScalarFieldContainer[Gyroscope.MagnetometerSensitivity]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[Gyroscope.Capability, str]]] = ..., accelerometer_sensitivity: _Optional[_Union[Gyroscope.AccelSensitivity, str]] = ..., alert_if_moved: _Optional[_Union[Gyroscope.AlertIfMoved, str]] = ..., accelerometer_sensitivity_capabilities: _Optional[_Iterable[_Union[Gyroscope.AccelSensitivity, str]]] = ..., magnetometer_sensitivity: _Optional[_Union[Gyroscope.MagnetometerSensitivity, str]] = ..., magnetometer_sensitivity_capabilities: _Optional[_Iterable[_Union[Gyroscope.MagnetometerSensitivity, str]]] = ...) -> None: ...
