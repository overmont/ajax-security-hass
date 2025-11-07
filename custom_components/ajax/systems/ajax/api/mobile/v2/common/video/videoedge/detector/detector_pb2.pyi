from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DT_UNKNOWN: _ClassVar[DetectorType]
    DT_FAKE: _ClassVar[DetectorType]
    DT_MOTION: _ClassVar[DetectorType]
    DT_OBJECT: _ClassVar[DetectorType]
    DT_PIR: _ClassVar[DetectorType]
    DT_RING: _ClassVar[DetectorType]

class DetectorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DK_UNKNOWN: _ClassVar[DetectorKind]
    DK_HARDWARE: _ClassVar[DetectorKind]
    DK_SOFTWARE: _ClassVar[DetectorKind]

class DetectorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DS_NONE: _ClassVar[DetectorState]
    DS_ONLINE: _ClassVar[DetectorState]
DT_UNKNOWN: DetectorType
DT_FAKE: DetectorType
DT_MOTION: DetectorType
DT_OBJECT: DetectorType
DT_PIR: DetectorType
DT_RING: DetectorType
DK_UNKNOWN: DetectorKind
DK_HARDWARE: DetectorKind
DK_SOFTWARE: DetectorKind
DS_NONE: DetectorState
DS_ONLINE: DetectorState

class Detector(_message.Message):
    __slots__ = ("guid", "type", "kind", "channel_guid", "enabled", "state", "settings")
    GUID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    guid: str
    type: DetectorType
    kind: DetectorKind
    channel_guid: str
    enabled: bool
    state: _containers.RepeatedScalarFieldContainer[DetectorState]
    settings: DetectorSettings
    def __init__(self, guid: _Optional[str] = ..., type: _Optional[_Union[DetectorType, str]] = ..., kind: _Optional[_Union[DetectorKind, str]] = ..., channel_guid: _Optional[str] = ..., enabled: bool = ..., state: _Optional[_Iterable[_Union[DetectorState, str]]] = ..., settings: _Optional[_Union[DetectorSettings, _Mapping]] = ...) -> None: ...

class DetectorSettings(_message.Message):
    __slots__ = ("fake_settings", "motion_settings", "object_settings", "pir_settings")
    FAKE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MOTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PIR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    fake_settings: FakeDetectorSettings
    motion_settings: MotionDetectorSettings
    object_settings: ObjectDetectorSettings
    pir_settings: PirDetectorSettings
    def __init__(self, fake_settings: _Optional[_Union[FakeDetectorSettings, _Mapping]] = ..., motion_settings: _Optional[_Union[MotionDetectorSettings, _Mapping]] = ..., object_settings: _Optional[_Union[ObjectDetectorSettings, _Mapping]] = ..., pir_settings: _Optional[_Union[PirDetectorSettings, _Mapping]] = ...) -> None: ...

class PirDetectorSettings(_message.Message):
    __slots__ = ("pir_details_sensitivity",)
    class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SENSITIVITY_UNSPECIFIED: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_LOW: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_MID: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_HIGH: _ClassVar[PirDetectorSettings.Sensitivity]
    SENSITIVITY_UNSPECIFIED: PirDetectorSettings.Sensitivity
    SENSITIVITY_LOW: PirDetectorSettings.Sensitivity
    SENSITIVITY_MID: PirDetectorSettings.Sensitivity
    SENSITIVITY_HIGH: PirDetectorSettings.Sensitivity
    class PirDetailsSensitivity(_message.Message):
        __slots__ = ("sensitivity",)
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        sensitivity: PirDetectorSettings.Sensitivity
        def __init__(self, sensitivity: _Optional[_Union[PirDetectorSettings.Sensitivity, str]] = ...) -> None: ...
    PIR_DETAILS_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    pir_details_sensitivity: PirDetectorSettings.PirDetailsSensitivity
    def __init__(self, pir_details_sensitivity: _Optional[_Union[PirDetectorSettings.PirDetailsSensitivity, _Mapping]] = ...) -> None: ...

class FakeDetectorSettings(_message.Message):
    __slots__ = ("loop_duration", "with_ts_text")
    LOOP_DURATION_FIELD_NUMBER: _ClassVar[int]
    WITH_TS_TEXT_FIELD_NUMBER: _ClassVar[int]
    loop_duration: _duration_pb2.Duration
    with_ts_text: bool
    def __init__(self, loop_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., with_ts_text: bool = ...) -> None: ...

class MotionDetectorSettings(_message.Message):
    __slots__ = ("mask",)
    class Mask(_message.Message):
        __slots__ = ("sensitivity", "width", "height", "data", "min_count")
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        MIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        sensitivity: int
        width: int
        height: int
        data: bytes
        min_count: int
        def __init__(self, sensitivity: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ..., min_count: _Optional[int] = ...) -> None: ...
    MASK_FIELD_NUMBER: _ClassVar[int]
    mask: MotionDetectorSettings.Mask
    def __init__(self, mask: _Optional[_Union[MotionDetectorSettings.Mask, _Mapping]] = ...) -> None: ...

class ObjectDetectorSettings(_message.Message):
    __slots__ = ("zone_mask", "class_settings")
    class ClassSettings(_message.Message):
        __slots__ = ("object_class", "enabled", "confidence", "sensitivity")
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        object_class: _types_pb2.ObjectClass
        enabled: bool
        confidence: int
        sensitivity: int
        def __init__(self, object_class: _Optional[_Union[_types_pb2.ObjectClass, str]] = ..., enabled: bool = ..., confidence: _Optional[int] = ..., sensitivity: _Optional[int] = ...) -> None: ...
    ZONE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLASS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    zone_mask: _types_pb2.Mask
    class_settings: _containers.RepeatedCompositeFieldContainer[ObjectDetectorSettings.ClassSettings]
    def __init__(self, zone_mask: _Optional[_Union[_types_pb2.Mask, _Mapping]] = ..., class_settings: _Optional[_Iterable[_Union[ObjectDetectorSettings.ClassSettings, _Mapping]]] = ...) -> None: ...
