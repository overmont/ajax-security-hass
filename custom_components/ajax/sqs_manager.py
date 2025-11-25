"""SQS Manager for Ajax real-time events.

Architecture:
- SQS events are used for INSTANT state updates (< 1 second)
- REST API polling confirms state periodically (fallback)
- SQS events directly update coordinator state for fastest response
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Any

from .models import SecurityState

if TYPE_CHECKING:
    from .coordinator import AjaxDataCoordinator
    from .sqs_client import AjaxSQSClient

_LOGGER = logging.getLogger(__name__)

# Map SQS event tags to SecurityState
EVENT_TAG_TO_STATE = {
    "arm": SecurityState.ARMED,
    "disarm": SecurityState.DISARMED,
    "nightmodeon": SecurityState.NIGHT_MODE,
    "partialarm": SecurityState.PARTIALLY_ARMED,
}


class SQSManager:
    """Manager for AWS SQS real-time event integration."""

    # Don't let REST overwrite SQS state for this many seconds
    STATE_PROTECTION_SECONDS = 15.0

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        sqs_client: AjaxSQSClient,
    ) -> None:
        self.coordinator = coordinator
        self.sqs_client = sqs_client
        self._enabled = False
        self._last_event_time: float = 0.0
        self._last_state_update: dict[str, float] = {}  # hub_id -> timestamp

    async def start(self) -> bool:
        try:
            if not await self.sqs_client.connect():
                _LOGGER.error("Failed to connect to SQS")
                return False

            self.sqs_client.event_callback = self._handle_event
            await self.sqs_client.start_receiving()

            self._enabled = True
            _LOGGER.info("SQS Manager started")
            return True

        except Exception as err:
            _LOGGER.error("Failed to start SQS Manager: %s", err)
            return False

    async def stop(self) -> None:
        self._enabled = False
        try:
            await self.sqs_client.stop_receiving()
            await self.sqs_client.close()
            _LOGGER.info("SQS Manager stopped")
        except Exception as err:
            _LOGGER.error("Error stopping SQS Manager: %s", err)

    async def _handle_event(self, event_data: dict[str, Any]) -> None:
        """Handle SQS event by directly updating state (instant response).

        SQS events contain the new state, so we update immediately
        without waiting for REST API polling.
        """
        if not self._enabled:
            return

        try:
            self._last_event_time = time.time()

            # Extract event info
            event = event_data.get("event", {})
            event_tag = event.get("eventTag", "").lower()
            hub_id = event.get("hubId", "")
            source_name = event.get("sourceObjectName", "")
            source_type = event.get("sourceObjectType", "")

            _LOGGER.debug(
                "SQS event data: tag=%s, source=%s (%s)",
                event_tag, source_name, source_type
            )

            if not hub_id or not event_tag:
                _LOGGER.debug("SQS event missing hubId or eventTag")
                return

            # Check if this is a security state change event
            new_state = EVENT_TAG_TO_STATE.get(event_tag)
            if not new_state:
                _LOGGER.debug("SQS event %s not a state change", event_tag)
                return

            # Find the space for this hub
            space = None
            for s in self.coordinator.account.spaces.values():
                if s.hub_id == hub_id or s.id == hub_id:
                    space = s
                    break

            if not space:
                _LOGGER.warning("SQS: No space found for hub %s", hub_id)
                return

            # Update state directly from SQS (instant!)
            old_state = space.security_state
            if old_state != new_state:
                space.security_state = new_state
                self._last_state_update[hub_id] = time.time()

                # Check if this was triggered by Home Assistant
                if self.coordinator.get_pending_ha_action(hub_id):
                    source_name = "Home Assistant"

                # Log with source info if available
                if source_name:
                    _LOGGER.info(
                        "SQS instant: %s -> %s par %s",
                        old_state.value, new_state.value, source_name
                    )
                else:
                    _LOGGER.info(
                        "SQS instant: %s -> %s",
                        old_state.value, new_state.value
                    )

                # Create event for the sensor (with source info)
                self.coordinator._create_event_from_sqs(
                    space, old_state, new_state, source_name
                )

                # Notify listeners (update UI immediately)
                self.coordinator.async_set_updated_data(self.coordinator.account)

        except Exception as err:
            _LOGGER.error("Error handling SQS event: %s", err)

    def is_state_protected(self, hub_id: str) -> bool:
        """Check if state was recently updated by SQS (protected from REST overwrite).

        Args:
            hub_id: Hub ID to check

        Returns:
            True if state should not be overwritten by REST polling
        """
        last_update = self._last_state_update.get(hub_id, 0)
        elapsed = time.time() - last_update
        is_protected = elapsed < self.STATE_PROTECTION_SECONDS
        if is_protected:
            _LOGGER.debug(
                "Hub %s state protected (%.1fs since SQS update)",
                hub_id, elapsed
            )
        return is_protected

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    @property
    def last_event_time(self) -> float:
        return self._last_event_time
