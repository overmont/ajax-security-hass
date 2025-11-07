from v3.mobilegwsvc.commonmodels.account import account_pb2 as _account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAccountProfileResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("account",)
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        account: _account_pb2.Account
        def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UpdateAccountProfileResponse.Success
    failure: UpdateAccountProfileResponse.Failure
    def __init__(self, success: _Optional[_Union[UpdateAccountProfileResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateAccountProfileResponse.Failure, _Mapping]] = ...) -> None: ...
