from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_in_space_update_pb2 as _smart_lock_in_space_update_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockRequest(_message.Message):
    __slots__ = ("space_id", "smart_lock_id", "update")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: str
    update: _smart_lock_in_space_update_pb2.SmartLockInSpaceUpdate
    def __init__(self, space_id: _Optional[str] = ..., smart_lock_id: _Optional[str] = ..., update: _Optional[_Union[_smart_lock_in_space_update_pb2.SmartLockInSpaceUpdate, _Mapping]] = ...) -> None: ...

class UpdateSmartLockResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "permission_denied", "space_not_found", "space_armed", "room_not_found", "smart_lock_not_found", "external_service_access_denied", "smart_lock_offline")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        external_service_access_denied: _response_pb2.DefaultError
        smart_lock_offline: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., room_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., external_service_access_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSmartLockResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateSmartLockResponse.Failure, _Mapping]] = ...) -> None: ...
