from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JewellerCommunicationPart(_message.Message):
    __slots__ = ("communication_method",)
    class CommunicationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMUNICATION_METHOD_UNSPECIFIED: _ClassVar[JewellerCommunicationPart.CommunicationMethod]
        COMMUNICATION_METHOD_BUILT_IN: _ClassVar[JewellerCommunicationPart.CommunicationMethod]
        COMMUNICATION_METHOD_EXTERNAL: _ClassVar[JewellerCommunicationPart.CommunicationMethod]
        COMMUNICATION_METHOD_AUTO_SWITCH: _ClassVar[JewellerCommunicationPart.CommunicationMethod]
    COMMUNICATION_METHOD_UNSPECIFIED: JewellerCommunicationPart.CommunicationMethod
    COMMUNICATION_METHOD_BUILT_IN: JewellerCommunicationPart.CommunicationMethod
    COMMUNICATION_METHOD_EXTERNAL: JewellerCommunicationPart.CommunicationMethod
    COMMUNICATION_METHOD_AUTO_SWITCH: JewellerCommunicationPart.CommunicationMethod
    class JewellerCommunicationPartSettings(_message.Message):
        __slots__ = ("communication_method",)
        COMMUNICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
        communication_method: JewellerCommunicationPart.CommunicationMethod
        def __init__(self, communication_method: _Optional[_Union[JewellerCommunicationPart.CommunicationMethod, str]] = ...) -> None: ...
    COMMUNICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    communication_method: JewellerCommunicationPart.CommunicationMethod
    def __init__(self, communication_method: _Optional[_Union[JewellerCommunicationPart.CommunicationMethod, str]] = ...) -> None: ...
