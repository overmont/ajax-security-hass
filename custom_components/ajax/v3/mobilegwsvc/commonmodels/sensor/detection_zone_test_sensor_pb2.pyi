from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Outdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTDOOR_UNSPECIFIED: _ClassVar[Outdoor]
    OUTDOOR_MOVING_SENSOR: _ClassVar[Outdoor]
    OUTDOOR_UPPER_PIR: _ClassVar[Outdoor]
    OUTDOOR_LOWER_PIR: _ClassVar[Outdoor]
    OUTDOOR_MASKING_SENSOR: _ClassVar[Outdoor]

class Curtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURTAIN_UNSPECIFIED: _ClassVar[Curtain]
    CURTAIN_MOVING_SENSOR: _ClassVar[Curtain]
    CURTAIN_MASKING_SENSORS: _ClassVar[Curtain]

class DualCurtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUAL_CURTAIN_UNSPECIFIED: _ClassVar[DualCurtain]
    DUAL_CURTAIN_ALL_PIR_SENSORS: _ClassVar[DualCurtain]
    DUAL_CURTAIN_UPPER_PIR_SENSORS: _ClassVar[DualCurtain]
    DUAL_CURTAIN_LOWER_PIR_SENSORS: _ClassVar[DualCurtain]
    DUAL_CURTAIN_MASKING_SENSORS: _ClassVar[DualCurtain]

class ButtonS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUTTON_S_UNSPECIFIED: _ClassVar[ButtonS]
    BUTTON_S_BUTTON_TEST: _ClassVar[ButtonS]

class CurtainOutdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURTAIN_OUTDOOR_UNSPECIFIED: _ClassVar[CurtainOutdoor]
    CURTAIN_OUTDOOR_MOVING_SENSOR: _ClassVar[CurtainOutdoor]
    CURTAIN_OUTDOOR_MASKING_SENSOR: _ClassVar[CurtainOutdoor]

