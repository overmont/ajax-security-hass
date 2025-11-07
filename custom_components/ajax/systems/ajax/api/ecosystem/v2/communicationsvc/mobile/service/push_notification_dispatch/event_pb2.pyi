from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_pb2 as _notification_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import media_pb2 as _media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import offline_event_count_pb2 as _offline_event_count_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import new_user_session_pb2 as _new_user_session_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import media_enriched_notification_pb2 as _media_enriched_notification_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import session_invalidation_notification_pb2 as _session_invalidation_notification_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushNotificationDispatchEvent(_message.Message):
    __slots__ = ("notification", "offline_event_count", "new_user_session", "media_enriched_notification", "session_invalidation")
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_SESSION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ENRICHED_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_INVALIDATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    offline_event_count: _offline_event_count_pb2.OfflineEventCount
    new_user_session: _new_user_session_pb2.NewUserSession
    media_enriched_notification: _media_enriched_notification_pb2.MediaEnrichedNotification
    session_invalidation: _session_invalidation_notification_pb2.SessionInvalidation
    def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ..., offline_event_count: _Optional[_Union[_offline_event_count_pb2.OfflineEventCount, _Mapping]] = ..., new_user_session: _Optional[_Union[_new_user_session_pb2.NewUserSession, _Mapping]] = ..., media_enriched_notification: _Optional[_Union[_media_enriched_notification_pb2.MediaEnrichedNotification, _Mapping]] = ..., session_invalidation: _Optional[_Union[_session_invalidation_notification_pb2.SessionInvalidation, _Mapping]] = ...) -> None: ...
