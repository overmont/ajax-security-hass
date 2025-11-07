from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionCam(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "sensitivity", "always_active", "image_resolution", "photos_per_alarm", "alarm_with_photos_limit_per_arming_session", "data_channel_ping_enabled", "data_channel_ok", "data_channel_signal_quality", "photos_on_demand", "camshot_availability_mode", "camshot_available_to_anyone", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionCam.SirenTrigger]
        MOTION: _ClassVar[MotionCam.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: MotionCam.SirenTrigger
    MOTION: MotionCam.SirenTrigger
    class ImageResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_IMAGE_RESOLUTION_INFO: _ClassVar[MotionCam.ImageResolution]
        PX_160_X_120: _ClassVar[MotionCam.ImageResolution]
        PX_320_X_240: _ClassVar[MotionCam.ImageResolution]
        PX_640_X_480: _ClassVar[MotionCam.ImageResolution]
    NO_IMAGE_RESOLUTION_INFO: MotionCam.ImageResolution
    PX_160_X_120: MotionCam.ImageResolution
    PX_320_X_240: MotionCam.ImageResolution
    PX_640_X_480: MotionCam.ImageResolution
    class SignalQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIGNAL_QUALITY_INFO: _ClassVar[MotionCam.SignalQuality]
        VERY_LOW: _ClassVar[MotionCam.SignalQuality]
        LOW: _ClassVar[MotionCam.SignalQuality]
        MEDIUM: _ClassVar[MotionCam.SignalQuality]
        HIGH: _ClassVar[MotionCam.SignalQuality]
    NO_SIGNAL_QUALITY_INFO: MotionCam.SignalQuality
    VERY_LOW: MotionCam.SignalQuality
    LOW: MotionCam.SignalQuality
    MEDIUM: MotionCam.SignalQuality
    HIGH: MotionCam.SignalQuality
    class CamshotAvailabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CAMSHOT_AVAILABILITY_MODE: _ClassVar[MotionCam.CamshotAvailabilityMode]
        NEVER: _ClassVar[MotionCam.CamshotAvailabilityMode]
        ALWAYS: _ClassVar[MotionCam.CamshotAvailabilityMode]
        ARMED_ONLY: _ClassVar[MotionCam.CamshotAvailabilityMode]
    NO_CAMSHOT_AVAILABILITY_MODE: MotionCam.CamshotAvailabilityMode
    NEVER: MotionCam.CamshotAvailabilityMode
    ALWAYS: MotionCam.CamshotAvailabilityMode
    ARMED_ONLY: MotionCam.CamshotAvailabilityMode
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionCam.Subtype]
    NO_SUBTYPE: MotionCam.Subtype
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
    PHOTOS_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    CAMSHOT_AVAILABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    CAMSHOT_AVAILABLE_TO_ANYONE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[MotionCam.SirenTrigger]
    sensitivity: int
    always_active: bool
    image_resolution: MotionCam.ImageResolution
    photos_per_alarm: int
    alarm_with_photos_limit_per_arming_session: int
    data_channel_ping_enabled: bool
    data_channel_ok: _wrappers_pb2.BoolValue
    data_channel_signal_quality: MotionCam.SignalQuality
    photos_on_demand: int
    camshot_availability_mode: MotionCam.CamshotAvailabilityMode
    camshot_available_to_anyone: bool
    subtype: MotionCam.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[MotionCam.SirenTrigger, str]]] = ..., sensitivity: _Optional[int] = ..., always_active: bool = ..., image_resolution: _Optional[_Union[MotionCam.ImageResolution, str]] = ..., photos_per_alarm: _Optional[int] = ..., alarm_with_photos_limit_per_arming_session: _Optional[int] = ..., data_channel_ping_enabled: bool = ..., data_channel_ok: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., data_channel_signal_quality: _Optional[_Union[MotionCam.SignalQuality, str]] = ..., photos_on_demand: _Optional[int] = ..., camshot_availability_mode: _Optional[_Union[MotionCam.CamshotAvailabilityMode, str]] = ..., camshot_available_to_anyone: bool = ..., subtype: _Optional[_Union[MotionCam.Subtype, str]] = ...) -> None: ...
