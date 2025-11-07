from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDeviceAboutRequest(_message.Message):
    __slots__ = ("qr_code",)
    QR_CODE_FIELD_NUMBER: _ClassVar[int]
    qr_code: str
    def __init__(self, qr_code: _Optional[str] = ...) -> None: ...

class GetDeviceAboutResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("hub", "video_edge", "hub_device")
        HUB_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        hub: GetDeviceAboutResponse.Hub
        video_edge: GetDeviceAboutResponse.VideoEdge
        hub_device: GetDeviceAboutResponse.HubDevice
        def __init__(self, hub: _Optional[_Union[GetDeviceAboutResponse.Hub, _Mapping]] = ..., video_edge: _Optional[_Union[GetDeviceAboutResponse.VideoEdge, _Mapping]] = ..., hub_device: _Optional[_Union[GetDeviceAboutResponse.HubDevice, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "device_not_found", "device_is_already_installed")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_IS_ALREADY_INSTALLED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        device_is_already_installed: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_is_already_installed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    class Hub(_message.Message):
        __slots__ = ("object_type",)
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        object_type: _object_type_pb2.ObjectType
        def __init__(self, object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    class VideoEdge(_message.Message):
        __slots__ = ("about",)
        ABOUT_FIELD_NUMBER: _ClassVar[int]
        about: _about_pb2.About
        def __init__(self, about: _Optional[_Union[_about_pb2.About, _Mapping]] = ...) -> None: ...
    class HubDevice(_message.Message):
        __slots__ = ("object_type",)
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        object_type: _object_type_pb2.ObjectType
        def __init__(self, object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetDeviceAboutResponse.Success
    failure: GetDeviceAboutResponse.Failure
    def __init__(self, success: _Optional[_Union[GetDeviceAboutResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetDeviceAboutResponse.Failure, _Mapping]] = ...) -> None: ...
