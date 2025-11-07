from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import cloud_archive_pb2 as _cloud_archive_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import duration_option_pb2 as _duration_option_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoCloudArchiveStorageInfoResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("cloud_archive_status", "cloud_archive_settings_available", "archive_depth", "max_archive_depth", "available_max_cloud_archive_depth_options")
        CLOUD_ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_SETTINGS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_DEPTH_FIELD_NUMBER: _ClassVar[int]
        MAX_ARCHIVE_DEPTH_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MAX_CLOUD_ARCHIVE_DEPTH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        cloud_archive_status: _cloud_archive_pb2.CloudArchive.CloudArchiveStatus
        cloud_archive_settings_available: bool
        archive_depth: _duration_pb2.Duration
        max_archive_depth: _duration_option_pb2.DurationOption
        available_max_cloud_archive_depth_options: _containers.RepeatedScalarFieldContainer[_duration_option_pb2.DurationOption]
        def __init__(self, cloud_archive_status: _Optional[_Union[_cloud_archive_pb2.CloudArchive.CloudArchiveStatus, str]] = ..., cloud_archive_settings_available: bool = ..., archive_depth: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_archive_depth: _Optional[_Union[_duration_option_pb2.DurationOption, str]] = ..., available_max_cloud_archive_depth_options: _Optional[_Iterable[_Union[_duration_option_pb2.DurationOption, str]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "video_edge_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoCloudArchiveStorageInfoResponse.Success
    failure: GetVideoCloudArchiveStorageInfoResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVideoCloudArchiveStorageInfoResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetVideoCloudArchiveStorageInfoResponse.Failure, _Mapping]] = ...) -> None: ...