class CurtainOutdoorMini(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURTAIN_OUTDOOR_MINI_UNSPECIFIED: _ClassVar[CurtainOutdoorMini]
    CURTAIN_OUTDOOR_MINI_MOVING_SENSOR: _ClassVar[CurtainOutdoorMini]
    CURTAIN_OUTDOOR_MINI_MASKING_SENSOR: _ClassVar[CurtainOutdoorMini]

class MotionProtectG3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTION_PROTECT_G3_UNSPECIFIED: _ClassVar[MotionProtectG3]
    MOTION_PROTECT_G3_MOVING_SENSOR: _ClassVar[MotionProtectG3]
    MOTION_PROTECT_G3_MASKING_SENSOR: _ClassVar[MotionProtectG3]

class MotionCamSPhodAm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTION_CAM_S_PHOD_AM_UNSPECIFIED: _ClassVar[MotionCamSPhodAm]
    MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: _ClassVar[MotionCamSPhodAm]
    MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: _ClassVar[MotionCamSPhodAm]

class DoubleButtonG3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOUBLE_BUTTON_G3_UNSPECIFIED: _ClassVar[DoubleButtonG3]
    DOUBLE_BUTTON_G3_BUTTON_TEST: _ClassVar[DoubleButtonG3]

class MotionCamG3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTION_CAM_G3_UNSPECIFIED: _ClassVar[MotionCamG3]
    MOTION_CAM_G3_MOVING_SENSOR: _ClassVar[MotionCamG3]
    MOTION_CAM_G3_MASKING_SENSOR: _ClassVar[MotionCamG3]

class CurtainCamOutdoorHmPhod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURTAIN_CAM_OUTDOOR_HM_PHOD_UNSPECIFIED: _ClassVar[CurtainCamOutdoorHmPhod]
    CURTAIN_CAM_OUTDOOR_HM_PHOD_ALL_MOTION_SENSORS: _ClassVar[CurtainCamOutdoorHmPhod]
    CURTAIN_CAM_OUTDOOR_HM_PHOD_MASKING_SENSOR: _ClassVar[CurtainCamOutdoorHmPhod]
OUTDOOR_UNSPECIFIED: Outdoor
OUTDOOR_MOVING_SENSOR: Outdoor
OUTDOOR_UPPER_PIR: Outdoor
OUTDOOR_LOWER_PIR: Outdoor
OUTDOOR_MASKING_SENSOR: Outdoor
CURTAIN_UNSPECIFIED: Curtain
CURTAIN_MOVING_SENSOR: Curtain
CURTAIN_MASKING_SENSORS: Curtain
DUAL_CURTAIN_UNSPECIFIED: DualCurtain
DUAL_CURTAIN_ALL_PIR_SENSORS: DualCurtain
DUAL_CURTAIN_UPPER_PIR_SENSORS: DualCurtain
DUAL_CURTAIN_LOWER_PIR_SENSORS: DualCurtain
DUAL_CURTAIN_MASKING_SENSORS: DualCurtain
BUTTON_S_UNSPECIFIED: ButtonS
BUTTON_S_BUTTON_TEST: ButtonS
CURTAIN_OUTDOOR_UNSPECIFIED: CurtainOutdoor
CURTAIN_OUTDOOR_MOVING_SENSOR: CurtainOutdoor
CURTAIN_OUTDOOR_MASKING_SENSOR: CurtainOutdoor
CURTAIN_OUTDOOR_MINI_UNSPECIFIED: CurtainOutdoorMini
CURTAIN_OUTDOOR_MINI_MOVING_SENSOR: CurtainOutdoorMini
CURTAIN_OUTDOOR_MINI_MASKING_SENSOR: CurtainOutdoorMini
MOTION_PROTECT_G3_UNSPECIFIED: MotionProtectG3
MOTION_PROTECT_G3_MOVING_SENSOR: MotionProtectG3
MOTION_PROTECT_G3_MASKING_SENSOR: MotionProtectG3
MOTION_CAM_S_PHOD_AM_UNSPECIFIED: MotionCamSPhodAm
MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: MotionCamSPhodAm
MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: MotionCamSPhodAm
DOUBLE_BUTTON_G3_UNSPECIFIED: DoubleButtonG3
DOUBLE_BUTTON_G3_BUTTON_TEST: DoubleButtonG3
MOTION_CAM_G3_UNSPECIFIED: MotionCamG3
MOTION_CAM_G3_MOVING_SENSOR: MotionCamG3
MOTION_CAM_G3_MASKING_SENSOR: MotionCamG3
CURTAIN_CAM_OUTDOOR_HM_PHOD_UNSPECIFIED: CurtainCamOutdoorHmPhod
CURTAIN_CAM_OUTDOOR_HM_PHOD_ALL_MOTION_SENSORS: CurtainCamOutdoorHmPhod
CURTAIN_CAM_OUTDOOR_HM_PHOD_MASKING_SENSOR: CurtainCamOutdoorHmPhod

class DeviceSensor(_message.Message):
    __slots__ = ("outdoor", "curtain", "dual_curtain", "button_s", "curtain_outdoor", "motion_protect_g3", "motion_cam_s_phod_am", "double_button_g3", "motion_cam_g3", "curtain_outdoor_mini", "curtain_cam_outdoor_hm_phod")
    OUTDOOR_FIELD_NUMBER: _ClassVar[int]
    CURTAIN_FIELD_NUMBER: _ClassVar[int]
    DUAL_CURTAIN_FIELD_NUMBER: _ClassVar[int]
    BUTTON_S_FIELD_NUMBER: _ClassVar[int]
    CURTAIN_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_G3_FIELD_NUMBER: _ClassVar[int]
    MOTION_CAM_S_PHOD_AM_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_BUTTON_G3_FIELD_NUMBER: _ClassVar[int]
    MOTION_CAM_G3_FIELD_NUMBER: _ClassVar[int]
    CURTAIN_OUTDOOR_MINI_FIELD_NUMBER: _ClassVar[int]
    CURTAIN_CAM_OUTDOOR_HM_PHOD_FIELD_NUMBER: _ClassVar[int]
    outdoor: Outdoor
    curtain: Curtain
    dual_curtain: DualCurtain
    button_s: ButtonS
    curtain_outdoor: CurtainOutdoor
    motion_protect_g3: MotionProtectG3
    motion_cam_s_phod_am: MotionCamSPhodAm
    double_button_g3: DoubleButtonG3
    motion_cam_g3: MotionCamG3
    curtain_outdoor_mini: CurtainOutdoorMini
    curtain_cam_outdoor_hm_phod: CurtainCamOutdoorHmPhod
    def __init__(self, outdoor: _Optional[_Union[Outdoor, str]] = ..., curtain: _Optional[_Union[Curtain, str]] = ..., dual_curtain: _Optional[_Union[DualCurtain, str]] = ..., button_s: _Optional[_Union[ButtonS, str]] = ..., curtain_outdoor: _Optional[_Union[CurtainOutdoor, str]] = ..., motion_protect_g3: _Optional[_Union[MotionProtectG3, str]] = ..., motion_cam_s_phod_am: _Optional[_Union[MotionCamSPhodAm, str]] = ..., double_button_g3: _Optional[_Union[DoubleButtonG3, str]] = ..., motion_cam_g3: _Optional[_Union[MotionCamG3, str]] = ..., curtain_outdoor_mini: _Optional[_Union[CurtainOutdoorMini, str]] = ..., curtain_cam_outdoor_hm_phod: _Optional[_Union[CurtainCamOutdoorHmPhod, str]] = ...) -> None: ...
