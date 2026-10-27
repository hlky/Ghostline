"""Stair geometry and native interactive door contracts for Building Lab."""
from __future__ import annotations

import math
import re

from generate_world import cname, node_ref, resource_path, spline_node

DOOR_ENTITY = r"base\gameplay\devices\doors\final\single_door.ent"
DOOR_CONTROLLER_CRUID = "1193887807258071040"
DOOR_OFFMESH_CRUID = "1455904520967634944"
DOOR_APPEARANCE = "doors_single_entropy_c"
DOOR_PRESETS = {
    "sliding_entropy_c": (DOOR_ENTITY, DOOR_APPEARANCE, .75),
    "sliding_kitsch_double_f": (r"base\gameplay\devices\doors\final\double_door.ent", "doors_double_kitsch_f", 0),
    # Vanilla casing centre is X=-89129/131072, not the sliding root's -.75.
    "hinged_h": (r"base\gameplay\devices\doors\final\single_door_hinged.ent", "doors_single_hinged_h", 89129 / 131072),
    "hinged_e": (r"base\gameplay\devices\doors\final\single_door_hinged.ent", "doors_single_hinged_e", 89129 / 131072),
    "garage_w300_h250": (r"base\gameplay\devices\doors\gates\shutter_window_w300_h250.ent", "shutter_w300_h250_rusty", 0),
}


def open_door_leaf(door):
    """Measured hinged_h leaf at the stock +90 degree open pose, local XY."""
    if door["appearance"] not in ("doors_single_hinged_h", "doors_single_hinged_e"):
        return None
    bounds = ((-1.3903896808624268, -.1090112179517746), (.05042128264904022, .1090112179517746)) if door['appearance']=='doors_single_hinged_e' else (
        (-1.4050682735443115, -.09126460552215576), (.03502822771668434, .08732765167951584))
    angle = math.radians(door["yaw"] + 90)
    return [[door["position"][0] + x * math.cos(angle) - y * math.sin(angle),
             door["position"][1] + x * math.sin(angle) + y * math.cos(angle)]
            for x, y in [(bounds[0][0],bounds[0][1]),(bounds[1][0],bounds[0][1]),
                         (bounds[1][0],bounds[1][1]),(bounds[0][0],bounds[1][1])]]


def validate_stairs(layout, cells, catalog):
    stairs = layout.setdefault("stairs", [])
    if not isinstance(stairs, list) or len(stairs) > 16:
        raise ValueError("A layout supports at most 16 stair flights")
    used, occupied = set(), set()
    for stair in stairs:
        if not isinstance(stair, dict) or not isinstance(stair.get("id"), str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,47}", stair["id"]) or stair["id"] in used:
            raise ValueError("Stair ids must be unique lowercase identifiers")
        used.add(stair["id"])
        if not isinstance(stair.get("railings", True), bool):
            raise ValueError("Stair railings must be enabled or disabled")
        if not isinstance(stair.get("reverse", False), bool):
            raise ValueError("Stair direction must be enabled or disabled")
        returning = stair.get("type", "straight") == "return"
        if stair.get('axis', 'y') not in ('x', 'y') or (returning and stair.get('axis', 'y') != 'y'):
            raise ValueError('Stair axis must be x or y; return stairs currently use y')
        if stair.get('wall_side') not in (None, 'left', 'right'):
            raise ValueError('Stair wall side must be left or right')
        if stair.get("type", "straight") not in ("straight", "return"):
            raise ValueError("Stair type must be straight or return")
        if returning:
            fw = stair.get("flight_width", 1.2)
            if isinstance(fw, bool) or not isinstance(fw, (int, float)) or not math.isfinite(fw) or not 1.2 <= fw <= 2.5:
                raise ValueError("Return stair flight width must be 1.2..2.5 m")
            stair["flight_width"] = fw
        for field, low, high in (("x", -60, 60), ("y", -60, 60), ("width", 1.2, 6), ("run", 3 if returning else 6, 15), ("level", 0, 2), ("landing", 1.2, 3)):
            if field == "landing":
                stair.setdefault(field, 3)
            value = stair.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not low <= value <= high or (value % 1 if field == "level" else abs(value * 20 - round(value * 20)) > 1e-6):
                raise ValueError(f"Stair {field} must be {'an integer' if field == 'level' else 'on the 5 cm grid'} in {low}..{high}")
        if returning and (stair['width'] < 2*fw+.15 or stair['width'] > 2*fw+.4 or stair.get('reverse')):
            raise ValueError("Return stairs need two flights and a 15..40 cm central partition; reverse is unsupported")
        if math.degrees(math.atan2(catalog["storey_height"] / (2 if returning else 1), stair["run"])) > 35:
            raise ValueError("Stairs must be at most 35 degrees; increase the run")
        x, y, w, run = (stair[k] for k in ("x", "y", "width", "run"))
        level = int(stair["level"])
        landing = stair["landing"]
        from building_stair_frame import rectangle
        lx,ly,hx,hy=rectangle(stair,[0,-landing,w,run+landing])
        # A compact flight can sit within a larger gridded room. Require the
        # entire continuous shaft/landing rectangle inside one room per floor.
        for floor in (level, level + 1):
            if not any(r["level"] == floor and r["x"] <= lx and r["y"] <= ly and
                       r["x"] + r["width"] >= hx and r["y"] + r["depth"] >= hy for r in layout["rooms"]):
                raise ValueError("Each stair flight needs its full shaft and clear landings inside one room per floor")
            for previous in occupied:
                pf, px, py, pw, pr = previous
                if pf == floor and x < px + pw and x + w > px and y < py + pr and y + run > py:
                    raise ValueError("Stair shafts cannot overlap")
            occupied.add((floor, x, y, w, run))
    return stairs


