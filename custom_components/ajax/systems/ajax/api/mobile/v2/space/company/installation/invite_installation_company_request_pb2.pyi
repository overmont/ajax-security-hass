from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InviteInstallationCompanyRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    def __init__(self, company_hex_id: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...

class InviteInstallationCompanyResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "hub_locked", "users_limit_exceed", "space_already_on_installation", "space_locked", "space_armed")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_FIELD_NUMBER: _ClassVar[int]
        USERS_LIMIT_EXCEED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ALREADY_ON_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        hub_locked: _response_pb2.DefaultError
        users_limit_exceed: _response_pb2.DefaultError
        space_already_on_installation: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        space_armed: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_locked: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., users_limit_exceed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_already_on_installation: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InviteInstallationCompanyResponse.Success
    failure: InviteInstallationCompanyResponse.Failure
    def __init__(self, success: _Optional[_Union[InviteInstallationCompanyResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[InviteInstallationCompanyResponse.Failure, _Mapping]] = ...) -> None: ...
