from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmVerification(_message.Message):
    __slots__ = ("verification",)
    class Verification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERIFICATION_UNSPECIFIED: _ClassVar[AlarmVerification.Verification]
        VERIFICATION_DISABLED: _ClassVar[AlarmVerification.Verification]
        VERIFICATION_ENABLED: _ClassVar[AlarmVerification.Verification]
    VERIFICATION_UNSPECIFIED: AlarmVerification.Verification
    VERIFICATION_DISABLED: AlarmVerification.Verification
    VERIFICATION_ENABLED: AlarmVerification.Verification
    class AlarmVerificationSettings(_message.Message):
        __slots__ = ("verification",)
        VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        verification: AlarmVerification.Verification
        def __init__(self, verification: _Optional[_Union[AlarmVerification.Verification, str]] = ...) -> None: ...
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    verification: AlarmVerification.Verification
    def __init__(self, verification: _Optional[_Union[AlarmVerification.Verification, str]] = ...) -> None: ...
