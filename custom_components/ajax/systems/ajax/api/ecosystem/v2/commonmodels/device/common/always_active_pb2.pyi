from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlwaysActive(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALWAYS_ACTIVE_UNSPECIFIED: _ClassVar[AlwaysActive]
    ALWAYS_ACTIVE_DISABLED: _ClassVar[AlwaysActive]
    ALWAYS_ACTIVE_ENABLED: _ClassVar[AlwaysActive]
ALWAYS_ACTIVE_UNSPECIFIED: AlwaysActive
ALWAYS_ACTIVE_DISABLED: AlwaysActive
ALWAYS_ACTIVE_ENABLED: AlwaysActive
