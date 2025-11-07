from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceIcon(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_ICON_UNSPECIFIED: _ClassVar[ServiceIcon]
    SERVICE_ICON_SIM: _ClassVar[ServiceIcon]
    SERVICE_ICON_CLOUD_STORAGE: _ClassVar[ServiceIcon]
    SERVICE_ICON_PHOTO_MODE: _ClassVar[ServiceIcon]
    SERVICE_ICON_TELEPHONY: _ClassVar[ServiceIcon]
    SERVICE_ICON_DP: _ClassVar[ServiceIcon]
SERVICE_ICON_UNSPECIFIED: ServiceIcon
SERVICE_ICON_SIM: ServiceIcon
SERVICE_ICON_CLOUD_STORAGE: ServiceIcon
SERVICE_ICON_PHOTO_MODE: ServiceIcon
SERVICE_ICON_TELEPHONY: ServiceIcon
SERVICE_ICON_DP: ServiceIcon
