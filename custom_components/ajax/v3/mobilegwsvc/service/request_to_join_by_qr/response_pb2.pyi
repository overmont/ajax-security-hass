from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateJoinByQrResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "member_already_exists", "hub_offline", "limit_reached")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        member_already_exists: _response_pb2.Error
        hub_offline: _response_pb2.Error
        limit_reached: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., member_already_exists: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., limit_reached: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: InitiateJoinByQrResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[InitiateJoinByQrResponse.Failure, _Mapping]] = ...) -> None: ...
