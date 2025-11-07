from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyCompanyTemplateResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("command_not_performed", "permission_denied", "hub_wrong_state", "hub_offline", "hub_busy", "illegal_argument", "not_found")
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        command_not_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        hub_offline: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        illegal_argument: _response_pb2.Error
        not_found: _response_pb2.Error
        def __init__(self, command_not_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: ApplyCompanyTemplateResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[ApplyCompanyTemplateResponse.Failure, _Mapping]] = ...) -> None: ...
