from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberPushPreferencesRequest(_message.Message):
    __slots__ = ("space_locator", "member_id", "push_preferences_patch", "push_preferences_patches", "push_preferences_patch_v2")
    class PushPreferencesPatch(_message.Message):
        __slots__ = ("push_preference", "enabled")
        PUSH_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        push_preference: _display_member_notification_preferences_pb2.DisplayMemberPushPreference
        enabled: bool
        def __init__(self, push_preference: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberPushPreference, str]] = ..., enabled: bool = ...) -> None: ...
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PUSH_PREFERENCES_PATCH_FIELD_NUMBER: _ClassVar[int]
    PUSH_PREFERENCES_PATCHES_FIELD_NUMBER: _ClassVar[int]
    PUSH_PREFERENCES_PATCH_V2_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    member_id: str
    push_preferences_patch: UpdateSpaceMemberPushPreferencesRequest.PushPreferencesPatch
    push_preferences_patches: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberPushPreferencesRequest.PushPreferencesPatch]
    push_preferences_patch_v2: _display_member_notification_preferences_pb2.DisplayMemberPushPreferencesV2
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., member_id: _Optional[str] = ..., push_preferences_patch: _Optional[_Union[UpdateSpaceMemberPushPreferencesRequest.PushPreferencesPatch, _Mapping]] = ..., push_preferences_patches: _Optional[_Iterable[_Union[UpdateSpaceMemberPushPreferencesRequest.PushPreferencesPatch, _Mapping]]] = ..., push_preferences_patch_v2: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberPushPreferencesV2, _Mapping]] = ...) -> None: ...

class UpdateSpaceMemberPushPreferencesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSpaceMemberPushPreferencesResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateSpaceMemberPushPreferencesResponse.Failure, _Mapping]] = ...) -> None: ...
