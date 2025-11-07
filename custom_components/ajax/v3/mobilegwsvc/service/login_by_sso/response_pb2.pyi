from v1.user import user_company_pb2 as _user_company_pb2
from v1.auth import login_response_pb2 as _login_response_pb2
from v3.mobilegwsvc.commonmodels.account import lite_account_pb2 as _lite_account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginBySsoResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("sign_on_url_response", "login_response", "company_list")
        class SignOnUrlResponse(_message.Message):
            __slots__ = ("sign_on_url", "request_id")
            SIGN_ON_URL_FIELD_NUMBER: _ClassVar[int]
            REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
            sign_on_url: str
            request_id: str
            def __init__(self, sign_on_url: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
        class LoginResponse(_message.Message):
            __slots__ = ("user_session_token", "lite_account", "user_id", "a911_session_token", "user_company", "pro_login_response")
            USER_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            LITE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
            USER_ID_FIELD_NUMBER: _ClassVar[int]
            A911_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            USER_COMPANY_FIELD_NUMBER: _ClassVar[int]
            PRO_LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
            user_session_token: bytes
            lite_account: _lite_account_pb2.LiteAccount
            user_id: str
            a911_session_token: str
            user_company: _user_company_pb2.UserCompany
            pro_login_response: _login_response_pb2.LoginResponse
            def __init__(self, user_session_token: _Optional[bytes] = ..., lite_account: _Optional[_Union[_lite_account_pb2.LiteAccount, _Mapping]] = ..., user_id: _Optional[str] = ..., a911_session_token: _Optional[str] = ..., user_company: _Optional[_Union[_user_company_pb2.UserCompany, _Mapping]] = ..., pro_login_response: _Optional[_Union[_login_response_pb2.LoginResponse, _Mapping]] = ...) -> None: ...
        SIGN_ON_URL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        COMPANY_LIST_FIELD_NUMBER: _ClassVar[int]
        sign_on_url_response: LoginBySsoResponse.Success.SignOnUrlResponse
        login_response: LoginBySsoResponse.Success.LoginResponse
        company_list: LoginBySsoResponse.CompanyList
        def __init__(self, sign_on_url_response: _Optional[_Union[LoginBySsoResponse.Success.SignOnUrlResponse, _Mapping]] = ..., login_response: _Optional[_Union[LoginBySsoResponse.Success.LoginResponse, _Mapping]] = ..., company_list: _Optional[_Union[LoginBySsoResponse.CompanyList, _Mapping]] = ...) -> None: ...
    class CompanyList(_message.Message):
        __slots__ = ("companies",)
        COMPANIES_FIELD_NUMBER: _ClassVar[int]
        companies: _containers.RepeatedCompositeFieldContainer[_user_company_pb2.UserCompany]
        def __init__(self, companies: _Optional[_Iterable[_Union[_user_company_pb2.UserCompany, _Mapping]]] = ...) -> None: ...
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
    success: LoginBySsoResponse.Success
    failure: LoginBySsoResponse.Failure
    def __init__(self, success: _Optional[_Union[LoginBySsoResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[LoginBySsoResponse.Failure, _Mapping]] = ...) -> None: ...
