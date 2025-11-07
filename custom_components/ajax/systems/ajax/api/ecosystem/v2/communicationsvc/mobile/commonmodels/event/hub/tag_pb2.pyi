from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtContactOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollerShutterAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollerShutterOffline(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShockDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TiltDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassByNumber(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassByRestoreTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FirmwareUpdateInProgress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Malfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObjectAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TurnOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisteredDeviceEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArcFaultDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Button1On(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Button2On(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHighDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHighUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayNotResponding(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByButton(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOverheatingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DataChannelCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedLeft(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedRight(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioUnsuccessfulWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemand(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandUnsuccessfulWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedLeft(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedRight(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoBySchedule(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScheduleUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CameraDirty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireAlarmMuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCoLevelDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCoLevelDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReserveBatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeChamberTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeChamberTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureHighEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureRiseDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureRiseDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireProtectMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCcoLevelDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CoTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CoTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Co2High(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Arm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmingIncomplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Disarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupDuressDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOnAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOnWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PasswordAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SecurityStateTransitionProgressUpdated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressAuthorization(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmDuringUpgradeAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CellularSignalLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DonorChosen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EthernetConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FactoryReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpAlarmConfirmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IncorrectCms(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationStart(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServerConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TargetChosen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TurnOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WalkTestStart(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsNoiseHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingsChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessDeniedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessDeniedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChimeActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChimeActivatedInGroup(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessGrantedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessGrantedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestoreDenied(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestoreRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessGrantedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessGrantedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BridgeNotResponding(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CardDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CodeDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeactivatedCardAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectorShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceMoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EthernetCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactLost(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDetectorShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FrontTamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GasDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GlassBreakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpLongPress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpShortPress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JewellerNoiseHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MedicalAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MonitoringStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class S1Alarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class S3Alarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScenarioNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackTamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperBoardDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineSabotage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FuseBreak(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimezoneChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusConflict(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndOfLife(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusPowerDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnetimeFullBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnetimeTamperBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LifeQualityMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByButton(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UndefinedValvePosition(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargerError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OverheatingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadBlocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadUnblockedByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadUnblockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeyarmBlocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeyarmUnblockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesBreak(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesConflict(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesUnregistered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReedSwitchBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccelerometerBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MagneticSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CalibrationRequired(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActivationRRUCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeactivationRRUCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImproperKeyarmUsage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoScenarioTriggered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeActivation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PeriodicTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecentClosing(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusPowerDisabledSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockViolation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SeismicAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TempSensorHighTemperature(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TempSensorLowTemperature(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocalExitError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AbortBurglary(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BurglaryCancel(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceSupervisionFailure(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SurveillanceScenarioExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeActivationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnvacatedPremises(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PasswordReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirection(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInForbiddenDirection(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirectionTimerStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirectionTimerActive(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AllowedDirectionTimerEnded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoArchiveExportPrepared(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoArchiveExportFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtSrcLowVoltage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSmokeDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallbackRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallNoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallMissed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallbackDenied(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmedGeneral(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmedDetailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnverifiedAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartBracketOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PirSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MicrowaveSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IncorrectDeviceInstallation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingSensorCalibrationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorDisabledByTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SipConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartHomeMotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumanDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CaseBreakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestDeviceDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SeismoSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VorfChannelCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoltSwitchContactOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BlockingElementOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveStuckPreventionNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveStuckPreventionExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineConnectError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandForDetectionArea(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandForDetectionAreaUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54FireAlarmReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceDoesNotRespond(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SounderFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VADFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatDetectionFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetectionFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedDuringTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryTemperatureOutOfRange(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitDelayComplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArmNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54Silence(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54Resound(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TriggerGroupNotArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiModuleUpgradeStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiModuleUpgradeFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubModuleUpgradeFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutPowerOverload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeWakeupSMS(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallTimeoutBSM(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallTimeoutBSM(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeWakeupByScheduled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutputFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54DeviceCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54FireAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54MedicalAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54PanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54GasDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54ExternalFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54LeakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactHardFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByAccessCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByAccessCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByAccessCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByAccessCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Evacuation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AudioRecord(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByFailSafe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByFailSafe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DelaysOverride(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SoftwareSystemFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemorySystemFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArcReportingOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDelaysOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDelaysOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireZoneTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsDeliveryFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmTemporaryBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDayAlarmTemporaryBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDayAlarmBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmBypassNotRestored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactResistanceFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmsToCmsDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmsToCmsEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultsToCmsDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultsToCmsEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectorVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDetectorVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ZoneTestSystemExit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsConnectionLost(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByKnob(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByTag(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByKeyboard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockModuleLockedAutomatically(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockDoorOpen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockDoorbellButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockKeyboardLocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModuleInsertedIntoDifferentLock(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialAddingError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialRemoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialRemovingError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockLockedWithConfirmation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialActivatedDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialActivationDeactivationError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54EthernetCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubEventTag(_message.Message):
    __slots__ = ("door_opened", "ext_contact_opened", "roller_shutter_alarm", "roller_shutter_offline", "shock_detected", "tilt_detected", "automatic_bypass_by_number", "automatic_bypass_by_restore_timer", "automatic_bypass_off", "power_low", "bypass_on", "device_communication_loss", "firmware_update_in_progress", "malfunction", "object_added", "tamper_bypass_on", "tamper_opened", "turn_off", "unregistered_device_event", "arc_fault_detected", "button_1_on", "button_2_on", "relay_current_high", "relay_current_high_device", "relay_current_high_user", "relay_current_low", "relay_current_ok", "relay_not_responding", "relay_off_bytimer", "relay_on", "relay_on_by_arming", "relay_on_by_button", "relay_on_by_device", "relay_on_by_disarming", "relay_on_by_scenario", "relay_on_by_user", "relay_overheating_detected", "relay_unable_to_switch_off", "relay_voltage_high", "relay_voltage_low", "relay_voltage_ok", "data_channel_communication_loss", "masking_detected", "masking_detected_left", "masking_detected_right", "motion_detected", "photo_by_scenario", "photo_by_scenario_unsuccessful", "photo_on_demand", "photo_on_demand_unsuccessful", "photo_on_demand_unsuccessful_with_name", "photo_on_demand_with_name", "motion_detected_left", "motion_detected_right", "photo_by_schedule", "photo_by_schedule_unsuccessful", "camera_dirty", "fire_alarm", "fire_alarm_muted", "high_co_level_detected", "high_co_level_detected_early_warning", "reserve_battery_low", "smoke_chamber_test_not_passed", "smoke_chamber_test_passed", "smoke_detected", "smoke_detected_early_warning", "temperature_high", "temperature_high_early_warning", "temperature_rise_detected", "temperature_rise_detected_early_warning", "fire_protect_malfunction", "heat_test_not_passed", "heat_test_passed", "high_cco_level_detected", "co_test_not_passed", "co_test_passed", "co_2_high", "humidity_high", "humidity_low", "humidity_ok", "temperature_low", "temperature_ok", "arm", "arm_attempt", "arming_incomplete", "arm_with_malfunctions", "disarm", "duress_disarm", "duress_night_mode_off", "group_arm", "group_arm_attempt", "group_arm_with_malfunctions", "group_disarm", "group_duress_disarm", "night_mode_off", "night_mode_on", "night_mode_on_attempt", "night_mode_on_with_malfunctions", "panic_button_pressed", "password_attempt", "security_state_transition_progress_updated", "duress_authorization", "arm_during_upgrade_attempt", "bus_short_circuit", "cellular_signal_low", "cms_connection_loss", "donor_chosen", "ethernet_connection_loss", "factory_reset", "gsm_connection_loss", "hold_up_alarm_confirmed", "incorrect_cms", "intrusion_alarm_confirmed", "migration_start", "server_connection_loss", "migration_ok", "migration_failed", "target_chosen", "turn_on", "walk_test_start", "wi_fi_connection_loss", "wings_noise_high", "settings_changed", "access_denied_to_company", "access_denied_to_pro", "access_request", "chime_activated", "chime_activated_in_group", "permanent_access_granted_to_company", "permanent_access_granted_to_pro", "photo_by_scenario_on", "photo_on_demand_on", "system_restored", "system_restore_denied", "system_restore_request", "temporary_access_granted_to_company", "temporary_access_granted_to_pro", "battery_disconnected", "bridge_not_responding", "CardDeactivated", "code_deactivated", "custom_event", "deactivated_card_attempt", "detector_short_circuit", "device_moved", "ethernet_communication_loss", "external_contact_lost", "external_contact_ok", "external_contact_short_circuit", "external_malfunction", "external_power_loss", "fire_detector_short_circuit", "front_tamper_opened", "gas_detected", "glass_break_detected", "hold_up_long_press", "hold_up_short_press", "intrusion_alarm", "jeweller_noise_high", "leak_detected", "medical_alarm", "monitoring_started", "permanent_access_request", "s_1_alarm", "s_3_alarm", "scenario_not_executed", "temporary_access_request", "battery_low", "back_tamper_opened", "short_circuit", "tamper_board_disconnect", "bus_voltage_high", "line_sabotage", "fuse_break", "timezone_changed", "ring_broken", "bus_conflict", "end_of_life", "dev_fw_upgrade_started", "dev_fw_upgrade_failed", "dev_fw_upgrade_finished", "bus_power_disabled", "onetime_full_bypass_on", "onetime_tamper_bypass_on", "life_quality_malfunction", "valve_opened_by_button", "valve_opened_by_scenario", "valve_opened_by_arming", "valve_opened_by_disarming", "valve_opened_by_device", "valve_opened_by_user", "undefined_valve_position", "battery_error", "restore_request", "bus_voltage_low", "charger_error", "overheating_detected", "keypad_blocked", "keypad_unblocked_by_timer", "keypad_unblocked_by_user", "relay_unable_to_switch_by_user", "relay_unable_to_switch_by_scenario", "relay_unable_to_switch_by_arming", "relay_unable_to_switch_by_disarming", "keyarm_blocked", "keyarm_unblocked_by_user", "buses_break", "buses_conflict", "buses_unregistered", "reed_switch_broken", "accelerometer_broken", "magnetic_sensor_broken", "calibration_required", "activation_rru_code", "deactivation_rru_code", "improper_keyarm_usage", "video_scenario_triggered", "battery_saving_mode_activation", "periodic_test", "exit_error", "recent_closing", "short_circuit_single_output", "bus_voltage_high_single_output", "bus_voltage_low_single_output", "bus_power_disabled_single_output", "lock_violation", "duress_code", "seismic_alarm", "temp_sensor_high_temperature", "temp_sensor_low_temperature", "local_exit_error", "abort_burglary", "burglary_cancel", "device_supervision_failure", "self_test_passed", "self_test_failed", "masking_detected_malfunction", "surveillance_scenario_executed", "battery_saving_mode_activation_failed", "photo_by_scenario_with_name", "photo_by_scenario_unsuccessful_with_name", "unvacated_premises", "password_reset", "motion_detected_in_allowed_direction", "motion_detected_in_forbidden_direction", "motion_detected_in_allowed_direction_timer_started", "motion_detected_in_allowed_direction_timer_active", "allowed_direction_timer_ended", "video_archive_export_prepared", "video_archive_export_failed", "ext_src_low_voltage", "jwl_antenna_disconnect", "jwl_antenna_connect", "wings_antenna_disconnect", "wings_antenna_connect", "gsm_antenna_disconnect", "gsm_antenna_connect", "jwl_antenna_damaged", "wings_antenna_damaged", "gsm_antenna_damaged", "csmoke_detected", "in_call", "out_call", "in_call_error", "out_call_error", "callback_request", "out_call_no_response", "out_call_timeout", "in_call_missed", "in_call_timeout", "callback_denied", "intrusion_alarm_confirmed_general", "intrusion_alarm_confirmed_detailed", "unverified_alarm", "smart_bracket_opened", "pir_sensor_broken", "microwave_sensor_broken", "incorrect_device_installation", "masking_sensor_broken", "masking_sensor_calibration_failed", "bukhoor_enabled", "bukhoor_disabled", "bukhoor_disabled_by_timeout", "sip_connection_loss", "smart_home_motion_detected", "human_detected", "pet_detected", "car_detected", "ring_button_pressed", "case_break_detected", "self_test_device_disconnected", "seismo_sensor_broken", "vorf_channel_communication_loss", "relay_short_circuit", "bolt_switch_contact_opened", "blocking_element_opened", "valve_stuck_prevention_not_executed", "valve_stuck_prevention_executed", "short_circuit_single_output1", "bus_voltage_high_single_output1", "bus_voltage_low_single_output1", "short_circuit_single_output2", "bus_voltage_high_single_output2", "bus_voltage_low_single_output2", "line_connect_error", "photo_on_demand_for_detection_area", "photo_on_demand_for_detection_area_unsuccessful", "en54_fire_alarm_reset", "device_does_not_respond", "sounder_fault", "vad_fault", "heat_detection_fault", "smoke_detection_fault", "motion_detected_during_test", "alarm_annunciation_test", "battery_temperature_out_of_range", "exit_delay_complete", "group_auto_arm", "group_auto_arm_with_malfunctions", "group_auto_arm_attempt", "group_auto_disarm", "auto_arm_not_executed", "auto_arm", "auto_arm_with_malfunctions", "auto_disarm", "auto_self_test_passed", "auto_self_test_failed", "auto_self_test_error", "en54_silence", "en54_resound", "trigger_group_not_armed", "alarm_annunciation_test_by_user", "alarm_annunciation_test_by_card", "alarm_annunciation_test_by_code", "wifi_module_upgrade_started", "wifi_module_upgrade_failed", "hub_module_upgrade_finished", "out_power_overload", "battery_saving_mode_wakeup_sms", "endpoint_disabled_by_user", "endpoint_disabled_by_code", "endpoint_disabled_by_card", "in_call_timeout_bsm", "out_call_timeout_bsm", "battery_saving_mode_wakeup_by_scheduled", "output_fault", "en54_tamper_opened", "en54_power_low", "en54_device_communication_loss", "en54_fire_alarm", "en54_medical_alarm", "en54_panic_button_pressed", "en54_gas_detected", "en54_external_fault", "en54_leak_detected", "external_contact_hard_fault", "fault_alarm", "relay_on_by_access_code", "relay_on_by_access_card", "relay_on_by_timer", "relay_off_by_user", "relay_off_by_access_code", "relay_off_by_access_card", "evacuation", "custom_alarm", "audio_record", "relay_on_by_fail_safe", "relay_off_by_fail_safe", "delays_override", "software_system_fault", "memory_system_fault", "arc_reporting_off", "fire_delays_on", "fire_delays_off", "battery_fault", "fire_zone_test", "cms_delivery_failed", "day_alarm_temporary_bypass_activated", "duress_day_alarm_temporary_bypass_activated", "day_alarm_bypass_activated", "duress_day_alarm_bypass_activated", "day_alarm_bypass_not_restored", "external_contact_resistance_fault", "alarms_to_cms_disabled", "alarms_to_cms_enabled", "faults_to_cms_disabled", "faults_to_cms_enabled", "detector_voltage_low", "fire_detector_voltage_low", "zone_test_system_exit", "cms_connection_lost", "smart_lock_unlocked_by_knob", "smart_lock_unlocked_by_code", "smart_lock_unlocked_by_tag", "smart_lock_unlocked_by_user", "smart_lock_unlocked_by_scenario", "smart_lock_unlocked_by_arm", "smart_lock_unlocked_by_disarm", "smart_lock_unlocked_by_keyboard", "smart_lock_module_locked_automatically", "smart_lock_door_open", "smart_lock_doorbell_button_pressed", "smart_lock_keyboard_locked", "module_inserted_into_different_lock", "smart_lock_credential_added", "smart_lock_credential_adding_error", "smart_lock_credential_removed", "smart_lock_credential_removing_error", "smart_lock_locked_with_confirmation", "smart_lock_credential_activated_deactivated", "smart_lock_credential_activation_deactivation_error", "en54_external_power_loss", "en54_ethernet_communication_loss")
    DOOR_OPENED_FIELD_NUMBER: _ClassVar[int]
    EXT_CONTACT_OPENED_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_ALARM_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    SHOCK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TILT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_BY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_BY_RESTORE_TIMER_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_OFF_FIELD_NUMBER: _ClassVar[int]
    POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPDATE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ADDED_FIELD_NUMBER: _ClassVar[int]
    TAMPER_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    TURN_OFF_FIELD_NUMBER: _ClassVar[int]
    UNREGISTERED_DEVICE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ARC_FAULT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BUTTON_1_ON_FIELD_NUMBER: _ClassVar[int]
    BUTTON_2_ON_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_DEVICE_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_LOW_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_OK_FIELD_NUMBER: _ClassVar[int]
    RELAY_NOT_RESPONDING_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BYTIMER_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_BUTTON_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_DEVICE_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OVERHEATING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_OFF_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_HIGH_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_OK_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_LEFT_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_UNSUCCESSFUL_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_LEFT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_RIGHT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCHEDULE_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_DIRTY_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_MUTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CO_LEVEL_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    RESERVE_BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CHAMBER_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CHAMBER_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_HIGH_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_HIGH_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_RISE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_RISE_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    FIRE_PROTECT_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    HEAT_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    HEAT_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CCO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CO_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    CO_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    CO_2_HIGH_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_HIGH_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_LOW_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_OK_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_LOW_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_OK_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ARMING_INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    DISARM_FIELD_NUMBER: _ClassVar[int]
    DURESS_DISARM_FIELD_NUMBER: _ClassVar[int]
    DURESS_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_DISARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_DURESS_DISARM_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STATE_TRANSITION_PROGRESS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    ARM_DURING_UPGRADE_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    BUS_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_SIGNAL_LOW_FIELD_NUMBER: _ClassVar[int]
    CMS_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    DONOR_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    FACTORY_RESET_FIELD_NUMBER: _ClassVar[int]
    GSM_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_ALARM_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    INCORRECT_CMS_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_START_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_OK_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    TURN_ON_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_START_FIELD_NUMBER: _ClassVar[int]
    WI_FI_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    WINGS_NOISE_HIGH_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DENIED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DENIED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHIME_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CHIME_ACTIVATED_IN_GROUP_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_GRANTED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_GRANTED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_ON_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_ON_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORED_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORE_DENIED_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_GRANTED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_GRANTED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    BATTERY_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NOT_RESPONDING_FIELD_NUMBER: _ClassVar[int]
    CARDDEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CODE_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EVENT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_CARD_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MOVED_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_LOST_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_OK_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    FIRE_DETECTOR_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    FRONT_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    GAS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_LONG_PRESS_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_SHORT_PRESS_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_FIELD_NUMBER: _ClassVar[int]
    JEWELLER_NOISE_HIGH_FIELD_NUMBER: _ClassVar[int]
    LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STARTED_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    S_1_ALARM_FIELD_NUMBER: _ClassVar[int]
    S_3_ALARM_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    BACK_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    TAMPER_BOARD_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_FIELD_NUMBER: _ClassVar[int]
    LINE_SABOTAGE_FIELD_NUMBER: _ClassVar[int]
    FUSE_BREAK_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    RING_BROKEN_FIELD_NUMBER: _ClassVar[int]
    BUS_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_STARTED_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_FAILED_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    BUS_POWER_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ONETIME_FULL_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    ONETIME_TAMPER_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    LIFE_QUALITY_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_BUTTON_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    UNDEFINED_VALVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    BATTERY_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    CHARGER_ERROR_FIELD_NUMBER: _ClassVar[int]
    OVERHEATING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_UNBLOCKED_BY_TIMER_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_UNBLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    KEYARM_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEYARM_UNBLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    BUSES_BREAK_FIELD_NUMBER: _ClassVar[int]
    BUSES_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    BUSES_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    REED_SWITCH_BROKEN_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MAGNETIC_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_RRU_CODE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATION_RRU_CODE_FIELD_NUMBER: _ClassVar[int]
    IMPROPER_KEYARM_USAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TEST_FIELD_NUMBER: _ClassVar[int]
    EXIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    RECENT_CLOSING_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_POWER_DISABLED_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LOCK_VIOLATION_FIELD_NUMBER: _ClassVar[int]
    DURESS_CODE_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_ALARM_FIELD_NUMBER: _ClassVar[int]
    TEMP_SENSOR_HIGH_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TEMP_SENSOR_LOW_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_BURGLARY_FIELD_NUMBER: _ClassVar[int]
    BURGLARY_CANCEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUPERVISION_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_FAILED_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    SURVEILLANCE_SCENARIO_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_ACTIVATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_UNSUCCESSFUL_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    UNVACATED_PREMISES_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_FORBIDDEN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_TIMER_STARTED_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_TIMER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DIRECTION_TIMER_ENDED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_EXPORT_PREPARED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_EXPORT_FAILED_FIELD_NUMBER: _ClassVar[int]
    EXT_SRC_LOW_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    CSMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_ERROR_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_ERROR_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_NO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_MISSED_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DENIED_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_GENERAL_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_DETAILED_FIELD_NUMBER: _ClassVar[int]
    UNVERIFIED_ALARM_FIELD_NUMBER: _ClassVar[int]
    SMART_BRACKET_OPENED_FIELD_NUMBER: _ClassVar[int]
    PIR_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MICROWAVE_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    INCORRECT_DEVICE_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_CALIBRATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_DISABLED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_DISABLED_BY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SIP_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    SMART_HOME_MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HUMAN_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PET_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CAR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    CASE_BREAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_DEVICE_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    SEISMO_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    VORF_CHANNEL_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    RELAY_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    BOLT_SWITCH_CONTACT_OPENED_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_ELEMENT_OPENED_FIELD_NUMBER: _ClassVar[int]
    VALVE_STUCK_PREVENTION_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    VALVE_STUCK_PREVENTION_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    LINE_CONNECT_ERROR_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FOR_DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FOR_DETECTION_AREA_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_ALARM_RESET_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DOES_NOT_RESPOND_FIELD_NUMBER: _ClassVar[int]
    SOUNDER_FAULT_FIELD_NUMBER: _ClassVar[int]
    VAD_FAULT_FIELD_NUMBER: _ClassVar[int]
    HEAT_DETECTION_FAULT_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTION_FAULT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_DURING_TEST_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_OUT_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
    EXIT_DELAY_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_FAILED_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_ERROR_FIELD_NUMBER: _ClassVar[int]
    EN54_SILENCE_FIELD_NUMBER: _ClassVar[int]
    EN54_RESOUND_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_NOT_ARMED_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_USER_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_CARD_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    WIFI_MODULE_UPGRADE_STARTED_FIELD_NUMBER: _ClassVar[int]
    WIFI_MODULE_UPGRADE_FAILED_FIELD_NUMBER: _ClassVar[int]
    HUB_MODULE_UPGRADE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    OUT_POWER_OVERLOAD_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_WAKEUP_SMS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_CARD_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_TIMEOUT_BSM_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_TIMEOUT_BSM_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_WAKEUP_BY_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FAULT_FIELD_NUMBER: _ClassVar[int]
    EN54_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    EN54_POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    EN54_DEVICE_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    EN54_MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    EN54_PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    EN54_GAS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EN54_EXTERNAL_FAULT_FIELD_NUMBER: _ClassVar[int]
    EN54_LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_HARD_FAULT_FIELD_NUMBER: _ClassVar[int]
    FAULT_ALARM_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_TIMER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    EVACUATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_FIELD_NUMBER: _ClassVar[int]
    AUDIO_RECORD_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_FAIL_SAFE_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_FAIL_SAFE_FIELD_NUMBER: _ClassVar[int]
    DELAYS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_SYSTEM_FAULT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SYSTEM_FAULT_FIELD_NUMBER: _ClassVar[int]
    ARC_REPORTING_OFF_FIELD_NUMBER: _ClassVar[int]
    FIRE_DELAYS_ON_FIELD_NUMBER: _ClassVar[int]
    FIRE_DELAYS_OFF_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FAULT_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    CMS_DELIVERY_FAILED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_TEMPORARY_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_DAY_ALARM_TEMPORARY_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_DAY_ALARM_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_BYPASS_NOT_RESTORED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_RESISTANCE_FAULT_FIELD_NUMBER: _ClassVar[int]
    ALARMS_TO_CMS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALARMS_TO_CMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAULTS_TO_CMS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    FAULTS_TO_CMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    FIRE_DETECTOR_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    ZONE_TEST_SYSTEM_EXIT_FIELD_NUMBER: _ClassVar[int]
    CMS_CONNECTION_LOST_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_KNOB_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_TAG_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_ARM_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_DISARM_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_MODULE_LOCKED_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_DOOR_OPEN_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_DOORBELL_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_KEYBOARD_LOCKED_FIELD_NUMBER: _ClassVar[int]
    MODULE_INSERTED_INTO_DIFFERENT_LOCK_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ADDED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ADDING_ERROR_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_REMOVED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_REMOVING_ERROR_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_LOCKED_WITH_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ACTIVATED_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ACTIVATION_DEACTIVATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    EN54_EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    EN54_ETHERNET_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    door_opened: DoorOpened
    ext_contact_opened: ExtContactOpened
    roller_shutter_alarm: RollerShutterAlarm
    roller_shutter_offline: RollerShutterOffline
    shock_detected: ShockDetected
    tilt_detected: TiltDetected
    automatic_bypass_by_number: AutomaticBypassByNumber
    automatic_bypass_by_restore_timer: AutomaticBypassByRestoreTimer
    automatic_bypass_off: AutomaticBypassOff
    power_low: PowerLow
    bypass_on: BypassOn
    device_communication_loss: DeviceCommunicationLoss
    firmware_update_in_progress: FirmwareUpdateInProgress
    malfunction: Malfunction
    object_added: ObjectAdded
    tamper_bypass_on: TamperBypassOn
    tamper_opened: TamperOpened
    turn_off: TurnOff
    unregistered_device_event: UnregisteredDeviceEvent
    arc_fault_detected: ArcFaultDetected
    button_1_on: Button1On
    button_2_on: Button2On
    relay_current_high: RelayCurrentHigh
    relay_current_high_device: RelayCurrentHighDevice
    relay_current_high_user: RelayCurrentHighUser
    relay_current_low: RelayCurrentLow
    relay_current_ok: RelayCurrentOk
    relay_not_responding: RelayNotResponding
    relay_off_bytimer: RelayOffByTimer
    relay_on: RelayOn
    relay_on_by_arming: RelayOnByArming
    relay_on_by_button: RelayOnByButton
    relay_on_by_device: RelayOnByDevice
    relay_on_by_disarming: RelayOnByDisarming
    relay_on_by_scenario: RelayOnByScenario
    relay_on_by_user: RelayOnByUser
    relay_overheating_detected: RelayOverheatingDetected
    relay_unable_to_switch_off: RelayUnableToSwitchOff
    relay_voltage_high: RelayVoltageHigh
    relay_voltage_low: RelayVoltageLow
    relay_voltage_ok: RelayVoltageOk
    data_channel_communication_loss: DataChannelCommunicationLoss
    masking_detected: MaskingDetected
    masking_detected_left: MaskingDetectedLeft
    masking_detected_right: MaskingDetectedRight
    motion_detected: MotionDetected
    photo_by_scenario: PhotoByScenario
    photo_by_scenario_unsuccessful: PhotoByScenarioUnsuccessful
    photo_on_demand: PhotoOnDemand
    photo_on_demand_unsuccessful: PhotoOnDemandUnsuccessful
    photo_on_demand_unsuccessful_with_name: PhotoOnDemandUnsuccessfulWithName
    photo_on_demand_with_name: PhotoOnDemandWithName
    motion_detected_left: MotionDetectedLeft
    motion_detected_right: MotionDetectedRight
    photo_by_schedule: PhotoBySchedule
    photo_by_schedule_unsuccessful: PhotoByScheduleUnsuccessful
    camera_dirty: CameraDirty
    fire_alarm: FireAlarm
    fire_alarm_muted: FireAlarmMuted
    high_co_level_detected: HighCoLevelDetected
    high_co_level_detected_early_warning: HighCoLevelDetectedEarlyWarning
    reserve_battery_low: ReserveBatteryLow
    smoke_chamber_test_not_passed: SmokeChamberTestNotPassed
    smoke_chamber_test_passed: SmokeChamberTestPassed
    smoke_detected: SmokeDetected
    smoke_detected_early_warning: SmokeDetectedEarlyWarning
    temperature_high: TemperatureHigh
    temperature_high_early_warning: TemperatureHighEarlyWarning
    temperature_rise_detected: TemperatureRiseDetected
    temperature_rise_detected_early_warning: TemperatureRiseDetectedEarlyWarning
    fire_protect_malfunction: FireProtectMalfunction
    heat_test_not_passed: HeatTestNotPassed
    heat_test_passed: HeatTestPassed
    high_cco_level_detected: HighCcoLevelDetected
    co_test_not_passed: CoTestNotPassed
    co_test_passed: CoTestPassed
    co_2_high: Co2High
    humidity_high: HumidityHigh
    humidity_low: HumidityLow
    humidity_ok: HumidityOk
    temperature_low: TemperatureLow
    temperature_ok: TemperatureOk
    arm: Arm
    arm_attempt: ArmAttempt
    arming_incomplete: ArmingIncomplete
    arm_with_malfunctions: ArmWithMalfunctions
    disarm: Disarm
    duress_disarm: DuressDisarm
    duress_night_mode_off: DuressNightModeOff
    group_arm: GroupArm
    group_arm_attempt: GroupArmAttempt
    group_arm_with_malfunctions: GroupArmWithMalfunctions
    group_disarm: GroupDisarm
    group_duress_disarm: GroupDuressDisarm
    night_mode_off: NightModeOff
    night_mode_on: NightModeOn
    night_mode_on_attempt: NightModeOnAttempt
    night_mode_on_with_malfunctions: NightModeOnWithMalfunctions
    panic_button_pressed: PanicButtonPressed
    password_attempt: PasswordAttempt
    security_state_transition_progress_updated: SecurityStateTransitionProgressUpdated
    duress_authorization: DuressAuthorization
    arm_during_upgrade_attempt: ArmDuringUpgradeAttempt
    bus_short_circuit: BusShortCircuit
    cellular_signal_low: CellularSignalLow
    cms_connection_loss: CmsConnectionLoss
    donor_chosen: DonorChosen
    ethernet_connection_loss: EthernetConnectionLoss
    factory_reset: FactoryReset
    gsm_connection_loss: GsmConnectionLoss
    hold_up_alarm_confirmed: HoldUpAlarmConfirmed
    incorrect_cms: IncorrectCms
    intrusion_alarm_confirmed: IntrusionAlarmConfirmed
    migration_start: MigrationStart
    server_connection_loss: ServerConnectionLoss
    migration_ok: MigrationOk
    migration_failed: MigrationFailed
    target_chosen: TargetChosen
    turn_on: TurnOn
    walk_test_start: WalkTestStart
    wi_fi_connection_loss: WiFiConnectionLoss
    wings_noise_high: WingsNoiseHigh
    settings_changed: SettingsChanged
    access_denied_to_company: AccessDeniedToCompany
    access_denied_to_pro: AccessDeniedToPro
    access_request: AccessRequest
    chime_activated: ChimeActivated
    chime_activated_in_group: ChimeActivatedInGroup
    permanent_access_granted_to_company: PermanentAccessGrantedToCompany
    permanent_access_granted_to_pro: PermanentAccessGrantedToPro
    photo_by_scenario_on: PhotoByScenarioOn
    photo_on_demand_on: PhotoOnDemandOn
    system_restored: SystemRestored
    system_restore_denied: SystemRestoreDenied
    system_restore_request: SystemRestoreRequest
    temporary_access_granted_to_company: TemporaryAccessGrantedToCompany
    temporary_access_granted_to_pro: TemporaryAccessGrantedToPro
    battery_disconnected: BatteryDisconnected
    bridge_not_responding: BridgeNotResponding
    CardDeactivated: CardDeactivated
    code_deactivated: CodeDeactivated
    custom_event: CustomEvent
    deactivated_card_attempt: DeactivatedCardAttempt
    detector_short_circuit: DetectorShortCircuit
    device_moved: DeviceMoved
    ethernet_communication_loss: EthernetCommunicationLoss
    external_contact_lost: ExternalContactLost
    external_contact_ok: ExternalContactOk
    external_contact_short_circuit: ExternalContactShortCircuit
    external_malfunction: ExternalMalfunction
    external_power_loss: ExternalPowerLoss
    fire_detector_short_circuit: FireDetectorShortCircuit
    front_tamper_opened: FrontTamperOpened
    gas_detected: GasDetected
    glass_break_detected: GlassBreakDetected
    hold_up_long_press: HoldUpLongPress
    hold_up_short_press: HoldUpShortPress
    intrusion_alarm: IntrusionAlarm
    jeweller_noise_high: JewellerNoiseHigh
    leak_detected: LeakDetected
    medical_alarm: MedicalAlarm
    monitoring_started: MonitoringStarted
    permanent_access_request: PermanentAccessRequest
    s_1_alarm: S1Alarm
    s_3_alarm: S3Alarm
    scenario_not_executed: ScenarioNotExecuted
    temporary_access_request: TemporaryAccessRequest
    battery_low: BatteryLow
    back_tamper_opened: BackTamperOpened
    short_circuit: ShortCircuit
    tamper_board_disconnect: TamperBoardDisconnect
    bus_voltage_high: BusVoltageHigh
    line_sabotage: LineSabotage
    fuse_break: FuseBreak
    timezone_changed: TimezoneChanged
    ring_broken: RingBroken
    bus_conflict: BusConflict
    end_of_life: EndOfLife
    dev_fw_upgrade_started: DevFWUpgradeStarted
    dev_fw_upgrade_failed: DevFWUpgradeFailed
    dev_fw_upgrade_finished: DevFWUpgradeFinished
    bus_power_disabled: BusPowerDisabled
    onetime_full_bypass_on: OnetimeFullBypassOn
    onetime_tamper_bypass_on: OnetimeTamperBypassOn
    life_quality_malfunction: LifeQualityMalfunction
    valve_opened_by_button: ValveOpenedByButton
    valve_opened_by_scenario: ValveOpenedByScenario
    valve_opened_by_arming: ValveOpenedByArming
    valve_opened_by_disarming: ValveOpenedByDisarming
    valve_opened_by_device: ValveOpenedByDevice
    valve_opened_by_user: ValveOpenedByUser
    undefined_valve_position: UndefinedValvePosition
    battery_error: BatteryError
    restore_request: RestoreRequest
    bus_voltage_low: BusVoltageLow
    charger_error: ChargerError
    overheating_detected: OverheatingDetected
    keypad_blocked: KeypadBlocked
    keypad_unblocked_by_timer: KeypadUnblockedByTimer
    keypad_unblocked_by_user: KeypadUnblockedByUser
    relay_unable_to_switch_by_user: RelayUnableToSwitchByUser
    relay_unable_to_switch_by_scenario: RelayUnableToSwitchByScenario
    relay_unable_to_switch_by_arming: RelayUnableToSwitchByArming
    relay_unable_to_switch_by_disarming: RelayUnableToSwitchByDisarming
    keyarm_blocked: KeyarmBlocked
    keyarm_unblocked_by_user: KeyarmUnblockedByUser
    buses_break: BusesBreak
    buses_conflict: BusesConflict
    buses_unregistered: BusesUnregistered
    reed_switch_broken: ReedSwitchBroken
    accelerometer_broken: AccelerometerBroken
    magnetic_sensor_broken: MagneticSensorBroken
    calibration_required: CalibrationRequired
    activation_rru_code: ActivationRRUCode
    deactivation_rru_code: DeactivationRRUCode
    improper_keyarm_usage: ImproperKeyarmUsage
    video_scenario_triggered: VideoScenarioTriggered
    battery_saving_mode_activation: BatterySavingModeActivation
    periodic_test: PeriodicTest
    exit_error: ExitError
    recent_closing: RecentClosing
    short_circuit_single_output: ShortCircuitSingleOutput
    bus_voltage_high_single_output: BusVoltageHighSingleOutput
    bus_voltage_low_single_output: BusVoltageLowSingleOutput
    bus_power_disabled_single_output: BusPowerDisabledSingleOutput
    lock_violation: LockViolation
    duress_code: DuressCode
    seismic_alarm: SeismicAlarm
    temp_sensor_high_temperature: TempSensorHighTemperature
    temp_sensor_low_temperature: TempSensorLowTemperature
    local_exit_error: LocalExitError
    abort_burglary: AbortBurglary
    burglary_cancel: BurglaryCancel
    device_supervision_failure: DeviceSupervisionFailure
    self_test_passed: SelfTestPassed
    self_test_failed: SelfTestFailed
    masking_detected_malfunction: MaskingDetectedMalfunction
    surveillance_scenario_executed: SurveillanceScenarioExecuted
    battery_saving_mode_activation_failed: BatterySavingModeActivationFailed
    photo_by_scenario_with_name: PhotoByScenarioWithName
    photo_by_scenario_unsuccessful_with_name: PhotoByScenarioUnsuccessfulWithName
    unvacated_premises: UnvacatedPremises
    password_reset: PasswordReset
    motion_detected_in_allowed_direction: MotionDetectedInAllowedDirection
    motion_detected_in_forbidden_direction: MotionDetectedInForbiddenDirection
    motion_detected_in_allowed_direction_timer_started: MotionDetectedInAllowedDirectionTimerStarted
    motion_detected_in_allowed_direction_timer_active: MotionDetectedInAllowedDirectionTimerActive
    allowed_direction_timer_ended: AllowedDirectionTimerEnded
    video_archive_export_prepared: VideoArchiveExportPrepared
    video_archive_export_failed: VideoArchiveExportFailed
    ext_src_low_voltage: ExtSrcLowVoltage
    jwl_antenna_disconnect: JwlAntennaDisconnect
    jwl_antenna_connect: JwlAntennaConnect
    wings_antenna_disconnect: WingsAntennaDisconnect
    wings_antenna_connect: WingsAntennaConnect
    gsm_antenna_disconnect: GsmAntennaDisconnect
    gsm_antenna_connect: GsmAntennaConnect
    jwl_antenna_damaged: JwlAntennaDamaged
    wings_antenna_damaged: WingsAntennaDamaged
    gsm_antenna_damaged: GsmAntennaDamaged
    csmoke_detected: CSmokeDetected
    in_call: InCall
    out_call: OutCall
    in_call_error: InCallError
    out_call_error: OutCallError
    callback_request: CallbackRequest
    out_call_no_response: OutCallNoResponse
    out_call_timeout: OutCallTimeout
    in_call_missed: InCallMissed
    in_call_timeout: InCallTimeout
    callback_denied: CallbackDenied
    intrusion_alarm_confirmed_general: IntrusionAlarmConfirmedGeneral
    intrusion_alarm_confirmed_detailed: IntrusionAlarmConfirmedDetailed
    unverified_alarm: UnverifiedAlarm
    smart_bracket_opened: SmartBracketOpened
    pir_sensor_broken: PirSensorBroken
    microwave_sensor_broken: MicrowaveSensorBroken
    incorrect_device_installation: IncorrectDeviceInstallation
    masking_sensor_broken: MaskingSensorBroken
    masking_sensor_calibration_failed: MaskingSensorCalibrationFailed
    bukhoor_enabled: BukhoorEnabled
    bukhoor_disabled: BukhoorDisabled
    bukhoor_disabled_by_timeout: BukhoorDisabledByTimeout
    sip_connection_loss: SipConnectionLoss
    smart_home_motion_detected: SmartHomeMotionDetected
    human_detected: HumanDetected
    pet_detected: PetDetected
    car_detected: CarDetected
    ring_button_pressed: RingButtonPressed
    case_break_detected: CaseBreakDetected
    self_test_device_disconnected: SelfTestDeviceDisconnected
    seismo_sensor_broken: SeismoSensorBroken
    vorf_channel_communication_loss: VorfChannelCommunicationLoss
    relay_short_circuit: RelayShortCircuit
    bolt_switch_contact_opened: BoltSwitchContactOpened
    blocking_element_opened: BlockingElementOpened
    valve_stuck_prevention_not_executed: ValveStuckPreventionNotExecuted
    valve_stuck_prevention_executed: ValveStuckPreventionExecuted
    short_circuit_single_output1: ShortCircuitSingleOutput1
    bus_voltage_high_single_output1: BusVoltageHighSingleOutput1
    bus_voltage_low_single_output1: BusVoltageLowSingleOutput1
    short_circuit_single_output2: ShortCircuitSingleOutput2
    bus_voltage_high_single_output2: BusVoltageHighSingleOutput2
    bus_voltage_low_single_output2: BusVoltageLowSingleOutput2
    line_connect_error: LineConnectError
    photo_on_demand_for_detection_area: PhotoOnDemandForDetectionArea
    photo_on_demand_for_detection_area_unsuccessful: PhotoOnDemandForDetectionAreaUnsuccessful
    en54_fire_alarm_reset: EN54FireAlarmReset
    device_does_not_respond: DeviceDoesNotRespond
    sounder_fault: SounderFault
    vad_fault: VADFault
    heat_detection_fault: HeatDetectionFault
    smoke_detection_fault: SmokeDetectionFault
    motion_detected_during_test: MotionDetectedDuringTest
    alarm_annunciation_test: AlarmAnnunciationTest
    battery_temperature_out_of_range: BatteryTemperatureOutOfRange
    exit_delay_complete: ExitDelayComplete
    group_auto_arm: GroupAutoArm
    group_auto_arm_with_malfunctions: GroupAutoArmWithMalfunctions
    group_auto_arm_attempt: GroupAutoArmAttempt
    group_auto_disarm: GroupAutoDisarm
    auto_arm_not_executed: AutoArmNotExecuted
    auto_arm: AutoArm
    auto_arm_with_malfunctions: AutoArmWithMalfunctions
    auto_disarm: AutoDisarm
    auto_self_test_passed: AutoSelfTestPassed
    auto_self_test_failed: AutoSelfTestFailed
    auto_self_test_error: AutoSelfTestError
    en54_silence: EN54Silence
    en54_resound: EN54Resound
    trigger_group_not_armed: TriggerGroupNotArmed
    alarm_annunciation_test_by_user: AlarmAnnunciationTestByUser
    alarm_annunciation_test_by_card: AlarmAnnunciationTestByCard
    alarm_annunciation_test_by_code: AlarmAnnunciationTestByCode
    wifi_module_upgrade_started: WiFiModuleUpgradeStarted
    wifi_module_upgrade_failed: WiFiModuleUpgradeFailed
    hub_module_upgrade_finished: HubModuleUpgradeFinished
    out_power_overload: OutPowerOverload
    battery_saving_mode_wakeup_sms: BatterySavingModeWakeupSMS
    endpoint_disabled_by_user: EndpointDisabledByUser
    endpoint_disabled_by_code: EndpointDisabledByCode
    endpoint_disabled_by_card: EndpointDisabledByCard
    in_call_timeout_bsm: InCallTimeoutBSM
    out_call_timeout_bsm: OutCallTimeoutBSM
    battery_saving_mode_wakeup_by_scheduled: BatterySavingModeWakeupByScheduled
    output_fault: OutputFault
    en54_tamper_opened: EN54TamperOpened
    en54_power_low: EN54PowerLow
    en54_device_communication_loss: EN54DeviceCommunicationLoss
    en54_fire_alarm: EN54FireAlarm
    en54_medical_alarm: EN54MedicalAlarm
    en54_panic_button_pressed: EN54PanicButtonPressed
    en54_gas_detected: EN54GasDetected
    en54_external_fault: EN54ExternalFault
    en54_leak_detected: EN54LeakDetected
    external_contact_hard_fault: ExternalContactHardFault
    fault_alarm: FaultAlarm
    relay_on_by_access_code: RelayOnByAccessCode
    relay_on_by_access_card: RelayOnByAccessCard
    relay_on_by_timer: RelayOnByTimer
    relay_off_by_user: RelayOffByUser
    relay_off_by_access_code: RelayOffByAccessCode
    relay_off_by_access_card: RelayOffByAccessCard
    evacuation: Evacuation
    custom_alarm: CustomAlarm
    audio_record: AudioRecord
    relay_on_by_fail_safe: RelayOnByFailSafe
    relay_off_by_fail_safe: RelayOffByFailSafe
    delays_override: DelaysOverride
    software_system_fault: SoftwareSystemFault
    memory_system_fault: MemorySystemFault
    arc_reporting_off: ArcReportingOff
    fire_delays_on: FireDelaysOn
    fire_delays_off: FireDelaysOff
    battery_fault: BatteryFault
    fire_zone_test: FireZoneTest
    cms_delivery_failed: CmsDeliveryFailed
    day_alarm_temporary_bypass_activated: DayAlarmTemporaryBypassActivated
    duress_day_alarm_temporary_bypass_activated: DuressDayAlarmTemporaryBypassActivated
    day_alarm_bypass_activated: DayAlarmBypassActivated
    duress_day_alarm_bypass_activated: DuressDayAlarmBypassActivated
    day_alarm_bypass_not_restored: DayAlarmBypassNotRestored
    external_contact_resistance_fault: ExternalContactResistanceFault
    alarms_to_cms_disabled: AlarmsToCmsDisabled
    alarms_to_cms_enabled: AlarmsToCmsEnabled
    faults_to_cms_disabled: FaultsToCmsDisabled
    faults_to_cms_enabled: FaultsToCmsEnabled
    detector_voltage_low: DetectorVoltageLow
    fire_detector_voltage_low: FireDetectorVoltageLow
    zone_test_system_exit: ZoneTestSystemExit
    cms_connection_lost: CmsConnectionLost
    smart_lock_unlocked_by_knob: SmartLockUnlockedByKnob
    smart_lock_unlocked_by_code: SmartLockUnlockedByCode
    smart_lock_unlocked_by_tag: SmartLockUnlockedByTag
    smart_lock_unlocked_by_user: SmartLockUnlockedByUser
    smart_lock_unlocked_by_scenario: SmartLockUnlockedByScenario
    smart_lock_unlocked_by_arm: SmartLockUnlockedByArm
    smart_lock_unlocked_by_disarm: SmartLockUnlockedByDisarm
    smart_lock_unlocked_by_keyboard: SmartLockUnlockedByKeyboard
    smart_lock_module_locked_automatically: SmartLockModuleLockedAutomatically
    smart_lock_door_open: SmartLockDoorOpen
    smart_lock_doorbell_button_pressed: SmartLockDoorbellButtonPressed
    smart_lock_keyboard_locked: SmartLockKeyboardLocked
    module_inserted_into_different_lock: ModuleInsertedIntoDifferentLock
    smart_lock_credential_added: SmartLockCredentialAdded
    smart_lock_credential_adding_error: SmartLockCredentialAddingError
    smart_lock_credential_removed: SmartLockCredentialRemoved
    smart_lock_credential_removing_error: SmartLockCredentialRemovingError
    smart_lock_locked_with_confirmation: SmartLockLockedWithConfirmation
    smart_lock_credential_activated_deactivated: SmartLockCredentialActivatedDeactivated
    smart_lock_credential_activation_deactivation_error: SmartLockCredentialActivationDeactivationError
    en54_external_power_loss: EN54ExternalPowerLoss
    en54_ethernet_communication_loss: EN54EthernetCommunicationLoss
    def __init__(self, door_opened: _Optional[_Union[DoorOpened, _Mapping]] = ..., ext_contact_opened: _Optional[_Union[ExtContactOpened, _Mapping]] = ..., roller_shutter_alarm: _Optional[_Union[RollerShutterAlarm, _Mapping]] = ..., roller_shutter_offline: _Optional[_Union[RollerShutterOffline, _Mapping]] = ..., shock_detected: _Optional[_Union[ShockDetected, _Mapping]] = ..., tilt_detected: _Optional[_Union[TiltDetected, _Mapping]] = ..., automatic_bypass_by_number: _Optional[_Union[AutomaticBypassByNumber, _Mapping]] = ..., automatic_bypass_by_restore_timer: _Optional[_Union[AutomaticBypassByRestoreTimer, _Mapping]] = ..., automatic_bypass_off: _Optional[_Union[AutomaticBypassOff, _Mapping]] = ..., power_low: _Optional[_Union[PowerLow, _Mapping]] = ..., bypass_on: _Optional[_Union[BypassOn, _Mapping]] = ..., device_communication_loss: _Optional[_Union[DeviceCommunicationLoss, _Mapping]] = ..., firmware_update_in_progress: _Optional[_Union[FirmwareUpdateInProgress, _Mapping]] = ..., malfunction: _Optional[_Union[Malfunction, _Mapping]] = ..., object_added: _Optional[_Union[ObjectAdded, _Mapping]] = ..., tamper_bypass_on: _Optional[_Union[TamperBypassOn, _Mapping]] = ..., tamper_opened: _Optional[_Union[TamperOpened, _Mapping]] = ..., turn_off: _Optional[_Union[TurnOff, _Mapping]] = ..., unregistered_device_event: _Optional[_Union[UnregisteredDeviceEvent, _Mapping]] = ..., arc_fault_detected: _Optional[_Union[ArcFaultDetected, _Mapping]] = ..., button_1_on: _Optional[_Union[Button1On, _Mapping]] = ..., button_2_on: _Optional[_Union[Button2On, _Mapping]] = ..., relay_current_high: _Optional[_Union[RelayCurrentHigh, _Mapping]] = ..., relay_current_high_device: _Optional[_Union[RelayCurrentHighDevice, _Mapping]] = ..., relay_current_high_user: _Optional[_Union[RelayCurrentHighUser, _Mapping]] = ..., relay_current_low: _Optional[_Union[RelayCurrentLow, _Mapping]] = ..., relay_current_ok: _Optional[_Union[RelayCurrentOk, _Mapping]] = ..., relay_not_responding: _Optional[_Union[RelayNotResponding, _Mapping]] = ..., relay_off_bytimer: _Optional[_Union[RelayOffByTimer, _Mapping]] = ..., relay_on: _Optional[_Union[RelayOn, _Mapping]] = ..., relay_on_by_arming: _Optional[_Union[RelayOnByArming, _Mapping]] = ..., relay_on_by_button: _Optional[_Union[RelayOnByButton, _Mapping]] = ..., relay_on_by_device: _Optional[_Union[RelayOnByDevice, _Mapping]] = ..., relay_on_by_disarming: _Optional[_Union[RelayOnByDisarming, _Mapping]] = ..., relay_on_by_scenario: _Optional[_Union[RelayOnByScenario, _Mapping]] = ..., relay_on_by_user: _Optional[_Union[RelayOnByUser, _Mapping]] = ..., relay_overheating_detected: _Optional[_Union[RelayOverheatingDetected, _Mapping]] = ..., relay_unable_to_switch_off: _Optional[_Union[RelayUnableToSwitchOff, _Mapping]] = ..., relay_voltage_high: _Optional[_Union[RelayVoltageHigh, _Mapping]] = ..., relay_voltage_low: _Optional[_Union[RelayVoltageLow, _Mapping]] = ..., relay_voltage_ok: _Optional[_Union[RelayVoltageOk, _Mapping]] = ..., data_channel_communication_loss: _Optional[_Union[DataChannelCommunicationLoss, _Mapping]] = ..., masking_detected: _Optional[_Union[MaskingDetected, _Mapping]] = ..., masking_detected_left: _Optional[_Union[MaskingDetectedLeft, _Mapping]] = ..., masking_detected_right: _Optional[_Union[MaskingDetectedRight, _Mapping]] = ..., motion_detected: _Optional[_Union[MotionDetected, _Mapping]] = ..., photo_by_scenario: _Optional[_Union[PhotoByScenario, _Mapping]] = ..., photo_by_scenario_unsuccessful: _Optional[_Union[PhotoByScenarioUnsuccessful, _Mapping]] = ..., photo_on_demand: _Optional[_Union[PhotoOnDemand, _Mapping]] = ..., photo_on_demand_unsuccessful: _Optional[_Union[PhotoOnDemandUnsuccessful, _Mapping]] = ..., photo_on_demand_unsuccessful_with_name: _Optional[_Union[PhotoOnDemandUnsuccessfulWithName, _Mapping]] = ..., photo_on_demand_with_name: _Optional[_Union[PhotoOnDemandWithName, _Mapping]] = ..., motion_detected_left: _Optional[_Union[MotionDetectedLeft, _Mapping]] = ..., motion_detected_right: _Optional[_Union[MotionDetectedRight, _Mapping]] = ..., photo_by_schedule: _Optional[_Union[PhotoBySchedule, _Mapping]] = ..., photo_by_schedule_unsuccessful: _Optional[_Union[PhotoByScheduleUnsuccessful, _Mapping]] = ..., camera_dirty: _Optional[_Union[CameraDirty, _Mapping]] = ..., fire_alarm: _Optional[_Union[FireAlarm, _Mapping]] = ..., fire_alarm_muted: _Optional[_Union[FireAlarmMuted, _Mapping]] = ..., high_co_level_detected: _Optional[_Union[HighCoLevelDetected, _Mapping]] = ..., high_co_level_detected_early_warning: _Optional[_Union[HighCoLevelDetectedEarlyWarning, _Mapping]] = ..., reserve_battery_low: _Optional[_Union[ReserveBatteryLow, _Mapping]] = ..., smoke_chamber_test_not_passed: _Optional[_Union[SmokeChamberTestNotPassed, _Mapping]] = ..., smoke_chamber_test_passed: _Optional[_Union[SmokeChamberTestPassed, _Mapping]] = ..., smoke_detected: _Optional[_Union[SmokeDetected, _Mapping]] = ..., smoke_detected_early_warning: _Optional[_Union[SmokeDetectedEarlyWarning, _Mapping]] = ..., temperature_high: _Optional[_Union[TemperatureHigh, _Mapping]] = ..., temperature_high_early_warning: _Optional[_Union[TemperatureHighEarlyWarning, _Mapping]] = ..., temperature_rise_detected: _Optional[_Union[TemperatureRiseDetected, _Mapping]] = ..., temperature_rise_detected_early_warning: _Optional[_Union[TemperatureRiseDetectedEarlyWarning, _Mapping]] = ..., fire_protect_malfunction: _Optional[_Union[FireProtectMalfunction, _Mapping]] = ..., heat_test_not_passed: _Optional[_Union[HeatTestNotPassed, _Mapping]] = ..., heat_test_passed: _Optional[_Union[HeatTestPassed, _Mapping]] = ..., high_cco_level_detected: _Optional[_Union[HighCcoLevelDetected, _Mapping]] = ..., co_test_not_passed: _Optional[_Union[CoTestNotPassed, _Mapping]] = ..., co_test_passed: _Optional[_Union[CoTestPassed, _Mapping]] = ..., co_2_high: _Optional[_Union[Co2High, _Mapping]] = ..., humidity_high: _Optional[_Union[HumidityHigh, _Mapping]] = ..., humidity_low: _Optional[_Union[HumidityLow, _Mapping]] = ..., humidity_ok: _Optional[_Union[HumidityOk, _Mapping]] = ..., temperature_low: _Optional[_Union[TemperatureLow, _Mapping]] = ..., temperature_ok: _Optional[_Union[TemperatureOk, _Mapping]] = ..., arm: _Optional[_Union[Arm, _Mapping]] = ..., arm_attempt: _Optional[_Union[ArmAttempt, _Mapping]] = ..., arming_incomplete: _Optional[_Union[ArmingIncomplete, _Mapping]] = ..., arm_with_malfunctions: _Optional[_Union[ArmWithMalfunctions, _Mapping]] = ..., disarm: _Optional[_Union[Disarm, _Mapping]] = ..., duress_disarm: _Optional[_Union[DuressDisarm, _Mapping]] = ..., duress_night_mode_off: _Optional[_Union[DuressNightModeOff, _Mapping]] = ..., group_arm: _Optional[_Union[GroupArm, _Mapping]] = ..., group_arm_attempt: _Optional[_Union[GroupArmAttempt, _Mapping]] = ..., group_arm_with_malfunctions: _Optional[_Union[GroupArmWithMalfunctions, _Mapping]] = ..., group_disarm: _Optional[_Union[GroupDisarm, _Mapping]] = ..., group_duress_disarm: _Optional[_Union[GroupDuressDisarm, _Mapping]] = ..., night_mode_off: _Optional[_Union[NightModeOff, _Mapping]] = ..., night_mode_on: _Optional[_Union[NightModeOn, _Mapping]] = ..., night_mode_on_attempt: _Optional[_Union[NightModeOnAttempt, _Mapping]] = ..., night_mode_on_with_malfunctions: _Optional[_Union[NightModeOnWithMalfunctions, _Mapping]] = ..., panic_button_pressed: _Optional[_Union[PanicButtonPressed, _Mapping]] = ..., password_attempt: _Optional[_Union[PasswordAttempt, _Mapping]] = ..., security_state_transition_progress_updated: _Optional[_Union[SecurityStateTransitionProgressUpdated, _Mapping]] = ..., duress_authorization: _Optional[_Union[DuressAuthorization, _Mapping]] = ..., arm_during_upgrade_attempt: _Optional[_Union[ArmDuringUpgradeAttempt, _Mapping]] = ..., bus_short_circuit: _Optional[_Union[BusShortCircuit, _Mapping]] = ..., cellular_signal_low: _Optional[_Union[CellularSignalLow, _Mapping]] = ..., cms_connection_loss: _Optional[_Union[CmsConnectionLoss, _Mapping]] = ..., donor_chosen: _Optional[_Union[DonorChosen, _Mapping]] = ..., ethernet_connection_loss: _Optional[_Union[EthernetConnectionLoss, _Mapping]] = ..., factory_reset: _Optional[_Union[FactoryReset, _Mapping]] = ..., gsm_connection_loss: _Optional[_Union[GsmConnectionLoss, _Mapping]] = ..., hold_up_alarm_confirmed: _Optional[_Union[HoldUpAlarmConfirmed, _Mapping]] = ..., incorrect_cms: _Optional[_Union[IncorrectCms, _Mapping]] = ..., intrusion_alarm_confirmed: _Optional[_Union[IntrusionAlarmConfirmed, _Mapping]] = ..., migration_start: _Optional[_Union[MigrationStart, _Mapping]] = ..., server_connection_loss: _Optional[_Union[ServerConnectionLoss, _Mapping]] = ..., migration_ok: _Optional[_Union[MigrationOk, _Mapping]] = ..., migration_failed: _Optional[_Union[MigrationFailed, _Mapping]] = ..., target_chosen: _Optional[_Union[TargetChosen, _Mapping]] = ..., turn_on: _Optional[_Union[TurnOn, _Mapping]] = ..., walk_test_start: _Optional[_Union[WalkTestStart, _Mapping]] = ..., wi_fi_connection_loss: _Optional[_Union[WiFiConnectionLoss, _Mapping]] = ..., wings_noise_high: _Optional[_Union[WingsNoiseHigh, _Mapping]] = ..., settings_changed: _Optional[_Union[SettingsChanged, _Mapping]] = ..., access_denied_to_company: _Optional[_Union[AccessDeniedToCompany, _Mapping]] = ..., access_denied_to_pro: _Optional[_Union[AccessDeniedToPro, _Mapping]] = ..., access_request: _Optional[_Union[AccessRequest, _Mapping]] = ..., chime_activated: _Optional[_Union[ChimeActivated, _Mapping]] = ..., chime_activated_in_group: _Optional[_Union[ChimeActivatedInGroup, _Mapping]] = ..., permanent_access_granted_to_company: _Optional[_Union[PermanentAccessGrantedToCompany, _Mapping]] = ..., permanent_access_granted_to_pro: _Optional[_Union[PermanentAccessGrantedToPro, _Mapping]] = ..., photo_by_scenario_on: _Optional[_Union[PhotoByScenarioOn, _Mapping]] = ..., photo_on_demand_on: _Optional[_Union[PhotoOnDemandOn, _Mapping]] = ..., system_restored: _Optional[_Union[SystemRestored, _Mapping]] = ..., system_restore_denied: _Optional[_Union[SystemRestoreDenied, _Mapping]] = ..., system_restore_request: _Optional[_Union[SystemRestoreRequest, _Mapping]] = ..., temporary_access_granted_to_company: _Optional[_Union[TemporaryAccessGrantedToCompany, _Mapping]] = ..., temporary_access_granted_to_pro: _Optional[_Union[TemporaryAccessGrantedToPro, _Mapping]] = ..., battery_disconnected: _Optional[_Union[BatteryDisconnected, _Mapping]] = ..., bridge_not_responding: _Optional[_Union[BridgeNotResponding, _Mapping]] = ..., CardDeactivated: _Optional[_Union[CardDeactivated, _Mapping]] = ..., code_deactivated: _Optional[_Union[CodeDeactivated, _Mapping]] = ..., custom_event: _Optional[_Union[CustomEvent, _Mapping]] = ..., deactivated_card_attempt: _Optional[_Union[DeactivatedCardAttempt, _Mapping]] = ..., detector_short_circuit: _Optional[_Union[DetectorShortCircuit, _Mapping]] = ..., device_moved: _Optional[_Union[DeviceMoved, _Mapping]] = ..., ethernet_communication_loss: _Optional[_Union[EthernetCommunicationLoss, _Mapping]] = ..., external_contact_lost: _Optional[_Union[ExternalContactLost, _Mapping]] = ..., external_contact_ok: _Optional[_Union[ExternalContactOk, _Mapping]] = ..., external_contact_short_circuit: _Optional[_Union[ExternalContactShortCircuit, _Mapping]] = ..., external_malfunction: _Optional[_Union[ExternalMalfunction, _Mapping]] = ..., external_power_loss: _Optional[_Union[ExternalPowerLoss, _Mapping]] = ..., fire_detector_short_circuit: _Optional[_Union[FireDetectorShortCircuit, _Mapping]] = ..., front_tamper_opened: _Optional[_Union[FrontTamperOpened, _Mapping]] = ..., gas_detected: _Optional[_Union[GasDetected, _Mapping]] = ..., glass_break_detected: _Optional[_Union[GlassBreakDetected, _Mapping]] = ..., hold_up_long_press: _Optional[_Union[HoldUpLongPress, _Mapping]] = ..., hold_up_short_press: _Optional[_Union[HoldUpShortPress, _Mapping]] = ..., intrusion_alarm: _Optional[_Union[IntrusionAlarm, _Mapping]] = ..., jeweller_noise_high: _Optional[_Union[JewellerNoiseHigh, _Mapping]] = ..., leak_detected: _Optional[_Union[LeakDetected, _Mapping]] = ..., medical_alarm: _Optional[_Union[MedicalAlarm, _Mapping]] = ..., monitoring_started: _Optional[_Union[MonitoringStarted, _Mapping]] = ..., permanent_access_request: _Optional[_Union[PermanentAccessRequest, _Mapping]] = ..., s_1_alarm: _Optional[_Union[S1Alarm, _Mapping]] = ..., s_3_alarm: _Optional[_Union[S3Alarm, _Mapping]] = ..., scenario_not_executed: _Optional[_Union[ScenarioNotExecuted, _Mapping]] = ..., temporary_access_request: _Optional[_Union[TemporaryAccessRequest, _Mapping]] = ..., battery_low: _Optional[_Union[BatteryLow, _Mapping]] = ..., back_tamper_opened: _Optional[_Union[BackTamperOpened, _Mapping]] = ..., short_circuit: _Optional[_Union[ShortCircuit, _Mapping]] = ..., tamper_board_disconnect: _Optional[_Union[TamperBoardDisconnect, _Mapping]] = ..., bus_voltage_high: _Optional[_Union[BusVoltageHigh, _Mapping]] = ..., line_sabotage: _Optional[_Union[LineSabotage, _Mapping]] = ..., fuse_break: _Optional[_Union[FuseBreak, _Mapping]] = ..., timezone_changed: _Optional[_Union[TimezoneChanged, _Mapping]] = ..., ring_broken: _Optional[_Union[RingBroken, _Mapping]] = ..., bus_conflict: _Optional[_Union[BusConflict, _Mapping]] = ..., end_of_life: _Optional[_Union[EndOfLife, _Mapping]] = ..., dev_fw_upgrade_started: _Optional[_Union[DevFWUpgradeStarted, _Mapping]] = ..., dev_fw_upgrade_failed: _Optional[_Union[DevFWUpgradeFailed, _Mapping]] = ..., dev_fw_upgrade_finished: _Optional[_Union[DevFWUpgradeFinished, _Mapping]] = ..., bus_power_disabled: _Optional[_Union[BusPowerDisabled, _Mapping]] = ..., onetime_full_bypass_on: _Optional[_Union[OnetimeFullBypassOn, _Mapping]] = ..., onetime_tamper_bypass_on: _Optional[_Union[OnetimeTamperBypassOn, _Mapping]] = ..., life_quality_malfunction: _Optional[_Union[LifeQualityMalfunction, _Mapping]] = ..., valve_opened_by_button: _Optional[_Union[ValveOpenedByButton, _Mapping]] = ..., valve_opened_by_scenario: _Optional[_Union[ValveOpenedByScenario, _Mapping]] = ..., valve_opened_by_arming: _Optional[_Union[ValveOpenedByArming, _Mapping]] = ..., valve_opened_by_disarming: _Optional[_Union[ValveOpenedByDisarming, _Mapping]] = ..., valve_opened_by_device: _Optional[_Union[ValveOpenedByDevice, _Mapping]] = ..., valve_opened_by_user: _Optional[_Union[ValveOpenedByUser, _Mapping]] = ..., undefined_valve_position: _Optional[_Union[UndefinedValvePosition, _Mapping]] = ..., battery_error: _Optional[_Union[BatteryError, _Mapping]] = ..., restore_request: _Optional[_Union[RestoreRequest, _Mapping]] = ..., bus_voltage_low: _Optional[_Union[BusVoltageLow, _Mapping]] = ..., charger_error: _Optional[_Union[ChargerError, _Mapping]] = ..., overheating_detected: _Optional[_Union[OverheatingDetected, _Mapping]] = ..., keypad_blocked: _Optional[_Union[KeypadBlocked, _Mapping]] = ..., keypad_unblocked_by_timer: _Optional[_Union[KeypadUnblockedByTimer, _Mapping]] = ..., keypad_unblocked_by_user: _Optional[_Union[KeypadUnblockedByUser, _Mapping]] = ..., relay_unable_to_switch_by_user: _Optional[_Union[RelayUnableToSwitchByUser, _Mapping]] = ..., relay_unable_to_switch_by_scenario: _Optional[_Union[RelayUnableToSwitchByScenario, _Mapping]] = ..., relay_unable_to_switch_by_arming: _Optional[_Union[RelayUnableToSwitchByArming, _Mapping]] = ..., relay_unable_to_switch_by_disarming: _Optional[_Union[RelayUnableToSwitchByDisarming, _Mapping]] = ..., keyarm_blocked: _Optional[_Union[KeyarmBlocked, _Mapping]] = ..., keyarm_unblocked_by_user: _Optional[_Union[KeyarmUnblockedByUser, _Mapping]] = ..., buses_break: _Optional[_Union[BusesBreak, _Mapping]] = ..., buses_conflict: _Optional[_Union[BusesConflict, _Mapping]] = ..., buses_unregistered: _Optional[_Union[BusesUnregistered, _Mapping]] = ..., reed_switch_broken: _Optional[_Union[ReedSwitchBroken, _Mapping]] = ..., accelerometer_broken: _Optional[_Union[AccelerometerBroken, _Mapping]] = ..., magnetic_sensor_broken: _Optional[_Union[MagneticSensorBroken, _Mapping]] = ..., calibration_required: _Optional[_Union[CalibrationRequired, _Mapping]] = ..., activation_rru_code: _Optional[_Union[ActivationRRUCode, _Mapping]] = ..., deactivation_rru_code: _Optional[_Union[DeactivationRRUCode, _Mapping]] = ..., improper_keyarm_usage: _Optional[_Union[ImproperKeyarmUsage, _Mapping]] = ..., video_scenario_triggered: _Optional[_Union[VideoScenarioTriggered, _Mapping]] = ..., battery_saving_mode_activation: _Optional[_Union[BatterySavingModeActivation, _Mapping]] = ..., periodic_test: _Optional[_Union[PeriodicTest, _Mapping]] = ..., exit_error: _Optional[_Union[ExitError, _Mapping]] = ..., recent_closing: _Optional[_Union[RecentClosing, _Mapping]] = ..., short_circuit_single_output: _Optional[_Union[ShortCircuitSingleOutput, _Mapping]] = ..., bus_voltage_high_single_output: _Optional[_Union[BusVoltageHighSingleOutput, _Mapping]] = ..., bus_voltage_low_single_output: _Optional[_Union[BusVoltageLowSingleOutput, _Mapping]] = ..., bus_power_disabled_single_output: _Optional[_Union[BusPowerDisabledSingleOutput, _Mapping]] = ..., lock_violation: _Optional[_Union[LockViolation, _Mapping]] = ..., duress_code: _Optional[_Union[DuressCode, _Mapping]] = ..., seismic_alarm: _Optional[_Union[SeismicAlarm, _Mapping]] = ..., temp_sensor_high_temperature: _Optional[_Union[TempSensorHighTemperature, _Mapping]] = ..., temp_sensor_low_temperature: _Optional[_Union[TempSensorLowTemperature, _Mapping]] = ..., local_exit_error: _Optional[_Union[LocalExitError, _Mapping]] = ..., abort_burglary: _Optional[_Union[AbortBurglary, _Mapping]] = ..., burglary_cancel: _Optional[_Union[BurglaryCancel, _Mapping]] = ..., device_supervision_failure: _Optional[_Union[DeviceSupervisionFailure, _Mapping]] = ..., self_test_passed: _Optional[_Union[SelfTestPassed, _Mapping]] = ..., self_test_failed: _Optional[_Union[SelfTestFailed, _Mapping]] = ..., masking_detected_malfunction: _Optional[_Union[MaskingDetectedMalfunction, _Mapping]] = ..., surveillance_scenario_executed: _Optional[_Union[SurveillanceScenarioExecuted, _Mapping]] = ..., battery_saving_mode_activation_failed: _Optional[_Union[BatterySavingModeActivationFailed, _Mapping]] = ..., photo_by_scenario_with_name: _Optional[_Union[PhotoByScenarioWithName, _Mapping]] = ..., photo_by_scenario_unsuccessful_with_name: _Optional[_Union[PhotoByScenarioUnsuccessfulWithName, _Mapping]] = ..., unvacated_premises: _Optional[_Union[UnvacatedPremises, _Mapping]] = ..., password_reset: _Optional[_Union[PasswordReset, _Mapping]] = ..., motion_detected_in_allowed_direction: _Optional[_Union[MotionDetectedInAllowedDirection, _Mapping]] = ..., motion_detected_in_forbidden_direction: _Optional[_Union[MotionDetectedInForbiddenDirection, _Mapping]] = ..., motion_detected_in_allowed_direction_timer_started: _Optional[_Union[MotionDetectedInAllowedDirectionTimerStarted, _Mapping]] = ..., motion_detected_in_allowed_direction_timer_active: _Optional[_Union[MotionDetectedInAllowedDirectionTimerActive, _Mapping]] = ..., allowed_direction_timer_ended: _Optional[_Union[AllowedDirectionTimerEnded, _Mapping]] = ..., video_archive_export_prepared: _Optional[_Union[VideoArchiveExportPrepared, _Mapping]] = ..., video_archive_export_failed: _Optional[_Union[VideoArchiveExportFailed, _Mapping]] = ..., ext_src_low_voltage: _Optional[_Union[ExtSrcLowVoltage, _Mapping]] = ..., jwl_antenna_disconnect: _Optional[_Union[JwlAntennaDisconnect, _Mapping]] = ..., jwl_antenna_connect: _Optional[_Union[JwlAntennaConnect, _Mapping]] = ..., wings_antenna_disconnect: _Optional[_Union[WingsAntennaDisconnect, _Mapping]] = ..., wings_antenna_connect: _Optional[_Union[WingsAntennaConnect, _Mapping]] = ..., gsm_antenna_disconnect: _Optional[_Union[GsmAntennaDisconnect, _Mapping]] = ..., gsm_antenna_connect: _Optional[_Union[GsmAntennaConnect, _Mapping]] = ..., jwl_antenna_damaged: _Optional[_Union[JwlAntennaDamaged, _Mapping]] = ..., wings_antenna_damaged: _Optional[_Union[WingsAntennaDamaged, _Mapping]] = ..., gsm_antenna_damaged: _Optional[_Union[GsmAntennaDamaged, _Mapping]] = ..., csmoke_detected: _Optional[_Union[CSmokeDetected, _Mapping]] = ..., in_call: _Optional[_Union[InCall, _Mapping]] = ..., out_call: _Optional[_Union[OutCall, _Mapping]] = ..., in_call_error: _Optional[_Union[InCallError, _Mapping]] = ..., out_call_error: _Optional[_Union[OutCallError, _Mapping]] = ..., callback_request: _Optional[_Union[CallbackRequest, _Mapping]] = ..., out_call_no_response: _Optional[_Union[OutCallNoResponse, _Mapping]] = ..., out_call_timeout: _Optional[_Union[OutCallTimeout, _Mapping]] = ..., in_call_missed: _Optional[_Union[InCallMissed, _Mapping]] = ..., in_call_timeout: _Optional[_Union[InCallTimeout, _Mapping]] = ..., callback_denied: _Optional[_Union[CallbackDenied, _Mapping]] = ..., intrusion_alarm_confirmed_general: _Optional[_Union[IntrusionAlarmConfirmedGeneral, _Mapping]] = ..., intrusion_alarm_confirmed_detailed: _Optional[_Union[IntrusionAlarmConfirmedDetailed, _Mapping]] = ..., unverified_alarm: _Optional[_Union[UnverifiedAlarm, _Mapping]] = ..., smart_bracket_opened: _Optional[_Union[SmartBracketOpened, _Mapping]] = ..., pir_sensor_broken: _Optional[_Union[PirSensorBroken, _Mapping]] = ..., microwave_sensor_broken: _Optional[_Union[MicrowaveSensorBroken, _Mapping]] = ..., incorrect_device_installation: _Optional[_Union[IncorrectDeviceInstallation, _Mapping]] = ..., masking_sensor_broken: _Optional[_Union[MaskingSensorBroken, _Mapping]] = ..., masking_sensor_calibration_failed: _Optional[_Union[MaskingSensorCalibrationFailed, _Mapping]] = ..., bukhoor_enabled: _Optional[_Union[BukhoorEnabled, _Mapping]] = ..., bukhoor_disabled: _Optional[_Union[BukhoorDisabled, _Mapping]] = ..., bukhoor_disabled_by_timeout: _Optional[_Union[BukhoorDisabledByTimeout, _Mapping]] = ..., sip_connection_loss: _Optional[_Union[SipConnectionLoss, _Mapping]] = ..., smart_home_motion_detected: _Optional[_Union[SmartHomeMotionDetected, _Mapping]] = ..., human_detected: _Optional[_Union[HumanDetected, _Mapping]] = ..., pet_detected: _Optional[_Union[PetDetected, _Mapping]] = ..., car_detected: _Optional[_Union[CarDetected, _Mapping]] = ..., ring_button_pressed: _Optional[_Union[RingButtonPressed, _Mapping]] = ..., case_break_detected: _Optional[_Union[CaseBreakDetected, _Mapping]] = ..., self_test_device_disconnected: _Optional[_Union[SelfTestDeviceDisconnected, _Mapping]] = ..., seismo_sensor_broken: _Optional[_Union[SeismoSensorBroken, _Mapping]] = ..., vorf_channel_communication_loss: _Optional[_Union[VorfChannelCommunicationLoss, _Mapping]] = ..., relay_short_circuit: _Optional[_Union[RelayShortCircuit, _Mapping]] = ..., bolt_switch_contact_opened: _Optional[_Union[BoltSwitchContactOpened, _Mapping]] = ..., blocking_element_opened: _Optional[_Union[BlockingElementOpened, _Mapping]] = ..., valve_stuck_prevention_not_executed: _Optional[_Union[ValveStuckPreventionNotExecuted, _Mapping]] = ..., valve_stuck_prevention_executed: _Optional[_Union[ValveStuckPreventionExecuted, _Mapping]] = ..., short_circuit_single_output1: _Optional[_Union[ShortCircuitSingleOutput1, _Mapping]] = ..., bus_voltage_high_single_output1: _Optional[_Union[BusVoltageHighSingleOutput1, _Mapping]] = ..., bus_voltage_low_single_output1: _Optional[_Union[BusVoltageLowSingleOutput1, _Mapping]] = ..., short_circuit_single_output2: _Optional[_Union[ShortCircuitSingleOutput2, _Mapping]] = ..., bus_voltage_high_single_output2: _Optional[_Union[BusVoltageHighSingleOutput2, _Mapping]] = ..., bus_voltage_low_single_output2: _Optional[_Union[BusVoltageLowSingleOutput2, _Mapping]] = ..., line_connect_error: _Optional[_Union[LineConnectError, _Mapping]] = ..., photo_on_demand_for_detection_area: _Optional[_Union[PhotoOnDemandForDetectionArea, _Mapping]] = ..., photo_on_demand_for_detection_area_unsuccessful: _Optional[_Union[PhotoOnDemandForDetectionAreaUnsuccessful, _Mapping]] = ..., en54_fire_alarm_reset: _Optional[_Union[EN54FireAlarmReset, _Mapping]] = ..., device_does_not_respond: _Optional[_Union[DeviceDoesNotRespond, _Mapping]] = ..., sounder_fault: _Optional[_Union[SounderFault, _Mapping]] = ..., vad_fault: _Optional[_Union[VADFault, _Mapping]] = ..., heat_detection_fault: _Optional[_Union[HeatDetectionFault, _Mapping]] = ..., smoke_detection_fault: _Optional[_Union[SmokeDetectionFault, _Mapping]] = ..., motion_detected_during_test: _Optional[_Union[MotionDetectedDuringTest, _Mapping]] = ..., alarm_annunciation_test: _Optional[_Union[AlarmAnnunciationTest, _Mapping]] = ..., battery_temperature_out_of_range: _Optional[_Union[BatteryTemperatureOutOfRange, _Mapping]] = ..., exit_delay_complete: _Optional[_Union[ExitDelayComplete, _Mapping]] = ..., group_auto_arm: _Optional[_Union[GroupAutoArm, _Mapping]] = ..., group_auto_arm_with_malfunctions: _Optional[_Union[GroupAutoArmWithMalfunctions, _Mapping]] = ..., group_auto_arm_attempt: _Optional[_Union[GroupAutoArmAttempt, _Mapping]] = ..., group_auto_disarm: _Optional[_Union[GroupAutoDisarm, _Mapping]] = ..., auto_arm_not_executed: _Optional[_Union[AutoArmNotExecuted, _Mapping]] = ..., auto_arm: _Optional[_Union[AutoArm, _Mapping]] = ..., auto_arm_with_malfunctions: _Optional[_Union[AutoArmWithMalfunctions, _Mapping]] = ..., auto_disarm: _Optional[_Union[AutoDisarm, _Mapping]] = ..., auto_self_test_passed: _Optional[_Union[AutoSelfTestPassed, _Mapping]] = ..., auto_self_test_failed: _Optional[_Union[AutoSelfTestFailed, _Mapping]] = ..., auto_self_test_error: _Optional[_Union[AutoSelfTestError, _Mapping]] = ..., en54_silence: _Optional[_Union[EN54Silence, _Mapping]] = ..., en54_resound: _Optional[_Union[EN54Resound, _Mapping]] = ..., trigger_group_not_armed: _Optional[_Union[TriggerGroupNotArmed, _Mapping]] = ..., alarm_annunciation_test_by_user: _Optional[_Union[AlarmAnnunciationTestByUser, _Mapping]] = ..., alarm_annunciation_test_by_card: _Optional[_Union[AlarmAnnunciationTestByCard, _Mapping]] = ..., alarm_annunciation_test_by_code: _Optional[_Union[AlarmAnnunciationTestByCode, _Mapping]] = ..., wifi_module_upgrade_started: _Optional[_Union[WiFiModuleUpgradeStarted, _Mapping]] = ..., wifi_module_upgrade_failed: _Optional[_Union[WiFiModuleUpgradeFailed, _Mapping]] = ..., hub_module_upgrade_finished: _Optional[_Union[HubModuleUpgradeFinished, _Mapping]] = ..., out_power_overload: _Optional[_Union[OutPowerOverload, _Mapping]] = ..., battery_saving_mode_wakeup_sms: _Optional[_Union[BatterySavingModeWakeupSMS, _Mapping]] = ..., endpoint_disabled_by_user: _Optional[_Union[EndpointDisabledByUser, _Mapping]] = ..., endpoint_disabled_by_code: _Optional[_Union[EndpointDisabledByCode, _Mapping]] = ..., endpoint_disabled_by_card: _Optional[_Union[EndpointDisabledByCard, _Mapping]] = ..., in_call_timeout_bsm: _Optional[_Union[InCallTimeoutBSM, _Mapping]] = ..., out_call_timeout_bsm: _Optional[_Union[OutCallTimeoutBSM, _Mapping]] = ..., battery_saving_mode_wakeup_by_scheduled: _Optional[_Union[BatterySavingModeWakeupByScheduled, _Mapping]] = ..., output_fault: _Optional[_Union[OutputFault, _Mapping]] = ..., en54_tamper_opened: _Optional[_Union[EN54TamperOpened, _Mapping]] = ..., en54_power_low: _Optional[_Union[EN54PowerLow, _Mapping]] = ..., en54_device_communication_loss: _Optional[_Union[EN54DeviceCommunicationLoss, _Mapping]] = ..., en54_fire_alarm: _Optional[_Union[EN54FireAlarm, _Mapping]] = ..., en54_medical_alarm: _Optional[_Union[EN54MedicalAlarm, _Mapping]] = ..., en54_panic_button_pressed: _Optional[_Union[EN54PanicButtonPressed, _Mapping]] = ..., en54_gas_detected: _Optional[_Union[EN54GasDetected, _Mapping]] = ..., en54_external_fault: _Optional[_Union[EN54ExternalFault, _Mapping]] = ..., en54_leak_detected: _Optional[_Union[EN54LeakDetected, _Mapping]] = ..., external_contact_hard_fault: _Optional[_Union[ExternalContactHardFault, _Mapping]] = ..., fault_alarm: _Optional[_Union[FaultAlarm, _Mapping]] = ..., relay_on_by_access_code: _Optional[_Union[RelayOnByAccessCode, _Mapping]] = ..., relay_on_by_access_card: _Optional[_Union[RelayOnByAccessCard, _Mapping]] = ..., relay_on_by_timer: _Optional[_Union[RelayOnByTimer, _Mapping]] = ..., relay_off_by_user: _Optional[_Union[RelayOffByUser, _Mapping]] = ..., relay_off_by_access_code: _Optional[_Union[RelayOffByAccessCode, _Mapping]] = ..., relay_off_by_access_card: _Optional[_Union[RelayOffByAccessCard, _Mapping]] = ..., evacuation: _Optional[_Union[Evacuation, _Mapping]] = ..., custom_alarm: _Optional[_Union[CustomAlarm, _Mapping]] = ..., audio_record: _Optional[_Union[AudioRecord, _Mapping]] = ..., relay_on_by_fail_safe: _Optional[_Union[RelayOnByFailSafe, _Mapping]] = ..., relay_off_by_fail_safe: _Optional[_Union[RelayOffByFailSafe, _Mapping]] = ..., delays_override: _Optional[_Union[DelaysOverride, _Mapping]] = ..., software_system_fault: _Optional[_Union[SoftwareSystemFault, _Mapping]] = ..., memory_system_fault: _Optional[_Union[MemorySystemFault, _Mapping]] = ..., arc_reporting_off: _Optional[_Union[ArcReportingOff, _Mapping]] = ..., fire_delays_on: _Optional[_Union[FireDelaysOn, _Mapping]] = ..., fire_delays_off: _Optional[_Union[FireDelaysOff, _Mapping]] = ..., battery_fault: _Optional[_Union[BatteryFault, _Mapping]] = ..., fire_zone_test: _Optional[_Union[FireZoneTest, _Mapping]] = ..., cms_delivery_failed: _Optional[_Union[CmsDeliveryFailed, _Mapping]] = ..., day_alarm_temporary_bypass_activated: _Optional[_Union[DayAlarmTemporaryBypassActivated, _Mapping]] = ..., duress_day_alarm_temporary_bypass_activated: _Optional[_Union[DuressDayAlarmTemporaryBypassActivated, _Mapping]] = ..., day_alarm_bypass_activated: _Optional[_Union[DayAlarmBypassActivated, _Mapping]] = ..., duress_day_alarm_bypass_activated: _Optional[_Union[DuressDayAlarmBypassActivated, _Mapping]] = ..., day_alarm_bypass_not_restored: _Optional[_Union[DayAlarmBypassNotRestored, _Mapping]] = ..., external_contact_resistance_fault: _Optional[_Union[ExternalContactResistanceFault, _Mapping]] = ..., alarms_to_cms_disabled: _Optional[_Union[AlarmsToCmsDisabled, _Mapping]] = ..., alarms_to_cms_enabled: _Optional[_Union[AlarmsToCmsEnabled, _Mapping]] = ..., faults_to_cms_disabled: _Optional[_Union[FaultsToCmsDisabled, _Mapping]] = ..., faults_to_cms_enabled: _Optional[_Union[FaultsToCmsEnabled, _Mapping]] = ..., detector_voltage_low: _Optional[_Union[DetectorVoltageLow, _Mapping]] = ..., fire_detector_voltage_low: _Optional[_Union[FireDetectorVoltageLow, _Mapping]] = ..., zone_test_system_exit: _Optional[_Union[ZoneTestSystemExit, _Mapping]] = ..., cms_connection_lost: _Optional[_Union[CmsConnectionLost, _Mapping]] = ..., smart_lock_unlocked_by_knob: _Optional[_Union[SmartLockUnlockedByKnob, _Mapping]] = ..., smart_lock_unlocked_by_code: _Optional[_Union[SmartLockUnlockedByCode, _Mapping]] = ..., smart_lock_unlocked_by_tag: _Optional[_Union[SmartLockUnlockedByTag, _Mapping]] = ..., smart_lock_unlocked_by_user: _Optional[_Union[SmartLockUnlockedByUser, _Mapping]] = ..., smart_lock_unlocked_by_scenario: _Optional[_Union[SmartLockUnlockedByScenario, _Mapping]] = ..., smart_lock_unlocked_by_arm: _Optional[_Union[SmartLockUnlockedByArm, _Mapping]] = ..., smart_lock_unlocked_by_disarm: _Optional[_Union[SmartLockUnlockedByDisarm, _Mapping]] = ..., smart_lock_unlocked_by_keyboard: _Optional[_Union[SmartLockUnlockedByKeyboard, _Mapping]] = ..., smart_lock_module_locked_automatically: _Optional[_Union[SmartLockModuleLockedAutomatically, _Mapping]] = ..., smart_lock_door_open: _Optional[_Union[SmartLockDoorOpen, _Mapping]] = ..., smart_lock_doorbell_button_pressed: _Optional[_Union[SmartLockDoorbellButtonPressed, _Mapping]] = ..., smart_lock_keyboard_locked: _Optional[_Union[SmartLockKeyboardLocked, _Mapping]] = ..., module_inserted_into_different_lock: _Optional[_Union[ModuleInsertedIntoDifferentLock, _Mapping]] = ..., smart_lock_credential_added: _Optional[_Union[SmartLockCredentialAdded, _Mapping]] = ..., smart_lock_credential_adding_error: _Optional[_Union[SmartLockCredentialAddingError, _Mapping]] = ..., smart_lock_credential_removed: _Optional[_Union[SmartLockCredentialRemoved, _Mapping]] = ..., smart_lock_credential_removing_error: _Optional[_Union[SmartLockCredentialRemovingError, _Mapping]] = ..., smart_lock_locked_with_confirmation: _Optional[_Union[SmartLockLockedWithConfirmation, _Mapping]] = ..., smart_lock_credential_activated_deactivated: _Optional[_Union[SmartLockCredentialActivatedDeactivated, _Mapping]] = ..., smart_lock_credential_activation_deactivation_error: _Optional[_Union[SmartLockCredentialActivationDeactivationError, _Mapping]] = ..., en54_external_power_loss: _Optional[_Union[EN54ExternalPowerLoss, _Mapping]] = ..., en54_ethernet_communication_loss: _Optional[_Union[EN54EthernetCommunicationLoss, _Mapping]] = ...) -> None: ...
