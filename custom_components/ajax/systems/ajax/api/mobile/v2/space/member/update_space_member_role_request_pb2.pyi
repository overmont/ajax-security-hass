from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMemberRoleRequest(_message.Message):
    __slots__ = ("space_id", "member_id", "role")
    class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_ROLE_UNSPECIFIED: _ClassVar[UpdateMemberRoleRequest.UserRole]
        USER_ROLE_USER: _ClassVar[UpdateMemberRoleRequest.UserRole]
        USER_ROLE_ADMIN: _ClassVar[UpdateMemberRoleRequest.UserRole]
    USER_ROLE_UNSPECIFIED: UpdateMemberRoleRequest.UserRole
    USER_ROLE_USER: UpdateMemberRoleRequest.UserRole
    USER_ROLE_ADMIN: UpdateMemberRoleRequest.UserRole
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    member_id: str
    role: UpdateMemberRoleRequest.UserRole
    def __init__(self, space_id: _Optional[str] = ..., member_id: _Optional[str] = ..., role: _Optional[_Union[UpdateMemberRoleRequest.UserRole, str]] = ...) -> None: ...

class UpdateMemberRoleResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateMemberRoleResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateMemberRoleResponse.Failure, _Mapping]] = ...) -> None: ...
