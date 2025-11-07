from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckIsCaptchaRequiredForNumberResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("need_captcha",)
        NEED_CAPTCHA_FIELD_NUMBER: _ClassVar[int]
        need_captcha: bool
        def __init__(self, need_captcha: bool = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CheckIsCaptchaRequiredForNumberResponse.Success
    failure: CheckIsCaptchaRequiredForNumberResponse.Failure
    def __init__(self, success: _Optional[_Union[CheckIsCaptchaRequiredForNumberResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CheckIsCaptchaRequiredForNumberResponse.Failure, _Mapping]] = ...) -> None: ...
