from systems.ajax.api.mobile.v2.common.space.scenario.trigger import event_pb2 as _event_pb2
from systems.ajax.api.mobile.v2.common.space.scenario.trigger import schedule_pb2 as _schedule_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Trigger(_message.Message):
    __slots__ = ("event", "schedule")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    event: _event_pb2.EventTrigger
    schedule: _schedule_pb2.ScheduleTrigger
    def __init__(self, event: _Optional[_Union[_event_pb2.EventTrigger, _Mapping]] = ..., schedule: _Optional[_Union[_schedule_pb2.ScheduleTrigger, _Mapping]] = ...) -> None: ...
