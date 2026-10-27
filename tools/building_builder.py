#!/usr/bin/env python3
"""Compile an editable room layout into vanilla modules and native world assets.

Layouts use RED X/Y/Z coordinates and metres. Cell coordinates are integers on
the curated kit's three-metre grid. The browser and exporter consume the same
compiled scene; no World Builder installation is required.
"""
from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import subprocess
import shutil
import tempfile

from artifact_io import atomic_write_json
from generate_world import (
    HandleAllocator, Vec3, cname, descriptor, node_data, resource_path,
    streaming_sector, trigger_node,
)
from toolchain import resolve_tool

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "generated/building-editor"
PROJECT = ROOT / "projects/experiments/building-lab"
KIT_PATH = ROOT / "tools/building_ui/common-kit.json"
ID = re.compile(r"^[a-z][a-z0-9_-]{0,47}$")
SIDES = ("south", "east", "north", "west")


class BuildingError(ValueError):
    """An actionable layout or export error."""


def kits():
    extra = [json.loads(path.read_bytes()) for path in (KIT_PATH.parent / "kits").glob("*.json")]
    return [json.loads(KIT_PATH.read_bytes())] + sorted(extra, key=lambda entry: entry["name"].casefold())


def kit(identity="common-3m"):
    for catalog in kits():
        if catalog["id"] == identity:
            return catalog
    raise BuildingError("Select a supported building kit")


def number(value, name, low=-8000, high=8000):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise BuildingError(f"{name} must be a finite number")
    if not low <= value <= high:
        raise BuildingError(f"{name} must be between {low} and {high}")
    return float(value)


def layout_kit(layout):
    catalog = kit(layout.get("kit"))
    if catalog['id']=='rancho-3m' and layout.get('fit_walls_to_storeys'):
        # The plaster body is 15 cm deep; the 17.5 cm overall bound includes
        # skirting. Reverse facings meet on the body plane, not that trim tip.
        catalog['wall_thickness']=.15
    if "storey_height" in layout:
        catalog["storey_height"] = number(layout["storey_height"], "Surveyed storey height", 3, 6)
    return catalog


def grid_number(value, name, low=-60, high=60):
    value = number(value, name, low, high)
    if abs(value / 3 - round(value / 3)) > 1e-8:
        raise BuildingError(f"{name} must be a multiple of 3 m")
    return round(value / 3)


def edge_key(level, axis, x, y):
    return f"{level}:{axis}:{x}:{y}"


def normalize(layout):
    if not isinstance(layout, dict) or layout.get("schema_version") != 1:
        raise BuildingError("Expected a version 1 building layout")
    if not isinstance(layout.get("id"), str) or not ID.fullmatch(layout["id"]):
        raise BuildingError("Layout id must start with a lowercase letter and contain letters, numbers, _ or -")
    catalog = layout_kit(layout)
    result = copy.deepcopy(layout)
    if not isinstance(result.get("name"), str) or not result["name"].strip() or len(result["name"]) > 100:
        raise BuildingError("Give the layout a name of at most 100 characters")
    origin = result.get("origin", {})
    if not isinstance(origin, dict):
        raise BuildingError("World anchor must be an object")
    result["origin"] = {axis: number(origin.get(axis, 0), f"World {axis}", -8000 if axis != "yaw" else -360, 8000 if axis != "yaw" else 360) for axis in ("x", "y", "z", "yaw")}
    if not isinstance(result.get("rooms"), list) or not 0 <= len(result["rooms"]) <= 32:
        raise BuildingError("A layout supports at most 32 rooms")
    used = set()
    cells = {}
    for room in result["rooms"]:
        if not isinstance(room, dict) or not isinstance(room.get("id"), str) or not ID.fullmatch(room["id"]) or room["id"] in used:
            raise BuildingError("Room ids must be unique lowercase identifiers")
        used.add(room["id"])
        if not isinstance(room.get("name"), str) or not room["name"].strip() or len(room["name"]) > 80:
            raise BuildingError(f"Give room {room['id']} a name of at most 80 characters")
        level = number(room.get("level", 0), "Floor level", 0, 3)
        if int(level) != level:
            raise BuildingError("Floor level must be a whole number")
        room["level"] = int(level)
        x, y = (grid_number(room.get(axis), f"{room['name']} {axis}") for axis in ("x", "y"))
        w, d = (grid_number(room.get(axis), f"{room['name']} {axis}", 3, 30) for axis in ("width", "depth"))
        if "ceiling_height" in room:
            room["ceiling_height"] = number(room["ceiling_height"], "Room ceiling height", 2.4, catalog["wall_height"])
        if x + w > 20 or y + d > 20:
            raise BuildingError("Rooms must stay inside the -60 to +60 m workspace")
        for cx in range(x, x + w):
            for cy in range(y, y + d):
                cell = (room["level"], cx, cy)
                if cell in cells:
                    raise BuildingError(f"{room['name']} overlaps {cells[cell]} on floor {room['level'] + 1}")
                cells[cell] = room["id"]
    if len(cells) > 600:
        raise BuildingError("This prototype supports at most 600 floor tiles")
    if not isinstance(result.get("openings", {}), dict):
        raise BuildingError("Openings must be a map of wall ids to opening types")
    result.setdefault("openings", {})
    if len(result["openings"]) > 1000:
        raise BuildingError("Too many openings")
    for key, value in result["openings"].items():
        if not isinstance(key, str):
            raise BuildingError("Opening wall ids must be strings")
        if value not in ("doorway", "passage", "door_auto", "door_manual", "window"):
            raise BuildingError("Choose a doorway, passage or interactive door")
    from building_features import DOOR_PRESETS
    devices = result.get("door_devices", {})
    if not isinstance(devices, dict) or len(devices) > 32:
        raise BuildingError("Door devices must map at most 32 doorway IDs to presets")
    for edge, device in devices.items():
        if result["openings"].get(edge) not in ("door_auto", "door_manual") or not isinstance(device, dict):
            raise BuildingError("Door devices must name a device doorway")
        if device.get("preset", "sliding_entropy_c") not in DOOR_PRESETS:
            raise BuildingError("Choose a measured door preset")
        if device.get("yaw_offset", 0) not in (0, 180):
            raise BuildingError("Door facing offset must be 0 or 180 degrees")
        offset = device.get("offset", [0, 0, 0])
        if not isinstance(offset, list) or len(offset) != 3:
            raise BuildingError("Door offset needs local XYZ values")
        for value in offset:
            number(value, "Door offset", -.5, .5)
    wall_appearance = result.setdefault("wall_appearance", catalog["wall_appearances"][0])
    floor_appearance = result.setdefault("floor_appearance", "tiles_grey")
    if wall_appearance not in catalog["wall_appearances"] or floor_appearance not in catalog["floor_appearances"]:
        raise BuildingError("Select a supported kit finish")
    if not isinstance(result.get("navigation", {}), dict):
        raise BuildingError("Navigation settings must be an object")
    navigation = result.get("navigation", {})
    if not isinstance(result.get("room_lighting", False), bool):
        raise BuildingError("Room lighting must be enabled or disabled")
    if not isinstance(result.get('join_storey_walls', False), bool) or (result.get('join_storey_walls') and catalog['id'] != 'common-3m'):
        raise BuildingError('Stacked wall joins require the measured common concrete kit')
    if not isinstance(result.get("plain_door_surrounds", False), bool):
        raise BuildingError("Plain door surrounds must be enabled or disabled")
    if result.get("plain_door_surrounds") and catalog["id"] != "rancho-3m":
        raise BuildingError("Plain surrounds require the measured Rancho wall mesh")
    if not isinstance(result.get("fit_walls_to_storeys", False), bool) or (result.get("fit_walls_to_storeys") and catalog["id"] != "rancho-3m"):
        raise BuildingError("Fitted storey walls require the measured Rancho wall mesh")
    windows = result.get("windows", {})
    if not isinstance(windows, dict) or len(windows) > 32:
        raise BuildingError("Window apertures must map at most 32 wall IDs")
    for edge, aperture in windows.items():
        if result["openings"].get(edge) != "window" or not isinstance(aperture, dict) or catalog["id"] != "rancho-3m":
            raise BuildingError("Window apertures require a measured Rancho window opening")
        width = number(aperture.get("width"), "Window width", .3, 2.5)
        sill = number(aperture.get("sill"), "Window sill", .5, 2)
        height = number(aperture.get("height"), "Window height", .3, 2)
        if width >= 3 or sill + height > catalog["wall_height"] - .1:
            raise BuildingError("Window aperture must fit inside its wall")
    if any(mode == "window" and edge not in windows for edge, mode in result["openings"].items()):
        raise BuildingError("Every window needs a measured aperture")
    test_points = navigation.get("test_points", [])
    if not isinstance(test_points, list) or len(test_points) > 16:
        raise BuildingError("At most 16 explicit runtime test points are supported")
    names = set()
    for point in test_points:
        if not isinstance(point, dict) or not isinstance(point.get("name"), str) or not 1 <= len(point["name"]) <= 80 or point["name"] in names:
            raise BuildingError("Runtime test points need unique names")
        names.add(point["name"])
        xyz = point.get("position")
        if not isinstance(xyz, list) or len(xyz) != 3:
            raise BuildingError("Runtime test points need a local XYZ position")
        for value in xyz:
            number(value, "Runtime test point", -100, 100)
    door_connections = navigation.get("door_connections", {})
    if not isinstance(door_connections, dict) or len(door_connections) > 32:
        raise BuildingError("Door connections must map at most 32 doorway IDs to endpoint pairs")
    for edge, connection in door_connections.items():
        if result["openings"].get(edge) not in ("door_auto", "door_manual") or not isinstance(connection, dict):
            raise BuildingError("An explicit door connection must name a device doorway")
        for field in ("from", "to"):
            xyz = connection.get(field)
            if not isinstance(xyz, list) or len(xyz) != 3:
                raise BuildingError("Door connection endpoints need local XYZ positions")
            for value in xyz:
                number(value, "Door connection endpoint", -100, 100)
        if math.dist(connection["from"], connection["to"]) > 4 or abs(connection["from"][2] - connection["to"][2]) > .6:
            raise BuildingError("Door connections must span at most 4 m and 0.6 m vertically")
    if not isinstance(navigation.get("export", False), bool):
        raise BuildingError("Navigation export must be enabled or disabled")
    layer = navigation.get("layer", 0)
    if isinstance(layer, bool) or not isinstance(layer, int) or not 0 <= layer <= 255:
        raise BuildingError("Navigation layer must be an integer from 0 to 255")
    if navigation.get("export") and not layer:
        raise BuildingError("Choose a nonzero navigation layer for additive tiles; layer 0 can collide with vanilla tiles")
    if not isinstance(result.get("door_states", {}), dict) or any(value not in ("CLOSED", "OPENED", "LOCKED") for value in result.get("door_states", {}).values()):
        raise BuildingError("Door states must be CLOSED, OPENED or LOCKED")
    from building_features import validate_stairs
    try:
        validate_stairs(result, cells, catalog)
    except ValueError as error:
        raise BuildingError(str(error)) from error
    return result, cells


