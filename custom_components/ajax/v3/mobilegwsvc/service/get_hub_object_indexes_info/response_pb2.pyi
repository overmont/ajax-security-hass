from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import hub_object_indexes_info_pb2 as _hub_object_indexes_info_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHubObjectIndexesInfoResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("hub_object_indexes_info",)
        HUB_OBJECT_INDEXES_INFO_FIELD_NUMBER: _ClassVar[int]
        hub_object_indexes_info: _hub_object_indexes_info_pb2.HubObjectIndexesInfo
        def __init__(self, hub_object_indexes_info: _Optional[_Union[_hub_object_indexes_info_pb2.HubObjectIndexesInfo, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetHubObjectIndexesInfoResponse.Success
    failure: GetHubObjectIndexesInfoResponse.Failure
    def __init__(self, success: _Optional[_Union[GetHubObjectIndexesInfoResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetHubObjectIndexesInfoResponse.Failure, _Mapping]] = ...) -> None: ...
