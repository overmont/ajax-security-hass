from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2
from systems.ajax.protobuf.hub import room_pb2 as _room_pb2
from systems.ajax.protobuf.hub import group_pb2 as _group_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.hub import company_binding_pb2 as _company_binding_pb2
from systems.ajax.protobuf.hub import config_migration_state_pb2 as _config_migration_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hub(_message.Message):
    __slots__ = ("devices", "rooms", "groups", "users", "cameras", "scenarios", "company_bindings", "config_migration_state", "settings_id")
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_ID_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
    rooms: _containers.RepeatedCompositeFieldContainer[_room_pb2.Room]
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    cameras: _containers.RepeatedCompositeFieldContainer[_camera_pb2.Camera]
    scenarios: _containers.RepeatedCompositeFieldContainer[_scenario_pb2.Scenario]
    company_bindings: _containers.RepeatedCompositeFieldContainer[_company_binding_pb2.CompanyBinding]
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    settings_id: str
    def __init__(self, devices: _Optional[_Iterable[_Union[_device_pb2.Device, _Mapping]]] = ..., rooms: _Optional[_Iterable[_Union[_room_pb2.Room, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., cameras: _Optional[_Iterable[_Union[_camera_pb2.Camera, _Mapping]]] = ..., scenarios: _Optional[_Iterable[_Union[_scenario_pb2.Scenario, _Mapping]]] = ..., company_bindings: _Optional[_Iterable[_Union[_company_binding_pb2.CompanyBinding, _Mapping]]] = ..., config_migration_state: _Optional[_Union[_config_migration_state_pb2.ConfigMigrationState, _Mapping]] = ..., settings_id: _Optional[str] = ...) -> None: ...
