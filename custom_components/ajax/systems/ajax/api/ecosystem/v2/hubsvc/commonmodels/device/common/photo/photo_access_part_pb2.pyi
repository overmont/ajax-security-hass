from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoAccessPart(_message.Message):
    __slots__ = ("someone_can_make_photo",)
    class SomeoneCanMakePhoto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOMEONE_CAN_MAKE_PHOTO_UNSPECIFIED: _ClassVar[PhotoAccessPart.SomeoneCanMakePhoto]
        SOMEONE_CAN_MAKE_PHOTO_DISABLED: _ClassVar[PhotoAccessPart.SomeoneCanMakePhoto]
        SOMEONE_CAN_MAKE_PHOTO_ENABLED: _ClassVar[PhotoAccessPart.SomeoneCanMakePhoto]
        SOMEONE_CAN_MAKE_PHOTO_HUB_PHOD_DISABLED: _ClassVar[PhotoAccessPart.SomeoneCanMakePhoto]
    SOMEONE_CAN_MAKE_PHOTO_UNSPECIFIED: PhotoAccessPart.SomeoneCanMakePhoto
    SOMEONE_CAN_MAKE_PHOTO_DISABLED: PhotoAccessPart.SomeoneCanMakePhoto
    SOMEONE_CAN_MAKE_PHOTO_ENABLED: PhotoAccessPart.SomeoneCanMakePhoto
    SOMEONE_CAN_MAKE_PHOTO_HUB_PHOD_DISABLED: PhotoAccessPart.SomeoneCanMakePhoto
    SOMEONE_CAN_MAKE_PHOTO_FIELD_NUMBER: _ClassVar[int]
    someone_can_make_photo: PhotoAccessPart.SomeoneCanMakePhoto
    def __init__(self, someone_can_make_photo: _Optional[_Union[PhotoAccessPart.SomeoneCanMakePhoto, str]] = ...) -> None: ...
