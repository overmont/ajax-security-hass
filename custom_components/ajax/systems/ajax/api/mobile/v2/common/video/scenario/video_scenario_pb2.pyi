from systems.ajax.api.mobile.v2.common.video.scenario import alarm_source_pb2 as _alarm_source_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import alarm_sources_condition_pb2 as _alarm_sources_condition_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import target_video_edge_pb2 as _target_video_edge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenario(_message.Message):
    __slots__ = ("id", "enabled", "name", "alarm_sources", "alarm_sources_condition", "targets", "monitoring_state")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    enabled: bool
    name: str
    alarm_sources: _containers.RepeatedCompositeFieldContainer[_alarm_source_pb2.AlarmSource]
    alarm_sources_condition: _alarm_sources_condition_pb2.AlarmSourcesCondition
    targets: _containers.RepeatedCompositeFieldContainer[_target_video_edge_pb2.TargetVideoEdge]
    monitoring_state: _target_video_edge_pb2.MonitoringState
    def __init__(self, id: _Optional[str] = ..., enabled: bool = ..., name: _Optional[str] = ..., alarm_sources: _Optional[_Iterable[_Union[_alarm_source_pb2.AlarmSource, _Mapping]]] = ..., alarm_sources_condition: _Optional[_Union[_alarm_sources_condition_pb2.AlarmSourcesCondition, _Mapping]] = ..., targets: _Optional[_Iterable[_Union[_target_video_edge_pb2.TargetVideoEdge, _Mapping]]] = ..., monitoring_state: _Optional[_Union[_target_video_edge_pb2.MonitoringState, str]] = ...) -> None: ...
