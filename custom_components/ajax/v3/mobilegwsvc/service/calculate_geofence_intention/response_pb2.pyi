from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateGeofenceIntentionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("space_name", "space_id")
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        space_name: str
        space_id: str
        def __init__(self, space_name: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CalculateGeofenceIntentionResponse.Success
    failure: CalculateGeofenceIntentionResponse.Failure
    def __init__(self, success: _Optional[_Union[CalculateGeofenceIntentionResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CalculateGeofenceIntentionResponse.Failure, _Mapping]] = ...) -> None: ...