def shaft_cell(stairs, level, x, y, *, ceiling=False):
    return any(level == s["level"] + (0 if ceiling else 1)
               and s["x"] <= x * 3 < s["x"] + s["width"]
               and s["y"] <= y * 3 < s["y"] + s["run"] for s in stairs)


def slab_rectangle(stairs, level, x, y, *, ceiling=False):
    """Trim slabs to guard exteriors instead of rendering coincident faces."""
    bounds = [x * 3, y * 3, (x + 1) * 3, (y + 1) * 3]
    for stair in stairs:
        if not stair.get("railings", True) or level != stair["level"] + (0 if ceiling else 1):
            continue
        sx, sy, width, run = (stair[k] for k in ("x", "y", "width", "run"))
        if sy <= y * 3 < sy + run:
            if (x + 1) * 3 == sx:
                bounds[2] -= .12
            if x * 3 == sx + width:
                bounds[0] += .12
        if (y + 1) * 3 == sy and sx <= x * 3 < sx + width:
            bounds[3] -= .12
    return bounds


def slab_rectangles(stairs, level, x, y, *, ceiling=False, wall_depth=0, wall_footprints=None):
    """Subtract exact shaft/guard rectangles, including flights within a tile."""
    result = [[x * 3, y * 3, (x + 1) * 3, (y + 1) * 3]]
    for stair in stairs:
        if level != stair["level"] + (0 if ceiling else 1):
            continue
        pad = .12 if stair.get("railings", True) else 0
        from building_stair_frame import shaft
        sx,sy,ex,ey=shaft(stair,guards=True)
        cuts = [[sx,sy,ex,ey]]
        # A room wall already fills the strip between the flight and its
        # grid boundary. A slab cut at the painted face would expose a
        # coincident vertical lip, flickering through the wall on stairs.
        if wall_depth and stair.get('wall_side'):
            from building_stair_frame import rectangle
            left = -wall_depth if stair['wall_side']=='left' else 0
            right = stair['width']+(wall_depth if stair['wall_side']=='right' else 0)
            a,b,c,d=rectangle(stair,[left,0,right,stair['run']])
            # Clip only where a solid room wall actually exists. At a hallway
            # passage the thin remaining floor strip must stay walkable.
            expanded=[min(sx,a),min(sy,b),max(ex,c),max(ey,d)]
            for wall in wall_footprints if wall_footprints is not None else [expanded]:
                u,v,w,h=wall
                clip=[max(expanded[0],u),max(expanded[1],v),min(expanded[2],w),min(expanded[3],h)]
                if clip[0]<clip[2] and clip[1]<clip[3]: cuts.append(clip)
        if stair.get('type') == 'return' and pad and not ceiling:
            # Only the low flight has a guard across this end. Cutting the
            # whole width would leave a 12 cm floor gap at the upper exit.
            cuts.append([stair['x'],ey,stair['x']+stair['flight_width'],ey+pad])
        # A ceiling below the guard must meet underneath its footprint. The
        # extra floor cut would stop it at the outer guard face and expose
        # the slab's vertical lip to cameras descending the stairs.
        for sx,sy,ex,ey in cuts:
            remaining = []
            for left, bottom, right, top in result:
                a, b, c, d = max(left, sx), max(bottom, sy), min(right, ex), min(top, ey)
                if a >= c or b >= d:
                    remaining.append([left, bottom, right, top])
                    continue
                for rect in ([left, bottom, a, top], [c, bottom, right, top], [a, bottom, c, b], [a, d, c, top]):
                    if rect[2] - rect[0] > 1e-7 and rect[3] - rect[1] > 1e-7:
                        remaining.append(rect)
            result = remaining
    return result


