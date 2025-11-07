from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from systems.ajax.api.mobile.v2.common.accounting import category_pb2 as _category_pb2
from v3.mobilegwsvc.commonmodels.accounting import available_extra_service_pb2 as _available_extra_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableExtraServiceGroup(_message.Message):
    __slots__ = ("id", "name", "lokalise_id", "item", "order", "max_target_count_to_assign", "category", "feature_target")
    class AvailableExtraServicesGroupItem(_message.Message):
        __slots__ = ("order", "service")
        ORDER_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        order: int
        service: _available_extra_service_pb2.AvailableExtraService
        def __init__(self, order: _Optional[int] = ..., service: _Optional[_Union[_available_extra_service_pb2.AvailableExtraService, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_COUNT_TO_ASSIGN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    lokalise_id: str
    item: _containers.RepeatedCompositeFieldContainer[AvailableExtraServiceGroup.AvailableExtraServicesGroupItem]
    order: int
    max_target_count_to_assign: int
    category: _category_pb2.Category
    feature_target: _feature_target_pb2.FeatureTarget
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., lokalise_id: _Optional[str] = ..., item: _Optional[_Iterable[_Union[AvailableExtraServiceGroup.AvailableExtraServicesGroupItem, _Mapping]]] = ..., order: _Optional[int] = ..., max_target_count_to_assign: _Optional[int] = ..., category: _Optional[_Union[_category_pb2.Category, str]] = ..., feature_target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ...) -> None: ...
