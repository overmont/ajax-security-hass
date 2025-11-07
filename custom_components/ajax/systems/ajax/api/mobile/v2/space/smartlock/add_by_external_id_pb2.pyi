from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddSmartLockByExternalIdRequest(_message.Message):
    __slots__ = ("space_id", "room_id", "external_smart_lock_id", "type", "name", "group_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    room_id: str
    external_smart_lock_id: str
    type: _smart_lock_pb2.SmartLockType
    name: str
    group_id: str
    def __init__(self, space_id: _Optional[str] = ..., room_id: _Optional[str] = ..., external_smart_lock_id: _Optional[str] = ..., type: _Optional[_Union[_smart_lock_pb2.SmartLockType, str]] = ..., name: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class AddSmartLockByExternalIdResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("external_service_access_denied", "bad_request", "smart_lock_not_found", "smart_lock_already_added_by_another_space_member", "permission_denied", "space_not_found", "room_not_found", "space_armed", "smart_lock_offline", "members_limit_exceeded", "group_not_found", "smart_lock_without_group")
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_ALREADY_ADDED_BY_ANOTHER_SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_WITHOUT_GROUP_FIELD_NUMBER: _ClassVar[int]
        external_service_access_denied: _response_pb2.DefaultError
        bad_request: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        smart_lock_already_added_by_another_space_member: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        smart_lock_offline: _response_pb2.DefaultError
        members_limit_exceeded: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        smart_lock_without_group: _response_pb2.DefaultError
        def __init__(self, external_service_access_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_already_added_by_another_space_member: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., room_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., members_limit_exceeded: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., group_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_without_group: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: AddSmartLockByExternalIdResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[AddSmartLockByExternalIdResponse.Failure, _Mapping]] = ...) -> None: ...
