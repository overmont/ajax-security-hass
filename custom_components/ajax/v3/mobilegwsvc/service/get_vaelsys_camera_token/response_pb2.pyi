from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVaelsysCameraTokenResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("token", "external_user_id")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
        token: str
        external_user_id: str
        def __init__(self, token: _Optional[str] = ..., external_user_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetVaelsysCameraTokenResponse.Success
    error: GetVaelsysCameraTokenResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVaelsysCameraTokenResponse.Success, _Mapping]] = ..., error: _Optional[_Union[GetVaelsysCameraTokenResponse.Failure, _Mapping]] = ...) -> None: ...
