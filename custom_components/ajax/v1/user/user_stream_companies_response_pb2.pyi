from v1.common import company_pb2 as _company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStreamCompaniesResponse(_message.Message):
    __slots__ = ("user_companies",)
    USER_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    user_companies: _containers.RepeatedCompositeFieldContainer[_company_pb2.Company]
    def __init__(self, user_companies: _Optional[_Iterable[_Union[_company_pb2.Company, _Mapping]]] = ...) -> None: ...
