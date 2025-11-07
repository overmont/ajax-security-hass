from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceArmingMode(_message.Message):
    __slots__ = ("instant", "entry_exit", "follower", "disabled")
    class Instant(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class EntryExit(_message.Message):
        __slots__ = ("arm_delay", "alarm_delay", "night_mode_arm_delay", "night_mode_alarm_delay")
        ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        NIGHT_MODE_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        NIGHT_MODE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        arm_delay: _duration_pb2.Duration
        alarm_delay: _duration_pb2.Duration
        night_mode_arm_delay: _duration_pb2.Duration
        night_mode_alarm_delay: _duration_pb2.Duration
        def __init__(self, arm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., alarm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., night_mode_arm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., night_mode_alarm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Follower(_message.Message):
        __slots__ = ("night_mode_alarm_delay",)
        NIGHT_MODE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        night_mode_alarm_delay: _duration_pb2.Duration
        def __init__(self, night_mode_alarm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Disabled(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    INSTANT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_EXIT_FIELD_NUMBER: _ClassVar[int]
    FOLLOWER_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    instant: DeviceArmingMode.Instant
    entry_exit: DeviceArmingMode.EntryExit
    follower: DeviceArmingMode.Follower
    disabled: DeviceArmingMode.Disabled
    def __init__(self, instant: _Optional[_Union[DeviceArmingMode.Instant, _Mapping]] = ..., entry_exit: _Optional[_Union[DeviceArmingMode.EntryExit, _Mapping]] = ..., follower: _Optional[_Union[DeviceArmingMode.Follower, _Mapping]] = ..., disabled: _Optional[_Union[DeviceArmingMode.Disabled, _Mapping]] = ...) -> None: ...
