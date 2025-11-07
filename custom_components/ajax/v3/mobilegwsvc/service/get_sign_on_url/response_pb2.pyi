from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSignOnUrlResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("sign_on_url",)
        SIGN_ON_URL_FIELD_NUMBER: _ClassVar[int]
        sign_on_url: str
        def __init__(self, sign_on_url: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "sso_config_not_found", "unauthenticated", "account_not_confirmed", "account_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SSO_CONFIG_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        UNAUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NOT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        sso_config_not_found: _response_pb2.Error
        unauthenticated: _response_pb2.Error
        account_not_confirmed: _response_pb2.Error
        account_locked: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., sso_config_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unauthenticated: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., account_not_confirmed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., account_locked: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetSignOnUrlResponse.Success
    failure: GetSignOnUrlResponse.Failure
    def __init__(self, success: _Optional[_Union[GetSignOnUrlResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetSignOnUrlResponse.Failure, _Mapping]] = ...) -> None: ...
