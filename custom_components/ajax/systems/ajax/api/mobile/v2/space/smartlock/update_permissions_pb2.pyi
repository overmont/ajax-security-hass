from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_permission_pb2 as _smart_lock_permission_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_device_permissions_pb2 as _smart_lock_device_permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockPermissionsRequest(_message.Message):
    __slots__ = ("assignee_space_member_id", "space_id", "smart_lock_id", "updates")
    class Update(_message.Message):
        __slots__ = ("permission", "enabled", "type")
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        permission: _smart_lock_permission_pb2.SmartLockPermission
        enabled: bool
        type: _smart_lock_device_permissions_pb2.SmartLockPermissions.PermissionState.Type
        def __init__(self, permission: _Optional[_Union[_smart_lock_permission_pb2.SmartLockPermission, str]] = ..., enabled: bool = ..., type: _Optional[_Union[_smart_lock_device_permissions_pb2.SmartLockPermissions.PermissionState.Type, _Mapping]] = ...) -> None: ...
    ASSIGNEE_SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    assignee_space_member_id: str
    space_id: str
    smart_lock_id: str
    updates: _containers.RepeatedCompositeFieldContainer[UpdateSmartLockPermissionsRequest.Update]
    def __init__(self, assignee_space_member_id: _Optional[str] = ..., space_id: _Optional[str] = ..., smart_lock_id: _Optional[str] = ..., updates: _Optional[_Iterable[_Union[UpdateSmartLockPermissionsRequest.Update, _Mapping]]] = ...) -> None: ...

class UpdateSmartLockPermissionsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "permission_denied", "space_not_found", "smart_lock_not_found", "space_armed", "member_not_found")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        member_not_found: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., smart_lock_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., member_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSmartLockPermissionsResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateSmartLockPermissionsResponse.Failure, _Mapping]] = ...) -> None: ...
