from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from ajax.video.v1.types import types_pb2 as _types_pb2
from ajax.svep.v1 import network_pb2 as _network_pb2
from ajax.svep.v1 import network_interface_pb2 as _network_interface_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfigurationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NCS_NONE: _ClassVar[NetworkConfigurationState]
    NCS_OK: _ClassVar[NetworkConfigurationState]
    NCS_FAILED: _ClassVar[NetworkConfigurationState]

class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    E_OTHER: _ClassVar[Error]
    E_UNKNOWN: _ClassVar[Error]
    E_UNIMPLEMENTED: _ClassVar[Error]
    E_INVALID_STATE: _ClassVar[Error]
    E_NETWORK_INTERFACE_NOT_FOUND: _ClassVar[Error]
    E_NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS: _ClassVar[Error]
    E_NETWORK_INTERFACE_INVALID_REQUEST: _ClassVar[Error]
NCS_NONE: NetworkConfigurationState
NCS_OK: NetworkConfigurationState
NCS_FAILED: NetworkConfigurationState
E_OTHER: Error
E_UNKNOWN: Error
E_UNIMPLEMENTED: Error
E_INVALID_STATE: Error
E_NETWORK_INTERFACE_NOT_FOUND: Error
E_NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS: Error
E_NETWORK_INTERFACE_INVALID_REQUEST: Error

class ClientMsg(_message.Message):
    __slots__ = ("sec1", "sec2", "encrypted_msg")
    SEC1_FIELD_NUMBER: _ClassVar[int]
    SEC2_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MSG_FIELD_NUMBER: _ClassVar[int]
    sec1: Sec1Request
    sec2: Sec2Request
    encrypted_msg: EncryptedMsg
    def __init__(self, sec1: _Optional[_Union[Sec1Request, _Mapping]] = ..., sec2: _Optional[_Union[Sec2Request, _Mapping]] = ..., encrypted_msg: _Optional[_Union[EncryptedMsg, _Mapping]] = ...) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = ("sec1", "sec2", "encrypted_msg")
    SEC1_FIELD_NUMBER: _ClassVar[int]
    SEC2_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MSG_FIELD_NUMBER: _ClassVar[int]
    sec1: Sec1Response
    sec2: Sec2Response
    encrypted_msg: EncryptedMsg
    def __init__(self, sec1: _Optional[_Union[Sec1Response, _Mapping]] = ..., sec2: _Optional[_Union[Sec2Response, _Mapping]] = ..., encrypted_msg: _Optional[_Union[EncryptedMsg, _Mapping]] = ...) -> None: ...

class Sec1Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sec1Response(_message.Message):
    __slots__ = ("nonce", "cert")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    nonce: str
    cert: str
    def __init__(self, nonce: _Optional[str] = ..., cert: _Optional[str] = ...) -> None: ...

class Sec2Request(_message.Message):
    __slots__ = ("hash_algorithm", "encrypted_key", "encrypted_key_signature")
    HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    hash_algorithm: _types_pb2.CryptoHashAlgorithm
    encrypted_key: bytes
    encrypted_key_signature: bytes
    def __init__(self, hash_algorithm: _Optional[_Union[_types_pb2.CryptoHashAlgorithm, str]] = ..., encrypted_key: _Optional[bytes] = ..., encrypted_key_signature: _Optional[bytes] = ...) -> None: ...

class Sec2Response(_message.Message):
    __slots__ = ("is_ok",)
    IS_OK_FIELD_NUMBER: _ClassVar[int]
    is_ok: bool
    def __init__(self, is_ok: bool = ...) -> None: ...

class EncryptedMsg(_message.Message):
    __slots__ = ("data", "iv", "tag")
    DATA_FIELD_NUMBER: _ClassVar[int]
    IV_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    iv: bytes
    tag: bytes
    def __init__(self, data: _Optional[bytes] = ..., iv: _Optional[bytes] = ..., tag: _Optional[bytes] = ...) -> None: ...

