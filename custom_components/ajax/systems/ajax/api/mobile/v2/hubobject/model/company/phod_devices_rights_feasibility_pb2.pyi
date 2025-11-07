from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PhodDevicesRightsFeasibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PHOD_DEVICES_RIGHTS_FEASIBILITY_INFO: _ClassVar[PhodDevicesRightsFeasibility]
    SLOW_AND_PHOD_DEVICES: _ClassVar[PhodDevicesRightsFeasibility]
    PHOD_DEVICES: _ClassVar[PhodDevicesRightsFeasibility]
NO_PHOD_DEVICES_RIGHTS_FEASIBILITY_INFO: PhodDevicesRightsFeasibility
SLOW_AND_PHOD_DEVICES: PhodDevicesRightsFeasibility
PHOD_DEVICES: PhodDevicesRightsFeasibility
