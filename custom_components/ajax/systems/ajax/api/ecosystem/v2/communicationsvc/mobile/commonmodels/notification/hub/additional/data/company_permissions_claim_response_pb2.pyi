from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import permission_claim_type_pb2 as _permission_claim_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyPermissionsClaimResponse(_message.Message):
    __slots__ = ("company_name", "company_mail", "permissions_type")
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_MAIL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    company_name: str
    company_mail: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    def __init__(self, company_name: _Optional[str] = ..., company_mail: _Optional[str] = ..., permissions_type: _Optional[_Union[_permission_claim_type_pb2.PermissionsClaimType, _Mapping]] = ...) -> None: ...
