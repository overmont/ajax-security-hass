from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskVideoEdgeDirectConnectAccessRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_certificate", "video_edge_id", "nonce", "crypto_cipher_algorithm", "crypto_hash_algorithm", "access_protocol")
    class AccessProtocol(_message.Message):
        __slots__ = ("bluetooth", "wi_fi")
        BLUETOOTH_FIELD_NUMBER: _ClassVar[int]
        WI_FI_FIELD_NUMBER: _ClassVar[int]
        bluetooth: AskVideoEdgeDirectConnectAccessRequest.Bluetooth
        wi_fi: AskVideoEdgeDirectConnectAccessRequest.WiFi
        def __init__(self, bluetooth: _Optional[_Union[AskVideoEdgeDirectConnectAccessRequest.Bluetooth, _Mapping]] = ..., wi_fi: _Optional[_Union[AskVideoEdgeDirectConnectAccessRequest.WiFi, _Mapping]] = ...) -> None: ...
    class Bluetooth(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class WiFi(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CIPHER_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_certificate: str
    video_edge_id: str
    nonce: str
    crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm
    crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm
    access_protocol: AskVideoEdgeDirectConnectAccessRequest.AccessProtocol
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_certificate: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., nonce: _Optional[str] = ..., crypto_cipher_algorithm: _Optional[_Union[_types_pb2.CryptoCipherAlgorithm, str]] = ..., crypto_hash_algorithm: _Optional[_Union[_types_pb2.CryptoHashAlgorithm, str]] = ..., access_protocol: _Optional[_Union[AskVideoEdgeDirectConnectAccessRequest.AccessProtocol, _Mapping]] = ...) -> None: ...
