from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ST_UNKNOWN: _ClassVar[StreamType]
    ST_MAIN: _ClassVar[StreamType]
    ST_SUB: _ClassVar[StreamType]

class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    C_NONE: _ClassVar[Color]
    C_RED: _ClassVar[Color]
    C_GREEN: _ClassVar[Color]
    C_YELLOW: _ClassVar[Color]
    C_BLACK: _ClassVar[Color]
    C_ORANGE: _ClassVar[Color]
    C_BLUE: _ClassVar[Color]
    C_WHITE: _ClassVar[Color]

class FrameType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FT_UNKNOWN: _ClassVar[FrameType]
    FT_VIDEO: _ClassVar[FrameType]
    FT_AUDIO: _ClassVar[FrameType]
    FT_METADATA: _ClassVar[FrameType]

class VideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VC_UNKNOWN: _ClassVar[VideoCodec]
    H264: _ClassVar[VideoCodec]
    H265: _ClassVar[VideoCodec]

class AudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AC_UNKNOWN: _ClassVar[AudioCodec]
    G711_ULAW: _ClassVar[AudioCodec]
    G711_ALAW: _ClassVar[AudioCodec]
    AAC: _ClassVar[AudioCodec]
    MP2: _ClassVar[AudioCodec]
    G726: _ClassVar[AudioCodec]
    G722: _ClassVar[AudioCodec]

class VideoBitrateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VBT_NONE: _ClassVar[VideoBitrateType]
    CBR: _ClassVar[VideoBitrateType]
    VBR: _ClassVar[VideoBitrateType]

class ObjectClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OC_OTHER: _ClassVar[ObjectClass]
    OC_PERSON: _ClassVar[ObjectClass]
    OC_PET: _ClassVar[ObjectClass]
    OC_VEHICLE: _ClassVar[ObjectClass]

class CryptoHashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHA_NONE: _ClassVar[CryptoHashAlgorithm]
    CHA_SHA256: _ClassVar[CryptoHashAlgorithm]

class CryptoCipherAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CCA_NONE: _ClassVar[CryptoCipherAlgorithm]
    CCA_AES256_GCM: _ClassVar[CryptoCipherAlgorithm]
ST_UNKNOWN: StreamType
ST_MAIN: StreamType
ST_SUB: StreamType
C_NONE: Color
C_RED: Color
C_GREEN: Color
C_YELLOW: Color
C_BLACK: Color
C_ORANGE: Color
C_BLUE: Color
C_WHITE: Color
FT_UNKNOWN: FrameType
FT_VIDEO: FrameType
FT_AUDIO: FrameType
FT_METADATA: FrameType
VC_UNKNOWN: VideoCodec
H264: VideoCodec
H265: VideoCodec
AC_UNKNOWN: AudioCodec
G711_ULAW: AudioCodec
G711_ALAW: AudioCodec
AAC: AudioCodec
MP2: AudioCodec
G726: AudioCodec
G722: AudioCodec
VBT_NONE: VideoBitrateType
CBR: VideoBitrateType
VBR: VideoBitrateType
OC_OTHER: ObjectClass
OC_PERSON: ObjectClass
OC_PET: ObjectClass
OC_VEHICLE: ObjectClass
CHA_NONE: CryptoHashAlgorithm
CHA_SHA256: CryptoHashAlgorithm
CCA_NONE: CryptoCipherAlgorithm
CCA_AES256_GCM: CryptoCipherAlgorithm

class FrameTypeId(_message.Message):
    __slots__ = ("frame_type", "metadata_type")
    FRAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    frame_type: FrameType
    metadata_type: str
    def __init__(self, frame_type: _Optional[_Union[FrameType, str]] = ..., metadata_type: _Optional[str] = ...) -> None: ...

