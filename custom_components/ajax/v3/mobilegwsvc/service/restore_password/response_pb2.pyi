from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestorePasswordResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("expected_token_length",)
        EXPECTED_TOKEN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        expected_token_length: int
        def __init__(self, expected_token_length: _Optional[int] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "cannot_send_confirmation_codes")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        CANNOT_SEND_CONFIRMATION_CODES_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        cannot_send_confirmation_codes: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., cannot_send_confirmation_codes: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RestorePasswordResponse.Success
    failure: RestorePasswordResponse.Failure
    def __init__(self, success: _Optional[_Union[RestorePasswordResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[RestorePasswordResponse.Failure, _Mapping]] = ...) -> None: ...
