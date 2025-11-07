from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import service_icon_pb2 as _service_icon_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionInfo(_message.Message):
    __slots__ = ("service_icon", "service_name_res_id")
    SERVICE_ICON_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_RES_ID_FIELD_NUMBER: _ClassVar[int]
    service_icon: _service_icon_pb2.ServiceIcon
    service_name_res_id: str
    def __init__(self, service_icon: _Optional[_Union[_service_icon_pb2.ServiceIcon, str]] = ..., service_name_res_id: _Optional[str] = ...) -> None: ...
