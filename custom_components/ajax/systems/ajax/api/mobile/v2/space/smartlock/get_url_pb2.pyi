from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUrlRequest(_message.Message):
    __slots__ = ("smart_lock_type",)
    SMART_LOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
    smart_lock_type: _smart_lock_pb2.SmartLockType
    def __init__(self, smart_lock_type: _Optional[_Union[_smart_lock_pb2.SmartLockType, str]] = ...) -> None: ...

class GetUrlResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetUrlResponse.Success
    failure: GetUrlResponse.Failure
    def __init__(self, success: _Optional[_Union[GetUrlResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetUrlResponse.Failure, _Mapping]] = ...) -> None: ...
