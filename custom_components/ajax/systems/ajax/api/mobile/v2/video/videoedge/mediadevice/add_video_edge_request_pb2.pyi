from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_pb2 as _media_device_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_capabilities_pb2 as _media_device_capabilities_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddVideoEdgeRequest(_message.Message):
    __slots__ = ("video_edge_id", "family", "model", "name", "source_video_edge_id", "space_locator", "make_permanent")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MAKE_PERMANENT_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    family: str
    model: str
    name: str
    source_video_edge_id: str
    space_locator: _space_locator_pb2.SpaceLocator
    make_permanent: bool
    def __init__(self, video_edge_id: _Optional[str] = ..., family: _Optional[str] = ..., model: _Optional[str] = ..., name: _Optional[str] = ..., source_video_edge_id: _Optional[str] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., make_permanent: bool = ...) -> None: ...

class AddVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("media_device_id", "channels")
        MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        media_device_id: str
        channels: _containers.RepeatedCompositeFieldContainer[AddVideoEdgeResponse.AvailableChannel]
        def __init__(self, media_device_id: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[AddVideoEdgeResponse.AvailableChannel, _Mapping]]] = ...) -> None: ...
    class AvailableChannel(_message.Message):
        __slots__ = ("id_on_media_device",)
        ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        id_on_media_device: str
        def __init__(self, id_on_media_device: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_armed", "permission_denied", "video_edge_not_found", "source_video_edge_not_found", "bad_device_family", "bad_device_model", "onvif_authorization_failed", "connection_failed", "channels_number_constraint_violation", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        BAD_DEVICE_FAMILY_FIELD_NUMBER: _ClassVar[int]
        BAD_DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
        ONVIF_AUTHORIZATION_FAILED_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FAILED_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_NUMBER_CONSTRAINT_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        source_video_edge_not_found: _response_pb2.DefaultError
        bad_device_family: _response_pb2.DefaultError
        bad_device_model: _response_pb2.DefaultError
        onvif_authorization_failed: _response_pb2.DefaultError
        connection_failed: _response_pb2.DefaultError
        channels_number_constraint_violation: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., source_video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., bad_device_family: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., bad_device_model: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., onvif_authorization_failed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., connection_failed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channels_number_constraint_violation: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AddVideoEdgeResponse.Success
    failure: AddVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[AddVideoEdgeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[AddVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
