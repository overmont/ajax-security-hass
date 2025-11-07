from systems.ajax.api.ecosystem.v2.commonmodels.device.common import security_standart_pb2 as _security_standart_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import always_active_pb2 as _always_active_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonArmingPart(_message.Message):
    __slots__ = ("night_mode_arm", "arm_delay", "apply_delays_to_night_mode", "perimeter_arm_delay", "arming_mode", "alarm_delay", "verifies_alarm", "perimeter_alarm_delay", "device_alarm_logic_type", "indicator_light_mode", "arming_capabilities", "current_standard", "always_active", "delay_ranges", "arming_mode_capabilities")
    class NightModeArm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NIGHT_MODE_ARM_UNSPECIFIED: _ClassVar[CommonArmingPart.NightModeArm]
        NIGHT_MODE_ARM_DISABLED: _ClassVar[CommonArmingPart.NightModeArm]
        NIGHT_MODE_ARM_ENABLED: _ClassVar[CommonArmingPart.NightModeArm]
    NIGHT_MODE_ARM_UNSPECIFIED: CommonArmingPart.NightModeArm
    NIGHT_MODE_ARM_DISABLED: CommonArmingPart.NightModeArm
    NIGHT_MODE_ARM_ENABLED: CommonArmingPart.NightModeArm
    class ApplyDelaysToNightMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPLY_DELAYS_TO_NIGHT_MODE_UNSPECIFIED: _ClassVar[CommonArmingPart.ApplyDelaysToNightMode]
        APPLY_DELAYS_TO_NIGHT_MODE_DISABLED: _ClassVar[CommonArmingPart.ApplyDelaysToNightMode]
        APPLY_DELAYS_TO_NIGHT_MODE_ENABLED: _ClassVar[CommonArmingPart.ApplyDelaysToNightMode]
    APPLY_DELAYS_TO_NIGHT_MODE_UNSPECIFIED: CommonArmingPart.ApplyDelaysToNightMode
    APPLY_DELAYS_TO_NIGHT_MODE_DISABLED: CommonArmingPart.ApplyDelaysToNightMode
    APPLY_DELAYS_TO_NIGHT_MODE_ENABLED: CommonArmingPart.ApplyDelaysToNightMode
    class VerifiesAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERIFIES_ALARM_UNSPECIFIED: _ClassVar[CommonArmingPart.VerifiesAlarm]
        VERIFIES_ALARM_DISABLED: _ClassVar[CommonArmingPart.VerifiesAlarm]
        VERIFIES_ALARM_ENABLED: _ClassVar[CommonArmingPart.VerifiesAlarm]
    VERIFIES_ALARM_UNSPECIFIED: CommonArmingPart.VerifiesAlarm
    VERIFIES_ALARM_DISABLED: CommonArmingPart.VerifiesAlarm
    VERIFIES_ALARM_ENABLED: CommonArmingPart.VerifiesAlarm
    class ArmingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARMING_MODE_UNSPECIFIED: _ClassVar[CommonArmingPart.ArmingMode]
        ARMING_MODE_NORMAL: _ClassVar[CommonArmingPart.ArmingMode]
        ARMING_MODE_ENTRY_EXIT: _ClassVar[CommonArmingPart.ArmingMode]
        ARMING_MODE_FOLLOWER: _ClassVar[CommonArmingPart.ArmingMode]
        ARMING_MODE_DISABLED: _ClassVar[CommonArmingPart.ArmingMode]
    ARMING_MODE_UNSPECIFIED: CommonArmingPart.ArmingMode
    ARMING_MODE_NORMAL: CommonArmingPart.ArmingMode
    ARMING_MODE_ENTRY_EXIT: CommonArmingPart.ArmingMode
    ARMING_MODE_FOLLOWER: CommonArmingPart.ArmingMode
    ARMING_MODE_DISABLED: CommonArmingPart.ArmingMode
    class DeviceAlarmLogicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_ALARM_LOGIC_TYPE_UNSPECIFIED: _ClassVar[CommonArmingPart.DeviceAlarmLogicType]
        DEVICE_ALARM_LOGIC_TYPE_NONE: _ClassVar[CommonArmingPart.DeviceAlarmLogicType]
        DEVICE_ALARM_LOGIC_TYPE_ARMING_COMPLETION_DEVICE: _ClassVar[CommonArmingPart.DeviceAlarmLogicType]
        DEVICE_ALARM_LOGIC_TYPE_ENTRY_ROUTE: _ClassVar[CommonArmingPart.DeviceAlarmLogicType]
    DEVICE_ALARM_LOGIC_TYPE_UNSPECIFIED: CommonArmingPart.DeviceAlarmLogicType
    DEVICE_ALARM_LOGIC_TYPE_NONE: CommonArmingPart.DeviceAlarmLogicType
    DEVICE_ALARM_LOGIC_TYPE_ARMING_COMPLETION_DEVICE: CommonArmingPart.DeviceAlarmLogicType
    DEVICE_ALARM_LOGIC_TYPE_ENTRY_ROUTE: CommonArmingPart.DeviceAlarmLogicType
    class ArmingCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARMING_CAPABILITY_UNSPECIFIED: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_ZONE_TEST: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_DELAYS: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_NIGHT_MODE_ARM: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_TIMEOUTS_TO_PERIMETER_HUB: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_PERIMETER_DELAYS: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_ARMING_MODE: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_SIA_STANDARD: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_ALWAYS_ACTIVE_PER_DEVICE: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_ARMING_MODE_DISABLED: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_HUB_WITHOUT_DELAYS_SUPPORT_BY_HUB_TYPE: _ClassVar[CommonArmingPart.ArmingCapability]
        ARMING_CAPABILITY_HUB_WITHOUT_DELAYS_SUPPORT_BY_HUB_VERSION: _ClassVar[CommonArmingPart.ArmingCapability]
    ARMING_CAPABILITY_UNSPECIFIED: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_ZONE_TEST: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_DELAYS: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_NIGHT_MODE_ARM: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_TIMEOUTS_TO_PERIMETER_HUB: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_PERIMETER_DELAYS: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_ARMING_MODE: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_SIA_STANDARD: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_ALWAYS_ACTIVE_PER_DEVICE: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_ARMING_MODE_DISABLED: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_HUB_WITHOUT_DELAYS_SUPPORT_BY_HUB_TYPE: CommonArmingPart.ArmingCapability
    ARMING_CAPABILITY_HUB_WITHOUT_DELAYS_SUPPORT_BY_HUB_VERSION: CommonArmingPart.ArmingCapability
    class CommonArmingPartSettings(_message.Message):
        __slots__ = ("night_mode_arm", "arm_delay", "perimeter_arm_delay", "arming_mode", "alarm_delay", "perimeter_alarm_delay", "always_active")
        NIGHT_MODE_ARM_FIELD_NUMBER: _ClassVar[int]
        ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        PERIMETER_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
        ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        PERIMETER_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        night_mode_arm: CommonArmingPart.NightModeArm
        arm_delay: CommonArmingPart.ArmDelay
        perimeter_arm_delay: CommonArmingPart.PerimeterArmDelay
        arming_mode: CommonArmingPart.ArmingMode
        alarm_delay: CommonArmingPart.AlarmDelay
        perimeter_alarm_delay: CommonArmingPart.PerimeterAlarmDelay
        always_active: _always_active_pb2.AlwaysActive
        def __init__(self, night_mode_arm: _Optional[_Union[CommonArmingPart.NightModeArm, str]] = ..., arm_delay: _Optional[_Union[CommonArmingPart.ArmDelay, _Mapping]] = ..., perimeter_arm_delay: _Optional[_Union[CommonArmingPart.PerimeterArmDelay, _Mapping]] = ..., arming_mode: _Optional[_Union[CommonArmingPart.ArmingMode, str]] = ..., alarm_delay: _Optional[_Union[CommonArmingPart.AlarmDelay, _Mapping]] = ..., perimeter_alarm_delay: _Optional[_Union[CommonArmingPart.PerimeterAlarmDelay, _Mapping]] = ..., always_active: _Optional[_Union[_always_active_pb2.AlwaysActive, str]] = ...) -> None: ...
    class ArmDelay(_message.Message):
        __slots__ = ("seconds",)
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        seconds: int
        def __init__(self, seconds: _Optional[int] = ...) -> None: ...
    class PerimeterArmDelay(_message.Message):
        __slots__ = ("seconds",)
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        seconds: int
        def __init__(self, seconds: _Optional[int] = ...) -> None: ...
    class AlarmDelay(_message.Message):
        __slots__ = ("seconds",)
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        seconds: int
        def __init__(self, seconds: _Optional[int] = ...) -> None: ...
    class PerimeterAlarmDelay(_message.Message):
        __slots__ = ("seconds",)
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        seconds: int
        def __init__(self, seconds: _Optional[int] = ...) -> None: ...
    class DelayRanges(_message.Message):
        __slots__ = ("entry_exit_delay_ranges", "follower_delay_ranges")
        class EntryExitDelayRanges(_message.Message):
            __slots__ = ("arm_delay_range", "alarm_delay_range", "perimeter_arm_delay_range", "perimeter_alarm_delay_range")
            ARM_DELAY_RANGE_FIELD_NUMBER: _ClassVar[int]
            ALARM_DELAY_RANGE_FIELD_NUMBER: _ClassVar[int]
            PERIMETER_ARM_DELAY_RANGE_FIELD_NUMBER: _ClassVar[int]
            PERIMETER_ALARM_DELAY_RANGE_FIELD_NUMBER: _ClassVar[int]
            arm_delay_range: CommonArmingPart.DelayRanges.DelayRange
            alarm_delay_range: CommonArmingPart.DelayRanges.DelayRange
            perimeter_arm_delay_range: CommonArmingPart.DelayRanges.DelayRange
            perimeter_alarm_delay_range: CommonArmingPart.DelayRanges.DelayRange
            def __init__(self, arm_delay_range: _Optional[_Union[CommonArmingPart.DelayRanges.DelayRange, _Mapping]] = ..., alarm_delay_range: _Optional[_Union[CommonArmingPart.DelayRanges.DelayRange, _Mapping]] = ..., perimeter_arm_delay_range: _Optional[_Union[CommonArmingPart.DelayRanges.DelayRange, _Mapping]] = ..., perimeter_alarm_delay_range: _Optional[_Union[CommonArmingPart.DelayRanges.DelayRange, _Mapping]] = ...) -> None: ...
        class FollowerDelayRanges(_message.Message):
            __slots__ = ("perimeter_delays_range",)
            PERIMETER_DELAYS_RANGE_FIELD_NUMBER: _ClassVar[int]
            perimeter_delays_range: CommonArmingPart.DelayRanges.DelayRange
            def __init__(self, perimeter_delays_range: _Optional[_Union[CommonArmingPart.DelayRanges.DelayRange, _Mapping]] = ...) -> None: ...
        class DelayRange(_message.Message):
            __slots__ = ("range_values", "default")
            RANGE_VALUES_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_FIELD_NUMBER: _ClassVar[int]
            range_values: _containers.RepeatedScalarFieldContainer[int]
            default: int
            def __init__(self, range_values: _Optional[_Iterable[int]] = ..., default: _Optional[int] = ...) -> None: ...
        ENTRY_EXIT_DELAY_RANGES_FIELD_NUMBER: _ClassVar[int]
        FOLLOWER_DELAY_RANGES_FIELD_NUMBER: _ClassVar[int]
        entry_exit_delay_ranges: CommonArmingPart.DelayRanges.EntryExitDelayRanges
        follower_delay_ranges: CommonArmingPart.DelayRanges.FollowerDelayRanges
        def __init__(self, entry_exit_delay_ranges: _Optional[_Union[CommonArmingPart.DelayRanges.EntryExitDelayRanges, _Mapping]] = ..., follower_delay_ranges: _Optional[_Union[CommonArmingPart.DelayRanges.FollowerDelayRanges, _Mapping]] = ...) -> None: ...
    class IndicatorLightMode(_message.Message):
        __slots__ = ("mode", "capabilities")
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[CommonArmingPart.IndicatorLightMode.Mode]
            MODE_DONT_BLINK_ON_ALARM: _ClassVar[CommonArmingPart.IndicatorLightMode.Mode]
            MODE_STANDARD: _ClassVar[CommonArmingPart.IndicatorLightMode.Mode]
        MODE_UNSPECIFIED: CommonArmingPart.IndicatorLightMode.Mode
        MODE_DONT_BLINK_ON_ALARM: CommonArmingPart.IndicatorLightMode.Mode
        MODE_STANDARD: CommonArmingPart.IndicatorLightMode.Mode
        class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CAPABILITY_UNSPECIFIED: _ClassVar[CommonArmingPart.IndicatorLightMode.Capability]
            CAPABILITY_INDICATOR_LIGHT_MODE: _ClassVar[CommonArmingPart.IndicatorLightMode.Capability]
        CAPABILITY_UNSPECIFIED: CommonArmingPart.IndicatorLightMode.Capability
        CAPABILITY_INDICATOR_LIGHT_MODE: CommonArmingPart.IndicatorLightMode.Capability
        MODE_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        mode: CommonArmingPart.IndicatorLightMode.Mode
        capabilities: _containers.RepeatedScalarFieldContainer[CommonArmingPart.IndicatorLightMode.Capability]
        def __init__(self, mode: _Optional[_Union[CommonArmingPart.IndicatorLightMode.Mode, str]] = ..., capabilities: _Optional[_Iterable[_Union[CommonArmingPart.IndicatorLightMode.Capability, str]]] = ...) -> None: ...
    NIGHT_MODE_ARM_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    APPLY_DELAYS_TO_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    VERIFIES_ALARM_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ALARM_LOGIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDICATOR_LIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    ARMING_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELAY_RANGES_FIELD_NUMBER: _ClassVar[int]
    ARMING_MODE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    night_mode_arm: CommonArmingPart.NightModeArm
    arm_delay: CommonArmingPart.ArmDelay
    apply_delays_to_night_mode: CommonArmingPart.ApplyDelaysToNightMode
    perimeter_arm_delay: CommonArmingPart.PerimeterArmDelay
    arming_mode: CommonArmingPart.ArmingMode
    alarm_delay: CommonArmingPart.AlarmDelay
    verifies_alarm: CommonArmingPart.VerifiesAlarm
    perimeter_alarm_delay: CommonArmingPart.PerimeterAlarmDelay
    device_alarm_logic_type: CommonArmingPart.DeviceAlarmLogicType
    indicator_light_mode: CommonArmingPart.IndicatorLightMode
    arming_capabilities: _containers.RepeatedScalarFieldContainer[CommonArmingPart.ArmingCapability]
    current_standard: _security_standart_pb2.SecurityStandard
    always_active: _always_active_pb2.AlwaysActive
    delay_ranges: CommonArmingPart.DelayRanges
    arming_mode_capabilities: _containers.RepeatedScalarFieldContainer[CommonArmingPart.ArmingMode]
    def __init__(self, night_mode_arm: _Optional[_Union[CommonArmingPart.NightModeArm, str]] = ..., arm_delay: _Optional[_Union[CommonArmingPart.ArmDelay, _Mapping]] = ..., apply_delays_to_night_mode: _Optional[_Union[CommonArmingPart.ApplyDelaysToNightMode, str]] = ..., perimeter_arm_delay: _Optional[_Union[CommonArmingPart.PerimeterArmDelay, _Mapping]] = ..., arming_mode: _Optional[_Union[CommonArmingPart.ArmingMode, str]] = ..., alarm_delay: _Optional[_Union[CommonArmingPart.AlarmDelay, _Mapping]] = ..., verifies_alarm: _Optional[_Union[CommonArmingPart.VerifiesAlarm, str]] = ..., perimeter_alarm_delay: _Optional[_Union[CommonArmingPart.PerimeterAlarmDelay, _Mapping]] = ..., device_alarm_logic_type: _Optional[_Union[CommonArmingPart.DeviceAlarmLogicType, str]] = ..., indicator_light_mode: _Optional[_Union[CommonArmingPart.IndicatorLightMode, _Mapping]] = ..., arming_capabilities: _Optional[_Iterable[_Union[CommonArmingPart.ArmingCapability, str]]] = ..., current_standard: _Optional[_Union[_security_standart_pb2.SecurityStandard, str]] = ..., always_active: _Optional[_Union[_always_active_pb2.AlwaysActive, str]] = ..., delay_ranges: _Optional[_Union[CommonArmingPart.DelayRanges, _Mapping]] = ..., arming_mode_capabilities: _Optional[_Iterable[_Union[CommonArmingPart.ArmingMode, str]]] = ...) -> None: ...
