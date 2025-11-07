from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from v3.mobilegwsvc.commonmodels.resource.audio import audio_format_pb2 as _audio_format_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAudioFilesForAudioScenariosResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("audio_files",)
        AUDIO_FILES_FIELD_NUMBER: _ClassVar[int]
        audio_files: _containers.RepeatedCompositeFieldContainer[FindAudioFilesForAudioScenariosResponse.AudioFile]
        def __init__(self, audio_files: _Optional[_Iterable[_Union[FindAudioFilesForAudioScenariosResponse.AudioFile, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("file_not_found",)
        FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        file_not_found: _response_pb2.Error
        def __init__(self, file_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    class AudioFile(_message.Message):
        __slots__ = ("file_id", "slot_id", "sample_id", "file_name", "audio_file_variant", "expiration_time")
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FILE_VARIANT_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
        file_id: str
        slot_id: int
        sample_id: int
        file_name: str
        audio_file_variant: FindAudioFilesForAudioScenariosResponse.AudioFileVariant
        expiration_time: _timestamp_pb2.Timestamp
        def __init__(self, file_id: _Optional[str] = ..., slot_id: _Optional[int] = ..., sample_id: _Optional[int] = ..., file_name: _Optional[str] = ..., audio_file_variant: _Optional[_Union[FindAudioFilesForAudioScenariosResponse.AudioFileVariant, _Mapping]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class AudioFileVariant(_message.Message):
        __slots__ = ("audio_format", "url", "duration")
        AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        audio_format: _audio_format_pb2.AudioFormat
        url: str
        duration: _duration_pb2.Duration
        def __init__(self, audio_format: _Optional[_Union[_audio_format_pb2.AudioFormat, str]] = ..., url: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAudioFilesForAudioScenariosResponse.Success
    failure: FindAudioFilesForAudioScenariosResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAudioFilesForAudioScenariosResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAudioFilesForAudioScenariosResponse.Failure, _Mapping]] = ...) -> None: ...
