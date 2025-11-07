from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetChannelPtzPresetRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "channel_id", "preset_name")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PRESET_NAME_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    channel_id: str
    preset_name: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., preset_name: _Optional[str] = ...) -> None: ...

class SetChannelPtzPresetResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "channel_not_found", "ptz_operation_not_supported", "ptz_temporary_unavailable", "ptz_presets_limit_exceeded", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PTZ_OPERATION_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        PTZ_TEMPORARY_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        PTZ_PRESETS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        ptz_operation_not_supported: _response_pb2.DefaultError
        ptz_temporary_unavailable: _response_pb2.DefaultError
        ptz_presets_limit_exceeded: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., ptz_operation_not_supported: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., ptz_temporary_unavailable: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., ptz_presets_limit_exceeded: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetChannelPtzPresetResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SetChannelPtzPresetResponse.Failure, _Mapping]] = ...) -> None: ...
