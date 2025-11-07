from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteAudioFileForAudioScenariosRequest(_message.Message):
    __slots__ = ("hub_id", "audio_sample_identifier")
    class AudioSampleIdentifier(_message.Message):
        __slots__ = ("slot_id", "file_id")
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        slot_id: int
        file_id: str
        def __init__(self, slot_id: _Optional[int] = ..., file_id: _Optional[str] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SAMPLE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    audio_sample_identifier: DeleteAudioFileForAudioScenariosRequest.AudioSampleIdentifier
    def __init__(self, hub_id: _Optional[str] = ..., audio_sample_identifier: _Optional[_Union[DeleteAudioFileForAudioScenariosRequest.AudioSampleIdentifier, _Mapping]] = ...) -> None: ...
