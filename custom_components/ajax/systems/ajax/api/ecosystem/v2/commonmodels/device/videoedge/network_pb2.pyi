from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHOD_UNSPECIFIED: _ClassVar[Method]
    METHOD_OFF: _ClassVar[Method]
    METHOD_DHCP: _ClassVar[Method]
    METHOD_MANUAL: _ClassVar[Method]
METHOD_UNSPECIFIED: Method
METHOD_OFF: Method
METHOD_DHCP: Method
METHOD_MANUAL: Method

class IpAddress(_message.Message):
    __slots__ = ("v4", "v6")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    v4: IpAddressV4
    v6: IpAddressV6
    def __init__(self, v4: _Optional[_Union[IpAddressV4, _Mapping]] = ..., v6: _Optional[_Union[IpAddressV6, _Mapping]] = ...) -> None: ...

class IpAddressV4(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class IpAddressV6(_message.Message):
    __slots__ = ("data", "scope_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    scope_id: int
    def __init__(self, data: _Optional[bytes] = ..., scope_id: _Optional[int] = ...) -> None: ...

class NetworkConfiguration(_message.Message):
    __slots__ = ("v4", "v6", "name_servers")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
    v4: NetworkConfigurationIPv4
    v6: NetworkConfigurationIPv6
    name_servers: _containers.RepeatedCompositeFieldContainer[IpAddress]
    def __init__(self, v4: _Optional[_Union[NetworkConfigurationIPv4, _Mapping]] = ..., v6: _Optional[_Union[NetworkConfigurationIPv6, _Mapping]] = ..., name_servers: _Optional[_Iterable[_Union[IpAddress, _Mapping]]] = ...) -> None: ...

class NetworkConfigurationIPv4(_message.Message):
    __slots__ = ("method", "address", "netmask", "gateway")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: Method
    address: IpAddressV4
    netmask: IpAddressV4
    gateway: IpAddressV4
    def __init__(self, method: _Optional[_Union[Method, str]] = ..., address: _Optional[_Union[IpAddressV4, _Mapping]] = ..., netmask: _Optional[_Union[IpAddressV4, _Mapping]] = ..., gateway: _Optional[_Union[IpAddressV4, _Mapping]] = ...) -> None: ...

class NetworkConfigurationIPv6(_message.Message):
    __slots__ = ("method", "address", "prefix_length", "gateway")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: Method
    address: IpAddressV6
    prefix_length: int
    gateway: IpAddressV6
    def __init__(self, method: _Optional[_Union[Method, str]] = ..., address: _Optional[_Union[IpAddressV6, _Mapping]] = ..., prefix_length: _Optional[int] = ..., gateway: _Optional[_Union[IpAddressV6, _Mapping]] = ...) -> None: ...
