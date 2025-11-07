from google.protobuf import duration_pb2 as _duration_pb2
from ajax.video.v1.types import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Dummy(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Batch(_message.Message):
    __slots__ = ("type", "frames")
    class Frame(_message.Message):
        __slots__ = ("ts", "tz_offset", "data")
        TS_FIELD_NUMBER: _ClassVar[int]
        TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ts: int
        tz_offset: int
        data: bytes
        def __init__(self, ts: _Optional[int] = ..., tz_offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    type: str
    frames: _containers.RepeatedCompositeFieldContainer[Batch.Frame]
    def __init__(self, type: _Optional[str] = ..., frames: _Optional[_Iterable[_Union[Batch.Frame, _Mapping]]] = ...) -> None: ...

class Figures(_message.Message):
    __slots__ = ("type", "items", "duration")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Figures.Type]
        DEBUG: _ClassVar[Figures.Type]
        SUBTITLES: _ClassVar[Figures.Type]
        MOTION_DETECTOR: _ClassVar[Figures.Type]
        OBJECT_DETECTOR: _ClassVar[Figures.Type]
    UNKNOWN: Figures.Type
    DEBUG: Figures.Type
    SUBTITLES: Figures.Type
    MOTION_DETECTOR: Figures.Type
    OBJECT_DETECTOR: Figures.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    type: Figures.Type
    items: _containers.RepeatedCompositeFieldContainer[Figure]
    duration: _duration_pb2.Duration
    def __init__(self, type: _Optional[_Union[Figures.Type, str]] = ..., items: _Optional[_Iterable[_Union[Figure, _Mapping]]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Figure(_message.Message):
    __slots__ = ("color", "thickness", "alpha", "rect", "label", "line", "rect_with_text", "mask")
    class Thickness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        T_NONE: _ClassVar[Figure.Thickness]
        T_THIN: _ClassVar[Figure.Thickness]
        T_NORMAL: _ClassVar[Figure.Thickness]
        T_THICK: _ClassVar[Figure.Thickness]
    T_NONE: Figure.Thickness
    T_THIN: Figure.Thickness
    T_NORMAL: Figure.Thickness
    T_THICK: Figure.Thickness
    COLOR_FIELD_NUMBER: _ClassVar[int]
    THICKNESS_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    RECT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    RECT_WITH_TEXT_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    color: _types_pb2.Color
    thickness: Figure.Thickness
    alpha: float
    rect: _types_pb2.Rect2f
    label: Label
    line: _types_pb2.Line2f
    rect_with_text: RectWithText
    mask: Mask
    def __init__(self, color: _Optional[_Union[_types_pb2.Color, str]] = ..., thickness: _Optional[_Union[Figure.Thickness, str]] = ..., alpha: _Optional[float] = ..., rect: _Optional[_Union[_types_pb2.Rect2f, _Mapping]] = ..., label: _Optional[_Union[Label, _Mapping]] = ..., line: _Optional[_Union[_types_pb2.Line2f, _Mapping]] = ..., rect_with_text: _Optional[_Union[RectWithText, _Mapping]] = ..., mask: _Optional[_Union[Mask, _Mapping]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ("extents", "text")
    EXTENTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    extents: _types_pb2.Rect2f
    text: str
    def __init__(self, extents: _Optional[_Union[_types_pb2.Rect2f, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class RectWithText(_message.Message):
    __slots__ = ("rect", "text", "alignment")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        A_NONE: _ClassVar[RectWithText.Alignment]
        A_TOP_LEFT: _ClassVar[RectWithText.Alignment]
        A_TOP_CENTER: _ClassVar[RectWithText.Alignment]
        A_TOP_RIGHT: _ClassVar[RectWithText.Alignment]
        A_CENTER_LEFT: _ClassVar[RectWithText.Alignment]
        A_CENTER_CENTER: _ClassVar[RectWithText.Alignment]
        A_CENTER_RIGHT: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_LEFT: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_CENTER: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_RIGHT: _ClassVar[RectWithText.Alignment]
    A_NONE: RectWithText.Alignment
    A_TOP_LEFT: RectWithText.Alignment
    A_TOP_CENTER: RectWithText.Alignment
    A_TOP_RIGHT: RectWithText.Alignment
    A_CENTER_LEFT: RectWithText.Alignment
    A_CENTER_CENTER: RectWithText.Alignment
    A_CENTER_RIGHT: RectWithText.Alignment
    A_BOTTOM_LEFT: RectWithText.Alignment
    A_BOTTOM_CENTER: RectWithText.Alignment
    A_BOTTOM_RIGHT: RectWithText.Alignment
    RECT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    rect: _types_pb2.Rect2f
    text: str
    alignment: RectWithText.Alignment
    def __init__(self, rect: _Optional[_Union[_types_pb2.Rect2f, _Mapping]] = ..., text: _Optional[str] = ..., alignment: _Optional[_Union[RectWithText.Alignment, str]] = ...) -> None: ...

class Thumbnail(_message.Message):
    __slots__ = ("format", "data")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Thumbnail.Format]
        JPEG: _ClassVar[Thumbnail.Format]
    NONE: Thumbnail.Format
    JPEG: Thumbnail.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    format: Thumbnail.Format
    data: bytes
    def __init__(self, format: _Optional[_Union[Thumbnail.Format, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class A(_message.Message):
    __slots__ = ("motion", "sound", "alarm", "offline", "objects", "ring", "duration_ms", "ended")
    class Motion(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Sound(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Alarm(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Offline(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Objects(_message.Message):
        __slots__ = ("class_mask",)
        CLASS_MASK_FIELD_NUMBER: _ClassVar[int]
        class_mask: int
        def __init__(self, class_mask: _Optional[int] = ...) -> None: ...
    class Ring(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MOTION_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    ALARM_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RING_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ENDED_FIELD_NUMBER: _ClassVar[int]
    motion: A.Motion
    sound: A.Sound
    alarm: A.Alarm
    offline: A.Offline
    objects: A.Objects
    ring: A.Ring
    duration_ms: int
    ended: bool
    def __init__(self, motion: _Optional[_Union[A.Motion, _Mapping]] = ..., sound: _Optional[_Union[A.Sound, _Mapping]] = ..., alarm: _Optional[_Union[A.Alarm, _Mapping]] = ..., offline: _Optional[_Union[A.Offline, _Mapping]] = ..., objects: _Optional[_Union[A.Objects, _Mapping]] = ..., ring: _Optional[_Union[A.Ring, _Mapping]] = ..., duration_ms: _Optional[int] = ..., ended: bool = ...) -> None: ...

class Motion(_message.Message):
    __slots__ = ("detected", "mask")
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    mask: Mask
    def __init__(self, detected: bool = ..., mask: _Optional[_Union[Mask, _Mapping]] = ...) -> None: ...

class Mask(_message.Message):
    __slots__ = ("width", "height", "data")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    data: bytes
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class Objects(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DObject]
    def __init__(self, items: _Optional[_Iterable[_Union[DObject, _Mapping]]] = ...) -> None: ...

class DObject(_message.Message):
    __slots__ = ("bbox", "confidence", "track")
    class Track(_message.Message):
        __slots__ = ("id", "points", "duration_ms")
        ID_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        id: int
        points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2f]
        duration_ms: int
        def __init__(self, id: _Optional[int] = ..., points: _Optional[_Iterable[_Union[_types_pb2.Point2f, _Mapping]]] = ..., duration_ms: _Optional[int] = ...) -> None: ...
    BBOX_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    bbox: _types_pb2.Rect2f
    confidence: int
    track: DObject.Track
    def __init__(self, bbox: _Optional[_Union[_types_pb2.Rect2f, _Mapping]] = ..., confidence: _Optional[int] = ..., track: _Optional[_Union[DObject.Track, _Mapping]] = ..., **kwargs) -> None: ...

class PirMotion(_message.Message):
    __slots__ = ("detected", "raw_pir_data")
    class RawPirData(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    RAW_PIR_DATA_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    raw_pir_data: PirMotion.RawPirData
    def __init__(self, detected: bool = ..., raw_pir_data: _Optional[_Union[PirMotion.RawPirData, _Mapping]] = ...) -> None: ...

class Ring(_message.Message):
    __slots__ = ("detected",)
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    def __init__(self, detected: bool = ...) -> None: ...
