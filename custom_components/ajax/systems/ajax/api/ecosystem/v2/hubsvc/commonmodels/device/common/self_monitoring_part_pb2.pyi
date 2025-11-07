from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import patch_type_pb2 as _patch_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SelfMonitoringPart(_message.Message):
    __slots__ = ("capabilities", "self_monitoring_configs")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[SelfMonitoringPart.Capability]
        CAPABILITY_ARC_REPORTING: _ClassVar[SelfMonitoringPart.Capability]
    CAPABILITY_UNSPECIFIED: SelfMonitoringPart.Capability
    CAPABILITY_ARC_REPORTING: SelfMonitoringPart.Capability
    class SelfMonitoringConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SELF_MONITORING_CONFIG_UNSPECIFIED: _ClassVar[SelfMonitoringPart.SelfMonitoringConfig]
        SELF_MONITORING_CONFIG_LOCAL_ALARM: _ClassVar[SelfMonitoringPart.SelfMonitoringConfig]
        SELF_MONITORING_CONFIG_DISABLE_ARC_REPORTING: _ClassVar[SelfMonitoringPart.SelfMonitoringConfig]
    SELF_MONITORING_CONFIG_UNSPECIFIED: SelfMonitoringPart.SelfMonitoringConfig
    SELF_MONITORING_CONFIG_LOCAL_ALARM: SelfMonitoringPart.SelfMonitoringConfig
    SELF_MONITORING_CONFIG_DISABLE_ARC_REPORTING: SelfMonitoringPart.SelfMonitoringConfig
    class SelfMonitoringPartSettings(_message.Message):
        __slots__ = ("self_monitoring_configs",)
        class SelfMonitoringConfigPatch(_message.Message):
            __slots__ = ("patch_type", "self_monitoring_config")
            PATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
            SELF_MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
            patch_type: _patch_type_pb2.PatchType
            self_monitoring_config: SelfMonitoringPart.SelfMonitoringConfig
            def __init__(self, patch_type: _Optional[_Union[_patch_type_pb2.PatchType, str]] = ..., self_monitoring_config: _Optional[_Union[SelfMonitoringPart.SelfMonitoringConfig, str]] = ...) -> None: ...
        SELF_MONITORING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        self_monitoring_configs: _containers.RepeatedCompositeFieldContainer[SelfMonitoringPart.SelfMonitoringPartSettings.SelfMonitoringConfigPatch]
        def __init__(self, self_monitoring_configs: _Optional[_Iterable[_Union[SelfMonitoringPart.SelfMonitoringPartSettings.SelfMonitoringConfigPatch, _Mapping]]] = ...) -> None: ...
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SELF_MONITORING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedScalarFieldContainer[SelfMonitoringPart.Capability]
    self_monitoring_configs: _containers.RepeatedScalarFieldContainer[SelfMonitoringPart.SelfMonitoringConfig]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[SelfMonitoringPart.Capability, str]]] = ..., self_monitoring_configs: _Optional[_Iterable[_Union[SelfMonitoringPart.SelfMonitoringConfig, str]]] = ...) -> None: ...
