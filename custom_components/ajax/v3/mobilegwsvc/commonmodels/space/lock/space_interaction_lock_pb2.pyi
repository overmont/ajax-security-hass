from v3.mobilegwsvc.commonmodels.space.lock import alarm_spam_notification_pb2 as _alarm_spam_notification_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceInteractionLock(_message.Message):
    __slots__ = ("alarm_spam_notification",)
    ALARM_SPAM_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    alarm_spam_notification: _alarm_spam_notification_pb2.AlarmSpamNotification
    def __init__(self, alarm_spam_notification: _Optional[_Union[_alarm_spam_notification_pb2.AlarmSpamNotification, _Mapping]] = ...) -> None: ...
