from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import extra_service_pb2 as _extra_service_pb2
from v3.mobilegwsvc.commonmodels.accounting import extra_service_state_pb2 as _extra_service_state_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_activation_availability_status_pb2 as _service_activation_availability_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamExtraServicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update", "stream_update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        STREAM_UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamExtraServicesResponse.ExtraServices
        update: StreamExtraServicesResponse.Update
        stream_update: StreamExtraServicesResponse.StreamUpdate
        def __init__(self, snapshot: _Optional[_Union[StreamExtraServicesResponse.ExtraServices, _Mapping]] = ..., update: _Optional[_Union[StreamExtraServicesResponse.Update, _Mapping]] = ..., stream_update: _Optional[_Union[StreamExtraServicesResponse.StreamUpdate, _Mapping]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("extra_service_id", "subscription_id", "extra_service_added", "extra_service_state_updated", "extra_service_removed", "extra_service_reactivated", "extra_service_replaced")
        EXTRA_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_STATE_UPDATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REACTIVATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REPLACED_FIELD_NUMBER: _ClassVar[int]
        extra_service_id: str
        subscription_id: str
        extra_service_added: StreamExtraServicesResponse.ExtraServiceAdded
        extra_service_state_updated: StreamExtraServicesResponse.ExtraServiceStateUpdated
        extra_service_removed: StreamExtraServicesResponse.ExtraServiceRemoved
        extra_service_reactivated: StreamExtraServicesResponse.ExtraServiceReactivated
        extra_service_replaced: StreamExtraServicesResponse.ExtraServiceReplaced
        def __init__(self, extra_service_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., extra_service_added: _Optional[_Union[StreamExtraServicesResponse.ExtraServiceAdded, _Mapping]] = ..., extra_service_state_updated: _Optional[_Union[StreamExtraServicesResponse.ExtraServiceStateUpdated, _Mapping]] = ..., extra_service_removed: _Optional[_Union[StreamExtraServicesResponse.ExtraServiceRemoved, _Mapping]] = ..., extra_service_reactivated: _Optional[_Union[StreamExtraServicesResponse.ExtraServiceReactivated, _Mapping]] = ..., extra_service_replaced: _Optional[_Union[StreamExtraServicesResponse.ExtraServiceReplaced, _Mapping]] = ...) -> None: ...
    class ExtraServiceAdded(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(self, new_extra_service: _Optional[_Union[_extra_service_pb2.ExtraService, _Mapping]] = ...) -> None: ...
    class ExtraServiceStateUpdated(_message.Message):
        __slots__ = ("new_state", "extra_service")
        NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_state: _extra_service_state_pb2.ExtraServiceState
        extra_service: _extra_service_pb2.ExtraService
        def __init__(self, new_state: _Optional[_Union[_extra_service_state_pb2.ExtraServiceState, _Mapping]] = ..., extra_service: _Optional[_Union[_extra_service_pb2.ExtraService, _Mapping]] = ...) -> None: ...
    class ExtraServiceRemoved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ExtraServiceReactivated(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(self, new_extra_service: _Optional[_Union[_extra_service_pb2.ExtraService, _Mapping]] = ...) -> None: ...
    class ExtraServiceReplaced(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(self, new_extra_service: _Optional[_Union[_extra_service_pb2.ExtraService, _Mapping]] = ...) -> None: ...
    class ExtraServices(_message.Message):
        __slots__ = ("extra_services", "service_activation_availability_status")
        EXTRA_SERVICES_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        extra_services: _containers.RepeatedCompositeFieldContainer[_extra_service_pb2.ExtraService]
        service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
        def __init__(self, extra_services: _Optional[_Iterable[_Union[_extra_service_pb2.ExtraService, _Mapping]]] = ..., service_activation_availability_status: _Optional[_Union[_service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus, str]] = ...) -> None: ...
    class StreamUpdate(_message.Message):
        __slots__ = ("service_activation_availability_status_changed",)
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_CHANGED_FIELD_NUMBER: _ClassVar[int]
        service_activation_availability_status_changed: StreamExtraServicesResponse.ServiceActivationAvailabilityStatusChanged
        def __init__(self, service_activation_availability_status_changed: _Optional[_Union[StreamExtraServicesResponse.ServiceActivationAvailabilityStatusChanged, _Mapping]] = ...) -> None: ...
    class ServiceActivationAvailabilityStatusChanged(_message.Message):
        __slots__ = ("service_activation_availability_status",)
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
        def __init__(self, service_activation_availability_status: _Optional[_Union[_service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus, str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "request_timeout", "illegal_argument", "extra_services_not_available")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICES_NOT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        extra_services_not_available: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., extra_services_not_available: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamExtraServicesResponse.Success
    failure: StreamExtraServicesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamExtraServicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamExtraServicesResponse.Failure, _Mapping]] = ...) -> None: ...
