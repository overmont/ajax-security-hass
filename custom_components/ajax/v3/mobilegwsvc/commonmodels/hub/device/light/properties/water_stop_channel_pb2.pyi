from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WaterStopChannel(_message.Message):
    __slots__ = ("id", "state", "is_transitioning", "malfunctions")
    class Malfunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALFUNCTION_UNSPECIFIED: _ClassVar[WaterStopChannel.Malfunction]
        MALFUNCTION_BATTERY_PLACEMENT_ERROR: _ClassVar[WaterStopChannel.Malfunction]
        MALFUNCTION_IS_STUCK: _ClassVar[WaterStopChannel.Malfunction]
        MALFUNCTION_FINISH_SETUP_REQUIRED: _ClassVar[WaterStopChannel.Malfunction]
        MALFUNCTION_BATTERY_LOW_ERROR: _ClassVar[WaterStopChannel.Malfunction]
    MALFUNCTION_UNSPECIFIED: WaterStopChannel.Malfunction
    MALFUNCTION_BATTERY_PLACEMENT_ERROR: WaterStopChannel.Malfunction
    MALFUNCTION_IS_STUCK: WaterStopChannel.Malfunction
    MALFUNCTION_FINISH_SETUP_REQUIRED: WaterStopChannel.Malfunction
    MALFUNCTION_BATTERY_LOW_ERROR: WaterStopChannel.Malfunction
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WaterStopChannel.State]
        STATE_UNKNOWN: _ClassVar[WaterStopChannel.State]
        STATE_OFF: _ClassVar[WaterStopChannel.State]
        STATE_ON: _ClassVar[WaterStopChannel.State]
    STATE_UNSPECIFIED: WaterStopChannel.State
    STATE_UNKNOWN: WaterStopChannel.State
    STATE_OFF: WaterStopChannel.State
    STATE_ON: WaterStopChannel.State
    class ChannelId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_ID_UNSPECIFIED: _ClassVar[WaterStopChannel.ChannelId]
        CHANNEL_ID_1: _ClassVar[WaterStopChannel.ChannelId]
    CHANNEL_ID_UNSPECIFIED: WaterStopChannel.ChannelId
    CHANNEL_ID_1: WaterStopChannel.ChannelId
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSITIONING_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    id: WaterStopChannel.ChannelId
    state: WaterStopChannel.State
    is_transitioning: bool
    malfunctions: _containers.RepeatedScalarFieldContainer[WaterStopChannel.Malfunction]
    def __init__(self, id: _Optional[_Union[WaterStopChannel.ChannelId, str]] = ..., state: _Optional[_Union[WaterStopChannel.State, str]] = ..., is_transitioning: bool = ..., malfunctions: _Optional[_Iterable[_Union[WaterStopChannel.Malfunction, str]]] = ...) -> None: ...
