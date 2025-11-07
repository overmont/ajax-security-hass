from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import time_zone_pb2 as _time_zone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllCloudArchiveMetadataFragmentsInfoResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("fragments_info", "time_zone_map")
        class MetadataFragmentInfo(_message.Message):
            __slots__ = ("fragment_id", "timestamp", "duration")
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            timestamp: _timestamp_pb2.Timestamp
            duration: _duration_pb2.Duration
            def __init__(self, fragment_id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        FRAGMENTS_INFO_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_MAP_FIELD_NUMBER: _ClassVar[int]
        fragments_info: _containers.RepeatedCompositeFieldContainer[FindAllCloudArchiveMetadataFragmentsInfoResponse.Success.MetadataFragmentInfo]
        time_zone_map: _containers.RepeatedCompositeFieldContainer[_time_zone_pb2.TimeZone]
        def __init__(self, fragments_info: _Optional[_Iterable[_Union[FindAllCloudArchiveMetadataFragmentsInfoResponse.Success.MetadataFragmentInfo, _Mapping]]] = ..., time_zone_map: _Optional[_Iterable[_Union[_time_zone_pb2.TimeZone, _Mapping]]] = ...) -> None: ...
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
    success: FindAllCloudArchiveMetadataFragmentsInfoResponse.Success
    failure: FindAllCloudArchiveMetadataFragmentsInfoResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAllCloudArchiveMetadataFragmentsInfoResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAllCloudArchiveMetadataFragmentsInfoResponse.Failure, _Mapping]] = ...) -> None: ...
