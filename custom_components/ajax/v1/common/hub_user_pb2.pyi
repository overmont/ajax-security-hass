from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from v1.common import image_urls_pb2 as _image_urls_pb2
from v1.common import permission_pb2 as _permission_pb2
from v1.common import restore_permission_pb2 as _restore_permission_pb2
from v1.common import group_permissions_pb2 as _group_permissions_pb2
from v1.common import notification_settings_pb2 as _notification_settings_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubUser(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "email", "phone", "image_urls", "role", "permissions", "restore_permissions", "group_permissions", "notification_settings", "user_index")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER: _ClassVar[HubUser.Role]
        PRO: _ClassVar[HubUser.Role]
        COMPANY: _ClassVar[HubUser.Role]
    USER: HubUser.Role
    PRO: HubUser.Role
    COMPANY: HubUser.Role
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    last_name: str
    email: _email_address_pb2.EmailAddress
    phone: _phone_number_pb2.PhoneNumber
    image_urls: _image_urls_pb2.ImageUrls
    role: HubUser.Role
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    restore_permissions: _containers.RepeatedScalarFieldContainer[_restore_permission_pb2.RestorePermission]
    group_permissions: _containers.RepeatedCompositeFieldContainer[_group_permissions_pb2.GroupPermissions]
    notification_settings: _notification_settings_pb2.NotificationSettings
    user_index: _wrappers_pb2.Int32Value
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[_Union[_email_address_pb2.EmailAddress, _Mapping]] = ..., phone: _Optional[_Union[_phone_number_pb2.PhoneNumber, _Mapping]] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., role: _Optional[_Union[HubUser.Role, str]] = ..., permissions: _Optional[_Iterable[_Union[_permission_pb2.Permission, str]]] = ..., restore_permissions: _Optional[_Iterable[_Union[_restore_permission_pb2.RestorePermission, str]]] = ..., group_permissions: _Optional[_Iterable[_Union[_group_permissions_pb2.GroupPermissions, _Mapping]]] = ..., notification_settings: _Optional[_Union[_notification_settings_pb2.NotificationSettings, _Mapping]] = ..., user_index: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
