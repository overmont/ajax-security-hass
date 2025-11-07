from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from v3.mobilegwsvc.commonmodels.company.monitoring import monitoring_state_pb2 as _monitoring_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Reseller(_message.Message):
    __slots__ = ("accounting_company", "monitoring_state")
    ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    accounting_company: _accounting_company_pb2.AccountingCompany
    monitoring_state: _monitoring_state_pb2.MonitoringState
    def __init__(self, accounting_company: _Optional[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]] = ..., monitoring_state: _Optional[_Union[_monitoring_state_pb2.MonitoringState, str]] = ...) -> None: ...
