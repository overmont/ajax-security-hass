from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_PERMISSION_NONE: _ClassVar[ChannelPermission]
    VIEW_LIVE_STREAM: _ClassVar[ChannelPermission]
    VIEW_ARCHIVE: _ClassVar[ChannelPermission]
    PTZ: _ClassVar[ChannelPermission]
    SOUND: _ClassVar[ChannelPermission]
    EXPORT_ARCHIVE: _ClassVar[ChannelPermission]
CHANNEL_PERMISSION_NONE: ChannelPermission
VIEW_LIVE_STREAM: ChannelPermission
VIEW_ARCHIVE: ChannelPermission
PTZ: ChannelPermission
SOUND: ChannelPermission
EXPORT_ARCHIVE: ChannelPermission
