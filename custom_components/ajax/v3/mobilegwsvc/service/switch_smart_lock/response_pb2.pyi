from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchSmartLockResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "smart_lock_not_found", "external_service_access_denied", "smart_lock_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        smart_lock_not_found: _response_pb2.Error
        external_service_access_denied: _response_pb2.Error
        smart_lock_offline: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., smart_lock_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., external_service_access_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., smart_lock_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SwitchSmartLockResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SwitchSmartLockResponse.Failure, _Mapping]] = ...) -> None: ...
