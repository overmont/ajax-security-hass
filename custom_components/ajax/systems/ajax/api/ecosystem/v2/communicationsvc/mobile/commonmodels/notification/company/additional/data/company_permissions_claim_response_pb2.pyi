from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import permission_claim_type_pb2 as _permission_claim_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import initiator_info_pb2 as _initiator_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyPermissionsClaimResponse(_message.Message):
    __slots__ = ("request_id", "company_name", "company_mail", "permissions_type", "initiator_info")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_MAIL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    company_name: str
    company_mail: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    initiator_info: _initiator_info_pb2.InitiatorInfo
    def __init__(self, request_id: _Optional[str] = ..., company_name: _Optional[str] = ..., company_mail: _Optional[str] = ..., permissions_type: _Optional[_Union[_permission_claim_type_pb2.PermissionsClaimType, _Mapping]] = ..., initiator_info: _Optional[_Union[_initiator_info_pb2.InitiatorInfo, _Mapping]] = ...) -> None: ...
