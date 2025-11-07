from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetChannelPtzPresetsRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "channel_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    channel_id: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class GetChannelPtzPresetsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("presets",)
        class Preset(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        PRESETS_FIELD_NUMBER: _ClassVar[int]
        presets: _containers.RepeatedCompositeFieldContainer[GetChannelPtzPresetsResponse.Success.Preset]
        def __init__(self, presets: _Optional[_Iterable[_Union[GetChannelPtzPresetsResponse.Success.Preset, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "channel_not_found", "ptz_operation_not_supported", "ptz_temporary_unavailable")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PTZ_OPERATION_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        PTZ_TEMPORARY_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        ptz_operation_not_supported: _response_pb2.DefaultError
        ptz_temporary_unavailable: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., ptz_operation_not_supported: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., ptz_temporary_unavailable: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetChannelPtzPresetsResponse.Success
    failure: GetChannelPtzPresetsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetChannelPtzPresetsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetChannelPtzPresetsResponse.Failure, _Mapping]] = ...) -> None: ...
