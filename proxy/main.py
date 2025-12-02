"""Ajax Secure Proxy Server.

This proxy handles all communication with Ajax API:
- Injects API key into requests (users never see the key)
- Forwards requests to api.ajax.systems
- Provides SSE endpoint for real-time events

Architecture:
    [Home Assistant] <---> [This Proxy] <---> [Ajax API]
                               |
                               +---> [SSE] ---> [Home Assistant]
"""

import asyncio
import hashlib
import json
import logging
import os
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# Configuration
AJAX_API_URL = "https://api.ajax.systems"
AJAX_API_KEY = os.environ.get("AJAX_API_KEY", "")
PROXY_SECRET = os.environ.get("PROXY_SECRET", "")  # Optional: restrict access to proxy
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ajax-proxy")

# Store active sessions and SSE connections
sessions: dict[
    str, dict[str, Any]
] = {}  # session_token -> {user_id, ajax_token, created_at}
sse_clients: dict[str, asyncio.Queue] = {}  # session_token -> event queue


# Pydantic models
class LoginRequest(BaseModel):
    login: str
    passwordHash: str


class LoginResponse(BaseModel):
    sessionToken: str
    userId: str
    sseUrl: str


class TwoFARequest(BaseModel):
    requestId: str
    code: str


# Import SQS listener
try:
    from sqs_listener import start_sqs_listener, stop_sqs_listener

    SQS_AVAILABLE = True
except ImportError:
    SQS_AVAILABLE = False


async def push_event_to_clients(event: dict[str, Any], user_id: str | None = None):
    """Push an event to SSE clients.

    Args:
        event: Event data to push
        user_id: If specified, only push to this user's sessions
    """
    for token, session in sessions.items():
        if user_id and session["user_id"] != user_id:
            continue

        queue = sse_clients.get(token)
        if queue:
            await queue.put(event)


# Lifespan for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    logger.info("Ajax Secure Proxy starting...")
    if not AJAX_API_KEY:
        logger.warning("AJAX_API_KEY not set! Proxy will not work.")

    # Start SQS listener if available
    if SQS_AVAILABLE:
        sqs_started = await start_sqs_listener(push_event_to_clients)
        if sqs_started:
            logger.info("SQS listener started - real-time events enabled")
        else:
            logger.info("SQS not configured - using webhook mode only")

    yield

    logger.info("Ajax Secure Proxy shutting down...")

    # Stop SQS listener
    if SQS_AVAILABLE:
        await stop_sqs_listener()

    # Close all SSE connections
    for queue in sse_clients.values():
        await queue.put(None)
    sse_clients.clear()
    sessions.clear()


app = FastAPI(
    title="Ajax Secure Proxy",
    description="Secure proxy for Ajax Security Systems API",
    version="1.0.0",
    lifespan=lifespan,
)


def generate_proxy_token(user_id: str) -> str:
    """Generate a unique proxy session token."""
    data = f"{user_id}:{time.time()}:{os.urandom(16).hex()}"
    return hashlib.sha256(data.encode()).hexdigest()[:32]


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "active_sessions": len(sessions),
        "sse_clients": len(sse_clients),
    }


@app.post("/api/login", response_model=LoginResponse)
async def login(request: LoginRequest, req: Request):
    """Handle login - forward to Ajax API with API key."""
    logger.info(f"Login request for: {request.login}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{AJAX_API_URL}/api/login",
                headers={
                    "X-Api-Key": AJAX_API_KEY,
                    "Content-Type": "application/json",
                },
                json={
                    "login": request.login,
                    "passwordHash": request.passwordHash,
                },
                timeout=30.0,
            )

            if response.status_code == 200:
                data = response.json()
                ajax_token = data.get("sessionToken")
                user_id = data.get("userId")

                # Generate proxy token (different from Ajax token)
                proxy_token = generate_proxy_token(user_id)

                # Store session mapping
                sessions[proxy_token] = {
                    "user_id": user_id,
                    "ajax_token": ajax_token,
                    "email": request.login,
                    "created_at": time.time(),
                }

                # Create SSE queue for this session
                sse_clients[proxy_token] = asyncio.Queue()

                logger.info(f"Login successful for user {user_id}")

                # Return proxy token and SSE URL
                base_url = str(req.base_url).rstrip("/")
                return LoginResponse(
                    sessionToken=proxy_token,
                    userId=user_id,
                    sseUrl=f"{base_url}/api/events/stream",
                )

            elif response.status_code == 428:
                # 2FA required
                data = response.json()
                raise HTTPException(
                    status_code=428,
                    detail={
                        "error": "2fa_required",
                        "requestId": data.get("requestId"),
                        "message": "Two-factor authentication required",
                    },
                )
            else:
                logger.error(f"Ajax login failed: {response.status_code}")
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Authentication failed",
                )

        except httpx.RequestError as e:
            logger.error(f"Connection error: {e}")
            raise HTTPException(
                status_code=502, detail="Cannot connect to Ajax API"
            ) from None


