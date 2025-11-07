from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifAndRtspPortsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "onvif_http_port", "rtsp_http_port")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ONVIF_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    RTSP_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    onvif_http_port: int
    rtsp_http_port: int
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., onvif_http_port: _Optional[int] = ..., rtsp_http_port: _Optional[int] = ...) -> None: ...
