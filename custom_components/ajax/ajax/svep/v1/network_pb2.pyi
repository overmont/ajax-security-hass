from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = ("ethernet", "wifi", "is_online")
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    ethernet: NetworkTechnology
    wifi: NetworkTechnology
    is_online: bool
    def __init__(self, ethernet: _Optional[_Union[NetworkTechnology, _Mapping]] = ..., wifi: _Optional[_Union[NetworkTechnology, _Mapping]] = ..., is_online: bool = ...) -> None: ...

class NetworkTechnology(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...
