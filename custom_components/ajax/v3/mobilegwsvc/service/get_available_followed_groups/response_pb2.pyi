from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_pb2 as _group_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableFollowedGroupsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("groups",)
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
        def __init__(self, groups: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_locked: _response_pb2_1.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2_1.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAvailableFollowedGroupsResponse.Success
    failure: GetAvailableFollowedGroupsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetAvailableFollowedGroupsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetAvailableFollowedGroupsResponse.Failure, _Mapping]] = ...) -> None: ...
