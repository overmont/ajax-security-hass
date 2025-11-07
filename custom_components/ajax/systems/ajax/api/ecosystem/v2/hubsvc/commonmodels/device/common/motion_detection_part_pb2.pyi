from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionDetectionPart(_message.Message):
    __slots__ = ("sensitivity", "sensitivity_capabilities", "always_active", "motion_detection_threshold", "motion_detection_threshold_capabilities", "capabilities")
    class AlwaysActive(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALWAYS_ACTIVE_UNSPECIFIED: _ClassVar[MotionDetectionPart.AlwaysActive]
        ALWAYS_ACTIVE_DISABLED: _ClassVar[MotionDetectionPart.AlwaysActive]
        ALWAYS_ACTIVE_ENABLED: _ClassVar[MotionDetectionPart.AlwaysActive]
    ALWAYS_ACTIVE_UNSPECIFIED: MotionDetectionPart.AlwaysActive
    ALWAYS_ACTIVE_DISABLED: MotionDetectionPart.AlwaysActive
    ALWAYS_ACTIVE_ENABLED: MotionDetectionPart.AlwaysActive
    class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SENSITIVITY_UNSPECIFIED: _ClassVar[MotionDetectionPart.Sensitivity]
        SENSITIVITY_LOW: _ClassVar[MotionDetectionPart.Sensitivity]
        SENSITIVITY_NORMAL: _ClassVar[MotionDetectionPart.Sensitivity]
        SENSITIVITY_HIGH: _ClassVar[MotionDetectionPart.Sensitivity]
        SENSITIVITY_VERY_HIGH: _ClassVar[MotionDetectionPart.Sensitivity]
    SENSITIVITY_UNSPECIFIED: MotionDetectionPart.Sensitivity
    SENSITIVITY_LOW: MotionDetectionPart.Sensitivity
    SENSITIVITY_NORMAL: MotionDetectionPart.Sensitivity
    SENSITIVITY_HIGH: MotionDetectionPart.Sensitivity
    SENSITIVITY_VERY_HIGH: MotionDetectionPart.Sensitivity
    class MotionDetectionThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_DETECTION_THRESHOLD_UNSPECIFIED: _ClassVar[MotionDetectionPart.MotionDetectionThreshold]
        MOTION_DETECTION_THRESHOLD_NORMAL: _ClassVar[MotionDetectionPart.MotionDetectionThreshold]
        MOTION_DETECTION_THRESHOLD_HIGH: _ClassVar[MotionDetectionPart.MotionDetectionThreshold]
    MOTION_DETECTION_THRESHOLD_UNSPECIFIED: MotionDetectionPart.MotionDetectionThreshold
    MOTION_DETECTION_THRESHOLD_NORMAL: MotionDetectionPart.MotionDetectionThreshold
    MOTION_DETECTION_THRESHOLD_HIGH: MotionDetectionPart.MotionDetectionThreshold
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[MotionDetectionPart.Capability]
        CAPABILITY_MOTION_DETECTION_THRESHOLD: _ClassVar[MotionDetectionPart.Capability]
    CAPABILITY_UNSPECIFIED: MotionDetectionPart.Capability
    CAPABILITY_MOTION_DETECTION_THRESHOLD: MotionDetectionPart.Capability
    class MotionDetectionPartSettings(_message.Message):
        __slots__ = ("motion_always_active", "sensitivity", "motion_detection_threshold")
        MOTION_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        MOTION_DETECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        motion_always_active: MotionDetectionPart.AlwaysActive
        sensitivity: MotionDetectionPart.Sensitivity
        motion_detection_threshold: MotionDetectionPart.MotionDetectionThreshold
        def __init__(self, motion_always_active: _Optional[_Union[MotionDetectionPart.AlwaysActive, str]] = ..., sensitivity: _Optional[_Union[MotionDetectionPart.Sensitivity, str]] = ..., motion_detection_threshold: _Optional[_Union[MotionDetectionPart.MotionDetectionThreshold, str]] = ...) -> None: ...
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_THRESHOLD_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    sensitivity: MotionDetectionPart.Sensitivity
    sensitivity_capabilities: _containers.RepeatedScalarFieldContainer[MotionDetectionPart.Sensitivity]
    always_active: MotionDetectionPart.AlwaysActive
    motion_detection_threshold: MotionDetectionPart.MotionDetectionThreshold
    motion_detection_threshold_capabilities: _containers.RepeatedScalarFieldContainer[MotionDetectionPart.MotionDetectionThreshold]
    capabilities: _containers.RepeatedScalarFieldContainer[MotionDetectionPart.Capability]
    def __init__(self, sensitivity: _Optional[_Union[MotionDetectionPart.Sensitivity, str]] = ..., sensitivity_capabilities: _Optional[_Iterable[_Union[MotionDetectionPart.Sensitivity, str]]] = ..., always_active: _Optional[_Union[MotionDetectionPart.AlwaysActive, str]] = ..., motion_detection_threshold: _Optional[_Union[MotionDetectionPart.MotionDetectionThreshold, str]] = ..., motion_detection_threshold_capabilities: _Optional[_Iterable[_Union[MotionDetectionPart.MotionDetectionThreshold, str]]] = ..., capabilities: _Optional[_Iterable[_Union[MotionDetectionPart.Capability, str]]] = ...) -> None: ...
