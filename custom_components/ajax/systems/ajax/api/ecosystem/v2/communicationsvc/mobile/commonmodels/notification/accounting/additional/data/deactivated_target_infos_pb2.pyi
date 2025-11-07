from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import target_info_pb2 as _target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeactivatedTargetInfos(_message.Message):
    __slots__ = ("target_infos",)
    TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    target_infos: _containers.RepeatedCompositeFieldContainer[_target_info_pb2.TargetInfo]
    def __init__(self, target_infos: _Optional[_Iterable[_Union[_target_info_pb2.TargetInfo, _Mapping]]] = ...) -> None: ...
