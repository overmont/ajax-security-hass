from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestFullPermissionsRequest(_message.Message):
    __slots__ = ("space_locator", "permanent_permissions", "temporary_permissions")
    class PermanentPermissions(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TemporaryPermissions(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    permanent_permissions: RequestFullPermissionsRequest.PermanentPermissions
    temporary_permissions: RequestFullPermissionsRequest.TemporaryPermissions
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., permanent_permissions: _Optional[_Union[RequestFullPermissionsRequest.PermanentPermissions, _Mapping]] = ..., temporary_permissions: _Optional[_Union[RequestFullPermissionsRequest.TemporaryPermissions, _Mapping]] = ...) -> None: ...

class RequestFullPermissionsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RequestFullPermissionsResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[RequestFullPermissionsResponse.Failure, _Mapping]] = ...) -> None: ...
