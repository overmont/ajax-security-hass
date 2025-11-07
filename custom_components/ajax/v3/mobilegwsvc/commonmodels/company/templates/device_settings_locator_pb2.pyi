from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceSettingsLocator(_message.Message):
    __slots__ = ("template_id", "preset_id")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PRESET_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    preset_id: str
    def __init__(self, template_id: _Optional[str] = ..., preset_id: _Optional[str] = ...) -> None: ...
