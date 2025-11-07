from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaidServicesActivationRequired(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BlankEventTag(_message.Message):
    __slots__ = ("paid_services_activation_required",)
    PAID_SERVICES_ACTIVATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    paid_services_activation_required: PaidServicesActivationRequired
    def __init__(self, paid_services_activation_required: _Optional[_Union[PaidServicesActivationRequired, _Mapping]] = ...) -> None: ...
