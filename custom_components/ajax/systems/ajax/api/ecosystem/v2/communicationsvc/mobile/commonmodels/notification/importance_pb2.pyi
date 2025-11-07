from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationImportance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORTANCE_UNSPECIFIED: _ClassVar[NotificationImportance]
    IMPORTANCE_DEFAULT: _ClassVar[NotificationImportance]
    IMPORTANCE_POSITIVE: _ClassVar[NotificationImportance]
    IMPORTANCE_WARNING: _ClassVar[NotificationImportance]
    IMPORTANCE_ATTENTION: _ClassVar[NotificationImportance]
IMPORTANCE_UNSPECIFIED: NotificationImportance
IMPORTANCE_DEFAULT: NotificationImportance
IMPORTANCE_POSITIVE: NotificationImportance
IMPORTANCE_WARNING: NotificationImportance
IMPORTANCE_ATTENTION: NotificationImportance
