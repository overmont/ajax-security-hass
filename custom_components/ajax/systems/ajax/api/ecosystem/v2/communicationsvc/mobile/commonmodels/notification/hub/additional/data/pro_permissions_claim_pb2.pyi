from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import permission_claim_type_pb2 as _permission_claim_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProPermissionsClaim(_message.Message):
    __slots__ = ("request_id", "hub_hex_id", "pro_name", "pro_mail", "pro_id", "permissions_type")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_NAME_FIELD_NUMBER: _ClassVar[int]
    PRO_MAIL_FIELD_NUMBER: _ClassVar[int]
    PRO_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    hub_hex_id: str
    pro_name: str
    pro_mail: str
    pro_id: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    def __init__(self, request_id: _Optional[str] = ..., hub_hex_id: _Optional[str] = ..., pro_name: _Optional[str] = ..., pro_mail: _Optional[str] = ..., pro_id: _Optional[str] = ..., permissions_type: _Optional[_Union[_permission_claim_type_pb2.PermissionsClaimType, _Mapping]] = ...) -> None: ...
