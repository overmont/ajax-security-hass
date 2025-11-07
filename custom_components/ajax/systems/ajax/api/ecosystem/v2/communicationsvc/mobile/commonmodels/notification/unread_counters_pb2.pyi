from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import folder_pb2 as _folder_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnreadNotificationCounters(_message.Message):
    __slots__ = ("counters",)
    class UnreadCounterEntry(_message.Message):
        __slots__ = ("folder", "unread_events_count")
        FOLDER_FIELD_NUMBER: _ClassVar[int]
        UNREAD_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        folder: _folder_pb2.NotificationFolder
        unread_events_count: int
        def __init__(self, folder: _Optional[_Union[_folder_pb2.NotificationFolder, str]] = ..., unread_events_count: _Optional[int] = ...) -> None: ...
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    counters: _containers.RepeatedCompositeFieldContainer[UnreadNotificationCounters.UnreadCounterEntry]
    def __init__(self, counters: _Optional[_Iterable[_Union[UnreadNotificationCounters.UnreadCounterEntry, _Mapping]]] = ...) -> None: ...
