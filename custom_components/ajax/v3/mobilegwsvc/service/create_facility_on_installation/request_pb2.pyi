from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFacilityOnInstallationRequest(_message.Message):
    __slots__ = ("facility_name", "registration_number", "device_qr_code")
    FACILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    facility_name: str
    registration_number: str
    device_qr_code: str
    def __init__(self, facility_name: _Optional[str] = ..., registration_number: _Optional[str] = ..., device_qr_code: _Optional[str] = ...) -> None: ...
