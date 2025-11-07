from systems.ajax.api.mobile.v2.common import connection_status_pb2 as _connection_status_pb2
from systems.ajax.api.mobile.v2.common.hub import battery_save_mode_pb2 as _battery_save_mode_pb2
from systems.ajax.api.mobile.v2.common.space.security import displayed_space_security_state_pb2 as _displayed_space_security_state_pb2
from systems.ajax.api.mobile.v2.common.space import space_profile_pb2 as _space_profile_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpace(_message.Message):
    __slots__ = ("id", "profile", "security_state", "new_notifications_count", "malfunctions_count", "sorting_key", "pagination_token", "hub_connection_status", "bsm_status", "hub_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STATE_FIELD_NUMBER: _ClassVar[int]
    NEW_NOTIFICATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BSM_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    profile: _space_profile_pb2.SpaceProfile
    security_state: _displayed_space_security_state_pb2.DisplayedSpaceSecurityState
    new_notifications_count: int
    malfunctions_count: int
    sorting_key: str
    pagination_token: str
    hub_connection_status: _connection_status_pb2.ConnectionStatus
    bsm_status: _battery_save_mode_pb2.BatterySaveModeStatus
    hub_id: str
    def __init__(self, id: _Optional[str] = ..., profile: _Optional[_Union[_space_profile_pb2.SpaceProfile, _Mapping]] = ..., security_state: _Optional[_Union[_displayed_space_security_state_pb2.DisplayedSpaceSecurityState, str]] = ..., new_notifications_count: _Optional[int] = ..., malfunctions_count: _Optional[int] = ..., sorting_key: _Optional[str] = ..., pagination_token: _Optional[str] = ..., hub_connection_status: _Optional[_Union[_connection_status_pb2.ConnectionStatus, str]] = ..., bsm_status: _Optional[_Union[_battery_save_mode_pb2.BatterySaveModeStatus, str]] = ..., hub_id: _Optional[str] = ...) -> None: ...
