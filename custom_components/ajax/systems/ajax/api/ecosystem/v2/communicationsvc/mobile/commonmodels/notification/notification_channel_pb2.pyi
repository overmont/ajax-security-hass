from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_NOTIFICATION_CHANNEL_INFO: _ClassVar[NotificationChannel]
    PUSH: _ClassVar[NotificationChannel]
    SMS: _ClassVar[NotificationChannel]
    CALL: _ClassVar[NotificationChannel]
NO_NOTIFICATION_CHANNEL_INFO: NotificationChannel
PUSH: NotificationChannel
SMS: NotificationChannel
CALL: NotificationChannel

class NotificationChannels(_message.Message):
    __slots__ = ("channels",)
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedScalarFieldContainer[NotificationChannel]
    def __init__(self, channels: _Optional[_Iterable[_Union[NotificationChannel, str]]] = ...) -> None: ...
