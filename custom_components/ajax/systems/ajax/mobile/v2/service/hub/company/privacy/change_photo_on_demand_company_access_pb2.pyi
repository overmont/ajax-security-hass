from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.hub import photo_on_demand_company_rights_pb2 as _photo_on_demand_company_rights_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangePhotoOnDemandCompanyAccessRequest(_message.Message):
    __slots__ = ("hub_id", "company_id", "company_rights")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    company_id: str
    company_rights: _photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights
    def __init__(self, hub_id: _Optional[str] = ..., company_id: _Optional[str] = ..., company_rights: _Optional[_Union[_photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights, _Mapping]] = ...) -> None: ...

class ChangePhotoOnDemandCompanyAccessResponse(_message.Message):
    __slots__ = ("success", "error")
    class Error(_message.Message):
        __slots__ = ("internal_error", "company_on_hub_not_found_error", "permission_denied_error", "deadline_exceeded_error")
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        COMPANY_ON_HUB_NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_ERROR_FIELD_NUMBER: _ClassVar[int]
        DEADLINE_EXCEEDED_ERROR_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.InternalError
        company_on_hub_not_found_error: _response_pb2.CompanyOnHubNotFoundError
        permission_denied_error: _response_pb2.PermissionDeniedError
        deadline_exceeded_error: _response_pb2.DeadlineExceededError
        def __init__(self, internal_error: _Optional[_Union[_response_pb2.InternalError, _Mapping]] = ..., company_on_hub_not_found_error: _Optional[_Union[_response_pb2.CompanyOnHubNotFoundError, _Mapping]] = ..., permission_denied_error: _Optional[_Union[_response_pb2.PermissionDeniedError, _Mapping]] = ..., deadline_exceeded_error: _Optional[_Union[_response_pb2.DeadlineExceededError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    error: ChangePhotoOnDemandCompanyAccessResponse.Error
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., error: _Optional[_Union[ChangePhotoOnDemandCompanyAccessResponse.Error, _Mapping]] = ...) -> None: ...
