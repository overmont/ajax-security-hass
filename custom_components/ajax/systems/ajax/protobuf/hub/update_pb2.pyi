from google.protobuf import field_mask_pb2 as _field_mask_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2
from systems.ajax.protobuf.hub import room_pb2 as _room_pb2
from systems.ajax.protobuf.hub import group_pb2 as _group_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.hub import company_binding_pb2 as _company_binding_pb2
from systems.ajax.protobuf.hub import config_migration_state_pb2 as _config_migration_state_pb2
from systems.ajax.protobuf.hub import hub_access_response_pb2 as _hub_access_response_pb2
from systems.ajax.protobuf.hub import access_card_reader_state_pb2 as _access_card_reader_state_pb2
from systems.ajax.protobuf.hub import access_card_rc_pb2 as _access_card_rc_pb2
from systems.ajax.protobuf.hub import access_key_pb2 as _access_key_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Update(_message.Message):
    __slots__ = ("room", "group", "user", "camera", "scenario", "company_binding", "config_migration_state", "device", "hub_access_response", "access_card_reader_state", "access_card_rc", "access_key_update", "mask", "type", "settings_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE: _ClassVar[Update.Type]
        ADD: _ClassVar[Update.Type]
        DELETE: _ClassVar[Update.Type]
        SETTINGS_ID: _ClassVar[Update.Type]
        LOGS_DROPPED: _ClassVar[Update.Type]
        PROFI_HUB_ACCESS_RESPONSE_RESULT: _ClassVar[Update.Type]
        ACCESS_CARD_STATE_CHANGED: _ClassVar[Update.Type]
        ACCESS_CARD_RC: _ClassVar[Update.Type]
        ACCESS_KEY_REGISTERED: _ClassVar[Update.Type]
        ACCESS_KEY_TIMEOUT: _ClassVar[Update.Type]
        DEV_REG_SEARCH_STARTED: _ClassVar[Update.Type]
        UNREG_DEVICE_FOUND: _ClassVar[Update.Type]
    UPDATE: Update.Type
    ADD: Update.Type
    DELETE: Update.Type
    SETTINGS_ID: Update.Type
    LOGS_DROPPED: Update.Type
    PROFI_HUB_ACCESS_RESPONSE_RESULT: Update.Type
    ACCESS_CARD_STATE_CHANGED: Update.Type
    ACCESS_CARD_RC: Update.Type
    ACCESS_KEY_REGISTERED: Update.Type
    ACCESS_KEY_TIMEOUT: Update.Type
    DEV_REG_SEARCH_STARTED: Update.Type
    UNREG_DEVICE_FOUND: Update.Type
    ROOM_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    HUB_ACCESS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_READER_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_RC_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_ID_FIELD_NUMBER: _ClassVar[int]
    room: _room_pb2.Room
    group: _group_pb2.Group
    user: _user_pb2.User
    camera: _camera_pb2.Camera
    scenario: _scenario_pb2.Scenario
    company_binding: _company_binding_pb2.CompanyBinding
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    device: _device_pb2.Device
    hub_access_response: _hub_access_response_pb2.HubAccessResponse
    access_card_reader_state: _access_card_reader_state_pb2.AccessCardReaderState
    access_card_rc: _access_card_rc_pb2.AccessCardRc
    access_key_update: _access_key_pb2.AccessKeyUpdate
    mask: _field_mask_pb2.FieldMask
    type: Update.Type
    settings_id: str
    def __init__(self, room: _Optional[_Union[_room_pb2.Room, _Mapping]] = ..., group: _Optional[_Union[_group_pb2.Group, _Mapping]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., camera: _Optional[_Union[_camera_pb2.Camera, _Mapping]] = ..., scenario: _Optional[_Union[_scenario_pb2.Scenario, _Mapping]] = ..., company_binding: _Optional[_Union[_company_binding_pb2.CompanyBinding, _Mapping]] = ..., config_migration_state: _Optional[_Union[_config_migration_state_pb2.ConfigMigrationState, _Mapping]] = ..., device: _Optional[_Union[_device_pb2.Device, _Mapping]] = ..., hub_access_response: _Optional[_Union[_hub_access_response_pb2.HubAccessResponse, _Mapping]] = ..., access_card_reader_state: _Optional[_Union[_access_card_reader_state_pb2.AccessCardReaderState, _Mapping]] = ..., access_card_rc: _Optional[_Union[_access_card_rc_pb2.AccessCardRc, _Mapping]] = ..., access_key_update: _Optional[_Union[_access_key_pb2.AccessKeyUpdate, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., type: _Optional[_Union[Update.Type, str]] = ..., settings_id: _Optional[str] = ...) -> None: ...
