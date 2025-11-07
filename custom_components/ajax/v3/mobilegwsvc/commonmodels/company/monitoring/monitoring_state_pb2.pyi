from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONITORING_STATE_UNSPECIFIED: _ClassVar[MonitoringState]
    MONITORING_STATE_PENDING_APPROVAL: _ClassVar[MonitoringState]
    MONITORING_STATE_APPROVED: _ClassVar[MonitoringState]
    MONITORING_STATE_PENDING_REMOVAL: _ClassVar[MonitoringState]
MONITORING_STATE_UNSPECIFIED: MonitoringState
MONITORING_STATE_PENDING_APPROVAL: MonitoringState
MONITORING_STATE_APPROVED: MonitoringState
MONITORING_STATE_PENDING_REMOVAL: MonitoringState
