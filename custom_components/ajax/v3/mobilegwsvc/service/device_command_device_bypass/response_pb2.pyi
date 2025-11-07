from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDeviceBypassResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("unknown_command", "command_not_performed", "hub_offline", "permission_denied", "alarm_reset_needed", "hub_wrong_state")
        UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ALARM_RESET_NEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        unknown_command: _response_pb2.Error
        command_not_performed: _response_pb2.Error
        hub_offline: _response_pb2.Error
        permission_denied: _response_pb2.Error
        alarm_reset_needed: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        def __init__(self, unknown_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., command_not_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., alarm_reset_needed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeviceCommandDeviceBypassResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[DeviceCommandDeviceBypassResponse.Failure, _Mapping]] = ...) -> None: ...
