from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyForMonitoringWithAccountNumberRequest(_message.Message):
    __slots__ = ("hub_hex_id", "company_hex_id", "account_number")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    company_hex_id: str
    account_number: str
    def __init__(self, hub_hex_id: _Optional[str] = ..., company_hex_id: _Optional[str] = ..., account_number: _Optional[str] = ...) -> None: ...

class ApplyForMonitoringWithAccountNumberResponse(_message.Message):
    __slots__ = ("success", "error")
    class Failure(_message.Message):
        __slots__ = ("message", "request_timeout", "cannot_apply_on_locked_hub", "hub_users_limit_exceeded", "permission_denied", "account_number_invalid")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        CANNOT_APPLY_ON_LOCKED_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_USERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_INVALID_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.DefaultError
        cannot_apply_on_locked_hub: _response_pb2.DefaultError
        hub_users_limit_exceeded: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        account_number_invalid: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., request_timeout: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., cannot_apply_on_locked_hub: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_users_limit_exceeded: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., account_number_invalid: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    error: ApplyForMonitoringWithAccountNumberResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., error: _Optional[_Union[ApplyForMonitoringWithAccountNumberResponse.Failure, _Mapping]] = ...) -> None: ...
