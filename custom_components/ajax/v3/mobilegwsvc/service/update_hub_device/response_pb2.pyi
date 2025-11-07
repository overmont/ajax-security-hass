from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHubDeviceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "device_no_found", "permission_denied", "hub_offline", "hub_wrong_state")
        class HubWrongStateError(_message.Message):
            __slots__ = ("error_cause",)
            ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
            error_cause: _containers.RepeatedCompositeFieldContainer[_response_pb2.ErrorCause]
            def __init__(self, error_cause: _Optional[_Iterable[_Union[_response_pb2.ErrorCause, _Mapping]]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NO_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        device_no_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_wrong_state: UpdateHubDeviceResponse.Failure.HubWrongStateError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., device_no_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[UpdateHubDeviceResponse.Failure.HubWrongStateError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateHubDeviceResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateHubDeviceResponse.Failure, _Mapping]] = ...) -> None: ...
