from v1.hub.privacy import privacy_motion_cam_access_pb2 as _privacy_motion_cam_access_pb2
from v1.hub.privacy import privacy_streaming_cam_access_pb2 as _privacy_streaming_cam_access_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacyAccessListStreamResponse(_message.Message):
    __slots__ = ("motion_cam_privacy_access", "streaming_cam_privacy_access")
    MOTION_CAM_PRIVACY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    STREAMING_CAM_PRIVACY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    motion_cam_privacy_access: _containers.RepeatedCompositeFieldContainer[_privacy_motion_cam_access_pb2.PrivacyMotionCamAccess]
    streaming_cam_privacy_access: _containers.RepeatedCompositeFieldContainer[_privacy_streaming_cam_access_pb2.PrivacyStreamingCamAccess]
    def __init__(self, motion_cam_privacy_access: _Optional[_Iterable[_Union[_privacy_motion_cam_access_pb2.PrivacyMotionCamAccess, _Mapping]]] = ..., streaming_cam_privacy_access: _Optional[_Iterable[_Union[_privacy_streaming_cam_access_pb2.PrivacyStreamingCamAccess, _Mapping]]] = ...) -> None: ...
