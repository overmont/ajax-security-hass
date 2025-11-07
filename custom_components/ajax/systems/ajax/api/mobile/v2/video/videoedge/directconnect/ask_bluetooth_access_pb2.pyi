from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskBluetoothDirectConnectAccessRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_certificate", "nonce", "crypto_cipher_algorithm", "crypto_hash_algorithm")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CIPHER_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_certificate: str
    nonce: str
    crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm
    crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_certificate: _Optional[str] = ..., nonce: _Optional[str] = ..., crypto_cipher_algorithm: _Optional[_Union[_types_pb2.CryptoCipherAlgorithm, str]] = ..., crypto_hash_algorithm: _Optional[_Union[_types_pb2.CryptoHashAlgorithm, str]] = ...) -> None: ...

class AskBluetoothDirectConnectAccessResponse(_message.Message):
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
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_not_disarmed")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_DISARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_not_disarmed: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_disarmed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AskBluetoothDirectConnectAccessResponse.Success
    failure: AskBluetoothDirectConnectAccessResponse.Failure
    def __init__(self, success: _Optional[_Union[AskBluetoothDirectConnectAccessResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[AskBluetoothDirectConnectAccessResponse.Failure, _Mapping]] = ...) -> None: ...
