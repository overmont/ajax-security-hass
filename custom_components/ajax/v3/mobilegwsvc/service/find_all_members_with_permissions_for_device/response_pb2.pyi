from systems.ajax.api.mobile.v2.common.space.member import standalone_device_permissions_pb2 as _standalone_device_permissions_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllMembersWithPermissionsForDeviceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("space_member_device_permissions",)
        class SpaceMemberDevicePermissions(_message.Message):
            __slots__ = ("space_member_id", "space_company_id", "device_permissions")
            class SpaceMemberId(_message.Message):
                __slots__ = ("space_member_id",)
                SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
                space_member_id: str
                def __init__(self, space_member_id: _Optional[str] = ...) -> None: ...
            class SpaceCompanyId(_message.Message):
                __slots__ = ("space_member_id", "company_id")
                SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
                COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
                space_member_id: str
                company_id: str
                def __init__(self, space_member_id: _Optional[str] = ..., company_id: _Optional[str] = ...) -> None: ...
            SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
            SPACE_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
            DEVICE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            space_member_id: FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions.SpaceMemberId
            space_company_id: FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions.SpaceCompanyId
            device_permissions: _standalone_device_permissions_pb2.StandaloneDevicePermissions
            def __init__(self, space_member_id: _Optional[_Union[FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions.SpaceMemberId, _Mapping]] = ..., space_company_id: _Optional[_Union[FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions.SpaceCompanyId, _Mapping]] = ..., device_permissions: _Optional[_Union[_standalone_device_permissions_pb2.StandaloneDevicePermissions, _Mapping]] = ...) -> None: ...
        SPACE_MEMBER_DEVICE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        space_member_device_permissions: _containers.RepeatedCompositeFieldContainer[FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions]
        def __init__(self, space_member_device_permissions: _Optional[_Iterable[_Union[FindAllMembersWithPermissionsForDeviceResponse.Success.SpaceMemberDevicePermissions, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllMembersWithPermissionsForDeviceResponse.Success
    failure: FindAllMembersWithPermissionsForDeviceResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAllMembersWithPermissionsForDeviceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAllMembersWithPermissionsForDeviceResponse.Failure, _Mapping]] = ...) -> None: ...
