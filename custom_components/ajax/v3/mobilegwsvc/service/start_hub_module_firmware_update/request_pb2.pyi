from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartHubModuleFirmwareUpdateRequest(_message.Message):
    __slots__ = ("hub_id", "hub_module")
    class HubModule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HUB_MODULE_UNSPECIFIED: _ClassVar[StartHubModuleFirmwareUpdateRequest.HubModule]
        HUB_MODULE_WIFI: _ClassVar[StartHubModuleFirmwareUpdateRequest.HubModule]
    HUB_MODULE_UNSPECIFIED: StartHubModuleFirmwareUpdateRequest.HubModule
    HUB_MODULE_WIFI: StartHubModuleFirmwareUpdateRequest.HubModule
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_MODULE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    hub_module: StartHubModuleFirmwareUpdateRequest.HubModule
    def __init__(self, hub_id: _Optional[str] = ..., hub_module: _Optional[_Union[StartHubModuleFirmwareUpdateRequest.HubModule, str]] = ...) -> None: ...
