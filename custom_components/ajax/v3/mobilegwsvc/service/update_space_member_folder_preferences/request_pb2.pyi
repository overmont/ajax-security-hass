from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberFolderPreferencesRequest(_message.Message):
    __slots__ = ("preference_patch",)
    class FolderPreferencesPatch(_message.Message):
        __slots__ = ("space_id", "member_id", "folder_preferences_patch")
        class FolderPreferencePatch(_message.Message):
            __slots__ = ("preference", "enabled")
            PREFERENCE_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            preference: _display_member_notification_preferences_pb2.DisplayMemberFolderPreference
            enabled: bool
            def __init__(self, preference: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberFolderPreference, str]] = ..., enabled: bool = ...) -> None: ...
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        FOLDER_PREFERENCES_PATCH_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        member_id: str
        folder_preferences_patch: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch.FolderPreferencePatch]
        def __init__(self, space_id: _Optional[str] = ..., member_id: _Optional[str] = ..., folder_preferences_patch: _Optional[_Iterable[_Union[UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch.FolderPreferencePatch, _Mapping]]] = ...) -> None: ...
    PREFERENCE_PATCH_FIELD_NUMBER: _ClassVar[int]
    preference_patch: UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch
    def __init__(self, preference_patch: _Optional[_Union[UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch, _Mapping]] = ...) -> None: ...
