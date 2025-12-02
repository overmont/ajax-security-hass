"""SQS Listener for Ajax events.

This module connects to AWS SQS to receive Ajax events
and pushes them to connected SSE clients.
"""

import asyncio
import contextlib
import json
import logging
import os
from typing import Any

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger("ajax-proxy.sqs")

# AWS Configuration
AWS_REGION = os.environ.get("AWS_REGION", "eu-west-1")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
SQS_QUEUE_NAME = os.environ.get("SQS_QUEUE_NAME", "")


class SQSListener:
    """Listen to SQS queue and forward events to SSE clients."""

    def __init__(self, event_callback):
        """Initialize SQS listener.

        Args:
            event_callback: Async function to call with each event
        """
        self.event_callback = event_callback
        self._running = False
        self._task: asyncio.Task | None = None
        self._sqs_client = None
        self._queue_url: str | None = None

    async def start(self) -> bool:
        """Start listening to SQS."""
        if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, SQS_QUEUE_NAME]):
            logger.warning("AWS SQS credentials not configured")
            return False

        try:
            # Create SQS client
            self._sqs_client = boto3.client(
                "sqs",
                region_name=AWS_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )

            # Get queue URL
            response = self._sqs_client.get_queue_url(QueueName=SQS_QUEUE_NAME)
            self._queue_url = response["QueueUrl"]

            logger.info(f"Connected to SQS queue: {SQS_QUEUE_NAME}")

            # Start polling task
            self._running = True
            self._task = asyncio.create_task(self._poll_loop())

            return True

        except ClientError as e:
            logger.error(f"Failed to connect to SQS: {e}")
            return False

    async def stop(self):
        """Stop listening to SQS."""
        self._running = False
        if self._task:
            self._task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._task
        logger.info("SQS listener stopped")

    async def _poll_loop(self):
        """Main polling loop."""
        while self._running:
            try:
                # Run blocking SQS call in thread pool
                messages = await asyncio.get_event_loop().run_in_executor(
                    None, self._receive_messages
                )

                for message in messages:
                    await self._process_message(message)

                # Small delay between polls
                await asyncio.sleep(0.1)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"SQS poll error: {e}")
                await asyncio.sleep(5)

    def _receive_messages(self) -> list[dict[str, Any]]:
        """Receive messages from SQS (blocking)."""
        if not self._sqs_client or not self._queue_url:
            return []

        try:
            response = self._sqs_client.receive_message(
                QueueUrl=self._queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=5,  # Long polling
                AttributeNames=["All"],
                MessageAttributeNames=["All"],
            )
            return response.get("Messages", [])

        except ClientError as e:
            logger.error(f"SQS receive error: {e}")
            return []

    async def _process_message(self, message: dict[str, Any]):
        """Process a single SQS message."""
        try:
            # Parse message body
            body = json.loads(message.get("Body", "{}"))

            # Extract event data (may be nested in 'Message' for SNS)
            if "Message" in body:
                event_data = json.loads(body["Message"])
            else:
                event_data = body

            logger.debug(f"Received event: {event_data.get('eventTag', 'unknown')}")

            # Forward to callback
            await self.event_callback(event_data)

            # Delete message from queue
            self._sqs_client.delete_message(
                QueueUrl=self._queue_url,
                ReceiptHandle=message["ReceiptHandle"],
            )

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in SQS message: {e}")
        except Exception as e:
            logger.error(f"Error processing SQS message: {e}")


# Integration with main app
_sqs_listener: SQSListener | None = None


async def start_sqs_listener(event_callback):
    """Start the global SQS listener."""
    global _sqs_listener
    _sqs_listener = SQSListener(event_callback)
    return await _sqs_listener.start()


async def stop_sqs_listener():
    """Stop the global SQS listener."""
    global _sqs_listener
    if _sqs_listener:
        await _sqs_listener.stop()
        _sqs_listener = None
