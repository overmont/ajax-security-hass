from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import display_member_permissions_pb2 as _display_member_permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberPermissionsRequest(_message.Message):
    __slots__ = ("space_id", "member_id", "update")
    class PermissionsUpdate(_message.Message):
        __slots__ = ("space_permission_patch", "hub_permission_patch", "hub_permission_extended_patch")
        class HubPermissionPatch(_message.Message):
            __slots__ = ("permission", "enabled")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: _display_member_permissions_pb2.DisplaySpaceMemberHubPermission
            enabled: bool
            def __init__(self, permission: _Optional[_Union[_display_member_permissions_pb2.DisplaySpaceMemberHubPermission, str]] = ..., enabled: bool = ...) -> None: ...
        class SpacePermissionPatch(_message.Message):
            __slots__ = ("permission", "enabled")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: _display_member_permissions_pb2.DisplaySpaceMemberSpacePermission
            enabled: bool
            def __init__(self, permission: _Optional[_Union[_display_member_permissions_pb2.DisplaySpaceMemberSpacePermission, str]] = ..., enabled: bool = ...) -> None: ...
        class HubPermissionExtendedPatch(_message.Message):
            __slots__ = ("permission", "enabled")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: _display_member_permissions_pb2.DisplaySpaceMemberHubPermissionExtended
            enabled: bool
            def __init__(self, permission: _Optional[_Union[_display_member_permissions_pb2.DisplaySpaceMemberHubPermissionExtended, str]] = ..., enabled: bool = ...) -> None: ...
        SPACE_PERMISSION_PATCH_FIELD_NUMBER: _ClassVar[int]
        HUB_PERMISSION_PATCH_FIELD_NUMBER: _ClassVar[int]
        HUB_PERMISSION_EXTENDED_PATCH_FIELD_NUMBER: _ClassVar[int]
        space_permission_patch: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.SpacePermissionPatch]
        hub_permission_patch: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionPatch]
        hub_permission_extended_patch: _containers.RepeatedCompositeFieldContainer[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionExtendedPatch]
        def __init__(self, space_permission_patch: _Optional[_Iterable[_Union[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.SpacePermissionPatch, _Mapping]]] = ..., hub_permission_patch: _Optional[_Iterable[_Union[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionPatch, _Mapping]]] = ..., hub_permission_extended_patch: _Optional[_Iterable[_Union[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionExtendedPatch, _Mapping]]] = ...) -> None: ...
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    member_id: str
    update: UpdateSpaceMemberPermissionsRequest.PermissionsUpdate
    def __init__(self, space_id: _Optional[str] = ..., member_id: _Optional[str] = ..., update: _Optional[_Union[UpdateSpaceMemberPermissionsRequest.PermissionsUpdate, _Mapping]] = ...) -> None: ...

class UpdateSpaceMemberPermissionsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSpaceMemberPermissionsResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[UpdateSpaceMemberPermissionsResponse.Failure, _Mapping]] = ...) -> None: ...
