from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class X509Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    X509_VERSION_UNSPECIFIED: _ClassVar[X509Version]
    X509_VERSION_1: _ClassVar[X509Version]
    X509_VERSION_2: _ClassVar[X509Version]
    X509_VERSION_3: _ClassVar[X509Version]
X509_VERSION_UNSPECIFIED: X509Version
X509_VERSION_1: X509Version
X509_VERSION_2: X509Version
X509_VERSION_3: X509Version

class X509Certificate(_message.Message):
    __slots__ = ("id", "alias", "sha256_fingerprint", "used")
    ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    SHA256_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    id: str
    alias: str
    sha256_fingerprint: str
    used: bool
    def __init__(self, id: _Optional[str] = ..., alias: _Optional[str] = ..., sha256_fingerprint: _Optional[str] = ..., used: bool = ...) -> None: ...
