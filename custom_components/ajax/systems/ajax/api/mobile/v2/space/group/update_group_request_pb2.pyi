from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import followed_group_ids_pb2 as _followed_group_ids_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_auto_arm_pb2 as _group_auto_arm_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_auto_disarm_pb2 as _group_auto_disarm_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import two_stage_arming_mode_pb2 as _two_stage_arming_mode_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.image import image_id_pb2 as _image_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateGroupRequest(_message.Message):
    __slots__ = ("space_locator", "group_id", "group_name", "bulk_arm_involved", "bulk_disarm_involved", "image_id", "two_stage_arming_mode", "image", "following_group_auto_arm", "following_group_auto_disarm", "auto_arm_delay", "followed_group_ids")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    BULK_ARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    BULK_DISARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    FOLLOWED_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    group_id: str
    group_name: str
    bulk_arm_involved: bool
    bulk_disarm_involved: bool
    image_id: str
    two_stage_arming_mode: _two_stage_arming_mode_pb2.TwoStageArmingMode
    image: _image_id_pb2.ImageIdValue
    following_group_auto_arm: _group_auto_arm_pb2.FollowingGroupAutoArm
    following_group_auto_disarm: _group_auto_disarm_pb2.FollowingGroupAutoDisarm
    auto_arm_delay: _duration_pb2.Duration
    followed_group_ids: _followed_group_ids_pb2.FollowedGroupIds
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., group_id: _Optional[str] = ..., group_name: _Optional[str] = ..., bulk_arm_involved: bool = ..., bulk_disarm_involved: bool = ..., image_id: _Optional[str] = ..., two_stage_arming_mode: _Optional[_Union[_two_stage_arming_mode_pb2.TwoStageArmingMode, str]] = ..., image: _Optional[_Union[_image_id_pb2.ImageIdValue, _Mapping]] = ..., following_group_auto_arm: _Optional[_Union[_group_auto_arm_pb2.FollowingGroupAutoArm, str]] = ..., following_group_auto_disarm: _Optional[_Union[_group_auto_disarm_pb2.FollowingGroupAutoDisarm, str]] = ..., auto_arm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., followed_group_ids: _Optional[_Union[_followed_group_ids_pb2.FollowedGroupIds, _Mapping]] = ...) -> None: ...

class UpdateGroupResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_armed", "permission_denied", "group_not_found", "hub_offline", "hub_busy", "hub_error", "hub_wrong_state", "space_locked", "followed_groups_conflict")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        FOLLOWED_GROUPS_CONFLICT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        followed_groups_conflict: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., group_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., followed_groups_conflict: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateGroupResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateGroupResponse.Failure, _Mapping]] = ...) -> None: ...
