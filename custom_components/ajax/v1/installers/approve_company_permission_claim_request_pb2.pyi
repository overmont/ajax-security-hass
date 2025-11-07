from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveCompanyPermissionsClaimRequest(_message.Message):
    __slots__ = ("claim_id",)
    CLAIM_ID_FIELD_NUMBER: _ClassVar[int]
    claim_id: str
    def __init__(self, claim_id: _Optional[str] = ...) -> None: ...
