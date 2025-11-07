from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSetWalkTestResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("hub_offline", "bad_request", "permission_denied", "hub_unknown_command", "hub_error", "hub_request_already_performed", "hub_busy", "hub_wrong_state")
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_REQUEST_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_unknown_command: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_request_already_performed: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_wrong_state: _response_pb2.HubWrongStateError
        def __init__(self, hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_unknown_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_request_already_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeviceCommandSetWalkTestResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[DeviceCommandSetWalkTestResponse.Failure, _Mapping]] = ...) -> None: ...
