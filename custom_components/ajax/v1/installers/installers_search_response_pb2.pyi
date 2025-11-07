from v1.common import hub_user_pb2 as _hub_user_pb2
from v1.common import company_pb2 as _company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstallersSearchResponse(_message.Message):
    __slots__ = ("hub_users", "companies")
    HUB_USERS_FIELD_NUMBER: _ClassVar[int]
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    hub_users: _containers.RepeatedCompositeFieldContainer[_hub_user_pb2.HubUser]
    companies: _containers.RepeatedCompositeFieldContainer[_company_pb2.Company]
    def __init__(self, hub_users: _Optional[_Iterable[_Union[_hub_user_pb2.HubUser, _Mapping]]] = ..., companies: _Optional[_Iterable[_Union[_company_pb2.Company, _Mapping]]] = ...) -> None: ...