def structural_box(scene, world_point, identity, center, size, level, kind):
    """Close a prism with a concrete underside/body and a thin floor top cap.

    The vanilla floor is an open-bottom slab, not a solid cube. Its 2.5 mm
    perimeter lip is normalized here so adjacent stair/guard segments meet
    without overlapping their side surfaces.
    """
    catalog, layout = scene["kit"], scene["layout"]
    if kind == 'guard' and layout.get('paint_stair_enclosures'):
        cx,cy,cz=center
        along_x = size[0] >= size[1]
        length,depth = (size[0],size[1]) if along_x else (size[1],size[0])
        foundation=.2988104820251465
        sz=size[2]/(4+foundation)
        z=cz-size[2]/2+foundation*sz
        faces=(([cx+length/2,cy-depth/2,z],0),([cx-length/2,cy+depth/2,z],180)) if along_x else (
            ([cx+depth/2,cy+length/2,z],90),([cx-depth/2,cy-length/2,z],270))
        for index,(point,yaw) in enumerate(faces):
            scene['instances'].append(dict(id=f'{identity}:paint:{index}', role='wall',kind=kind,
                mesh=catalog['pieces']['wall']['mesh'],appearance=layout['wall_appearance'],
                position=point,yaw=yaw,scale=[length/3,depth/.15,sz],
                world_position=world_point(point,layout['origin']),world_yaw=yaw+layout['origin']['yaw'],
                level=level,room=None,edge=None))
        return
    cap = min(.02, size[2] / 2)
    lower = [center[i] - size[i] / 2 for i in range(3)]
    upper = [center[i] + size[i] / 2 for i in range(3)]
    for suffix, role, point, scale, appearance in (
        ("body", "ceiling", [upper[0], upper[1], lower[2]],
         [size[0] / 3, size[1] / 3, (size[2] - cap) / .1], "concrete"),
        ("cap", "floor", [upper[0] - .0025 * size[0] / 3.005,
                           upper[1] - .0025 * size[1] / 3.005, upper[2]],
         [size[0] / 3.005, size[1] / 3.005, cap / .2], layout["floor_appearance"]),
    ):
        scene["instances"].append({"id": identity + ":" + suffix, "role": role, "kind": kind,
            "mesh": catalog["pieces"][role]["mesh"], "appearance": appearance,
            "position": point, "yaw": 0, "scale": scale,
            "world_position": world_point(point, layout["origin"]), "world_yaw": layout["origin"]["yaw"],
            "level": level, "room": None, "edge": None})


def add_stairs(scene, world_point):
    catalog = scene["kit"]
    for stair in scene["stairs"]:
        original_stair=stair
        if stair.get('axis')=='x':
            stair={**stair,'x':0,'y':0}
        rise = catalog["storey_height"]
        count = math.ceil(rise / .2)
        tread, riser = stair["run"] / count, rise / count
        base, upper = stair["level"] * rise, (stair["level"] + 1) * rise

        def box(identity, center, size, level, kind, role):
            if original_stair.get('axis')=='x':
                from building_stair_frame import point
                center=point(original_stair,*center)
                size=[size[1],size[0],size[2]]
            structural_box(scene, world_point, identity, center, size, level, kind)
            scene["solids"].append({"id": identity, "role": role, "center": center,
                "size": size, "yaw": 0, "world_center": world_point(center, scene["layout"]["origin"]),
                "world_yaw": scene["layout"]["origin"]["yaw"], "level": level, "edge": None})

        if stair.get('type') == 'return':
            from building_return_stairs import add_geometry
            add_geometry(scene, stair, box)
            continue

        for index in range(count):
            height = (count - index if stair.get("reverse") else index + 1) * riser
            box(f"stair:{stair['id']}:{index}",
                [stair["x"] + stair["width"] / 2, stair["y"] + (index + .5) * tread, base + height / 2],
                [stair["width"], tread, height], stair["level"], "stair", "stair")

        if stair.get("railings", True):
            # The continuous upper shaft guard owns everything from the slab's
            # underside upwards. Clip the rising guards there: overlapping
            # coplanar outer faces caused the flicker at the upper landing.
            slab_bottom = upper - .2
            for index in range(count):
                if stair.get('enclosed'):
                    continue
                top = min(base + (count - index if stair.get("reverse") else index + 1) * riser + 1.05, slab_bottom)
                for side in (-1, 1):
                    if stair.get('wall_side') == ('left' if side == -1 else 'right'):
                        continue
                    x = stair["x"] - .06 if side == -1 else stair["x"] + stair["width"] + .06
                    box(f"guard:{stair['id']}:{index}:{side}",
                        [x, stair["y"] + (index + .5) * tread, (base + top) / 2],
                        [.12, tread, top - base], stair["level"], "guard", "guard")
            guard_height = upper + 1.1 - slab_bottom
            for side in (-1, 1):
                if stair.get('wall_side') == ('left' if side == -1 else 'right'):
                    continue
                x = stair["x"] - .06 if side == -1 else stair["x"] + stair["width"] + .06
                box(f"guard:{stair['id']}:shaft:{side}",
                    [x, stair["y"] + stair["run"] / 2, slab_bottom + guard_height / 2],
                    [.12, stair["run"], guard_height], stair["level"] + 1, "guard", "guard")
            box(f"guard:{stair['id']}:shaft:front",
                [stair["x"] + stair["width"] / 2, stair["y"] + (stair["run"] + .06 if stair.get("reverse") else -.06), slab_bottom + guard_height / 2],
                [stair["width"], .12, guard_height], stair["level"] + 1, "guard", "guard")


