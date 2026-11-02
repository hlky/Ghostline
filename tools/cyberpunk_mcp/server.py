"""MCP tools for ordinary gameplay with FreeFly disabled."""
from __future__ import annotations

import asyncio
import base64
import json

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, ImageContent, TextContent, ToolAnnotations

from .core import GameplayError


def make_server(game):
    server = FastMCP('cyberpunk_mcp', instructions=(
        'Play Cyberpunk 2077 using normal keyboard/mouse input. Disable FreeFly, close CET/menus, '
        'unpause and focus the game before begin_session. Observe, act briefly, then inspect the '
        'returned image and telemetry. Actions release all their keys and return fresh evidence. '
        'walk is on-foot; drive requires a mounted vehicle. interact uses the visible contextual prompt '
        'and can open doors, talk or enter a vehicle. Input completion does not prove objective success. '
        'Look uses relative mouse counts, not degrees. Throttle/steer use keyboard duty cycles, '
        'not native analog axes. Negative throttle brakes then reverses. Zero throttle coasts. '
        'Use brake or handbrake to stop the vehicle. No action exceeds two seconds. '
        'F8, the CET emergency-stop hotkey or stop interrupts control. End sessions when finished.'))
    read = ToolAnnotations(readOnlyHint=True, destructiveHint=False, openWorldHint=False)
    control = ToolAnnotations(readOnlyHint=False, destructiveHint=True, openWorldHint=False)

    async def invoke(function, *args, **kwargs):
        try:
            value = dict(await asyncio.to_thread(function, *args, **kwargs))
            preview = value.pop('preview_jpeg', None)
            content = [TextContent(type='text', text=json.dumps(value, allow_nan=False))]
            if preview:
                content.append(ImageContent(type='image', data=base64.b64encode(preview).decode(), mimeType='image/jpeg'))
            return CallToolResult(structuredContent=value, content=content)
        except asyncio.CancelledError:
            game.stop()
            raise
        except (GameplayError, ValueError, KeyError, OSError) as error:
            return CallToolResult(isError=True, content=[TextContent(type='text', text=str(error))])

    @server.tool(annotations=read)
    async def capabilities() -> CallToolResult:
        """Read input bindings and limits without taking game control."""
        return await invoke(lambda: {'backend': 'windows_sendinput_scancodes', 'max_action_seconds': 2,
                                    'bindings': game.bindings, 'freefly_required': False,
                                    'freefly_must_be_disabled': True, 'emergency_stop_key': 'F8',
                                    'look_units': 'relative mouse counts', 'driving_axes': 'keyboard duty cycle'})

    @server.tool(annotations=read)
    async def state() -> CallToolResult:
        """Read live readiness, player position, camera, vehicle mode and session."""
        return await invoke(game.state)

    @server.tool(annotations=read)
    async def observe() -> CallToolResult:
        """Capture the game window and telemetry without enabling FreeFly or acquiring input."""
        return await invoke(game.observe)

    @server.tool(annotations=control)
    async def begin_session() -> CallToolResult:
        """Acquire exclusive gameplay ownership. Requires loaded, unpaused gameplay and FreeFly off."""
        return await invoke(game.begin)

    @server.tool(annotations=control)
    async def walk(forward: float=0, right: float=0, seconds: float=0.4, sprint: bool=False,
                   mouse_dx: float=0, mouse_dy: float=0) -> CallToolResult:
        """Move on foot: axes -1..1, duration 0.05..2 s; optional simultaneous mouse turn."""
        return await invoke(game.walk, forward, right, seconds, sprint, mouse_dx, mouse_dy)

    @server.tool(annotations=control)
    async def look(mouse_dx: float=0, mouse_dy: float=0, seconds: float=0.2) -> CallToolResult:
        """Turn the view with relative mouse counts. Positive dx right, positive dy down; sensitivity is game-dependent."""
        return await invoke(game.look, mouse_dx, mouse_dy, seconds)

    @server.tool(annotations=control)
    async def interact(seconds: float=0.15) -> CallToolResult:
        """Press/hold the interact binding for the visible prompt: door, conversation, loot or vehicle entry."""
        return await invoke(game.press, 'interact', seconds)

    @server.tool(annotations=control)
    async def press_action(action: str, seconds: float=0.15) -> CallToolResult:
        """Press interact, exit_vehicle, jump or crouch. Vehicle exit may require a longer hold."""
        return await invoke(game.press, action, seconds)

    @server.tool(annotations=control)
    async def drive(throttle: float=0, steer: float=0, seconds: float=0.4,
                    handbrake: bool=False) -> CallToolResult:
        """Drive a mounted vehicle. Throttle -1 brake/reverse to +1 accelerate; steer -1 left to +1 right. Zero coasts."""
        return await invoke(game.drive, throttle, steer, seconds, handbrake)

    @server.tool(annotations=control)
    async def stop() -> CallToolResult:
        """Interrupt inputs and end ownership. Releases keys; does not physically brake a coasting vehicle."""
        return await invoke(game.stop)

    @server.tool(annotations=control)
    async def end_session() -> CallToolResult:
        """Stop inputs and release session locks. If an action is still releasing, retry once it finishes."""
        return await invoke(game.end)

    @server.tool(annotations=read)
    async def get_record(record_id: str) -> CallToolResult:
        """Read saved action evidence or image metadata."""
        return await invoke(game.library.get, record_id)

    return server
