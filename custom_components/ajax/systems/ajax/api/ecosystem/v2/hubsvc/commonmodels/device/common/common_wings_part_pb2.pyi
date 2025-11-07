from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonWingsPart(_message.Message):
    __slots__ = ("device_signal_level", "connection_status", "capabilities")
    class DataChannelConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_STATUS_UNSPECIFIED: _ClassVar[CommonWingsPart.DataChannelConnectionStatus]
        DATA_CHANNEL_CONNECTION_STATUS_NOT_OK: _ClassVar[CommonWingsPart.DataChannelConnectionStatus]
        DATA_CHANNEL_CONNECTION_STATUS_OK: _ClassVar[CommonWingsPart.DataChannelConnectionStatus]
    CONNECTION_STATUS_UNSPECIFIED: CommonWingsPart.DataChannelConnectionStatus
    DATA_CHANNEL_CONNECTION_STATUS_NOT_OK: CommonWingsPart.DataChannelConnectionStatus
    DATA_CHANNEL_CONNECTION_STATUS_OK: CommonWingsPart.DataChannelConnectionStatus
    class DataChannelDeviceSignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_SIGNAL_LEVEL_UNSPECIFIED: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_NO_SIGNAL: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_WEAK: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_NORMAL: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_STRONG: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_DISCONNECTED: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
        DEVICE_SIGNAL_LEVEL_POOR: _ClassVar[CommonWingsPart.DataChannelDeviceSignalLevel]
    DEVICE_SIGNAL_LEVEL_UNSPECIFIED: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_NO_SIGNAL: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_WEAK: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_NORMAL: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_STRONG: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_DISCONNECTED: CommonWingsPart.DataChannelDeviceSignalLevel
    DEVICE_SIGNAL_LEVEL_POOR: CommonWingsPart.DataChannelDeviceSignalLevel
    class Capabilities(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITIES_UNSPECIFIED: _ClassVar[CommonWingsPart.Capabilities]
        CAPABILITIES_WINGS: _ClassVar[CommonWingsPart.Capabilities]
    CAPABILITIES_UNSPECIFIED: CommonWingsPart.Capabilities
    CAPABILITIES_WINGS: CommonWingsPart.Capabilities
    DEVICE_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    device_signal_level: CommonWingsPart.DataChannelDeviceSignalLevel
    connection_status: CommonWingsPart.DataChannelConnectionStatus
    capabilities: _containers.RepeatedScalarFieldContainer[CommonWingsPart.Capabilities]
    def __init__(self, device_signal_level: _Optional[_Union[CommonWingsPart.DataChannelDeviceSignalLevel, str]] = ..., connection_status: _Optional[_Union[CommonWingsPart.DataChannelConnectionStatus, str]] = ..., capabilities: _Optional[_Iterable[_Union[CommonWingsPart.Capabilities, str]]] = ...) -> None: ...
