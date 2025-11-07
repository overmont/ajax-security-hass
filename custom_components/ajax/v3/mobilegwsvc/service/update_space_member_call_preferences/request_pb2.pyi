from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberCallPreferencesRequest(_message.Message):
    __slots__ = ("hub_id", "member_id", "call_preferences_patches")
    class CallPreferencesPatch(_message.Message):
        __slots__ = ("call_preference", "enabled")
        CALL_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        call_preference: _display_member_notification_preferences_pb2.DisplayMemberCallPreference
        enabled: bool
        def __init__(self, call_preference: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberCallPreference, str]] = ..., enabled: bool = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_PREFERENCES_PATCHES_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    member_id: str
    call_preferences_patches: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberCallPreferencesRequest.CallPreferencesPatch]
    def __init__(self, hub_id: _Optional[str] = ..., member_id: _Optional[str] = ..., call_preferences_patches: _Optional[_Iterable[_Union[UpdateSpaceMemberCallPreferencesRequest.CallPreferencesPatch, _Mapping]]] = ...) -> None: ...
