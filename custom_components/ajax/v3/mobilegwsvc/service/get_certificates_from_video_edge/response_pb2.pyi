from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.crypto import x509_certificate_pb2 as _x509_certificate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCertificatesFromVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("supported_x509_versions", "supported_rsa_key_lengths", "supported_signature_algorithms", "server_certificates", "pkcs12_supported", "pkcs10_supported")
        SUPPORTED_X509_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_RSA_KEY_LENGTHS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_SIGNATURE_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
        SERVER_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        PKCS12_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        PKCS10_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        supported_x509_versions: _containers.RepeatedScalarFieldContainer[_x509_certificate_pb2.X509Version]
        supported_rsa_key_lengths: _containers.RepeatedScalarFieldContainer[int]
        supported_signature_algorithms: _containers.RepeatedScalarFieldContainer[_types_pb2.CryptoHashAlgorithm]
        server_certificates: _containers.RepeatedCompositeFieldContainer[_x509_certificate_pb2.X509Certificate]
        pkcs12_supported: bool
        pkcs10_supported: bool
        def __init__(self, supported_x509_versions: _Optional[_Iterable[_Union[_x509_certificate_pb2.X509Version, str]]] = ..., supported_rsa_key_lengths: _Optional[_Iterable[int]] = ..., supported_signature_algorithms: _Optional[_Iterable[_Union[_types_pb2.CryptoHashAlgorithm, str]]] = ..., server_certificates: _Optional[_Iterable[_Union[_x509_certificate_pb2.X509Certificate, _Mapping]]] = ..., pkcs12_supported: bool = ..., pkcs10_supported: bool = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_is_offline", "unimplemented_video_edge_command")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unimplemented_video_edge_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetCertificatesFromVideoEdgeResponse.Success
    failure: GetCertificatesFromVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[GetCertificatesFromVideoEdgeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetCertificatesFromVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
