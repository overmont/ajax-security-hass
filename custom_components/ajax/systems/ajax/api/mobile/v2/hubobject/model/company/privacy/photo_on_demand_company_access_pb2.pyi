from systems.ajax.api.mobile.v2.common.hub import photo_on_demand_company_rights_pb2 as _photo_on_demand_company_rights_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOnDemandCompanyAccess(_message.Message):
    __slots__ = ("company_id", "rights")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    rights: _photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights
    def __init__(self, company_id: _Optional[str] = ..., rights: _Optional[_Union[_photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights, _Mapping]] = ...) -> None: ...
