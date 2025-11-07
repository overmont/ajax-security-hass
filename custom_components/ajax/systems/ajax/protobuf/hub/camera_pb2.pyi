from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Camera(_message.Message):
    __slots__ = ("id", "room_id", "service_id", "dvr", "parent_camera_id", "stream_access_denied", "name", "stream_settings")
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SERVICE_TYPE_INFO: _ClassVar[Camera.ServiceType]
        RTSP_STREAM: _ClassVar[Camera.ServiceType]
        XMEYE: _ClassVar[Camera.ServiceType]
        HIKVISION: _ClassVar[Camera.ServiceType]
        DAHUA: _ClassVar[Camera.ServiceType]
        SAFIRE: _ClassVar[Camera.ServiceType]
        UNIVIEW: _ClassVar[Camera.ServiceType]
        IVIDEON: _ClassVar[Camera.ServiceType]
    NO_SERVICE_TYPE_INFO: Camera.ServiceType
    RTSP_STREAM: Camera.ServiceType
    XMEYE: Camera.ServiceType
    HIKVISION: Camera.ServiceType
    DAHUA: Camera.ServiceType
    SAFIRE: Camera.ServiceType
    UNIVIEW: Camera.ServiceType
    IVIDEON: Camera.ServiceType
    class StreamSettings(_message.Message):
        __slots__ = ("service_type", "result", "crc", "stream_data_url", "hikvision_or_safire_settings", "dahua_or_uniview_settings")
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        CRC_FIELD_NUMBER: _ClassVar[int]
        STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
        HIKVISION_OR_SAFIRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DAHUA_OR_UNIVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        service_type: Camera.ServiceType
        result: bool
        crc: int
        stream_data_url: str
        hikvision_or_safire_settings: Camera.HikvisionOrSafireSettings
        dahua_or_uniview_settings: Camera.DahuaOrUniviewSettings
        def __init__(self, service_type: _Optional[_Union[Camera.ServiceType, str]] = ..., result: bool = ..., crc: _Optional[int] = ..., stream_data_url: _Optional[str] = ..., hikvision_or_safire_settings: _Optional[_Union[Camera.HikvisionOrSafireSettings, _Mapping]] = ..., dahua_or_uniview_settings: _Optional[_Union[Camera.DahuaOrUniviewSettings, _Mapping]] = ...) -> None: ...
    class HikvisionOrSafireSettings(_message.Message):
        __slots__ = ("area_domain", "auth_domain", "authid", "expirydate", "no", "refreshtoken", "serial", "token", "verificationcode")
        AREA_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTHID_FIELD_NUMBER: _ClassVar[int]
        EXPIRYDATE_FIELD_NUMBER: _ClassVar[int]
        NO_FIELD_NUMBER: _ClassVar[int]
        REFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        VERIFICATIONCODE_FIELD_NUMBER: _ClassVar[int]
        area_domain: str
        auth_domain: str
        authid: str
        expirydate: _timestamp_pb2.Timestamp
        no: int
        refreshtoken: str
        serial: str
        token: str
        verificationcode: str
        def __init__(self, area_domain: _Optional[str] = ..., auth_domain: _Optional[str] = ..., authid: _Optional[str] = ..., expirydate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., no: _Optional[int] = ..., refreshtoken: _Optional[str] = ..., serial: _Optional[str] = ..., token: _Optional[str] = ..., verificationcode: _Optional[str] = ...) -> None: ...
    class DahuaOrUniviewSettings(_message.Message):
        __slots__ = ("login", "password", "serial")
        LOGIN_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        login: str
        password: str
        serial: str
        def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ..., serial: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DVR_FIELD_NUMBER: _ClassVar[int]
    PARENT_CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    service_id: str
    dvr: bool
    parent_camera_id: str
    stream_access_denied: bool
    name: _name_pb2.Name
    stream_settings: Camera.StreamSettings
    def __init__(self, id: _Optional[str] = ..., room_id: _Optional[str] = ..., service_id: _Optional[str] = ..., dvr: bool = ..., parent_camera_id: _Optional[str] = ..., stream_access_denied: bool = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., stream_settings: _Optional[_Union[Camera.StreamSettings, _Mapping]] = ...) -> None: ...
