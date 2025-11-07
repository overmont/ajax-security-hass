from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacyStreamingCamAccess(_message.Message):
    __slots__ = ("user_id", "device_id", "access_type")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISABLED: _ClassVar[PrivacyStreamingCamAccess.AccessType]
        ALWAYS: _ClassVar[PrivacyStreamingCamAccess.AccessType]
    DISABLED: PrivacyStreamingCamAccess.AccessType
    ALWAYS: PrivacyStreamingCamAccess.AccessType
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    device_id: str
    access_type: PrivacyStreamingCamAccess.AccessType
    def __init__(self, user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., access_type: _Optional[_Union[PrivacyStreamingCamAccess.AccessType, str]] = ...) -> None: ...
