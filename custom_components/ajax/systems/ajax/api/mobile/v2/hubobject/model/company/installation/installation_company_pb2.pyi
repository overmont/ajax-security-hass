from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company import company_info_pb2 as _company_info_pb2
from systems.ajax.api.mobile.v2.common.hub import hub_permission_pb2 as _hub_permission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstallationCompany(_message.Message):
    __slots__ = ("company_info", "permissions", "permissions_expired_at", "hub_user_index")
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    permissions: _hub_permission_pb2.HubPermissions
    permissions_expired_at: _timestamp_pb2.Timestamp
    hub_user_index: int
    def __init__(self, company_info: _Optional[_Union[_company_info_pb2.CompanyInfo, _Mapping]] = ..., permissions: _Optional[_Union[_hub_permission_pb2.HubPermissions, _Mapping]] = ..., permissions_expired_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hub_user_index: _Optional[int] = ...) -> None: ...
