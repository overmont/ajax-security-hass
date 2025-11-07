from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.source.info import hub_info_pb2 as _hub_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.source.info import video_edge_info_pb2 as _video_edge_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.source.info import subscription_info_pb2 as _subscription_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingNotificationSourceInfo(_message.Message):
    __slots__ = ("hub_info", "video_edge_info", "subscription_info")
    HUB_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    hub_info: _hub_info_pb2.HubInfo
    video_edge_info: _video_edge_info_pb2.VideoEdgeInfo
    subscription_info: _subscription_info_pb2.SubscriptionInfo
    def __init__(self, hub_info: _Optional[_Union[_hub_info_pb2.HubInfo, _Mapping]] = ..., video_edge_info: _Optional[_Union[_video_edge_info_pb2.VideoEdgeInfo, _Mapping]] = ..., subscription_info: _Optional[_Union[_subscription_info_pb2.SubscriptionInfo, _Mapping]] = ...) -> None: ...