def world_point(point, origin):
    yaw = math.radians(origin["yaw"])
    x, y, z = point
    return [origin["x"] + x * math.cos(yaw) - y * math.sin(yaw),
            origin["y"] + x * math.sin(yaw) + y * math.cos(yaw), origin["z"] + z]


def compile_layout(layout, *, reconcile=False):
    layout, cells = normalize(layout)
    catalog = layout_kit(layout)
    from building_features import slab_rectangles, add_stairs, compile_doors
    height, storey = catalog["wall_height"], catalog["storey_height"]
    edges = {}
    for (level, x, y), owner in sorted(cells.items()):
        sides = (("x", x, y, (level, x, y - 1)),
                 ("y", x + 1, y, (level, x + 1, y)),
                 ("x", x, y + 1, (level, x, y + 1)),
                 ("y", x, y, (level, x - 1, y)))
        for side, (axis, ex, ey, neighbor) in zip(SIDES, sides):
            if cells.get(neighbor) == owner:
                continue
            key = edge_key(level, axis, ex, ey)
            if key not in edges:
                edges[key] = {"id": key, "axis": axis, "x": ex * 3, "y": ey * 3,
                              "level": level, "side": side, "rooms": []}
            edges[key]["rooms"].append(owner)
    stale = sorted(set(layout["openings"]) - set(edges))
    if stale and not reconcile:
        raise BuildingError(f"Opening {stale[0]} no longer belongs to a wall; reconcile the resized layout")
    for key in stale:
        del layout["openings"][key]
    instances, solids = [], []

    def visual(identity, role, point, yaw=0, room=None, edge=None, scale=None):
        offset = catalog["pieces"][role].get("offset", [0, 0, 0])
        angle = math.radians(yaw)
        point = [point[0] + offset[0]*math.cos(angle)-offset[1]*math.sin(angle),
                 point[1] + offset[0]*math.sin(angle)+offset[1]*math.cos(angle), point[2]+offset[2]]
        instances.append({"id": identity, "role": role, "mesh": catalog["pieces"][role]["mesh"],
                          "appearance": layout["floor_appearance"] if role == "floor" else ("concrete" if role == "ceiling" else layout["wall_appearance"]),
                          "position": point, "yaw": yaw, "world_position": world_point(point, layout["origin"]),
                          "world_yaw": yaw + layout["origin"]["yaw"], "level": int(round(point[2] / storey)) if role != "ceiling" else int(round((point[2] - height) / storey)),
                          "room": room, "edge": edge})
        if scale is not None:
            instances[-1]["scale"] = scale

    def solid(identity, role, center, size, yaw=0, level=0, edge=None):
        solids.append({"id": identity, "role": role, "center": center, "size": size, "yaw": yaw,
                       "world_center": world_point(center, layout["origin"]), "world_yaw": yaw + layout["origin"]["yaw"],
                       "level": level, "edge": edge})

    room_heights = {room["id"]: room.get("ceiling_height", height) for room in layout["rooms"]}
    extensions = layout.get('wall_extensions', {})
    if not isinstance(extensions, dict) or (extensions and catalog['id'] != 'common-3m'):
        raise BuildingError('Wall end extensions require the measured common concrete kit')
    for key, value in extensions.items():
        if key not in edges or layout['openings'].get(key) or not isinstance(value, dict) or set(value) - {'start', 'end'}:
            raise BuildingError('Wall end extensions require a solid wall edge and start/end distances')
        for name in ('start', 'end'):
            value[name] = number(value.get(name, 0), 'Wall end extension', 0, .5)

    def wall_facing(identity, point, yaw, opening, key):
        fitted = layout.get("fit_walls_to_storeys", False)
        wall_height = edges[key].get("height", height)
        if not opening and catalog['id']=='common-3m':
            # Give mating skins a 1 mm overlap at their ends. Exact shared
            # vertices can leave a hairline after float/mesh quantization.
            a=math.radians(yaw);overlap=.001
            start, end = (extensions.get(key, {}).get(k, 0) for k in ('start', 'end'))
            axis = 0 if edges[key]['axis'] == 'x' else 1
            tangent = math.cos(a) if axis == 0 else math.sin(a)
            point = point[:]
            point[axis] += end if tangent > 0 else -start
            visual(identity,'wall',[point[0]+overlap*math.cos(a),
                   point[1]+overlap*math.sin(a),point[2]],yaw,edge=key,
                   scale=[(3+start+end+2*overlap)/3,1,wall_height/height])
            return
        foundation = .2988104820251465
        lower = 0 if fitted and edges[key]["level"] else -foundation
        if opening == 'window' and layout.get('native_window_linings'):
            # The matching whole vanilla module owns its frame and UVs.
            # Upper windows are shorter, so only infill above that module.
            top = 3 if edges[key]['level'] else 4
            if wall_height > top:
                sz = (wall_height-top)/(height+foundation)
                visual(identity+':top-fill', 'wall', [*point[:2],point[2]+top+foundation*sz], yaw,
                       edge=key, scale=[1,1,sz])
                instances[-1]['level'] = edges[key]['level']
            return
        if not opening and fitted:
            scale_z = (wall_height - lower) / (height + foundation)
            visual(identity, "wall", [*point[:2], point[2] + lower + foundation * scale_z], yaw, edge=key, scale=[1, 1, scale_z])
            instances[-1]["level"] = edges[key]["level"]
            return
        if opening != "window" and (not opening or not layout.get("plain_door_surrounds")):
            visual(identity, "doorway" if opening else "wall", point, yaw, edge=key)
            return
        width, clear = catalog["door_clearance"]
        if layout.get("door_devices", {}).get(key, {}).get("preset") == "hinged_h":
            clear = max(clear, 2.5)
        jamb = (3 - width) / 2
        a = math.radians(yaw)
        # The full wall has a foundation below zero. Account for its measured
        # lower bound when scaling the header; never fill the door aperture.
        parts = [("", 0, lower, jamb, wall_height - lower),
                 (":left", -jamb - width, lower, jamb, wall_height - lower),
                 (":header", -jamb, clear, width, wall_height - clear)]
        if opening == "window":
            aperture = layout["windows"][key]
            width, sill, opening_height = (aperture[k] for k in ("width", "sill", "height"))
            jamb = (3 - width) / 2
            parts = [("", 0, lower, jamb, wall_height - lower),
                     (":left", -jamb - width, lower, jamb, wall_height - lower),
                     (":sill", -jamb, lower, width, sill - lower),
                     (":header", -jamb, sill + opening_height, width, wall_height - sill - opening_height)]
        for suffix, dx, zmin, w, h in parts:
            scale_z = h / (height + foundation)
            p = [point[0] + dx * math.cos(a), point[1] + dx * math.sin(a), point[2] + zmin + foundation * scale_z]
            visual(identity + suffix, "wall", p, yaw, edge=key, scale=[w / 3, 1, scale_z])
            instances[-1]["level"] = edges[key]["level"]
    for (level, x, y), owner in sorted(cells.items()):
        z = level * storey
        identity = f"tile:{level}:{x}:{y}"
        for role in ("floor", "ceiling"):
            is_ceiling = role == "ceiling"
            for part, (xmin, ymin, xmax, ymax) in enumerate(slab_rectangles(
                    layout["stairs"], level, x, y, ceiling=is_ceiling,
                    wall_depth=catalog.get('wall_facing_depth',0),
                    wall_footprints=[
                        ([e['x'],e['y']-.2,e['x']+3,e['y']+.2] if e['axis']=='x' else
                         [e['x']-.2,e['y'],e['x']+.2,e['y']+3])
                        for k,e in edges.items() if e['level']==level and not layout['openings'].get(k)])):
                width, depth = xmax - xmin, ymax - ymin
                part_id = identity + ":" + role + (f":{part}" if part else "")
                if is_ceiling:
                    ceiling_height = room_heights[owner]
                    thickness = max(.1, storey - ceiling_height - .2) if (level + 1, x, y) in cells else .1
                    visual(part_id, "ceiling", [xmax, ymax, z + ceiling_height], room=owner,
                           scale=[width / 3, depth / 3, thickness / .1])
                    center_z = z + ceiling_height + thickness / 2
                else:
                    thickness = .2
                    # The measured floor includes a 2.5 mm lip on every edge.
                    # Normalize all tiles, not only shaft cuts, so adjacent
                    # top faces cannot flicker where those lips overlap.
                    scale = [width / 3.005, depth / 3.005, 1]
                    point = [xmax - .0025 * scale[0], ymax - .0025 * scale[1], z]
                    visual(part_id, "floor", point, room=owner, scale=scale)
                    center_z = z - thickness / 2
                solid(part_id, role, [(xmin + xmax) / 2, (ymin + ymax) / 2, center_z],
                      [width, depth, thickness], level=level)
                if is_ceiling and layout.get('close_ceiling_slabs'):
                    # The vanilla ceiling has a downward face and sides, but
                    # no top. Stair cameras can see that open back face.
                    cap = min(.02, thickness / 2)
                    visual(part_id+':top', 'floor',
                           [xmax-.0025*width/3.005, ymax-.0025*depth/3.005,
                            z+ceiling_height+thickness], room=owner,
                           scale=[width/3.005, depth/3.005, cap/.2])
                    instances[-1]['level'] = level
    for key, edge in sorted(edges.items()):
        x, y, z = edge["x"], edge["y"], edge["level"] * storey
        side = edge["side"]
        yaw = {"south": 0, "east": 90, "north": 180, "west": -90}[side]
        position = {"south": [x + 3, y, z], "east": [x, y + 3, z],
                    "north": [x, y, z], "west": [x, y, z]}[side]
        opening = layout["openings"].get(key)
        wall_height = height
        above_key = str(edge['level'] + 1) + ':' + key.split(':', 1)[1]
        if (layout.get('join_storey_walls') and not opening and above_key in edges
                and layout['openings'].get(above_key) != 'passage'):
            # Native common walls end at 3.8 m. At an open stair shaft there
            # is no slab edge to conceal the gap to the next storey's wall.
            # Meet the next wall at its base without a coplanar vertical lap.
            wall_height = storey
        if layout.get("fit_walls_to_storeys"):
            wall_height = min(height, max(room_heights[owner] for owner in edge["rooms"]) + .1)
            ex, ey = round(x / 3), round(y / 3)
            above = ((edge["level"] + 1, ex, ey - 1), (edge["level"] + 1, ex, ey)) if edge["axis"] == "x" else (
                (edge["level"] + 1, ex - 1, ey), (edge["level"] + 1, ex, ey))
            if any(cell in cells for cell in above):
                wall_height = min(wall_height, storey - .21)
            edge["frame"] = {"position": position[:], "yaw": yaw}
        edge["height"] = wall_height
        edge["opening"] = opening
        edge["shared"] = len(edge["rooms"]) == 2
        # A measured infill can share a boundary with a regular room without
        # occupying its three-metre cells. Render both decorated facings and
        # centre the casing in the same single wall volume.
        for shell in layout.get("shell_rooms", []):
            if not isinstance(shell, dict) or not isinstance(shell.get("position"), list) or len(shell["position"]) != 3:
                continue
            sx, sy, sz = [number(v, "Shell coordinate", -100, 100) for v in shell["position"]]
            sw = number(shell.get("width"), "Shell room width", .9, 20)
            sd = number(shell.get("depth"), "Shell room depth", .9, 20)
            if shell.get("level", 0) != edge["level"] or abs(sz-z) > .600001:
                continue
            if ((side == "south" and abs(sy+sd-y)<1e-6 and sx<=x and sx+sw>=x+3) or
                (side == "north" and abs(sy-y)<1e-6 and sx<=x and sx+sw>=x+3) or
                (side == "west" and abs(sx+sw-x)<1e-6 and sy<=y and sy+sd>=y+3) or
                (side == "east" and abs(sx-x)<1e-6 and sy<=y and sy+sd>=y+3)):
                edge["shared"] = True
        if opening == "window" and edge["shared"]:
            raise BuildingError("Exterior windows must be on an exterior room edge")
        if opening == "passage":
            ceilings=[room_heights[owner] for owner in edge['rooms']]
            if len(ceilings)==2 and max(ceilings)-min(ceilings)>1e-6:
                low,high=min(ceilings),max(ceilings)+.1
                h=high-low;foundation=.2988104820251465
                a=math.radians(yaw);sz=h/(height+foundation)
                p=[*position[:2],z+low+foundation*sz]
                visual('bulkhead:'+key,'wall',p,yaw,edge=key,scale=[1,1,sz]);instances[-1]['level']=edge['level']
                t=catalog.get('wall_facing_depth',catalog['wall_thickness'])
                reverse=[position[0]-3*math.cos(a)-t*math.sin(a),position[1]-3*math.sin(a)+t*math.cos(a),p[2]]
                visual('bulkhead:'+key+':reverse','wall',reverse,yaw+180,edge=key,scale=[1,1,sz]);instances[-1]['level']=edge['level']
                solid('bulkhead:'+key,'wall',[position[0]-1.5*math.cos(a)-t/2*math.sin(a),position[1]-1.5*math.sin(a)+t/2*math.cos(a),z+(low+high)/2],[3,t,h],yaw,edge['level'],key)
            continue
        wall_facing("wall:" + key, position, yaw, opening, key)
        if edge["shared"]:
            # Interior kit walls have one decorated facing. Rotate the second
            # facing around the centre of the same wall volume, leaving the
            # centred doorway aperture and native door placement unchanged.
            angle = math.radians(yaw)
            # Bounds include projecting trim; place the opposing decorated
            # face using the measured skin depth so T/corner joins meet.
            facing_depth = catalog.get('wall_facing_depth',catalog['wall_thickness'])
            reverse = [position[0] - 3 * math.cos(angle) - facing_depth * math.sin(angle),
                       position[1] - 3 * math.sin(angle) + facing_depth * math.cos(angle), z]
            wall_facing("wall:" + key + ":reverse", reverse, yaw + 180, opening, key)
        # Work in the same local frame as the visual mesh: X=-3..0,
        # Y=0..thickness. Door solids deliberately leave the aperture clear.
        parts = [(-1.5, wall_height / 2, 3, wall_height)]
        if opening in ("doorway", "door_auto", "door_manual"):
            width, clear_height = catalog["door_clearance"]
            if layout.get("door_devices", {}).get(key, {}).get("preset") == "hinged_h":
                clear_height = max(clear_height, 2.5)
            jamb = (3 - width) / 2
            parts = [(-3 + jamb / 2, wall_height / 2, jamb, wall_height),
                     (-jamb / 2, wall_height / 2, jamb, wall_height),
                     (-1.5, (clear_height + wall_height) / 2, width, wall_height - clear_height)]
        a = math.radians(yaw)
        for index, (cx, cz, w, h) in enumerate(parts):
            thickness = catalog["wall_thickness"]
            center = [position[0] + cx * math.cos(a) - thickness / 2 * math.sin(a),
                      position[1] + cx * math.sin(a) + thickness / 2 * math.cos(a), position[2] + cz]
            if key in extensions:
                start, end = (extensions[key][k] for k in ('start', 'end'))
                center[0 if edge['axis'] == 'x' else 1] += (end-start)/2
                w += start+end
            solid(f"wall:{key}:{index}", "wall", center, [w, thickness, h], yaw, edge["level"], key)
    scene = {"layout": layout, "kit": catalog, "instances": instances, "solids": solids,
             "stairs": layout["stairs"], "edges": list(edges.values()), "removed_openings": stale}
    add_stairs(scene, world_point)
    if layout.get('window_reveals'):
        from building_features import structural_box
        for edge in scene['edges']:
            if edge['opening']!='window':
                continue
            aperture=layout['windows'][edge['id']]
            width,sill,h=(aperture[k] for k in ('width','sill','height'))
            # These measured front-window reveals bridge the plaster lining
            # to the original pane, leaving its full frame visible inside.
            if edge['axis']!='x' or edge['y']!=0:
                raise BuildingError('Measured window reveals require front-facing Rancho apertures')
            cx,cz=edge['x']+1.5,edge['level']*storey+sill+h/2
            bar=.12;vertical=.09 if edge['level'] else .12
            for label,center,size in (
                ('left',[cx-width/2+bar/2,-.075,cz],[bar,.2,h]),
                ('right',[cx+width/2-bar/2,-.075,cz],[bar,.2,h]),
                ('sill',[cx,-.075,cz-h/2+vertical/2],[width-2*bar,.2,vertical]),
                ('head',[cx,-.075,cz+h/2-vertical/2],[width-2*bar,.2,vertical])):
                structural_box(scene,world_point,'reveal:'+edge['id']+':'+label,center,size,edge['level'],'reveal')
                instances[-1]['appearance']='tiles_grey'
    from building_library import compile_modules
    try:
        compile_modules(scene, world_point)
        if layout.get('native_window_linings'):
            for original in list(instances):
                if original.get('asset') != '8d7d3e6409823ceb7395':
                    continue
                lining = copy.deepcopy(original)
                lining['id'] += ':interior'
                lining['position'][0] -= 3
                lining['yaw'] += 180
                lining['appearance'] = layout['wall_appearance']
                lining['world_position'] = world_point(lining['position'],layout['origin'])
                lining['world_yaw'] = lining['yaw']+layout['origin']['yaw']
                lining['align_wall_uv'] = True
                instances.append(lining)
    except ValueError as error:
        raise BuildingError(str(error)) from error
    try:
        from building_shell_rooms import compile_shell_rooms
        compile_shell_rooms(scene, world_point)
        scene["doors"] = compile_doors(scene, world_point)
        scene["doors"].extend(scene["shell_doors"])
    except ValueError as error:
        raise BuildingError(str(error)) from error
    from building_encounters import compile_workstations
    compile_workstations(scene, world_point)
    from building_lighting import compile_lights
    from building_audio import compile_audio_areas
    try:
        compile_lights(scene, world_point)
        compile_audio_areas(scene, world_point)
    except ValueError as error:
        raise BuildingError(str(error)) from error
    from building_navigation import compile_navigation
    try:
        scene["navigation"] = compile_navigation(scene)
    except ValueError as error:
        raise BuildingError(str(error)) from error
    from building_retrofit import validate_retrofit
    try:
        scene["retrofit_patches"] = validate_retrofit(layout)
    except (ValueError, OSError, KeyError) as error:
        raise BuildingError(str(error)) from error
    scene["warnings"] = ["Native navigation is experimental; offline routes and serialization do not prove live NPC reachability.",
                         "Preview uses neutral materials. Validate lighting, audio, doors and streaming in game."]
    if any(link.get("external") for link in scene["navigation"]["links"]):
        scene["warnings"].append("Entrance links target existing world navigation. Survey that exact endpoint and validate it with the native game query.")
    if layout.get("navigation", {}).get("export"):
        scene["warnings"].append("Additive navigation uses a separate layer. It does not rebuild or carve overlapping vanilla tiles; use surveyed entrance links and validate surrounding routes.")
    if scene["stairs"]:
        scene["warnings"].append("Stair shafts and guard walls are generated. Verify headroom, collision and approaches in game.")
    if layout.get("modules"):
        scene["warnings"].append("Library modules preserve vanilla sizes and pivots. They do not add walkable navigation surfaces, native device behaviour or original collision. Optional solid boxes fill all mesh openings.")
    if scene["navigation"]["stats"]["islands"] > 1:
        scene["warnings"].append(f"Navigation contains {scene['navigation']['stats']['islands']} disconnected islands; use openings or stairs to connect them.")
    scene["stats"] = {"rooms": len(layout["rooms"]) + len(scene["shell_rooms"]),
                      "area": len(cells) * 9 + sum((b[2]-b[0])*(b[3]-b[1]) for r in scene["shell_rooms"] for b in r['footprints']), "tiles": len(cells),
                      "walls": len(edges), "openings": len(layout["openings"]), "meshes": len(instances), "colliders": len(solids),
                      "stairs": len(scene["stairs"]), "doors": len(scene["doors"]), **scene["navigation"]["stats"]}
    return scene



