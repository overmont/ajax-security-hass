from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCard(_message.Message):
    __slots__ = ("id", "name", "card_record", "card_UID", "card_key_seed", "app_id", "group_permissions", "associated_user_id", "device_index", "perimeter_arm", "full_arm", "card_enabled", "attribute")
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WHITE: _ClassVar[AccessCard.Color]
        BLACK: _ClassVar[AccessCard.Color]
    WHITE: AccessCard.Color
    BLACK: AccessCard.Color
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CARD: _ClassVar[AccessCard.Type]
        TAG: _ClassVar[AccessCard.Type]
    CARD: AccessCard.Type
    TAG: AccessCard.Type
    class GroupPermissions(_message.Message):
        __slots__ = ("group_id", "permissions")
        class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_PERMISSION_INFO: _ClassVar[AccessCard.GroupPermissions.Permission]
            ARM: _ClassVar[AccessCard.GroupPermissions.Permission]
            DISARM: _ClassVar[AccessCard.GroupPermissions.Permission]
        NO_PERMISSION_INFO: AccessCard.GroupPermissions.Permission
        ARM: AccessCard.GroupPermissions.Permission
        DISARM: AccessCard.GroupPermissions.Permission
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        permissions: _containers.RepeatedScalarFieldContainer[AccessCard.GroupPermissions.Permission]
        def __init__(self, group_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[AccessCard.GroupPermissions.Permission, str]]] = ...) -> None: ...
    class Attribute(_message.Message):
        __slots__ = ("color", "type")
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        color: AccessCard.Color
        type: AccessCard.Type
        def __init__(self, color: _Optional[_Union[AccessCard.Color, str]] = ..., type: _Optional[_Union[AccessCard.Type, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CARD_RECORD_FIELD_NUMBER: _ClassVar[int]
    CARD_UID_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_SEED_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ARM_FIELD_NUMBER: _ClassVar[int]
    FULL_ARM_FIELD_NUMBER: _ClassVar[int]
    CARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    card_record: int
    card_UID: int
    card_key_seed: int
    app_id: int
    group_permissions: _containers.RepeatedCompositeFieldContainer[AccessCard.GroupPermissions]
    associated_user_id: str
    device_index: int
    perimeter_arm: bool
    full_arm: bool
    card_enabled: bool
    attribute: AccessCard.Attribute
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., card_record: _Optional[int] = ..., card_UID: _Optional[int] = ..., card_key_seed: _Optional[int] = ..., app_id: _Optional[int] = ..., group_permissions: _Optional[_Iterable[_Union[AccessCard.GroupPermissions, _Mapping]]] = ..., associated_user_id: _Optional[str] = ..., device_index: _Optional[int] = ..., perimeter_arm: bool = ..., full_arm: bool = ..., card_enabled: bool = ..., attribute: _Optional[_Union[AccessCard.Attribute, _Mapping]] = ...) -> None: ...
