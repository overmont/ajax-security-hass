from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_pb2 as _notification_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineNotificationsData(_message.Message):
    __slots__ = ("parent_notification_id", "notifications")
    PARENT_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    parent_notification_id: str
    notifications: _containers.RepeatedCompositeFieldContainer[_notification_pb2.Notification]
    def __init__(self, parent_notification_id: _Optional[str] = ..., notifications: _Optional[_Iterable[_Union[_notification_pb2.Notification, _Mapping]]] = ...) -> None: ...