def fnv_name(value):
    value_hash = 0xCBF29CE484222325
    for byte in value.encode("utf-8"):
        value_hash = ((value_hash ^ byte) * 0x100000001B3) & ((1 << 64) - 1)
    return value_hash


def collision_node(solid, buffer_id):
    """One oriented box, encoded from WKit's documented collision-buffer layout."""
    xyz = [round(v * 131072) for v in solid["world_center"]]
    if any(not -(1 << 31) <= v < (1 << 31) for v in xyz):
        raise BuildingError("Collision is outside RED fixed-point coordinate range")
    angle = math.radians(solid["world_yaw"]) / 2
    orientation = solid.get('world_orientation', [0, 0, math.sin(angle), math.cos(angle)])
    actor = struct.pack("<4i4fHHhhQ", *xyz, 0, *orientation, 0, 1, -1, 0, 0)
    shape = struct.pack("<3f6h2BHI", *(v / 2 for v in solid["size"]), 0, 0, 0, 1, -1, -1, 0, 11, 0, 0)
    raw = actor + shape + struct.pack("<QQIB", fnv_name("concrete.physmat"), fnv_name("World Static"), 0, 0)
    return {"$type": "worldCollisionNode", "debugName": cname(solid["id"]),
            "compiledData": {"BufferId": str(buffer_id), "Flags": 4063232, "Bytes": base64.b64encode(raw).decode("ascii")},
            "numActors": 1, "numShapeInfos": 1, "numShapePositions": 0, "numShapeRotations": 0,
            "numScales": 0, "numMaterials": 1, "numPresets": 1, "numMaterialIndices": 1, "numShapeIndices": 1,
            "sectorHash": "0", "resourceVersion": 2, "lod": 0,
            "extents": {"$type": "Vector4", "X": max(solid["size"]), "Y": max(solid["size"]), "Z": max(solid["size"]), "W": 0},
            "staticCollisionShapeCategories": {"$type": "worldStaticCollisionShapeCategories_CollisionNode", "arr": {"Elements": [
                {"Elements": [0, 0, 0, 0, 0, 0]}, {"Elements": [0, 1, 0, 0, 0, 0]},
                {"Elements": [0, 0, 0, 0, 0, 0]}, {"Elements": [0, 0, 0, 0, 0, 0]}, {"Elements": [0, 1, 0, 0, 0, 0]}]}}}


