from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chime(_message.Message):
    __slots__ = ("off", "mechanical", "digital", "siren")
    class OffMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MechanicalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class DigitalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class SirenMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    OFF_FIELD_NUMBER: _ClassVar[int]
    MECHANICAL_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_FIELD_NUMBER: _ClassVar[int]
    SIREN_FIELD_NUMBER: _ClassVar[int]
    off: Chime.OffMode
    mechanical: Chime.MechanicalMode
    digital: Chime.DigitalMode
    siren: Chime.SirenMode
    def __init__(self, off: _Optional[_Union[Chime.OffMode, _Mapping]] = ..., mechanical: _Optional[_Union[Chime.MechanicalMode, _Mapping]] = ..., digital: _Optional[_Union[Chime.DigitalMode, _Mapping]] = ..., siren: _Optional[_Union[Chime.SirenMode, _Mapping]] = ...) -> None: ...
