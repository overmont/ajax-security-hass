from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.capability import space_capabilities_pb2 as _space_capabilities_pb2
from systems.ajax.api.mobile.v2.common.space.company import privacy_override_pb2 as _privacy_override_pb2
from systems.ajax.api.mobile.v2.common.space.company import space_installation_company_pb2 as _space_installation_company_pb2
from systems.ajax.api.mobile.v2.common.space.company import space_monitoring_company_pb2 as _space_monitoring_company_pb2
from systems.ajax.api.mobile.v2.common.space import current_member_pb2 as _current_member_pb2
from systems.ajax.api.mobile.v2.common.space.device import standalone_device_pb2 as _standalone_device_pb2
from systems.ajax.api.mobile.v2.common.space.member import pending_member_pb2 as _pending_member_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_member_pb2 as _space_member_pb2
from systems.ajax.api.mobile.v2.common.space.room import room_pb2 as _room_pb2
from systems.ajax.api.mobile.v2.common.space.security.group import group_pb2 as _group_pb2
from systems.ajax.api.mobile.v2.common.space.security import space_security_mode_pb2 as _space_security_mode_pb2
from systems.ajax.api.mobile.v2.common.space import space_pb2 as _space_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.space import space_profile_pb2 as _space_profile_pb2
from systems.ajax.api.mobile.v2.common.time import time_zone_pb2 as _time_zone_pb2
from systems.ajax.api.mobile.v2.common.video import video_wall_pb2 as _video_wall_pb2
from systems.ajax.api.mobile.v2.common.space import space_address_pb2 as _space_address_pb2
from systems.ajax.api.mobile.v2.common.accounting import service_deactivation_pending_status_pb2 as _service_deactivation_pending_status_pb2
from systems.ajax.api.mobile.v2.common.accounting import extra_services_availability_status_pb2 as _extra_services_availability_status_pb2
from systems.ajax.api.mobile.v2.common.space.stream import external_stream_control_pb2 as _external_stream_control_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceUpdatesRequest(_message.Message):
    __slots__ = ("space_locator",)
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class StreamSpaceUpdatesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update", "updates")
        class Updates(_message.Message):
            __slots__ = ("updates",)
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            updates: _containers.RepeatedCompositeFieldContainer[StreamSpaceUpdatesResponse.Success.Update]
            def __init__(self, updates: _Optional[_Iterable[_Union[StreamSpaceUpdatesResponse.Success.Update, _Mapping]]] = ...) -> None: ...
        class Update(_message.Message):
            __slots__ = ("space_id", "space_update_type", "current_member", "total_notification_unread_counter", "security_mode", "group", "profile", "member", "room", "device", "installation_company", "monitoring_company", "privacy_override", "time_zone_id", "pending_member", "video_wall", "address", "service_deactivation_pending_status", "extra_services_availability_status", "space_capabilities", "extra_services_availability_status_v2", "external_stream_controls")
            class SpaceUpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SPACE_UPDATE_TYPE_UNKNOWN: _ClassVar[StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType]
                SPACE_UPDATE_TYPE_ADD: _ClassVar[StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType]
                SPACE_UPDATE_TYPE_UPDATE: _ClassVar[StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType]
                SPACE_UPDATE_TYPE_REMOVE: _ClassVar[StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType]
            SPACE_UPDATE_TYPE_UNKNOWN: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            SPACE_UPDATE_TYPE_ADD: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            SPACE_UPDATE_TYPE_UPDATE: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            SPACE_UPDATE_TYPE_REMOVE: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            SPACE_ID_FIELD_NUMBER: _ClassVar[int]
            SPACE_UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
            TOTAL_NOTIFICATION_UNREAD_COUNTER_FIELD_NUMBER: _ClassVar[int]
            SECURITY_MODE_FIELD_NUMBER: _ClassVar[int]
            GROUP_FIELD_NUMBER: _ClassVar[int]
            PROFILE_FIELD_NUMBER: _ClassVar[int]
            MEMBER_FIELD_NUMBER: _ClassVar[int]
            ROOM_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
            MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
            PRIVACY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
            TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
            PENDING_MEMBER_FIELD_NUMBER: _ClassVar[int]
            VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            SERVICE_DEACTIVATION_PENDING_STATUS_FIELD_NUMBER: _ClassVar[int]
            EXTRA_SERVICES_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
            SPACE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
            EXTRA_SERVICES_AVAILABILITY_STATUS_V2_FIELD_NUMBER: _ClassVar[int]
            EXTERNAL_STREAM_CONTROLS_FIELD_NUMBER: _ClassVar[int]
            space_id: str
            space_update_type: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            current_member: _current_member_pb2.CurrentMember
            total_notification_unread_counter: int
            security_mode: _space_security_mode_pb2.SpaceSecurityMode
            group: _group_pb2.Group
            profile: _space_profile_pb2.SpaceProfile
            member: _space_member_pb2.SpaceMember
            room: _room_pb2.Room
            device: _standalone_device_pb2.StandaloneDevice
            installation_company: _space_installation_company_pb2.SpaceInstallationCompany
            monitoring_company: _space_monitoring_company_pb2.SpaceMonitoringCompany
            privacy_override: _privacy_override_pb2.PrivacyOverride
            time_zone_id: _time_zone_pb2.TimeZone
            pending_member: _pending_member_pb2.PendingMember
            video_wall: _video_wall_pb2.VideoWall
            address: _space_address_pb2.SpaceAddress
            service_deactivation_pending_status: _service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus
            extra_services_availability_status: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
            space_capabilities: _space_capabilities_pb2.SpaceCapabilities
            extra_services_availability_status_v2: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
            external_stream_controls: _external_stream_control_pb2.ExternalStreamControl
            def __init__(self, space_id: _Optional[str] = ..., space_update_type: _Optional[_Union[StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType, str]] = ..., current_member: _Optional[_Union[_current_member_pb2.CurrentMember, _Mapping]] = ..., total_notification_unread_counter: _Optional[int] = ..., security_mode: _Optional[_Union[_space_security_mode_pb2.SpaceSecurityMode, _Mapping]] = ..., group: _Optional[_Union[_group_pb2.Group, _Mapping]] = ..., profile: _Optional[_Union[_space_profile_pb2.SpaceProfile, _Mapping]] = ..., member: _Optional[_Union[_space_member_pb2.SpaceMember, _Mapping]] = ..., room: _Optional[_Union[_room_pb2.Room, _Mapping]] = ..., device: _Optional[_Union[_standalone_device_pb2.StandaloneDevice, _Mapping]] = ..., installation_company: _Optional[_Union[_space_installation_company_pb2.SpaceInstallationCompany, _Mapping]] = ..., monitoring_company: _Optional[_Union[_space_monitoring_company_pb2.SpaceMonitoringCompany, _Mapping]] = ..., privacy_override: _Optional[_Union[_privacy_override_pb2.PrivacyOverride, _Mapping]] = ..., time_zone_id: _Optional[_Union[_time_zone_pb2.TimeZone, _Mapping]] = ..., pending_member: _Optional[_Union[_pending_member_pb2.PendingMember, _Mapping]] = ..., video_wall: _Optional[_Union[_video_wall_pb2.VideoWall, _Mapping]] = ..., address: _Optional[_Union[_space_address_pb2.SpaceAddress, _Mapping]] = ..., service_deactivation_pending_status: _Optional[_Union[_service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus, str]] = ..., extra_services_availability_status: _Optional[_Union[_extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus, str]] = ..., space_capabilities: _Optional[_Union[_space_capabilities_pb2.SpaceCapabilities, _Mapping]] = ..., extra_services_availability_status_v2: _Optional[_Union[_extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus, str]] = ..., external_stream_controls: _Optional[_Union[_external_stream_control_pb2.ExternalStreamControl, _Mapping]] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        snapshot: _space_pb2.Space
        update: StreamSpaceUpdatesResponse.Success.Update
        updates: StreamSpaceUpdatesResponse.Success.Updates
        def __init__(self, snapshot: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., update: _Optional[_Union[StreamSpaceUpdatesResponse.Success.Update, _Mapping]] = ..., updates: _Optional[_Union[StreamSpaceUpdatesResponse.Success.Updates, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceUpdatesResponse.Success
    failure: StreamSpaceUpdatesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamSpaceUpdatesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamSpaceUpdatesResponse.Failure, _Mapping]] = ...) -> None: ...
