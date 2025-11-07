from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionSettings(_message.Message):
    __slots__ = ("address", "port", "username", "password")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: str
    username: str
    password: str
    def __init__(self, address: _Optional[str] = ..., port: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VideoSettings(_message.Message):
    __slots__ = ("brightness", "contrast", "saturation", "sharpness", "blc", "white_balance", "wdr", "exposure", "ircut_filter", "transform", "off_illumination", "ir_illumination", "white_illumination", "smart_illumination", "privacy_masks", "exposure_metering_area", "anti_flicker", "noise_reduction", "main", "sub", "image_profile")
    class ImageProfile(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _types_pb2.ImageProfileType
        def __init__(self, type: _Optional[_Union[_types_pb2.ImageProfileType, str]] = ...) -> None: ...
    class BacklightCompensation(_message.Message):
        __slots__ = ("off", "on")
        class OnMode(_message.Message):
            __slots__ = ("level",)
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: float
            def __init__(self, level: _Optional[float] = ...) -> None: ...
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        off: VideoSettings.BacklightCompensation.OffMode
        on: VideoSettings.BacklightCompensation.OnMode
        def __init__(self, off: _Optional[_Union[VideoSettings.BacklightCompensation.OffMode, _Mapping]] = ..., on: _Optional[_Union[VideoSettings.BacklightCompensation.OnMode, _Mapping]] = ...) -> None: ...
    class WhiteBalance(_message.Message):
        __slots__ = ("manual", "auto")
        class ManualMode(_message.Message):
            __slots__ = ("red_gain", "blue_gain")
            RED_GAIN_FIELD_NUMBER: _ClassVar[int]
            BLUE_GAIN_FIELD_NUMBER: _ClassVar[int]
            red_gain: float
            blue_gain: float
            def __init__(self, red_gain: _Optional[float] = ..., blue_gain: _Optional[float] = ...) -> None: ...
        class AutoMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        manual: VideoSettings.WhiteBalance.ManualMode
        auto: VideoSettings.WhiteBalance.AutoMode
        def __init__(self, manual: _Optional[_Union[VideoSettings.WhiteBalance.ManualMode, _Mapping]] = ..., auto: _Optional[_Union[VideoSettings.WhiteBalance.AutoMode, _Mapping]] = ...) -> None: ...
    class WideDynamicRange(_message.Message):
        __slots__ = ("off", "on")
        class OnMode(_message.Message):
            __slots__ = ("level",)
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: float
            def __init__(self, level: _Optional[float] = ...) -> None: ...
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        off: VideoSettings.WideDynamicRange.OffMode
        on: VideoSettings.WideDynamicRange.OnMode
        def __init__(self, off: _Optional[_Union[VideoSettings.WideDynamicRange.OffMode, _Mapping]] = ..., on: _Optional[_Union[VideoSettings.WideDynamicRange.OnMode, _Mapping]] = ...) -> None: ...
    class Exposure(_message.Message):
        __slots__ = ("manual", "auto")
        class ManualMode(_message.Message):
            __slots__ = ("exposure_time", "gain", "iris")
            EXPOSURE_TIME_FIELD_NUMBER: _ClassVar[int]
            GAIN_FIELD_NUMBER: _ClassVar[int]
            IRIS_FIELD_NUMBER: _ClassVar[int]
            exposure_time: _duration_pb2.Duration
            gain: float
            iris: float
            def __init__(self, exposure_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gain: _Optional[float] = ..., iris: _Optional[float] = ...) -> None: ...
        class AutoMode(_message.Message):
            __slots__ = ("priority", "exposure_time_range", "gain_range", "iris_range", "exposure_compensation", "preset")
            PRIORITY_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
            PRESET_FIELD_NUMBER: _ClassVar[int]
            priority: _types_pb2.ExposurePriority
            exposure_time_range: _types_pb2.DurationRange
            gain_range: _types_pb2.FloatRange
            iris_range: _types_pb2.FloatRange
            exposure_compensation: int
            preset: _types_pb2.AutoExposurePreset
            def __init__(self, priority: _Optional[_Union[_types_pb2.ExposurePriority, str]] = ..., exposure_time_range: _Optional[_Union[_types_pb2.DurationRange, _Mapping]] = ..., gain_range: _Optional[_Union[_types_pb2.FloatRange, _Mapping]] = ..., iris_range: _Optional[_Union[_types_pb2.FloatRange, _Mapping]] = ..., exposure_compensation: _Optional[int] = ..., preset: _Optional[_Union[_types_pb2.AutoExposurePreset, str]] = ...) -> None: ...
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        manual: VideoSettings.Exposure.ManualMode
        auto: VideoSettings.Exposure.AutoMode
        def __init__(self, manual: _Optional[_Union[VideoSettings.Exposure.ManualMode, _Mapping]] = ..., auto: _Optional[_Union[VideoSettings.Exposure.AutoMode, _Mapping]] = ...) -> None: ...
    class IrCutFilter(_message.Message):
        __slots__ = ("on", "off", "auto")
        class OnMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AutoMode(_message.Message):
            __slots__ = ("ircut_filter_auto_adjustments",)
            class IrCutFilterAutoAdjustment(_message.Message):
                __slots__ = ("boundary_type", "boundary_offset", "response_time")
                BOUNDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
                BOUNDARY_OFFSET_FIELD_NUMBER: _ClassVar[int]
                RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
                boundary_type: _types_pb2.IrCutFilterAutoBoundaryType
                boundary_offset: float
                response_time: _duration_pb2.Duration
                def __init__(self, boundary_type: _Optional[_Union[_types_pb2.IrCutFilterAutoBoundaryType, str]] = ..., boundary_offset: _Optional[float] = ..., response_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            IRCUT_FILTER_AUTO_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
            ircut_filter_auto_adjustments: _containers.RepeatedCompositeFieldContainer[VideoSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment]
            def __init__(self, ircut_filter_auto_adjustments: _Optional[_Iterable[_Union[VideoSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment, _Mapping]]] = ...) -> None: ...
        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        on: VideoSettings.IrCutFilter.OnMode
        off: VideoSettings.IrCutFilter.OffMode
        auto: VideoSettings.IrCutFilter.AutoMode
        def __init__(self, on: _Optional[_Union[VideoSettings.IrCutFilter.OnMode, _Mapping]] = ..., off: _Optional[_Union[VideoSettings.IrCutFilter.OffMode, _Mapping]] = ..., auto: _Optional[_Union[VideoSettings.IrCutFilter.AutoMode, _Mapping]] = ...) -> None: ...
    class Stream(_message.Message):
        __slots__ = ("enabled", "codec", "codec_extradata", "resolution", "bitrate", "bitrate_type", "gop_size", "fps", "quality")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        CODEC_EXTRADATA_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        BITRATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        GOP_SIZE_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        codec: _types_pb2.VideoCodec
        codec_extradata: bytes
        resolution: _types_pb2.VideoResolution
        bitrate: int
        bitrate_type: _types_pb2.VideoBitrateType
        gop_size: int
        fps: int
        quality: int
        def __init__(self, enabled: bool = ..., codec: _Optional[_Union[_types_pb2.VideoCodec, str]] = ..., codec_extradata: _Optional[bytes] = ..., resolution: _Optional[_Union[_types_pb2.VideoResolution, _Mapping]] = ..., bitrate: _Optional[int] = ..., bitrate_type: _Optional[_Union[_types_pb2.VideoBitrateType, str]] = ..., gop_size: _Optional[int] = ..., fps: _Optional[int] = ..., quality: _Optional[int] = ...) -> None: ...
    class Transform(_message.Message):
        __slots__ = ("rotation", "mirror")
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        MIRROR_FIELD_NUMBER: _ClassVar[int]
        rotation: _types_pb2.Rotation
        mirror: bool
        def __init__(self, rotation: _Optional[_Union[_types_pb2.Rotation, str]] = ..., mirror: bool = ...) -> None: ...
    class OffIllumination(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class IrIllumination(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("power_level",)
            POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            power_level: int
            def __init__(self, power_level: _Optional[int] = ...) -> None: ...
        class AutoMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        AUTO_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        auto: VideoSettings.IrIllumination.AutoMode
        manual: VideoSettings.IrIllumination.ManualMode
        def __init__(self, auto: _Optional[_Union[VideoSettings.IrIllumination.AutoMode, _Mapping]] = ..., manual: _Optional[_Union[VideoSettings.IrIllumination.ManualMode, _Mapping]] = ...) -> None: ...
    class WhiteIllumination(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("power_level",)
            POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            power_level: int
            def __init__(self, power_level: _Optional[int] = ...) -> None: ...
        class AutoMode(_message.Message):
            __slots__ = ("max_power_level",)
            MAX_POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            max_power_level: int
            def __init__(self, max_power_level: _Optional[int] = ...) -> None: ...
        AUTO_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        auto: VideoSettings.WhiteIllumination.AutoMode
        manual: VideoSettings.WhiteIllumination.ManualMode
        def __init__(self, auto: _Optional[_Union[VideoSettings.WhiteIllumination.AutoMode, _Mapping]] = ..., manual: _Optional[_Union[VideoSettings.WhiteIllumination.ManualMode, _Mapping]] = ...) -> None: ...
    class SmartIllumination(_message.Message):
        __slots__ = ("ir_illumination", "white_illumination")
        IR_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        WHITE_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        ir_illumination: VideoSettings.IrIllumination
        white_illumination: VideoSettings.WhiteIllumination
        def __init__(self, ir_illumination: _Optional[_Union[VideoSettings.IrIllumination, _Mapping]] = ..., white_illumination: _Optional[_Union[VideoSettings.WhiteIllumination, _Mapping]] = ...) -> None: ...
    class PrivacyMasks(_message.Message):
        __slots__ = ("entries",)
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[VideoSettings.PrivacyMask]
        def __init__(self, entries: _Optional[_Iterable[_Union[VideoSettings.PrivacyMask, _Mapping]]] = ...) -> None: ...
    class PrivacyMask(_message.Message):
        __slots__ = ("enabled", "polygon", "type", "color")
        class Polygon(_message.Message):
            __slots__ = ("points",)
            POINTS_FIELD_NUMBER: _ClassVar[int]
            points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2i]
            def __init__(self, points: _Optional[_Iterable[_Union[_types_pb2.Point2i, _Mapping]]] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        POLYGON_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        polygon: VideoSettings.PrivacyMask.Polygon
        type: _types_pb2.PrivacyMaskType
        color: _types_pb2.Color
        def __init__(self, enabled: bool = ..., polygon: _Optional[_Union[VideoSettings.PrivacyMask.Polygon, _Mapping]] = ..., type: _Optional[_Union[_types_pb2.PrivacyMaskType, str]] = ..., color: _Optional[_Union[_types_pb2.Color, _Mapping]] = ...) -> None: ...
    class ExposureMeteringArea(_message.Message):
        __slots__ = ("predefined",)
        PREDEFINED_FIELD_NUMBER: _ClassVar[int]
        predefined: _types_pb2.PredefinedExposureMeteringArea
        def __init__(self, predefined: _Optional[_Union[_types_pb2.PredefinedExposureMeteringArea, str]] = ...) -> None: ...
    class AntiFlicker(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _types_pb2.AntiFlickerType
        def __init__(self, type: _Optional[_Union[_types_pb2.AntiFlickerType, str]] = ...) -> None: ...
    class NoiseReduction(_message.Message):
        __slots__ = ("on", "off")
        class OnMode(_message.Message):
            __slots__ = ("level", "midpoint_level")
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            MIDPOINT_LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: int
            midpoint_level: int
            def __init__(self, level: _Optional[int] = ..., midpoint_level: _Optional[int] = ...) -> None: ...
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        on: VideoSettings.NoiseReduction.OnMode
        off: VideoSettings.NoiseReduction.OffMode
        def __init__(self, on: _Optional[_Union[VideoSettings.NoiseReduction.OnMode, _Mapping]] = ..., off: _Optional[_Union[VideoSettings.NoiseReduction.OffMode, _Mapping]] = ...) -> None: ...
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    CONTRAST_FIELD_NUMBER: _ClassVar[int]
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    BLC_FIELD_NUMBER: _ClassVar[int]
    WHITE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    WDR_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    IRCUT_FILTER_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    OFF_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    IR_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    WHITE_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    SMART_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MASKS_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_METERING_AREA_FIELD_NUMBER: _ClassVar[int]
    ANTI_FLICKER_FIELD_NUMBER: _ClassVar[int]
    NOISE_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    brightness: int
    contrast: int
    saturation: int
    sharpness: int
    blc: VideoSettings.BacklightCompensation
    white_balance: VideoSettings.WhiteBalance
    wdr: VideoSettings.WideDynamicRange
    exposure: VideoSettings.Exposure
    ircut_filter: VideoSettings.IrCutFilter
    transform: VideoSettings.Transform
    off_illumination: VideoSettings.OffIllumination
    ir_illumination: VideoSettings.IrIllumination
    white_illumination: VideoSettings.WhiteIllumination
    smart_illumination: VideoSettings.SmartIllumination
    privacy_masks: VideoSettings.PrivacyMasks
    exposure_metering_area: VideoSettings.ExposureMeteringArea
    anti_flicker: VideoSettings.AntiFlicker
    noise_reduction: VideoSettings.NoiseReduction
    main: VideoSettings.Stream
    sub: VideoSettings.Stream
    image_profile: VideoSettings.ImageProfile
    def __init__(self, brightness: _Optional[int] = ..., contrast: _Optional[int] = ..., saturation: _Optional[int] = ..., sharpness: _Optional[int] = ..., blc: _Optional[_Union[VideoSettings.BacklightCompensation, _Mapping]] = ..., white_balance: _Optional[_Union[VideoSettings.WhiteBalance, _Mapping]] = ..., wdr: _Optional[_Union[VideoSettings.WideDynamicRange, _Mapping]] = ..., exposure: _Optional[_Union[VideoSettings.Exposure, _Mapping]] = ..., ircut_filter: _Optional[_Union[VideoSettings.IrCutFilter, _Mapping]] = ..., transform: _Optional[_Union[VideoSettings.Transform, _Mapping]] = ..., off_illumination: _Optional[_Union[VideoSettings.OffIllumination, _Mapping]] = ..., ir_illumination: _Optional[_Union[VideoSettings.IrIllumination, _Mapping]] = ..., white_illumination: _Optional[_Union[VideoSettings.WhiteIllumination, _Mapping]] = ..., smart_illumination: _Optional[_Union[VideoSettings.SmartIllumination, _Mapping]] = ..., privacy_masks: _Optional[_Union[VideoSettings.PrivacyMasks, _Mapping]] = ..., exposure_metering_area: _Optional[_Union[VideoSettings.ExposureMeteringArea, _Mapping]] = ..., anti_flicker: _Optional[_Union[VideoSettings.AntiFlicker, _Mapping]] = ..., noise_reduction: _Optional[_Union[VideoSettings.NoiseReduction, _Mapping]] = ..., main: _Optional[_Union[VideoSettings.Stream, _Mapping]] = ..., sub: _Optional[_Union[VideoSettings.Stream, _Mapping]] = ..., image_profile: _Optional[_Union[VideoSettings.ImageProfile, _Mapping]] = ...) -> None: ...

class AudioSettings(_message.Message):
    __slots__ = ("enabled", "codec", "codec_extradata", "bitrate", "sample_rate", "mic_volume", "mic_gain")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    CODEC_EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    MIC_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MIC_GAIN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    codec: _types_pb2.AudioCodec
    codec_extradata: bytes
    bitrate: int
    sample_rate: int
    mic_volume: int
    mic_gain: int
    def __init__(self, enabled: bool = ..., codec: _Optional[_Union[_types_pb2.AudioCodec, str]] = ..., codec_extradata: _Optional[bytes] = ..., bitrate: _Optional[int] = ..., sample_rate: _Optional[int] = ..., mic_volume: _Optional[int] = ..., mic_gain: _Optional[int] = ...) -> None: ...

class AudioOutputSettings(_message.Message):
    __slots__ = ("volume",)
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    volume: int
    def __init__(self, volume: _Optional[int] = ...) -> None: ...

class ChannelSettings(_message.Message):
    __slots__ = ("channel_id", "video", "audio", "audio_output")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    video: VideoSettings
    audio: AudioSettings
    audio_output: AudioOutputSettings
    def __init__(self, channel_id: _Optional[str] = ..., video: _Optional[_Union[VideoSettings, _Mapping]] = ..., audio: _Optional[_Union[AudioSettings, _Mapping]] = ..., audio_output: _Optional[_Union[AudioOutputSettings, _Mapping]] = ...) -> None: ...

class MediaDeviceSettings(_message.Message):
    __slots__ = ("channels",)
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ChannelSettings]
    def __init__(self, channels: _Optional[_Iterable[_Union[ChannelSettings, _Mapping]]] = ...) -> None: ...
