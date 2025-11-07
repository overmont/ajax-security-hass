from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import event_settings_pb2 as _event_settings_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import app_settings_pb2 as _app_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeSpaceSettings(_message.Message):
    __slots__ = ("room_id", "event_settings", "app_settings")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    event_settings: _event_settings_pb2.EventSettings
    app_settings: _app_settings_pb2.AppSettings
    def __init__(self, room_id: _Optional[str] = ..., event_settings: _Optional[_Union[_event_settings_pb2.EventSettings, _Mapping]] = ..., app_settings: _Optional[_Union[_app_settings_pb2.AppSettings, _Mapping]] = ...) -> None: ...