def native_documents(scene, output):
    layout = scene["layout"]
    depot = f"mod\\building_lab\\{layout['id']}"
    sector_depot, block_depot = depot + ".streamingsector", depot + ".streamingblock"
    archive = output / "source/archive/mod/building_lab"
    handles = HandleAllocator()
    nodes, placements = [], []

    def add(node, point, yaw, size=None):
        index = len(nodes)
        nodes.append(node)
        placement = node_data(index, 0, Vec3(*point), yaw)
        # Bound radius includes off-centre pivots and rotated modules. Streaming
        # extents are conservative, not inferred from a point-only NodeData box.
        radius = max(size or [5, 5, 5])
        placement["Bounds"]["Min"].update({axis: point[i] - radius for i, axis in enumerate(("X", "Y", "Z"))})
        placement["Bounds"]["Max"].update({axis: point[i] + radius for i, axis in enumerate(("X", "Y", "Z"))})
        placements.append(placement)

    for instance in scene["instances"]:
        if instance.get('reference_only'):
            continue
        add({"HandleId": handles.take(), "Data": {"$type": "worldMeshNode", "debugName": cname(instance["id"]),
             "mesh": resource_path(instance["mesh"]), "meshAppearance": cname(instance["appearance"]),
             "isVisibleInGame": 1, "isHostOnly": 0,
             "castShadows": "Always", "castLocalShadows": "Always", "occluderType": "None", "forceAutoHideDistance": 150}},
            instance["world_position"], instance["world_yaw"], ([2*instance["extent_radius"]]*3 if "extent_radius" in instance else
                [3 * instance["scale"][0], 3 * instance["scale"][1], .2 * instance["scale"][2]] if "scale" in instance else None))
        if "scale" in instance:
            placements[-1]["Scale"].update(dict(zip(("X", "Y", "Z"), instance["scale"])))
        if "world_orientation" in instance:
            placements[-1]["Orientation"] = instance["world_orientation"]
    for index, solid in enumerate(scene["solids"], 1):
        # Collision actor transforms are world-space; the node placement remains
        # at that actor's location for streaming, not for another transform bake.
        add({"HandleId": handles.take(), "Data": collision_node(solid, index)}, solid["world_center"], 0, solid["size"])
    from building_features import door_node, door_connection_node
    from generate_world import node_ref
    for index, door in enumerate(scene["doors"], len(scene["solids"]) + 1):
        add(door_node(door, handles, index), door["world_position"], door["world_yaw"])
        if 'scale' in door and not door.get('component_scale'):
            placements[-1]['Scale'].update(dict(zip(('X','Y','Z'), door['scale'])))
        placements[-1]["QuestPrefabRefHash"] = node_ref(door["ref"])
        add(door_connection_node(door, handles), door["world_position"], 0)
        placements[-1]["QuestPrefabRefHash"] = node_ref(door["connection_ref"])
    from building_features import entrance_connection_node
    for link in scene["navigation"]["links"]:
        if link.get("kind") != "entrance":
            continue
        add(entrance_connection_node(link, handles), link["world_endpoints"][0], 0)
        placements[-1]["QuestPrefabRefHash"] = node_ref(link["ref"])
    interior_rooms = [*layout["rooms"], *[{"id":r["id"],"x":r["position"][0],"y":r["position"][1],"width":r["width"],"depth":r["depth"],
        "level":r.get("level",0),"floor_z":r["position"][2],"ceiling_height":r["height"]} for r in layout.get("shell_rooms",[])]]
    from building_lighting import light_node
    for light in scene.get('lights', []):
        add(light_node(light, handles, cname), light['world_position'], 0, [light['radius']] * 3)
    from building_audio import audio_area_node
    for area in scene.get('audio_areas', []):
        add(audio_area_node(area,handles),area['world_position'],layout['origin']['yaw'],area['size'])
    for room in interior_rooms:
        floor_z = room.get("floor_z", room["level"] * scene["kit"]["storey_height"])
        if layout.get("room_lighting"):
            light_point = world_point([room["x"] + room["width"] / 2, room["y"] + room["depth"] / 2,
                                       floor_z + room.get("ceiling_height", scene["kit"]["wall_height"]) - .4], layout["origin"])
            add({"HandleId": handles.take(), "Data": {"$type": "worldStaticLightNode", "debugName": cname("room_light_" + room["id"]),
                 "color": {"$type": "Color", "Red": 255, "Green": 224, "Blue": 190, "Alpha": 255},
                 "radius": max(room["width"], room["depth"]) + 2, "intensity": 120.0, "autoHideDistance": 100.0}}, light_point, 0)
        spec = {"outline": {"type": "box", "width": room["width"], "depth": room["depth"], "height": scene["kit"]["wall_height"]},
                "notifiers": ["interior"]}
        point = world_point([room["x"] + room["width"] / 2, room["y"] + room["depth"] / 2,
                             floor_z], layout["origin"])
        add(trigger_node(spec, "building_" + room["id"], handles), point, layout["origin"]["yaw"], [room["width"], room["depth"], 4])
    references = [value for door in scene["doors"] for value in (door["ref"], door["connection_ref"])]
    references.extend(link["ref"] for link in scene["navigation"]["links"] if link.get("kind") == "entrance")
    sector = streaming_sector("Exterior", 0, archive / (layout["id"] + ".streamingsector"), placements, references, nodes)
    sector["Data"]["RootChunk"]["cookingPlatform"] = "PLATFORM_PC"
    lower = Vec3(*(min(p["Bounds"]["Min"][axis] for p in placements) - 80 for axis in ("X", "Y", "Z")))
    upper = Vec3(*(max(p["Bounds"]["Max"][axis] for p in placements) + 80 for axis in ("X", "Y", "Z")))
    block = copy.deepcopy(sector)
    block["Header"]["ArchiveFileName"] = str((archive / (layout["id"] + ".streamingblock")).resolve())
    block["Data"]["RootChunk"] = {"$type": "worldStreamingBlock", "cookingPlatform": "PLATFORM_PC",
                                  "descriptors": [descriptor("Exterior", sector_depot, 0, None, lower, upper)],
                                  "index": {"$type": "worldStreamingBlockIndex", "oup": "Base", "rldGridCell": 0}}
    return sector, block, block_depot


