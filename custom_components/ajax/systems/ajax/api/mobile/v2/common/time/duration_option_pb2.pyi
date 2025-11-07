from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DurationOption(_message.Message):
    __slots__ = ("time_unit", "amount_in_time_unit", "amount_in_seconds")
    class TimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_UNIT_UNSPECIFIED: _ClassVar[DurationOption.TimeUnit]
        TIME_UNIT_SECONDS: _ClassVar[DurationOption.TimeUnit]
        TIME_UNIT_MINUTES: _ClassVar[DurationOption.TimeUnit]
        TIME_UNIT_HOURS: _ClassVar[DurationOption.TimeUnit]
    TIME_UNIT_UNSPECIFIED: DurationOption.TimeUnit
    TIME_UNIT_SECONDS: DurationOption.TimeUnit
    TIME_UNIT_MINUTES: DurationOption.TimeUnit
    TIME_UNIT_HOURS: DurationOption.TimeUnit
    TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_IN_TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    time_unit: DurationOption.TimeUnit
    amount_in_time_unit: int
    amount_in_seconds: int
    def __init__(self, time_unit: _Optional[_Union[DurationOption.TimeUnit, str]] = ..., amount_in_time_unit: _Optional[int] = ..., amount_in_seconds: _Optional[int] = ...) -> None: ...
