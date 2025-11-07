from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONITORING_STATUS_UNSPECIFIED: _ClassVar[MonitoringStatus]
    MONITORING_STATUS_ON_MONITORING: _ClassVar[MonitoringStatus]
    MONITORING_STATUS_ON_MULTIPLE_MONITORING: _ClassVar[MonitoringStatus]
    MONITORING_STATUS_REQUEST_FROM_INSTALLER: _ClassVar[MonitoringStatus]
    MONITORING_STATUS_NO_MONITORING: _ClassVar[MonitoringStatus]
    MONITORING_STATUS_IN_SLEEP_MODE: _ClassVar[MonitoringStatus]
MONITORING_STATUS_UNSPECIFIED: MonitoringStatus
MONITORING_STATUS_ON_MONITORING: MonitoringStatus
MONITORING_STATUS_ON_MULTIPLE_MONITORING: MonitoringStatus
MONITORING_STATUS_REQUEST_FROM_INSTALLER: MonitoringStatus
MONITORING_STATUS_NO_MONITORING: MonitoringStatus
MONITORING_STATUS_IN_SLEEP_MODE: MonitoringStatus
