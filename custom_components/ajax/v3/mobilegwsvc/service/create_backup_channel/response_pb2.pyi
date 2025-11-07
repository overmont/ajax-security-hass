from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBackupChannelResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "hub_not_found", "space_armed", "hub_error", "search_timeout", "hub_is_busy", "wrong_hub_state", "objects_limit_exceeded", "hub_device_already_added", "unknown_hub_device", "unsupported_hub_device", "need_update_hub_firmware", "hub_offline", "video_edge_is_offline", "mcu_io_error", "mcu_invalid_state", "mcu_no_response_from_mcu")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        WRONG_HUB_STATE_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_ALREADY_ADDED_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        UNSUPPORTED_HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        NEED_UPDATE_HUB_FIRMWARE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        MCU_IO_ERROR_FIELD_NUMBER: _ClassVar[int]
        MCU_INVALID_STATE_FIELD_NUMBER: _ClassVar[int]
        MCU_NO_RESPONSE_FROM_MCU_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        hub_error: _response_pb2.Error
        search_timeout: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        wrong_hub_state: _response_pb2.Error
        objects_limit_exceeded: _response_pb2.Error
        hub_device_already_added: _response_pb2.Error
        unknown_hub_device: _response_pb2.Error
        unsupported_hub_device: _response_pb2.Error
        need_update_hub_firmware: _response_pb2.Error
        hub_offline: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        mcu_io_error: _response_pb2.Error
        mcu_invalid_state: _response_pb2.Error
        mcu_no_response_from_mcu: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., search_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_is_busy: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., wrong_hub_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., objects_limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_device_already_added: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unknown_hub_device: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unsupported_hub_device: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., need_update_hub_firmware: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., mcu_io_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., mcu_invalid_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., mcu_no_response_from_mcu: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateBackupChannelResponse.Success
    failure: CreateBackupChannelResponse.Failure
    def __init__(self, success: _Optional[_Union[CreateBackupChannelResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CreateBackupChannelResponse.Failure, _Mapping]] = ...) -> None: ...
