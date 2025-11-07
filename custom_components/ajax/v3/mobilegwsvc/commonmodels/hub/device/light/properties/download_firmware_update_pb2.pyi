from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadFirmwareUpdate(_message.Message):
    __slots__ = ("restrictions", "is_progress", "fw_version")
    class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTRICTION_UNSPECIFIED: _ClassVar[DownloadFirmwareUpdate.Restriction]
        RESTRICTION_ARMED: _ClassVar[DownloadFirmwareUpdate.Restriction]
        RESTRICTION_EN_54_ALARM: _ClassVar[DownloadFirmwareUpdate.Restriction]
        RESTRICTION_WALK_TEST_IN_PROGRESS: _ClassVar[DownloadFirmwareUpdate.Restriction]
    RESTRICTION_UNSPECIFIED: DownloadFirmwareUpdate.Restriction
    RESTRICTION_ARMED: DownloadFirmwareUpdate.Restriction
    RESTRICTION_EN_54_ALARM: DownloadFirmwareUpdate.Restriction
    RESTRICTION_WALK_TEST_IN_PROGRESS: DownloadFirmwareUpdate.Restriction
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    FW_VERSION_FIELD_NUMBER: _ClassVar[int]
    restrictions: _containers.RepeatedScalarFieldContainer[DownloadFirmwareUpdate.Restriction]
    is_progress: bool
    fw_version: str
    def __init__(self, restrictions: _Optional[_Iterable[_Union[DownloadFirmwareUpdate.Restriction, str]]] = ..., is_progress: bool = ..., fw_version: _Optional[str] = ...) -> None: ...
