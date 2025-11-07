from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_FORMAT_UNSPECIFIED: _ClassVar[AudioFormat]
    AUDIO_FORMAT_MP3: _ClassVar[AudioFormat]
    AUDIO_FORMAT_OGG: _ClassVar[AudioFormat]
    AUDIO_FORMAT_WAV: _ClassVar[AudioFormat]
    AUDIO_FORMAT_AAC: _ClassVar[AudioFormat]
    AUDIO_FORMAT_OGG_IN_UDF: _ClassVar[AudioFormat]
AUDIO_FORMAT_UNSPECIFIED: AudioFormat
AUDIO_FORMAT_MP3: AudioFormat
AUDIO_FORMAT_OGG: AudioFormat
AUDIO_FORMAT_WAV: AudioFormat
AUDIO_FORMAT_AAC: AudioFormat
AUDIO_FORMAT_OGG_IN_UDF: AudioFormat
