from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import release_notes_pb2 as _release_notes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindVideoEdgeFirmwareReleaseNotesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("release_notes",)
        RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
        release_notes: _release_notes_pb2.ReleaseNotes
        def __init__(self, release_notes: _Optional[_Union[_release_notes_pb2.ReleaseNotes, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "firmware_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        firmware_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., firmware_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindVideoEdgeFirmwareReleaseNotesResponse.Success
    failure: FindVideoEdgeFirmwareReleaseNotesResponse.Failure
    def __init__(self, success: _Optional[_Union[FindVideoEdgeFirmwareReleaseNotesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindVideoEdgeFirmwareReleaseNotesResponse.Failure, _Mapping]] = ...) -> None: ...
