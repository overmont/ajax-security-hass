from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadSpaceImageResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("images",)
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        images: _image_pb2.Images
        def __init__(self, images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "too_large_file", "unsupported_format")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TOO_LARGE_FILE_FIELD_NUMBER: _ClassVar[int]
        UNSUPPORTED_FORMAT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        too_large_file: _response_pb2.DefaultError
        unsupported_format: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., too_large_file: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., unsupported_format: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UploadSpaceImageResponse.Success
    failure: UploadSpaceImageResponse.Failure
    def __init__(self, success: _Optional[_Union[UploadSpaceImageResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[UploadSpaceImageResponse.Failure, _Mapping]] = ...) -> None: ...
