from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaveRexPairingDevicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "hub_offline", "hub_busy", "hub_wrong_state", "rex_offline", "wrong_parameters")
        class RexOfflineError(_message.Message):
            __slots__ = ("rex_name",)
            REX_NAME_FIELD_NUMBER: _ClassVar[int]
            rex_name: str
            def __init__(self, rex_name: _Optional[str] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        REX_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        WRONG_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_wrong_state: _response_pb2.HubWrongStateError
        rex_offline: SaveRexPairingDevicesResponse.Failure.RexOfflineError
        wrong_parameters: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., rex_offline: _Optional[_Union[SaveRexPairingDevicesResponse.Failure.RexOfflineError, _Mapping]] = ..., wrong_parameters: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SaveRexPairingDevicesResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[SaveRexPairingDevicesResponse.Failure, _Mapping]] = ...) -> None: ...
