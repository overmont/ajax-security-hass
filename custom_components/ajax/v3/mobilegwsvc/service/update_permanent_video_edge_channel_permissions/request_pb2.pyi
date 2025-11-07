from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.privacy import channel_permission_policy_pb2 as _channel_permission_policy_pb2
from v3.mobilegwsvc.commonmodels.video.privacy import channel_permission_update_pb2 as _channel_permission_update_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePermanentVideoEdgeChannelPermissionsRequest(_message.Message):
    __slots__ = ("space_locator", "assignee_id", "video_edge_id", "channel_id", "updates", "policy")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    assignee_id: str
    video_edge_id: str
    channel_id: str
    updates: _containers.RepeatedCompositeFieldContainer[_channel_permission_update_pb2.ChannelPermissionUpdate]
    policy: _channel_permission_policy_pb2.ChannelPermissionPolicy
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., assignee_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., updates: _Optional[_Iterable[_Union[_channel_permission_update_pb2.ChannelPermissionUpdate, _Mapping]]] = ..., policy: _Optional[_Union[_channel_permission_policy_pb2.ChannelPermissionPolicy, _Mapping]] = ...) -> None: ...
