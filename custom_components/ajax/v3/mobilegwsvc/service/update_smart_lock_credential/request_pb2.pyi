from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockCredentialRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "credential")
    class SmartLockCredentialToUpdate(_message.Message):
        __slots__ = ("id", "name", "enabled", "code")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        enabled: bool
        code: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enabled: bool = ..., code: _Optional[str] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    credential: UpdateSmartLockCredentialRequest.SmartLockCredentialToUpdate
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., credential: _Optional[_Union[UpdateSmartLockCredentialRequest.SmartLockCredentialToUpdate, _Mapping]] = ...) -> None: ...
