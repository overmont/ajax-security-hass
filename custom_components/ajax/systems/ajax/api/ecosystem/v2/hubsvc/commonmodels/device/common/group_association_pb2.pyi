from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupAssociation(_message.Message):
    __slots__ = ("group_associated", "capabilities")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[GroupAssociation.Capability]
        CAPABILITY_GROUP_ASSOCIATED: _ClassVar[GroupAssociation.Capability]
    CAPABILITY_UNSPECIFIED: GroupAssociation.Capability
    CAPABILITY_GROUP_ASSOCIATED: GroupAssociation.Capability
    class GroupsAssociated(_message.Message):
        __slots__ = ("group_associated", "all")
        class All(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        group_associated: str
        all: GroupAssociation.GroupsAssociated.All
        def __init__(self, group_associated: _Optional[str] = ..., all: _Optional[_Union[GroupAssociation.GroupsAssociated.All, _Mapping]] = ...) -> None: ...
    class GroupAssociationSettings(_message.Message):
        __slots__ = ("group_associated",)
        GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
        group_associated: GroupAssociation.GroupsAssociated
        def __init__(self, group_associated: _Optional[_Union[GroupAssociation.GroupsAssociated, _Mapping]] = ...) -> None: ...
    GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    group_associated: GroupAssociation.GroupsAssociated
    capabilities: _containers.RepeatedScalarFieldContainer[GroupAssociation.Capability]
    def __init__(self, group_associated: _Optional[_Union[GroupAssociation.GroupsAssociated, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[GroupAssociation.Capability, str]]] = ...) -> None: ...
