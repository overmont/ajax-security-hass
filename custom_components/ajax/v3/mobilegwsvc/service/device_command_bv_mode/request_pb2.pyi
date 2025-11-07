from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandBvModeRequest(_message.Message):
    __slots__ = ("hub_id", "alarm_verification_mode")
    class AlarmVerificationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_VERIFICATION_MODE_UNSPECIFIED: _ClassVar[DeviceCommandBvModeRequest.AlarmVerificationMode]
        ALARM_VERIFICATION_MODE_DISABLE: _ClassVar[DeviceCommandBvModeRequest.AlarmVerificationMode]
        ALARM_VERIFICATION_MODE_ENABLE: _ClassVar[DeviceCommandBvModeRequest.AlarmVerificationMode]
    ALARM_VERIFICATION_MODE_UNSPECIFIED: DeviceCommandBvModeRequest.AlarmVerificationMode
    ALARM_VERIFICATION_MODE_DISABLE: DeviceCommandBvModeRequest.AlarmVerificationMode
    ALARM_VERIFICATION_MODE_ENABLE: DeviceCommandBvModeRequest.AlarmVerificationMode
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    alarm_verification_mode: DeviceCommandBvModeRequest.AlarmVerificationMode
    def __init__(self, hub_id: _Optional[str] = ..., alarm_verification_mode: _Optional[_Union[DeviceCommandBvModeRequest.AlarmVerificationMode, str]] = ...) -> None: ...
