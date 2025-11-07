from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddSmartLockCredentialRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "credential")
    class SmartLockCredentialToAdd(_message.Message):
        __slots__ = ("name", "entry_code", "contactless_key")
        class EntryCode(_message.Message):
            __slots__ = ("code",)
            CODE_FIELD_NUMBER: _ClassVar[int]
            code: str
            def __init__(self, code: _Optional[str] = ...) -> None: ...
        class ContactlessKey(_message.Message):
            __slots__ = ("code",)
            CODE_FIELD_NUMBER: _ClassVar[int]
            code: str
            def __init__(self, code: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        ENTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        CONTACTLESS_KEY_FIELD_NUMBER: _ClassVar[int]
        name: str
        entry_code: AddSmartLockCredentialRequest.SmartLockCredentialToAdd.EntryCode
        contactless_key: AddSmartLockCredentialRequest.SmartLockCredentialToAdd.ContactlessKey
        def __init__(self, name: _Optional[str] = ..., entry_code: _Optional[_Union[AddSmartLockCredentialRequest.SmartLockCredentialToAdd.EntryCode, _Mapping]] = ..., contactless_key: _Optional[_Union[AddSmartLockCredentialRequest.SmartLockCredentialToAdd.ContactlessKey, _Mapping]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    credential: AddSmartLockCredentialRequest.SmartLockCredentialToAdd
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., credential: _Optional[_Union[AddSmartLockCredentialRequest.SmartLockCredentialToAdd, _Mapping]] = ...) -> None: ...
