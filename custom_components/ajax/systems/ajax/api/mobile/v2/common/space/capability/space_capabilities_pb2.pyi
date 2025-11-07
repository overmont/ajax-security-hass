from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceSecurityCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_SECURITY_CAPABILITY_UNSPECIFIED: _ClassVar[SpaceSecurityCapability]
    SPACE_SECURITY_CAPABILITY_FOLLOWING_GROUPS: _ClassVar[SpaceSecurityCapability]

class VideoChannelSettingCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_CHANNEL_SETTING_CAPABILITY_UNSPECIFIED: _ClassVar[VideoChannelSettingCapability]
    VIDEO_CHANNEL_SETTING_CAPABILITY_NEW_DESIGN_DISABLED: _ClassVar[VideoChannelSettingCapability]

class SpaceMemberCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_MEMBER_CAPABILITY_UNSPECIFIED: _ClassVar[SpaceMemberCapability]
    SPACE_MEMBER_CAPABILITY_PRIVACY_OFFICER_PRESENT: _ClassVar[SpaceMemberCapability]
SPACE_SECURITY_CAPABILITY_UNSPECIFIED: SpaceSecurityCapability
SPACE_SECURITY_CAPABILITY_FOLLOWING_GROUPS: SpaceSecurityCapability
VIDEO_CHANNEL_SETTING_CAPABILITY_UNSPECIFIED: VideoChannelSettingCapability
VIDEO_CHANNEL_SETTING_CAPABILITY_NEW_DESIGN_DISABLED: VideoChannelSettingCapability
SPACE_MEMBER_CAPABILITY_UNSPECIFIED: SpaceMemberCapability
SPACE_MEMBER_CAPABILITY_PRIVACY_OFFICER_PRESENT: SpaceMemberCapability

class SpaceCapabilities(_message.Message):
    __slots__ = ("space_security_capabilities", "video_channel_setting_capabilities", "space_member_capabilities")
    SPACE_SECURITY_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CHANNEL_SETTING_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    space_security_capabilities: _containers.RepeatedScalarFieldContainer[SpaceSecurityCapability]
    video_channel_setting_capabilities: _containers.RepeatedScalarFieldContainer[VideoChannelSettingCapability]
    space_member_capabilities: _containers.RepeatedScalarFieldContainer[SpaceMemberCapability]
    def __init__(self, space_security_capabilities: _Optional[_Iterable[_Union[SpaceSecurityCapability, str]]] = ..., video_channel_setting_capabilities: _Optional[_Iterable[_Union[VideoChannelSettingCapability, str]]] = ..., space_member_capabilities: _Optional[_Iterable[_Union[SpaceMemberCapability, str]]] = ...) -> None: ...