class ClientSecMsg(_message.Message):
    __slots__ = ("seq_no", "hello", "ping", "network_update_configuration", "network_wifi_scan")
    SEQ_NO_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPDATE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_WIFI_SCAN_FIELD_NUMBER: _ClassVar[int]
    seq_no: int
    hello: HelloRequest
    ping: PingRequest
    network_update_configuration: NetworkUpdateConfigurationRequest
    network_wifi_scan: NetworkWifiScanRequest
    def __init__(self, seq_no: _Optional[int] = ..., hello: _Optional[_Union[HelloRequest, _Mapping]] = ..., ping: _Optional[_Union[PingRequest, _Mapping]] = ..., network_update_configuration: _Optional[_Union[NetworkUpdateConfigurationRequest, _Mapping]] = ..., network_wifi_scan: _Optional[_Union[NetworkWifiScanRequest, _Mapping]] = ...) -> None: ...

class ServerSecMsg(_message.Message):
    __slots__ = ("seq_no", "change", "network_configuration_state", "error", "hello", "ping", "network_update_configuration", "network_wifi_scan")
    SEQ_NO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIGURATION_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPDATE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_WIFI_SCAN_FIELD_NUMBER: _ClassVar[int]
    seq_no: int
    change: StateChange
    network_configuration_state: NetworkConfigurationState
    error: Error
    hello: HelloResponse
    ping: PingResponse
    network_update_configuration: NetworkUpdateConfigurationResponse
    network_wifi_scan: NetworkWifiScanResponse
    def __init__(self, seq_no: _Optional[int] = ..., change: _Optional[_Union[StateChange, _Mapping]] = ..., network_configuration_state: _Optional[_Union[NetworkConfigurationState, str]] = ..., error: _Optional[_Union[Error, str]] = ..., hello: _Optional[_Union[HelloResponse, _Mapping]] = ..., ping: _Optional[_Union[PingResponse, _Mapping]] = ..., network_update_configuration: _Optional[_Union[NetworkUpdateConfigurationResponse, _Mapping]] = ..., network_wifi_scan: _Optional[_Union[NetworkWifiScanResponse, _Mapping]] = ...) -> None: ...

class StateChange(_message.Message):
    __slots__ = ("network", "network_interface", "mask", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[StateChange.Type]
        UPDATE: _ClassVar[StateChange.Type]
        ADD: _ClassVar[StateChange.Type]
        REMOVE: _ClassVar[StateChange.Type]
    NONE: StateChange.Type
    UPDATE: StateChange.Type
    ADD: StateChange.Type
    REMOVE: StateChange.Type
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    network: _network_pb2.Network
    network_interface: _network_interface_pb2.NetworkInterface
    mask: _field_mask_pb2.FieldMask
    type: StateChange.Type
    def __init__(self, network: _Optional[_Union[_network_pb2.Network, _Mapping]] = ..., network_interface: _Optional[_Union[_network_interface_pb2.NetworkInterface, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., type: _Optional[_Union[StateChange.Type, str]] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: Snapshot
    def __init__(self, snapshot: _Optional[_Union[Snapshot, _Mapping]] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkUpdateConfigurationRequest(_message.Message):
    __slots__ = ("network_interface_guid", "desired_configuration", "wifi", "configuration_timeout")
    class Wifi(_message.Message):
        __slots__ = ("enabled", "credentials")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        credentials: _network_interface_pb2.NetworkWifiCredentials
        def __init__(self, enabled: bool = ..., credentials: _Optional[_Union[_network_interface_pb2.NetworkWifiCredentials, _Mapping]] = ...) -> None: ...
    NETWORK_INTERFACE_GUID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    network_interface_guid: str
    desired_configuration: _network_interface_pb2.NetworkConfiguration
    wifi: NetworkUpdateConfigurationRequest.Wifi
    configuration_timeout: _duration_pb2.Duration
    def __init__(self, network_interface_guid: _Optional[str] = ..., desired_configuration: _Optional[_Union[_network_interface_pb2.NetworkConfiguration, _Mapping]] = ..., wifi: _Optional[_Union[NetworkUpdateConfigurationRequest.Wifi, _Mapping]] = ..., configuration_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class NetworkUpdateConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkWifiScanRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkWifiScanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ("network", "network_interfaces")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    network: _network_pb2.Network
    network_interfaces: _containers.RepeatedCompositeFieldContainer[_network_interface_pb2.NetworkInterface]
    def __init__(self, network: _Optional[_Union[_network_pb2.Network, _Mapping]] = ..., network_interfaces: _Optional[_Iterable[_Union[_network_interface_pb2.NetworkInterface, _Mapping]]] = ...) -> None: ...
