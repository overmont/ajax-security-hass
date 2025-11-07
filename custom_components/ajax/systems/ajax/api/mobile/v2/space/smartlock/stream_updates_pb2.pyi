from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_in_space_pb2 as _smart_lock_in_space_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_space_settings_pb2 as _smart_lock_space_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSmartLockUpdatesRequest(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class StreamSmartLockUpdatesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("initial_state", "installed", "uninstalled", "partially_changed")
        class InitialState(_message.Message):
            __slots__ = ("smart_locks",)
            SMART_LOCKS_FIELD_NUMBER: _ClassVar[int]
            smart_locks: _containers.RepeatedCompositeFieldContainer[_smart_lock_in_space_pb2.SmartLockInSpace]
            def __init__(self, smart_locks: _Optional[_Iterable[_Union[_smart_lock_in_space_pb2.SmartLockInSpace, _Mapping]]] = ...) -> None: ...
        class Installed(_message.Message):
            __slots__ = ("smart_lock",)
            SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
            smart_lock: _smart_lock_in_space_pb2.SmartLockInSpace
            def __init__(self, smart_lock: _Optional[_Union[_smart_lock_in_space_pb2.SmartLockInSpace, _Mapping]] = ...) -> None: ...
        class Uninstalled(_message.Message):
            __slots__ = ("smart_lock_id",)
            SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
            smart_lock_id: str
            def __init__(self, smart_lock_id: _Optional[str] = ...) -> None: ...
        class PartiallyChanged(_message.Message):
            __slots__ = ("smart_lock_id", "details", "space_settings")
            SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            smart_lock_id: str
            details: _smart_lock_pb2.SmartLock
            space_settings: _smart_lock_space_settings_pb2.SmartLockSpaceSettings
            def __init__(self, smart_lock_id: _Optional[str] = ..., details: _Optional[_Union[_smart_lock_pb2.SmartLock, _Mapping]] = ..., space_settings: _Optional[_Union[_smart_lock_space_settings_pb2.SmartLockSpaceSettings, _Mapping]] = ...) -> None: ...
        INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
        INSTALLED_FIELD_NUMBER: _ClassVar[int]
        UNINSTALLED_FIELD_NUMBER: _ClassVar[int]
        PARTIALLY_CHANGED_FIELD_NUMBER: _ClassVar[int]
        initial_state: StreamSmartLockUpdatesResponse.Success.InitialState
        installed: StreamSmartLockUpdatesResponse.Success.Installed
        uninstalled: StreamSmartLockUpdatesResponse.Success.Uninstalled
        partially_changed: StreamSmartLockUpdatesResponse.Success.PartiallyChanged
        def __init__(self, initial_state: _Optional[_Union[StreamSmartLockUpdatesResponse.Success.InitialState, _Mapping]] = ..., installed: _Optional[_Union[StreamSmartLockUpdatesResponse.Success.Installed, _Mapping]] = ..., uninstalled: _Optional[_Union[StreamSmartLockUpdatesResponse.Success.Uninstalled, _Mapping]] = ..., partially_changed: _Optional[_Union[StreamSmartLockUpdatesResponse.Success.PartiallyChanged, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("permission_denied", "bad_request", "space_not_found")
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        permission_denied: _response_pb2.DefaultError
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        def __init__(self, permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSmartLockUpdatesResponse.Success
    failure: StreamSmartLockUpdatesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamSmartLockUpdatesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamSmartLockUpdatesResponse.Failure, _Mapping]] = ...) -> None: ...
