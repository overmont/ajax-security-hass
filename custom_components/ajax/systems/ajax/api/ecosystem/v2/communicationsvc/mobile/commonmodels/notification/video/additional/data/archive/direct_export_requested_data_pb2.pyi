from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DirectExportRequestedData(_message.Message):
    __slots__ = ("initiator_member_id", "initiator_name", "channel_id", "channel_name", "export_ranges", "timezone_id")
    INITIATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    initiator_member_id: str
    initiator_name: str
    channel_id: str
    channel_name: str
    export_ranges: _containers.RepeatedCompositeFieldContainer[_types_pb2.TimestampRange]
    timezone_id: str
    def __init__(self, initiator_member_id: _Optional[str] = ..., initiator_name: _Optional[str] = ..., channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., export_ranges: _Optional[_Iterable[_Union[_types_pb2.TimestampRange, _Mapping]]] = ..., timezone_id: _Optional[str] = ...) -> None: ...
