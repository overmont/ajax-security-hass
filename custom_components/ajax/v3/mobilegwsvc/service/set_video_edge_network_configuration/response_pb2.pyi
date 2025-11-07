from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeNetworkConfigurationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_not_found", "video_edge_not_found", "video_edge_is_offline", "network_interface_not_found", "network_interface_configuration_in_progress", "operation_timeout", "configuration_apply_failed", "hub_is_busy")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        OPERATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_APPLY_FAILED_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        network_interface_not_found: _response_pb2.Error
        network_interface_configuration_in_progress: _response_pb2.Error
        operation_timeout: _response_pb2.Error
        configuration_apply_failed: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., network_interface_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., network_interface_configuration_in_progress: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., operation_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., configuration_apply_failed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_is_busy: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetVideoEdgeNetworkConfigurationResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SetVideoEdgeNetworkConfigurationResponse.Failure, _Mapping]] = ...) -> None: ...
