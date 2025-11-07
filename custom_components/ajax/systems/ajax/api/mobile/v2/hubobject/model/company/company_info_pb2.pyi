from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common import strings_pb2 as _strings_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company import phod_devices_rights_feasibility_pb2 as _phod_devices_rights_feasibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyInfo(_message.Message):
    __slots__ = ("hex_id", "name", "logo", "emails", "phones", "web_page_url", "available_in", "phod_devices_company_rights_feasibility", "cobranded_status")
    class CobrandedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COBRANDED_STATUS_UNSPECIFIED: _ClassVar[CompanyInfo.CobrandedStatus]
        COBRANDED_STATUS_ON: _ClassVar[CompanyInfo.CobrandedStatus]
        COBRANDED_STATUS_OFF: _ClassVar[CompanyInfo.CobrandedStatus]
    COBRANDED_STATUS_UNSPECIFIED: CompanyInfo.CobrandedStatus
    COBRANDED_STATUS_ON: CompanyInfo.CobrandedStatus
    COBRANDED_STATUS_OFF: CompanyInfo.CobrandedStatus
    class PhoneNumber(_message.Message):
        __slots__ = ("number", "phone_description")
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        PHONE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        number: _wrappers_pb2.StringValue
        phone_description: _wrappers_pb2.StringValue
        def __init__(self, number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone_description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class PhoneNumbers(_message.Message):
        __slots__ = ("phoneNumbers",)
        PHONENUMBERS_FIELD_NUMBER: _ClassVar[int]
        phoneNumbers: _containers.RepeatedCompositeFieldContainer[CompanyInfo.PhoneNumber]
        def __init__(self, phoneNumbers: _Optional[_Iterable[_Union[CompanyInfo.PhoneNumber, _Mapping]]] = ...) -> None: ...
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    WEB_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_IN_FIELD_NUMBER: _ClassVar[int]
    PHOD_DEVICES_COMPANY_RIGHTS_FEASIBILITY_FIELD_NUMBER: _ClassVar[int]
    COBRANDED_STATUS_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    name: _wrappers_pb2.StringValue
    logo: _image_pb2.Images
    emails: _strings_pb2.Strings
    phones: CompanyInfo.PhoneNumbers
    web_page_url: _wrappers_pb2.StringValue
    available_in: _strings_pb2.Strings
    phod_devices_company_rights_feasibility: _phod_devices_rights_feasibility_pb2.PhodDevicesRightsFeasibility
    cobranded_status: CompanyInfo.CobrandedStatus
    def __init__(self, hex_id: _Optional[str] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., logo: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., emails: _Optional[_Union[_strings_pb2.Strings, _Mapping]] = ..., phones: _Optional[_Union[CompanyInfo.PhoneNumbers, _Mapping]] = ..., web_page_url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., available_in: _Optional[_Union[_strings_pb2.Strings, _Mapping]] = ..., phod_devices_company_rights_feasibility: _Optional[_Union[_phod_devices_rights_feasibility_pb2.PhodDevicesRightsFeasibility, str]] = ..., cobranded_status: _Optional[_Union[CompanyInfo.CobrandedStatus, str]] = ...) -> None: ...
