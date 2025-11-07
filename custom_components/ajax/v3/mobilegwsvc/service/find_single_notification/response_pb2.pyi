from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import notification_pb2 as _notification_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindSingleNotificationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("notification",)
        NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        notification: _notification_pb2.Notification
        def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindSingleNotificationResponse.Success
    failure: FindSingleNotificationResponse.Failure
    def __init__(self, success: _Optional[_Union[FindSingleNotificationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindSingleNotificationResponse.Failure, _Mapping]] = ...) -> None: ...
