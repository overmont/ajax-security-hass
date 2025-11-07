from v1.security_company import security_company_pb2 as _security_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchCompanyResponse(_message.Message):
    __slots__ = ("companies",)
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[_security_company_pb2.SecurityCompanyPreview]
    def __init__(self, companies: _Optional[_Iterable[_Union[_security_company_pb2.SecurityCompanyPreview, _Mapping]]] = ...) -> None: ...
