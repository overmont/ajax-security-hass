from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_pb2 as _notification_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamUnconfirmedAlarmEventsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "created", "updated")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamUnconfirmedAlarmEventsResponse.Notifications
        created: StreamUnconfirmedAlarmEventsResponse.Notifications
        updated: StreamUnconfirmedAlarmEventsResponse.Notifications
        def __init__(self, snapshot: _Optional[_Union[StreamUnconfirmedAlarmEventsResponse.Notifications, _Mapping]] = ..., created: _Optional[_Union[StreamUnconfirmedAlarmEventsResponse.Notifications, _Mapping]] = ..., updated: _Optional[_Union[StreamUnconfirmedAlarmEventsResponse.Notifications, _Mapping]] = ...) -> None: ...
    class Notifications(_message.Message):
        __slots__ = ("notifications",)
        NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        notifications: _containers.RepeatedCompositeFieldContainer[_notification_pb2.Notification]
        def __init__(self, notifications: _Optional[_Iterable[_Union[_notification_pb2.Notification, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("not_found", "illegal_argument", "request_timeout")
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        not_found: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        def __init__(self, not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamUnconfirmedAlarmEventsResponse.Success
    failure: StreamUnconfirmedAlarmEventsResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamUnconfirmedAlarmEventsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamUnconfirmedAlarmEventsResponse.Failure, _Mapping]] = ...) -> None: ...
