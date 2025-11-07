from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeNetworkConfigurationRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "network_interface_id", "ip_configuration_v4", "dns")
    class IpConfigurationV4(_message.Message):
        __slots__ = ("dhcp", "static")
        class DhcpConfigurationV4(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class StaticConfigurationV4(_message.Message):
            __slots__ = ("address", "netmask", "gateway")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            NETMASK_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            address: _types_pb2.IpAddressV4
            netmask: _types_pb2.IpAddressV4
            gateway: _types_pb2.IpAddressV4
            def __init__(self, address: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ..., netmask: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ..., gateway: _Optional[_Union[_types_pb2.IpAddressV4, _Mapping]] = ...) -> None: ...
        DHCP_FIELD_NUMBER: _ClassVar[int]
        STATIC_FIELD_NUMBER: _ClassVar[int]
        dhcp: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.DhcpConfigurationV4
        static: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.StaticConfigurationV4
        def __init__(self, dhcp: _Optional[_Union[SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.DhcpConfigurationV4, _Mapping]] = ..., static: _Optional[_Union[SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.StaticConfigurationV4, _Mapping]] = ...) -> None: ...
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_V4_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    network_interface_id: str
    ip_configuration_v4: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4
    dns: _containers.RepeatedCompositeFieldContainer[_types_pb2.IpAddress]
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., network_interface_id: _Optional[str] = ..., ip_configuration_v4: _Optional[_Union[SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4, _Mapping]] = ..., dns: _Optional[_Iterable[_Union[_types_pb2.IpAddress, _Mapping]]] = ...) -> None: ...
