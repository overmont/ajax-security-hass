from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponsiblePerson(_message.Message):
    __slots__ = ("id", "facility_id", "first_name", "last_name", "phone_numbers", "email_addresses")
    ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    id: str
    facility_id: str
    first_name: str
    last_name: str
    phone_numbers: _containers.RepeatedCompositeFieldContainer[_phone_number_pb2.PhoneNumber]
    email_addresses: _containers.RepeatedCompositeFieldContainer[_email_address_pb2.EmailAddress]
    def __init__(self, id: _Optional[str] = ..., facility_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_numbers: _Optional[_Iterable[_Union[_phone_number_pb2.PhoneNumber, _Mapping]]] = ..., email_addresses: _Optional[_Iterable[_Union[_email_address_pb2.EmailAddress, _Mapping]]] = ...) -> None: ...
