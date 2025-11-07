from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubEvent(_message.Message):
    __slots__ = ("id", "hub_id", "hub_name", "source_id", "source_name", "code", "type", "source_room_name", "event_id", "server_received_timestamp", "source_type", "source_room_id", "additional_data", "hub_sub_type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM: _ClassVar[HubEvent.Type]
        ALARM_RECOVERED: _ClassVar[HubEvent.Type]
        MALFUNCTION: _ClassVar[HubEvent.Type]
        FUNCTION_RECOVERED: _ClassVar[HubEvent.Type]
        SECURITY: _ClassVar[HubEvent.Type]
        COMMON: _ClassVar[HubEvent.Type]
        USER: _ClassVar[HubEvent.Type]
        LIFECYCLE: _ClassVar[HubEvent.Type]
        FIBRA_SCAN_ALARM: _ClassVar[HubEvent.Type]
    ALARM: HubEvent.Type
    ALARM_RECOVERED: HubEvent.Type
    MALFUNCTION: HubEvent.Type
    FUNCTION_RECOVERED: HubEvent.Type
    SECURITY: HubEvent.Type
    COMMON: HubEvent.Type
    USER: HubEvent.Type
    LIFECYCLE: HubEvent.Type
    FIBRA_SCAN_ALARM: HubEvent.Type
    class AdditionalData(_message.Message):
        __slots__ = ("access_request", "coordinates", "device_malfunctions", "resource_description", "firmware_version", "malfunction_additional_data", "initiator_additional_data", "approve_permissions_permanently_additional_data", "reject_permissions_additional_data", "approve_permissions_temporary_additional_data", "claim_permissions_request_temporary_additional_data", "claim_permissions_request_permanent_additional_data")
        class AccessRequest(_message.Message):
            __slots__ = ("request_id", "pro_id", "pro_name", "pro_email", "pro_company_id", "owner_id", "owner_name", "owner_email", "requested_access_rights", "access_time_hours")
            class AccessRights(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FULL_ACCESS: _ClassVar[HubEvent.AdditionalData.AccessRequest.AccessRights]
            FULL_ACCESS: HubEvent.AdditionalData.AccessRequest.AccessRights
            REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
            PRO_ID_FIELD_NUMBER: _ClassVar[int]
            PRO_NAME_FIELD_NUMBER: _ClassVar[int]
            PRO_EMAIL_FIELD_NUMBER: _ClassVar[int]
            PRO_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
            OWNER_ID_FIELD_NUMBER: _ClassVar[int]
            OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
            OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
            REQUESTED_ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            request_id: int
            pro_id: str
            pro_name: str
            pro_email: str
            pro_company_id: str
            owner_id: str
            owner_name: str
            owner_email: str
            requested_access_rights: HubEvent.AdditionalData.AccessRequest.AccessRights
            access_time_hours: int
            def __init__(self, request_id: _Optional[int] = ..., pro_id: _Optional[str] = ..., pro_name: _Optional[str] = ..., pro_email: _Optional[str] = ..., pro_company_id: _Optional[str] = ..., owner_id: _Optional[str] = ..., owner_name: _Optional[str] = ..., owner_email: _Optional[str] = ..., requested_access_rights: _Optional[_Union[HubEvent.AdditionalData.AccessRequest.AccessRights, str]] = ..., access_time_hours: _Optional[int] = ...) -> None: ...
        class Coordinates(_message.Message):
            __slots__ = ("latitude", "longitude")
            LATITUDE_FIELD_NUMBER: _ClassVar[int]
            LONGITUDE_FIELD_NUMBER: _ClassVar[int]
            latitude: float
            longitude: float
            def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...
        class DeviceMalfunctions(_message.Message):
            __slots__ = ("items",)
            class DeviceMalfunction(_message.Message):
                __slots__ = ("obj_id", "obj_type", "obj_name", "obj_room_id", "obj_room_name", "hub_name", "text")
                OBJ_ID_FIELD_NUMBER: _ClassVar[int]
                OBJ_TYPE_FIELD_NUMBER: _ClassVar[int]
                OBJ_NAME_FIELD_NUMBER: _ClassVar[int]
                OBJ_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                OBJ_ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
                HUB_NAME_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                obj_id: str
                obj_type: str
                obj_name: str
                obj_room_id: str
                obj_room_name: str
                hub_name: str
                text: str
                def __init__(self, obj_id: _Optional[str] = ..., obj_type: _Optional[str] = ..., obj_name: _Optional[str] = ..., obj_room_id: _Optional[str] = ..., obj_room_name: _Optional[str] = ..., hub_name: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            items: _containers.RepeatedCompositeFieldContainer[HubEvent.AdditionalData.DeviceMalfunctions.DeviceMalfunction]
            def __init__(self, items: _Optional[_Iterable[_Union[HubEvent.AdditionalData.DeviceMalfunctions.DeviceMalfunction, _Mapping]]] = ...) -> None: ...
        class ResourceDescription(_message.Message):
            __slots__ = ("ordered_resource_links", "link_expiration_timestamp")
            class ResourceLink(_message.Message):
                __slots__ = ("url", "status")
                class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    IN_PROGRESS: _ClassVar[HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status]
                    READY: _ClassVar[HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status]
                    FAILED: _ClassVar[HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status]
                IN_PROGRESS: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                READY: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                FAILED: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                URL_FIELD_NUMBER: _ClassVar[int]
                STATUS_FIELD_NUMBER: _ClassVar[int]
                url: str
                status: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                def __init__(self, url: _Optional[str] = ..., status: _Optional[_Union[HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status, str]] = ...) -> None: ...
            ORDERED_RESOURCE_LINKS_FIELD_NUMBER: _ClassVar[int]
            LINK_EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            ordered_resource_links: _containers.RepeatedCompositeFieldContainer[HubEvent.AdditionalData.ResourceDescription.ResourceLink]
            link_expiration_timestamp: _timestamp_pb2.Timestamp
            def __init__(self, ordered_resource_links: _Optional[_Iterable[_Union[HubEvent.AdditionalData.ResourceDescription.ResourceLink, _Mapping]]] = ..., link_expiration_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class FirmwareVersion(_message.Message):
            __slots__ = ("version",)
            VERSION_FIELD_NUMBER: _ClassVar[int]
            version: str
            def __init__(self, version: _Optional[str] = ...) -> None: ...
        class MalfunctionAdditionalData(_message.Message):
            __slots__ = ("device_malfunction",)
            class DeviceMalfunctionInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_MALFUNCTION_INFO: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                CABLE_BREAK_ISSUE: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                VOLTAGE_INSTABILITY: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                SIREN_VOLUME_TEST_REQUIRED: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                CO_SENSOR_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                SMOKE_DETECTOR_CAMERA_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                ACCELEROMETER_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                BAD_INPUT_RESISTANCE: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                MODEM_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                WIFI_CONNECTION_FAIL: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                BATTERY_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                BATTERY_CHARGE_ERROR: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                SOFTWARE_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
                FLASH_MALFUNCTION: _ClassVar[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo]
            NO_MALFUNCTION_INFO: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            CABLE_BREAK_ISSUE: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            VOLTAGE_INSTABILITY: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            SIREN_VOLUME_TEST_REQUIRED: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            CO_SENSOR_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            CO_SENSOR_LEVEL_EXCEEDED: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            SMOKE_DETECTOR_CAMERA_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            MICROWAVE_SENSOR_CALIBRATION_ERROR: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            ACCELEROMETER_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            BAD_INPUT_RESISTANCE: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            MODEM_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            WIFI_CONNECTION_FAIL: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            BATTERY_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            BATTERY_CHARGE_ERROR: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            SOFTWARE_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            FLASH_MALFUNCTION: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            DEVICE_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
            device_malfunction: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            def __init__(self, device_malfunction: _Optional[_Union[HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo, str]] = ...) -> None: ...
        class Initiator(_message.Message):
            __slots__ = ("initiator_name",)
            INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
            initiator_name: str
            def __init__(self, initiator_name: _Optional[str] = ...) -> None: ...
        class ApprovePermissionsRequestPermanentlyAdditionalData(_message.Message):
            __slots__ = ("name", "email")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
        class RejectPermissionsRequestAdditionalData(_message.Message):
            __slots__ = ("name", "email")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
        class ApprovePermissionsRequestTemporaryAdditionalData(_message.Message):
            __slots__ = ("name", "email", "access_time_hours")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            access_time_hours: int
            def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., access_time_hours: _Optional[int] = ...) -> None: ...
        class ClaimPermissionsRequestTemporaryAdditionalData(_message.Message):
            __slots__ = ("claimID", "emailCompany", "access_time_hours")
            CLAIMID_FIELD_NUMBER: _ClassVar[int]
            EMAILCOMPANY_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            claimID: str
            emailCompany: str
            access_time_hours: int
            def __init__(self, claimID: _Optional[str] = ..., emailCompany: _Optional[str] = ..., access_time_hours: _Optional[int] = ...) -> None: ...
        class ClaimPermissionsRequestPermanentAdditionalData(_message.Message):
            __slots__ = ("claimID", "emailCompany")
            CLAIMID_FIELD_NUMBER: _ClassVar[int]
            EMAILCOMPANY_FIELD_NUMBER: _ClassVar[int]
            claimID: str
            emailCompany: str
            def __init__(self, claimID: _Optional[str] = ..., emailCompany: _Optional[str] = ...) -> None: ...
        ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        COORDINATES_FIELD_NUMBER: _ClassVar[int]
        DEVICE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTION_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        INITIATOR_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        APPROVE_PERMISSIONS_PERMANENTLY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        REJECT_PERMISSIONS_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        APPROVE_PERMISSIONS_TEMPORARY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        CLAIM_PERMISSIONS_REQUEST_TEMPORARY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        CLAIM_PERMISSIONS_REQUEST_PERMANENT_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        access_request: HubEvent.AdditionalData.AccessRequest
        coordinates: HubEvent.AdditionalData.Coordinates
        device_malfunctions: HubEvent.AdditionalData.DeviceMalfunctions
        resource_description: HubEvent.AdditionalData.ResourceDescription
        firmware_version: HubEvent.AdditionalData.FirmwareVersion
        malfunction_additional_data: HubEvent.AdditionalData.MalfunctionAdditionalData
        initiator_additional_data: HubEvent.AdditionalData.Initiator
        approve_permissions_permanently_additional_data: HubEvent.AdditionalData.ApprovePermissionsRequestPermanentlyAdditionalData
        reject_permissions_additional_data: HubEvent.AdditionalData.RejectPermissionsRequestAdditionalData
        approve_permissions_temporary_additional_data: HubEvent.AdditionalData.ApprovePermissionsRequestTemporaryAdditionalData
        claim_permissions_request_temporary_additional_data: HubEvent.AdditionalData.ClaimPermissionsRequestTemporaryAdditionalData
        claim_permissions_request_permanent_additional_data: HubEvent.AdditionalData.ClaimPermissionsRequestPermanentAdditionalData
        def __init__(self, access_request: _Optional[_Union[HubEvent.AdditionalData.AccessRequest, _Mapping]] = ..., coordinates: _Optional[_Union[HubEvent.AdditionalData.Coordinates, _Mapping]] = ..., device_malfunctions: _Optional[_Union[HubEvent.AdditionalData.DeviceMalfunctions, _Mapping]] = ..., resource_description: _Optional[_Union[HubEvent.AdditionalData.ResourceDescription, _Mapping]] = ..., firmware_version: _Optional[_Union[HubEvent.AdditionalData.FirmwareVersion, _Mapping]] = ..., malfunction_additional_data: _Optional[_Union[HubEvent.AdditionalData.MalfunctionAdditionalData, _Mapping]] = ..., initiator_additional_data: _Optional[_Union[HubEvent.AdditionalData.Initiator, _Mapping]] = ..., approve_permissions_permanently_additional_data: _Optional[_Union[HubEvent.AdditionalData.ApprovePermissionsRequestPermanentlyAdditionalData, _Mapping]] = ..., reject_permissions_additional_data: _Optional[_Union[HubEvent.AdditionalData.RejectPermissionsRequestAdditionalData, _Mapping]] = ..., approve_permissions_temporary_additional_data: _Optional[_Union[HubEvent.AdditionalData.ApprovePermissionsRequestTemporaryAdditionalData, _Mapping]] = ..., claim_permissions_request_temporary_additional_data: _Optional[_Union[HubEvent.AdditionalData.ClaimPermissionsRequestTemporaryAdditionalData, _Mapping]] = ..., claim_permissions_request_permanent_additional_data: _Optional[_Union[HubEvent.AdditionalData.ClaimPermissionsRequestPermanentAdditionalData, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_RECEIVED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    HUB_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    hub_id: str
    hub_name: str
    source_id: str
    source_name: str
    code: str
    type: HubEvent.Type
    source_room_name: str
    event_id: str
    server_received_timestamp: _timestamp_pb2.Timestamp
    source_type: str
    source_room_id: str
    additional_data: HubEvent.AdditionalData
    hub_sub_type: str
    def __init__(self, id: _Optional[str] = ..., hub_id: _Optional[str] = ..., hub_name: _Optional[str] = ..., source_id: _Optional[str] = ..., source_name: _Optional[str] = ..., code: _Optional[str] = ..., type: _Optional[_Union[HubEvent.Type, str]] = ..., source_room_name: _Optional[str] = ..., event_id: _Optional[str] = ..., server_received_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_type: _Optional[str] = ..., source_room_id: _Optional[str] = ..., additional_data: _Optional[_Union[HubEvent.AdditionalData, _Mapping]] = ..., hub_sub_type: _Optional[str] = ...) -> None: ...
