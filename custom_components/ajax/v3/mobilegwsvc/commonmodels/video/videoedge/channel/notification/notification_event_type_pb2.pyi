from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ALARM: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_REGULAR: _ClassVar[NotificationEventType]
NOTIFICATION_EVENT_TYPE_UNSPECIFIED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ALARM: NotificationEventType
NOTIFICATION_EVENT_TYPE_REGULAR: NotificationEventType