def door_ref(layout_id, edge_id):
    return "$/03_night_city/#building_" + layout_id + "_door_" + edge_id.replace(":", "_").replace("-", "m")


def compile_doors(scene, world_point):
    result = []
    for edge in scene["edges"]:
        mode = {"door_auto": "AUTOMATIC", "door_manual": "INTERACTIVE"}.get(edge["opening"])
        if not mode:
            continue
        visual = next(i for i in scene["instances"] if i["edge"] == edge["id"])
        visual = edge.get("frame", visual)
        a = math.radians(visual["yaw"])
        # Locate the aperture first; each native preset supplies its own
        # hinge-to-casing-centre distance and can face either side of the wall.
        middle = [visual["position"][0] - 1.5 * math.cos(a), visual["position"][1] - 1.5 * math.sin(a), visual["position"][2]]
        # Shared walls have a decorated facing on both sides of one volume.
        # Centre the casing in that volume so its back reaches the reverse
        # facing. Exterior retrofits retain their surveyed facade alignment.
        depth = scene["kit"]["wall_thickness"] / 2 if edge["shared"] else 0
        device = scene["layout"].get("door_devices", {}).get(edge["id"], {})
        if device.get('preset') == 'sliding_kitsch_double_f':
            raise ValueError('The measured double door requires a shell aperture, not a single-width grid bay')
        template, appearance, hinge = DOOR_PRESETS[device.get("preset", "sliding_entropy_c")]
        yaw = visual["yaw"] + device.get("yaw_offset", 0)
        angle = math.radians(yaw)
        offset = device.get("offset", [0, 0, 0])
        point = [middle[0] + hinge * math.cos(angle) - depth * math.sin(a) + offset[0],
                 middle[1] + hinge * math.sin(angle) + depth * math.cos(a) + offset[1], middle[2] + offset[2]]
        endpoints = [[middle[0] - direction * .8 * math.sin(a), middle[1] + direction * .8 * math.cos(a), middle[2]] for direction in (-1, 1)]
        explicit = scene["layout"].get("navigation", {}).get("door_connections", {}).get(edge["id"])
        if explicit:
            endpoints = [explicit["from"], explicit["to"]]
            # Both approach points must straddle the actual door plane and
            # cross its centre, not bridge around a wall or another doorway.
            def door_frame(p):
                dx, dy = p[0] - middle[0], p[1] - middle[1]
                return dx * math.cos(a) + dy * math.sin(a), -dx * math.sin(a) + dy * math.cos(a)
            first, last = map(door_frame, endpoints)
            if first[1] * last[1] >= 0:
                raise ValueError("Door connection endpoints must straddle the door plane")
            fraction = -first[1] / (last[1] - first[1])
            crossing = first[0] + fraction * (last[0] - first[0])
            if abs(crossing) > .35:
                raise ValueError("Door connection must cross the centred clear aperture")
        reference = door_ref(scene["layout"]["id"], edge["id"])
        result.append({"id": edge["id"], "level": edge["level"], "mode": mode,
                       "state": scene["layout"].get("door_states", {}).get(edge["id"], "CLOSED"),
                       "position": point, "world_position": world_point(point, scene["layout"]["origin"]),
                       "yaw": yaw, "world_yaw": yaw + scene["layout"]["origin"]["yaw"], "ref": reference,
                       "template": template, "appearance": appearance,
                       "connection_ref": reference + "_connection", "endpoints": endpoints,
                       "world_endpoints": [world_point(p, scene["layout"]["origin"]) for p in endpoints]})
    return result


