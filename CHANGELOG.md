# Changelog

All notable changes to the Ajax Security System integration will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2024-11-09

### Fixed
- **Critical**: Fixed grpcio dependency conflict with Home Assistant
  - Changed requirement from `grpcio==1.72.1` to `grpcio>=1.62.0`
  - Now compatible with both Home Assistant 2024.10.x (grpcio 1.72.1) and 2024.11+ (grpcio 1.75.1)
  - Resolves issue #1 where integration failed to load due to dependency conflicts

### Changed
- Updated manifest.json to use flexible grpcio version constraint

## [0.1.1] - 2024-11-09

### Fixed
- Fixed grpcio version compatibility for Home Assistant OS 2025.10.4
  - Updated all v3 protobuf files to use grpcio 1.72.1 instead of 1.75.1
  - Changed manifest requirement from `grpcio>=1.60.0` to `grpcio==1.72.1`

### Note
- This version was superseded by 0.1.2 due to dependency conflicts with newer Home Assistant versions

## [0.1.0] - 2024-11-08

### Added
- **Initial release** of Ajax Security System integration
- **Alarm Control Panel** platform
  - Real-time security mode control (Armed, Disarmed, Night Mode)
  - Live status updates via gRPC streaming
  - Instant synchronization with Ajax mobile app
- **Sensor** platform
  - Battery level monitoring for all devices
  - Temperature readings from supported devices
  - Hub status monitoring
- **Button** platform
  - Panic button activation
  - Siren test functionality
- **HACS Support**
  - Added hacs.json configuration
  - Added info.md documentation for HACS store
- **GitHub Actions**
  - Automatic release creation on version tags
  - ZIP package generation for easy installation

### Technical Details
- Uses gRPC streaming for real-time updates
- 60-second polling interval for minimal API load
- Direct communication using Ajax's mobile app protocol
- Compatible with Home Assistant 2023.8.0+

### Known Limitations
- Binary sensors not yet implemented (motion, door/window, smoke detectors)
- Only tested with Ajax Hub and basic sensors
- Requires connection to Ajax cloud services (no offline mode)

---

## Release Notes Format

For each release, we document:
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

## Contributing

When contributing changes, please update this CHANGELOG.md file with your changes under the "Unreleased" section at the top of the file.
