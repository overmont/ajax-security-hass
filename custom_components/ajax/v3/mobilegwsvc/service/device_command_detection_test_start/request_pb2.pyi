from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from v3.mobilegwsvc.commonmodels.sensor import detection_zone_test_sensor_pb2 as _detection_zone_test_sensor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDetectionTestStartRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "object_type", "additional_param", "device_sensor")
    class Outdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTDOOR_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_UPPER_PIR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_LOWER_PIR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_MASKING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
    OUTDOOR_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_UPPER_PIR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_LOWER_PIR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_MASKING_SENSOR: DeviceCommandDetectionTestStartRequest.Outdoor
    class Curtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURTAIN_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.Curtain]
        CURTAIN_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.Curtain]
        CURTAIN_MASKING_SENSORS: _ClassVar[DeviceCommandDetectionTestStartRequest.Curtain]
    CURTAIN_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.Curtain
    CURTAIN_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.Curtain
    CURTAIN_MASKING_SENSORS: DeviceCommandDetectionTestStartRequest.Curtain
    class DualCurtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DUAL_CURTAIN_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.DualCurtain]
        DUAL_CURTAIN_ALL_PIR_SENSORS: _ClassVar[DeviceCommandDetectionTestStartRequest.DualCurtain]
        DUAL_CURTAIN_UPPER_PIR_SENSORS: _ClassVar[DeviceCommandDetectionTestStartRequest.DualCurtain]
        DUAL_CURTAIN_LOWER_PIR_SENSORS: _ClassVar[DeviceCommandDetectionTestStartRequest.DualCurtain]
        DUAL_CURTAIN_MASKING_SENSORS: _ClassVar[DeviceCommandDetectionTestStartRequest.DualCurtain]
    DUAL_CURTAIN_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_ALL_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_UPPER_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_LOWER_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_MASKING_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    class ButtonS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUTTON_S_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.ButtonS]
        BUTTON_S_BUTTON_TEST: _ClassVar[DeviceCommandDetectionTestStartRequest.ButtonS]
    BUTTON_S_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.ButtonS
    BUTTON_S_BUTTON_TEST: DeviceCommandDetectionTestStartRequest.ButtonS
    class CurtainOutdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURTAIN_OUTDOOR_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.CurtainOutdoor]
        CURTAIN_OUTDOOR_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.CurtainOutdoor]
        CURTAIN_OUTDOOR_MASKING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.CurtainOutdoor]
    CURTAIN_OUTDOOR_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    CURTAIN_OUTDOOR_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    CURTAIN_OUTDOOR_MASKING_SENSOR: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    class MotionProtectG3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_PROTECT_G3_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionProtectG3]
        MOTION_PROTECT_G3_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionProtectG3]
        MOTION_PROTECT_G3_MASKING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionProtectG3]
    MOTION_PROTECT_G3_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.MotionProtectG3
    MOTION_PROTECT_G3_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.MotionProtectG3
    MOTION_PROTECT_G3_MASKING_SENSOR: DeviceCommandDetectionTestStartRequest.MotionProtectG3
    class MotionCamSPhodAm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_CAM_S_PHOD_AM_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm]
        MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm]
        MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm]
    MOTION_CAM_S_PHOD_AM_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    class AdditionalParam(_message.Message):
        __slots__ = ("outdoor", "curtain", "dual_curtain", "button_s", "curtain_outdoor", "motion_protect_g3", "motion_cam_s_phod_am")
        OUTDOOR_FIELD_NUMBER: _ClassVar[int]
        CURTAIN_FIELD_NUMBER: _ClassVar[int]
        DUAL_CURTAIN_FIELD_NUMBER: _ClassVar[int]
        BUTTON_S_FIELD_NUMBER: _ClassVar[int]
        CURTAIN_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
        MOTION_PROTECT_G3_FIELD_NUMBER: _ClassVar[int]
        MOTION_CAM_S_PHOD_AM_FIELD_NUMBER: _ClassVar[int]
        outdoor: DeviceCommandDetectionTestStartRequest.Outdoor
        curtain: DeviceCommandDetectionTestStartRequest.Curtain
        dual_curtain: DeviceCommandDetectionTestStartRequest.DualCurtain
        button_s: DeviceCommandDetectionTestStartRequest.ButtonS
        curtain_outdoor: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
        motion_protect_g3: DeviceCommandDetectionTestStartRequest.MotionProtectG3
        motion_cam_s_phod_am: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
        def __init__(self, outdoor: _Optional[_Union[DeviceCommandDetectionTestStartRequest.Outdoor, str]] = ..., curtain: _Optional[_Union[DeviceCommandDetectionTestStartRequest.Curtain, str]] = ..., dual_curtain: _Optional[_Union[DeviceCommandDetectionTestStartRequest.DualCurtain, str]] = ..., button_s: _Optional[_Union[DeviceCommandDetectionTestStartRequest.ButtonS, str]] = ..., curtain_outdoor: _Optional[_Union[DeviceCommandDetectionTestStartRequest.CurtainOutdoor, str]] = ..., motion_protect_g3: _Optional[_Union[DeviceCommandDetectionTestStartRequest.MotionProtectG3, str]] = ..., motion_cam_s_phod_am: _Optional[_Union[DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm, str]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    additional_param: DeviceCommandDetectionTestStartRequest.AdditionalParam
    device_sensor: _detection_zone_test_sensor_pb2.DeviceSensor
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., additional_param: _Optional[_Union[DeviceCommandDetectionTestStartRequest.AdditionalParam, _Mapping]] = ..., device_sensor: _Optional[_Union[_detection_zone_test_sensor_pb2.DeviceSensor, _Mapping]] = ...) -> None: ...