def prepare_assets(game=None):
    game = resolve_tool("game", game)
    CACHE.mkdir(parents=True, exist_ok=True)
    jobs = []
    from building_library import CACHE as LIBRARY_CACHE
    for catalog in kits():
        for identity, piece in catalog["pieces"].items():
            output = CACHE / "assets" / catalog["id"] / (identity + ".glb")
            source = LIBRARY_CACHE / "assets" / (piece.get("catalog_asset", "") + ".glb")
            if source.is_file():
                output.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, output)
            else:
                jobs.append({"mesh": piece["mesh"], "appearance": piece["preview_appearance"], "output": str(output.resolve())})
    if not jobs:
        return []
    manifest = CACHE / "asset-jobs.json"
    atomic_write_json(manifest, {"jobs": jobs})
    from ghostline_red import ensure_schema
    subprocess.run([str(resolve_tool("ghostline_red")), "mesh-export-batch", str(manifest), "--schema", str(ensure_schema()),
                    "--archives-root", str(game / "archive/pc/content"), "--material-repo", str(CACHE / "materials"),
                    "--report", str(CACHE / "asset-report.json"), "--threads", "3"], check=True)
    report = json.loads((CACHE / "asset-report.json").read_bytes())
    if any(job.get("error") for job in report):
        raise BuildingError("Some kit geometry could not be exported; see generated/building-editor/asset-report.json")
    return jobs


def runtime_contract(scene):
    from shapely.geometry import Polygon
    points = [{"name": point["name"], "local": point["position"],
               "world": world_point(point["position"], scene["layout"]["origin"])}
              for point in scene["layout"].get("navigation", {}).get("test_points", [])]
    for room in scene["layout"]["rooms"]:
        z = room["level"] * scene["kit"]["storey_height"]
        candidates = []
        for triangle in scene["navigation"]["triangles"]:
            if any(abs(p[2] - z) > 1e-5 for p in triangle):
                continue
            polygon = Polygon([p[:2] for p in triangle])
            center = polygon.centroid
            if room["x"] < center.x < room["x"] + room["width"] and room["y"] < center.y < room["y"] + room["depth"]:
                candidates.append((polygon.area, [center.x, center.y, z]))
        if candidates:
            local = max(candidates)[1]
            points.append({"name": room["name"], "local": local, "world": world_point(local, scene["layout"]["origin"])})
    for stair in scene["stairs"]:
        if stair.get('type') == 'return':
            from building_return_stairs import probes
            for label, local in zip(('foot', 'top'), probes(stair, scene['kit']['storey_height'])):
                points.append({'name':stair['id']+' stairs '+label,'local':local,'world':world_point(local,scene['layout']['origin'])})
            continue
        probe_distance=min(.8,stair['landing']/2+.1)
        foot_y, top_y = stair["y"] - probe_distance, stair["y"] + stair["run"] + probe_distance
        if stair.get("reverse"):
            foot_y, top_y = top_y, foot_y
        for label, local in (("foot", [stair["x"] + stair["width"] / 2, foot_y, stair["level"] * scene["kit"]["storey_height"]]),
                             ("top", [stair["x"] + stair["width"] / 2, top_y, (stair["level"] + 1) * scene["kit"]["storey_height"]])):
            if stair.get('axis')=='x':
                from building_stair_frame import point
                local=point(stair,local[0]-stair['x'],local[1]-stair['y'],local[2])
            points.append({"name": stair["id"] + " stairs " + label, "local": local, "world": world_point(local, scene["layout"]["origin"])})
    return {"schema_version": 1, "layout_id": scene["layout"]["id"], "origin": scene["layout"]["origin"], "points": points,
            "restore_auto_close": [door['ref'] for door in scene['doors'] if door.get('restore_auto_close')],
            "doors": [{k: door[k] for k in ("id", "ref", "connection_ref", "world_position", "world_endpoints")} for door in scene["doors"]],
            "source_layout_sha256": hashlib.sha256(json.dumps(scene["layout"], sort_keys=True).encode()).hexdigest(), "runtime_verified": False}


