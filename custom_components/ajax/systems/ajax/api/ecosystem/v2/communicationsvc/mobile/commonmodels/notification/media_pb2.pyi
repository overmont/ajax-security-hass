from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import media_pb2 as _media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media.video import hub_video_scenario_media_pb2 as _hub_video_scenario_media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media.video import video_archive_export_completed_media_pb2 as _video_archive_export_completed_media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.media.archive import archive_export_completed_media_pb2 as _archive_export_completed_media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.media.channel import video_frames_media_pb2 as _video_frames_media_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.media.scenario import video_scenario_media_pb2 as _video_scenario_media_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationMedia(_message.Message):
    __slots__ = ("notification_id", "hub_notification_media", "archive_export_media", "video_scenario_media", "video_archive_export_completed_media", "hub_video_scenario_media", "video_frames_media")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_NOTIFICATION_MEDIA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_EXPORT_MEDIA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_MEDIA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_EXPORT_COMPLETED_MEDIA_FIELD_NUMBER: _ClassVar[int]
    HUB_VIDEO_SCENARIO_MEDIA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FRAMES_MEDIA_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    hub_notification_media: _media_pb2.HubNotificationMedia
    archive_export_media: _archive_export_completed_media_pb2.ArchiveExportCompletedMedia
    video_scenario_media: _video_scenario_media_pb2.VideoScenarioMedia
    video_archive_export_completed_media: _video_archive_export_completed_media_pb2.VideoArchiveExportCompletedMedia
    hub_video_scenario_media: _hub_video_scenario_media_pb2.HubVideoScenarioMedia
    video_frames_media: _video_frames_media_pb2.VideoFramesMedia
    def __init__(self, notification_id: _Optional[str] = ..., hub_notification_media: _Optional[_Union[_media_pb2.HubNotificationMedia, _Mapping]] = ..., archive_export_media: _Optional[_Union[_archive_export_completed_media_pb2.ArchiveExportCompletedMedia, _Mapping]] = ..., video_scenario_media: _Optional[_Union[_video_scenario_media_pb2.VideoScenarioMedia, _Mapping]] = ..., video_archive_export_completed_media: _Optional[_Union[_video_archive_export_completed_media_pb2.VideoArchiveExportCompletedMedia, _Mapping]] = ..., hub_video_scenario_media: _Optional[_Union[_hub_video_scenario_media_pb2.HubVideoScenarioMedia, _Mapping]] = ..., video_frames_media: _Optional[_Union[_video_frames_media_pb2.VideoFramesMedia, _Mapping]] = ...) -> None: ...
