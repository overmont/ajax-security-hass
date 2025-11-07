from v3.mobilegwsvc.commonmodels.account import lite_account_pb2 as _lite_account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamQrSessionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("initial", "login_response")
        INITIAL_FIELD_NUMBER: _ClassVar[int]
        LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        initial: StreamQrSessionResponse.Initial
        login_response: StreamQrSessionResponse.LoginResponse
        def __init__(self, initial: _Optional[_Union[StreamQrSessionResponse.Initial, _Mapping]] = ..., login_response: _Optional[_Union[StreamQrSessionResponse.LoginResponse, _Mapping]] = ...) -> None: ...
    class Initial(_message.Message):
        __slots__ = ("qr_session_key",)
        QR_SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
        qr_session_key: bytes
        def __init__(self, qr_session_key: _Optional[bytes] = ...) -> None: ...
    class LoginResponse(_message.Message):
        __slots__ = ("session_token", "lite_account")
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        LITE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        session_token: bytes
        lite_account: _lite_account_pb2.LiteAccount
        def __init__(self, session_token: _Optional[bytes] = ..., lite_account: _Optional[_Union[_lite_account_pb2.LiteAccount, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamQrSessionResponse.Success
    failure: StreamQrSessionResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamQrSessionResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamQrSessionResponse.Failure, _Mapping]] = ...) -> None: ...
