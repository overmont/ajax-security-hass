from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import alarm_source_pb2 as _alarm_source_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import alarm_sources_condition_pb2 as _alarm_sources_condition_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import target_video_edge_pb2 as _target_video_edge_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import video_scenario_pb2 as _video_scenario_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateScenarioRequest(_message.Message):
    __slots__ = ("scenario_id", "name", "alarm_sources", "alarm_sources_condition", "targets", "monitoring_state", "space_locator")
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    scenario_id: str
    name: str
    alarm_sources: _containers.RepeatedCompositeFieldContainer[_alarm_source_pb2.AlarmSource]
    alarm_sources_condition: _alarm_sources_condition_pb2.AlarmSourcesCondition
    targets: _containers.RepeatedCompositeFieldContainer[_target_video_edge_pb2.TargetVideoEdge]
    monitoring_state: _target_video_edge_pb2.MonitoringState
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, scenario_id: _Optional[str] = ..., name: _Optional[str] = ..., alarm_sources: _Optional[_Iterable[_Union[_alarm_source_pb2.AlarmSource, _Mapping]]] = ..., alarm_sources_condition: _Optional[_Union[_alarm_sources_condition_pb2.AlarmSourcesCondition, _Mapping]] = ..., targets: _Optional[_Iterable[_Union[_target_video_edge_pb2.TargetVideoEdge, _Mapping]]] = ..., monitoring_state: _Optional[_Union[_target_video_edge_pb2.MonitoringState, str]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class UpdateScenarioResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("scenario",)
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        scenario: _video_scenario_pb2.VideoScenario
        def __init__(self, scenario: _Optional[_Union[_video_scenario_pb2.VideoScenario, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "space_armed", "scenario_not_found", "empty_source_list", "hub_not_found", "source_not_found", "target_channel_list_is_empty", "target_video_edge_not_found", "target_channel_not_found", "invalid_channel_state", "duplicated_name", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SOURCE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TARGET_CHANNEL_LIST_IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TARGET_CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        INVALID_CHANNEL_STATE_FIELD_NUMBER: _ClassVar[int]
        DUPLICATED_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        scenario_not_found: _response_pb2.DefaultError
        empty_source_list: _response_pb2.DefaultError
        hub_not_found: _response_pb2.DefaultError
        source_not_found: _response_pb2.DefaultError
        target_channel_list_is_empty: _response_pb2.DefaultError
        target_video_edge_not_found: _response_pb2.DefaultError
        target_channel_not_found: _response_pb2.DefaultError
        invalid_channel_state: _response_pb2.DefaultError
        duplicated_name: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., scenario_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., empty_source_list: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., source_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_channel_list_is_empty: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_channel_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., invalid_channel_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., duplicated_name: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UpdateScenarioResponse.Success
    failure: UpdateScenarioResponse.Failure
    def __init__(self, success: _Optional[_Union[UpdateScenarioResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateScenarioResponse.Failure, _Mapping]] = ...) -> None: ...