def node_reference_value(value):
    from generate_world import node_ref_hash
    value = value or {"$storage": "uint64", "$value": "0"}
    return int(value["$value"]) if value.get("$storage") == "uint64" else node_ref_hash(value["$value"])


def export_project(scene, output, *, serialize=False):
    if not scene["layout"]["rooms"] and not scene["layout"].get("modules"):
        raise BuildingError("Draw a room or place a prepared library module before exporting")
    output = Path(output).resolve()
    scene = copy.deepcopy(scene)
    archive_name = scene['layout'].get('archive_name', 'Ghostline_BuildingLab')
    if not isinstance(archive_name, str) or not re.fullmatch(r'[A-Za-z0-9_]{1,64}', archive_name):
        raise BuildingError('Archive name must contain only letters, numbers and underscores')
    # Retained vanilla shell pieces are context for designing the interior,
    # never duplicate runtime placements or derived material resources.
    scene['instances'] = [v for v in scene['instances'] if not v.get('reference_only')]
    if not scene['instances'] and not scene['layout']['rooms']:
        raise BuildingError('Shell references alone cannot be exported; add an interior room or a new module')
    aligned = {}
    if scene['layout'].get('align_wall_finishes'):
        from building_wall_uv import prepare_documents
        aligned = prepare_documents(scene, ROOT)
    sector, block, block_depot = native_documents(scene, output)
    layout = scene["layout"]
    documents = {f"{layout['id']}.streamingsector": sector, f"{layout['id']}.streamingblock": block}
    for instance in scene['instances']:
        if not instance.get('authored_raw'):
            continue
        source = (ROOT/instance['authored_raw']).resolve()
        owner = ROOT/'projects/experiments/building-lab/source/raw/mod/building_lab'
        if not source.is_relative_to(owner.resolve()) or not instance['mesh'].startswith('mod\\building_lab\\'):
            raise BuildingError('Authored mesh must belong to the Building Lab raw source tree')
        if hashlib.sha256(source.read_bytes()).hexdigest()!=instance['authored_sha256']:
            raise BuildingError('Authored mesh changed after compilation')
        name = instance['mesh'].rsplit('\\',1)[-1]
        document = json.loads(source.read_bytes())
        document['Header']['ArchiveFileName'] = str(output/'source/archive/mod/building_lab'/name)
        documents[name] = document
    for name, document in aligned.items():
        document['Header']['ArchiveFileName'] = str(output/'source/archive/mod/building_lab'/name)
        documents[name] = document
    if any(d.get('component_scale') for d in scene['doors']):
        name = 'rancho-garage.rig'
        document = json.loads((ROOT / 'projects/experiments/building-lab/source/raw/mod/building_lab' / (name+'.json')).read_bytes())
        document['Header']['ArchiveFileName'] = str(output / 'source/archive/mod/building_lab' / name)
        documents[name] = document
    if any(m.get("clear_glass") for m in layout.get("modules", [])):
        name = "rancho-window-clear.mesh"
        document = json.loads((ROOT / "projects/experiments/building-lab/source/raw/mod/building_lab" / (name + ".json")).read_bytes())
        document["Header"]["ArchiveFileName"] = str(output / "source/archive/mod/building_lab" / name)
        documents[name] = document
    if layout.get("navigation", {}).get("terrain_mask"):
        from building_nav_mask import build_mask_document
        masked = build_mask_document(scene, output)
        documents[masked["name"]] = masked["document"]
        lo, hi = masked["bounds"]
        block["Data"]["RootChunk"]["descriptors"].append(descriptor("Navigation", "mod\\building_lab\\" + masked["name"], 3, None,
            Vec3(*(v - 40 for v in lo)), Vec3(*(v + 40 for v in hi))))
        atomic_write_json(output / "terrain-mask-report.json", {k: v for k, v in masked.items() if k != "document"})
    if layout.get("navigation", {}).get("export", False):
        from building_navigation import navigation_resource
        nav_name = layout["id"] + ".navmesh"
        nav_resource = navigation_resource(scene)
        # Vanilla embeds navigation resources; WolvenKit deliberately excludes
        # standalone .navmesh files from archives.
        for index, buffer in enumerate(nav_resource["tileBuffers"], start=1):
            buffer["BufferId"] = str(index)
        nav_depot = "mod\\building_lab\\" + nav_name
        nav_placement = node_data(0, 0, Vec3(*(layout["origin"][axis] for axis in ("x", "y", "z"))), 0)
        nav_placement["MaxStreamingDistance"] = 500
        nav_node = {"HandleId": "0", "Data": {"$type": "worldNavigationNode", "debugName": cname(layout["id"] + "_human_navigation"),
                    "navigationTileResource": {**resource_path(nav_depot), "Flags": "Embedded"}, "isVisibleInGame": 1}}
        nav_sector_name = layout["id"] + "_navigation.streamingsector"
        nav_sector = streaming_sector("Navigation", 3, output / "source/archive/mod/building_lab" / nav_sector_name, [nav_placement], [], [nav_node])
        nav_sector["Data"]["RootChunk"]["cookingPlatform"] = "PLATFORM_PC"
        nav_sector["Data"]["RootChunk"]["localInplaceResource"] = [{**resource_path(nav_depot), "Flags": "Embedded"}]
        nav_sector["Data"]["EmbeddedFiles"] = [{"FileName": resource_path(nav_depot)["DepotPath"], "Content": nav_resource}]
        documents[nav_sector_name] = nav_sector
        main_descriptor = block["Data"]["RootChunk"]["descriptors"][0]
        nav_descriptor = copy.deepcopy(main_descriptor)
        nav_descriptor.update(category="Navigation", level=3, data=resource_path("mod\\building_lab\\" + nav_sector_name))
        block["Data"]["RootChunk"]["descriptors"].append(nav_descriptor)
    if scene["doors"]:
        from generate_world import device_registry, DeviceRegistryEntry, node_ref_hash
        name = layout["id"] + ".devices"
        entries = [DeviceRegistryEntry(d["ref"], node_ref_hash(d["ref"]), "DoorControllerPS", Vec3(*d["world_position"])) for d in scene["doors"]]
        documents[name] = device_registry(output / "source/archive/mod/building_lab" / name, entries)
    from building_encounters import content_documents
    content, content_block, quest_bindings = content_documents(scene, output)
    documents.update(content)
    if quest_bindings:
        atomic_write_json(output / 'quest-bindings.json', quest_bindings)
        from building_encounters import quest_fragment
        atomic_write_json(output / 'quest-block-fragment.json', quest_fragment(quest_bindings))
    paths = []
    for name, document in documents.items():
        path = output / "source/raw/mod/building_lab" / (name + ".json")
        atomic_write_json(path, document)
        paths.append(path)
    atomic_write_json(output / "buildings" / (layout["id"] + ".building.json"), layout)
    atomic_write_json(output / "building-report.json", {"stats": scene["stats"], "warnings": scene["warnings"],
                                                       "world_origin": layout["origin"], "native_serialized": False})
    atomic_write_json(output / "project.json", {"schema_version": 1, "id": "building-lab", "depot_prefixes": ["mod/building_lab/"],
                                              "dependencies": [], "default_profile": "building-lab", "registration": archive_name+".archive.xl"})
    atomic_write_json(output / "packaging/profiles.json", {"schema_version": 1, "profiles": {"building-lab": {
        "archive_name": archive_name, "active_quests": [], "support_quests": ["building_lab"], "characters": [], "tweaks": [], "deduplicate_meshes": False,
        "streaming_sectors": [patch["path"] for patch in scene["retrofit_patches"]],
        "minimum_archivexl": "1.27.0" if scene["retrofit_patches"] else None}}})
    if layout.get("navigation", {}).get("export"):
        relative = "bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_building_lab"
        target = output / "source/resources" / relative
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "tools/building_runtime_cet/init.lua", target / "init.lua")
        atomic_write_json(target / "contract.json", runtime_contract(scene))
        profile_path = output / "packaging/profiles.json"
        profiles = json.loads(profile_path.read_bytes())
        test_profile = copy.deepcopy(profiles["profiles"]["building-lab"])
        test_profile["include_loose"] = [relative + "/init.lua", relative + "/contract.json"]
        profiles["profiles"]["building-lab-test"] = test_profile
        atomic_write_json(profile_path, profiles)
    resource = output / 'source/resources' / (archive_name+'.archive.xl')
    resource.parent.mkdir(parents=True, exist_ok=True)
    import yaml
    registration = {"streaming": {"blocks": [block_depot]}}
    if content_block:
        registration['streaming']['blocks'].append(content_block)
    if scene["retrofit_patches"]:
        registration["streaming"]["sectors"] = scene["retrofit_patches"]
    if scene["doors"]:
        registration["resource"] = {"patch": {"mod\\building_lab\\" + layout["id"] + ".devices": [r"base\worlds\03_night_city\_compiled\default\03_night_city.devices"]}}
    if quest_bindings:
        registration.setdefault('resource', {}).setdefault('patch', {})['mod\\building_lab\\'+layout['id']+'_content.devices'] = [r'base\worlds\03_night_city\_compiled\default\03_night_city.devices']
    resource.write_text(yaml.safe_dump(registration, sort_keys=False), encoding="utf-8")
    (output / "BuildingLab.cpmodproj").write_text('<?xml version="1.0" encoding="utf-8"?>\n<CP77Mod><Name>Ghostline Building Lab</Name><ModName>'+archive_name+'</ModName><Author>Ghostline</Author><Version>0.1.0</Version></CP77Mod>\n', encoding="utf-8")
    if serialize:
        with tempfile.TemporaryDirectory(prefix="building-resource-") as temporary:
            subprocess.run([str(resolve_tool("wolvenkit")), "convert", "deserialize", *[str(path) for path in paths], "-o", temporary],
                           check=True, capture_output=True, text=True, timeout=180)
            for path in paths:
                binary = output / "source/archive/mod/building_lab" / path.name.removesuffix(".json")
                candidate = Path(temporary) / binary.name
                if not candidate.is_file():
                    raise BuildingError(f"WolvenKit did not create {binary.name}")
                binary.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(candidate, binary)
        verify_native_project(scene, output, paths)
    return output


