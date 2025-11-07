from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetSecurityModeRequest(_message.Message):
    __slots__ = ("space_locator", "mode")
    class SecurityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SetSecurityModeRequest.SecurityMode]
        REGULAR: _ClassVar[SetSecurityModeRequest.SecurityMode]
        GROUP: _ClassVar[SetSecurityModeRequest.SecurityMode]
    NONE: SetSecurityModeRequest.SecurityMode
    REGULAR: SetSecurityModeRequest.SecurityMode
    GROUP: SetSecurityModeRequest.SecurityMode
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    mode: SetSecurityModeRequest.SecurityMode
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., mode: _Optional[_Union[SetSecurityModeRequest.SecurityMode, str]] = ...) -> None: ...

class SetSecurityModeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_armed", "space_without_groups", "permission_denied", "some_devices_without_groups", "security_mode_already_enabled", "hub_offline", "hub_busy", "hub_error", "hub_wrong_state", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_WITHOUT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SOME_DEVICES_WITHOUT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_MODE_ALREADY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_without_groups: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        some_devices_without_groups: _response_pb2.DefaultError
        security_mode_already_enabled: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_without_groups: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., some_devices_without_groups: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., security_mode_already_enabled: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetSecurityModeResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SetSecurityModeResponse.Failure, _Mapping]] = ...) -> None: ...
