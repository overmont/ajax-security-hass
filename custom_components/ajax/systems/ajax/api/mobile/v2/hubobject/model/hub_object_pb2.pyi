from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company.installation import installation_company_pb2 as _installation_company_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company.monitoring import monitoring_company_pb2 as _monitoring_company_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import surveillance_cameras_company_access_pb2 as _surveillance_cameras_company_access_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import photo_on_demand_company_access_pb2 as _photo_on_demand_company_access_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import privacy_override_pb2 as _privacy_override_pb2
from systems.ajax.api.mobile.v2.hubobject.model.firmware import device_firmware_update_pb2 as _device_firmware_update_pb2
from systems.ajax.api.mobile.v2.hubobject.model.firmware import system_firmware_update_pb2 as _system_firmware_update_pb2
from systems.ajax.api.mobile.v2.common.hub import hub_connection_properties_pb2 as _hub_connection_properties_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubObject(_message.Message):
    __slots__ = ("hex_id", "installation_companies", "monitoring_companies", "photo_on_demand_companies_access", "surveillance_cameras_companies_access", "privacy_overrides", "sim_card", "device_firmware_updates", "system_firmware_update", "hub_connection_properties")
    class InstallationCompanies(_message.Message):
        __slots__ = ("installation_company",)
        INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
        installation_company: _containers.RepeatedCompositeFieldContainer[_installation_company_pb2.InstallationCompany]
        def __init__(self, installation_company: _Optional[_Iterable[_Union[_installation_company_pb2.InstallationCompany, _Mapping]]] = ...) -> None: ...
    class MonitoringCompanies(_message.Message):
        __slots__ = ("monitoring_company",)
        MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
        monitoring_company: _containers.RepeatedCompositeFieldContainer[_monitoring_company_pb2.MonitoringCompany]
        def __init__(self, monitoring_company: _Optional[_Iterable[_Union[_monitoring_company_pb2.MonitoringCompany, _Mapping]]] = ...) -> None: ...
    class PhotoOnDemandCompaniesAccess(_message.Message):
        __slots__ = ("company_access",)
        COMPANY_ACCESS_FIELD_NUMBER: _ClassVar[int]
        company_access: _containers.RepeatedCompositeFieldContainer[_photo_on_demand_company_access_pb2.PhotoOnDemandCompanyAccess]
        def __init__(self, company_access: _Optional[_Iterable[_Union[_photo_on_demand_company_access_pb2.PhotoOnDemandCompanyAccess, _Mapping]]] = ...) -> None: ...
    class SurveillanceCamerasCompaniesAccess(_message.Message):
        __slots__ = ("company_access",)
        COMPANY_ACCESS_FIELD_NUMBER: _ClassVar[int]
        company_access: _containers.RepeatedCompositeFieldContainer[_surveillance_cameras_company_access_pb2.SurveillanceCamerasCompanyAccess]
        def __init__(self, company_access: _Optional[_Iterable[_Union[_surveillance_cameras_company_access_pb2.SurveillanceCamerasCompanyAccess, _Mapping]]] = ...) -> None: ...
    class PrivacyOverrides(_message.Message):
        __slots__ = ("privacy_override",)
        PRIVACY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        privacy_override: _containers.RepeatedCompositeFieldContainer[_privacy_override_pb2.PrivacyOverride]
        def __init__(self, privacy_override: _Optional[_Iterable[_Union[_privacy_override_pb2.PrivacyOverride, _Mapping]]] = ...) -> None: ...
    class DeviceFirmwareUpdates(_message.Message):
        __slots__ = ("device_firmware_update",)
        DEVICE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        device_firmware_update: _containers.RepeatedCompositeFieldContainer[_device_firmware_update_pb2.DeviceFirmwareUpdate]
        def __init__(self, device_firmware_update: _Optional[_Iterable[_Union[_device_firmware_update_pb2.DeviceFirmwareUpdate, _Mapping]]] = ...) -> None: ...
    class SimCard(_message.Message):
        __slots__ = ("active_sim_card", "sim_card_status", "imei", "deactivation_date")
        class SimCardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SIM_CARD_STATUS_NO_INFO: _ClassVar[HubObject.SimCard.SimCardStatus]
            SIM_CARD_STATUS_INACTIVE: _ClassVar[HubObject.SimCard.SimCardStatus]
            SIM_CARD_STATUS_ACTIVE: _ClassVar[HubObject.SimCard.SimCardStatus]
        SIM_CARD_STATUS_NO_INFO: HubObject.SimCard.SimCardStatus
        SIM_CARD_STATUS_INACTIVE: HubObject.SimCard.SimCardStatus
        SIM_CARD_STATUS_ACTIVE: HubObject.SimCard.SimCardStatus
        ACTIVE_SIM_CARD_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_STATUS_FIELD_NUMBER: _ClassVar[int]
        IMEI_FIELD_NUMBER: _ClassVar[int]
        DEACTIVATION_DATE_FIELD_NUMBER: _ClassVar[int]
        active_sim_card: int
        sim_card_status: HubObject.SimCard.SimCardStatus
        imei: str
        deactivation_date: _timestamp_pb2.Timestamp
        def __init__(self, active_sim_card: _Optional[int] = ..., sim_card_status: _Optional[_Union[HubObject.SimCard.SimCardStatus, str]] = ..., imei: _Optional[str] = ..., deactivation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_COMPANIES_ACCESS_FIELD_NUMBER: _ClassVar[int]
    SURVEILLANCE_CAMERAS_COMPANIES_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    SIM_CARD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    installation_companies: HubObject.InstallationCompanies
    monitoring_companies: HubObject.MonitoringCompanies
    photo_on_demand_companies_access: HubObject.PhotoOnDemandCompaniesAccess
    surveillance_cameras_companies_access: HubObject.SurveillanceCamerasCompaniesAccess
    privacy_overrides: HubObject.PrivacyOverrides
    sim_card: HubObject.SimCard
    device_firmware_updates: HubObject.DeviceFirmwareUpdates
    system_firmware_update: _system_firmware_update_pb2.SystemFirmwareUpdate
    hub_connection_properties: _hub_connection_properties_pb2.HubConnectionProperties
    def __init__(self, hex_id: _Optional[str] = ..., installation_companies: _Optional[_Union[HubObject.InstallationCompanies, _Mapping]] = ..., monitoring_companies: _Optional[_Union[HubObject.MonitoringCompanies, _Mapping]] = ..., photo_on_demand_companies_access: _Optional[_Union[HubObject.PhotoOnDemandCompaniesAccess, _Mapping]] = ..., surveillance_cameras_companies_access: _Optional[_Union[HubObject.SurveillanceCamerasCompaniesAccess, _Mapping]] = ..., privacy_overrides: _Optional[_Union[HubObject.PrivacyOverrides, _Mapping]] = ..., sim_card: _Optional[_Union[HubObject.SimCard, _Mapping]] = ..., device_firmware_updates: _Optional[_Union[HubObject.DeviceFirmwareUpdates, _Mapping]] = ..., system_firmware_update: _Optional[_Union[_system_firmware_update_pb2.SystemFirmwareUpdate, _Mapping]] = ..., hub_connection_properties: _Optional[_Union[_hub_connection_properties_pb2.HubConnectionProperties, _Mapping]] = ...) -> None: ...
