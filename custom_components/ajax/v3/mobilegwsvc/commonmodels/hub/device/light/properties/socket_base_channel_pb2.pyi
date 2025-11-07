from v3.mobilegwsvc.commonmodels.hub.device.light.properties import action_timer_pb2 as _action_timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SocketBaseChannel(_message.Message):
    __slots__ = ("id", "operating_mode", "malfunctions", "state", "shutoff_timer", "is_transitioning")
    class OperatingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATING_MODE_UNSPECIFIED: _ClassVar[SocketBaseChannel.OperatingMode]
        OPERATING_MODE_IMPULSE: _ClassVar[SocketBaseChannel.OperatingMode]
        OPERATING_MODE_BISTABLE: _ClassVar[SocketBaseChannel.OperatingMode]
    OPERATING_MODE_UNSPECIFIED: SocketBaseChannel.OperatingMode
    OPERATING_MODE_IMPULSE: SocketBaseChannel.OperatingMode
    OPERATING_MODE_BISTABLE: SocketBaseChannel.OperatingMode
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[SocketBaseChannel.State]
        STATE_OFF: _ClassVar[SocketBaseChannel.State]
        STATE_ON: _ClassVar[SocketBaseChannel.State]
    STATE_UNSPECIFIED: SocketBaseChannel.State
    STATE_OFF: SocketBaseChannel.State
    STATE_ON: SocketBaseChannel.State
    class ChannelId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_ID_UNSPECIFIED: _ClassVar[SocketBaseChannel.ChannelId]
        CHANNEL_ID_1: _ClassVar[SocketBaseChannel.ChannelId]
    CHANNEL_ID_UNSPECIFIED: SocketBaseChannel.ChannelId
    CHANNEL_ID_1: SocketBaseChannel.ChannelId
    class Malfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALFUNCTION_UNSPECIFIED: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_LOW_VOLTAGE: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_HIGH_VOLTAGE: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_HIGH_CURRENT_PROTECTION: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_HIGH_TEMPERATURE_DETECTED: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_RELAY_STUCK: _ClassVar[SocketBaseChannel.Malfunction]
        MALFUNCTION_ARC_SPARK_DETECTED: _ClassVar[SocketBaseChannel.Malfunction]
    MALFUNCTION_UNSPECIFIED: SocketBaseChannel.Malfunction
    MALFUNCTION_LOW_VOLTAGE: SocketBaseChannel.Malfunction
    MALFUNCTION_HIGH_VOLTAGE: SocketBaseChannel.Malfunction
    MALFUNCTION_HIGH_CURRENT_PROTECTION: SocketBaseChannel.Malfunction
    MALFUNCTION_HIGH_TEMPERATURE_DETECTED: SocketBaseChannel.Malfunction
    MALFUNCTION_RELAY_STUCK: SocketBaseChannel.Malfunction
    MALFUNCTION_ARC_SPARK_DETECTED: SocketBaseChannel.Malfunction
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATING_MODE_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SHUTOFF_TIMER_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSITIONING_FIELD_NUMBER: _ClassVar[int]
    id: SocketBaseChannel.ChannelId
    operating_mode: SocketBaseChannel.OperatingMode
    malfunctions: _containers.RepeatedScalarFieldContainer[SocketBaseChannel.Malfunction]
    state: SocketBaseChannel.State
    shutoff_timer: _action_timer_pb2.ActionTimer
    is_transitioning: bool
    def __init__(self, id: _Optional[_Union[SocketBaseChannel.ChannelId, str]] = ..., operating_mode: _Optional[_Union[SocketBaseChannel.OperatingMode, str]] = ..., malfunctions: _Optional[_Iterable[_Union[SocketBaseChannel.Malfunction, str]]] = ..., state: _Optional[_Union[SocketBaseChannel.State, str]] = ..., shutoff_timer: _Optional[_Union[_action_timer_pb2.ActionTimer, _Mapping]] = ..., is_transitioning: bool = ...) -> None: ...
