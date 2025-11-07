from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import followed_group_ids_pb2 as _followed_group_ids_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_auto_arm_pb2 as _group_auto_arm_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_auto_disarm_pb2 as _group_auto_disarm_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import two_stage_arming_mode_pb2 as _two_stage_arming_mode_pb2
from systems.ajax.api.mobile.v2.common.space import displayed_chime_status_pb2 as _displayed_chime_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "name", "images", "bulk_arm_involved", "bulk_disarm_involved", "two_stage_arming_mode", "sorting_key", "chime_status", "following_group_auto_arm", "following_group_auto_disarm", "auto_arm_delay", "followed_group_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    BULK_ARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    BULK_DISARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    CHIME_STATUS_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    FOLLOWED_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    images: _image_pb2.Images
    bulk_arm_involved: bool
    bulk_disarm_involved: bool
    two_stage_arming_mode: _two_stage_arming_mode_pb2.TwoStageArmingMode
    sorting_key: str
    chime_status: _displayed_chime_status_pb2.DisplayedChimeStatus
    following_group_auto_arm: _group_auto_arm_pb2.FollowingGroupAutoArm
    following_group_auto_disarm: _group_auto_disarm_pb2.FollowingGroupAutoDisarm
    auto_arm_delay: _duration_pb2.Duration
    followed_group_ids: _followed_group_ids_pb2.FollowedGroupIds
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., bulk_arm_involved: bool = ..., bulk_disarm_involved: bool = ..., two_stage_arming_mode: _Optional[_Union[_two_stage_arming_mode_pb2.TwoStageArmingMode, str]] = ..., sorting_key: _Optional[str] = ..., chime_status: _Optional[_Union[_displayed_chime_status_pb2.DisplayedChimeStatus, str]] = ..., following_group_auto_arm: _Optional[_Union[_group_auto_arm_pb2.FollowingGroupAutoArm, str]] = ..., following_group_auto_disarm: _Optional[_Union[_group_auto_disarm_pb2.FollowingGroupAutoDisarm, str]] = ..., auto_arm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., followed_group_ids: _Optional[_Union[_followed_group_ids_pb2.FollowedGroupIds, _Mapping]] = ...) -> None: ...
