from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WalkTestSensor(_message.Message):
    __slots__ = ("magnetic_contact", "external_contact", "motion_sensor", "motion_sensor_right", "motion_sensor_left", "smoke_sensor", "gas_sensor", "co_sensor", "panic_button", "glass_break_sensor", "masking_sensor", "temperature_sensor", "seismic_sensor", "shock_sensor", "tilt_sensor", "tamper_sensor", "intrusion_sensor", "fire_sensor", "medical_alarm", "malfunction", "leak_sensor", "custom_event", "duress_code", "roller_shutter_sensor", "masking_sensor_right", "masking_sensor_left")
    class MagneticContact(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ExternalContact(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MotionSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MotionSensorRight(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MotionSensorLeft(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MaskingSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MaskingSensorRight(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MaskingSensorLeft(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SmokeSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CoSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SeismicSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PanicButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GlassBreakSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TemperatureSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ShockSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TiltSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TamperSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class IntrusionSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class FireSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GasSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MedicalAlarm(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Malfunction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class LeakSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CustomEvent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DuressCode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RollerShutterSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MAGNETIC_CONTACT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_LEFT_FIELD_NUMBER: _ClassVar[int]
    SMOKE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    GAS_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CO_SENSOR_FIELD_NUMBER: _ClassVar[int]
    PANIC_BUTTON_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SHOCK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TILT_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TAMPER_SENSOR_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    FIRE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    LEAK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EVENT_FIELD_NUMBER: _ClassVar[int]
    DURESS_CODE_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_LEFT_FIELD_NUMBER: _ClassVar[int]
    magnetic_contact: WalkTestSensor.MagneticContact
    external_contact: WalkTestSensor.ExternalContact
    motion_sensor: WalkTestSensor.MotionSensor
    motion_sensor_right: WalkTestSensor.MotionSensorRight
    motion_sensor_left: WalkTestSensor.MotionSensorLeft
    smoke_sensor: WalkTestSensor.SmokeSensor
    gas_sensor: WalkTestSensor.GasSensor
    co_sensor: WalkTestSensor.CoSensor
    panic_button: WalkTestSensor.PanicButton
    glass_break_sensor: WalkTestSensor.GlassBreakSensor
    masking_sensor: WalkTestSensor.MaskingSensor
    temperature_sensor: WalkTestSensor.TemperatureSensor
    seismic_sensor: WalkTestSensor.SeismicSensor
    shock_sensor: WalkTestSensor.ShockSensor
    tilt_sensor: WalkTestSensor.TiltSensor
    tamper_sensor: WalkTestSensor.TamperSensor
    intrusion_sensor: WalkTestSensor.IntrusionSensor
    fire_sensor: WalkTestSensor.FireSensor
    medical_alarm: WalkTestSensor.MedicalAlarm
    malfunction: WalkTestSensor.Malfunction
    leak_sensor: WalkTestSensor.LeakSensor
    custom_event: WalkTestSensor.CustomEvent
    duress_code: WalkTestSensor.DuressCode
    roller_shutter_sensor: WalkTestSensor.RollerShutterSensor
    masking_sensor_right: WalkTestSensor.MaskingSensorRight
    masking_sensor_left: WalkTestSensor.MaskingSensorLeft
    def __init__(self, magnetic_contact: _Optional[_Union[WalkTestSensor.MagneticContact, _Mapping]] = ..., external_contact: _Optional[_Union[WalkTestSensor.ExternalContact, _Mapping]] = ..., motion_sensor: _Optional[_Union[WalkTestSensor.MotionSensor, _Mapping]] = ..., motion_sensor_right: _Optional[_Union[WalkTestSensor.MotionSensorRight, _Mapping]] = ..., motion_sensor_left: _Optional[_Union[WalkTestSensor.MotionSensorLeft, _Mapping]] = ..., smoke_sensor: _Optional[_Union[WalkTestSensor.SmokeSensor, _Mapping]] = ..., gas_sensor: _Optional[_Union[WalkTestSensor.GasSensor, _Mapping]] = ..., co_sensor: _Optional[_Union[WalkTestSensor.CoSensor, _Mapping]] = ..., panic_button: _Optional[_Union[WalkTestSensor.PanicButton, _Mapping]] = ..., glass_break_sensor: _Optional[_Union[WalkTestSensor.GlassBreakSensor, _Mapping]] = ..., masking_sensor: _Optional[_Union[WalkTestSensor.MaskingSensor, _Mapping]] = ..., temperature_sensor: _Optional[_Union[WalkTestSensor.TemperatureSensor, _Mapping]] = ..., seismic_sensor: _Optional[_Union[WalkTestSensor.SeismicSensor, _Mapping]] = ..., shock_sensor: _Optional[_Union[WalkTestSensor.ShockSensor, _Mapping]] = ..., tilt_sensor: _Optional[_Union[WalkTestSensor.TiltSensor, _Mapping]] = ..., tamper_sensor: _Optional[_Union[WalkTestSensor.TamperSensor, _Mapping]] = ..., intrusion_sensor: _Optional[_Union[WalkTestSensor.IntrusionSensor, _Mapping]] = ..., fire_sensor: _Optional[_Union[WalkTestSensor.FireSensor, _Mapping]] = ..., medical_alarm: _Optional[_Union[WalkTestSensor.MedicalAlarm, _Mapping]] = ..., malfunction: _Optional[_Union[WalkTestSensor.Malfunction, _Mapping]] = ..., leak_sensor: _Optional[_Union[WalkTestSensor.LeakSensor, _Mapping]] = ..., custom_event: _Optional[_Union[WalkTestSensor.CustomEvent, _Mapping]] = ..., duress_code: _Optional[_Union[WalkTestSensor.DuressCode, _Mapping]] = ..., roller_shutter_sensor: _Optional[_Union[WalkTestSensor.RollerShutterSensor, _Mapping]] = ..., masking_sensor_right: _Optional[_Union[WalkTestSensor.MaskingSensorRight, _Mapping]] = ..., masking_sensor_left: _Optional[_Union[WalkTestSensor.MaskingSensorLeft, _Mapping]] = ...) -> None: ...
