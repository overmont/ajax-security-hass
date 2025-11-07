from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllSmartLocksAvailableToAddRequest(_message.Message):
    __slots__ = ("space_id", "type")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    type: _smart_lock_pb2.SmartLockType
    def __init__(self, space_id: _Optional[str] = ..., type: _Optional[_Union[_smart_lock_pb2.SmartLockType, str]] = ...) -> None: ...

class FindAllSmartLocksAvailableToAddResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("smart_locks",)
        SMART_LOCKS_FIELD_NUMBER: _ClassVar[int]
        smart_locks: _containers.RepeatedCompositeFieldContainer[_smart_lock_pb2.SmartLockAvailableToAdd]
        def __init__(self, smart_locks: _Optional[_Iterable[_Union[_smart_lock_pb2.SmartLockAvailableToAdd, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("external_service_access_denied", "permission_denied", "bad_request", "space_not_found", "space_armed")
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        external_service_access_denied: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        def __init__(self, external_service_access_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllSmartLocksAvailableToAddResponse.Success
    failure: FindAllSmartLocksAvailableToAddResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAllSmartLocksAvailableToAddResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAllSmartLocksAvailableToAddResponse.Failure, _Mapping]] = ...) -> None: ...
