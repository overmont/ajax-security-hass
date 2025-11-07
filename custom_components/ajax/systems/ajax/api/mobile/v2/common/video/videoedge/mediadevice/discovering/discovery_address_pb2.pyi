from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_pb2 as _media_device_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoveryAddress(_message.Message):
    __slots__ = ("host", "port", "protocol")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: str
    protocol: _media_device_pb2.MediaDeviceProtocol
    def __init__(self, host: _Optional[str] = ..., port: _Optional[str] = ..., protocol: _Optional[_Union[_media_device_pb2.MediaDeviceProtocol, str]] = ...) -> None: ...
