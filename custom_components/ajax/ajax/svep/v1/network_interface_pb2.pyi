from ajax.video.v1.types import types_pb2 as _types_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NS_NONE: _ClassVar[NetworkState]
    NS_OFFLINE: _ClassVar[NetworkState]
    NS_CONFIGURING: _ClassVar[NetworkState]
    NS_ONLINE: _ClassVar[NetworkState]

class NetworkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NE_OTHER: _ClassVar[NetworkError]
    NE_OK: _ClassVar[NetworkError]
    NE_OUT_OF_RANGE: _ClassVar[NetworkError]
    NE_PIN_MISSING: _ClassVar[NetworkError]
    NE_DHCP_FAILED: _ClassVar[NetworkError]
    NE_CONNECT_FAILED: _ClassVar[NetworkError]
    NE_LOGIN_FAILED: _ClassVar[NetworkError]
    NE_AUTH_FAILED: _ClassVar[NetworkError]
    NE_INVALID_KEY: _ClassVar[NetworkError]
    NE_BLOCKED: _ClassVar[NetworkError]

class NetworkWifiSecurity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NWS_OTHER: _ClassVar[NetworkWifiSecurity]
    NWS_NONE: _ClassVar[NetworkWifiSecurity]
    NWS_WEP: _ClassVar[NetworkWifiSecurity]
    NWS_PSK: _ClassVar[NetworkWifiSecurity]
    NWS_IEEE8021X: _ClassVar[NetworkWifiSecurity]
    NWS_WPS: _ClassVar[NetworkWifiSecurity]
NS_NONE: NetworkState
NS_OFFLINE: NetworkState
NS_CONFIGURING: NetworkState
NS_ONLINE: NetworkState
NE_OTHER: NetworkError
NE_OK: NetworkError
NE_OUT_OF_RANGE: NetworkError
NE_PIN_MISSING: NetworkError
NE_DHCP_FAILED: NetworkError
NE_CONNECT_FAILED: NetworkError
NE_LOGIN_FAILED: NetworkError
NE_AUTH_FAILED: NetworkError
NE_INVALID_KEY: NetworkError
NE_BLOCKED: NetworkError
NWS_OTHER: NetworkWifiSecurity
NWS_NONE: NetworkWifiSecurity
NWS_WEP: NetworkWifiSecurity
NWS_PSK: NetworkWifiSecurity
NWS_IEEE8021X: NetworkWifiSecurity
NWS_WPS: NetworkWifiSecurity

