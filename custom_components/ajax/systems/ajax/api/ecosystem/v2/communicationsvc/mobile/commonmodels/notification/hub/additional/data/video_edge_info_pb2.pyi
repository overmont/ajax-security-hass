from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeInfo(_message.Message):
    __slots__ = ("color", "type")
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_UNKNOWN: _ClassVar[VideoEdgeInfo.Color]
        WHITE: _ClassVar[VideoEdgeInfo.Color]
        BLACK: _ClassVar[VideoEdgeInfo.Color]
        GREY: _ClassVar[VideoEdgeInfo.Color]
        GRAPHITE: _ClassVar[VideoEdgeInfo.Color]
    COLOR_UNKNOWN: VideoEdgeInfo.Color
    WHITE: VideoEdgeInfo.Color
    BLACK: VideoEdgeInfo.Color
    GREY: VideoEdgeInfo.Color
    GRAPHITE: VideoEdgeInfo.Color
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[VideoEdgeInfo.Type]
        NVR: _ClassVar[VideoEdgeInfo.Type]
        TURRET: _ClassVar[VideoEdgeInfo.Type]
        BULLET: _ClassVar[VideoEdgeInfo.Type]
        MINIDOME: _ClassVar[VideoEdgeInfo.Type]
        DOORBELL: _ClassVar[VideoEdgeInfo.Type]
        INDOOR: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_DC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_8P_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_16P_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_AI_2G_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_AI_8P_AC: _ClassVar[VideoEdgeInfo.Type]
        NVR_H_2D_AI_16P_AC: _ClassVar[VideoEdgeInfo.Type]
        TURRET_HL: _ClassVar[VideoEdgeInfo.Type]
        TURRET_HL_VF: _ClassVar[VideoEdgeInfo.Type]
        S_TURRET_HL_VF: _ClassVar[VideoEdgeInfo.Type]
        BULLET_HL: _ClassVar[VideoEdgeInfo.Type]
        BULLET_HL_VF: _ClassVar[VideoEdgeInfo.Type]
        S_BULLET_HL_VF: _ClassVar[VideoEdgeInfo.Type]
        MINIDOME_HL: _ClassVar[VideoEdgeInfo.Type]
        MINIDOME_HL_VF: _ClassVar[VideoEdgeInfo.Type]
        S_MINIDOME_HL_VF: _ClassVar[VideoEdgeInfo.Type]
    TYPE_UNKNOWN: VideoEdgeInfo.Type
    NVR: VideoEdgeInfo.Type
    TURRET: VideoEdgeInfo.Type
    BULLET: VideoEdgeInfo.Type
    MINIDOME: VideoEdgeInfo.Type
    DOORBELL: VideoEdgeInfo.Type
    INDOOR: VideoEdgeInfo.Type
    NVR_H_AC: VideoEdgeInfo.Type
    NVR_H_DC: VideoEdgeInfo.Type
    NVR_H_2D_AC: VideoEdgeInfo.Type
    NVR_H_2D_8P_AC: VideoEdgeInfo.Type
    NVR_H_2D_16P_AC: VideoEdgeInfo.Type
    NVR_H_2D_AI_2G_AC: VideoEdgeInfo.Type
    NVR_H_2D_AI_8P_AC: VideoEdgeInfo.Type
    NVR_H_2D_AI_16P_AC: VideoEdgeInfo.Type
    TURRET_HL: VideoEdgeInfo.Type
    TURRET_HL_VF: VideoEdgeInfo.Type
    S_TURRET_HL_VF: VideoEdgeInfo.Type
    BULLET_HL: VideoEdgeInfo.Type
    BULLET_HL_VF: VideoEdgeInfo.Type
    S_BULLET_HL_VF: VideoEdgeInfo.Type
    MINIDOME_HL: VideoEdgeInfo.Type
    MINIDOME_HL_VF: VideoEdgeInfo.Type
    S_MINIDOME_HL_VF: VideoEdgeInfo.Type
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    color: VideoEdgeInfo.Color
    type: VideoEdgeInfo.Type
    def __init__(self, color: _Optional[_Union[VideoEdgeInfo.Color, str]] = ..., type: _Optional[_Union[VideoEdgeInfo.Type, str]] = ...) -> None: ...
