from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Case(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CASE_UNSPECIFIED: _ClassVar[Case]
    CASE_EN54_TEST: _ClassVar[Case]
CASE_UNSPECIFIED: Case
CASE_EN54_TEST: Case
