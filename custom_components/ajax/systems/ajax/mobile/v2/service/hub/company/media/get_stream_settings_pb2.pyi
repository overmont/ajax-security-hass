from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.hub import surveillance_camera_stream_settings_pb2 as _surveillance_camera_stream_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStreamSettingsRequest(_message.Message):
    __slots__ = ("hub_hex_id", "camera_hex_id", "service_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    camera_hex_id: str
    service_id: str
    def __init__(self, hub_hex_id: _Optional[str] = ..., camera_hex_id: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...

class GetStreamSettingsResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("stream_settings",)
        STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        stream_settings: _surveillance_camera_stream_settings_pb2.SurveillanceCameraStreamSettings
        def __init__(self, stream_settings: _Optional[_Union[_surveillance_camera_stream_settings_pb2.SurveillanceCameraStreamSettings, _Mapping]] = ...) -> None: ...
    class Error(_message.Message):
        __slots__ = ("internal_error",)
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.InternalError
        def __init__(self, internal_error: _Optional[_Union[_response_pb2.InternalError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetStreamSettingsResponse.Success
    error: GetStreamSettingsResponse.Error
    def __init__(self, success: _Optional[_Union[GetStreamSettingsResponse.Success, _Mapping]] = ..., error: _Optional[_Union[GetStreamSettingsResponse.Error, _Mapping]] = ...) -> None: ...
