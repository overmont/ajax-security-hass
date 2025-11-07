from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartSystemFirmwareUpdateRequest(_message.Message):
    __slots__ = ("hub_id",)
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    def __init__(self, hub_id: _Optional[str] = ...) -> None: ...

class StartSystemFirmwareUpdateResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("message", "no_update_available", "hub_offline")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NO_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        message: str
        no_update_available: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., no_update_available: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: StartSystemFirmwareUpdateResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[StartSystemFirmwareUpdateResponse.Failure, _Mapping]] = ...) -> None: ...
