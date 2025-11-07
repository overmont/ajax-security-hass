from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeAboutRequest(_message.Message):
    __slots__ = ("video_edge_id", "video_edge_qr_code")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    video_edge_qr_code: str
    def __init__(self, video_edge_id: _Optional[str] = ..., video_edge_qr_code: _Optional[str] = ...) -> None: ...

class GetVideoEdgeAboutResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("about",)
        ABOUT_FIELD_NUMBER: _ClassVar[int]
        about: _about_pb2.About
        def __init__(self, about: _Optional[_Union[_about_pb2.About, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "video_edge_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoEdgeAboutResponse.Success
    failure: GetVideoEdgeAboutResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVideoEdgeAboutResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetVideoEdgeAboutResponse.Failure, _Mapping]] = ...) -> None: ...
