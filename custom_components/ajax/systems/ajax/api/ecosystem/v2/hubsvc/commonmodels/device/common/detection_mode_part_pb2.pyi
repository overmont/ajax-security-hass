from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectionModePart(_message.Message):
    __slots__ = ("correlation_processing", "detection_distance", "shatter_state", "capabilities")
    class CorrelationProcessing(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CORRELATION_PROCESSING_STATUS_UNSPECIFIED: _ClassVar[DetectionModePart.CorrelationProcessing]
        CORRELATION_PROCESSING_STATUS_NOT_ACTIVE: _ClassVar[DetectionModePart.CorrelationProcessing]
        CORRELATION_PROCESSING_STATUS_ACTIVE: _ClassVar[DetectionModePart.CorrelationProcessing]
    CORRELATION_PROCESSING_STATUS_UNSPECIFIED: DetectionModePart.CorrelationProcessing
    CORRELATION_PROCESSING_STATUS_NOT_ACTIVE: DetectionModePart.CorrelationProcessing
    CORRELATION_PROCESSING_STATUS_ACTIVE: DetectionModePart.CorrelationProcessing
    class DetectionDistance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTION_DISTANCE_UNSPECIFIED: _ClassVar[DetectionModePart.DetectionDistance]
        DETECTION_DISTANCE_PET_IMMUNE: _ClassVar[DetectionModePart.DetectionDistance]
        DETECTION_DISTANCE_NEAR: _ClassVar[DetectionModePart.DetectionDistance]
        DETECTION_DISTANCE_FAR: _ClassVar[DetectionModePart.DetectionDistance]
    DETECTION_DISTANCE_UNSPECIFIED: DetectionModePart.DetectionDistance
    DETECTION_DISTANCE_PET_IMMUNE: DetectionModePart.DetectionDistance
    DETECTION_DISTANCE_NEAR: DetectionModePart.DetectionDistance
    DETECTION_DISTANCE_FAR: DetectionModePart.DetectionDistance
    class ShatterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHATTER_STATE_UNSPECIFIED: _ClassVar[DetectionModePart.ShatterState]
        SHATTER_STATE_NORMAL: _ClassVar[DetectionModePart.ShatterState]
        SHATTER_STATE_PET_IMMUNE: _ClassVar[DetectionModePart.ShatterState]
    SHATTER_STATE_UNSPECIFIED: DetectionModePart.ShatterState
    SHATTER_STATE_NORMAL: DetectionModePart.ShatterState
    SHATTER_STATE_PET_IMMUNE: DetectionModePart.ShatterState
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[DetectionModePart.Capability]
        CAPABILITY_SETTINGS_SUPPORTED: _ClassVar[DetectionModePart.Capability]
    CAPABILITY_UNSPECIFIED: DetectionModePart.Capability
    CAPABILITY_SETTINGS_SUPPORTED: DetectionModePart.Capability
    class DetectionModePartSettings(_message.Message):
        __slots__ = ("correlation_processing", "detection_distance")
        CORRELATION_PROCESSING_FIELD_NUMBER: _ClassVar[int]
        DETECTION_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        correlation_processing: DetectionModePart.CorrelationProcessing
        detection_distance: DetectionModePart.DetectionDistance
        def __init__(self, correlation_processing: _Optional[_Union[DetectionModePart.CorrelationProcessing, str]] = ..., detection_distance: _Optional[_Union[DetectionModePart.DetectionDistance, str]] = ...) -> None: ...
    CORRELATION_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    DETECTION_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SHATTER_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    correlation_processing: DetectionModePart.CorrelationProcessing
    detection_distance: DetectionModePart.DetectionDistance
    shatter_state: DetectionModePart.ShatterState
    capabilities: _containers.RepeatedScalarFieldContainer[DetectionModePart.Capability]
    def __init__(self, correlation_processing: _Optional[_Union[DetectionModePart.CorrelationProcessing, str]] = ..., detection_distance: _Optional[_Union[DetectionModePart.DetectionDistance, str]] = ..., shatter_state: _Optional[_Union[DetectionModePart.ShatterState, str]] = ..., capabilities: _Optional[_Iterable[_Union[DetectionModePart.Capability, str]]] = ...) -> None: ...
