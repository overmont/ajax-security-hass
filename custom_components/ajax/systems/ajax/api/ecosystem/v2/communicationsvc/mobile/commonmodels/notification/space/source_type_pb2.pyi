from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceNotificationSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_SOURCE_TYPE_UNSPECIFIED: _ClassVar[SpaceNotificationSourceType]
    SPACE: _ClassVar[SpaceNotificationSourceType]
    SPACE_MEMBER: _ClassVar[SpaceNotificationSourceType]
    GROUP: _ClassVar[SpaceNotificationSourceType]
    ROOM: _ClassVar[SpaceNotificationSourceType]
    STANDALONE_DEVICE: _ClassVar[SpaceNotificationSourceType]
    COMPANY: _ClassVar[SpaceNotificationSourceType]
    SPACE_SCENARIO: _ClassVar[SpaceNotificationSourceType]
SPACE_SOURCE_TYPE_UNSPECIFIED: SpaceNotificationSourceType
SPACE: SpaceNotificationSourceType
SPACE_MEMBER: SpaceNotificationSourceType
GROUP: SpaceNotificationSourceType
ROOM: SpaceNotificationSourceType
STANDALONE_DEVICE: SpaceNotificationSourceType
COMPANY: SpaceNotificationSourceType
SPACE_SCENARIO: SpaceNotificationSourceType