def verify_native_project(scene, output, paths):
    """Check every native resource against its authored scene and raw metadata."""
    from ghostline_red import serialize as readback
    def component_equal(wanted, actual):
        if isinstance(wanted, dict):
            return isinstance(actual, dict) and all(component_equal(v, actual.get(k)) for k,v in wanted.items() if k != 'HandleId')
        if isinstance(wanted, list):
            return isinstance(actual, list) and len(wanted)==len(actual) and all(component_equal(a,b) for a,b in zip(wanted,actual))
        if isinstance(wanted, (int,float)) and not isinstance(wanted,bool):
            return isinstance(actual, (int,float)) and math.isclose(wanted,actual,rel_tol=1e-6,abs_tol=1e-6)
        return wanted == actual
    layout = scene["layout"]
    for path in paths:
        binary = output / "source/archive/mod/building_lab" / path.name.removesuffix(".json")
        expected = json.loads(path.read_bytes())["Data"]["RootChunk"]
        back = output / "generated/readback" / path.name
        readback(binary, back)
        rebuilt = json.loads(back.read_bytes())
        if binary.suffix == '.rig':
            import base64
            import struct
            transforms = expected['boneTransforms']
            tail = struct.pack('<'+'h'*len(transforms),*expected['boneParentIndexes'])
            for transform in transforms:
                values = [transform[field][axis] for field,axes in (('Translation','XYZW'),('Rotation','ijkr'),('Scale','XYZW')) for axis in axes]
                tail += struct.pack('<12f',*values)
            if base64.b64decode(rebuilt['Data']['RootChunk']['$rawTail']) != tail:
                raise BuildingError('Readback changed garage skeleton transforms')
        if binary.suffix == ".mesh":
            actual = rebuilt["Data"]["RootChunk"]
            if actual.get("externalMaterials") != expected.get("externalMaterials"):
                raise BuildingError("Readback changed transparent window material")
            for wanted, restored in zip(expected["materialEntries"], actual["materialEntries"], strict=True):
                if any(wanted.get(k, default) != restored.get(k, default) for k, default in (("name", None), ("index", 0), ("isLocalInstance", False))):
                    raise BuildingError("Readback changed window material assignments")
            if expected["renderResourceBlob"]["Data"]["renderBuffer"]["Bytes"] != actual["renderResourceBlob"]["Data"]["renderBuffer"]["Bytes"]:
                raise BuildingError("Readback changed window mesh geometry bytes")
        if binary.suffix == ".streamingsector":
            root = rebuilt["Data"]["RootChunk"]
            if root.get('category', 'Exterior') != expected['category'] or root.get('level', 0) != expected['level']:
                raise BuildingError('Readback changed sector streaming category or level')
            if len(root["nodes"]) != len(expected["nodes"]) or len(root["nodeData"]["Data"]) != len(root["nodes"]):
                raise BuildingError("Native readback changed the building node/instance count")
            expected_refs = {node_reference_value(ref) for ref in expected.get("nodeRefs", [])}
            actual_refs = {node_reference_value(ref) for ref in root.get("nodeRefs", [])}
            if expected_refs != actual_refs:
                raise BuildingError("Readback changed the sector NodeRef registry")
            for desired, actual in zip(expected["nodeData"]["Data"], root["nodeData"]["Data"]):
                if desired["NodeIndex"] != actual["NodeIndex"]:
                    raise BuildingError("Readback changed a placement node index")
                if node_reference_value(desired.get("QuestPrefabRefHash")) != node_reference_value(actual.get("QuestPrefabRefHash")):
                    raise BuildingError("Readback changed a device or connection NodeRef")
                for field in ("Position", "Orientation", "Scale", "Pivot"):
                    for axis, value in desired[field].items():
                        if axis != "$type" and not math.isclose(value, actual[field][axis], rel_tol=1e-6, abs_tol=1e-4):
                            raise BuildingError(f"Readback changed placement {field}.{axis}")
            for desired, actual in zip(expected["nodes"], root["nodes"]):
                for field in ("$type", "mesh", "meshAppearance", "entityTemplate", "appearanceName", "navigationTileResource"):
                    wanted_value, actual_value = desired["Data"].get(field), actual["Data"].get(field)
                    if field == "meshAppearance" and wanted_value and wanted_value.get("$value") == "default" and actual_value is None:
                        continue  # worldMeshNode constructor default is omitted on readback.
                    if wanted_value != actual_value:
                        raise BuildingError(f"Readback changed node {field}")
                if desired["Data"]["$type"] == "worldDeviceNode" and desired['Data'].get('appearanceName',{}).get('$value') == 'computer_computer_1':
                    wanted_package = desired['Data']['instanceData']['Data']['buffer']['Data']
                    actual_package = actual['Data']['instanceData']['Data']['buffer']['Data']
                    def explicit_fields(value):
                        if isinstance(value, dict):
                            return {k:explicit_fields(v) for k,v in value.items() if k != 'HandleId' and v not in (0, [], None)}
                        if isinstance(value, list):
                            return [explicit_fields(v) for v in value]
                        return value
                    if not component_equal(explicit_fields(wanted_package), explicit_fields(actual_package)):
                        raise BuildingError('Readback changed workstation computer setup')
                elif desired["Data"]["$type"] == "worldDeviceNode":
                    wanted_package = desired["Data"]["instanceData"]["Data"]["buffer"]["Data"]
                    actual_package = actual["Data"]["instanceData"]["Data"]["buffer"]["Data"]
                    if wanted_package["CruidDict"] != actual_package["CruidDict"] or len(actual_package["Chunks"]) != len(wanted_package['Chunks']):
                        raise BuildingError("Readback changed door component identities")
                    for wanted_chunk, actual_chunk in zip(wanted_package['Chunks'][2:],actual_package['Chunks'][2:]):
                        for field in ('id','visualScale','rig','localTransform','colliders'):
                            if field in wanted_chunk and not component_equal(wanted_chunk[field], actual_chunk.get(field)):
                                raise BuildingError('Readback changed scaled door component '+field)
                    wanted_setup = wanted_package["Chunks"][0]["persistentState"]["Data"]["doorProperties"]
                    actual_setup = actual_package["Chunks"][0]["persistentState"]["Data"].get("doorProperties", {})
                    for field, default in (("doorType", "INTERACTIVE"), ("doorTypeSideOne", "NONE"), ("doorTypeSideTwo", "NONE"), ("initialDoorState", "CLOSED")):
                        if wanted_setup[field] != actual_setup.get(field, default):
                            raise BuildingError("Readback changed door " + field)
                    wanted_ref = wanted_package["Chunks"][1]["offMeshConnectionNodesRefs"][0]
                    actual_ref = actual_package["Chunks"][1]["offMeshConnectionNodesRefs"][0]
                    if node_reference_value(wanted_ref) != node_reference_value(actual_ref):
                        raise BuildingError("Readback changed the door's navigation connection")
                if desired['Data']['$type'] == 'worldCommunityRegistryNode':
                    import zlib
                    old = desired['Data']['communitiesData']
                    new = actual['Data']['communitiesData']
                    if len(old) != len(new):
                        raise BuildingError('Readback changed community count')
                    for a,b in zip(old,new):
                        def initial_states(item):
                            return [(v['entryName'],v['initialPhaseName'],bool(v.get('entryActiveOnStart',False))) for v in item['entriesInitialState']]
                        if a['communityId'] != b['communityId'] or initial_states(a) != initial_states(b):
                            raise BuildingError('Readback changed worker activation')
                        for ea,eb in zip(a['template']['Data']['entries'], b['template']['Data']['entries'], strict=True):
                            record = ea['Data']['characterRecordId']['$value']
                            expected_hash = zlib.crc32(record.encode()) | (len(record) << 32)
                            if str(expected_hash) != str(eb['Data']['characterRecordId']['$value']):
                                raise BuildingError('Readback changed worker character record')
                            if ea['Data']['phases'][0]['Data']['appearances'] != eb['Data']['phases'][0]['Data']['appearances']:
                                raise BuildingError('Readback changed worker appearance')
                if desired['Data']['$type'] == 'worldAISpotNode':
                    for field in ('isWorkspotInfinite','isWorkspotStatic'):
                        if desired['Data'].get(field,0) != actual['Data'].get(field,0):
                            raise BuildingError('Readback changed seated workspot '+field)
                    if desired['Data']['spot']['Data']['resource'] != actual['Data']['spot']['Data']['resource']:
                        raise BuildingError('Readback changed workspot resource')
                if desired["Data"]["$type"] == "worldStaticLightNode":
                    for field in ("color", "radius", "intensity", "autoHideDistance"):
                        if desired["Data"][field] != actual["Data"].get(field, 5.0 if field == "radius" else None):
                            raise BuildingError("Readback changed room lighting " + field)
                if desired['Data']['$type']=='worldAmbientAreaNode':
                    from building_audio import verify_audio_area
                    verify_audio_area(desired['Data'],actual['Data'])
                if desired["Data"].get("compiledData", {}).get("Bytes") != actual["Data"].get("compiledData", {}).get("Bytes"):
                    raise BuildingError("Native readback changed collision bytes")
        if binary.suffix == ".devices":
            wanted_entries = expected["data"]["Data"]["unk1"]
            actual_entries = rebuilt["Data"]["RootChunk"]["data"]["Data"]["unk1"]
            wanted_registry = {entry["hash"]: entry["className"] for entry in wanted_entries}
            actual_registry = {entry["hash"]: entry["className"] for entry in actual_entries}
            if wanted_registry != actual_registry:
                raise BuildingError("Readback changed device registry identities")
        expected_embedded = json.loads(path.read_bytes())["Data"].get("EmbeddedFiles", [])
        if expected_embedded:
            from world_location_nav import load_navigation_sector
            restored_embedded = rebuilt["Data"].get("EmbeddedFiles", [])
            if len(restored_embedded) != 1 or expected_embedded[0]["FileName"] != restored_embedded[0]["FileName"]:
                raise BuildingError("Native navigation lost its embedded resource identity")
            wanted_resource, actual_resource = expected_embedded[0]["Content"], restored_embedded[0]["Content"]
            wanted = load_navigation_sector({"Data": {"RootChunk": wanted_resource}})
            actual = load_navigation_sector({"Data": {"RootChunk": actual_resource}})
            if len(wanted.buffers) != len(actual.buffers):
                raise BuildingError("Native navigation lost tile buffers")
            if len(wanted_resource["tilesData"]) != len(actual_resource.get("tilesData", [])):
                raise BuildingError("Native navigation lost tile metadata")
            for desired, restored in zip(wanted_resource["tilesData"], actual_resource["tilesData"]):
                for field, default in (("tileX", 0), ("tileY", 0), ("tileIndex", 4294967295), ("bufferIndex", 4294967295),
                                       ("agentSize", "Human"), ("tileRef", "9223372036854775807")):
                    if desired.get(field, default) != restored.get(field, default):
                        raise BuildingError("Native navigation changed tile " + field)
                a, b = desired.get("offMeshConnections", {}), restored.get("offMeshConnections", {})
                for field in ("flags", "areas", "directions", "ids", "tagIntervals", "globalNodeIDs", "tagsX"):
                    if a.get(field, []) != b.get(field, []):
                        raise BuildingError("Native navigation changed connection " + field)
                for field in ("verts", "radii"):
                    x, y = a.get(field, []), b.get(field, [])
                    if len(x) != len(y) or any(not math.isclose(i, j, rel_tol=1e-6, abs_tol=1e-4) for i, j in zip(x, y)):
                        raise BuildingError("Native navigation changed connection " + field)
                if len(a.get("userData", [])) != len(b.get("userData", [])):
                    raise BuildingError("Native navigation lost connection user data")
            for desired, restored in zip(wanted_resource["tileBuffers"], actual_resource["tileBuffers"]):
                if desired["Bytes"] != restored["Bytes"]:
                    raise BuildingError("Native navigation tile bytes changed")
            atomic_write_json(output / "navigation-report.json", {"status": "experimental-native", "tiles": len(actual.buffers),
                              "faces": sum(len(buffer.faces) for buffer in actual.buffers), "islands": scene["navigation"]["stats"]["islands"],
                              "runtime_verified": False, "tile_size": 32.4, "layer": layout.get("navigation", {}).get("layer", 0)})
        if binary.suffix == '.streamingblock':
            actual_descriptors = rebuilt['Data']['RootChunk']['descriptors']
            for desired, actual in zip(expected['descriptors'], actual_descriptors, strict=True):
                if (desired['category'],desired['level']) != (actual.get('category','Exterior'),actual.get('level',0)):
                    raise BuildingError('Readback changed descriptor streaming category or level')
                if node_reference_value(desired.get('questPrefabNodeRef')) != node_reference_value(actual.get('questPrefabNodeRef')):
                    raise BuildingError('Readback changed descriptor quest activation gate')
    report_path = output / "building-report.json"
    report = json.loads(report_path.read_bytes())
    report["native_serialized"] = True
    report["serializers"] = {"sector": "WolvenKit", "block": "WolvenKit", "readback": "ghostline-red"}
    report["binaries"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (output / "source/archive/mod/building_lab").iterdir()}
    atomic_write_json(report_path, report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("prepare-assets", help="Read the configured vanilla archives and cache room-preset geometry")
    for name in ("validate", "compile", "export"):
        command = sub.add_parser(name)
        command.add_argument("layout", type=Path)
        if name != "validate":
            command.add_argument("--out", type=Path, required=True)
        if name == "export":
            command.add_argument("--serialize", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "prepare-assets":
            prepare_assets()
        else:
            scene = compile_layout(json.loads(args.layout.read_bytes()))
            if args.command == "compile":
                atomic_write_json(args.out, scene)
            elif args.command == "export":
                export_project(scene, args.out, serialize=args.serialize)
            print(json.dumps(scene["stats"], indent=2))
    except (BuildingError, OSError, json.JSONDecodeError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f"Building error: {error}\n")


if __name__ == "__main__":
    main()
