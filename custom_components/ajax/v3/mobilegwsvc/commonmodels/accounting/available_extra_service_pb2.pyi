from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from v3.mobilegwsvc.commonmodels.accounting import enriched_target_info_pb2 as _enriched_target_info_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.accounting import reseller_pb2 as _reseller_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableExtraService(_message.Message):
    __slots__ = ("service", "resellers", "feature_target_infos", "reseller_infos")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESELLERS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    RESELLER_INFOS_FIELD_NUMBER: _ClassVar[int]
    service: _service_pb2.Service
    resellers: _containers.RepeatedCompositeFieldContainer[_accounting_company_pb2.AccountingCompany]
    feature_target_infos: _containers.RepeatedCompositeFieldContainer[_enriched_target_info_pb2.EnrichedTargetInfo]
    reseller_infos: _containers.RepeatedCompositeFieldContainer[_reseller_pb2.Reseller]
    def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., resellers: _Optional[_Iterable[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]]] = ..., feature_target_infos: _Optional[_Iterable[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]]] = ..., reseller_infos: _Optional[_Iterable[_Union[_reseller_pb2.Reseller, _Mapping]]] = ...) -> None: ...
