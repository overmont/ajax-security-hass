from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel import channel_reference_pb2 as _channel_reference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenarioTriggerOptionsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class DeviceCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_CATEGORY_UNSPECIFIED: _ClassVar[GetScenarioTriggerOptionsResponse.DeviceCategory]
        DEVICE_CATEGORY_SECURITY: _ClassVar[GetScenarioTriggerOptionsResponse.DeviceCategory]
        DEVICE_CATEGORY_FIRE: _ClassVar[GetScenarioTriggerOptionsResponse.DeviceCategory]
        DEVICE_CATEGORY_LEAK: _ClassVar[GetScenarioTriggerOptionsResponse.DeviceCategory]
    DEVICE_CATEGORY_UNSPECIFIED: GetScenarioTriggerOptionsResponse.DeviceCategory
    DEVICE_CATEGORY_SECURITY: GetScenarioTriggerOptionsResponse.DeviceCategory
    DEVICE_CATEGORY_FIRE: GetScenarioTriggerOptionsResponse.DeviceCategory
    DEVICE_CATEGORY_LEAK: GetScenarioTriggerOptionsResponse.DeviceCategory
    class AlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_TYPE_UNSPECIFIED: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_REED: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_CONTACT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_MOTION: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_MOTION_CAM_OUTDOOR_MOVE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_COMBI_GLASS: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_PANIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_BUTTON_PANIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_ROLLER_SHUTTER_CUT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_VIBRATION: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_TILT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_GLASS: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_TRANSMITTER_CONTACT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_TRANSMITTER_MOVE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SERVICE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SERVICE_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SERVICE_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_ROLLER_SHUTTER_ALARM: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_ROLLER_SHUTTER_CUT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SMOKE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_TEMP: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_TEMPRISE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_CO: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_LEAK: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_DCO_LEFT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_DCO_RIGHT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_KPT_PANIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_KPT_FIRE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_KPT_MEDICAL: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_FIRE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_MPCO_PLUS_MOVE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SPFG3_SEISMIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SPFG3_SHOCK: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SPFG3_TEMP_RISE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SPFG3_CASE_BROKEN: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SPFG3_TILT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_MEDICAL: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_PANIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_GAS: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_MALFUNCTION: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_SWITCH_BASE_LEAK: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_BULGARY: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_FIRE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MEDICAL: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_PANIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GAS: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_TAMPER: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MALFUNCTION: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LEAK: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GLASS_BREAK: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MASKING: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_DURESS_CODE: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SEISMIC: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_BLOCKING_ELEMENT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_BOLT_CONTACT: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_BULGARY_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_FIRE_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MEDICAL_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_PANIC_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GAS_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_TAMPER_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MALFUNCTION_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LEAK_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GLASS_BREAK_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MASKING_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_DURESS_CODE_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SEISMIC_2: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_BULGARY_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_FIRE_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MEDICAL_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_PANIC_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GAS_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_TAMPER_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MALFUNCTION_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LEAK_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_GLASS_BREAK_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_MASKING_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_DURESS_CODE_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
        ALARM_TYPE_WIRE_INPUT_SEISMIC_3: _ClassVar[GetScenarioTriggerOptionsResponse.AlarmType]
    ALARM_TYPE_UNSPECIFIED: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_REED: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_CONTACT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_MOTION: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_MOTION_CAM_OUTDOOR_MOVE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_COMBI_GLASS: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_PANIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_BUTTON_PANIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_ROLLER_SHUTTER_CUT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_VIBRATION: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_TILT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_GLASS: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_TRANSMITTER_CONTACT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_TRANSMITTER_MOVE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SERVICE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SERVICE_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SERVICE_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_ROLLER_SHUTTER_ALARM: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_ROLLER_SHUTTER_CUT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SMOKE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_TEMP: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_TEMPRISE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_CO: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_LEAK: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_DCO_LEFT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_DCO_RIGHT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_KPT_PANIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_KPT_FIRE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_KPT_MEDICAL: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_FIRE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_MPCO_PLUS_MOVE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SPFG3_SEISMIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SPFG3_SHOCK: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SPFG3_TEMP_RISE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SPFG3_CASE_BROKEN: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SPFG3_TILT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_MEDICAL: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_PANIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_GAS: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_MALFUNCTION: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_SWITCH_BASE_LEAK: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_BULGARY: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_FIRE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MEDICAL: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_PANIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GAS: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_TAMPER: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MALFUNCTION: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LEAK: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GLASS_BREAK: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MASKING: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_DURESS_CODE: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SEISMIC: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_BLOCKING_ELEMENT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_BOLT_CONTACT: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_BULGARY_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_FIRE_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MEDICAL_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_PANIC_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GAS_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_TAMPER_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MALFUNCTION_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LEAK_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GLASS_BREAK_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MASKING_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_DURESS_CODE_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SEISMIC_2: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_BULGARY_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_FIRE_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MEDICAL_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_PANIC_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GAS_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_TAMPER_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MALFUNCTION_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LEAK_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_GLASS_BREAK_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_HIGH_TEMPERATURE_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_LOW_TEMPERATURE_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_MASKING_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_DURESS_CODE_3: GetScenarioTriggerOptionsResponse.AlarmType
    ALARM_TYPE_WIRE_INPUT_SEISMIC_3: GetScenarioTriggerOptionsResponse.AlarmType
    class Success(_message.Message):
        __slots__ = ("scenario_trigger_options",)
        SCENARIO_TRIGGER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        scenario_trigger_options: _containers.RepeatedCompositeFieldContainer[GetScenarioTriggerOptionsResponse.ScenarioTriggerOption]
        def __init__(self, scenario_trigger_options: _Optional[_Iterable[_Union[GetScenarioTriggerOptionsResponse.ScenarioTriggerOption, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permissions_denied", "space_armed", "hub_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permissions_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permissions_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    class ScenarioTriggerOption(_message.Message):
        __slots__ = ("temperature_trigger_option", "alarming_device_trigger_option", "cross_zone_trigger_option", "smart_lock_trigger_option", "video_detection_trigger_option")
        TEMPERATURE_TRIGGER_OPTION_FIELD_NUMBER: _ClassVar[int]
        ALARMING_DEVICE_TRIGGER_OPTION_FIELD_NUMBER: _ClassVar[int]
        CROSS_ZONE_TRIGGER_OPTION_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_TRIGGER_OPTION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_DETECTION_TRIGGER_OPTION_FIELD_NUMBER: _ClassVar[int]
        temperature_trigger_option: GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption
        alarming_device_trigger_option: GetScenarioTriggerOptionsResponse.AlarmingDeviceTriggerOption
        cross_zone_trigger_option: GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption
        smart_lock_trigger_option: GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption
        video_detection_trigger_option: GetScenarioTriggerOptionsResponse.VideoDetectionTriggerOption
        def __init__(self, temperature_trigger_option: _Optional[_Union[GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption, _Mapping]] = ..., alarming_device_trigger_option: _Optional[_Union[GetScenarioTriggerOptionsResponse.AlarmingDeviceTriggerOption, _Mapping]] = ..., cross_zone_trigger_option: _Optional[_Union[GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption, _Mapping]] = ..., smart_lock_trigger_option: _Optional[_Union[GetScenarioTriggerOptionsResponse.GenericObjectTriggerOption, _Mapping]] = ..., video_detection_trigger_option: _Optional[_Union[GetScenarioTriggerOptionsResponse.VideoDetectionTriggerOption, _Mapping]] = ...) -> None: ...
    class GenericObjectTriggerOption(_message.Message):
        __slots__ = ("object_id",)
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        object_id: str
        def __init__(self, object_id: _Optional[str] = ...) -> None: ...
    class VideoDetectionTriggerOption(_message.Message):
        __slots__ = ("channel_reference",)
        CHANNEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
        channel_reference: _channel_reference_pb2.ChannelReference
        def __init__(self, channel_reference: _Optional[_Union[_channel_reference_pb2.ChannelReference, _Mapping]] = ...) -> None: ...
    class AlarmingDeviceTriggerOption(_message.Message):
        __slots__ = ("device_id", "alarm_options", "device_category")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        ALARM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        alarm_options: _containers.RepeatedCompositeFieldContainer[GetScenarioTriggerOptionsResponse.AlarmOption]
        device_category: GetScenarioTriggerOptionsResponse.DeviceCategory
        def __init__(self, device_id: _Optional[str] = ..., alarm_options: _Optional[_Iterable[_Union[GetScenarioTriggerOptionsResponse.AlarmOption, _Mapping]]] = ..., device_category: _Optional[_Union[GetScenarioTriggerOptionsResponse.DeviceCategory, str]] = ...) -> None: ...
    class AlarmOption(_message.Message):
        __slots__ = ("is_available", "alarm_type")
        IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
        is_available: bool
        alarm_type: GetScenarioTriggerOptionsResponse.AlarmType
        def __init__(self, is_available: bool = ..., alarm_type: _Optional[_Union[GetScenarioTriggerOptionsResponse.AlarmType, str]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetScenarioTriggerOptionsResponse.Success
    failure: GetScenarioTriggerOptionsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetScenarioTriggerOptionsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetScenarioTriggerOptionsResponse.Failure, _Mapping]] = ...) -> None: ...
