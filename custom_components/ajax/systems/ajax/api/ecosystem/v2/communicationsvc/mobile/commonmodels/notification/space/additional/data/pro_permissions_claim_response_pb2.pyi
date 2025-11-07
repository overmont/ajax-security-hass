from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import permissions_claim_type_pb2 as _permissions_claim_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import access_request_subject_pb2 as _access_request_subject_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProPermissionsClaimResponse(_message.Message):
    __slots__ = ("grantee", "initiator", "permissions_type", "is_rejected")
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_REJECTED_FIELD_NUMBER: _ClassVar[int]
    grantee: _access_request_subject_pb2.AccessRequestSubject
    initiator: _access_request_subject_pb2.AccessRequestSubject
    permissions_type: _permissions_claim_type_pb2.PermissionsClaimType
    is_rejected: bool
    def __init__(self, grantee: _Optional[_Union[_access_request_subject_pb2.AccessRequestSubject, _Mapping]] = ..., initiator: _Optional[_Union[_access_request_subject_pb2.AccessRequestSubject, _Mapping]] = ..., permissions_type: _Optional[_Union[_permissions_claim_type_pb2.PermissionsClaimType, _Mapping]] = ..., is_rejected: bool = ...) -> None: ...
