from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteScheduledAccessResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("permission_denied", "schedule_access_not_found")
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_ACCESS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        permission_denied: _response_pb2.Error
        schedule_access_not_found: _response_pb2.Error
        def __init__(self, permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., schedule_access_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeleteScheduledAccessResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[DeleteScheduledAccessResponse.Failure, _Mapping]] = ...) -> None: ...
