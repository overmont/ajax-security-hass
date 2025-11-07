from systems.ajax.api.mobile.v2.common.video.videoedge.network import network_interface_pb2 as _network_interface_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScanVideoEdgeWifiResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("network_interfaces_snapshot", "network_interfaces_replaced", "network_interfaces_removed")
        class NetworkInterfacesSnapshot(_message.Message):
            __slots__ = ("network_interfaces",)
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            network_interfaces: _containers.RepeatedCompositeFieldContainer[_network_interface_pb2.NetworkInterface]
            def __init__(self, network_interfaces: _Optional[_Iterable[_Union[_network_interface_pb2.NetworkInterface, _Mapping]]] = ...) -> None: ...
        class NetworkInterfacesReplaced(_message.Message):
            __slots__ = ("network_interfaces",)
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            network_interfaces: _containers.RepeatedCompositeFieldContainer[_network_interface_pb2.NetworkInterface]
            def __init__(self, network_interfaces: _Optional[_Iterable[_Union[_network_interface_pb2.NetworkInterface, _Mapping]]] = ...) -> None: ...
        class NetworkInterfacesRemoved(_message.Message):
            __slots__ = ("network_interface_ids",)
            NETWORK_INTERFACE_IDS_FIELD_NUMBER: _ClassVar[int]
            network_interface_ids: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, network_interface_ids: _Optional[_Iterable[str]] = ...) -> None: ...
        NETWORK_INTERFACES_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACES_REPLACED_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACES_REMOVED_FIELD_NUMBER: _ClassVar[int]
        network_interfaces_snapshot: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesSnapshot
        network_interfaces_replaced: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesReplaced
        network_interfaces_removed: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesRemoved
        def __init__(self, network_interfaces_snapshot: _Optional[_Union[ScanVideoEdgeWifiResponse.Success.NetworkInterfacesSnapshot, _Mapping]] = ..., network_interfaces_replaced: _Optional[_Union[ScanVideoEdgeWifiResponse.Success.NetworkInterfacesReplaced, _Mapping]] = ..., network_interfaces_removed: _Optional[_Union[ScanVideoEdgeWifiResponse.Success.NetworkInterfacesRemoved, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_armed", "video_edge_not_found", "video_edge_is_offline", "unimplemented_video_edge_command", "hub_is_busy")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unimplemented_video_edge_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_is_busy: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ScanVideoEdgeWifiResponse.Success
    failure: ScanVideoEdgeWifiResponse.Failure
    def __init__(self, success: _Optional[_Union[ScanVideoEdgeWifiResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ScanVideoEdgeWifiResponse.Failure, _Mapping]] = ...) -> None: ...
