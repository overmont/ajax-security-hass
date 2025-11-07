from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import image_analysis_mode_pb2 as _image_analysis_mode_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import detector_pb2 as _detector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectionSettings(_message.Message):
    __slots__ = ("pir", "motion", "object", "line_crossing")
    PIR_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSING_FIELD_NUMBER: _ClassVar[int]
    pir: PirDetectionSettings
    motion: MotionDetectionSettings
    object: ObjectDetectionSettings
    line_crossing: LineCrossingDetectionSettings
    def __init__(self, pir: _Optional[_Union[PirDetectionSettings, _Mapping]] = ..., motion: _Optional[_Union[MotionDetectionSettings, _Mapping]] = ..., object: _Optional[_Union[ObjectDetectionSettings, _Mapping]] = ..., line_crossing: _Optional[_Union[LineCrossingDetectionSettings, _Mapping]] = ...) -> None: ...

class PirDetectionSettings(_message.Message):
    __slots__ = ("enabled", "sensitivity")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    sensitivity: _detector_pb2.PirDetectorSettings.Sensitivity
    def __init__(self, enabled: bool = ..., sensitivity: _Optional[_Union[_detector_pb2.PirDetectorSettings.Sensitivity, str]] = ...) -> None: ...

class MotionDetectionSettings(_message.Message):
    __slots__ = ("enabled", "image_analysis_mode", "available_image_analysis_modes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ANALYSIS_MODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_IMAGE_ANALYSIS_MODES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    image_analysis_mode: _image_analysis_mode_pb2.ImageAnalysisMode
    available_image_analysis_modes: _containers.RepeatedScalarFieldContainer[_image_analysis_mode_pb2.ImageAnalysisMode]
    def __init__(self, enabled: bool = ..., image_analysis_mode: _Optional[_Union[_image_analysis_mode_pb2.ImageAnalysisMode, str]] = ..., available_image_analysis_modes: _Optional[_Iterable[_Union[_image_analysis_mode_pb2.ImageAnalysisMode, str]]] = ...) -> None: ...

class ObjectDetectionSettings(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class LineCrossingDetectionSettings(_message.Message):
    __slots__ = ("rule_count",)
    RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    rule_count: int
    def __init__(self, rule_count: _Optional[int] = ...) -> None: ...
