from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_candidate_pb2 as _ice_candidate_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_candidate_filters_pb2 as _ice_candidate_filters_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_server_pb2 as _ice_server_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import session_description_pb2 as _session_description_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateWebRtcRequest(_message.Message):
    __slots__ = ("video_edge_id", "initial_streams", "ice_filters", "allow_large_rtp_packets", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    ICE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LARGE_RTP_PACKETS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    initial_streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
    ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
    allow_large_rtp_packets: bool
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., initial_streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ..., ice_filters: _Optional[_Union[_ice_candidate_filters_pb2.IceCandidateFilters, _Mapping]] = ..., allow_large_rtp_packets: bool = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class InitiateWebRtcResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("init", "offer", "new_ice_candidate", "answer")
        class WebRtcInit(_message.Message):
            __slots__ = ("session_id", "ice_servers", "streams")
            SESSION_ID_FIELD_NUMBER: _ClassVar[int]
            ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
            STREAMS_FIELD_NUMBER: _ClassVar[int]
            session_id: str
            ice_servers: _containers.RepeatedCompositeFieldContainer[_ice_server_pb2.IceServer]
            streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
            def __init__(self, session_id: _Optional[str] = ..., ice_servers: _Optional[_Iterable[_Union[_ice_server_pb2.IceServer, _Mapping]]] = ..., streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ...) -> None: ...
        class WebRtcOffer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(self, session_description: _Optional[_Union[_session_description_pb2.SessionDescription, _Mapping]] = ...) -> None: ...
        class WebRtcAnswer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(self, session_description: _Optional[_Union[_session_description_pb2.SessionDescription, _Mapping]] = ...) -> None: ...
        class WebRtcNewIceCandidate(_message.Message):
            __slots__ = ("candidate",)
            CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            candidate: _ice_candidate_pb2.IceCandidate
            def __init__(self, candidate: _Optional[_Union[_ice_candidate_pb2.IceCandidate, _Mapping]] = ...) -> None: ...
        INIT_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        init: InitiateWebRtcResponse.Success.WebRtcInit
        offer: InitiateWebRtcResponse.Success.WebRtcOffer
        new_ice_candidate: InitiateWebRtcResponse.Success.WebRtcNewIceCandidate
        answer: InitiateWebRtcResponse.Success.WebRtcAnswer
        def __init__(self, init: _Optional[_Union[InitiateWebRtcResponse.Success.WebRtcInit, _Mapping]] = ..., offer: _Optional[_Union[InitiateWebRtcResponse.Success.WebRtcOffer, _Mapping]] = ..., new_ice_candidate: _Optional[_Union[InitiateWebRtcResponse.Success.WebRtcNewIceCandidate, _Mapping]] = ..., answer: _Optional[_Union[InitiateWebRtcResponse.Success.WebRtcAnswer, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "video_edge_not_found", "permission_denied", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InitiateWebRtcResponse.Success
    failure: InitiateWebRtcResponse.Failure
    def __init__(self, success: _Optional[_Union[InitiateWebRtcResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[InitiateWebRtcResponse.Failure, _Mapping]] = ...) -> None: ...
