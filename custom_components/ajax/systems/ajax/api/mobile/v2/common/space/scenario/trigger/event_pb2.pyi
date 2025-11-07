from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.smartlock import qualifier_pb2 as _qualifier_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.space import qualifier_pb2 as _qualifier_pb2_1
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.video import qualifier_pb2 as _qualifier_pb2_1_1
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import qualifier_pb2 as _qualifier_pb2_1_1_1
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventTrigger(_message.Message):
    __slots__ = ("sources", "condition")
    class EventSource(_message.Message):
        __slots__ = ("space", "hub_device", "video_edge", "smart_lock")
        class Space(_message.Message):
            __slots__ = ("events",)
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            events: _containers.RepeatedCompositeFieldContainer[_qualifier_pb2_1.SpaceEventQualifier]
            def __init__(self, events: _Optional[_Iterable[_Union[_qualifier_pb2_1.SpaceEventQualifier, _Mapping]]] = ...) -> None: ...
        class HubDevice(_message.Message):
            __slots__ = ("id", "hub_id", "events")
            ID_FIELD_NUMBER: _ClassVar[int]
            HUB_ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            id: str
            hub_id: str
            events: _containers.RepeatedCompositeFieldContainer[_qualifier_pb2_1_1_1.HubEventQualifier]
            def __init__(self, id: _Optional[str] = ..., hub_id: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_qualifier_pb2_1_1_1.HubEventQualifier, _Mapping]]] = ...) -> None: ...
        class VideoEdge(_message.Message):
            __slots__ = ("id", "events", "channel_id")
            ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            events: _containers.RepeatedCompositeFieldContainer[_qualifier_pb2_1_1.VideoEventQualifier]
            channel_id: str
            def __init__(self, id: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_qualifier_pb2_1_1.VideoEventQualifier, _Mapping]]] = ..., channel_id: _Optional[str] = ...) -> None: ...
        class SmartLock(_message.Message):
            __slots__ = ("id", "events")
            ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            id: str
            events: _containers.RepeatedCompositeFieldContainer[_qualifier_pb2.SmartLockEventQualifier]
            def __init__(self, id: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_qualifier_pb2.SmartLockEventQualifier, _Mapping]]] = ...) -> None: ...
        SPACE_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
        space: EventTrigger.EventSource.Space
        hub_device: EventTrigger.EventSource.HubDevice
        video_edge: EventTrigger.EventSource.VideoEdge
        smart_lock: EventTrigger.EventSource.SmartLock
        def __init__(self, space: _Optional[_Union[EventTrigger.EventSource.Space, _Mapping]] = ..., hub_device: _Optional[_Union[EventTrigger.EventSource.HubDevice, _Mapping]] = ..., video_edge: _Optional[_Union[EventTrigger.EventSource.VideoEdge, _Mapping]] = ..., smart_lock: _Optional[_Union[EventTrigger.EventSource.SmartLock, _Mapping]] = ...) -> None: ...
    class EventCondition(_message.Message):
        __slots__ = ("any", "all")
        class Any(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class All(_message.Message):
            __slots__ = ("max_actuating_time",)
            MAX_ACTUATING_TIME_FIELD_NUMBER: _ClassVar[int]
            max_actuating_time: _duration_pb2.Duration
            def __init__(self, max_actuating_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        ANY_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        any: EventTrigger.EventCondition.Any
        all: EventTrigger.EventCondition.All
        def __init__(self, any: _Optional[_Union[EventTrigger.EventCondition.Any, _Mapping]] = ..., all: _Optional[_Union[EventTrigger.EventCondition.All, _Mapping]] = ...) -> None: ...
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[EventTrigger.EventSource]
    condition: EventTrigger.EventCondition
    def __init__(self, sources: _Optional[_Iterable[_Union[EventTrigger.EventSource, _Mapping]]] = ..., condition: _Optional[_Union[EventTrigger.EventCondition, _Mapping]] = ...) -> None: ...
