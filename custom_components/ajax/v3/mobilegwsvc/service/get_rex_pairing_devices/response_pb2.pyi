from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import selected_device_pb2 as _selected_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRexPairingDevicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[_selected_device_pb2.SelectedDevice]
        def __init__(self, devices: _Optional[_Iterable[_Union[_selected_device_pb2.SelectedDevice, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetRexPairingDevicesResponse.Success
    failure: GetRexPairingDevicesResponse.Failure
    def __init__(self, success: _Optional[_Union[GetRexPairingDevicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetRexPairingDevicesResponse.Failure, _Mapping]] = ...) -> None: ...
