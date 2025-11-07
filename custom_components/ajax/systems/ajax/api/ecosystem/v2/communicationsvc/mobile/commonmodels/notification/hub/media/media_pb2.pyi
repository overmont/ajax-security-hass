from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import image_status_pb2 as _image_status_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import resource_status_pb2 as _resource_status_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubNotificationMedia(_message.Message):
    __slots__ = ("expirationTime", "images", "audio")
    class Image(_message.Message):
        __slots__ = ("status", "file_name", "url")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        status: _image_status_pb2.ImageStatus
        file_name: str
        url: str
        def __init__(self, status: _Optional[_Union[_image_status_pb2.ImageStatus, str]] = ..., file_name: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Audio(_message.Message):
        __slots__ = ("status", "file_name", "url")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        status: _resource_status_pb2.ResourceStatus
        file_name: str
        url: str
        def __init__(self, status: _Optional[_Union[_resource_status_pb2.ResourceStatus, str]] = ..., file_name: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    expirationTime: _timestamp_pb2.Timestamp
    images: _containers.RepeatedCompositeFieldContainer[HubNotificationMedia.Image]
    audio: _containers.RepeatedCompositeFieldContainer[HubNotificationMedia.Audio]
    def __init__(self, expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., images: _Optional[_Iterable[_Union[HubNotificationMedia.Image, _Mapping]]] = ..., audio: _Optional[_Iterable[_Union[HubNotificationMedia.Audio, _Mapping]]] = ...) -> None: ...
