"""MCP tool surface. All blocking work leaves the event loop free for stop."""
from __future__ import annotations

import asyncio
import base64
import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, ImageContent, TextContent, ToolAnnotations

from .core import ScoutError


def tool_result(value):
    value = dict(value)
    images = value.pop('preview_jpegs',[])
    if 'preview_jpeg' in value:
        images.append(value.pop('preview_jpeg'))
    return CallToolResult(structuredContent=value,content=[
        TextContent(type='text',text=json.dumps(value,allow_nan=False)),
        *[ImageContent(type='image',data=base64.b64encode(data).decode(),mimeType='image/jpeg') for data in images],
    ])


def make_server(scout):
    server = FastMCP('game_scout',instructions=(
        'Scout Cyberpunk 2077 with FreeFly. Begin a session before controlling the camera. '
        'Coordinates are world-space ACTIVE CAMERA coordinates, metres, yaw degrees (0=+Y,90=-X), '
        'pitch positive up. Inspect u/v are 0..1 left-to-right/top-to-bottom in the latest image. '
        'Observe after manual camera changes. Prefer short collision-checked movement. '
        'Long travel requires allow_teleport. Scout/replay jobs run in background; use job_status, '
        'get_record and read_image for results. Stop interrupts immediately and releases camera control. '
        'FreeFly remains under player control. Semantic exploration is performed by the calling model; '
        'autonomous_scout is a bounded geometric coverage walker. End sessions when finished.'))

    async def invoke(function, *args, **kwargs):
        try:
            return tool_result(await asyncio.to_thread(function,*args,**kwargs))
        except asyncio.CancelledError:
            scout.stop()
            raise
        except (ScoutError,ValueError,KeyError,OSError) as error:
            return CallToolResult(isError=True,content=[TextContent(type='text',text=str(error))])

    read_only = ToolAnnotations(readOnlyHint=True,destructiveHint=False,openWorldHint=False)
    control = ToolAnnotations(readOnlyHint=False,destructiveHint=False,openWorldHint=False)

    @server.tool(annotations=read_only)
    async def state() -> CallToolResult:
        """Read live runtime state, active camera pose, loading, flight and ownership; no screenshot."""
        return await invoke(scout.bridge.state)

    @server.tool(annotations=control)
    async def begin_session(hide_hud: bool=True) -> CallToolResult:
        """Acquire game control and return a preview. Activate FreeFly and close CET first."""
        return await invoke(scout.begin,hide_hud)

    @server.tool(annotations=control)
    async def end_session() -> CallToolResult:
        """Release camera/HUD changes and controller locks. Does not disable the player's FreeFly."""
        return await invoke(scout.end)

    @server.tool(annotations=read_only)
    async def observe() -> CallToolResult:
        """See a fresh game-window image and actual pose. During jobs returns status without competing capture."""
        return await invoke(scout.observe)

    @server.tool(annotations=control)
    async def move(forward: float=0,right: float=0,up: float=0,duration: float=2,collision: bool=True) -> CallToolResult:
        """Move relative to the camera by metres, then return a fresh image. Up is world vertical; 50 m limit."""
        return await invoke(scout.move,forward,right,up,duration,collision)

    @server.tool(annotations=control)
    async def go_to(pose: dict[str,float] | None=None,viewpoint_id: str | None=None,duration: float=2,
                    allow_teleport: bool=False,collision: bool=True) -> CallToolResult:
        """Visit camera pose {x,y,z,yaw,pitch} or a saved viewpoint, and return an image. Teleport explicitly bypasses path collision."""
        return await invoke(scout.go_to,pose,viewpoint_id,duration,allow_teleport,collision)

    @server.tool(annotations=control)
    async def look_at(target: dict[str,float] | None=None,yaw_delta: float=0,pitch_delta: float=0) -> CallToolResult:
        """Aim at world {x,y,z}, or turn by relative degrees, and return an image."""
        return await invoke(scout.look,yaw_delta,pitch_delta,target)

    @server.tool(annotations=control)
    async def inspect(u: float=0.5,v: float=0.5,range_m: float=100) -> CallToolResult:
        """Raycast a point in the latest image; return nearest hit position and optional entity identity. Camera must be unchanged."""
        return await invoke(scout.inspect,u,v,range_m)

    @server.tool(annotations=control)
    async def capture(name: str='Scout capture') -> CallToolResult:
        """Save an original-resolution PNG and pose sidecar, returning a preview and image ID."""
        return await invoke(scout.capture,name)

    @server.tool(annotations=control)
    async def sweep(yaw_offsets: list[float] | None=None,pitch: float | None=None,save: bool=True) -> CallToolResult:
        """Capture 1–12 angles from the same position, default -45/0/+45; returns each image preview."""
        return await invoke(scout.sweep,yaw_offsets,pitch,save)

    @server.tool(annotations=control)
    async def orbit(center: dict[str,float],radius_m: float=5,height_m: float=0,count: int=4,save: bool=True) -> CallToolResult:
        """Capture 2–12 viewpoints around a world target, looking inward. Blocked paths are reported and skipped."""
        return await invoke(scout.orbit,center,radius_m,height_m,count,save)

    @server.tool(annotations=control)
    async def save_viewpoint(name: str,notes: str='',tags: list[str] | None=None,location_id: str | None=None) -> CallToolResult:
        """Save a named camera pose, original image and notes; optionally attach it to a location."""
        return await invoke(scout.save_viewpoint,name,notes,tags,location_id)

    @server.tool(annotations=control)
    async def save_location(name: str,description: str='',tags: list[str] | None=None,
                            viewpoint_ids: list[str] | None=None,location_id: str | None=None) -> CallToolResult:
        """Create/update a quest location with a description, tags and independent viewpoints."""
        return await invoke(scout.save_location,name,description,tags,viewpoint_ids,location_id)

    @server.tool(annotations=control)
    async def connect_locations(from_id: str,to_id: str,kind: str,description: str='',bidirectional: bool=True) -> CallToolResult:
        """Record an observed passage, stairs, entrance or other connection between saved locations."""
        return await invoke(scout.connect,from_id,to_id,kind,description,bidirectional)

    @server.tool(annotations=read_only)
    async def search_library(kind: str | None=None,query: str='',limit: int=50) -> CallToolResult:
        """Search saved locations/viewpoints/images/routes/jobs/connections by name, notes or tags."""
        return await invoke(lambda: {'records':scout.library.list(kind,query,limit)})

    @server.tool(annotations=read_only)
    async def coverage(limit: int=200) -> CallToolResult:
        """Read visited 8 m 3D cells and 45-degree heading sectors; floors at different heights remain distinct."""
        return await invoke(scout.library.coverage,limit)

    @server.tool(annotations=read_only)
    async def get_record(record_id: str) -> CallToolResult:
        """Read a complete saved record, including route waypoints or job output image IDs."""
        return await invoke(scout.library.get,record_id)

    @server.tool(annotations=read_only)
    async def read_image(image_id: str) -> CallToolResult:
        """Show a saved image by library ID, with its recorded camera metadata."""
        def read():
            from PIL import Image
            record = scout.library.get(image_id)
            if record['kind'] != 'image':
                raise ScoutError('Expected an image record')
            path = Path(record['data']['path']).resolve()
            if not path.is_relative_to(scout.library.root.resolve()/'images'):
                raise ScoutError('Image path is outside the scout library')
            with Image.open(path) as image:
                return {'record':record,'preview_jpeg':scout.images.preview(image)}
        return await invoke(read)

    @server.tool(annotations=control)
    async def record_route(name: str | None=None) -> CallToolResult:
        """Start recording with a name; omit name to finish. Completed movement and capture poses are persisted."""
        return await invoke(scout.record_route,name)

    @server.tool(annotations=control)
    async def replay_route(route_id: str,capture: bool=True,allow_teleport: bool=False,maximum_seconds: float=600,start_index: int=0) -> CallToolResult:
        """Start a background route replay, optionally capturing every waypoint; poll job_status and use stop to interrupt."""
        return await invoke(scout.start_job,'replay',route_id=route_id,capture=capture,allow_teleport=allow_teleport,maximum_seconds=maximum_seconds,start_index=start_index)

    @server.tool(annotations=control)
    async def autonomous_scout(maximum_steps: int=20,radius_m: float=100,step_m: float=8,maximum_seconds: float=600) -> CallToolResult:
        """Start bounded geometric exploration using collision clearance and 3D coverage novelty; saves images and a replayable route."""
        return await invoke(scout.start_job,'scout',maximum_steps=maximum_steps,radius_m=radius_m,step_m=step_m,maximum_seconds=maximum_seconds)

    @server.tool(annotations=read_only)
    async def job_status() -> CallToolResult:
        """Read job progress, saved image IDs, route ID and the stop/failure reason."""
        return await invoke(scout.job_status)

    @server.tool(annotations=control)
    async def stop() -> CallToolResult:
        """Interrupt movement, image capture or background work out of band; release game-side camera/HUD control."""
        return await invoke(scout.stop)

    @server.tool(annotations=control)
    async def export_library() -> CallToolResult:
        """Export locations, viewpoints, connections, image metadata, routes and coverage into a standalone JSON bundle."""
        return await invoke(lambda: {'export_path':scout.library.export()})

    @server.resource('scout://library')
    def library_resource() -> str:
        return json.dumps(scout.library.list(limit=50))

    @server.prompt()
    def explore_for_quests(start_description: str) -> str:
        return (f'Explore {start_description} using Game Scout. Observe before moving. Follow visible passages, stairs, '
                'courtyards and entrances with short moves and inspect image points for world targets. Save useful '
                'spaces as locations with viewpoints showing layout and connections. Describe concrete physical '
                'features useful for quest staging. Record routes for later replay. Use geometric autonomous_scout '
                'only within a bounded area, review its saved images, and end the session when finished.')

    return server
