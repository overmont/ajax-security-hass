from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceConstraint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_CONSTRAINT_UNSPECIFIED: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_DISABLE_INTERACTION: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_DISABLE_NOTIFICATIONS: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_SHOW_DEVICE_AS_SUSPENDED: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_SHOW_DEVICE_AS_LOCKED: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION_ON_ACTIVATION: _ClassVar[DeviceConstraint]
    DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION_ON_SUSPENSION: _ClassVar[DeviceConstraint]
DEVICE_CONSTRAINT_UNSPECIFIED: DeviceConstraint
DEVICE_CONSTRAINT_DISABLE_INTERACTION: DeviceConstraint
DEVICE_CONSTRAINT_DISABLE_NOTIFICATIONS: DeviceConstraint
DEVICE_CONSTRAINT_SHOW_DEVICE_AS_SUSPENDED: DeviceConstraint
DEVICE_CONSTRAINT_SHOW_DEVICE_AS_LOCKED: DeviceConstraint
DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION: DeviceConstraint
DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION_ON_ACTIVATION: DeviceConstraint
DEVICE_CONSTRAINT_DISABLE_HUB_CONNECTIVITY_SETTINGS_INTERACTION_ON_SUSPENSION: DeviceConstraint

class DeviceConstraints(_message.Message):
    __slots__ = ("constraints",)
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    constraints: _containers.RepeatedScalarFieldContainer[DeviceConstraint]
    def __init__(self, constraints: _Optional[_Iterable[_Union[DeviceConstraint, str]]] = ...) -> None: ...
