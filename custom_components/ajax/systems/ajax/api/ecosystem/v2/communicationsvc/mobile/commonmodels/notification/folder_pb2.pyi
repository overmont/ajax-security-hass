from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationFolder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOLDER_UNSPECIFIED: _ClassVar[NotificationFolder]
    FOLDER_ALARM: _ClassVar[NotificationFolder]
    FOLDER_MALFUNCTION: _ClassVar[NotificationFolder]
    FOLDER_USER_AUTOMATION: _ClassVar[NotificationFolder]
    FOLDER_HOME_AUTOMATION: _ClassVar[NotificationFolder]
    FOLDER_SYSTEM: _ClassVar[NotificationFolder]
    FOLDER_VIDEO: _ClassVar[NotificationFolder]
FOLDER_UNSPECIFIED: NotificationFolder
FOLDER_ALARM: NotificationFolder
FOLDER_MALFUNCTION: NotificationFolder
FOLDER_USER_AUTOMATION: NotificationFolder
FOLDER_HOME_AUTOMATION: NotificationFolder
FOLDER_SYSTEM: NotificationFolder
FOLDER_VIDEO: NotificationFolder
