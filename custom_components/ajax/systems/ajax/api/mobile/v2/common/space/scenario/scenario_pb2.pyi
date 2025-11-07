from systems.ajax.api.mobile.v2.common.space.scenario.trigger import trigger_pb2 as _trigger_pb2
from systems.ajax.api.mobile.v2.common.space.scenario.action import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scenario(_message.Message):
    __slots__ = ("id", "name", "enabled", "cases")
    class Case(_message.Message):
        __slots__ = ("trigger", "action")
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        trigger: _trigger_pb2.Trigger
        action: _action_pb2.Action
        def __init__(self, trigger: _Optional[_Union[_trigger_pb2.Trigger, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    enabled: bool
    cases: _containers.RepeatedCompositeFieldContainer[Scenario.Case]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enabled: bool = ..., cases: _Optional[_Iterable[_Union[Scenario.Case, _Mapping]]] = ...) -> None: ...
