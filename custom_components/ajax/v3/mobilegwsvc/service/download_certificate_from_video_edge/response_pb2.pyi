from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadCertificateFromVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("certificates_pem",)
        CERTIFICATES_PEM_FIELD_NUMBER: _ClassVar[int]
        certificates_pem: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, certificates_pem: _Optional[_Iterable[str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_is_offline", "unimplemented_video_edge_command", "certificate_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        certificate_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unimplemented_video_edge_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., certificate_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DownloadCertificateFromVideoEdgeResponse.Success
    failure: DownloadCertificateFromVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[DownloadCertificateFromVideoEdgeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[DownloadCertificateFromVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
