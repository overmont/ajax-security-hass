from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_pb2 as _notification_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import filter_pb2 as _filter_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import offline_notifications_data_pb2 as _offline_notifications_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindNotificationsRequest(_message.Message):
    __slots__ = ("filter", "limit", "pagination")
    class Pagination(_message.Message):
        __slots__ = ("forward_pagination_token", "backward_pagination_token")
        FORWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        BACKWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        forward_pagination_token: str
        backward_pagination_token: str
        def __init__(self, forward_pagination_token: _Optional[str] = ..., backward_pagination_token: _Optional[str] = ...) -> None: ...
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.NotificationsFilter
    limit: int
    pagination: FindNotificationsRequest.Pagination
    def __init__(self, filter: _Optional[_Union[_filter_pb2.NotificationsFilter, _Mapping]] = ..., limit: _Optional[int] = ..., pagination: _Optional[_Union[FindNotificationsRequest.Pagination, _Mapping]] = ...) -> None: ...

class FindNotificationsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("notifications", "next_forward_pagination_token", "next_backward_pagination_token", "offline_notifications_data")
        NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        NEXT_FORWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        NEXT_BACKWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_NOTIFICATIONS_DATA_FIELD_NUMBER: _ClassVar[int]
        notifications: _containers.RepeatedCompositeFieldContainer[_notification_pb2.Notification]
        next_forward_pagination_token: str
        next_backward_pagination_token: str
        offline_notifications_data: _containers.RepeatedCompositeFieldContainer[_offline_notifications_data_pb2.OfflineNotificationsData]
        def __init__(self, notifications: _Optional[_Iterable[_Union[_notification_pb2.Notification, _Mapping]]] = ..., next_forward_pagination_token: _Optional[str] = ..., next_backward_pagination_token: _Optional[str] = ..., offline_notifications_data: _Optional[_Iterable[_Union[_offline_notifications_data_pb2.OfflineNotificationsData, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "not_found", "internal_error")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.DefaultError
        not_found: _response_pb2.DefaultError
        internal_error: _response_pb2.DefaultError
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., internal_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindNotificationsResponse.Success
    failure: FindNotificationsResponse.Failure
    def __init__(self, success: _Optional[_Union[FindNotificationsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindNotificationsResponse.Failure, _Mapping]] = ...) -> None: ...
