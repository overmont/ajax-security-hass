from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from v3.mobilegwsvc.commonmodels.hub.device import motion_cam_video_base_pb2 as _motion_cam_video_base_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeChimeSettingsRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "chime")
    class Chime(_message.Message):
        __slots__ = ("off", "mechanical", "digital", "siren")
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MechanicalMode(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: _duration_pb2.Duration
            def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class DigitalMode(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: _duration_pb2.Duration
            def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class SirenMode(_message.Message):
            __slots__ = ("chime_triggers", "chime_signal")
            CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
            CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
            chime_triggers: _containers.RepeatedScalarFieldContainer[_motion_cam_video_base_pb2.MotionCamVideoBase.ChimeTrigger]
            chime_signal: int
            def __init__(self, chime_triggers: _Optional[_Iterable[_Union[_motion_cam_video_base_pb2.MotionCamVideoBase.ChimeTrigger, str]]] = ..., chime_signal: _Optional[int] = ...) -> None: ...
        OFF_FIELD_NUMBER: _ClassVar[int]
        MECHANICAL_FIELD_NUMBER: _ClassVar[int]
        DIGITAL_FIELD_NUMBER: _ClassVar[int]
        SIREN_FIELD_NUMBER: _ClassVar[int]
        off: SetVideoEdgeChimeSettingsRequest.Chime.OffMode
        mechanical: SetVideoEdgeChimeSettingsRequest.Chime.MechanicalMode
        digital: SetVideoEdgeChimeSettingsRequest.Chime.DigitalMode
        siren: SetVideoEdgeChimeSettingsRequest.Chime.SirenMode
        def __init__(self, off: _Optional[_Union[SetVideoEdgeChimeSettingsRequest.Chime.OffMode, _Mapping]] = ..., mechanical: _Optional[_Union[SetVideoEdgeChimeSettingsRequest.Chime.MechanicalMode, _Mapping]] = ..., digital: _Optional[_Union[SetVideoEdgeChimeSettingsRequest.Chime.DigitalMode, _Mapping]] = ..., siren: _Optional[_Union[SetVideoEdgeChimeSettingsRequest.Chime.SirenMode, _Mapping]] = ...) -> None: ...
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    chime: SetVideoEdgeChimeSettingsRequest.Chime
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., chime: _Optional[_Union[SetVideoEdgeChimeSettingsRequest.Chime, _Mapping]] = ...) -> None: ...
