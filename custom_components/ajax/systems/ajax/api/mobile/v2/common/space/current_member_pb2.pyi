from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.mobile.v2.common.space.member import group_permissions_pb2 as _group_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_member_role_pb2 as _space_member_role_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_permissions_pb2 as _space_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import standalone_device_permissions_pb2 as _standalone_device_permissions_pb2
from systems.ajax.api.mobile.v2.common.video.privacy import request_video_access_available_actions_pb2 as _request_video_access_available_actions_pb2
from systems.ajax.api.mobile.v2.common.video import video_wall_pb2 as _video_wall_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentMember(_message.Message):
    __slots__ = ("user_current_member", "pro_current_member", "employee_current_member")
    class UserCurrentMember(_message.Message):
        __slots__ = ("id", "space_permissions", "devices_permissions", "role", "group_permissions", "video_wall", "notification_info", "hex_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        space_permissions: _space_permissions_pb2.SpacePermissions
        devices_permissions: _containers.RepeatedCompositeFieldContainer[_standalone_device_permissions_pb2.StandaloneDevicePermissions]
        role: _space_member_role_pb2.SpaceMemberRole
        group_permissions: _containers.RepeatedCompositeFieldContainer[_group_permissions_pb2.GroupPermissions]
        video_wall: _video_wall_pb2.VideoWall
        notification_info: CurrentMember.NotificationInfo
        hex_id: str
        def __init__(self, id: _Optional[str] = ..., space_permissions: _Optional[_Union[_space_permissions_pb2.SpacePermissions, _Mapping]] = ..., devices_permissions: _Optional[_Iterable[_Union[_standalone_device_permissions_pb2.StandaloneDevicePermissions, _Mapping]]] = ..., role: _Optional[_Union[_space_member_role_pb2.SpaceMemberRole, str]] = ..., group_permissions: _Optional[_Iterable[_Union[_group_permissions_pb2.GroupPermissions, _Mapping]]] = ..., video_wall: _Optional[_Union[_video_wall_pb2.VideoWall, _Mapping]] = ..., notification_info: _Optional[_Union[CurrentMember.NotificationInfo, _Mapping]] = ..., hex_id: _Optional[str] = ...) -> None: ...
    class ProCurrentMember(_message.Message):
        __slots__ = ("id", "space_permissions", "devices_permissions", "access_rights", "group_permissions", "video_wall", "notification_info", "hex_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
        GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        space_permissions: _space_permissions_pb2.SpacePermissions
        devices_permissions: _containers.RepeatedCompositeFieldContainer[_standalone_device_permissions_pb2.StandaloneDevicePermissions]
        access_rights: CurrentMember.AccessRights
        group_permissions: _containers.RepeatedCompositeFieldContainer[_group_permissions_pb2.GroupPermissions]
        video_wall: _video_wall_pb2.VideoWall
        notification_info: CurrentMember.NotificationInfo
        hex_id: str
        def __init__(self, id: _Optional[str] = ..., space_permissions: _Optional[_Union[_space_permissions_pb2.SpacePermissions, _Mapping]] = ..., devices_permissions: _Optional[_Iterable[_Union[_standalone_device_permissions_pb2.StandaloneDevicePermissions, _Mapping]]] = ..., access_rights: _Optional[_Union[CurrentMember.AccessRights, _Mapping]] = ..., group_permissions: _Optional[_Iterable[_Union[_group_permissions_pb2.GroupPermissions, _Mapping]]] = ..., video_wall: _Optional[_Union[_video_wall_pb2.VideoWall, _Mapping]] = ..., notification_info: _Optional[_Union[CurrentMember.NotificationInfo, _Mapping]] = ..., hex_id: _Optional[str] = ...) -> None: ...
    class EmployeeCurrentMember(_message.Message):
        __slots__ = ("id", "space_permissions", "devices_permissions", "access_rights", "group_permissions", "video_wall", "available_actions", "notification_info", "hex_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
        GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        space_permissions: _space_permissions_pb2.SpacePermissions
        devices_permissions: _containers.RepeatedCompositeFieldContainer[_standalone_device_permissions_pb2.StandaloneDevicePermissions]
        access_rights: CurrentMember.AccessRights
        group_permissions: _containers.RepeatedCompositeFieldContainer[_group_permissions_pb2.GroupPermissions]
        video_wall: _video_wall_pb2.VideoWall
        available_actions: CurrentMember.EmployeeCurrentMemberAvailableActions
        notification_info: CurrentMember.NotificationInfo
        hex_id: str
        def __init__(self, id: _Optional[str] = ..., space_permissions: _Optional[_Union[_space_permissions_pb2.SpacePermissions, _Mapping]] = ..., devices_permissions: _Optional[_Iterable[_Union[_standalone_device_permissions_pb2.StandaloneDevicePermissions, _Mapping]]] = ..., access_rights: _Optional[_Union[CurrentMember.AccessRights, _Mapping]] = ..., group_permissions: _Optional[_Iterable[_Union[_group_permissions_pb2.GroupPermissions, _Mapping]]] = ..., video_wall: _Optional[_Union[_video_wall_pb2.VideoWall, _Mapping]] = ..., available_actions: _Optional[_Union[CurrentMember.EmployeeCurrentMemberAvailableActions, _Mapping]] = ..., notification_info: _Optional[_Union[CurrentMember.NotificationInfo, _Mapping]] = ..., hex_id: _Optional[str] = ...) -> None: ...
    class AccessRights(_message.Message):
        __slots__ = ("expiration_timestamp", "access_type", "full_permissions")
        class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACCESS_TYPE_UNSPECIFIED: _ClassVar[CurrentMember.AccessRights.AccessType]
            ACCESS_TYPE_EXPIRED: _ClassVar[CurrentMember.AccessRights.AccessType]
            ACCESS_TYPE_PERMANENT: _ClassVar[CurrentMember.AccessRights.AccessType]
            ACCESS_TYPE_TEMPORARY: _ClassVar[CurrentMember.AccessRights.AccessType]
        ACCESS_TYPE_UNSPECIFIED: CurrentMember.AccessRights.AccessType
        ACCESS_TYPE_EXPIRED: CurrentMember.AccessRights.AccessType
        ACCESS_TYPE_PERMANENT: CurrentMember.AccessRights.AccessType
        ACCESS_TYPE_TEMPORARY: CurrentMember.AccessRights.AccessType
        EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
        FULL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        expiration_timestamp: _timestamp_pb2.Timestamp
        access_type: CurrentMember.AccessRights.AccessType
        full_permissions: bool
        def __init__(self, expiration_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_type: _Optional[_Union[CurrentMember.AccessRights.AccessType, str]] = ..., full_permissions: bool = ...) -> None: ...
    class EmployeeCurrentMemberAvailableActions(_message.Message):
        __slots__ = ("request_video_access", "invite_to_space_access", "manage_members_access", "view_event_photos_access")
        REQUEST_VIDEO_ACCESS_FIELD_NUMBER: _ClassVar[int]
        INVITE_TO_SPACE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        MANAGE_MEMBERS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        VIEW_EVENT_PHOTOS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        request_video_access: _request_video_access_available_actions_pb2.RequestVideoAccessAvailableActions
        invite_to_space_access: CurrentMember.InviteToSpaceAvailableActions
        manage_members_access: CurrentMember.ManageMembersAvailableActions
        view_event_photos_access: CurrentMember.ViewEventPhotosActions
        def __init__(self, request_video_access: _Optional[_Union[_request_video_access_available_actions_pb2.RequestVideoAccessAvailableActions, _Mapping]] = ..., invite_to_space_access: _Optional[_Union[CurrentMember.InviteToSpaceAvailableActions, _Mapping]] = ..., manage_members_access: _Optional[_Union[CurrentMember.ManageMembersAvailableActions, _Mapping]] = ..., view_event_photos_access: _Optional[_Union[CurrentMember.ViewEventPhotosActions, _Mapping]] = ...) -> None: ...
    class InviteToSpaceAvailableActions(_message.Message):
        __slots__ = ("can_invite_installer", "can_invite_security_company")
        CAN_INVITE_INSTALLER_FIELD_NUMBER: _ClassVar[int]
        CAN_INVITE_SECURITY_COMPANY_FIELD_NUMBER: _ClassVar[int]
        can_invite_installer: bool
        can_invite_security_company: bool
        def __init__(self, can_invite_installer: bool = ..., can_invite_security_company: bool = ...) -> None: ...
    class ManageMembersAvailableActions(_message.Message):
        __slots__ = ("can_change_role", "can_change_member_permissions")
        CAN_CHANGE_ROLE_FIELD_NUMBER: _ClassVar[int]
        CAN_CHANGE_MEMBER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        can_change_role: bool
        can_change_member_permissions: CurrentMember.CanChangeMemberPermissions
        def __init__(self, can_change_role: bool = ..., can_change_member_permissions: _Optional[_Union[CurrentMember.CanChangeMemberPermissions, _Mapping]] = ...) -> None: ...
    class CanChangeMemberPermissions(_message.Message):
        __slots__ = ("system_settings",)
        SYSTEM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        system_settings: bool
        def __init__(self, system_settings: bool = ...) -> None: ...
    class ViewEventPhotosActions(_message.Message):
        __slots__ = ("can_view_photo",)
        class CanViewPhoto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CAN_VIEW_PHOTO_UNSPECIFIED: _ClassVar[CurrentMember.ViewEventPhotosActions.CanViewPhoto]
            CAN_VIEW_PHOTO_ON_DEMAND: _ClassVar[CurrentMember.ViewEventPhotosActions.CanViewPhoto]
            CAN_VIEW_PHOTO_BY_ALARM_SCENARIO: _ClassVar[CurrentMember.ViewEventPhotosActions.CanViewPhoto]
        CAN_VIEW_PHOTO_UNSPECIFIED: CurrentMember.ViewEventPhotosActions.CanViewPhoto
        CAN_VIEW_PHOTO_ON_DEMAND: CurrentMember.ViewEventPhotosActions.CanViewPhoto
        CAN_VIEW_PHOTO_BY_ALARM_SCENARIO: CurrentMember.ViewEventPhotosActions.CanViewPhoto
        CAN_VIEW_PHOTO_FIELD_NUMBER: _ClassVar[int]
        can_view_photo: _containers.RepeatedScalarFieldContainer[CurrentMember.ViewEventPhotosActions.CanViewPhoto]
        def __init__(self, can_view_photo: _Optional[_Iterable[_Union[CurrentMember.ViewEventPhotosActions.CanViewPhoto, str]]] = ...) -> None: ...
    class NotificationInfo(_message.Message):
        __slots__ = ("are_notifications_accessible",)
        ARE_NOTIFICATIONS_ACCESSIBLE_FIELD_NUMBER: _ClassVar[int]
        are_notifications_accessible: bool
        def __init__(self, are_notifications_accessible: bool = ...) -> None: ...
    USER_CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    PRO_CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    user_current_member: CurrentMember.UserCurrentMember
    pro_current_member: CurrentMember.ProCurrentMember
    employee_current_member: CurrentMember.EmployeeCurrentMember
    def __init__(self, user_current_member: _Optional[_Union[CurrentMember.UserCurrentMember, _Mapping]] = ..., pro_current_member: _Optional[_Union[CurrentMember.ProCurrentMember, _Mapping]] = ..., employee_current_member: _Optional[_Union[CurrentMember.EmployeeCurrentMember, _Mapping]] = ...) -> None: ...
