from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InviteSpaceMembersRequest(_message.Message):
    __slots__ = ("space_id", "emails")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    emails: _containers.RepeatedCompositeFieldContainer[SpaceMemberEmail]
    def __init__(self, space_id: _Optional[str] = ..., emails: _Optional[_Iterable[_Union[SpaceMemberEmail, _Mapping]]] = ...) -> None: ...

class InviteSpaceMembersResponse(_message.Message):
    __slots__ = ("result",)
    class InviteResult(_message.Message):
        __slots__ = ("email", "success", "failure")
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        email: SpaceMemberEmail
        success: _response_pb2.Success
        failure: InviteSpaceMembersResponse.Failure
        def __init__(self, email: _Optional[_Union[SpaceMemberEmail, _Mapping]] = ..., success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[InviteSpaceMembersResponse.Failure, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "too_many_users", "already_exist", "pro_not_found", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        TOO_MANY_USERS_FIELD_NUMBER: _ClassVar[int]
        ALREADY_EXIST_FIELD_NUMBER: _ClassVar[int]
        PRO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        too_many_users: _response_pb2.DefaultError
        already_exist: _response_pb2.DefaultError
        pro_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., too_many_users: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., already_exist: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., pro_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[InviteSpaceMembersResponse.InviteResult]
    def __init__(self, result: _Optional[_Iterable[_Union[InviteSpaceMembersResponse.InviteResult, _Mapping]]] = ...) -> None: ...

class SpaceMemberEmail(_message.Message):
    __slots__ = ("pro_email", "user_email")
    PRO_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    pro_email: str
    user_email: str
    def __init__(self, pro_email: _Optional[str] = ..., user_email: _Optional[str] = ...) -> None: ...
