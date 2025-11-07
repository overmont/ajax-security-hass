from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccelerometerSettings(_message.Message):
    __slots__ = ("accelerometer_types",)
    class AccelerometerTypeSettings(_message.Message):
        __slots__ = ("enabled", "movement", "shock")
        class Movement(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Shock(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOVEMENT_FIELD_NUMBER: _ClassVar[int]
        SHOCK_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        movement: AccelerometerSettings.AccelerometerTypeSettings.Movement
        shock: AccelerometerSettings.AccelerometerTypeSettings.Shock
        def __init__(self, enabled: bool = ..., movement: _Optional[_Union[AccelerometerSettings.AccelerometerTypeSettings.Movement, _Mapping]] = ..., shock: _Optional[_Union[AccelerometerSettings.AccelerometerTypeSettings.Shock, _Mapping]] = ...) -> None: ...
    ACCELEROMETER_TYPES_FIELD_NUMBER: _ClassVar[int]
    accelerometer_types: _containers.RepeatedCompositeFieldContainer[AccelerometerSettings.AccelerometerTypeSettings]
    def __init__(self, accelerometer_types: _Optional[_Iterable[_Union[AccelerometerSettings.AccelerometerTypeSettings, _Mapping]]] = ...) -> None: ...
