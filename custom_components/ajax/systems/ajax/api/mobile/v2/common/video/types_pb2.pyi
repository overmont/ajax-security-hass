from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
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
    MJPEG: _ClassVar[VideoCodec]

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
    CHA_SHA1: _ClassVar[CryptoHashAlgorithm]

class CryptoCipherAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CCA_NONE: _ClassVar[CryptoCipherAlgorithm]
    CCA_AES256_GCM: _ClassVar[CryptoCipherAlgorithm]

class ExposurePriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EP_NONE: _ClassVar[ExposurePriority]
    EP_LOW_NOISE: _ClassVar[ExposurePriority]
    EP_FRAME_RATE: _ClassVar[ExposurePriority]

class PredefinedExposureMeteringArea(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PREDEFINED_EXPOSURE_METERING_AREA_UNSPECIFIED: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_FULL_FRAME: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_TOP: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_RIGHT: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_BOTTOM: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_LEFT: _ClassVar[PredefinedExposureMeteringArea]
    PREDEFINED_EXPOSURE_METERING_AREA_CENTER: _ClassVar[PredefinedExposureMeteringArea]

class IrCutFilterAutoBoundaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IFB_NONE: _ClassVar[IrCutFilterAutoBoundaryType]
    IFB_COMMON: _ClassVar[IrCutFilterAutoBoundaryType]
    IFB_TO_ON: _ClassVar[IrCutFilterAutoBoundaryType]
    IFB_TO_OFF: _ClassVar[IrCutFilterAutoBoundaryType]

class PrivacyMaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVACY_MASK_TYPE_UNSPECIFIED: _ClassVar[PrivacyMaskType]
    PRIVACY_MASK_TYPE_COLOR: _ClassVar[PrivacyMaskType]
    PRIVACY_MASK_TYPE_PIXELATED: _ClassVar[PrivacyMaskType]
    PRIVACY_MASK_TYPE_BLURRED: _ClassVar[PrivacyMaskType]

class AntiFlickerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANTI_FLICKER_TYPE_UNSPECIFIED: _ClassVar[AntiFlickerType]
    ANTI_FLICKER_TYPE_DISABLED: _ClassVar[AntiFlickerType]
    ANTI_FLICKER_TYPE_50HZ: _ClassVar[AntiFlickerType]
    ANTI_FLICKER_TYPE_60HZ: _ClassVar[AntiFlickerType]

class AutoExposurePreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTO_EXPOSURE_PRESET_UNSPECIFIED: _ClassVar[AutoExposurePreset]
    AUTO_EXPOSURE_PRESET_LESS_NOISE: _ClassVar[AutoExposurePreset]
    AUTO_EXPOSURE_PRESET_BALANCE: _ClassVar[AutoExposurePreset]
    AUTO_EXPOSURE_PRESET_LESS_MOTION_BLUR: _ClassVar[AutoExposurePreset]

class Rotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROTATION_UNSPECIFIED: _ClassVar[Rotation]
    ROTATION_0: _ClassVar[Rotation]
    ROTATION_90: _ClassVar[Rotation]
    ROTATION_180: _ClassVar[Rotation]
    ROTATION_270: _ClassVar[Rotation]

class VideoSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_SOURCE_TYPE_UNSPECIFIED: _ClassVar[VideoSourceType]
    VIDEO_SOURCE_TYPE_VIDEO_EDGE: _ClassVar[VideoSourceType]
    VIDEO_SOURCE_TYPE_CLOUD_ARCHIVE: _ClassVar[VideoSourceType]

class IceCandidateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ICE_CANDIDATE_TYPE_UNSPECIFIED: _ClassVar[IceCandidateType]
    ICE_CANDIDATE_TYPE_HOST: _ClassVar[IceCandidateType]
    ICE_CANDIDATE_TYPE_REFLEXIVE: _ClassVar[IceCandidateType]
    ICE_CANDIDATE_TYPE_RELAY: _ClassVar[IceCandidateType]

class NetworkTechnologyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TECHNOLOGY_TYPE_UNSPECIFIED: _ClassVar[NetworkTechnologyType]
    NETWORK_TECHNOLOGY_TYPE_ETHERNET: _ClassVar[NetworkTechnologyType]
    NETWORK_TECHNOLOGY_TYPE_WIFI: _ClassVar[NetworkTechnologyType]
    NETWORK_TECHNOLOGY_TYPE_CELLULAR: _ClassVar[NetworkTechnologyType]

class TransportProtocolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSPORT_PROTOCOL_TYPE_UNSPECIFIED: _ClassVar[TransportProtocolType]
    TRANSPORT_PROTOCOL_TYPE_TCP: _ClassVar[TransportProtocolType]
    TRANSPORT_PROTOCOL_TYPE_UDP: _ClassVar[TransportProtocolType]

class ImageProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE_PROFILE_TYPE_UNSPECIFIED: _ClassVar[ImageProfileType]
    IMAGE_PROFILE_TYPE_NATURAL: _ClassVar[ImageProfileType]
    IMAGE_PROFILE_TYPE_INSTAMODE: _ClassVar[ImageProfileType]
ST_UNKNOWN: StreamType
ST_MAIN: StreamType
ST_SUB: StreamType
FT_UNKNOWN: FrameType
FT_VIDEO: FrameType
FT_AUDIO: FrameType
FT_METADATA: FrameType
VC_UNKNOWN: VideoCodec
H264: VideoCodec
H265: VideoCodec
MJPEG: VideoCodec
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
CHA_SHA1: CryptoHashAlgorithm
CCA_NONE: CryptoCipherAlgorithm
CCA_AES256_GCM: CryptoCipherAlgorithm
EP_NONE: ExposurePriority
EP_LOW_NOISE: ExposurePriority
EP_FRAME_RATE: ExposurePriority
PREDEFINED_EXPOSURE_METERING_AREA_UNSPECIFIED: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_FULL_FRAME: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_TOP: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_RIGHT: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_BOTTOM: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_LEFT: PredefinedExposureMeteringArea
PREDEFINED_EXPOSURE_METERING_AREA_CENTER: PredefinedExposureMeteringArea
IFB_NONE: IrCutFilterAutoBoundaryType
IFB_COMMON: IrCutFilterAutoBoundaryType
IFB_TO_ON: IrCutFilterAutoBoundaryType
IFB_TO_OFF: IrCutFilterAutoBoundaryType
PRIVACY_MASK_TYPE_UNSPECIFIED: PrivacyMaskType
PRIVACY_MASK_TYPE_COLOR: PrivacyMaskType
PRIVACY_MASK_TYPE_PIXELATED: PrivacyMaskType
PRIVACY_MASK_TYPE_BLURRED: PrivacyMaskType
ANTI_FLICKER_TYPE_UNSPECIFIED: AntiFlickerType
ANTI_FLICKER_TYPE_DISABLED: AntiFlickerType
ANTI_FLICKER_TYPE_50HZ: AntiFlickerType
ANTI_FLICKER_TYPE_60HZ: AntiFlickerType
AUTO_EXPOSURE_PRESET_UNSPECIFIED: AutoExposurePreset
AUTO_EXPOSURE_PRESET_LESS_NOISE: AutoExposurePreset
AUTO_EXPOSURE_PRESET_BALANCE: AutoExposurePreset
AUTO_EXPOSURE_PRESET_LESS_MOTION_BLUR: AutoExposurePreset
ROTATION_UNSPECIFIED: Rotation
ROTATION_0: Rotation
ROTATION_90: Rotation
ROTATION_180: Rotation
ROTATION_270: Rotation
VIDEO_SOURCE_TYPE_UNSPECIFIED: VideoSourceType
VIDEO_SOURCE_TYPE_VIDEO_EDGE: VideoSourceType
VIDEO_SOURCE_TYPE_CLOUD_ARCHIVE: VideoSourceType
ICE_CANDIDATE_TYPE_UNSPECIFIED: IceCandidateType
ICE_CANDIDATE_TYPE_HOST: IceCandidateType
ICE_CANDIDATE_TYPE_REFLEXIVE: IceCandidateType
ICE_CANDIDATE_TYPE_RELAY: IceCandidateType
NETWORK_TECHNOLOGY_TYPE_UNSPECIFIED: NetworkTechnologyType
NETWORK_TECHNOLOGY_TYPE_ETHERNET: NetworkTechnologyType
NETWORK_TECHNOLOGY_TYPE_WIFI: NetworkTechnologyType
NETWORK_TECHNOLOGY_TYPE_CELLULAR: NetworkTechnologyType
TRANSPORT_PROTOCOL_TYPE_UNSPECIFIED: TransportProtocolType
TRANSPORT_PROTOCOL_TYPE_TCP: TransportProtocolType
TRANSPORT_PROTOCOL_TYPE_UDP: TransportProtocolType
IMAGE_PROFILE_TYPE_UNSPECIFIED: ImageProfileType
IMAGE_PROFILE_TYPE_NATURAL: ImageProfileType
IMAGE_PROFILE_TYPE_INSTAMODE: ImageProfileType

class FrameTypeId(_message.Message):
    __slots__ = ("frame_type", "metadata_type")
    FRAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    frame_type: FrameType
    metadata_type: str
    def __init__(self, frame_type: _Optional[_Union[FrameType, str]] = ..., metadata_type: _Optional[str] = ...) -> None: ...

class Mask(_message.Message):
    __slots__ = ("width", "height", "data")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    data: bytes
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class VideoResolution(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class Int32Range(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: int
    max_value: int
    def __init__(self, min_value: _Optional[int] = ..., max_value: _Optional[int] = ...) -> None: ...

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

class MacAddress(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

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

class Color(_message.Message):
    __slots__ = ("r", "g", "b", "a")
    R_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    r: int
    g: int
    b: int
    a: int
    def __init__(self, r: _Optional[int] = ..., g: _Optional[int] = ..., b: _Optional[int] = ..., a: _Optional[int] = ...) -> None: ...

class ShutterSpeed(_message.Message):
    __slots__ = ("id", "duration")
    ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    duration: _duration_pb2.Duration
    def __init__(self, id: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
