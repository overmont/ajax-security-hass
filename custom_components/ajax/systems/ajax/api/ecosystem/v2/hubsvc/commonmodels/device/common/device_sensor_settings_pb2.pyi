from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import sensitivity_pb2 as _sensitivity_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReedSensorSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class ExtraContactSensorSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class MotionSensorSettings(_message.Message):
    __slots__ = ("sensitivity",)
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    sensitivity: _sensitivity_pb2.Sensitivity
    def __init__(self, sensitivity: _Optional[_Union[_sensitivity_pb2.Sensitivity, str]] = ...) -> None: ...

class FastTamperSettings(_message.Message):
    __slots__ = ("fast_tamper",)
    class FastTamper(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAST_TAMPER_UNSPECIFIED: _ClassVar[FastTamperSettings.FastTamper]
        FAST_TAMPER_DISABLED: _ClassVar[FastTamperSettings.FastTamper]
        FAST_TAMPER_ENABLED: _ClassVar[FastTamperSettings.FastTamper]
    FAST_TAMPER_UNSPECIFIED: FastTamperSettings.FastTamper
    FAST_TAMPER_DISABLED: FastTamperSettings.FastTamper
    FAST_TAMPER_ENABLED: FastTamperSettings.FastTamper
    FAST_TAMPER_FIELD_NUMBER: _ClassVar[int]
    fast_tamper: FastTamperSettings.FastTamper
    def __init__(self, fast_tamper: _Optional[_Union[FastTamperSettings.FastTamper, str]] = ...) -> None: ...
