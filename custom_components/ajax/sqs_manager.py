"""SQS Manager for Ajax real-time events.

This module manages the integration between AWS SQS events and the Ajax coordinator.
It acts as a bridge between real-time events and the REST API polling system.
"""

from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any, Callable

from .event_parser import AjaxEventParser

if TYPE_CHECKING:
    from .coordinator import AjaxDataCoordinator
    from .sqs_client import AjaxSQSClient

_LOGGER = logging.getLogger(__name__)


class SQSManager:
    """Manager for AWS SQS real-time event integration."""

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        sqs_client: AjaxSQSClient,
    ) -> None:
        """Initialize SQS manager.

        Args:
            coordinator: Ajax data coordinator
            sqs_client: SQS client instance
        """
        self.coordinator = coordinator
        self.sqs_client = sqs_client
        self.parser = AjaxEventParser()

        self._enabled = False
        self._last_event_time: float = 0.0

        _LOGGER.debug("SQS Manager initialized")

    async def start(self) -> bool:
        """Start SQS event receiving.

        Returns:
            True if started successfully
        """
        try:
            # Connect to SQS
            if not await self.sqs_client.connect():
                _LOGGER.error("Failed to connect to SQS")
                return False

            # Set event callback
            self.sqs_client.event_callback = self._handle_event

            # Start receiving
            await self.sqs_client.start_receiving()

            self._enabled = True
            _LOGGER.info("SQS Manager started successfully")
            return True

        except Exception as err:
            _LOGGER.error("Failed to start SQS Manager: %s", err)
            return False

    async def stop(self) -> None:
        """Stop SQS event receiving."""
        self._enabled = False

        try:
            await self.sqs_client.stop_receiving()
            await self.sqs_client.close()
            _LOGGER.info("SQS Manager stopped")
        except Exception as err:
            _LOGGER.error("Error stopping SQS Manager: %s", err)

    async def _handle_event(self, event_data: dict[str, Any]) -> None:
        """Handle received SQS event.

        Args:
            event_data: Raw event data from SQS
        """
        if not self._enabled:
            return

        try:
            # Parse event
            event = self.parser.parse_event(event_data)
            if not event:
                return

            _LOGGER.info(
                "Received Ajax event: %s - %s (%s)",
                event["event_type"],
                event["action"],
                event["source_name"],
            )

            # Update last event time
            self._last_event_time = event.get("timestamp", 0)

            # Store event in space recent_events (keep last 5)
            space_id = event.get("space_id")
            if space_id and self.coordinator.account:
                space = self.coordinator.account.spaces.get(space_id)
                if space:
                    # Add event to beginning of list
                    space.recent_events.insert(0, event)
                    # Keep only last 5 events
                    space.recent_events = space.recent_events[:5]

            # Trigger coordinator update based on event type
            await self._process_event(event)

        except Exception as err:
            _LOGGER.error("Error handling SQS event: %s", err)

    async def _process_event(self, event: dict[str, Any]) -> None:
        """Process parsed event and trigger appropriate actions.

        Args:
            event: Parsed event dict
        """
        # Determine if we should fast poll
        should_fast_poll = self.parser.should_trigger_fast_poll(event)

        if should_fast_poll:
            _LOGGER.debug("Event triggers fast poll: %s", event["action"])

        # Always trigger an immediate coordinator refresh for real-time updates
        await self.coordinator.async_request_refresh()

        # Handle specific event types
        if self.parser.is_alarm_event(event):
            await self._handle_alarm_event(event)
        elif self.parser.is_arming_event(event):
            await self._handle_arming_event(event)
        elif self.parser.is_malfunction_event(event):
            await self._handle_malfunction_event(event)
        elif self.parser.is_connection_event(event):
            await self._handle_connection_event(event)

    async def _handle_alarm_event(self, event: dict[str, Any]) -> None:
        """Handle alarm event.

        Args:
            event: Parsed alarm event
        """
        action = event["action"]
        source_name = event["source_name"]
        is_active = event["is_active"]

        _LOGGER.warning(
            "ALARM: %s - %s (%s)",
            action,
            source_name,
            "TRIGGERED" if is_active else "CLEARED",
        )

        # Create Home Assistant persistent notification if configured
        if hasattr(self.coordinator, "hass"):
            from homeassistant.components.persistent_notification import async_create

            message = f"Ajax Alarm: {action.replace('_', ' ').title()}\n"
            message += f"Device: {source_name}\n"
            message += f"Status: {'TRIGGERED' if is_active else 'CLEARED'}\n"
            message += f"Time: {event['event_time']}"

            async_create(
                self.coordinator.hass,
                message=message,
                title="Ajax Security Alert",
                notification_id=f"ajax_alarm_{event['event_id']}",
            )

    async def _handle_arming_event(self, event: dict[str, Any]) -> None:
        """Handle arming/disarming event.

        Args:
            event: Parsed arming event
        """
        action = event["action"]
        _LOGGER.info("Hub arming state changed: %s", action)

        # Trigger hub state update
        await self.coordinator.async_request_refresh()

    async def _handle_malfunction_event(self, event: dict[str, Any]) -> None:
        """Handle malfunction event.

        Args:
            event: Parsed malfunction event
        """
        action = event["action"]
        source_name = event["source_name"]
        is_active = event["is_active"]

        _LOGGER.warning(
            "MALFUNCTION: %s - %s (%s)",
            action,
            source_name,
            "TRIGGERED" if is_active else "CLEARED",
        )

        # Trigger device update
        await self.coordinator.async_request_refresh()

    async def _handle_connection_event(self, event: dict[str, Any]) -> None:
        """Handle connection/offline event.

        Args:
            event: Parsed connection event
        """
        source_name = event["source_name"]
        is_active = event["is_active"]

        _LOGGER.info(
            "Device connection: %s (%s)",
            source_name,
            "OFFLINE" if is_active else "ONLINE",
        )

        # Trigger device update
        await self.coordinator.async_request_refresh()

    @property
    def is_enabled(self) -> bool:
        """Check if SQS is enabled and running.

        Returns:
            True if enabled
        """
        return self._enabled

    @property
    def last_event_time(self) -> float:
        """Get timestamp of last received event.

        Returns:
            Unix timestamp
        """
        return self._last_event_time
