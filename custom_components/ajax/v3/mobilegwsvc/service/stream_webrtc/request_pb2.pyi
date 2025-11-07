import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_candidate_pb2 as _ice_candidate_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import ice_candidate_filters_pb2 as _ice_candidate_filters_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import session_description_pb2 as _session_description_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamWebrtcRequest(_message.Message):
    __slots__ = ("init", "ask_streams", "new_ice_candidate", "offer", "answer", "peer_connection_established")
    class Init(_message.Message):
        __slots__ = ("space_locator", "video_edge_id", "initial_streams", "ice_filters", "allow_large_rtp_packets")
        SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        INITIAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
        ICE_FILTERS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_LARGE_RTP_PACKETS_FIELD_NUMBER: _ClassVar[int]
        space_locator: _space_locator_pb2.SpaceLocator
        video_edge_id: str
        initial_streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
        ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
        allow_large_rtp_packets: bool
        def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., initial_streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ..., ice_filters: _Optional[_Union[_ice_candidate_filters_pb2.IceCandidateFilters, _Mapping]] = ..., allow_large_rtp_packets: bool = ...) -> None: ...
    class AskStreams(_message.Message):
        __slots__ = ("streams",)
        STREAMS_FIELD_NUMBER: _ClassVar[int]
        streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
        def __init__(self, streams: _Optional[_Iterable[_Union[_stream_pb2.Stream, _Mapping]]] = ...) -> None: ...
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
    class PeerConnectionEstablished(_message.Message):
        __slots__ = ("latency", "network_technology_type", "transport_protocol_type", "ice_candidate_type")
        LATENCY_FIELD_NUMBER: _ClassVar[int]
        NETWORK_TECHNOLOGY_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_PROTOCOL_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICE_CANDIDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        latency: _duration_pb2.Duration
        network_technology_type: _types_pb2.NetworkTechnologyType
        transport_protocol_type: _types_pb2.TransportProtocolType
        ice_candidate_type: _types_pb2.IceCandidateType
        def __init__(self, latency: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., network_technology_type: _Optional[_Union[_types_pb2.NetworkTechnologyType, str]] = ..., transport_protocol_type: _Optional[_Union[_types_pb2.TransportProtocolType, str]] = ..., ice_candidate_type: _Optional[_Union[_types_pb2.IceCandidateType, str]] = ...) -> None: ...
    INIT_FIELD_NUMBER: _ClassVar[int]
    ASK_STREAMS_FIELD_NUMBER: _ClassVar[int]
    NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    PEER_CONNECTION_ESTABLISHED_FIELD_NUMBER: _ClassVar[int]
    init: StreamWebrtcRequest.Init
    ask_streams: StreamWebrtcRequest.AskStreams
    new_ice_candidate: StreamWebrtcRequest.NewIceCandidate
    offer: StreamWebrtcRequest.Offer
    answer: StreamWebrtcRequest.Answer
    peer_connection_established: StreamWebrtcRequest.PeerConnectionEstablished
    def __init__(self, init: _Optional[_Union[StreamWebrtcRequest.Init, _Mapping]] = ..., ask_streams: _Optional[_Union[StreamWebrtcRequest.AskStreams, _Mapping]] = ..., new_ice_candidate: _Optional[_Union[StreamWebrtcRequest.NewIceCandidate, _Mapping]] = ..., offer: _Optional[_Union[StreamWebrtcRequest.Offer, _Mapping]] = ..., answer: _Optional[_Union[StreamWebrtcRequest.Answer, _Mapping]] = ..., peer_connection_established: _Optional[_Union[StreamWebrtcRequest.PeerConnectionEstablished, _Mapping]] = ...) -> None: ...
