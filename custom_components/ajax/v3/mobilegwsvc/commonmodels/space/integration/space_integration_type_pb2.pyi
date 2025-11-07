from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceIntegrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_INTEGRATION_TYPE_UNSPECIFIED: _ClassVar[SpaceIntegrationType]
    SPACE_INTEGRATION_TYPE_YALE_SMART_LOCK: _ClassVar[SpaceIntegrationType]
    SPACE_INTEGRATION_TYPE_YALE_SMART_LOCK_NA: _ClassVar[SpaceIntegrationType]
SPACE_INTEGRATION_TYPE_UNSPECIFIED: SpaceIntegrationType
SPACE_INTEGRATION_TYPE_YALE_SMART_LOCK: SpaceIntegrationType
SPACE_INTEGRATION_TYPE_YALE_SMART_LOCK_NA: SpaceIntegrationType
