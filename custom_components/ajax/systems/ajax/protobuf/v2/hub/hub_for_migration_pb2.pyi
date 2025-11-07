from systems.ajax.protobuf.hub import config_migration_state_pb2 as _config_migration_state_pb2
from systems.ajax.protobuf.hub import lightweight_hub_pb2 as _lightweight_hub_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubForMigration(_message.Message):
    __slots__ = ("hub", "config_migration_state")
    HUB_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    hub: _lightweight_hub_pb2.LightweightHub
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    def __init__(self, hub: _Optional[_Union[_lightweight_hub_pb2.LightweightHub, _Mapping]] = ..., config_migration_state: _Optional[_Union[_config_migration_state_pb2.ConfigMigrationState, _Mapping]] = ...) -> None: ...
