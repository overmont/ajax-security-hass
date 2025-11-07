from systems.ajax.api.mobile.v2.common.context import company_pb2 as _company_pb2
from systems.ajax.api.mobile.v2.common.context import personal_pb2 as _personal_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RejectRequestedFullPermissionsRequest(_message.Message):
    __slots__ = ("space_locator", "request_id", "personal_context", "company_context")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    request_id: str
    personal_context: _personal_pb2.PersonalContext
    company_context: _company_pb2.CompanyContext
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., request_id: _Optional[str] = ..., personal_context: _Optional[_Union[_personal_pb2.PersonalContext, _Mapping]] = ..., company_context: _Optional[_Union[_company_pb2.CompanyContext, _Mapping]] = ...) -> None: ...

class RejectRequestedFullPermissionsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "request_expired")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        REQUEST_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        request_expired: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., request_expired: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RejectRequestedFullPermissionsResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[RejectRequestedFullPermissionsResponse.Failure, _Mapping]] = ...) -> None: ...
