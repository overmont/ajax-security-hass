from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorsPowerLinePart(_message.Message):
    __slots__ = ("detectors_power_lines",)
    class DetectorsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTORS_TYPE_UNSPECIFIED: _ClassVar[DetectorsPowerLinePart.DetectorsType]
        DETECTORS_TYPE_COMMON: _ClassVar[DetectorsPowerLinePart.DetectorsType]
        DETECTORS_TYPE_FIRE: _ClassVar[DetectorsPowerLinePart.DetectorsType]
    DETECTORS_TYPE_UNSPECIFIED: DetectorsPowerLinePart.DetectorsType
    DETECTORS_TYPE_COMMON: DetectorsPowerLinePart.DetectorsType
    DETECTORS_TYPE_FIRE: DetectorsPowerLinePart.DetectorsType
    class PowerLineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_LINE_STATUS_UNSPECIFIED: _ClassVar[DetectorsPowerLinePart.PowerLineStatus]
        POWER_LINE_STATUS_OK: _ClassVar[DetectorsPowerLinePart.PowerLineStatus]
        POWER_LINE_STATUS_SHORTED_OUT: _ClassVar[DetectorsPowerLinePart.PowerLineStatus]
        POWER_LINE_STATUS_LOW_VOLTAGE: _ClassVar[DetectorsPowerLinePart.PowerLineStatus]
    POWER_LINE_STATUS_UNSPECIFIED: DetectorsPowerLinePart.PowerLineStatus
    POWER_LINE_STATUS_OK: DetectorsPowerLinePart.PowerLineStatus
    POWER_LINE_STATUS_SHORTED_OUT: DetectorsPowerLinePart.PowerLineStatus
    POWER_LINE_STATUS_LOW_VOLTAGE: DetectorsPowerLinePart.PowerLineStatus
    class DetectorsPowerLine(_message.Message):
        __slots__ = ("detectors_type", "power_line_status")
        DETECTORS_TYPE_FIELD_NUMBER: _ClassVar[int]
        POWER_LINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        detectors_type: DetectorsPowerLinePart.DetectorsType
        power_line_status: DetectorsPowerLinePart.PowerLineStatus
        def __init__(self, detectors_type: _Optional[_Union[DetectorsPowerLinePart.DetectorsType, str]] = ..., power_line_status: _Optional[_Union[DetectorsPowerLinePart.PowerLineStatus, str]] = ...) -> None: ...
    DETECTORS_POWER_LINES_FIELD_NUMBER: _ClassVar[int]
    detectors_power_lines: _containers.RepeatedCompositeFieldContainer[DetectorsPowerLinePart.DetectorsPowerLine]
    def __init__(self, detectors_power_lines: _Optional[_Iterable[_Union[DetectorsPowerLinePart.DetectorsPowerLine, _Mapping]]] = ...) -> None: ...
