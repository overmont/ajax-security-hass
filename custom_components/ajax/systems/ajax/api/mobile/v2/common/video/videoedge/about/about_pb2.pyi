from systems.ajax.api.mobile.v2.common.video.videoedge.about import constraints_pb2 as _constraints_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class About(_message.Message):
    __slots__ = ("type", "color", "device_features", "constraints", "mono_channel", "fully_qualified_id")
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_UNKNOWN: _ClassVar[About.Color]
        WHITE: _ClassVar[About.Color]
        BLACK: _ClassVar[About.Color]
        GREY: _ClassVar[About.Color]
        GRAPHITE: _ClassVar[About.Color]
    COLOR_UNKNOWN: About.Color
    WHITE: About.Color
    BLACK: About.Color
    GREY: About.Color
    GRAPHITE: About.Color
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[About.Type]
        NVR: _ClassVar[About.Type]
        TURRET: _ClassVar[About.Type]
        BULLET: _ClassVar[About.Type]
        MINIDOME: _ClassVar[About.Type]
        DOORBELL: _ClassVar[About.Type]
        INDOOR: _ClassVar[About.Type]
        NVR_H_AC: _ClassVar[About.Type]
        NVR_H_DC: _ClassVar[About.Type]
        NVR_H_2D_AC: _ClassVar[About.Type]
        NVR_H_2D_8P_AC: _ClassVar[About.Type]
        NVR_H_2D_16P_AC: _ClassVar[About.Type]
        NVR_H_2D_AI_2G_AC: _ClassVar[About.Type]
        NVR_H_2D_AI_8P_AC: _ClassVar[About.Type]
        NVR_H_2D_AI_16P_AC: _ClassVar[About.Type]
        TURRET_HL: _ClassVar[About.Type]
        TURRET_HL_VF: _ClassVar[About.Type]
        S_TURRET_HL_VF: _ClassVar[About.Type]
        BULLET_HL: _ClassVar[About.Type]
        BULLET_HL_VF: _ClassVar[About.Type]
        S_BULLET_HL_VF: _ClassVar[About.Type]
        MINIDOME_HL: _ClassVar[About.Type]
        MINIDOME_HL_VF: _ClassVar[About.Type]
        S_MINIDOME_HL_VF: _ClassVar[About.Type]
    TYPE_UNKNOWN: About.Type
    NVR: About.Type
    TURRET: About.Type
    BULLET: About.Type
    MINIDOME: About.Type
    DOORBELL: About.Type
    INDOOR: About.Type
    NVR_H_AC: About.Type
    NVR_H_DC: About.Type
    NVR_H_2D_AC: About.Type
    NVR_H_2D_8P_AC: About.Type
    NVR_H_2D_16P_AC: About.Type
    NVR_H_2D_AI_2G_AC: About.Type
    NVR_H_2D_AI_8P_AC: About.Type
    NVR_H_2D_AI_16P_AC: About.Type
    TURRET_HL: About.Type
    TURRET_HL_VF: About.Type
    S_TURRET_HL_VF: About.Type
    BULLET_HL: About.Type
    BULLET_HL_VF: About.Type
    S_BULLET_HL_VF: About.Type
    MINIDOME_HL: About.Type
    MINIDOME_HL_VF: About.Type
    S_MINIDOME_HL_VF: About.Type
    class DeviceFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNKNOWN: _ClassVar[About.DeviceFeature]
        BLUETOOTH: _ClassVar[About.DeviceFeature]
        JEWELLER: _ClassVar[About.DeviceFeature]
        WIFI: _ClassVar[About.DeviceFeature]
    FEATURE_UNKNOWN: About.DeviceFeature
    BLUETOOTH: About.DeviceFeature
    JEWELLER: About.DeviceFeature
    WIFI: About.DeviceFeature
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    MONO_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_ID_FIELD_NUMBER: _ClassVar[int]
    type: About.Type
    color: About.Color
    device_features: _containers.RepeatedScalarFieldContainer[About.DeviceFeature]
    constraints: _constraints_pb2.Constraints
    mono_channel: bool
    fully_qualified_id: str
    def __init__(self, type: _Optional[_Union[About.Type, str]] = ..., color: _Optional[_Union[About.Color, str]] = ..., device_features: _Optional[_Iterable[_Union[About.DeviceFeature, str]]] = ..., constraints: _Optional[_Union[_constraints_pb2.Constraints, _Mapping]] = ..., mono_channel: bool = ..., fully_qualified_id: _Optional[str] = ...) -> None: ...
