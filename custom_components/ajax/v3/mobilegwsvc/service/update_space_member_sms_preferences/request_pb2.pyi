from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberSmsPreferencesRequest(_message.Message):
    __slots__ = ("hub_id", "member_id", "sms_preferences_patches")
    class SmsPreferencesPatch(_message.Message):
        __slots__ = ("sms_preference", "enabled")
        SMS_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        sms_preference: _display_member_notification_preferences_pb2.DisplayMemberSmsPreference
        enabled: bool
        def __init__(self, sms_preference: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberSmsPreference, str]] = ..., enabled: bool = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_PREFERENCES_PATCHES_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    member_id: str
    sms_preferences_patches: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberSmsPreferencesRequest.SmsPreferencesPatch]
    def __init__(self, hub_id: _Optional[str] = ..., member_id: _Optional[str] = ..., sms_preferences_patches: _Optional[_Iterable[_Union[UpdateSpaceMemberSmsPreferencesRequest.SmsPreferencesPatch, _Mapping]]] = ...) -> None: ...
