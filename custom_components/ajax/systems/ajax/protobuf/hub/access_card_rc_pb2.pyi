from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCardRc(_message.Message):
    __slots__ = ("rc",)
    class Rc(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADDED: _ClassVar[AccessCardRc.Rc]
        ALREADY_ADDED: _ClassVar[AccessCardRc.Rc]
        CARD_FULL: _ClassVar[AccessCardRc.Rc]
        TIMEOUT: _ClassVar[AccessCardRc.Rc]
        INVALID_CARD: _ClassVar[AccessCardRc.Rc]
        USER_TIMEOUT: _ClassVar[AccessCardRc.Rc]
        NO_ANSWER: _ClassVar[AccessCardRc.Rc]
    ADDED: AccessCardRc.Rc
    ALREADY_ADDED: AccessCardRc.Rc
    CARD_FULL: AccessCardRc.Rc
    TIMEOUT: AccessCardRc.Rc
    INVALID_CARD: AccessCardRc.Rc
    USER_TIMEOUT: AccessCardRc.Rc
    NO_ANSWER: AccessCardRc.Rc
    RC_FIELD_NUMBER: _ClassVar[int]
    rc: AccessCardRc.Rc
    def __init__(self, rc: _Optional[_Union[AccessCardRc.Rc, str]] = ...) -> None: ...
