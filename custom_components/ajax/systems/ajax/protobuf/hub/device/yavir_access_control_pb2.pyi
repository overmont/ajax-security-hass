from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YavirAccessControl(_message.Message):
    __slots__ = ("id", "name", "group_id", "time_to_block_on_multiple_password_failures_minutes", "cms_device_index", "blocking_enabled", "associated_group_id", "access_profiles", "device_type", "enabled", "room_id", "blocked", "online", "tampered", "service_problems_count", "bypass_mode", "is_bypass_mode", "password_hash", "password_hash_duress")
    class AccessProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACCESS_PROFILE_INFO: _ClassVar[YavirAccessControl.AccessProfile]
        KEYBOARD_PASSWORD: _ClassVar[YavirAccessControl.AccessProfile]
        USER_PASSWORD: _ClassVar[YavirAccessControl.AccessProfile]
    NO_ACCESS_PROFILE_INFO: YavirAccessControl.AccessProfile
    KEYBOARD_PASSWORD: YavirAccessControl.AccessProfile
    USER_PASSWORD: YavirAccessControl.AccessProfile
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_TYPE_INFO: _ClassVar[YavirAccessControl.DeviceType]
        DUNAY_KEYBOARD: _ClassVar[YavirAccessControl.DeviceType]
        YAVIR_READER: _ClassVar[YavirAccessControl.DeviceType]
    NO_DEVICE_TYPE_INFO: YavirAccessControl.DeviceType
    DUNAY_KEYBOARD: YavirAccessControl.DeviceType
    YAVIR_READER: YavirAccessControl.DeviceType
    class BypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BYPASS_MODE_INFO: _ClassVar[YavirAccessControl.BypassMode]
        ENGINEER_BYPASS_OFF: _ClassVar[YavirAccessControl.BypassMode]
        ENGINEER_BYPASS_ON: _ClassVar[YavirAccessControl.BypassMode]
        TAMPER_BYPASS_ON: _ClassVar[YavirAccessControl.BypassMode]
    NO_BYPASS_MODE_INFO: YavirAccessControl.BypassMode
    ENGINEER_BYPASS_OFF: YavirAccessControl.BypassMode
    ENGINEER_BYPASS_ON: YavirAccessControl.BypassMode
    TAMPER_BYPASS_ON: YavirAccessControl.BypassMode
    class IsBypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_IN_BYPASS_MODE: _ClassVar[YavirAccessControl.IsBypassMode]
        ENABLED_ENGINEER_BYPASS: _ClassVar[YavirAccessControl.IsBypassMode]
        ENABLED_TAMPER_BYPASS: _ClassVar[YavirAccessControl.IsBypassMode]
    NO_IN_BYPASS_MODE: YavirAccessControl.IsBypassMode
    ENABLED_ENGINEER_BYPASS: YavirAccessControl.IsBypassMode
    ENABLED_TAMPER_BYPASS: YavirAccessControl.IsBypassMode
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_BLOCK_ON_MULTIPLE_PASSWORD_FAILURES_MINUTES_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROFILES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    TAMPERED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROBLEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_DURESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    group_id: str
    time_to_block_on_multiple_password_failures_minutes: int
    cms_device_index: int
    blocking_enabled: bool
    associated_group_id: str
    access_profiles: _containers.RepeatedScalarFieldContainer[YavirAccessControl.AccessProfile]
    device_type: YavirAccessControl.DeviceType
    enabled: bool
    room_id: str
    blocked: _wrappers_pb2.BoolValue
    online: _wrappers_pb2.BoolValue
    tampered: _wrappers_pb2.BoolValue
    service_problems_count: _wrappers_pb2.Int32Value
    bypass_mode: YavirAccessControl.BypassMode
    is_bypass_mode: _containers.RepeatedScalarFieldContainer[YavirAccessControl.IsBypassMode]
    password_hash: str
    password_hash_duress: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., group_id: _Optional[str] = ..., time_to_block_on_multiple_password_failures_minutes: _Optional[int] = ..., cms_device_index: _Optional[int] = ..., blocking_enabled: bool = ..., associated_group_id: _Optional[str] = ..., access_profiles: _Optional[_Iterable[_Union[YavirAccessControl.AccessProfile, str]]] = ..., device_type: _Optional[_Union[YavirAccessControl.DeviceType, str]] = ..., enabled: bool = ..., room_id: _Optional[str] = ..., blocked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., online: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., tampered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., service_problems_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., bypass_mode: _Optional[_Union[YavirAccessControl.BypassMode, str]] = ..., is_bypass_mode: _Optional[_Iterable[_Union[YavirAccessControl.IsBypassMode, str]]] = ..., password_hash: _Optional[str] = ..., password_hash_duress: _Optional[str] = ...) -> None: ...
