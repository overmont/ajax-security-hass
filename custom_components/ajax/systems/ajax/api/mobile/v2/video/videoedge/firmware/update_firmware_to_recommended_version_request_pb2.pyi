from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import firmware_version_pb2 as _firmware_version_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateFirmwareToRecommendedVersionRequest(_message.Message):
    __slots__ = ("video_edge_id", "acknowledged_firmware_version", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    acknowledged_firmware_version: _firmware_version_pb2.FirmwareVersion
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., acknowledged_firmware_version: _Optional[_Union[_firmware_version_pb2.FirmwareVersion, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class UpdateFirmwareToRecommendedVersionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "firmware_update_already_in_progress", "no_available_firmware_update", "acknowledged_firmware_version_mismatch", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_UPDATE_ALREADY_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        NO_AVAILABLE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        ACKNOWLEDGED_FIRMWARE_VERSION_MISMATCH_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        firmware_update_already_in_progress: _response_pb2.DefaultError
        no_available_firmware_update: _response_pb2.DefaultError
        acknowledged_firmware_version_mismatch: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., firmware_update_already_in_progress: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., no_available_firmware_update: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., acknowledged_firmware_version_mismatch: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateFirmwareToRecommendedVersionResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateFirmwareToRecommendedVersionResponse.Failure, _Mapping]] = ...) -> None: ...
