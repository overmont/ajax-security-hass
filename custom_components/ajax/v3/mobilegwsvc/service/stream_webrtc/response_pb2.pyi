from systems.ajax.api.mobile.v2.common.video.webrtc import ice_candidate_pb2 as _ice_candidate_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_server_pb2 as _ice_server_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import session_description_pb2 as _session_description_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamWebrtcResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("init", "ask_streams_response", "new_ice_candidate", "offer", "answer")
        class Init(_message.Message):
            __slots__ = ("ice_servers", "streams")
            ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
            STREAMS_FIELD_NUMBER: _ClassVar[int]
            ice_servers: _containers.RepeatedCompositeFieldContainer[_ice_server_pb2.IceServer]
            streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
            def __init__(self, ice_servers: _Optional[_Iterable[_Union[_ice_server_pb2.IceServer, _Mapping]]] = ..., streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ...) -> None: ...
        class AskStreamsResponse(_message.Message):
            __slots__ = ("success", "failure")
            class AskStreamsSuccess(_message.Message):
                __slots__ = ("streams",)
                STREAMS_FIELD_NUMBER: _ClassVar[int]
                streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
                def __init__(self, streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ...) -> None: ...
            class AskStreamsFailure(_message.Message):
                __slots__ = ("bad_request", "video_edge_not_found", "permission_denied", "video_edge_is_offline")
                BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
                PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
                bad_request: _response_pb2.Error
                video_edge_not_found: _response_pb2.Error
                permission_denied: _response_pb2.Error
                video_edge_is_offline: _response_pb2.Error
                def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            FAILURE_FIELD_NUMBER: _ClassVar[int]
            success: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsSuccess
            failure: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsFailure
            def __init__(self, success: _Optional[_Union[StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsSuccess, _Mapping]] = ..., failure: _Optional[_Union[StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsFailure, _Mapping]] = ...) -> None: ...
        class NewIceCandidate(_message.Message):
            __slots__ = ("candidate",)
            CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            candidate: _ice_candidate_pb2.IceCandidate
            def __init__(self, candidate: _Optional[_Union[_ice_candidate_pb2.IceCandidate, _Mapping]] = ...) -> None: ...
        class Offer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(self, session_description: _Optional[_Union[_session_description_pb2.SessionDescription, _Mapping]] = ...) -> None: ...
        class Answer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(self, session_description: _Optional[_Union[_session_description_pb2.SessionDescription, _Mapping]] = ...) -> None: ...
        INIT_FIELD_NUMBER: _ClassVar[int]
        ASK_STREAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        init: StreamWebrtcResponse.Success.Init
        ask_streams_response: StreamWebrtcResponse.Success.AskStreamsResponse
        new_ice_candidate: StreamWebrtcResponse.Success.NewIceCandidate
        offer: StreamWebrtcResponse.Success.Offer
        answer: StreamWebrtcResponse.Success.Answer
        def __init__(self, init: _Optional[_Union[StreamWebrtcResponse.Success.Init, _Mapping]] = ..., ask_streams_response: _Optional[_Union[StreamWebrtcResponse.Success.AskStreamsResponse, _Mapping]] = ..., new_ice_candidate: _Optional[_Union[StreamWebrtcResponse.Success.NewIceCandidate, _Mapping]] = ..., offer: _Optional[_Union[StreamWebrtcResponse.Success.Offer, _Mapping]] = ..., answer: _Optional[_Union[StreamWebrtcResponse.Success.Answer, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "video_edge_not_found", "permission_denied", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamWebrtcResponse.Success
    failure: StreamWebrtcResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamWebrtcResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamWebrtcResponse.Failure, _Mapping]] = ...) -> None: ...