def door_node(door, handles, buffer_id):
    properties = {"$type": "DoorSetup", "doorType": door["mode"], "doorTypeSideOne": door["mode"], "doorTypeSideTwo": door["mode"],
                  "initialDoorState": door["state"], "automaticallyClosesItself": 1, "canPlayerToggleLockState": 0,
                  "openingSpeed": 1, "doorOpeningTime": 1}
    controller_id = door.get('controller_id', DOOR_CONTROLLER_CRUID)
    if door.get('appearance', '').startswith('shutter_w300_h250_'):
        controller_id = '1563417374541762560'
        properties.update({'isShutter': 1, 'doorOpeningTime': 1.3})
    chunks = [{"$type": "DoorController", "name": cname("controller"), "id": controller_id,
               "persistentState": {"HandleId": handles.take(), "Data": {"$type": "DoorControllerPS", "doorProperties": properties}}},
              {"$type": "AIOffMeshConnectionComponent", "name": cname("offMeshConnection"), "id": DOOR_OFFMESH_CRUID,
               "offMeshConnectionNodesRefs": [node_ref(door["connection_ref"])]}]
    if door.get('component_scale'):
        sx,sy,sz=door['scale']
        for kind,name,identity in (
            ('entPhysicalMeshComponent','entropy_shutter_door_frame_w300_h_250_a','2302343969809895424'),
            ):
            chunks.append({'$type':kind,'name':cname(name),'id':identity,'visualScale':{'$type':'Vector3','X':sx,'Y':sy,'Z':sz}})
        # Skinned components have no visualScale. Scale the skeleton root so
        # both its closed mesh and opening translation follow the same size.
        chunks.append({'$type':'entAnimatedComponent','name':cname('anim'),'id':'2380823018022113280',
                       'rig':{**resource_path(r'mod\building_lab\rancho-garage.rig'),'Flags':'Obligatory'}})
        chunks.append({'$type':'entColliderComponent','name':cname('player_blocker'),'id':'2678189905129508864',
            'localTransform':{'$type':'WorldTransform','Position':{'$type':'WorldPosition',**{a:{'$type':'FixedPoint','Bits':round(v*131072)} for a,v in zip(('x','y','z'),(0,0,1.25*sz))}},
                              'Orientation':{'$type':'Quaternion','i':0,'j':0,'k':0,'r':1}},
            'colliders':[{'HandleId':handles.take(),'Data':{'$type':'physicsColliderBox','halfExtents':{'$type':'Vector3','X':1.5*sx,'Y':.02*sy,'Z':1.25*sz}}}]})
    instance = {"HandleId": handles.take(), "Data": {"$type": "entEntityInstanceData", "buffer": {
        "BufferId": str(buffer_id), "Flags": 4063232,
        "Type": "WolvenKit.RED4.Archive.Buffer.RedPackage, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null",
        "Data": {"Version": 4, "Sections": 6, "CruidIndex": -1,
                 "CruidDict": {str(i):chunk['id'] for i,chunk in enumerate(chunks)}, "Chunks": chunks}}}}
    return {"HandleId": handles.take(), "Data": {"$type": "worldDeviceNode", "debugName": cname(door["ref"]),
            "entityTemplate": resource_path(door.get("template", DOOR_ENTITY)), "appearanceName": cname(door.get("appearance", DOOR_APPEARANCE)),
            "deviceClassName": cname("DoorControllerPS"), "instanceData": instance, "deviceConnections": [],
            "entityLod": 0, "isHostOnly": 0, "isVisibleInGame": 1}}


def door_connection_node(door, handles):
    node = spline_node({"points": [[a - b for a, b in zip(point, door["world_position"])] for point in door["world_endpoints"]]}, door["connection_ref"], handles)
    node["Data"].update({"$type": "worldOffMeshConnectionNode", "type": "Door", "radius": .75, "isBidirectional": 1})
    return node


def entrance_connection_node(link, handles):
    origin = link["world_endpoints"][0]
    points = [[a - b for a, b in zip(point, origin)] for point in link["world_endpoints"]]
    node = spline_node({"points": points}, link["ref"], handles)
    node["Data"].update({"$type": "worldOffMeshConnectionNode", "type": "Floor", "radius": link["radius"], "isBidirectional": 1})
    return node
