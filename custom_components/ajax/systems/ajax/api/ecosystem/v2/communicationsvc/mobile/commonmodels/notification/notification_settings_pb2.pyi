from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_channel_pb2 as _notification_channel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSettings(_message.Message):
    __slots__ = ("alarms", "events", "malfunctions", "armings")
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ARMINGS_FIELD_NUMBER: _ClassVar[int]
    alarms: _notification_channel_pb2.NotificationChannels
    events: _notification_channel_pb2.NotificationChannels
    malfunctions: _notification_channel_pb2.NotificationChannels
    armings: _notification_channel_pb2.NotificationChannels
    def __init__(self, alarms: _Optional[_Union[_notification_channel_pb2.NotificationChannels, _Mapping]] = ..., events: _Optional[_Union[_notification_channel_pb2.NotificationChannels, _Mapping]] = ..., malfunctions: _Optional[_Union[_notification_channel_pb2.NotificationChannels, _Mapping]] = ..., armings: _Optional[_Union[_notification_channel_pb2.NotificationChannels, _Mapping]] = ...) -> None: ...
