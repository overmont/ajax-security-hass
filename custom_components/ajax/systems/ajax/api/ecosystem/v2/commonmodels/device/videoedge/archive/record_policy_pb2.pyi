from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RecordPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECORD_POLICY_UNSPECIFIED: _ClassVar[RecordPolicy]
    RECORD_POLICY_ALWAYS: _ClassVar[RecordPolicy]
    RECORD_POLICY_WHEN_REQUESTED: _ClassVar[RecordPolicy]
RECORD_POLICY_UNSPECIFIED: RecordPolicy
RECORD_POLICY_ALWAYS: RecordPolicy
RECORD_POLICY_WHEN_REQUESTED: RecordPolicy
