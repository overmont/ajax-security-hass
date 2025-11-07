from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonFibraPart(_message.Message):
    __slots__ = ("bus_number", "scan_state", "blinking_cmd_state", "max_power_test_result")
    class ScanState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SCAN_STATE: _ClassVar[CommonFibraPart.ScanState]
        SCANNED: _ClassVar[CommonFibraPart.ScanState]
        BLINKING: _ClassVar[CommonFibraPart.ScanState]
    NO_SCAN_STATE: CommonFibraPart.ScanState
    SCANNED: CommonFibraPart.ScanState
    BLINKING: CommonFibraPart.ScanState
    class BlinkingCmdState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BLINKING_CMD_STATE: _ClassVar[CommonFibraPart.BlinkingCmdState]
        IDLE: _ClassVar[CommonFibraPart.BlinkingCmdState]
        NEED_STOP_BLINKING: _ClassVar[CommonFibraPart.BlinkingCmdState]
        NEED_BLINKING: _ClassVar[CommonFibraPart.BlinkingCmdState]
    NO_BLINKING_CMD_STATE: CommonFibraPart.BlinkingCmdState
    IDLE: CommonFibraPart.BlinkingCmdState
    NEED_STOP_BLINKING: CommonFibraPart.BlinkingCmdState
    NEED_BLINKING: CommonFibraPart.BlinkingCmdState
    class MaxPowerTestResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DATA: _ClassVar[CommonFibraPart.MaxPowerTestResult]
        OK: _ClassVar[CommonFibraPart.MaxPowerTestResult]
        POWER_IS_LOW: _ClassVar[CommonFibraPart.MaxPowerTestResult]
        POWER_IS_LOST: _ClassVar[CommonFibraPart.MaxPowerTestResult]
    NO_DATA: CommonFibraPart.MaxPowerTestResult
    OK: CommonFibraPart.MaxPowerTestResult
    POWER_IS_LOW: CommonFibraPart.MaxPowerTestResult
    POWER_IS_LOST: CommonFibraPart.MaxPowerTestResult
    BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SCAN_STATE_FIELD_NUMBER: _ClassVar[int]
    BLINKING_CMD_STATE_FIELD_NUMBER: _ClassVar[int]
    MAX_POWER_TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    bus_number: int
    scan_state: _containers.RepeatedScalarFieldContainer[CommonFibraPart.ScanState]
    blinking_cmd_state: CommonFibraPart.BlinkingCmdState
    max_power_test_result: CommonFibraPart.MaxPowerTestResult
    def __init__(self, bus_number: _Optional[int] = ..., scan_state: _Optional[_Iterable[_Union[CommonFibraPart.ScanState, str]]] = ..., blinking_cmd_state: _Optional[_Union[CommonFibraPart.BlinkingCmdState, str]] = ..., max_power_test_result: _Optional[_Union[CommonFibraPart.MaxPowerTestResult, str]] = ...) -> None: ...
