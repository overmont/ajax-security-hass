from v3.mobilegwsvc.commonmodels.account import account_pb2 as _account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("account",)
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        account: _account_pb2.Account
        def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAccountResponse.Success
    failure: GetAccountResponse.Failure
    def __init__(self, success: _Optional[_Union[GetAccountResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetAccountResponse.Failure, _Mapping]] = ...) -> None: ...
