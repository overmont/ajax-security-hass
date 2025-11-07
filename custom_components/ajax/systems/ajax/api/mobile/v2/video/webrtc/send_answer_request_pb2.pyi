from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import session_description_pb2 as _session_description_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendWebRtcAnswerRequest(_message.Message):
    __slots__ = ("video_edge_id", "webrtc_session_id", "session_description", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    webrtc_session_id: str
    session_description: _session_description_pb2.SessionDescription
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., webrtc_session_id: _Optional[str] = ..., session_description: _Optional[_Union[_session_description_pb2.SessionDescription, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class SendWebRtcAnswerResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "session_not_found", "video_edge_not_found", "permission_denied", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SESSION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        session_not_found: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., session_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SendWebRtcAnswerResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SendWebRtcAnswerResponse.Failure, _Mapping]] = ...) -> None: ...
