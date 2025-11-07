from v3.mobilegwsvc.commonmodels.space.device import smart_lock_id_pb2 as _smart_lock_id_pb2
from v3.mobilegwsvc.commonmodels.space.device import video_channel_id_pb2 as _video_channel_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllMembersWithPermissionsForDeviceRequest(_message.Message):
    __slots__ = ("space_id", "smart_lock_id", "video_channel_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: _smart_lock_id_pb2.SmartLockId
    video_channel_id: _video_channel_id_pb2.VideoChannelId
    def __init__(self, space_id: _Optional[str] = ..., smart_lock_id: _Optional[_Union[_smart_lock_id_pb2.SmartLockId, _Mapping]] = ..., video_channel_id: _Optional[_Union[_video_channel_id_pb2.VideoChannelId, _Mapping]] = ...) -> None: ...
