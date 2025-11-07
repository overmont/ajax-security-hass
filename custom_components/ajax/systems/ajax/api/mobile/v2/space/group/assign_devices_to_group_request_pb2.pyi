from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.device import hub_device_pb2 as _hub_device_pb2
from systems.ajax.api.mobile.v2.common.space.device import video_edge_channel_pb2 as _video_edge_channel_pb2
from systems.ajax.api.mobile.v2.common.space.device import smart_lock_device_pb2 as _smart_lock_device_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignDevicesToGroupRequest(_message.Message):
    __slots__ = ("space_locator", "group_id", "devices")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    group_id: str
    devices: _containers.RepeatedCompositeFieldContainer[DeviceForGroup]
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., group_id: _Optional[str] = ..., devices: _Optional[_Iterable[_Union[DeviceForGroup, _Mapping]]] = ...) -> None: ...

class DeviceForGroup(_message.Message):
    __slots__ = ("hub_device", "video_edge_channel", "smart_lock")
    HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    hub_device: _hub_device_pb2.HubDevice
    video_edge_channel: _video_edge_channel_pb2.VideoEdgeChannel
    smart_lock: _smart_lock_device_pb2.SmartLockDevice
    def __init__(self, hub_device: _Optional[_Union[_hub_device_pb2.HubDevice, _Mapping]] = ..., video_edge_channel: _Optional[_Union[_video_edge_channel_pb2.VideoEdgeChannel, _Mapping]] = ..., smart_lock: _Optional[_Union[_smart_lock_device_pb2.SmartLockDevice, _Mapping]] = ...) -> None: ...

class AssignDevicesToGroupResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_armed", "permission_denied", "group_not_found", "devices_not_found", "hub_offline", "hub_busy", "hub_error", "hub_wrong_state", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICES_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        devices_not_found: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., group_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., devices_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: AssignDevicesToGroupResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[AssignDevicesToGroupResponse.Failure, _Mapping]] = ...) -> None: ...
