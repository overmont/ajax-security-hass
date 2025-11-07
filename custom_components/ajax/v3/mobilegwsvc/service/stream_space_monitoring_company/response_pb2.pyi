from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2_1
from systems.ajax.api.mobile.v2.common.space.company import space_monitoring_company_pb2 as _space_monitoring_company_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceMonitoringCompanyResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        class Snapshot(_message.Message):
            __slots__ = ("space_monitoring_company",)
            SPACE_MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
            space_monitoring_company: _space_monitoring_company_pb2.SpaceMonitoringCompany
            def __init__(self, space_monitoring_company: _Optional[_Union[_space_monitoring_company_pb2.SpaceMonitoringCompany, _Mapping]] = ...) -> None: ...
        class Update(_message.Message):
            __slots__ = ("space_monitoring_company", "update_type")
            class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UPDATE_TYPE_UNSPECIFIED: _ClassVar[StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType]
                UPDATE_TYPE_UPDATE: _ClassVar[StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType]
                UPDATE_TYPE_REMOVE: _ClassVar[StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType]
            UPDATE_TYPE_UNSPECIFIED: StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType
            UPDATE_TYPE_UPDATE: StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType
            UPDATE_TYPE_REMOVE: StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType
            SPACE_MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
            UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            space_monitoring_company: _space_monitoring_company_pb2.SpaceMonitoringCompany
            update_type: StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType
            def __init__(self, space_monitoring_company: _Optional[_Union[_space_monitoring_company_pb2.SpaceMonitoringCompany, _Mapping]] = ..., update_type: _Optional[_Union[StreamSpaceMonitoringCompanyResponse.Success.Update.UpdateType, str]] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamSpaceMonitoringCompanyResponse.Success.Snapshot
        update: StreamSpaceMonitoringCompanyResponse.Success.Update
        def __init__(self, snapshot: _Optional[_Union[StreamSpaceMonitoringCompanyResponse.Success.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamSpaceMonitoringCompanyResponse.Success.Update, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceMonitoringCompanyResponse.Success
    failure: StreamSpaceMonitoringCompanyResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamSpaceMonitoringCompanyResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamSpaceMonitoringCompanyResponse.Failure, _Mapping]] = ...) -> None: ...
