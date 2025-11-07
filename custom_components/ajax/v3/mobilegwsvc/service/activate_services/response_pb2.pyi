from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import enriched_target_info_pb2 as _enriched_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateServicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("subscription_id",)
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        subscription_id: str
        def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "service_not_found", "reseller_not_found", "dealer_not_found", "linkage_not_active", "linkage_suspended", "target_suspended", "no_price_in_currency", "illegal_state", "already_active_on_targets")
        class AlreadyActiveOnTargetsError(_message.Message):
            __slots__ = ("feature_target_infos",)
            FEATURE_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
            feature_target_infos: _containers.RepeatedCompositeFieldContainer[_enriched_target_info_pb2.EnrichedTargetInfo]
            def __init__(self, feature_target_infos: _Optional[_Iterable[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        LINKAGE_NOT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        LINKAGE_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        TARGET_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        NO_PRICE_IN_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ACTIVE_ON_TARGETS_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        linkage_not_active: _response_pb2.Error
        linkage_suspended: _response_pb2.Error
        target_suspended: _response_pb2.Error
        no_price_in_currency: _response_pb2.Error
        illegal_state: _response_pb2.Error
        already_active_on_targets: ActivateServicesResponse.Failure.AlreadyActiveOnTargetsError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., reseller_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., linkage_not_active: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., linkage_suspended: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., target_suspended: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., no_price_in_currency: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_state: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., already_active_on_targets: _Optional[_Union[ActivateServicesResponse.Failure.AlreadyActiveOnTargetsError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ActivateServicesResponse.Success
    failure: ActivateServicesResponse.Failure
    def __init__(self, success: _Optional[_Union[ActivateServicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ActivateServicesResponse.Failure, _Mapping]] = ...) -> None: ...
