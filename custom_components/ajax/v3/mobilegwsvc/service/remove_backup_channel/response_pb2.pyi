from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveBackupChannelResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "hub_not_found", "space_armed", "hub_error", "hub_is_busy", "wrong_hub_state", "hub_device_not_found", "hub_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        WRONG_HUB_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        wrong_hub_state: _response_pb2.Error
        hub_device_not_found: _response_pb2.Error
        hub_offline: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_is_busy: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., wrong_hub_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_device_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RemoveBackupChannelResponse.Success
    failure: RemoveBackupChannelResponse.Failure
    def __init__(self, success: _Optional[_Union[RemoveBackupChannelResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[RemoveBackupChannelResponse.Failure, _Mapping]] = ...) -> None: ...
