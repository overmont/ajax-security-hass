from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteScenarioRequest(_message.Message):
    __slots__ = ("space_id", "scenario_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    scenario_id: str
    def __init__(self, space_id: _Optional[str] = ..., scenario_id: _Optional[str] = ...) -> None: ...

class DeleteScenarioResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_armed", "space_locked", "scenario_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        scenario_not_found: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., scenario_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeleteScenarioResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[DeleteScenarioResponse.Failure, _Mapping]] = ...) -> None: ...
