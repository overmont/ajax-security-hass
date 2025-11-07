from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityStandard(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_STANDARD_UNSPECIFIED: _ClassVar[SecurityStandard]
    SECURITY_STANDARD_EU: _ClassVar[SecurityStandard]
    SECURITY_STANDARD_PD: _ClassVar[SecurityStandard]
    SECURITY_STANDARD_SIACP: _ClassVar[SecurityStandard]
    SECURITY_STANDARD_VDS: _ClassVar[SecurityStandard]
SECURITY_STANDARD_UNSPECIFIED: SecurityStandard
SECURITY_STANDARD_EU: SecurityStandard
SECURITY_STANDARD_PD: SecurityStandard
SECURITY_STANDARD_SIACP: SecurityStandard
SECURITY_STANDARD_VDS: SecurityStandard
