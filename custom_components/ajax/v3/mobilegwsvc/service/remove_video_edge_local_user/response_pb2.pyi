from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveVideoEdgeLocalUserResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_armed", "permission_denied", "video_edge_is_offline", "command_not_supported", "local_user_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        LOCAL_USER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        command_not_supported: _response_pb2.Error
        local_user_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., command_not_supported: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., local_user_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RemoveVideoEdgeLocalUserResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[RemoveVideoEdgeLocalUserResponse.Failure, _Mapping]] = ...) -> None: ...
