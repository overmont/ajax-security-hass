from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MakeMediaDevicePermanentRequest(_message.Message):
    __slots__ = ("video_edge_id", "media_device_id", "name", "new_channel", "space_locator")
    class NewChannel(_message.Message):
        __slots__ = ("channel_id_on_media_device", "group_id", "room_id")
        CHANNEL_ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        channel_id_on_media_device: str
        group_id: str
        room_id: str
        def __init__(self, channel_id_on_media_device: _Optional[str] = ..., group_id: _Optional[str] = ..., room_id: _Optional[str] = ...) -> None: ...
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    media_device_id: str
    name: str
    new_channel: _containers.RepeatedCompositeFieldContainer[MakeMediaDevicePermanentRequest.NewChannel]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., media_device_id: _Optional[str] = ..., name: _Optional[str] = ..., new_channel: _Optional[_Iterable[_Union[MakeMediaDevicePermanentRequest.NewChannel, _Mapping]]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class MakeMediaDevicePermanentResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "device_not_found", "room_not_found", "group_not_found", "channels_number_constraint_violation", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_NUMBER_CONSTRAINT_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        channels_number_constraint_violation: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., room_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., group_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channels_number_constraint_violation: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: MakeMediaDevicePermanentResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[MakeMediaDevicePermanentResponse.Failure, _Mapping]] = ...) -> None: ...
