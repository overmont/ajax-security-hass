# Changelog

All notable changes to this project will be documented in this file.

## [0.7.44] - 2025-01-10

### Fixed
- Round sensor values to avoid jitter on last decimal (#29)
  - Battery level: round to integer
  - Signal strength: round to integer
  - Temperature: round to 1 decimal place

### Changed
- Use HA native translations for standard device classes (#27)
  - Entities with standard device_class now use HA automatic naming
  - Removed redundant translation_key for TAMPER, BATTERY, DOOR, MOTION, etc.

## [0.7.43] - 2025-01-08

### Fixed
- Add SSE event deduplication (#28)
- Handle tamperopened SSE event (#28)
- Use SWITCH_ON/OFF with channel parameter for multi-gang switches
- Parse multi-gang LightSwitch data from device root level

## [0.7.42] - 2025-01-07

### Fixed
- Use correct API path for cameras endpoint

## [0.7.41] - 2025-01-06

### Added
- Multi-gang LightSwitch support (#26)

### Fixed
- Use actions/checkout@v4 in release workflow

## [0.7.40] - 2025-01-05

### Added
- LightSwitch device type mappings (#26)
- Include cameras in get_raw_devices service

### Fixed
- Use async file write in get_raw_devices service

### Changed
- Remove expensive debug logging for REPEATER/BUTTON

## [0.7.38] - 2025-01-04

### Added
- Proxy URL option in integration settings
- Tamper sensor support for TWO_EOL wiring scheme (#23)

## [0.7.36] - 2025-01-03

### Fixed
- Parse transition from event code for SSE/proxy mode (#22)
- Improve SSE manager device lookup for proxy mode (#22)

## [0.7.34] - 2025-01-02

### Fixed
- Add detailed logging for WireInput device debugging (#23)
- Improve WireInput event handling and device matching (#23)
- Add NO_EOL and ONE_EOL wiring scheme support (#23)

## [0.7.32] - 2025-01-01

### Fixed
- Use contactTwoDetails.contactState for TWO_EOL wiring (#23)
- Improve Fibra device support and conditional entity creation (#23)
- Add TRANSMITTER to device handlers (#23)

## [0.7.29] - 2024-12-30

### Added
- Fibra device type mappings (#23)
- Scenario events handling to SSE manager (#22)

### Fixed
- Add relayonbyuser/relayoffbyuser to relay events (#22)

## [0.7.26] - 2024-12-28

### Added
- MultiTransmitter and LightSwitch to device support table

### Fixed
- Remove tamper entity from WireInput devices (#13)
- Exclude wiringSchemeSpecificDetails from device update (#13)

## [0.7.24] - 2024-12-26

### Added
- Support armwithmalfunctions and nightmodeonwithmalfunctions states (#20)
- Fast polling for door sensors excluded from night mode (#21)

### Fixed
- Add missing security_state arg to _manage_door_sensor_polling (#21)
- Update outdated comments and remove unused function (#18)

## [0.7.23] - 2024-12-25

### Fixed
- Update polling interval on SQS arm/disarm events (#18)
- Protect group states from REST overwrite (#17)

### Added
- Detect scenario events triggered by Button (#15)

## [0.7.22] - 2024-12-24

### Fixed
- Add NORMAL to signal strength mapping (#16)
- Deep merge for WireInput settings (#13)

## [0.7.20] - 2024-12-23

### Fixed
- Protect optimistic state from SQS overwrite (#17)

## [0.7.18] - 2024-12-22

### Added
- Button device support (#15)

### Fixed
- Handle None wiredDeviceSettings (#13)
- Consistent signal strength units (#14)
- MultiTransmitter wired devices support (#13)
- Detect night mode from state string (#8)
- Respect user area assignments, remove hardcoded French colors (#11)

## [0.7.12] - 2024-12-20

### Fixed
- Use transition field for door open/close state (#9)
- Check nightMode field for night mode state (#8)

## [0.7.11] - 2024-12-19

### Fixed
- Use translation_key for switches, button, and device_tracker

## [0.7.10] - 2024-12-18

### Fixed
- Change hardcoded 'Piece' to 'Room' in notifications
- Remove all hardcoded French strings, use translation keys

## [0.7.9] - 2024-12-17

### Fixed
- Add missing state translations for sensors
- Use translation key for 'no event' state in recent_events sensor
- Format duration as readable format (3 min, 30s)
- Use translation keys for siren volume and duration sensors
- Use translation keys for hub tamper and external power sensors
- Use translation keys for hub noise level sensor
- Use translation keys for shock sensitivity options

## [0.7.8] - 2024-12-16

### Added
- Group arming support
- Door sensor fast polling
- English translations

## [0.7.7] - 2024-12-15

### Added
- MultiTransmitter Fibra support

### Fixed
- Multitransmitter state not updated

## [0.7.6] - 2024-12-14

### Changed
- Update repo URLs to new repository

### Fixed
- Better auth errors + fix sensors after reboot
- Alarm panel availability to prevent false automation triggers
- Prevent duplicate entity creation errors
- Token refresh for proxy mode

## [0.6.0] - 2024-11-15

### Changed
- Complete migration from reverse-engineered gRPC API to official Ajax REST API
- New api.py: Complete REST API client with rate limiting (2 req/min/user)
- New sqs_client.py: AWS SQS client for real-time events
- Architecture now uses api.ajax.systems/api/v1 + AWS SQS

### Removed
- All protobuf/gRPC code (~2MB)
- grpcio and protobuf dependencies

### Added
- aiohttp and aiobotocore dependencies

## [0.5.0] - 2024-10-01

### Added
- Device color conversion
- Real-time streaming improvements
- Periodic polling for wire_input EOL sensors
- Support for EOL sensors via MultiTransmitter

## [0.4.13] - 2024-09-15

### Fixed
- Alarm showing incorrect state on Home Assistant restart
- GSM status displaying numeric values instead of text

## [0.4.12] - 2024-09-10

### Added
- PayPal donation option

### Changed
- Reduce log verbosity for repetitive operations

## [0.4.11] - 2024-09-05

### Added
- Support for CombiProtect device (motion + glass break detector)

## [0.4.10] - 2024-09-01

### Fixed
- Door sensor state initialization from historical notifications
- 2FA authentication flow and improve password security
- Store password as SHA256 hash for improved security

## [0.4.9] - 2024-08-25

### Fixed
- Night mode detection - check night_mode_enabled flag first
- GitHub security alerts

## [0.4.8] - 2024-08-20

### Added
- Detailed debug logging for night mode detection

## [0.4.7] - 2024-08-15

### Added
- Revolut donation option
- Home Assistant Community Forum badge
- Two-factor authentication (2FA/TOTP) support

### Fixed
- Alarm control panel not updating when arming night mode

## [0.4.6] - 2024-08-10

### Changed
- Change group/zone entities from alarm panels to switches

## [0.4.5] - 2024-08-05

### Added
- Support for Ajax wired input modules and line splitters

## [0.4.4] - 2024-08-01

### Added
- Improved debug support for unknown device types

### Fixed
- Dataclass field ordering for raw_type in AjaxDevice

## [0.4.3] - 2024-07-25

### Fixed
- Group/zone alarm panels not being created on initial setup
- Duplicate malfunctions sensor causing unique ID conflict

## [0.4.2] - 2024-07-20

### Fixed
- TypeError: malfunctions is already an int, not a list

## [0.4.1] - 2024-07-15

### Fixed
- arm_night state synchronization issue (#16)
- Device state and malfunction monitoring

## [0.4.0] - 2024-07-10

### Added
- Automation events
- Batch updates
- Device info diagnostic

### Fixed
- Blocking I/O warning in device info generation

## [0.3.5] - 2024-07-05

### Added
- Group/zone support
- Improved logging

## [0.3.4] - 2024-07-01

### Added
- Space selection feature (#14)

### Fixed
- Missing config_validation import

## [0.3.3] - 2024-06-25

### Added
- Room support in device names

## [0.3.2] - 2024-06-20

### Added
- Persistent notification configuration options
- Force ARM services

### Fixed
- NoneType error for notifications without event_type

## [0.3.1] - 2024-06-15

### Fixed
- Alarm control panel missing from hub device
- Merge duplicate hub devices into single device
- Real-time alarm status updates reliability
- Handle users without notification access gracefully
- Door sensor not detecting closed state

### Added
- Socket/relay support
