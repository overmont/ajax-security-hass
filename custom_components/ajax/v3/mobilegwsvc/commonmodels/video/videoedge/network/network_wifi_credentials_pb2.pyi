from google.protobuf import empty_pb2 as _empty_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkWifiCredentials(_message.Message):
    __slots__ = ("none", "psk")
    class PSK(_message.Message):
        __slots__ = ("password",)
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        password: str
        def __init__(self, password: _Optional[str] = ...) -> None: ...
    NONE_FIELD_NUMBER: _ClassVar[int]
    PSK_FIELD_NUMBER: _ClassVar[int]
    none: _empty_pb2.Empty
    psk: NetworkWifiCredentials.PSK
    def __init__(self, none: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., psk: _Optional[_Union[NetworkWifiCredentials.PSK, _Mapping]] = ...) -> None: ...