class VideoResolution(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class UInt32Range(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: int
    max_value: int
    def __init__(self, min_value: _Optional[int] = ..., max_value: _Optional[int] = ...) -> None: ...

class FloatRange(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: float
    max_value: float
    def __init__(self, min_value: _Optional[float] = ..., max_value: _Optional[float] = ...) -> None: ...

class DurationRange(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: _duration_pb2.Duration
    max_value: _duration_pb2.Duration
    def __init__(self, min_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TimestampRange(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: _timestamp_pb2.Timestamp
    max_value: _timestamp_pb2.Timestamp
    def __init__(self, min_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SparseRange(_message.Message):
    __slots__ = ("max_frames", "ts_range")
    MAX_FRAMES_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    max_frames: int
    ts_range: TimestampRange
    def __init__(self, max_frames: _Optional[int] = ..., ts_range: _Optional[_Union[TimestampRange, _Mapping]] = ...) -> None: ...

class Point2f(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Point2i(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class Rect2f(_message.Message):
    __slots__ = ("top_left", "size")
    TOP_LEFT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    top_left: Point2f
    size: Point2f
    def __init__(self, top_left: _Optional[_Union[Point2f, _Mapping]] = ..., size: _Optional[_Union[Point2f, _Mapping]] = ...) -> None: ...

class Rect2i(_message.Message):
    __slots__ = ("top_left", "size")
    TOP_LEFT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    top_left: Point2i
    size: Point2i
    def __init__(self, top_left: _Optional[_Union[Point2i, _Mapping]] = ..., size: _Optional[_Union[Point2i, _Mapping]] = ...) -> None: ...

class Line2f(_message.Message):
    __slots__ = ("p1", "p2")
    P1_FIELD_NUMBER: _ClassVar[int]
    P2_FIELD_NUMBER: _ClassVar[int]
    p1: Point2f
    p2: Point2f
    def __init__(self, p1: _Optional[_Union[Point2f, _Mapping]] = ..., p2: _Optional[_Union[Point2f, _Mapping]] = ...) -> None: ...

class Line2i(_message.Message):
    __slots__ = ("p1", "p2")
    P1_FIELD_NUMBER: _ClassVar[int]
    P2_FIELD_NUMBER: _ClassVar[int]
    p1: Point2i
    p2: Point2i
    def __init__(self, p1: _Optional[_Union[Point2i, _Mapping]] = ..., p2: _Optional[_Union[Point2i, _Mapping]] = ...) -> None: ...

class Mask(_message.Message):
    __slots__ = ("width", "height", "data")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    data: bytes
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class MacAddress(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class IpEndpoint(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: IpAddress
    port: int
    def __init__(self, address: _Optional[_Union[IpAddress, _Mapping]] = ..., port: _Optional[int] = ...) -> None: ...

class IpAddress(_message.Message):
    __slots__ = ("v4", "v6")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    v4: IpAddressV4
    v6: IpAddressV6
    def __init__(self, v4: _Optional[_Union[IpAddressV4, _Mapping]] = ..., v6: _Optional[_Union[IpAddressV6, _Mapping]] = ...) -> None: ...

class IpAddressV4(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class IpAddressV6(_message.Message):
    __slots__ = ("data", "scope_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    scope_id: int
    def __init__(self, data: _Optional[bytes] = ..., scope_id: _Optional[int] = ...) -> None: ...

class CryptoKey(_message.Message):
    __slots__ = ("bluetooth", "wap")
    class Bluetooth(_message.Message):
        __slots__ = ("algorithm", "nonce", "data")
        ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        NONCE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        algorithm: CryptoCipherAlgorithm
        nonce: str
        data: bytes
        def __init__(self, algorithm: _Optional[_Union[CryptoCipherAlgorithm, str]] = ..., nonce: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    class WAP(_message.Message):
        __slots__ = ("algorithm", "nonce", "data")
        ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        NONCE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        algorithm: CryptoCipherAlgorithm
        nonce: str
        data: bytes
        def __init__(self, algorithm: _Optional[_Union[CryptoCipherAlgorithm, str]] = ..., nonce: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    BLUETOOTH_FIELD_NUMBER: _ClassVar[int]
    WAP_FIELD_NUMBER: _ClassVar[int]
    bluetooth: CryptoKey.Bluetooth
    wap: CryptoKey.WAP
    def __init__(self, bluetooth: _Optional[_Union[CryptoKey.Bluetooth, _Mapping]] = ..., wap: _Optional[_Union[CryptoKey.WAP, _Mapping]] = ...) -> None: ...
