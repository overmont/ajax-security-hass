from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.scenario import video_scenario_pb2 as _video_scenario_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetEnabledScenarioRequest(_message.Message):
    __slots__ = ("scenario_id", "enabled", "space_locator")
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    scenario_id: str
    enabled: bool
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, scenario_id: _Optional[str] = ..., enabled: bool = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class SetEnabledScenarioResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("scenario",)
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        scenario: _video_scenario_pb2.VideoScenario
        def __init__(self, scenario: _Optional[_Union[_video_scenario_pb2.VideoScenario, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "space_armed", "scenario_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        scenario_not_found: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., scenario_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetEnabledScenarioResponse.Success
    failure: SetEnabledScenarioResponse.Failure
    def __init__(self, success: _Optional[_Union[SetEnabledScenarioResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SetEnabledScenarioResponse.Failure, _Mapping]] = ...) -> None: ...
