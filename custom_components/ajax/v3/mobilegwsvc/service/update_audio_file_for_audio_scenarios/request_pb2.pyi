from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAudioFileForAudioScenariosRequest(_message.Message):
    __slots__ = ("file_id", "update", "hub_id")
    class Update(_message.Message):
        __slots__ = ("file_name",)
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        def __init__(self, file_name: _Optional[str] = ...) -> None: ...
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    update: UpdateAudioFileForAudioScenariosRequest.Update
    hub_id: str
    def __init__(self, file_id: _Optional[str] = ..., update: _Optional[_Union[UpdateAudioFileForAudioScenariosRequest.Update, _Mapping]] = ..., hub_id: _Optional[str] = ...) -> None: ...
