# Ajax Security Integration - Notes for Claude

## Important API Limitations

### SSE/SQS Real-time Events
- **SSE/SQS events are ONLY received when the alarm is ARMED**
- When disarmed, there are NO real-time events from Ajax
- Ajax has been asked to add SQS events for disarmed mode but refused for now
- This means polling is the ONLY way to get state updates when disarmed

### API Rate Limiting Concerns
- For 15 users, current polling generates ~200 requests/minute
- Julien (proxy maintainer) requested optimization for load testing
- Target: reduce API calls while maintaining reasonable responsiveness

## API Endpoints

### Video Edge Cameras
- Endpoint: `/user/{userId}/spaces/{spaceId}/devices/video-edges`
- Requires `real_space_id` (from spaceBinding), NOT `hub_id`
- Types: NVR, TURRET, BULLET, MINIDOME
- AI detections: VIDEO_MOTION, VIDEO_HUMAN, VIDEO_VEHICLE, VIDEO_PET

### Cameras (MotionCam)
- Endpoint: `/user/{userId}/hubs/{hubId}/cameras`
- This is for MotionCam devices (motion detectors with camera)
- NOT for surveillance cameras (those are Video Edge)

## Polling Strategy Considerations
- Armed mode: Can rely on SSE/SQS for real-time, polling is fallback
- Disarmed mode: Must poll for updates (no SSE/SQS)
- Door sensors need fast updates when disarmed for good UX
