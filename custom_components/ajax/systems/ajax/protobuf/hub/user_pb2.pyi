from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "first_name", "email", "phone", "language", "index", "agreement_version", "attached_company_id", "permissions", "hub_binding_role", "restore_permissions", "password_hash", "password_hash_duress", "image_id", "keypad_prefix", "image_urls", "notification_settings", "group_permissions")
    class HubBindingRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ROLE_INFO: _ClassVar[User.HubBindingRole]
        USER: _ClassVar[User.HubBindingRole]
        MASTER: _ClassVar[User.HubBindingRole]
        PRO: _ClassVar[User.HubBindingRole]
        COMPANY: _ClassVar[User.HubBindingRole]
    NO_ROLE_INFO: User.HubBindingRole
    USER: User.HubBindingRole
    MASTER: User.HubBindingRole
    PRO: User.HubBindingRole
    COMPANY: User.HubBindingRole
    class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED_0: _ClassVar[User.Permission]
        USER_DELETE: _ClassVar[User.Permission]
        USER_ADD: _ClassVar[User.Permission]
        USER_ROLE_UPDATE: _ClassVar[User.Permission]
        USER_PERMISSIONS_UPDATE: _ClassVar[User.Permission]
        USER_NOTIFICATION_SETTINGS_UPDATE: _ClassVar[User.Permission]
        RESERVED_6: _ClassVar[User.Permission]
        RESERVED_7: _ClassVar[User.Permission]
        ARM: _ClassVar[User.Permission]
        NIGHT_MODE: _ClassVar[User.Permission]
        DISARM: _ClassVar[User.Permission]
        PANIC: _ClassVar[User.Permission]
        ROOM_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        DEVICE_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        HUB_NET_SETTINGS_UPDATE: _ClassVar[User.Permission]
        HUB_OTHER_SETTINGS_UPDATE: _ClassVar[User.Permission]
        STATE_COMMANDS: _ClassVar[User.Permission]
        FIRMWARE_COMMANDS: _ClassVar[User.Permission]
        CAMERA_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        CAMERA_GET: _ClassVar[User.Permission]
        GROUP_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        EVENTS_GET: _ClassVar[User.Permission]
        GET: _ClassVar[User.Permission]
        SCENARIO: _ClassVar[User.Permission]
        CHIMES_UPDATE: _ClassVar[User.Permission]
        PRIVACY_ACCESS_SETTINGS: _ClassVar[User.Permission]
        RESERVED_26: _ClassVar[User.Permission]
        RESERVED_27: _ClassVar[User.Permission]
        RESERVED_28: _ClassVar[User.Permission]
        RESERVED_29: _ClassVar[User.Permission]
        RESERVED_30: _ClassVar[User.Permission]
        RESERVED_31: _ClassVar[User.Permission]
    RESERVED_0: User.Permission
    USER_DELETE: User.Permission
    USER_ADD: User.Permission
    USER_ROLE_UPDATE: User.Permission
    USER_PERMISSIONS_UPDATE: User.Permission
    USER_NOTIFICATION_SETTINGS_UPDATE: User.Permission
    RESERVED_6: User.Permission
    RESERVED_7: User.Permission
    ARM: User.Permission
    NIGHT_MODE: User.Permission
    DISARM: User.Permission
    PANIC: User.Permission
    ROOM_ADD_UPDATE_DELETE: User.Permission
    DEVICE_ADD_UPDATE_DELETE: User.Permission
    HUB_NET_SETTINGS_UPDATE: User.Permission
    HUB_OTHER_SETTINGS_UPDATE: User.Permission
    STATE_COMMANDS: User.Permission
    FIRMWARE_COMMANDS: User.Permission
    CAMERA_ADD_UPDATE_DELETE: User.Permission
    CAMERA_GET: User.Permission
    GROUP_ADD_UPDATE_DELETE: User.Permission
    EVENTS_GET: User.Permission
    GET: User.Permission
    SCENARIO: User.Permission
    CHIMES_UPDATE: User.Permission
    PRIVACY_ACCESS_SETTINGS: User.Permission
    RESERVED_26: User.Permission
    RESERVED_27: User.Permission
    RESERVED_28: User.Permission
    RESERVED_29: User.Permission
    RESERVED_30: User.Permission
    RESERVED_31: User.Permission
    class RestorePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_RESTORE_PERMISSION_INFO: _ClassVar[User.RestorePermission]
        RESTORE_CONFIRMED_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_CONFIRMED_HU_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_UNCONFIRMED_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_UNCONFIRMED_HU_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_TAMPER_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_EXTERNAL_POWER_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_ATS_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_OTHER_FAULT_ACTIVATION: _ClassVar[User.RestorePermission]
    NO_RESTORE_PERMISSION_INFO: User.RestorePermission
    RESTORE_CONFIRMED_ALARMS: User.RestorePermission
    RESTORE_CONFIRMED_HU_ALARMS: User.RestorePermission
    RESTORE_UNCONFIRMED_ALARMS: User.RestorePermission
    RESTORE_UNCONFIRMED_HU_ALARMS: User.RestorePermission
    RESTORE_TAMPER_ACTIVATION: User.RestorePermission
    RESTORE_EXTERNAL_POWER_ACTIVATION: User.RestorePermission
    RESTORE_ATS_ACTIVATION: User.RestorePermission
    RESTORE_OTHER_FAULT_ACTIVATION: User.RestorePermission
    class NotificationSettings(_message.Message):
        __slots__ = ("alarms", "events", "malfunctions", "armings")
        class NotificationChannel(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_NOTIFICATION_CHANNEL_INFO: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
                PUSH: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
                SMS: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
                CALL: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
            NO_NOTIFICATION_CHANNEL_INFO: User.NotificationSettings.NotificationChannel.Type
            PUSH: User.NotificationSettings.NotificationChannel.Type
            SMS: User.NotificationSettings.NotificationChannel.Type
            CALL: User.NotificationSettings.NotificationChannel.Type
            def __init__(self) -> None: ...
        class MessageNotificationChannel(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_MESSAGE_NOTIFICATION_CHANNEL_INFO: _ClassVar[User.NotificationSettings.MessageNotificationChannel.Type]
                PUSH: _ClassVar[User.NotificationSettings.MessageNotificationChannel.Type]
                SMS: _ClassVar[User.NotificationSettings.MessageNotificationChannel.Type]
            NO_MESSAGE_NOTIFICATION_CHANNEL_INFO: User.NotificationSettings.MessageNotificationChannel.Type
            PUSH: User.NotificationSettings.MessageNotificationChannel.Type
            SMS: User.NotificationSettings.MessageNotificationChannel.Type
            def __init__(self) -> None: ...
        ALARMS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        ARMINGS_FIELD_NUMBER: _ClassVar[int]
        alarms: _containers.RepeatedScalarFieldContainer[User.NotificationSettings.NotificationChannel.Type]
        events: _containers.RepeatedScalarFieldContainer[User.NotificationSettings.MessageNotificationChannel.Type]
        malfunctions: _containers.RepeatedScalarFieldContainer[User.NotificationSettings.MessageNotificationChannel.Type]
        armings: _containers.RepeatedScalarFieldContainer[User.NotificationSettings.MessageNotificationChannel.Type]
        def __init__(self, alarms: _Optional[_Iterable[_Union[User.NotificationSettings.NotificationChannel.Type, str]]] = ..., events: _Optional[_Iterable[_Union[User.NotificationSettings.MessageNotificationChannel.Type, str]]] = ..., malfunctions: _Optional[_Iterable[_Union[User.NotificationSettings.MessageNotificationChannel.Type, str]]] = ..., armings: _Optional[_Iterable[_Union[User.NotificationSettings.MessageNotificationChannel.Type, str]]] = ...) -> None: ...
    class GroupPermissions(_message.Message):
        __slots__ = ("group_id", "permissions")
        class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_PERMISSION_INFO: _ClassVar[User.GroupPermissions.Permission]
            ARM: _ClassVar[User.GroupPermissions.Permission]
            DISARM: _ClassVar[User.GroupPermissions.Permission]
        NO_PERMISSION_INFO: User.GroupPermissions.Permission
        ARM: User.GroupPermissions.Permission
        DISARM: User.GroupPermissions.Permission
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        permissions: _containers.RepeatedScalarFieldContainer[User.GroupPermissions.Permission]
        def __init__(self, group_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[User.GroupPermissions.Permission, str]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_BINDING_ROLE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_DURESS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    email: str
    phone: str
    language: str
    index: int
    agreement_version: int
    attached_company_id: str
    permissions: _containers.RepeatedScalarFieldContainer[User.Permission]
    hub_binding_role: User.HubBindingRole
    restore_permissions: _containers.RepeatedScalarFieldContainer[User.RestorePermission]
    password_hash: str
    password_hash_duress: str
    image_id: str
    keypad_prefix: str
    image_urls: _image_urls_pb2.ImageUrls
    notification_settings: User.NotificationSettings
    group_permissions: _containers.RepeatedCompositeFieldContainer[User.GroupPermissions]
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., language: _Optional[str] = ..., index: _Optional[int] = ..., agreement_version: _Optional[int] = ..., attached_company_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[User.Permission, str]]] = ..., hub_binding_role: _Optional[_Union[User.HubBindingRole, str]] = ..., restore_permissions: _Optional[_Iterable[_Union[User.RestorePermission, str]]] = ..., password_hash: _Optional[str] = ..., password_hash_duress: _Optional[str] = ..., image_id: _Optional[str] = ..., keypad_prefix: _Optional[str] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., notification_settings: _Optional[_Union[User.NotificationSettings, _Mapping]] = ..., group_permissions: _Optional[_Iterable[_Union[User.GroupPermissions, _Mapping]]] = ...) -> None: ...
