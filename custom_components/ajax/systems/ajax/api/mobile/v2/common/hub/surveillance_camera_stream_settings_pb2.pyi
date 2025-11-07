from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SurveillanceCameraStreamSettings(_message.Message):
    __slots__ = ("service_type", "crc", "stream_data_url", "hikvision_or_safire_settings", "dahua_or_uniview_settings")
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SERVICE_TYPE_INFO: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        RTSP_STREAM: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        XMEYE: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        HIKVISION: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        DAHUA: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        SAFIRE: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        UNIVIEW: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        IVIDEON: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
    NO_SERVICE_TYPE_INFO: SurveillanceCameraStreamSettings.ServiceType
    RTSP_STREAM: SurveillanceCameraStreamSettings.ServiceType
    XMEYE: SurveillanceCameraStreamSettings.ServiceType
    HIKVISION: SurveillanceCameraStreamSettings.ServiceType
    DAHUA: SurveillanceCameraStreamSettings.ServiceType
    SAFIRE: SurveillanceCameraStreamSettings.ServiceType
    UNIVIEW: SurveillanceCameraStreamSettings.ServiceType
    IVIDEON: SurveillanceCameraStreamSettings.ServiceType
    class HikvisionOrSafireSettings(_message.Message):
        __slots__ = ("area_domain", "auth_domain", "auth_id", "expire_date", "no", "refresh_token", "serial", "token", "verification_code")
        AREA_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_ID_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_DATE_FIELD_NUMBER: _ClassVar[int]
        NO_FIELD_NUMBER: _ClassVar[int]
        REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
        area_domain: str
        auth_domain: str
        auth_id: str
        expire_date: _timestamp_pb2.Timestamp
        no: int
        refresh_token: str
        serial: str
        token: str
        verification_code: str
        def __init__(self, area_domain: _Optional[str] = ..., auth_domain: _Optional[str] = ..., auth_id: _Optional[str] = ..., expire_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., no: _Optional[int] = ..., refresh_token: _Optional[str] = ..., serial: _Optional[str] = ..., token: _Optional[str] = ..., verification_code: _Optional[str] = ...) -> None: ...
    class DahuaOrUniviewSettings(_message.Message):
        __slots__ = ("login", "password", "serial", "no")
        LOGIN_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        NO_FIELD_NUMBER: _ClassVar[int]
        login: str
        password: str
        serial: str
        no: int
        def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ..., serial: _Optional[str] = ..., no: _Optional[int] = ...) -> None: ...
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    HIKVISION_OR_SAFIRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DAHUA_OR_UNIVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    service_type: SurveillanceCameraStreamSettings.ServiceType
    crc: int
    stream_data_url: str
    hikvision_or_safire_settings: SurveillanceCameraStreamSettings.HikvisionOrSafireSettings
    dahua_or_uniview_settings: SurveillanceCameraStreamSettings.DahuaOrUniviewSettings
    def __init__(self, service_type: _Optional[_Union[SurveillanceCameraStreamSettings.ServiceType, str]] = ..., crc: _Optional[int] = ..., stream_data_url: _Optional[str] = ..., hikvision_or_safire_settings: _Optional[_Union[SurveillanceCameraStreamSettings.HikvisionOrSafireSettings, _Mapping]] = ..., dahua_or_uniview_settings: _Optional[_Union[SurveillanceCameraStreamSettings.DahuaOrUniviewSettings, _Mapping]] = ...) -> None: ...
