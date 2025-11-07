from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandPhotoOnDemandModeRequest(_message.Message):
    __slots__ = ("hub_id", "photo_on_demand_mode_user", "photo_on_demand_mode_scenario")
    class PhotoOnDemandModeUser(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHOTO_ON_DEMAND_MODE_USER_UNSPECIFIED: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser]
        PHOTO_ON_DEMAND_MODE_USER_DISABLE: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser]
        PHOTO_ON_DEMAND_MODE_USER_ENABLE: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser]
    PHOTO_ON_DEMAND_MODE_USER_UNSPECIFIED: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser
    PHOTO_ON_DEMAND_MODE_USER_DISABLE: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser
    PHOTO_ON_DEMAND_MODE_USER_ENABLE: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser
    class PhotoOnDemandModeScenario(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHOTO_ON_DEMAND_MODE_SCENARIO_UNSPECIFIED: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario]
        PHOTO_ON_DEMAND_MODE_SCENARIO_DISABLE: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario]
        PHOTO_ON_DEMAND_MODE_SCENARIO_ENABLE: _ClassVar[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario]
    PHOTO_ON_DEMAND_MODE_SCENARIO_UNSPECIFIED: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario
    PHOTO_ON_DEMAND_MODE_SCENARIO_DISABLE: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario
    PHOTO_ON_DEMAND_MODE_SCENARIO_ENABLE: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_MODE_USER_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_MODE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    photo_on_demand_mode_user: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser
    photo_on_demand_mode_scenario: DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario
    def __init__(self, hub_id: _Optional[str] = ..., photo_on_demand_mode_user: _Optional[_Union[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeUser, str]] = ..., photo_on_demand_mode_scenario: _Optional[_Union[DeviceCommandPhotoOnDemandModeRequest.PhotoOnDemandModeScenario, str]] = ...) -> None: ...
