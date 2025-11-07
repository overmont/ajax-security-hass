from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import folder_pb2 as _folder_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import origin_id_pb2 as _origin_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkNotificationsAsReadRequest(_message.Message):
    __slots__ = ("origin", "mark_as_read")
    class Action(_message.Message):
        __slots__ = ("all", "all_in_folder", "some_in_folder")
        class AllNotifications(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AllNotificationsInFolder(_message.Message):
            __slots__ = ("folder",)
            FOLDER_FIELD_NUMBER: _ClassVar[int]
            folder: _folder_pb2.NotificationFolder
            def __init__(self, folder: _Optional[_Union[_folder_pb2.NotificationFolder, str]] = ...) -> None: ...
        class SomeNotificationsInFolder(_message.Message):
            __slots__ = ("folder", "read_notifications_tokens")
            FOLDER_FIELD_NUMBER: _ClassVar[int]
            READ_NOTIFICATIONS_TOKENS_FIELD_NUMBER: _ClassVar[int]
            folder: _folder_pb2.NotificationFolder
            read_notifications_tokens: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, folder: _Optional[_Union[_folder_pb2.NotificationFolder, str]] = ..., read_notifications_tokens: _Optional[_Iterable[str]] = ...) -> None: ...
        ALL_FIELD_NUMBER: _ClassVar[int]
        ALL_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
        SOME_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
        all: MarkNotificationsAsReadRequest.Action.AllNotifications
        all_in_folder: MarkNotificationsAsReadRequest.Action.AllNotificationsInFolder
        some_in_folder: MarkNotificationsAsReadRequest.Action.SomeNotificationsInFolder
        def __init__(self, all: _Optional[_Union[MarkNotificationsAsReadRequest.Action.AllNotifications, _Mapping]] = ..., all_in_folder: _Optional[_Union[MarkNotificationsAsReadRequest.Action.AllNotificationsInFolder, _Mapping]] = ..., some_in_folder: _Optional[_Union[MarkNotificationsAsReadRequest.Action.SomeNotificationsInFolder, _Mapping]] = ...) -> None: ...
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MARK_AS_READ_FIELD_NUMBER: _ClassVar[int]
    origin: _origin_id_pb2.NotificationOriginId
    mark_as_read: _containers.RepeatedCompositeFieldContainer[MarkNotificationsAsReadRequest.Action]
    def __init__(self, origin: _Optional[_Union[_origin_id_pb2.NotificationOriginId, _Mapping]] = ..., mark_as_read: _Optional[_Iterable[_Union[MarkNotificationsAsReadRequest.Action, _Mapping]]] = ...) -> None: ...

class MarkNotificationsAsReadResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
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
    success: MarkNotificationsAsReadResponse.Success
    failure: MarkNotificationsAsReadResponse.Failure
    def __init__(self, success: _Optional[_Union[MarkNotificationsAsReadResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[MarkNotificationsAsReadResponse.Failure, _Mapping]] = ...) -> None: ...
