from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandChimesModeRequest(_message.Message):
    __slots__ = ("hub_id", "chimes_status", "groups_statuses")
    class ChimesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHIMES_STATUS_UNSPECIFIED: _ClassVar[DeviceCommandChimesModeRequest.ChimesStatus]
        CHIMES_STATUS_DISABLE: _ClassVar[DeviceCommandChimesModeRequest.ChimesStatus]
        CHIMES_STATUS_ENABLE: _ClassVar[DeviceCommandChimesModeRequest.ChimesStatus]
    CHIMES_STATUS_UNSPECIFIED: DeviceCommandChimesModeRequest.ChimesStatus
    CHIMES_STATUS_DISABLE: DeviceCommandChimesModeRequest.ChimesStatus
    CHIMES_STATUS_ENABLE: DeviceCommandChimesModeRequest.ChimesStatus
    class GroupsStatuses(_message.Message):
        __slots__ = ("groups_statuses",)
        class GroupChimesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GROUP_CHIMES_STATUS_UNSPECIFIED: _ClassVar[DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus]
            GROUP_CHIMES_STATUS_DISABLE: _ClassVar[DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus]
            GROUP_CHIMES_STATUS_ENABLE: _ClassVar[DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus]
        GROUP_CHIMES_STATUS_UNSPECIFIED: DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus
        GROUP_CHIMES_STATUS_DISABLE: DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus
        GROUP_CHIMES_STATUS_ENABLE: DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus
        class GroupStatus(_message.Message):
            __slots__ = ("group_id", "group_chimes_status")
            GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            GROUP_CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
            group_id: str
            group_chimes_status: DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus
            def __init__(self, group_id: _Optional[str] = ..., group_chimes_status: _Optional[_Union[DeviceCommandChimesModeRequest.GroupsStatuses.GroupChimesStatus, str]] = ...) -> None: ...
        GROUPS_STATUSES_FIELD_NUMBER: _ClassVar[int]
        groups_statuses: _containers.RepeatedCompositeFieldContainer[DeviceCommandChimesModeRequest.GroupsStatuses.GroupStatus]
        def __init__(self, groups_statuses: _Optional[_Iterable[_Union[DeviceCommandChimesModeRequest.GroupsStatuses.GroupStatus, _Mapping]]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_STATUSES_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    chimes_status: DeviceCommandChimesModeRequest.ChimesStatus
    groups_statuses: DeviceCommandChimesModeRequest.GroupsStatuses
    def __init__(self, hub_id: _Optional[str] = ..., chimes_status: _Optional[_Union[DeviceCommandChimesModeRequest.ChimesStatus, str]] = ..., groups_statuses: _Optional[_Union[DeviceCommandChimesModeRequest.GroupsStatuses, _Mapping]] = ...) -> None: ...
