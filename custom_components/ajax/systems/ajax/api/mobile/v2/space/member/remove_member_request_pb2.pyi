from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveSpaceMemberRequest(_message.Message):
    __slots__ = ("space_locator", "space_member_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    space_member_id: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., space_member_id: _Optional[str] = ...) -> None: ...

class RemoveSpaceMemberResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked", "unable_to_delete_last_member", "active_subscription_exist_error")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        UNABLE_TO_DELETE_LAST_MEMBER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_SUBSCRIPTION_EXIST_ERROR_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        unable_to_delete_last_member: _response_pb2.DefaultError
        active_subscription_exist_error: _response_pb2.ActiveSubscriptionExistError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., unable_to_delete_last_member: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., active_subscription_exist_error: _Optional[_Union[_response_pb2.ActiveSubscriptionExistError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RemoveSpaceMemberResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[RemoveSpaceMemberResponse.Failure, _Mapping]] = ...) -> None: ...
