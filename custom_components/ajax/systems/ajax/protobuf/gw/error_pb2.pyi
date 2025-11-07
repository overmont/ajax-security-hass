from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GwError(_message.Message):
    __slots__ = ("not_found_error", "authentication_error", "timeout_error", "master_key_error", "hub_already_in_use_error", "hub_already_in_use_by_another_company_error", "request_was_already_sent_error", "hub_not_found_by_master_key_error", "permission_denied_error", "internal_error")
    class NotFoundError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class InternalError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class AuthenticationError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class TimeoutError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class MasterKeyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class HubAlreadyInUseError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class HubAlreadyInUseByAnotherCompanyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class RequestWasAlreadySentError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class HubNotFoundByMasterKeyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class PermissionDeniedError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_ERROR_FIELD_NUMBER: _ClassVar[int]
    MASTER_KEY_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_ALREADY_IN_USE_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_ALREADY_IN_USE_BY_ANOTHER_COMPANY_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_WAS_ALREADY_SENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_NOT_FOUND_BY_MASTER_KEY_ERROR_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_ERROR_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    not_found_error: GwError.NotFoundError
    authentication_error: GwError.AuthenticationError
    timeout_error: GwError.TimeoutError
    master_key_error: GwError.MasterKeyError
    hub_already_in_use_error: GwError.HubAlreadyInUseError
    hub_already_in_use_by_another_company_error: GwError.HubAlreadyInUseByAnotherCompanyError
    request_was_already_sent_error: GwError.RequestWasAlreadySentError
    hub_not_found_by_master_key_error: GwError.HubNotFoundByMasterKeyError
    permission_denied_error: GwError.PermissionDeniedError
    internal_error: GwError.InternalError
    def __init__(self, not_found_error: _Optional[_Union[GwError.NotFoundError, _Mapping]] = ..., authentication_error: _Optional[_Union[GwError.AuthenticationError, _Mapping]] = ..., timeout_error: _Optional[_Union[GwError.TimeoutError, _Mapping]] = ..., master_key_error: _Optional[_Union[GwError.MasterKeyError, _Mapping]] = ..., hub_already_in_use_error: _Optional[_Union[GwError.HubAlreadyInUseError, _Mapping]] = ..., hub_already_in_use_by_another_company_error: _Optional[_Union[GwError.HubAlreadyInUseByAnotherCompanyError, _Mapping]] = ..., request_was_already_sent_error: _Optional[_Union[GwError.RequestWasAlreadySentError, _Mapping]] = ..., hub_not_found_by_master_key_error: _Optional[_Union[GwError.HubNotFoundByMasterKeyError, _Mapping]] = ..., permission_denied_error: _Optional[_Union[GwError.PermissionDeniedError, _Mapping]] = ..., internal_error: _Optional[_Union[GwError.InternalError, _Mapping]] = ...) -> None: ...
