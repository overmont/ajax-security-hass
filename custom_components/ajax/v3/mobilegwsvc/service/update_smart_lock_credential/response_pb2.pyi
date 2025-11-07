from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockCredentialResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("hub_offline", "hub_wrong_state", "command_not_performed", "delivered_was_already_performed", "permission_denied", "object_not_found", "hub_busy", "code_not_unique", "name_not_unique", "cannot_disable_last_credential", "hub_error", "bad_request")
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        DELIVERED_WAS_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        CODE_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        NAME_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        CANNOT_DISABLE_LAST_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        command_not_performed: _response_pb2.Error
        delivered_was_already_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        object_not_found: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        code_not_unique: _response_pb2.Error
        name_not_unique: _response_pb2.Error
        cannot_disable_last_credential: _response_pb2.Error
        hub_error: _response_pb2.Error
        bad_request: _response_pb2.Error
        def __init__(self, hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., command_not_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., delivered_was_already_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., object_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., code_not_unique: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., name_not_unique: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., cannot_disable_last_credential: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UpdateSmartLockCredentialResponse.Success
    failure: UpdateSmartLockCredentialResponse.Failure
    def __init__(self, success: _Optional[_Union[UpdateSmartLockCredentialResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateSmartLockCredentialResponse.Failure, _Mapping]] = ...) -> None: ...
