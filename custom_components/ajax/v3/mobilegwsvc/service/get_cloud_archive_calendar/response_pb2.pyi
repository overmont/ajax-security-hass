from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import calendar_pb2 as _calendar_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCloudArchiveCalendarResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("calendar",)
        CALENDAR_FIELD_NUMBER: _ClassVar[int]
        calendar: _calendar_pb2.Calendar
        def __init__(self, calendar: _Optional[_Union[_calendar_pb2.Calendar, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetCloudArchiveCalendarResponse.Success
    failure: GetCloudArchiveCalendarResponse.Failure
    def __init__(self, success: _Optional[_Union[GetCloudArchiveCalendarResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetCloudArchiveCalendarResponse.Failure, _Mapping]] = ...) -> None: ...
