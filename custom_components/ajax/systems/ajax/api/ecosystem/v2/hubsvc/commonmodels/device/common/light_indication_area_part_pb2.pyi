from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightIndicationAreaPart(_message.Message):
    __slots__ = ("light_indication_area",)
    class LightIndicationArea(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIGHT_INDICATION_AREA_UNSPECIFIED: _ClassVar[LightIndicationAreaPart.LightIndicationArea]
        LIGHT_INDICATION_AREA_CORNER_BACKLIGHT: _ClassVar[LightIndicationAreaPart.LightIndicationArea]
        LIGHT_INDICATION_AREA_FULL_FRAME_BACKLIGHT: _ClassVar[LightIndicationAreaPart.LightIndicationArea]
    LIGHT_INDICATION_AREA_UNSPECIFIED: LightIndicationAreaPart.LightIndicationArea
    LIGHT_INDICATION_AREA_CORNER_BACKLIGHT: LightIndicationAreaPart.LightIndicationArea
    LIGHT_INDICATION_AREA_FULL_FRAME_BACKLIGHT: LightIndicationAreaPart.LightIndicationArea
    class LightIndicationAreaPartSettings(_message.Message):
        __slots__ = ("light_indication_area",)
        LIGHT_INDICATION_AREA_FIELD_NUMBER: _ClassVar[int]
        light_indication_area: LightIndicationAreaPart.LightIndicationArea
        def __init__(self, light_indication_area: _Optional[_Union[LightIndicationAreaPart.LightIndicationArea, str]] = ...) -> None: ...
    LIGHT_INDICATION_AREA_FIELD_NUMBER: _ClassVar[int]
    light_indication_area: LightIndicationAreaPart.LightIndicationArea
    def __init__(self, light_indication_area: _Optional[_Union[LightIndicationAreaPart.LightIndicationArea, str]] = ...) -> None: ...
