from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RejectRequestForTemporaryVideoEdgeChannelPermissionsRequest(_message.Message):
    __slots__ = ("space_locator", "request_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    request_id: str
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...
