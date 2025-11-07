from systems.ajax.api.mobile.v2.common.accounting import feature_pb2 as _feature_pb2
from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureOnTarget(_message.Message):
    __slots__ = ("feature", "reseller", "dealer")
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    RESELLER_FIELD_NUMBER: _ClassVar[int]
    DEALER_FIELD_NUMBER: _ClassVar[int]
    feature: _feature_pb2.Feature
    reseller: _accounting_company_pb2.AccountingCompany
    dealer: _accounting_company_pb2.AccountingCompany
    def __init__(self, feature: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., reseller: _Optional[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]] = ..., dealer: _Optional[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]] = ...) -> None: ...
