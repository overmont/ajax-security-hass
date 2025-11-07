from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.service.stream_video_player import player_video_edge_pb2 as _player_video_edge_pb2
from v3.mobilegwsvc.service.stream_video_player import updates_pb2 as _updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamVideoPlayerResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("initial_state", "updates")
        class InitialState(_message.Message):
            __slots__ = ("video_edges",)
            VIDEO_EDGES_FIELD_NUMBER: _ClassVar[int]
            video_edges: _containers.RepeatedCompositeFieldContainer[_player_video_edge_pb2.PlayerVideoEdge]
            def __init__(self, video_edges: _Optional[_Iterable[_Union[_player_video_edge_pb2.PlayerVideoEdge, _Mapping]]] = ...) -> None: ...
        INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        initial_state: StreamVideoPlayerResponse.Success.InitialState
        updates: _updates_pb2.Updates
        def __init__(self, initial_state: _Optional[_Union[StreamVideoPlayerResponse.Success.InitialState, _Mapping]] = ..., updates: _Optional[_Union[_updates_pb2.Updates, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamVideoPlayerResponse.Success
    failure: StreamVideoPlayerResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamVideoPlayerResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamVideoPlayerResponse.Failure, _Mapping]] = ...) -> None: ...
