from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import hub_device_pb2 as _hub_device_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubDeviceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot",)
        class Snapshot(_message.Message):
            __slots__ = ("hub_device",)
            HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
            hub_device: _hub_device_pb2.HubDevice
            def __init__(self, hub_device: _Optional[_Union[_hub_device_pb2.HubDevice, _Mapping]] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamHubDeviceResponse.Success.Snapshot
        def __init__(self, snapshot: _Optional[_Union[StreamHubDeviceResponse.Success.Snapshot, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "device_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        device_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamHubDeviceResponse.Success
    failure: StreamHubDeviceResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamHubDeviceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamHubDeviceResponse.Failure, _Mapping]] = ...) -> None: ...
