from v1.common import notification_channel_pb2 as _notification_channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSettings(_message.Message):
    __slots__ = ("alarms", "events", "malfunctions", "armings")
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ARMINGS_FIELD_NUMBER: _ClassVar[int]
    alarms: _containers.RepeatedScalarFieldContainer[_notification_channel_pb2.NotificationChannel]
    events: _containers.RepeatedScalarFieldContainer[_notification_channel_pb2.NotificationChannel]
    malfunctions: _containers.RepeatedScalarFieldContainer[_notification_channel_pb2.NotificationChannel]
    armings: _containers.RepeatedScalarFieldContainer[_notification_channel_pb2.NotificationChannel]
    def __init__(self, alarms: _Optional[_Iterable[_Union[_notification_channel_pb2.NotificationChannel, str]]] = ..., events: _Optional[_Iterable[_Union[_notification_channel_pb2.NotificationChannel, str]]] = ..., malfunctions: _Optional[_Iterable[_Union[_notification_channel_pb2.NotificationChannel, str]]] = ..., armings: _Optional[_Iterable[_Union[_notification_channel_pb2.NotificationChannel, str]]] = ...) -> None: ...
