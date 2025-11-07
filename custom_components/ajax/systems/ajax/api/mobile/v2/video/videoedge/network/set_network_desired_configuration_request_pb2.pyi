from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.network import network_interface_pb2 as _network_interface_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetNetworkDesiredConfigurationRequest(_message.Message):
    __slots__ = ("video_edge_id", "network_interface_id", "desired_configuration", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    network_interface_id: str
    desired_configuration: _network_interface_pb2.NetworkConfiguration
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., network_interface_id: _Optional[str] = ..., desired_configuration: _Optional[_Union[_network_interface_pb2.NetworkConfiguration, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class SetNetworkDesiredConfigurationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("requestId", "network_configuration_timeout")
        REQUESTID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_CONFIGURATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        requestId: str
        network_configuration_timeout: _duration_pb2.Duration
        def __init__(self, requestId: _Optional[str] = ..., network_configuration_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "network_interface_not_found", "network_interface_configuration_in_progress", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        network_interface_not_found: _response_pb2.DefaultError
        network_interface_configuration_in_progress: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., network_interface_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., network_interface_configuration_in_progress: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetNetworkDesiredConfigurationResponse.Success
    failure: SetNetworkDesiredConfigurationResponse.Failure
    def __init__(self, success: _Optional[_Union[SetNetworkDesiredConfigurationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SetNetworkDesiredConfigurationResponse.Failure, _Mapping]] = ...) -> None: ...
