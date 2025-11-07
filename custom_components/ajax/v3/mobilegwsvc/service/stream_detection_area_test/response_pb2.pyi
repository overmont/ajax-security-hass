from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionAreaTestResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_IN_PROGRESS: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_READY: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_FAILED: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
        STATE_UNSPECIFIED: StreamDetectionAreaTestResponse.Success.State
        STATE_IN_PROGRESS: StreamDetectionAreaTestResponse.Success.State
        STATE_READY: StreamDetectionAreaTestResponse.Success.State
        STATE_FAILED: StreamDetectionAreaTestResponse.Success.State
        class Snapshot(_message.Message):
            __slots__ = ("detection_area",)
            DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
            detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
            def __init__(self, detection_area: _Optional[_Union[StreamDetectionAreaTestResponse.Success.DetectionArea, _Mapping]] = ...) -> None: ...
        class Update(_message.Message):
            __slots__ = ("detection_area",)
            DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
            detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
            def __init__(self, detection_area: _Optional[_Union[StreamDetectionAreaTestResponse.Success.DetectionArea, _Mapping]] = ...) -> None: ...
        class DetectionArea(_message.Message):
            __slots__ = ("state", "photo_info")
            STATE_FIELD_NUMBER: _ClassVar[int]
            PHOTO_INFO_FIELD_NUMBER: _ClassVar[int]
            state: StreamDetectionAreaTestResponse.Success.State
            photo_info: StreamDetectionAreaTestResponse.Success.PhotoInfo
            def __init__(self, state: _Optional[_Union[StreamDetectionAreaTestResponse.Success.State, str]] = ..., photo_info: _Optional[_Union[StreamDetectionAreaTestResponse.Success.PhotoInfo, _Mapping]] = ...) -> None: ...
        class PhotoInfo(_message.Message):
            __slots__ = ("url", "creation_time")
            URL_FIELD_NUMBER: _ClassVar[int]
            CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
            url: str
            creation_time: _timestamp_pb2.Timestamp
            def __init__(self, url: _Optional[str] = ..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDetectionAreaTestResponse.Success.Snapshot
        update: StreamDetectionAreaTestResponse.Success.Update
        def __init__(self, snapshot: _Optional[_Union[StreamDetectionAreaTestResponse.Success.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamDetectionAreaTestResponse.Success.Update, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDetectionAreaTestResponse.Success
    failure: StreamDetectionAreaTestResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamDetectionAreaTestResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamDetectionAreaTestResponse.Failure, _Mapping]] = ...) -> None: ...
