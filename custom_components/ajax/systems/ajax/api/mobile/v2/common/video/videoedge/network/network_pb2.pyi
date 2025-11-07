from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = ("server_ping_interval", "connection_failure_alarm_delay", "ethernet", "wifi", "configuration_status")
    SERVER_PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FAILURE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    server_ping_interval: _duration_pb2.Duration
    connection_failure_alarm_delay: _duration_pb2.Duration
    ethernet: NetworkTechnology
    wifi: NetworkTechnology
    configuration_status: NetworkConfigurationStatus
    def __init__(self, server_ping_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., connection_failure_alarm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ethernet: _Optional[_Union[NetworkTechnology, _Mapping]] = ..., wifi: _Optional[_Union[NetworkTechnology, _Mapping]] = ..., configuration_status: _Optional[_Union[NetworkConfigurationStatus, _Mapping]] = ...) -> None: ...

class NetworkTechnology(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class NetworkConfigurationStatus(_message.Message):
    __slots__ = ("request_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationStatus.State]
        OK: _ClassVar[NetworkConfigurationStatus.State]
        FAILED: _ClassVar[NetworkConfigurationStatus.State]
    NONE: NetworkConfigurationStatus.State
    OK: NetworkConfigurationStatus.State
    FAILED: NetworkConfigurationStatus.State
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    state: NetworkConfigurationStatus.State
    def __init__(self, request_id: _Optional[str] = ..., state: _Optional[_Union[NetworkConfigurationStatus.State, str]] = ...) -> None: ...
