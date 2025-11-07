from systems.ajax.api.mobile.v2.common import connection_status_pb2 as _connection_status_pb2
from systems.ajax.api.mobile.v2.common.hub import battery_save_mode_pb2 as _battery_save_mode_pb2
from systems.ajax.api.mobile.v2.common.space.security import displayed_space_security_state_pb2 as _displayed_space_security_state_pb2
from systems.ajax.api.mobile.v2.common.space import space_profile_pb2 as _space_profile_pb2
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamUserSpacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StreamUserSpacesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("initial_state", "lite_space_event")
        INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
        LITE_SPACE_EVENT_FIELD_NUMBER: _ClassVar[int]
        initial_state: StreamUserSpacesResponse.InitialState
        lite_space_event: StreamUserSpacesResponse.LiteSpaceEvent
        def __init__(self, initial_state: _Optional[_Union[StreamUserSpacesResponse.InitialState, _Mapping]] = ..., lite_space_event: _Optional[_Union[StreamUserSpacesResponse.LiteSpaceEvent, _Mapping]] = ...) -> None: ...
    class InitialState(_message.Message):
        __slots__ = ("spaces",)
        SPACES_FIELD_NUMBER: _ClassVar[int]
        spaces: _containers.RepeatedCompositeFieldContainer[_space_lite_pb2.LiteSpace]
        def __init__(self, spaces: _Optional[_Iterable[_Union[_space_lite_pb2.LiteSpace, _Mapping]]] = ...) -> None: ...
    class LiteSpaceEvent(_message.Message):
        __slots__ = ("space_id", "lite_space_created", "lite_space_updated", "lite_space_removed")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        LITE_SPACE_CREATED_FIELD_NUMBER: _ClassVar[int]
        LITE_SPACE_UPDATED_FIELD_NUMBER: _ClassVar[int]
        LITE_SPACE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        lite_space_created: StreamUserSpacesResponse.LiteSpaceCreated
        lite_space_updated: StreamUserSpacesResponse.LiteSpaceUpdated
        lite_space_removed: StreamUserSpacesResponse.LiteSpaceRemoved
        def __init__(self, space_id: _Optional[str] = ..., lite_space_created: _Optional[_Union[StreamUserSpacesResponse.LiteSpaceCreated, _Mapping]] = ..., lite_space_updated: _Optional[_Union[StreamUserSpacesResponse.LiteSpaceUpdated, _Mapping]] = ..., lite_space_removed: _Optional[_Union[StreamUserSpacesResponse.LiteSpaceRemoved, _Mapping]] = ...) -> None: ...
    class LiteSpaceCreated(_message.Message):
        __slots__ = ("lite_space",)
        LITE_SPACE_FIELD_NUMBER: _ClassVar[int]
        lite_space: _space_lite_pb2.LiteSpace
        def __init__(self, lite_space: _Optional[_Union[_space_lite_pb2.LiteSpace, _Mapping]] = ...) -> None: ...
    class LiteSpaceUpdated(_message.Message):
        __slots__ = ("id", "sorting_key", "profile", "security_state", "hub_id", "new_notifications_count", "malfunctions_count", "hub_connection_status", "bsm_status")
        ID_FIELD_NUMBER: _ClassVar[int]
        SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        SECURITY_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        NEW_NOTIFICATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        HUB_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        BSM_STATUS_FIELD_NUMBER: _ClassVar[int]
        id: str
        sorting_key: str
        profile: _space_profile_pb2.SpaceProfile
        security_state: _displayed_space_security_state_pb2.DisplayedSpaceSecurityState
        hub_id: str
        new_notifications_count: int
        malfunctions_count: int
        hub_connection_status: _connection_status_pb2.ConnectionStatus
        bsm_status: _battery_save_mode_pb2.BatterySaveModeStatus
        def __init__(self, id: _Optional[str] = ..., sorting_key: _Optional[str] = ..., profile: _Optional[_Union[_space_profile_pb2.SpaceProfile, _Mapping]] = ..., security_state: _Optional[_Union[_displayed_space_security_state_pb2.DisplayedSpaceSecurityState, str]] = ..., hub_id: _Optional[str] = ..., new_notifications_count: _Optional[int] = ..., malfunctions_count: _Optional[int] = ..., hub_connection_status: _Optional[_Union[_connection_status_pb2.ConnectionStatus, str]] = ..., bsm_status: _Optional[_Union[_battery_save_mode_pb2.BatterySaveModeStatus, str]] = ...) -> None: ...
    class LiteSpaceRemoved(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamUserSpacesResponse.Success
    failure: StreamUserSpacesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamUserSpacesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamUserSpacesResponse.Failure, _Mapping]] = ...) -> None: ...
