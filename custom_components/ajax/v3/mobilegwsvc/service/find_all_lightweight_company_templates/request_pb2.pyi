from v3.mobilegwsvc.commonmodels.company.templates import company_template_type_pb2 as _company_template_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllLightweightCompanyTemplatesRequest(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _company_template_type_pb2.CompanyTemplateType
    def __init__(self, type: _Optional[_Union[_company_template_type_pb2.CompanyTemplateType, str]] = ...) -> None: ...
