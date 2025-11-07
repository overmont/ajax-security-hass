from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRoomRequest(_message.Message):
    __slots__ = ("space_locator", "room_name", "image_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    room_name: str
    image_id: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., room_name: _Optional[str] = ..., image_id: _Optional[str] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("room_id",)
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        def __init__(self, room_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_armed", "rooms_limit_exceeded", "hub_offline", "hub_busy", "hub_error", "hub_wrong_state", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        ROOMS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        rooms_limit_exceeded: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., rooms_limit_exceeded: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateRoomResponse.Success
    failure: CreateRoomResponse.Failure
    def __init__(self, success: _Optional[_Union[CreateRoomResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CreateRoomResponse.Failure, _Mapping]] = ...) -> None: ...
