from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorSettings(_message.Message):
    __slots__ = ("enabled", "fake_settings", "motion_settings", "object_settings", "pir_settings")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAKE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MOTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PIR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    fake_settings: FakeDetectorSettings
    motion_settings: MotionDetectorSettings
    object_settings: ObjectDetectorSettings
    pir_settings: PirDetectorSettings
    def __init__(self, enabled: bool = ..., fake_settings: _Optional[_Union[FakeDetectorSettings, _Mapping]] = ..., motion_settings: _Optional[_Union[MotionDetectorSettings, _Mapping]] = ..., object_settings: _Optional[_Union[ObjectDetectorSettings, _Mapping]] = ..., pir_settings: _Optional[_Union[PirDetectorSettings, _Mapping]] = ...) -> None: ...

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
        __slots__ = ("sensitivity", "min_count")
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        MIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        sensitivity: int
        min_count: int
        def __init__(self, sensitivity: _Optional[int] = ..., min_count: _Optional[int] = ...) -> None: ...
    MASK_FIELD_NUMBER: _ClassVar[int]
    mask: MotionDetectorSettings.Mask
    def __init__(self, mask: _Optional[_Union[MotionDetectorSettings.Mask, _Mapping]] = ...) -> None: ...

class ObjectDetectorSettings(_message.Message):
    __slots__ = ("class_settings",)
    class ClassSettings(_message.Message):
        __slots__ = ("object_class", "enabled", "sensitivity")
        class ObjectClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OBJECT_CLASS_UNSPECIFIED: _ClassVar[ObjectDetectorSettings.ClassSettings.ObjectClass]
            OBJECT_CLASS_PERSON: _ClassVar[ObjectDetectorSettings.ClassSettings.ObjectClass]
            OBJECT_CLASS_PET: _ClassVar[ObjectDetectorSettings.ClassSettings.ObjectClass]
            OBJECT_CLASS_VEHICLE: _ClassVar[ObjectDetectorSettings.ClassSettings.ObjectClass]
        OBJECT_CLASS_UNSPECIFIED: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_PERSON: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_PET: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_VEHICLE: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        object_class: ObjectDetectorSettings.ClassSettings.ObjectClass
        enabled: bool
        sensitivity: int
        def __init__(self, object_class: _Optional[_Union[ObjectDetectorSettings.ClassSettings.ObjectClass, str]] = ..., enabled: bool = ..., sensitivity: _Optional[int] = ...) -> None: ...
    CLASS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    class_settings: _containers.RepeatedCompositeFieldContainer[ObjectDetectorSettings.ClassSettings]
    def __init__(self, class_settings: _Optional[_Iterable[_Union[ObjectDetectorSettings.ClassSettings, _Mapping]]] = ...) -> None: ...
