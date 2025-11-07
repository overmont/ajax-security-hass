from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyBillingInfo(_message.Message):
    __slots__ = ("hub_billing_info", "billing_status")
    class Blocked(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKED_UNSPECIFIED: _ClassVar[CompanyBillingInfo.Blocked]
        BLOCKED_FALSE: _ClassVar[CompanyBillingInfo.Blocked]
        BLOCKED_TRUE: _ClassVar[CompanyBillingInfo.Blocked]
    BLOCKED_UNSPECIFIED: CompanyBillingInfo.Blocked
    BLOCKED_FALSE: CompanyBillingInfo.Blocked
    BLOCKED_TRUE: CompanyBillingInfo.Blocked
    class BillingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BILLING_STATUS_UNSPECIFIED: _ClassVar[CompanyBillingInfo.BillingStatus]
        BILLING_STATUS_ENABLED: _ClassVar[CompanyBillingInfo.BillingStatus]
        BILLING_STATUS_DISABLED: _ClassVar[CompanyBillingInfo.BillingStatus]
    BILLING_STATUS_UNSPECIFIED: CompanyBillingInfo.BillingStatus
    BILLING_STATUS_ENABLED: CompanyBillingInfo.BillingStatus
    BILLING_STATUS_DISABLED: CompanyBillingInfo.BillingStatus
    class HubBillingInfo(_message.Message):
        __slots__ = ("hub_hex_id", "company_hex_id", "balance", "subscription_fee", "blocked", "currency", "payment_date")
        HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_FEE_FIELD_NUMBER: _ClassVar[int]
        BLOCKED_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_DATE_FIELD_NUMBER: _ClassVar[int]
        hub_hex_id: str
        company_hex_id: str
        balance: float
        subscription_fee: float
        blocked: CompanyBillingInfo.Blocked
        currency: str
        payment_date: str
        def __init__(self, hub_hex_id: _Optional[str] = ..., company_hex_id: _Optional[str] = ..., balance: _Optional[float] = ..., subscription_fee: _Optional[float] = ..., blocked: _Optional[_Union[CompanyBillingInfo.Blocked, str]] = ..., currency: _Optional[str] = ..., payment_date: _Optional[str] = ...) -> None: ...
    HUB_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    BILLING_STATUS_FIELD_NUMBER: _ClassVar[int]
    hub_billing_info: CompanyBillingInfo.HubBillingInfo
    billing_status: CompanyBillingInfo.BillingStatus
    def __init__(self, hub_billing_info: _Optional[_Union[CompanyBillingInfo.HubBillingInfo, _Mapping]] = ..., billing_status: _Optional[_Union[CompanyBillingInfo.BillingStatus, str]] = ...) -> None: ...
