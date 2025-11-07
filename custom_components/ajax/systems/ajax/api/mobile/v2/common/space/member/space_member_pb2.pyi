from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.api.mobile.v2.common.space.member import group_permissions_pb2 as _group_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_permissions_pb2 as _space_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import standalone_device_permissions_pb2 as _standalone_device_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_member_role_pb2 as _space_member_role_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_permissions_pb2 as _display_member_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMember(_message.Message):
    __slots__ = ("id", "space_permissions", "devices_permissions", "name", "email", "role", "group_permissions", "display_member_permissions", "user_index", "display_member_notification_preferences", "images", "sorting_key", "hex_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MEMBER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MEMBER_NOTIFICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    space_permissions: _space_permissions_pb2.SpacePermissions
    devices_permissions: _containers.RepeatedCompositeFieldContainer[_standalone_device_permissions_pb2.StandaloneDevicePermissions]
    name: str
    email: str
    role: _space_member_role_pb2.SpaceMemberRole
    group_permissions: _containers.RepeatedCompositeFieldContainer[_group_permissions_pb2.GroupPermissions]
    display_member_permissions: _display_member_permissions_pb2.DisplayMemberPermissions
    user_index: int
    display_member_notification_preferences: _display_member_notification_preferences_pb2.DisplayMemberNotificationPreferences
    images: _image_pb2.Images
    sorting_key: str
    hex_id: str
    def __init__(self, id: _Optional[str] = ..., space_permissions: _Optional[_Union[_space_permissions_pb2.SpacePermissions, _Mapping]] = ..., devices_permissions: _Optional[_Iterable[_Union[_standalone_device_permissions_pb2.StandaloneDevicePermissions, _Mapping]]] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[_space_member_role_pb2.SpaceMemberRole, str]] = ..., group_permissions: _Optional[_Iterable[_Union[_group_permissions_pb2.GroupPermissions, _Mapping]]] = ..., display_member_permissions: _Optional[_Union[_display_member_permissions_pb2.DisplayMemberPermissions, _Mapping]] = ..., user_index: _Optional[int] = ..., display_member_notification_preferences: _Optional[_Union[_display_member_notification_preferences_pb2.DisplayMemberNotificationPreferences, _Mapping]] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., sorting_key: _Optional[str] = ..., hex_id: _Optional[str] = ...) -> None: ...
