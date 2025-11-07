from v1.common import permission_pb2 as _permission_pb2
from v1.common import restore_permission_pb2 as _restore_permission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessRights(_message.Message):
    __slots__ = ("expiration_seconds", "access_type", "permissions")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPIRED: _ClassVar[AccessRights.AccessType]
        PERMANENT: _ClassVar[AccessRights.AccessType]
        VALID: _ClassVar[AccessRights.AccessType]
    EXPIRED: AccessRights.AccessType
    PERMANENT: AccessRights.AccessType
    VALID: AccessRights.AccessType
    EXPIRATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    expiration_seconds: int
    access_type: AccessRights.AccessType
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    def __init__(self, expiration_seconds: _Optional[int] = ..., access_type: _Optional[_Union[AccessRights.AccessType, str]] = ..., permissions: _Optional[_Iterable[_Union[_permission_pb2.Permission, str]]] = ...) -> None: ...
