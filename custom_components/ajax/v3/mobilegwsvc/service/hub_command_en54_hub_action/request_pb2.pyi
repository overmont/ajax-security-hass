from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommandEn54HubActionRequest(_message.Message):
    __slots__ = ("hub_id", "command_type", "cms_disablement_events_args")
    class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMAND_TYPE_UNSPECIFIED: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_RESET_FIRE_ALARM: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_SILENCE_SOUNDERS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_RESOUND_SOUNDERS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_RESOUND_EVACUATION: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_START_INV_DELAY: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_OVERRIDE_INV_ACK_DELAYS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_ON_INV_ACK_DELAYS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_OFF_INV_ACK_DELAYS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_CMS_DISABLEMENT_ALARM_EVENT: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
        COMMAND_TYPE_CMS_DISABLEMENT_FAULT_EVENTS: _ClassVar[HubCommandEn54HubActionRequest.CommandType]
    COMMAND_TYPE_UNSPECIFIED: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_RESET_FIRE_ALARM: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_SILENCE_SOUNDERS: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_RESOUND_SOUNDERS: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_RESOUND_EVACUATION: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_START_INV_DELAY: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_OVERRIDE_INV_ACK_DELAYS: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_ON_INV_ACK_DELAYS: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_OFF_INV_ACK_DELAYS: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_CMS_DISABLEMENT_ALARM_EVENT: HubCommandEn54HubActionRequest.CommandType
    COMMAND_TYPE_CMS_DISABLEMENT_FAULT_EVENTS: HubCommandEn54HubActionRequest.CommandType
    class En54HubActionCmsDisablementEventsArgs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_UNSPECIFIED: _ClassVar[HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs]
        EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_OFF: _ClassVar[HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs]
        EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_DISABLEMENT: _ClassVar[HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs]
    EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_UNSPECIFIED: HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs
    EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_OFF: HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs
    EN54_HUB_ACTION_CMS_DISABLEMENT_EVENTS_ARGS_DISABLEMENT: HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    CMS_DISABLEMENT_EVENTS_ARGS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    command_type: HubCommandEn54HubActionRequest.CommandType
    cms_disablement_events_args: HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs
    def __init__(self, hub_id: _Optional[str] = ..., command_type: _Optional[_Union[HubCommandEn54HubActionRequest.CommandType, str]] = ..., cms_disablement_events_args: _Optional[_Union[HubCommandEn54HubActionRequest.En54HubActionCmsDisablementEventsArgs, str]] = ...) -> None: ...
