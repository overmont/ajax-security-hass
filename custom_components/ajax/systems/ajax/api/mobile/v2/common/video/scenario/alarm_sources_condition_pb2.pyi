from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSourcesCondition(_message.Message):
    __slots__ = ("any", "all")
    class AnySource(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AllSources(_message.Message):
        __slots__ = ("max_actuating_time",)
        MAX_ACTUATING_TIME_FIELD_NUMBER: _ClassVar[int]
        max_actuating_time: _duration_pb2.Duration
        def __init__(self, max_actuating_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    ANY_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    any: AlarmSourcesCondition.AnySource
    all: AlarmSourcesCondition.AllSources
    def __init__(self, any: _Optional[_Union[AlarmSourcesCondition.AnySource, _Mapping]] = ..., all: _Optional[_Union[AlarmSourcesCondition.AllSources, _Mapping]] = ...) -> None: ...