class NetworkInterface(_message.Message):
    __slots__ = ("guid", "mac_address", "enabled", "ethernet", "wifi", "name", "status", "desired_configuration", "configuration", "stats")
    class Ethernet(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Wifi(_message.Message):
        __slots__ = ("signal_strength", "security", "credentials")
        SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        SECURITY_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        signal_strength: int
        security: _containers.RepeatedScalarFieldContainer[NetworkWifiSecurity]
        credentials: NetworkWifiCredentials
        def __init__(self, signal_strength: _Optional[int] = ..., security: _Optional[_Iterable[_Union[NetworkWifiSecurity, str]]] = ..., credentials: _Optional[_Union[NetworkWifiCredentials, _Mapping]] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ("tx_bytes", "rx_bytes", "tx_errors", "rx_errors", "tx_dropped", "rx_dropped")
        TX_BYTES_FIELD_NUMBER: _ClassVar[int]
        RX_BYTES_FIELD_NUMBER: _ClassVar[int]
        TX_ERRORS_FIELD_NUMBER: _ClassVar[int]
        RX_ERRORS_FIELD_NUMBER: _ClassVar[int]
        TX_DROPPED_FIELD_NUMBER: _ClassVar[int]
        RX_DROPPED_FIELD_NUMBER: _ClassVar[int]
        tx_bytes: int
        rx_bytes: int
        tx_errors: int
        rx_errors: int
        tx_dropped: int
        rx_dropped: int
        def __init__(self, tx_bytes: _Optional[int] = ..., rx_bytes: _Optional[int] = ..., tx_errors: _Optional[int] = ..., rx_errors: _Optional[int] = ..., tx_dropped: _Optional[int] = ..., rx_dropped: _Optional[int] = ...) -> None: ...
    GUID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    guid: str
    mac_address: _types_pb2.MacAddress
    enabled: bool
    ethernet: NetworkInterface.Ethernet
    wifi: NetworkInterface.Wifi
    name: str
    status: NetworkStatus
    desired_configuration: NetworkConfiguration
    configuration: NetworkConfiguration
    stats: NetworkInterface.Stats
    def __init__(self, guid: _Optional[str] = ..., mac_address: _Optional[_Union[_types_pb2.MacAddress, _Mapping]] = ..., enabled: bool = ..., ethernet: _Optional[_Union[NetworkInterface.Ethernet, _Mapping]] = ..., wifi: _Optional[_Union[NetworkInterface.Wifi, _Mapping]] = ..., name: _Optional[str] = ..., status: _Optional[_Union[NetworkStatus, _Mapping]] = ..., desired_configuration: _Optional[_Union[NetworkConfiguration, _Mapping]] = ..., configuration: _Optional[_Union[NetworkConfiguration, _Mapping]] = ..., stats: _Optional[_Union[NetworkInterface.Stats, _Mapping]] = ...) -> None: ...

class NetworkStatus(_message.Message):
    __slots__ = ("state", "error")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: NetworkState
    error: NetworkError
    def __init__(self, state: _Optional[_Union[NetworkState, str]] = ..., error: _Optional[_Union[NetworkError, str]] = ...) -> None: ...

class NetworkConfiguration(_message.Message):
    __slots__ = ("v4", "v6", "name_servers")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
    v4: NetworkConfigurationIPv4
    v6: NetworkConfigurationIPv6
    name_servers: _containers.RepeatedCompositeFieldContainer[_types_pb2.IpAddress]
    def __init__(self, v4: _Optional[_Union[NetworkConfigurationIPv4, _Mapping]] = ..., v6: _Optional[_Union[NetworkConfigurationIPv6, _Mapping]] = ..., name_servers: _Optional[_Iterable[_Union[_types_pb2.IpAddress, _Mapping]]] = ...) -> None: ...

class NetworkConfigurationIPv4(_message.Message):
    __slots__ = ("method", "address", "netmask", "gateway")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationIPv4.Method]
        OFF: _ClassVar[NetworkConfigurationIPv4.Method]
        DHCP: _ClassVar[NetworkConfigurationIPv4.Method]
        MANUAL: _ClassVar[NetworkConfigurationIPv4.Method]
    NONE: NetworkConfigurationIPv4.Method
    OFF: NetworkConfigurationIPv4.Method
    DHCP: NetworkConfigurationIPv4.Method
    MANUAL: NetworkConfigurationIPv4.Method
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: NetworkConfigurationIPv4.Method
    address: _types_pb2.IpAddressV4
    netmask: _types_pb2.IpAddressV4
    gateway: _types_pb2.IpAddressV4
    def __init__(self, method: _Optional[_Union[NetworkConfigurationIPv4.Method, str]] = ..., address: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ..., netmask: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ..., gateway: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ...) -> None: ...

class NetworkConfigurationIPv6(_message.Message):
    __slots__ = ("method", "address", "prefix_length", "gateway")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationIPv6.Method]
        OFF: _ClassVar[NetworkConfigurationIPv6.Method]
        AUTO: _ClassVar[NetworkConfigurationIPv6.Method]
        MANUAL: _ClassVar[NetworkConfigurationIPv6.Method]
    NONE: NetworkConfigurationIPv6.Method
    OFF: NetworkConfigurationIPv6.Method
    AUTO: NetworkConfigurationIPv6.Method
    MANUAL: NetworkConfigurationIPv6.Method
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: NetworkConfigurationIPv6.Method
    address: _types_pb2.IpAddressV6
    prefix_length: int
    gateway: _types_pb2.IpAddressV6
    def __init__(self, method: _Optional[_Union[NetworkConfigurationIPv6.Method, str]] = ..., address: _Optional[_Union[_types_pb2.IpAddressV6, _Mapping]] = ..., prefix_length: _Optional[int] = ..., gateway: _Optional[_Union[_types_pb2.IpAddressV6, _Mapping]] = ...) -> None: ...

class NetworkWifiCredentials(_message.Message):
    __slots__ = ("none", "psk")
    class PSK(_message.Message):
        __slots__ = ("password",)
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        password: str
        def __init__(self, password: _Optional[str] = ...) -> None: ...
    NONE_FIELD_NUMBER: _ClassVar[int]
    PSK_FIELD_NUMBER: _ClassVar[int]
    none: _empty_pb2.Empty
    psk: NetworkWifiCredentials.PSK
    def __init__(self, none: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., psk: _Optional[_Union[NetworkWifiCredentials.PSK, _Mapping]] = ...) -> None: ...
