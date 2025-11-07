from v3.mobilegwsvc.commonmodels.account import lite_account_pb2 as _lite_account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v1.auth import login_response_pb2 as _login_response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByTotpResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("session_token", "lite_account", "pro_login_response")
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        LITE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PRO_LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        session_token: bytes
        lite_account: _lite_account_pb2.LiteAccount
        pro_login_response: _login_response_pb2.LoginResponse
        def __init__(self, session_token: _Optional[bytes] = ..., lite_account: _Optional[_Union[_lite_account_pb2.LiteAccount, _Mapping]] = ..., pro_login_response: _Optional[_Union[_login_response_pb2.LoginResponse, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "account_not_confirmed", "account_locked", "invalid_totp")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NOT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        INVALID_TOTP_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        account_not_confirmed: _response_pb2.Error
        account_locked: _response_pb2.Error
        invalid_totp: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., account_not_confirmed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., account_locked: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., invalid_totp: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: LoginByTotpResponse.Success
    failure: LoginByTotpResponse.Failure
    def __init__(self, success: _Optional[_Union[LoginByTotpResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[LoginByTotpResponse.Failure, _Mapping]] = ...) -> None: ...
