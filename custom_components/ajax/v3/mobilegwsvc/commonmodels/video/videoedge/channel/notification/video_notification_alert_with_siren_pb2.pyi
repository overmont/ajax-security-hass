from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlertWithSiren(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_WITH_SIREN_UNSPECIFIED: _ClassVar[AlertWithSiren]
    ALERT_WITH_SIREN_DISABLED: _ClassVar[AlertWithSiren]
    ALERT_WITH_SIREN_ENABLED: _ClassVar[AlertWithSiren]
ALERT_WITH_SIREN_UNSPECIFIED: AlertWithSiren
ALERT_WITH_SIREN_DISABLED: AlertWithSiren
ALERT_WITH_SIREN_ENABLED: AlertWithSiren
