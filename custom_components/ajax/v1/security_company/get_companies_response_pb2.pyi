from v1.security_company import security_company_pb2 as _security_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompaniesResponse(_message.Message):
    __slots__ = ("on_monitoring", "all")
    ON_MONITORING_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    on_monitoring: _containers.RepeatedCompositeFieldContainer[_security_company_pb2.SecurityCompanyPreview]
    all: _containers.RepeatedCompositeFieldContainer[_security_company_pb2.SecurityCompanyPreview]
    def __init__(self, on_monitoring: _Optional[_Iterable[_Union[_security_company_pb2.SecurityCompanyPreview, _Mapping]]] = ..., all: _Optional[_Iterable[_Union[_security_company_pb2.SecurityCompanyPreview, _Mapping]]] = ...) -> None: ...

class GetCompaniesResponseV2(_message.Message):
    __slots__ = ("all",)
    ALL_FIELD_NUMBER: _ClassVar[int]
    all: _containers.RepeatedCompositeFieldContainer[_security_company_pb2.SecurityCompanyPreview]
    def __init__(self, all: _Optional[_Iterable[_Union[_security_company_pb2.SecurityCompanyPreview, _Mapping]]] = ...) -> None: ...
