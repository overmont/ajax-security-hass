from v3.mobilegwsvc.commonmodels.hub.device import hub_device_view_source_pb2 as _hub_device_view_source_pb2
from v3.mobilegwsvc.commonmodels.space.lock import space_interaction_lock_pb2 as _space_interaction_lock_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceInteractionLockResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update", "delete")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamSpaceInteractionLockResponse.Snapshot
        update: StreamSpaceInteractionLockResponse.Update
        delete: StreamSpaceInteractionLockResponse.Delete
        def __init__(self, snapshot: _Optional[_Union[StreamSpaceInteractionLockResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamSpaceInteractionLockResponse.Update, _Mapping]] = ..., delete: _Optional[_Union[StreamSpaceInteractionLockResponse.Delete, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("space_interaction_locks",)
        SPACE_INTERACTION_LOCKS_FIELD_NUMBER: _ClassVar[int]
        space_interaction_locks: _containers.RepeatedCompositeFieldContainer[_space_interaction_lock_pb2.SpaceInteractionLock]
        def __init__(self, space_interaction_locks: _Optional[_Iterable[_Union[_space_interaction_lock_pb2.SpaceInteractionLock, _Mapping]]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("space_interaction_lock",)
        SPACE_INTERACTION_LOCK_FIELD_NUMBER: _ClassVar[int]
        space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
        def __init__(self, space_interaction_lock: _Optional[_Union[_space_interaction_lock_pb2.SpaceInteractionLock, _Mapping]] = ...) -> None: ...
    class Delete(_message.Message):
        __slots__ = ("space_interaction_lock",)
        SPACE_INTERACTION_LOCK_FIELD_NUMBER: _ClassVar[int]
        space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
        def __init__(self, space_interaction_lock: _Optional[_Union[_space_interaction_lock_pb2.SpaceInteractionLock, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceInteractionLockResponse.Success
    failure: StreamSpaceInteractionLockResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamSpaceInteractionLockResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamSpaceInteractionLockResponse.Failure, _Mapping]] = ...) -> None: ...
