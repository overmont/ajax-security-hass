from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceRequest(_message.Message):
    __slots__ = ("name", "image_id", "device_qr_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    image_id: str
    device_qr_code: str
    def __init__(self, name: _Optional[str] = ..., image_id: _Optional[str] = ..., device_qr_code: _Optional[str] = ...) -> None: ...
