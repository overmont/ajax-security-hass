from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_fibra_part_pb2 as _common_fibra_part_pb2
from v3.mobilegwsvc.commonmodels.hub.device import hub_device_view_source_pb2 as _hub_device_view_source_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamScanFibraDevicesUpdatesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("state_update", "device_triggered", "device_added")
        class State(_message.Message):
            __slots__ = ("not_started", "in_progress", "finished", "blocked")
            class NotStarted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class InProgress(_message.Message):
                __slots__ = ("found_devices_count",)
                FOUND_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
                found_devices_count: int
                def __init__(self, found_devices_count: _Optional[int] = ...) -> None: ...
            class Finished(_message.Message):
                __slots__ = ("scanned_devices", "no_fibra_devices_found")
                class ScannedDevices(_message.Message):
                    __slots__ = ("scanned_devices",)
                    SCANNED_DEVICES_FIELD_NUMBER: _ClassVar[int]
                    scanned_devices: _containers.RepeatedCompositeFieldContainer[StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevice]
                    def __init__(self, scanned_devices: _Optional[_Iterable[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevice, _Mapping]]] = ...) -> None: ...
                class ScannedDevice(_message.Message):
                    __slots__ = ("marketing_id", "line", "hub_device_view_source")
                    MARKETING_ID_FIELD_NUMBER: _ClassVar[int]
                    LINE_FIELD_NUMBER: _ClassVar[int]
                    HUB_DEVICE_VIEW_SOURCE_FIELD_NUMBER: _ClassVar[int]
                    marketing_id: str
                    line: _common_fibra_part_pb2.FibraLine
                    hub_device_view_source: _hub_device_view_source_pb2.HubDeviceViewSource
                    def __init__(self, marketing_id: _Optional[str] = ..., line: _Optional[_Union[_common_fibra_part_pb2.FibraLine, _Mapping]] = ..., hub_device_view_source: _Optional[_Union[_hub_device_view_source_pb2.HubDeviceViewSource, _Mapping]] = ...) -> None: ...
                class NoFibraDevicesFound(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                SCANNED_DEVICES_FIELD_NUMBER: _ClassVar[int]
                NO_FIBRA_DEVICES_FOUND_FIELD_NUMBER: _ClassVar[int]
                scanned_devices: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevices
                no_fibra_devices_found: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.NoFibraDevicesFound
                def __init__(self, scanned_devices: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevices, _Mapping]] = ..., no_fibra_devices_found: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.NoFibraDevicesFound, _Mapping]] = ...) -> None: ...
            class Blocked(_message.Message):
                __slots__ = ("malfunction", "malfunction_on_rings")
                class Malfunction(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class MalfunctionOnRings(_message.Message):
                    __slots__ = ("lines",)
                    LINES_FIELD_NUMBER: _ClassVar[int]
                    lines: _containers.RepeatedCompositeFieldContainer[_common_fibra_part_pb2.FibraLine]
                    def __init__(self, lines: _Optional[_Iterable[_Union[_common_fibra_part_pb2.FibraLine, _Mapping]]] = ...) -> None: ...
                MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
                MALFUNCTION_ON_RINGS_FIELD_NUMBER: _ClassVar[int]
                malfunction: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.Malfunction
                malfunction_on_rings: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.MalfunctionOnRings
                def __init__(self, malfunction: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.Malfunction, _Mapping]] = ..., malfunction_on_rings: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.MalfunctionOnRings, _Mapping]] = ...) -> None: ...
            NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
            IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            FINISHED_FIELD_NUMBER: _ClassVar[int]
            BLOCKED_FIELD_NUMBER: _ClassVar[int]
            not_started: StreamScanFibraDevicesUpdatesResponse.Success.State.NotStarted
            in_progress: StreamScanFibraDevicesUpdatesResponse.Success.State.InProgress
            finished: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished
            blocked: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked
            def __init__(self, not_started: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.NotStarted, _Mapping]] = ..., in_progress: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.InProgress, _Mapping]] = ..., finished: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Finished, _Mapping]] = ..., blocked: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked, _Mapping]] = ...) -> None: ...
        class DeviceTriggered(_message.Message):
            __slots__ = ("device_id", "timestamp")
            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            device_id: str
            timestamp: _timestamp_pb2.Timestamp
            def __init__(self, device_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class DeviceAdded(_message.Message):
            __slots__ = ("device_id",)
            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            device_id: str
            def __init__(self, device_id: _Optional[str] = ...) -> None: ...
        STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        state_update: StreamScanFibraDevicesUpdatesResponse.Success.State
        device_triggered: StreamScanFibraDevicesUpdatesResponse.Success.DeviceTriggered
        device_added: StreamScanFibraDevicesUpdatesResponse.Success.DeviceAdded
        def __init__(self, state_update: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.State, _Mapping]] = ..., device_triggered: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.DeviceTriggered, _Mapping]] = ..., device_added: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success.DeviceAdded, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "unknown_command", "command_not_performed", "hub_wrong_state", "permission_denied", "hub_offline", "hub_busy", "hub_error")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        unknown_command: _response_pb2.Error
        command_not_performed: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unknown_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., command_not_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamScanFibraDevicesUpdatesResponse.Success
    failure: StreamScanFibraDevicesUpdatesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamScanFibraDevicesUpdatesResponse.Failure, _Mapping]] = ...) -> None: ...
