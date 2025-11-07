from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import enriched_target_info_pb2 as _enriched_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAvailableTargetsForSubscriptionResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("max_target_count_to_assign", "selected_targets", "available_targets")
        MAX_TARGET_COUNT_TO_ASSIGN_FIELD_NUMBER: _ClassVar[int]
        SELECTED_TARGETS_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_TARGETS_FIELD_NUMBER: _ClassVar[int]
        max_target_count_to_assign: int
        selected_targets: _containers.RepeatedCompositeFieldContainer[_enriched_target_info_pb2.EnrichedTargetInfo]
        available_targets: _containers.RepeatedCompositeFieldContainer[_enriched_target_info_pb2.EnrichedTargetInfo]
        def __init__(self, max_target_count_to_assign: _Optional[int] = ..., selected_targets: _Optional[_Iterable[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]]] = ..., available_targets: _Optional[_Iterable[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("subscription_not_found",)
        SUBSCRIPTION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        subscription_not_found: _response_pb2.Error
        def __init__(self, subscription_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAvailableTargetsForSubscriptionResponse.Success
    failure: FindAvailableTargetsForSubscriptionResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAvailableTargetsForSubscriptionResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAvailableTargetsForSubscriptionResponse.Failure, _Mapping]] = ...) -> None: ...
