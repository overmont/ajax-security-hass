from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UninstallVideoEdgeRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ...) -> None: ...

class UninstallVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "space_armed", "space_locked", "unable_to_remove_backup_channel", "video_edge_has_subscriptions", "video_edge_has_subscriptions_member")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        UNABLE_TO_REMOVE_BACKUP_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_HAS_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_HAS_SUBSCRIPTIONS_MEMBER_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        unable_to_remove_backup_channel: _response_pb2.DefaultError
        video_edge_has_subscriptions: _response_pb2.DefaultError
        video_edge_has_subscriptions_member: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., unable_to_remove_backup_channel: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_has_subscriptions: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_has_subscriptions_member: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UninstallVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UninstallVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
