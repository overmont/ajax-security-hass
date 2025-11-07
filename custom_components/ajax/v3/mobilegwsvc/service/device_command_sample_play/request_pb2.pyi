from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSamplePlayRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "object_type", "sample_play")
    class SamplePlay(_message.Message):
        __slots__ = ("audio_sample_index", "repeat_count")
        AUDIO_SAMPLE_INDEX_FIELD_NUMBER: _ClassVar[int]
        REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
        audio_sample_index: int
        repeat_count: int
        def __init__(self, audio_sample_index: _Optional[int] = ..., repeat_count: _Optional[int] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_PLAY_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    sample_play: DeviceCommandSamplePlayRequest.SamplePlay
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., sample_play: _Optional[_Union[DeviceCommandSamplePlayRequest.SamplePlay, _Mapping]] = ...) -> None: ...
