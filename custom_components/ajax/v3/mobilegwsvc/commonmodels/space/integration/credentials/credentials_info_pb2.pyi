from v3.mobilegwsvc.commonmodels.space.integration import space_integration_type_pb2 as _space_integration_type_pb2
from systems.ajax.api.mobile.v2.common.space import space_profile_pb2 as _space_profile_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialsInfo(_message.Message):
    __slots__ = ("id", "type", "created_at", "relations", "external_user")
    class Relation(_message.Message):
        __slots__ = ("standalone_device_relation", "space_relation")
        STANDALONE_DEVICE_RELATION_FIELD_NUMBER: _ClassVar[int]
        SPACE_RELATION_FIELD_NUMBER: _ClassVar[int]
        standalone_device_relation: CredentialsInfo.StandaloneDeviceRelation
        space_relation: CredentialsInfo.SpaceRelation
        def __init__(self, standalone_device_relation: _Optional[_Union[CredentialsInfo.StandaloneDeviceRelation, _Mapping]] = ..., space_relation: _Optional[_Union[CredentialsInfo.SpaceRelation, _Mapping]] = ...) -> None: ...
    class StandaloneDeviceRelation(_message.Message):
        __slots__ = ("space_id", "smart_lock_id", "device_name", "space_name", "room_id", "room_name")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        smart_lock_id: str
        device_name: str
        space_name: str
        room_id: str
        room_name: str
        def __init__(self, space_id: _Optional[str] = ..., smart_lock_id: _Optional[str] = ..., device_name: _Optional[str] = ..., space_name: _Optional[str] = ..., room_id: _Optional[str] = ..., room_name: _Optional[str] = ...) -> None: ...
    class SpaceRelation(_message.Message):
        __slots__ = ("space_id", "space_name", "profile")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        space_name: str
        profile: _space_profile_pb2.SpaceProfile
        def __init__(self, space_id: _Optional[str] = ..., space_name: _Optional[str] = ..., profile: _Optional[_Union[_space_profile_pb2.SpaceProfile, _Mapping]] = ...) -> None: ...
    class ExternalUser(_message.Message):
        __slots__ = ("id", "email", "image_url")
        ID_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        id: str
        email: str
        image_url: str
        def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _space_integration_type_pb2.SpaceIntegrationType
    created_at: _timestamp_pb2.Timestamp
    relations: _containers.RepeatedCompositeFieldContainer[CredentialsInfo.Relation]
    external_user: CredentialsInfo.ExternalUser
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_space_integration_type_pb2.SpaceIntegrationType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., relations: _Optional[_Iterable[_Union[CredentialsInfo.Relation, _Mapping]]] = ..., external_user: _Optional[_Union[CredentialsInfo.ExternalUser, _Mapping]] = ...) -> None: ...
