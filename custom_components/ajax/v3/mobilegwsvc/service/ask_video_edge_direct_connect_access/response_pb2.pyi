from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskVideoEdgeDirectConnectAccessResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("raw_key", "encrypted_key", "encrypted_key_signature")
        RAW_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        raw_key: bytes
        encrypted_key: bytes
        encrypted_key_signature: bytes
        def __init__(self, raw_key: _Optional[bytes] = ..., encrypted_key: _Optional[bytes] = ..., encrypted_key_signature: _Optional[bytes] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_armed", "certificate_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        certificate_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., certificate_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AskVideoEdgeDirectConnectAccessResponse.Success
    failure: AskVideoEdgeDirectConnectAccessResponse.Failure
    def __init__(self, success: _Optional[_Union[AskVideoEdgeDirectConnectAccessResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[AskVideoEdgeDirectConnectAccessResponse.Failure, _Mapping]] = ...) -> None: ...
