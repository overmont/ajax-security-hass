from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import enriched_target_info_pb2 as _enriched_target_info_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServicesWithPendingDeactivationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("target_services",)
        class TargetPendingDeactivationServices(_message.Message):
            __slots__ = ("target_info", "pending_deactivation_services")
            class PendingDeactivationService(_message.Message):
                __slots__ = ("deactivation_date", "service")
                DEACTIVATION_DATE_FIELD_NUMBER: _ClassVar[int]
                SERVICE_FIELD_NUMBER: _ClassVar[int]
                deactivation_date: _timestamp_pb2.Timestamp
                service: _service_pb2.Service
                def __init__(self, deactivation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ...) -> None: ...
            TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
            PENDING_DEACTIVATION_SERVICES_FIELD_NUMBER: _ClassVar[int]
            target_info: _enriched_target_info_pb2.EnrichedTargetInfo
            pending_deactivation_services: _containers.RepeatedCompositeFieldContainer[GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices.PendingDeactivationService]
            def __init__(self, target_info: _Optional[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]] = ..., pending_deactivation_services: _Optional[_Iterable[_Union[GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices.PendingDeactivationService, _Mapping]]] = ...) -> None: ...
        TARGET_SERVICES_FIELD_NUMBER: _ClassVar[int]
        target_services: _containers.RepeatedCompositeFieldContainer[GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices]
        def __init__(self, target_services: _Optional[_Iterable[_Union[GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("not_found",)
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        not_found: _response_pb2.Error
        def __init__(self, not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetServicesWithPendingDeactivationResponse.Success
    failure: GetServicesWithPendingDeactivationResponse.Failure
    def __init__(self, success: _Optional[_Union[GetServicesWithPendingDeactivationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetServicesWithPendingDeactivationResponse.Failure, _Mapping]] = ...) -> None: ...
