from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HubColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUB_COLOR_UNSPECIFIED: _ClassVar[HubColor]
    HUB_COLOR_WHITE: _ClassVar[HubColor]
    HUB_COLOR_BLACK: _ClassVar[HubColor]
HUB_COLOR_UNSPECIFIED: HubColor
HUB_COLOR_WHITE: HubColor
HUB_COLOR_BLACK: HubColor
