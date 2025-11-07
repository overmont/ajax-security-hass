from v3.mobilegwsvc.commonmodels.hub.device.light.properties import action_timer_pb2 as _action_timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RelayChannel(_message.Message):
    __slots__ = ("channel_id", "channel_name", "output_mode", "operating_mode", "malfunctions", "is_channel_enabled", "is_channel_on", "shutoff_timer", "is_transitioning")
    class OutputMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTPUT_MODE_UNSPECIFIED: _ClassVar[RelayChannel.OutputMode]
        OUTPUT_MODE_BLOCKING_ELEMENT: _ClassVar[RelayChannel.OutputMode]
        OUTPUT_MODE_ELECTRIC_LOCK: _ClassVar[RelayChannel.OutputMode]
        OUTPUT_MODE_RELAY: _ClassVar[RelayChannel.OutputMode]
    OUTPUT_MODE_UNSPECIFIED: RelayChannel.OutputMode
    OUTPUT_MODE_BLOCKING_ELEMENT: RelayChannel.OutputMode
    OUTPUT_MODE_ELECTRIC_LOCK: RelayChannel.OutputMode
    OUTPUT_MODE_RELAY: RelayChannel.OutputMode
    class OperatingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATING_MODE_UNSPECIFIED: _ClassVar[RelayChannel.OperatingMode]
        OPERATING_MODE_IMPULSE: _ClassVar[RelayChannel.OperatingMode]
        OPERATING_MODE_BISTABLE: _ClassVar[RelayChannel.OperatingMode]
    OPERATING_MODE_UNSPECIFIED: RelayChannel.OperatingMode
    OPERATING_MODE_IMPULSE: RelayChannel.OperatingMode
    OPERATING_MODE_BISTABLE: RelayChannel.OperatingMode
    class Malfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALFUNCTION_UNSPECIFIED: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_EXTREME_TEMPERATURE: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_HARDWARE_ERROR: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_LOW_VOLTAGE: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_HIGH_VOLTAGE: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_CURRENT_SHORT_CIRCUIT: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_HIGH_CURRENT_PROTECTION: _ClassVar[RelayChannel.Malfunction]
        MALFUNCTION_CONTACT_HANG: _ClassVar[RelayChannel.Malfunction]
    MALFUNCTION_UNSPECIFIED: RelayChannel.Malfunction
    MALFUNCTION_EXTREME_TEMPERATURE: RelayChannel.Malfunction
    MALFUNCTION_HARDWARE_ERROR: RelayChannel.Malfunction
    MALFUNCTION_LOW_VOLTAGE: RelayChannel.Malfunction
    MALFUNCTION_HIGH_VOLTAGE: RelayChannel.Malfunction
    MALFUNCTION_CURRENT_SHORT_CIRCUIT: RelayChannel.Malfunction
    MALFUNCTION_HIGH_CURRENT_PROTECTION: RelayChannel.Malfunction
    MALFUNCTION_CONTACT_HANG: RelayChannel.Malfunction
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_MODE_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_CHANNEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_CHANNEL_ON_FIELD_NUMBER: _ClassVar[int]
    SHUTOFF_TIMER_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSITIONING_FIELD_NUMBER: _ClassVar[int]
    channel_id: int
    channel_name: str
    output_mode: RelayChannel.OutputMode
    operating_mode: RelayChannel.OperatingMode
    malfunctions: _containers.RepeatedScalarFieldContainer[RelayChannel.Malfunction]
    is_channel_enabled: bool
    is_channel_on: bool
    shutoff_timer: _action_timer_pb2.ActionTimer
    is_transitioning: bool
    def __init__(self, channel_id: _Optional[int] = ..., channel_name: _Optional[str] = ..., output_mode: _Optional[_Union[RelayChannel.OutputMode, str]] = ..., operating_mode: _Optional[_Union[RelayChannel.OperatingMode, str]] = ..., malfunctions: _Optional[_Iterable[_Union[RelayChannel.Malfunction, str]]] = ..., is_channel_enabled: bool = ..., is_channel_on: bool = ..., shutoff_timer: _Optional[_Union[_action_timer_pb2.ActionTimer, _Mapping]] = ..., is_transitioning: bool = ...) -> None: ...
