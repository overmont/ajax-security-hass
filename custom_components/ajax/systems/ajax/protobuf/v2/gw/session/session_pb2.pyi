from systems.ajax.protobuf.gw import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATED: _ClassVar[EventType]
    DELETED: _ClassVar[EventType]

class Response(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESSFUL: _ClassVar[Response]
CREATED: EventType
DELETED: EventType
SUCCESSFUL: Response

class SessionInfo(_message.Message):
    __slots__ = ("session", "event_type", "user_id")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session: Session
    event_type: EventType
    user_id: str
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., event_type: _Optional[_Union[EventType, str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("session_id", "session_creation_timestamp", "last_connection_ip", "client_device_model", "client_os", "session_expiry_time", "client_version_major", "client_device_id", "legacy_session", "application_label", "session_refresh_timestamp", "is_active")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_IP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_FIELD_NUMBER: _ClassVar[int]
    SESSION_EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_SESSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SESSION_REFRESH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    session_creation_timestamp: int
    last_connection_ip: str
    client_device_model: str
    client_os: str
    session_expiry_time: int
    client_version_major: str
    client_device_id: str
    legacy_session: bool
    application_label: str
    session_refresh_timestamp: int
    is_active: bool
    def __init__(self, session_id: _Optional[int] = ..., session_creation_timestamp: _Optional[int] = ..., last_connection_ip: _Optional[str] = ..., client_device_model: _Optional[str] = ..., client_os: _Optional[str] = ..., session_expiry_time: _Optional[int] = ..., client_version_major: _Optional[str] = ..., client_device_id: _Optional[str] = ..., legacy_session: bool = ..., application_label: _Optional[str] = ..., session_refresh_timestamp: _Optional[int] = ..., is_active: bool = ...) -> None: ...

class GetActiveSessionsResponse(_message.Message):
    __slots__ = ("sessions", "error")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sessions: ActiveSessions
    error: _error_pb2.GwError
    def __init__(self, sessions: _Optional[_Union[ActiveSessions, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.GwError, _Mapping]] = ...) -> None: ...

class ActiveSessions(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class DropUserSessionResponse(_message.Message):
    __slots__ = ("response", "error")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    response: Response
    error: _error_pb2.GwError
    def __init__(self, response: _Optional[_Union[Response, str]] = ..., error: _Optional[_Union[_error_pb2.GwError, _Mapping]] = ...) -> None: ...

class CreateNewSessionResponse(_message.Message):
    __slots__ = ("session", "error")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    session: Session
    error: _error_pb2.GwError
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.GwError, _Mapping]] = ...) -> None: ...
