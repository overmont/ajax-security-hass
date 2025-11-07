from systems.ajax.api.mobile.v2.common.logo import logo_pb2 as _logo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShortCompany(_message.Message):
    __slots__ = ("company_hex_id", "name", "logo", "websiteUrl")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    WEBSITEURL_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    name: str
    logo: _logo_pb2.Logo
    websiteUrl: str
    def __init__(self, company_hex_id: _Optional[str] = ..., name: _Optional[str] = ..., logo: _Optional[_Union[_logo_pb2.Logo, _Mapping]] = ..., websiteUrl: _Optional[str] = ...) -> None: ...
