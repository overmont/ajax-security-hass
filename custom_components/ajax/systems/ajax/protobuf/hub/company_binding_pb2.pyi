from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyBinding(_message.Message):
    __slots__ = ("company_id", "hub_id", "state", "billing_enabled", "company_locked", "hub_blocked_by_company", "balance", "subscription_fee", "currency", "next_payment_date", "company_name")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE_INFO: _ClassVar[CompanyBinding.State]
        PENDING_ACCEPTANCE: _ClassVar[CompanyBinding.State]
        ACCEPTED: _ClassVar[CompanyBinding.State]
        PENDING_DELETION: _ClassVar[CompanyBinding.State]
    NO_STATE_INFO: CompanyBinding.State
    PENDING_ACCEPTANCE: CompanyBinding.State
    ACCEPTED: CompanyBinding.State
    PENDING_DELETION: CompanyBinding.State
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BILLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPANY_LOCKED_FIELD_NUMBER: _ClassVar[int]
    HUB_BLOCKED_BY_COMPANY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FEE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAYMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    hub_id: str
    state: CompanyBinding.State
    billing_enabled: bool
    company_locked: bool
    hub_blocked_by_company: bool
    balance: str
    subscription_fee: str
    currency: str
    next_payment_date: str
    company_name: str
    def __init__(self, company_id: _Optional[str] = ..., hub_id: _Optional[str] = ..., state: _Optional[_Union[CompanyBinding.State, str]] = ..., billing_enabled: bool = ..., company_locked: bool = ..., hub_blocked_by_company: bool = ..., balance: _Optional[str] = ..., subscription_fee: _Optional[str] = ..., currency: _Optional[str] = ..., next_payment_date: _Optional[str] = ..., company_name: _Optional[str] = ...) -> None: ...
