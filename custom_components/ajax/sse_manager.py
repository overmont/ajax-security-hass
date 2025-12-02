"""SSE Manager for Ajax real-time events via proxy.

This manager receives events from the SSE client (proxy mode) and processes them
in the same way as the SQS manager. The event format from the proxy should be
compatible with the SQS event format.

Architecture:
- SSE events are used for INSTANT state updates (< 1 second)
- REST API polling confirms state periodically (fallback)
- SSE events directly update coordinator state for fastest response
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from .event_codes import (
    DEFAULT_LANGUAGE,
    parse_event_code,
)

# Import event mappings from SQS manager to avoid duplication
from .sqs_manager import (
    DEVICE_STATUS_EVENTS,
    DOOR_EVENTS,
    EVENT_TAG_TO_STATE,
    FLOOD_EVENTS,
    GLASS_EVENTS,
    MOTION_EVENTS,
    RELAY_EVENTS,
    SMOKE_EVENTS,
    TAMPER_EVENTS,
)

if TYPE_CHECKING:
    from .coordinator import AjaxDataCoordinator
    from .sse_client import AjaxSSEClient

_LOGGER = logging.getLogger(__name__)


class SSEManager:
    """Manages SSE events from Ajax proxy."""

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        sse_client: AjaxSSEClient,
    ):
        """Initialize SSE Manager.

        Args:
            coordinator: The Ajax data coordinator
            sse_client: SSE client instance
        """
        self.coordinator = coordinator
        self.sse_client = sse_client
        self._language = DEFAULT_LANGUAGE
        self._last_state_update: dict[str, float] = {}  # hub_id -> timestamp

    def set_language(self, language: str) -> None:
        """Set language for event messages."""
        self._language = language

    async def start(self) -> bool:
        """Start receiving SSE events.

        Returns:
            True if started successfully
        """
        _LOGGER.info("Starting SSE Manager...")

        # Set up callback for received events
        self.sse_client._callback = self._handle_event

        # Start SSE client
        success = await self.sse_client.start()

        if success:
            _LOGGER.info("SSE Manager started successfully")
        else:
            _LOGGER.error("Failed to start SSE Manager")

        return success

    async def stop(self) -> None:
        """Stop receiving SSE events."""
        _LOGGER.info("Stopping SSE Manager...")
        await self.sse_client.stop()
        _LOGGER.info("SSE Manager stopped")

    def is_state_protected(self, hub_id: str) -> bool:
        """Check if a hub's state was recently updated via SSE.

        This prevents REST polling from overwriting recent SSE updates.

        Args:
            hub_id: Hub ID to check

        Returns:
            True if state was updated via SSE in the last 5 seconds
        """
        last_update = self._last_state_update.get(hub_id, 0)
        return (time.time() - last_update) < 5

    def _handle_event(self, event_data: dict[str, Any]) -> None:
        """Handle an SSE event.

        The proxy should send events in a format similar to SQS:
        {
            "event": {
                "eventTag": "Disarm",
                "eventCode": "M_22_00",
                "hubId": "002BB321",
                "timestamp": 1234567890,
                "source": {"name": "User Name", "type": "USER"},
                "device": {"id": "xxx", "name": "Device Name", "type": "DoorProtect"}
            }
        }

        Or a simplified format from the proxy:
        {
            "eventTag": "Disarm",
            "hubId": "002BB321",
            "sourceName": "User Name",
            ...
        }
        """
        try:
            # Handle both nested and flat event formats
            event = event_data.get("event", event_data)

            event_tag = event.get("eventTag", "").lower()
            hub_id = event.get("hubId")

            if not event_tag or not hub_id:
                _LOGGER.debug("SSE event missing eventTag or hubId: %s", event_data)
                return

            # Extract event details
            event_code = event.get("eventCode", "")
            source = event.get("source", {})
            source_name = (
                source.get("name")
                if isinstance(source, dict)
                else event.get("sourceName", "")
            )
            source_type = (
                source.get("type")
                if isinstance(source, dict)
                else event.get("sourceType", "")
            )

            # Parse event code for type info
            code_info = parse_event_code(event_code)
            event_type = code_info.get("type", "UNKNOWN") if code_info else "UNKNOWN"
            transition = (
                code_info.get("transition", "TRIGGERED") if code_info else "TRIGGERED"
            )

            _LOGGER.info(
                "SSE event: type=%s, tag=%s, code=%s, source=%s (%s), transition=%s",
                event_type,
                event_tag,
                event_code,
                source_name,
                source_type,
                transition,
            )

            # Get space by hub_id
            space = None
            for s in self.coordinator.account.spaces.values():
                if s.hub_id == hub_id:
                    space = s
                    break

            if not space:
                _LOGGER.warning("SSE: Unknown hub %s", hub_id)
                return

            # Process event by type
            if event_tag in EVENT_TAG_TO_STATE:
                self._handle_security_event(space, event_tag, source_name)
            elif event_tag in DOOR_EVENTS:
                self._handle_door_event(space, event, event_tag)
            elif event_tag in MOTION_EVENTS:
                self._handle_motion_event(space, event, event_tag)
            elif event_tag in SMOKE_EVENTS:
                self._handle_smoke_event(space, event, event_tag)
            elif event_tag in FLOOD_EVENTS:
                self._handle_flood_event(space, event, event_tag)
            elif event_tag in GLASS_EVENTS:
                self._handle_glass_event(space, event, event_tag)
            elif event_tag in TAMPER_EVENTS:
                self._handle_tamper_event(space, event, event_tag)
            elif event_tag in DEVICE_STATUS_EVENTS:
                self._handle_device_status_event(space, event, event_tag)
            elif event_tag in RELAY_EVENTS:
                self._handle_relay_event(space, event, event_tag)
            else:
                _LOGGER.debug("SSE: Unhandled event tag: %s", event_tag)

            # Notify HA of update
            self.coordinator.async_set_updated_data(self.coordinator.account)

        except Exception as err:
            _LOGGER.error("SSE event processing error: %s", err, exc_info=True)

    def _handle_security_event(self, space, event_tag: str, source_name: str) -> None:
        """Handle arm/disarm/night mode events."""
        new_state = EVENT_TAG_TO_STATE.get(event_tag)
        if not new_state:
            return

        old_state = space.security_state
        state_changed = old_state != new_state

        _LOGGER.info(
            "SSE security: tag=%s, old=%s, new=%s, changed=%s",
            event_tag,
            old_state.value,
            new_state.value,
            state_changed,
        )

        # Check if this was triggered by Home Assistant
        if self.coordinator.get_pending_ha_action(space.hub_id):
            source_name = "Home Assistant"

        if state_changed:
            space.security_state = new_state
            self._last_state_update[space.hub_id] = time.time()

        # Always create notification (even if state unchanged)
        _LOGGER.info(
            "SSE instant: %s -> %s par %s (state_changed=%s)",
            old_state.value,
            new_state.value,
            source_name or "inconnu",
            state_changed,
        )

        # Create notification
        import asyncio

        asyncio.create_task(
            self.coordinator._create_sqs_notification(
                action=new_state.value,
                source_name=source_name,
                space_name=space.name,
            )
        )

    def _handle_door_event(self, space, event: dict, event_tag: str) -> None:
        """Handle door opened/closed events."""
        action_key, is_triggered = DOOR_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["door_opened"] = is_triggered
            dev.attributes["door_opened_at"] = datetime.now(timezone.utc).isoformat()
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_motion_event(self, space, event: dict, event_tag: str) -> None:
        """Handle motion detected events."""
        action_key, is_triggered = MOTION_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["motion_detected"] = is_triggered
            dev.attributes["motion_detected_at"] = datetime.now(
                timezone.utc
            ).isoformat()
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_smoke_event(self, space, event: dict, event_tag: str) -> None:
        """Handle smoke/fire detector events."""
        action_key, is_triggered = SMOKE_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            if "smoke" in action_key:
                dev.attributes["smoke_detected"] = is_triggered
            elif "temp" in action_key:
                dev.attributes["temperature_alert"] = is_triggered
            elif "co" in action_key:
                dev.attributes["co_detected"] = is_triggered
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_flood_event(self, space, event: dict, event_tag: str) -> None:
        """Handle flood/leak detector events."""
        action_key, is_triggered = FLOOD_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["leak_detected"] = is_triggered
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_glass_event(self, space, event: dict, event_tag: str) -> None:
        """Handle glass break events."""
        action_key, is_triggered = GLASS_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["glass_break_detected"] = is_triggered
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_tamper_event(self, space, event: dict, event_tag: str) -> None:
        """Handle tamper events."""
        action_key, is_triggered = TAMPER_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["tampered"] = is_triggered
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_device_status_event(self, space, event: dict, event_tag: str) -> None:
        """Handle device status events (online/offline, battery)."""
        action_key, is_problem = DEVICE_STATUS_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            if "online" in action_key or "offline" in action_key:
                dev.online = not is_problem
            elif "battery" in action_key:
                dev.attributes["low_battery"] = is_problem
            elif "power" in action_key:
                dev.attributes["external_power_lost"] = is_problem
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)

    def _handle_relay_event(self, space, event: dict, event_tag: str) -> None:
        """Handle relay/socket on/off events."""
        action_key, is_on = RELAY_EVENTS[event_tag]
        device = event.get("device", {})
        device_id = (
            device.get("id") if isinstance(device, dict) else event.get("deviceId")
        )

        if device_id and device_id in space.devices:
            dev = space.devices[device_id]
            dev.attributes["is_on"] = is_on
            _LOGGER.debug("SSE: %s %s", dev.name, action_key)
