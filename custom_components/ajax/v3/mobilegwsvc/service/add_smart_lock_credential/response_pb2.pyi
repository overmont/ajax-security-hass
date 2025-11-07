from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.hub.device.smartlock.credential import smart_lock_credential_pb2 as _smart_lock_credential_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddSmartLockCredentialResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("waiting_for_device_pairing", "credential_added")
        WAITING_FOR_DEVICE_PAIRING_FIELD_NUMBER: _ClassVar[int]
        CREDENTIAL_ADDED_FIELD_NUMBER: _ClassVar[int]
        waiting_for_device_pairing: AddSmartLockCredentialResponse.WaitingForDevicePairing
        credential_added: _smart_lock_credential_pb2.SmartLockCredential
        def __init__(self, waiting_for_device_pairing: _Optional[_Union[AddSmartLockCredentialResponse.WaitingForDevicePairing, _Mapping]] = ..., credential_added: _Optional[_Union[_smart_lock_credential_pb2.SmartLockCredential, _Mapping]] = ...) -> None: ...
    class WaitingForDevicePairing(_message.Message):
        __slots__ = ("timeout",)
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        timeout: _timestamp_pb2.Timestamp
        def __init__(self, timeout: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("hub_offline", "hub_wrong_state", "command_not_performed", "delivered_was_already_performed", "permission_denied", "object_not_found", "hub_busy", "device_pairing_timeout", "code_not_unique", "name_not_unique", "limit_exceeded", "hub_error", "bad_request")
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        DELIVERED_WAS_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PAIRING_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        CODE_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        NAME_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        command_not_performed: _response_pb2.Error
        delivered_was_already_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        object_not_found: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        device_pairing_timeout: _response_pb2.Error
        code_not_unique: _response_pb2.Error
        name_not_unique: _response_pb2.Error
        limit_exceeded: _response_pb2.Error
        hub_error: _response_pb2.Error
        bad_request: _response_pb2.Error
        def __init__(self, hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., command_not_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., delivered_was_already_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., object_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., device_pairing_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., code_not_unique: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., name_not_unique: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AddSmartLockCredentialResponse.Success
    failure: AddSmartLockCredentialResponse.Failure
    def __init__(self, success: _Optional[_Union[AddSmartLockCredentialResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[AddSmartLockCredentialResponse.Failure, _Mapping]] = ...) -> None: ...
