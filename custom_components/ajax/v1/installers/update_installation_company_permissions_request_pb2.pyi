from v1.installers.model import permissions_pb2 as _permissions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateInstallationCompanyPermissionsRequest(_message.Message):
    __slots__ = ("company_id", "hub_hex_id", "installation_permissions")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    hub_hex_id: str
    installation_permissions: _permissions_pb2.Permissions
    def __init__(self, company_id: _Optional[str] = ..., hub_hex_id: _Optional[str] = ..., installation_permissions: _Optional[_Union[_permissions_pb2.Permissions, _Mapping]] = ...) -> None: ...
