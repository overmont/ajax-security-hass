from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import access_card_type_pb2 as _access_card_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_type_pb2 as _source_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import wire_input_alarm_type_pb2 as _wire_input_alarm_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import yavir_access_control_type_pb2 as _yavir_access_control_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_special_appearance_type_pb2 as _device_special_appearance_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "device_color", "device_label", "hub_user_type", "access_card_type", "yavir_access_control_type", "box_type", "wire_input_alarm_type", "device_special_appearance_type", "image_info", "room_hex_id", "room_name")
    class HubUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_TYPE_UNSPECIFIED: _ClassVar[HubNotificationSource.HubUserType]
        USER: _ClassVar[HubNotificationSource.HubUserType]
        PRO: _ClassVar[HubNotificationSource.HubUserType]
        COMPANY: _ClassVar[HubNotificationSource.HubUserType]
    USER_TYPE_UNSPECIFIED: HubNotificationSource.HubUserType
    USER: HubNotificationSource.HubUserType
    PRO: HubNotificationSource.HubUserType
    COMPANY: HubNotificationSource.HubUserType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    YAVIR_ACCESS_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SPECIAL_APPEARANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.HubNotificationSourceType
    id: str
    name: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    hub_user_type: HubNotificationSource.HubUserType
    access_card_type: _access_card_type_pb2.AccessCardType
    yavir_access_control_type: _yavir_access_control_type_pb2.YavirAccessControlType
    box_type: _hub_box_type_pb2.HubBoxType
    wire_input_alarm_type: _wire_input_alarm_type_pb2.CustomAlarmType
    device_special_appearance_type: _device_special_appearance_type_pb2.DeviceSpecialAppearanceType
    image_info: _source_image_info_pb2.SourceImageInfo
    room_hex_id: str
    room_name: str
    def __init__(self, type: _Optional[_Union[_source_type_pb2.HubNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., hub_user_type: _Optional[_Union[HubNotificationSource.HubUserType, str]] = ..., access_card_type: _Optional[_Union[_access_card_type_pb2.AccessCardType, str]] = ..., yavir_access_control_type: _Optional[_Union[_yavir_access_control_type_pb2.YavirAccessControlType, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ..., wire_input_alarm_type: _Optional[_Union[_wire_input_alarm_type_pb2.CustomAlarmType, str]] = ..., device_special_appearance_type: _Optional[_Union[_device_special_appearance_type_pb2.DeviceSpecialAppearanceType, str]] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ..., room_hex_id: _Optional[str] = ..., room_name: _Optional[str] = ...) -> None: ...
