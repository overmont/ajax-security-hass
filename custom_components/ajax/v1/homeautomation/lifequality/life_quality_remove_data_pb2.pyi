from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeQualityRemoveDataRequest(_message.Message):
    __slots__ = ("hub_hex_id", "device_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    def __init__(self, hub_hex_id: _Optional[str] = ..., device_hex_id: _Optional[str] = ...) -> None: ...

class LifeQualityRemoveDataResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "not_found_error", "authentication_error", "timeout_error", "internal_error")
        class NotFoundError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class InternalError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AuthenticationError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TimeoutError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_ERROR_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        message: str
        not_found_error: LifeQualityRemoveDataResponse.Failure.NotFoundError
        authentication_error: LifeQualityRemoveDataResponse.Failure.AuthenticationError
        timeout_error: LifeQualityRemoveDataResponse.Failure.TimeoutError
        internal_error: LifeQualityRemoveDataResponse.Failure.InternalError
        def __init__(self, message: _Optional[str] = ..., not_found_error: _Optional[_Union[LifeQualityRemoveDataResponse.Failure.NotFoundError, _Mapping]] = ..., authentication_error: _Optional[_Union[LifeQualityRemoveDataResponse.Failure.AuthenticationError, _Mapping]] = ..., timeout_error: _Optional[_Union[LifeQualityRemoveDataResponse.Failure.TimeoutError, _Mapping]] = ..., internal_error: _Optional[_Union[LifeQualityRemoveDataResponse.Failure.InternalError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: LifeQualityRemoveDataResponse.Success
    failure: LifeQualityRemoveDataResponse.Failure
    def __init__(self, success: _Optional[_Union[LifeQualityRemoveDataResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[LifeQualityRemoveDataResponse.Failure, _Mapping]] = ...) -> None: ...
