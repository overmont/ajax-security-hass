from v1.common import address_pb2 as _address_pb2
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v1.facility import facility_monitoring_status_pb2 as _facility_monitoring_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Facility(_message.Message):
    __slots__ = ("id", "hub_id", "hub_name", "company_id", "facility_general_info", "status", "connection_status", "version", "hub_locked_by_company", "sleep_until", "privacy_override_status", "monitoring_status", "space_id")
    class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFFLINE: _ClassVar[Facility.ConnectionStatus]
        ONLINE: _ClassVar[Facility.ConnectionStatus]
    OFFLINE: Facility.ConnectionStatus
    ONLINE: Facility.ConnectionStatus
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MONITORING_APPROVED: _ClassVar[Facility.Status]
        MONITORING_REQUESTED: _ClassVar[Facility.Status]
        IN_SLEEP_MODE: _ClassVar[Facility.Status]
        NO_MONITORING: _ClassVar[Facility.Status]
    MONITORING_APPROVED: Facility.Status
    MONITORING_REQUESTED: Facility.Status
    IN_SLEEP_MODE: Facility.Status
    NO_MONITORING: Facility.Status
    class PrivacyOverrideStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVACY_OVERRIDE_STATUS_UNSPECIFIED: _ClassVar[Facility.PrivacyOverrideStatus]
        PRIVACY_OVERRIDE_STATUS_DISABLED: _ClassVar[Facility.PrivacyOverrideStatus]
        PRIVACY_OVERRIDE_STATUS_ENABLED: _ClassVar[Facility.PrivacyOverrideStatus]
    PRIVACY_OVERRIDE_STATUS_UNSPECIFIED: Facility.PrivacyOverrideStatus
    PRIVACY_OVERRIDE_STATUS_DISABLED: Facility.PrivacyOverrideStatus
    PRIVACY_OVERRIDE_STATUS_ENABLED: Facility.PrivacyOverrideStatus
    class GeneralInfo(_message.Message):
        __slots__ = ("name", "registration_number", "address", "phone_numbers", "email_addresses")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        name: str
        registration_number: str
        address: _address_pb2.Address
        phone_numbers: _containers.RepeatedCompositeFieldContainer[_phone_number_pb2.PhoneNumber]
        email_addresses: _containers.RepeatedCompositeFieldContainer[_email_address_pb2.EmailAddress]
        def __init__(self, name: _Optional[str] = ..., registration_number: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., phone_numbers: _Optional[_Iterable[_Union[_phone_number_pb2.PhoneNumber, _Mapping]]] = ..., email_addresses: _Optional[_Iterable[_Union[_email_address_pb2.EmailAddress, _Mapping]]] = ...) -> None: ...
    class Note(_message.Message):
        __slots__ = ("id", "facility_id", "text", "version", "index")
        ID_FIELD_NUMBER: _ClassVar[int]
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        id: str
        facility_id: str
        text: str
        version: int
        index: int
        def __init__(self, id: _Optional[str] = ..., facility_id: _Optional[str] = ..., text: _Optional[str] = ..., version: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_GENERAL_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HUB_LOCKED_BY_COMPANY_FIELD_NUMBER: _ClassVar[int]
    SLEEP_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDE_STATUS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATUS_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    hub_id: str
    hub_name: str
    company_id: str
    facility_general_info: Facility.GeneralInfo
    status: Facility.Status
    connection_status: Facility.ConnectionStatus
    version: int
    hub_locked_by_company: bool
    sleep_until: _timestamp_pb2.Timestamp
    privacy_override_status: Facility.PrivacyOverrideStatus
    monitoring_status: _facility_monitoring_status_pb2.MonitoringStatus
    space_id: str
    def __init__(self, id: _Optional[str] = ..., hub_id: _Optional[str] = ..., hub_name: _Optional[str] = ..., company_id: _Optional[str] = ..., facility_general_info: _Optional[_Union[Facility.GeneralInfo, _Mapping]] = ..., status: _Optional[_Union[Facility.Status, str]] = ..., connection_status: _Optional[_Union[Facility.ConnectionStatus, str]] = ..., version: _Optional[int] = ..., hub_locked_by_company: bool = ..., sleep_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., privacy_override_status: _Optional[_Union[Facility.PrivacyOverrideStatus, str]] = ..., monitoring_status: _Optional[_Union[_facility_monitoring_status_pb2.MonitoringStatus, str]] = ..., space_id: _Optional[str] = ...) -> None: ...
