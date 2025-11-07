from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import origin_id_pb2 as _origin_id_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import media_pb2 as _media_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamNotificationMediaRequest(_message.Message):
    __slots__ = ("notification_id", "origin")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    origin: _origin_id_pb2.NotificationOriginId
    def __init__(self, notification_id: _Optional[str] = ..., origin: _Optional[_Union[_origin_id_pb2.NotificationOriginId, _Mapping]] = ...) -> None: ...

class StreamNotificationMediaResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("media",)
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        media: _media_pb2.NotificationMedia
        def __init__(self, media: _Optional[_Union[_media_pb2.NotificationMedia, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "not_found", "internal_error", "media_expired", "permission_denied")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        MEDIA_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.DefaultError
        not_found: _response_pb2.DefaultError
        internal_error: _response_pb2.DefaultError
        media_expired: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., internal_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., media_expired: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamNotificationMediaResponse.Success
    failure: StreamNotificationMediaResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamNotificationMediaResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamNotificationMediaResponse.Failure, _Mapping]] = ...) -> None: ...
