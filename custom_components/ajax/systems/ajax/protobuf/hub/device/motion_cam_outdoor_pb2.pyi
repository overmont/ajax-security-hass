from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionCamOutdoor(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "sensitivity", "always_active", "image_resolution", "photos_per_alarm", "alarm_with_photos_limit_per_arming_session", "data_channel_ping_enabled", "data_channel_ok", "data_channel_signal_quality", "antimasking", "is_masked", "logging_enabled", "photos_on_demand", "camshot_availability_mode", "camshot_available_to_anyone", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionCamOutdoor.SirenTrigger]
        MOTION: _ClassVar[MotionCamOutdoor.SirenTrigger]
        ANTIMASKING: _ClassVar[MotionCamOutdoor.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: MotionCamOutdoor.SirenTrigger
    MOTION: MotionCamOutdoor.SirenTrigger
    ANTIMASKING: MotionCamOutdoor.SirenTrigger
    class ImageResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_IMAGE_RESOLUTION_INFO: _ClassVar[MotionCamOutdoor.ImageResolution]
        PX_320_X_176: _ClassVar[MotionCamOutdoor.ImageResolution]
        PX_640_X_352: _ClassVar[MotionCamOutdoor.ImageResolution]
    NO_IMAGE_RESOLUTION_INFO: MotionCamOutdoor.ImageResolution
    PX_320_X_176: MotionCamOutdoor.ImageResolution
    PX_640_X_352: MotionCamOutdoor.ImageResolution
    class SignalQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIGNAL_QUALITY_INFO: _ClassVar[MotionCamOutdoor.SignalQuality]
        VERY_LOW: _ClassVar[MotionCamOutdoor.SignalQuality]
        LOW: _ClassVar[MotionCamOutdoor.SignalQuality]
        MEDIUM: _ClassVar[MotionCamOutdoor.SignalQuality]
        HIGH: _ClassVar[MotionCamOutdoor.SignalQuality]
    NO_SIGNAL_QUALITY_INFO: MotionCamOutdoor.SignalQuality
    VERY_LOW: MotionCamOutdoor.SignalQuality
    LOW: MotionCamOutdoor.SignalQuality
    MEDIUM: MotionCamOutdoor.SignalQuality
    HIGH: MotionCamOutdoor.SignalQuality
    class CamshotAvailabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CAMSHOT_AVAILABILITY_MODE: _ClassVar[MotionCamOutdoor.CamshotAvailabilityMode]
        NEVER: _ClassVar[MotionCamOutdoor.CamshotAvailabilityMode]
        ALWAYS: _ClassVar[MotionCamOutdoor.CamshotAvailabilityMode]
        ARMED_ONLY: _ClassVar[MotionCamOutdoor.CamshotAvailabilityMode]
    NO_CAMSHOT_AVAILABILITY_MODE: MotionCamOutdoor.CamshotAvailabilityMode
    NEVER: MotionCamOutdoor.CamshotAvailabilityMode
    ALWAYS: MotionCamOutdoor.CamshotAvailabilityMode
    ARMED_ONLY: MotionCamOutdoor.CamshotAvailabilityMode
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionCamOutdoor.Subtype]
    NO_SUBTYPE: MotionCamOutdoor.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_PER_ALARM_FIELD_NUMBER: _ClassVar[int]
    ALARM_WITH_PHOTOS_LIMIT_PER_ARMING_SESSION_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_PING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_OK_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    IS_MASKED_FIELD_NUMBER: _ClassVar[int]
    LOGGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    CAMSHOT_AVAILABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    CAMSHOT_AVAILABLE_TO_ANYONE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[MotionCamOutdoor.SirenTrigger]
    sensitivity: int
    always_active: bool
    image_resolution: MotionCamOutdoor.ImageResolution
    photos_per_alarm: int
    alarm_with_photos_limit_per_arming_session: int
    data_channel_ping_enabled: bool
    data_channel_ok: _wrappers_pb2.BoolValue
    data_channel_signal_quality: MotionCamOutdoor.SignalQuality
    antimasking: bool
    is_masked: _wrappers_pb2.BoolValue
    logging_enabled: bool
    photos_on_demand: int
    camshot_availability_mode: MotionCamOutdoor.CamshotAvailabilityMode
    camshot_available_to_anyone: bool
    subtype: MotionCamOutdoor.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[MotionCamOutdoor.SirenTrigger, str]]] = ..., sensitivity: _Optional[int] = ..., always_active: bool = ..., image_resolution: _Optional[_Union[MotionCamOutdoor.ImageResolution, str]] = ..., photos_per_alarm: _Optional[int] = ..., alarm_with_photos_limit_per_arming_session: _Optional[int] = ..., data_channel_ping_enabled: bool = ..., data_channel_ok: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., data_channel_signal_quality: _Optional[_Union[MotionCamOutdoor.SignalQuality, str]] = ..., antimasking: bool = ..., is_masked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., logging_enabled: bool = ..., photos_on_demand: _Optional[int] = ..., camshot_availability_mode: _Optional[_Union[MotionCamOutdoor.CamshotAvailabilityMode, str]] = ..., camshot_available_to_anyone: bool = ..., subtype: _Optional[_Union[MotionCamOutdoor.Subtype, str]] = ...) -> None: ...
