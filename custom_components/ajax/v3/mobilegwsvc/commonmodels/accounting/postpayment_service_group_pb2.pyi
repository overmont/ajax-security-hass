from v3.mobilegwsvc.commonmodels.accounting import service_group_pb2 as _service_group_pb2
from v3.mobilegwsvc.commonmodels.accounting import available_extra_service_pb2 as _available_extra_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvailablePostPaymentServiceGroup(_message.Message):
    __slots__ = ("service_group", "item")
    class AvailableExtraServicesGroupItem(_message.Message):
        __slots__ = ("order", "service")
        ORDER_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        order: int
        service: _available_extra_service_pb2.AvailableExtraService
        def __init__(self, order: _Optional[int] = ..., service: _Optional[_Union[_available_extra_service_pb2.AvailableExtraService, _Mapping]] = ...) -> None: ...
    SERVICE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    service_group: _service_group_pb2.ServiceGroup
    item: _containers.RepeatedCompositeFieldContainer[AvailablePostPaymentServiceGroup.AvailableExtraServicesGroupItem]
    def __init__(self, service_group: _Optional[_Union[_service_group_pb2.ServiceGroup, _Mapping]] = ..., item: _Optional[_Iterable[_Union[AvailablePostPaymentServiceGroup.AvailableExtraServicesGroupItem, _Mapping]]] = ...) -> None: ...
