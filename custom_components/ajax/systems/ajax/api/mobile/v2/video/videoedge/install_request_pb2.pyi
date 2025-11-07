from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstallVideoEdgeRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "video_edge_name", "room_id", "default_channel_group_id", "video_edge_qr_code")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    video_edge_name: str
    room_id: str
    default_channel_group_id: str
    video_edge_qr_code: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., video_edge_name: _Optional[str] = ..., room_id: _Optional[str] = ..., default_channel_group_id: _Optional[str] = ..., video_edge_qr_code: _Optional[str] = ...) -> None: ...

class InstallVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("video_edge_id", "channel_ids")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, video_edge_id: _Optional[str] = ..., channel_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_is_already_installed", "video_edge_not_found", "space_armed", "room_not_found", "space_locked", "group_not_found", "video_edge_is_offline", "role_access_required")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_ALREADY_INSTALLED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        ROLE_ACCESS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_already_installed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        group_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        role_access_required: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_already_installed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., room_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., group_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., role_access_required: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InstallVideoEdgeResponse.Success
    failure: InstallVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[InstallVideoEdgeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[InstallVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
