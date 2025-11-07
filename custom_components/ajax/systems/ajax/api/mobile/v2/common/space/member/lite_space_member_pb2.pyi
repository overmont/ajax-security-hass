from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.space.member import space_member_role_pb2 as _space_member_role_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpaceMember(_message.Message):
    __slots__ = ("id", "name", "email", "role", "images", "has_privacy_permission", "sorting_key", "hex_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_PRIVACY_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    role: _space_member_role_pb2.SpaceMemberRole
    images: _image_pb2.Images
    has_privacy_permission: bool
    sorting_key: str
    hex_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[_space_member_role_pb2.SpaceMemberRole, str]] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., has_privacy_permission: bool = ..., sorting_key: _Optional[str] = ..., hex_id: _Optional[str] = ...) -> None: ...
