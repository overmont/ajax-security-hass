from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import permissions_claim_type_pb2 as _permissions_claim_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProPermissionsClaimRequest(_message.Message):
    __slots__ = ("request_id", "grantee_name", "grantee_mail", "permissions_type")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_NAME_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_MAIL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    grantee_name: str
    grantee_mail: str
    permissions_type: _permissions_claim_type_pb2.PermissionsClaimType
    def __init__(self, request_id: _Optional[str] = ..., grantee_name: _Optional[str] = ..., grantee_mail: _Optional[str] = ..., permissions_type: _Optional[_Union[_permissions_claim_type_pb2.PermissionsClaimType, _Mapping]] = ...) -> None: ...
