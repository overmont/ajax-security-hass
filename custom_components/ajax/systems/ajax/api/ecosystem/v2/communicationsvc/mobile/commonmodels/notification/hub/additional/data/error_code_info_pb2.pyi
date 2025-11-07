from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCodeInfo(_message.Message):
    __slots__ = ("water_stop_error_code_info",)
    class WaterStopErrorCodeInfo(_message.Message):
        __slots__ = ("water_stop_error_codes",)
        class WaterStopErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WATER_STOP_ERROR_CODE_UNSPECIFIED: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_DEVICE_OFFLINE: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_IN_BYPASS_MODE: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_VALVE_STATE_CLOSE: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_VALVE_STATE_UNKNOWN: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_BATTERY_ERROR: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_LOW_BATTERY: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_TAMPER_OPEN: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_NO_RESPONSE: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_FIRE_ALARM: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_DEVICE_BUSY: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
            WATER_STOP_ERROR_CODE_GENERIC: _ClassVar[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
        WATER_STOP_ERROR_CODE_UNSPECIFIED: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_DEVICE_OFFLINE: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_IN_BYPASS_MODE: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_VALVE_STATE_CLOSE: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_VALVE_STATE_UNKNOWN: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_BATTERY_ERROR: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_LOW_BATTERY: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_TAMPER_OPEN: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_NO_RESPONSE: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_FIRE_ALARM: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_DEVICE_BUSY: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODE_GENERIC: ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode
        WATER_STOP_ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
        water_stop_error_codes: _containers.RepeatedScalarFieldContainer[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode]
        def __init__(self, water_stop_error_codes: _Optional[_Iterable[_Union[ErrorCodeInfo.WaterStopErrorCodeInfo.WaterStopErrorCode, str]]] = ...) -> None: ...
    WATER_STOP_ERROR_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
    water_stop_error_code_info: ErrorCodeInfo.WaterStopErrorCodeInfo
    def __init__(self, water_stop_error_code_info: _Optional[_Union[ErrorCodeInfo.WaterStopErrorCodeInfo, _Mapping]] = ...) -> None: ...
