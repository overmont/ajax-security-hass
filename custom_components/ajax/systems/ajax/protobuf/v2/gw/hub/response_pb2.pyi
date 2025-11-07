from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.v2.hub import hub_for_migration_pb2 as _hub_for_migration_pb2
from systems.ajax.protobuf.gw import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionResponse(_message.Message):
    __slots__ = ("timestamp_to_drop", "permissions")
    TIMESTAMP_TO_DROP_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    timestamp_to_drop: int
    permissions: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
    def __init__(self, timestamp_to_drop: _Optional[int] = ..., permissions: _Optional[_Iterable[_Union[_user_pb2.User.Permission, str]]] = ...) -> None: ...

class GetHubForMigrationResponse(_message.Message):
    __slots__ = ("error", "hub_for_migration")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_FOR_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.GwError
    hub_for_migration: _hub_for_migration_pb2.HubForMigration
    def __init__(self, error: _Optional[_Union[_error_pb2.GwError, _Mapping]] = ..., hub_for_migration: _Optional[_Union[_hub_for_migration_pb2.HubForMigration, _Mapping]] = ...) -> None: ...
