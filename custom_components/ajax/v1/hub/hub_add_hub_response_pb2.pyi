from v1.common import access_rights_pb2 as _access_rights_pb2
from v1.common.privacy import employee_photo_on_demand_access_pb2 as _employee_photo_on_demand_access_pb2
from v1.common.privacy import employee_surveillance_cameras_access_pb2 as _employee_surveillance_cameras_access_pb2
from v1.facility import facility_pb2 as _facility_pb2
from v1.facility import facility_editable_fields_pb2 as _facility_editable_fields_pb2
from v1.hub import monitoring_company_on_hub_pb2 as _monitoring_company_on_hub_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubAddHubResponse(_message.Message):
    __slots__ = ("facility", "access_rights", "monitoring_companies", "facility_editable_fields", "employee_photo_on_demand_access", "employee_surveillance_cameras_access")
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    FACILITY_EDITABLE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_PHOTO_ON_DEMAND_ACCESS_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_SURVEILLANCE_CAMERAS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    facility: _facility_pb2.Facility
    access_rights: _access_rights_pb2.AccessRights
    monitoring_companies: _containers.RepeatedCompositeFieldContainer[_monitoring_company_on_hub_pb2.MonitoringCompanyOnHub]
    facility_editable_fields: _facility_editable_fields_pb2.FacilityEditableFields
    employee_photo_on_demand_access: _employee_photo_on_demand_access_pb2.EmployeePhotoOnDemandAccess
    employee_surveillance_cameras_access: _employee_surveillance_cameras_access_pb2.EmployeeSurveillanceCamerasAccess
    def __init__(self, facility: _Optional[_Union[_facility_pb2.Facility, _Mapping]] = ..., access_rights: _Optional[_Union[_access_rights_pb2.AccessRights, _Mapping]] = ..., monitoring_companies: _Optional[_Iterable[_Union[_monitoring_company_on_hub_pb2.MonitoringCompanyOnHub, _Mapping]]] = ..., facility_editable_fields: _Optional[_Union[_facility_editable_fields_pb2.FacilityEditableFields, _Mapping]] = ..., employee_photo_on_demand_access: _Optional[_Union[_employee_photo_on_demand_access_pb2.EmployeePhotoOnDemandAccess, _Mapping]] = ..., employee_surveillance_cameras_access: _Optional[_Union[_employee_surveillance_cameras_access_pb2.EmployeeSurveillanceCamerasAccess, _Mapping]] = ...) -> None: ...
