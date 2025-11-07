from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.hub.device import motion_cam_video_base_pb2 as _motion_cam_video_base_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeIntrusionSettingsRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "arm_delay_seconds", "alarm_delay_seconds", "night_mode_arm_delay_seconds", "night_mode_alarm_delay_seconds", "arming_mode", "siren_triggers")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    arm_delay_seconds: int
    alarm_delay_seconds: int
    night_mode_arm_delay_seconds: int
    night_mode_alarm_delay_seconds: int
    arming_mode: _common_arming_part_pb2.CommonArmingPart.ArmingMode
    siren_triggers: _containers.RepeatedScalarFieldContainer[_motion_cam_video_base_pb2.MotionCamVideoBase.SirenTrigger]
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., arm_delay_seconds: _Optional[int] = ..., alarm_delay_seconds: _Optional[int] = ..., night_mode_arm_delay_seconds: _Optional[int] = ..., night_mode_alarm_delay_seconds: _Optional[int] = ..., arming_mode: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart.ArmingMode, str]] = ..., siren_triggers: _Optional[_Iterable[_Union[_motion_cam_video_base_pb2.MotionCamVideoBase.SirenTrigger, str]]] = ...) -> None: ...
