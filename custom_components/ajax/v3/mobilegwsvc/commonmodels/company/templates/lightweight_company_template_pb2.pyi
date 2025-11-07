from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.company.templates import company_template_type_pb2 as _company_template_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightweightCompanyTemplate(_message.Message):
    __slots__ = ("id", "company_id", "name", "description", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    company_id: str
    name: str
    description: str
    type: _company_template_type_pb2.CompanyTemplateType
    def __init__(self, id: _Optional[str] = ..., company_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_company_template_type_pb2.CompanyTemplateType, str]] = ...) -> None: ...