@app.post("/api/2fa/verify")
async def verify_2fa(request: TwoFARequest, req: Request):
    """Verify 2FA code."""
    logger.info(f"2FA verification for request: {request.requestId}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{AJAX_API_URL}/api/2fa/verify",
                headers={
                    "X-Api-Key": AJAX_API_KEY,
                    "Content-Type": "application/json",
                },
                json={
                    "requestId": request.requestId,
                    "code": request.code,
                },
                timeout=30.0,
            )

            if response.status_code == 200:
                data = response.json()
                ajax_token = data.get("sessionToken")
                user_id = data.get("userId")

                # Generate proxy token
                proxy_token = generate_proxy_token(user_id)

                # Store session
                sessions[proxy_token] = {
                    "user_id": user_id,
                    "ajax_token": ajax_token,
                    "created_at": time.time(),
                }

                # Create SSE queue
                sse_clients[proxy_token] = asyncio.Queue()

                base_url = str(req.base_url).rstrip("/")
                return {
                    "sessionToken": proxy_token,
                    "userId": user_id,
                    "sseUrl": f"{base_url}/api/events/stream",
                }
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="2FA verification failed",
                )

        except httpx.RequestError as e:
            logger.error(f"Connection error: {e}")
            raise HTTPException(
                status_code=502, detail="Cannot connect to Ajax API"
            ) from None


def get_ajax_token(proxy_token: str) -> str:
    """Get Ajax token from proxy token."""
    session = sessions.get(proxy_token)
    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    return session["ajax_token"]


@app.api_route(
    "/api/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
)
async def proxy_request(path: str, request: Request):
    """Forward all API requests to Ajax with API key injection."""
    # Get proxy token from header
    proxy_token = request.headers.get("X-Session-Token")
    if not proxy_token:
        raise HTTPException(status_code=401, detail="Missing session token")

    # Get real Ajax token
    ajax_token = get_ajax_token(proxy_token)

    # Build target URL
    target_url = f"{AJAX_API_URL}/api/{path}"
    if request.query_params:
        target_url += f"?{request.query_params}"

    # Forward headers (excluding hop-by-hop)
    headers = {
        "X-Api-Key": AJAX_API_KEY,
        "X-Session-Token": ajax_token,
        "Content-Type": request.headers.get("Content-Type", "application/json"),
    }

    # Get request body
    body = await request.body()

    logger.debug(f"Proxying {request.method} {path}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                content=body if body else None,
                timeout=30.0,
            )

            # Return response
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers={
                    "Content-Type": response.headers.get(
                        "Content-Type", "application/json"
                    )
                },
            )

        except httpx.RequestError as e:
            logger.error(f"Proxy error: {e}")
            raise HTTPException(
                status_code=502, detail="Cannot connect to Ajax API"
            ) from None


@app.get("/api/events/stream")
async def sse_stream(request: Request):
    """SSE endpoint for real-time events."""
    proxy_token = request.headers.get("X-Session-Token")
    if not proxy_token or proxy_token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid session")

    logger.info(f"SSE client connected: {proxy_token[:8]}...")

    async def event_generator():
        """Generate SSE events."""
        queue = sse_clients.get(proxy_token)
        if not queue:
            return

        try:
            # Send initial connection event
            yield f"event: connected\ndata: {json.dumps({'status': 'connected'})}\n\n"

            while True:
                try:
                    # Wait for events with timeout (keepalive)
                    event = await asyncio.wait_for(queue.get(), timeout=30.0)

                    if event is None:
                        # Shutdown signal
                        break

                    yield f"event: {event.get('eventType', 'message')}\ndata: {json.dumps(event)}\n\n"

                except asyncio.TimeoutError:
                    # Send keepalive comment
                    yield ": keepalive\n\n"

        except asyncio.CancelledError:
            logger.info(f"SSE client disconnected: {proxy_token[:8]}...")
        finally:
            # Cleanup on disconnect
            if proxy_token in sse_clients:
                del sse_clients[proxy_token]

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# Webhook endpoint for receiving events from Ajax (if using webhook mode)
@app.post("/webhook/events")
async def receive_webhook(request: Request):
    """Receive events from Ajax webhook and forward to SSE clients."""
    try:
        event = await request.json()
        logger.info(f"Received webhook event: {event.get('eventTag', 'unknown')}")

        # Push to all connected clients
        await push_event_to_clients(event)

        return {"status": "ok"}

    except Exception as e:
        logger.error(f"Webhook error: {e}")
        raise HTTPException(status_code=400, detail="Invalid event data") from None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        reload=True,
    )
