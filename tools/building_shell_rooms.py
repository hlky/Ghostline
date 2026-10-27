"""Measured shell infills outside the editor's regular three-metre room grid.

These rooms preserve surveyed floor elevations and entrance centres. They
share native devices/navigation with the main house, rather than teleporting
between disconnected interiors.
"""
from __future__ import annotations

import math


def ceiling_join_bands(scene):
    """Wall strips over open grid/annex joins, clipped to the actual overlap."""
    layout = scene['layout']
    owners = {room['id']: room for room in layout['rooms']}
    bands = []
    for edge in scene['edges']:
        if edge['opening'] != 'passage' or len(edge['rooms']) != 1:
            continue
        owner = owners[edge['rooms'][0]]
        level = edge['level']
        upper = level * scene['kit']['storey_height'] + owner.get('ceiling_height', scene['kit']['wall_height'])
        axis = 0 if edge['axis'] == 'x' else 1
        normal = 1 - axis
        plane = edge['y'] if axis == 0 else edge['x']
        edge_start = edge['x'] if axis == 0 else edge['y']
        for shell in layout.get('shell_rooms', []):
            if shell.get('level', 0) != level:
                continue
            x, y, z = shell['position']
            low = z + shell['height']
            if upper <= low + 1e-6:
                continue
            sx, sy = (x, y) if axis == 0 else (y, x)
            length, depth = ((shell['width'], shell['depth']) if axis == 0
                             else (shell['depth'], shell['width']))
            if min(abs(sy-plane), abs(sy+depth-plane)) > 1e-6:
                continue
            left, right = max(edge_start, sx), min(edge_start+3, sx+length)
            if right-left < .1:
                continue
            top = upper + .1
            spans = [(left, right)]
            # A custom liner or existing lintel may already close the join.
            for solid in scene['solids']:
                if solid['role'] != 'wall' or solid['level'] != level:
                    continue
                cx, cy, cz = solid['center']
                w, d, h = solid['size']
                if cz-h/2 > low+1e-6 or cz+h/2 < top-1e-6:
                    continue
                angle = math.radians(solid['yaw'])
                # Only parallel walls replace a band facing. Perpendicular
                # walls need an overlapping corner joint: subtracting their
                # thickness leaves a slit on the other side of the corner.
                parallel = abs(math.cos(angle)) if axis == 0 else abs(math.sin(angle))
                if parallel < 1-1e-6:
                    continue
                extent = [(abs(w*math.cos(angle))+abs(d*math.sin(angle)))/2,
                          (abs(w*math.sin(angle))+abs(d*math.cos(angle)))/2]
                center = [cx, cy]
                if abs(center[normal]-plane) > extent[normal]+1e-6:
                    continue
                a, b = center[axis]-extent[axis], center[axis]+extent[axis]
                spans = [(u, v) for start, end in spans
                         for u, v in ((start, min(end, a)), (max(start, b), end))
                         if v-u >= .1]
            for index, (a, b) in enumerate(spans):
                start, end = ([a, plane, low], [b, plane, low]) if axis == 0 else (
                    [plane, b, low], [plane, a, low])
                if edge['side'] in ('north', 'east'):
                    start, end = end, start
                bands.append((f"ceiling-join:{shell['id']}:{edge['id']}:{index}",
                              start, end, top-low, level))
    return bands


def compile_shell_rooms(scene, world_point):
    from building_builder import number, ID
    from building_features import door_ref, DOOR_PRESETS

    layout, catalog = scene["layout"], scene["kit"]
    rooms = layout.get("shell_rooms", [])
    liners = layout.get("shell_liners", [])
    devices = layout.get("shell_doors", [])
    if not isinstance(rooms, list) or len(rooms) > 8 or not isinstance(liners, list) or len(liners) > 16 or not isinstance(devices, list) or len(devices) > 8:
        raise ValueError("Shell infills support eight rooms/devices and sixteen liners")
    if (rooms and catalog["id"] != "rancho-3m") or (liners and catalog["id"] not in ("rancho-3m", "common-3m")):
        raise ValueError("Measured rooms require Rancho; liners require a measured Rancho or common wall contract")
    used = {r["id"] for r in layout["rooms"]}
    scene["shell_rooms"], scene["shell_steps"], scene["shell_doors"] = [], [], []

    def point(value):
        if not isinstance(value, list) or len(value) != 3:
            raise ValueError("Shell points need local XYZ values")
        return [number(v, "Shell coordinate", -100, 100) for v in value]

    def mesh(identity, role, p, size, yaw=0, level=0, foundation=False):
        # Normalize the source mesh bounds, including its buried foundation.
        source = catalog["pieces"][role]
        scale = [size[0] / 3, size[1] / (.15 if role == "wall" else 3), 1]
        if role == "wall":
            if catalog["id"] == "common-3m":
                # Measured common wall: X=-3.005..0.005, Y=0..0.23,
                # Z=0..3.8. Normalize its lip so liner ends meet exactly.
                scale = [size[0] / 3.01, size[1] / .23, size[2] / 3.8]
                angle = math.radians(yaw)
                p = [p[0] - .005 * scale[0] * math.cos(angle),
                     p[1] - .005 * scale[0] * math.sin(angle), p[2]]
            else:
                depth = .2988104820251465
                scale[2] = size[2] / (4 + depth)
                p = [*p[:2], p[2] + depth * scale[2]]
        elif role == "floor":
            scale = [size[0] / 3.005, size[1] / 3.005, size[2] / .2]
            p = [p[0] - .0025 * scale[0], p[1] - .0025 * scale[1], p[2]]
        else:
            scale[2] = size[2] / .1
        scene["instances"].append({"id": identity, "role": role, "kind": "shell", "mesh": source["mesh"],
            "appearance": layout["floor_appearance"] if role == "floor" else ("concrete" if role == "ceiling" else layout["wall_appearance"]),
            "position": p, "yaw": yaw, "scale": scale, "world_position": world_point(p, layout["origin"]),
            "world_yaw": yaw + layout["origin"]["yaw"], "level": level, "room": None, "edge": None})

    def solid(identity, center, size, level, yaw=0, role="wall"):
        scene["solids"].append({"id": identity, "role": role, "center": center, "size": size, "yaw": yaw,
            "world_center": world_point(center, layout["origin"]), "world_yaw": yaw + layout["origin"]["yaw"], "level": level, "edge": None})

    def wall(identity, start, end, h, level, openings, double_sided=False):
        dx, dy = end[0] - start[0], end[1] - start[1]
        length = math.hypot(dx, dy)
        if length < .1 or (abs(dx) > 1e-6 and abs(dy) > 1e-6):
            raise ValueError("Shell liners must be axis-aligned and at least 10 cm long")
        ux, uy = dx / length, dy / length
        yaw = math.degrees(math.atan2(uy, ux))
        parts, cursor = [], 0
        for opening in sorted(openings, key=lambda o: o["center"]):
            center = number(opening.get("center"), "Shell opening centre", 0, length)
            width = number(opening.get("width"), "Shell opening width", .7, 6)
            clear = number(opening.get("height"), "Shell opening height", 2, h)
            left, right = center - width / 2, center + width / 2
            if left < cursor or right > length:
                raise ValueError("Shell openings must fit their liner without overlapping")
            parts.extend([(cursor, left, 0, h), (left, right, clear, h)])
            cursor = right
        parts.append((cursor, length, 0, h))
        for index, (a, b, bottom, top) in enumerate(parts):
            if b - a < 1e-6 or top - bottom < 1e-6:
                continue
            root = [start[0] + ux * b, start[1] + uy * b, start[2] + bottom]
            identity_part = f"shell:{identity}:{index}"
            thickness = catalog['wall_thickness']
            mesh(identity_part, "wall", root, [b-a, thickness, top-bottom], yaw, level)
            if double_sided:
                reverse=[start[0]+ux*a-uy*thickness,start[1]+uy*a+ux*thickness,start[2]+bottom]
                mesh(identity_part+':reverse','wall',reverse,[b-a,thickness,top-bottom],yaw+180,level)
            solid(identity_part, [start[0]+ux*(a+b)/2-uy*thickness/2, start[1]+uy*(a+b)/2+ux*thickness/2, start[2]+(top+bottom)/2],
                  [b-a, thickness, top-bottom], level, yaw)

    for room in rooms:
        if not isinstance(room, dict) or not ID.fullmatch(room.get("id", "")) or room["id"] in used:
            raise ValueError("Shell room IDs must be unique")
        used.add(room["id"])
        x, y, z = point(room.get("position"))
        width = number(room.get("width"), "Shell room width", .9, 20)
        depth = number(room.get("depth"), "Shell room depth", .9, 20)
        height = number(room.get("height"), "Shell room height", 2.4, 4)
        level = room.get("level", 0)
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 3:
            raise ValueError("Shell room level must be 0..3")
        rectangle = [x, y, x+width, y+depth]
        for main in layout["rooms"]:
            if main["level"] == level and x < main["x"]+main["width"]-1e-6 and x+width > main["x"]+1e-6 and y < main["y"]+main["depth"]-1e-6 and y+depth > main["y"]+1e-6:
                raise ValueError("Measured shell rooms must not overlap gridded rooms")
        for prior in scene["shell_rooms"]:
            a, b, c, d = prior["bounds"]
            if prior["level"] == level and x < c and x+width > a and y < d and y+depth > b:
                raise ValueError("Measured shell rooms must not overlap each other")
        footprints = [rectangle]
        from shapely.geometry import box
        from shapely.ops import unary_union
        for extension in room.get('extensions', []):
            ex,ey = [number(v,'Extension coordinate',-100,100) for v in extension['position']]
            ew = number(extension['width'],'Extension width',.9,20)
            ed = number(extension['depth'],'Extension depth',.9,20)
            extra = [ex,ey,ex+ew,ey+ed]
            shape = box(*extra)
            prior_shape = unary_union([box(*r) for r in footprints])
            if prior_shape.intersection(shape).area > 1e-8 or prior_shape.boundary.intersection(shape.boundary).length < .9:
                raise ValueError('Shell extensions must share a wall without overlapping')
            for main in layout['rooms']:
                if main['level']==level and shape.intersection(box(main['x'],main['y'],main['x']+main['width'],main['y']+main['depth'])).area > 1e-8:
                    raise ValueError('Shell extensions must not overlap gridded rooms')
            footprints.append(extra)
            suffix = str(len(footprints)-1)
            mesh('shell:'+room['id']+':extension-floor:'+suffix,'floor',[ex+ew,ey+ed,z],[ew,ed,.2],level=level)
            if 'floor_appearance' in room:
                scene['instances'][-1]['appearance']=room['floor_appearance']
            solid('shell:'+room['id']+':extension-floor:'+suffix,[ex+ew/2,ey+ed/2,z-.1],[ew,ed,.2],level,role='floor')
            mesh('shell:'+room['id']+':extension-ceiling:'+suffix,'ceiling',[ex+ew,ey+ed,z+height],[ew,ed,.1],level=level)
            solid('shell:'+room['id']+':extension-ceiling:'+suffix,[ex+ew/2,ey+ed/2,z+height+.05],[ew,ed,.1],level,role='ceiling')
        for prior in scene['shell_rooms']:
            if prior['level']==level and unary_union([box(*r) for r in footprints]).intersection(unary_union([box(*r) for r in prior['footprints']])).area > 1e-8:
                raise ValueError('Measured shell footprints must not overlap each other')
        outline = list(unary_union([box(*r) for r in footprints]).exterior.coords)
        scene["shell_rooms"].append({"id": room["id"], "bounds": rectangle, 'footprints': footprints, 'outline': outline, "z": z, "level": level})
        mesh("shell:"+room["id"]+":floor", "floor", [x+width,y+depth,z], [width,depth,.2], level=level)
        if 'floor_appearance' in room:
            if room['floor_appearance'] not in catalog['floor_appearances']:
                raise ValueError('Unknown shell floor appearance')
            scene['instances'][-1]['appearance'] = room['floor_appearance']
        solid("shell:"+room["id"]+":floor", [x+width/2,y+depth/2,z-.1], [width,depth,.2], level, role="floor")
        mesh("shell:"+room["id"]+":ceiling", "ceiling", [x+width,y+depth,z+height], [width,depth,.1], level=level)
        solid("shell:"+room["id"]+":ceiling", [x+width/2,y+depth/2,z+height+.05], [width,depth,.1], level, role="ceiling")
        sides = {"south": ([x,y,z],[x+width,y,z]), "east": ([x+width,y,z],[x+width,y+depth,z]),
                 "north": ([x+width,y+depth,z],[x,y+depth,z]), "west": ([x,y+depth,z],[x,y,z])}
        for side, (start, end) in sides.items():
            settings = room.get("walls", {}).get(side, {})
            if settings is False:
                continue
            if not isinstance(settings, dict):
                raise ValueError("Shell wall settings must be an object or false")
            wall(room["id"]+":"+side, start, end, height+.1, level, settings.get("openings", []),
                 settings.get('double_sided', False))
    for index, liner in enumerate(liners):
        if liner.get('disabled',False):
            continue
        # Raised liners can be short bulkheads, not only full-height walls.
        wall("liner:"+str(index), point(liner.get("start")), point(liner.get("end")), number(liner.get("height"), "Liner height", .1, 4),
             int(number(liner.get("level", 0), "Liner level", 0, 3)), liner.get("openings", []), liner.get('double_sided',False))
    # Open measured annexes can meet a taller gridded room across only part
    # of a bay. Close the height difference without closing the passage below.
    for identity, start, end, height, level in ceiling_join_bands(scene):
        wall(identity, start, end, height, level, [], True)
    for device in devices:
        identity = device.get("id", "")
        if not ID.fullmatch(identity) or any(d["id"] == identity for d in scene["shell_doors"]):
            raise ValueError("Shell device IDs must be unique")
        position = point(device.get("position"))
        endpoints = [point(device.get(k)) for k in ("from", "to")]
        if math.dist(*endpoints) > 4 or abs(endpoints[0][2]-endpoints[1][2]) > .6:
            raise ValueError("Shell door endpoints must span at most 4 m and 0.6 m vertically")
        template, appearance, _ = DOOR_PRESETS[device.get("preset", "sliding_entropy_c")]
        yaw = number(device.get("yaw"), "Shell door yaw", -360, 360)
        ref = door_ref(layout["id"], identity)
        gate = device.get("gate")
        if not isinstance(gate, list) or len(gate) != 4:
            raise ValueError("Shell door needs its four-coordinate gate bounds")
        gate = [number(v, "Shell gate coordinate", -100, 100) for v in gate]
        if gate[2] <= gate[0] or gate[3] <= gate[1]:
            raise ValueError("Shell gate must have area")
        state = layout.get("door_states", {}).get(identity, "CLOSED")
        if state not in ('CLOSED', 'OPENED', 'LOCKED'):
            raise ValueError('Invalid shell door state')
        scale = device.get('scale', [1, 1, 1])
        if not isinstance(scale, list) or len(scale) != 3:
            raise ValueError('Shell door scale needs three positive values')
        scale = [number(v, 'Shell door scale', .5, 2) for v in scale]
        mode = device.get('mode', 'AUTOMATIC')
        if mode not in ('AUTOMATIC', 'INTERACTIVE'):
            raise ValueError('Shell door mode must be AUTOMATIC or INTERACTIVE')
        scene["shell_doors"].append({"id":identity,"level":device.get("level",0),"mode":mode,"state":state,
            "position":position,"world_position":world_point(position,layout["origin"]),"yaw":yaw,"world_yaw":yaw+layout["origin"]["yaw"],
            "ref":ref,"connection_ref":ref+"_connection","template":template,"appearance":appearance,"scale":scale,
                       "component_scale":device.get('preset')=='garage_w300_h250' and device.get('scale',[1,1,1]) != [1,1,1],
            "restore_auto_close":bool(device.get('restore_auto_close', False)),
            "endpoints":endpoints,"world_endpoints":[world_point(p,layout["origin"]) for p in endpoints],"gate":gate})
    for step in layout.get("shell_steps", []):
        x,y,z = point(step.get("position"))
        axis = step.get('axis','y')
        if axis not in ('x','y'):
            raise ValueError('Shell step axis must be x or y')
        from building_stair_frame import point as stair_point
        frame = {'x':x,'y':y,'axis':axis}
        width = number(step.get("width"), "Shell step width", 1.2, 4)
        run = number(step.get("run"), "Shell step run", .5, 4)
        rise = number(step.get("rise"), "Shell step rise", .1, 1)
        landing = number(step.get("landing", .8), "Shell step landing", .6, 2)
        if math.degrees(math.atan2(rise,run)) > 35:
            raise ValueError("Shell steps must be no steeper than 35 degrees")
        level = step.get("level",0)
        count = math.ceil(rise/.2)
        for i in range(count):
            h=(i+1)*rise/count
            from building_features import structural_box
            center=stair_point(frame,width/2,(i+.5)*run/count,z+h/2)
            size=[run/count,width,h] if axis=='x' else [width,run/count,h]
            structural_box(scene,world_point,f"shell-step:{step['id']}:{i}",center,size,level,"shell-step")
            solid(f"shell-step:{step['id']}:{i}",center,size,level,role="stair")
        from building_features import structural_box
        center=stair_point(frame,width/2,run+landing/2,z+rise/2)
        size=[landing,width,rise] if axis=='x' else [width,landing,rise]
        structural_box(scene,world_point,f"shell-step:{step['id']}:landing",center,size,level,"shell-step")
        solid(f"shell-step:{step['id']}:landing",center,size,level,role="stair")
        scene["shell_steps"].append({"x":x,"y":y,"z":z,'axis':axis,"width":width,"run":run,"rise":rise,"landing":landing,"level":level})
    for index, blocker in enumerate(layout.get("shell_blockers", [])):
        center = point(blocker.get("center"))
        size = point(blocker.get("size"))
        if any(v <= 0 or v > 20 for v in size):
            raise ValueError("Shell blocker sizes must be positive and no larger than 20 m")
        yaw=number(blocker.get('yaw',0),'Shell blocker yaw',-360,360)
        solid("shell:blocker:"+str(index), center, size, blocker.get("level",0), yaw, role="module_blocker")
        if 'rotation' in blocker:
            rotation = blocker['rotation']
            if not isinstance(rotation, list) or len(rotation) != 4:
                raise ValueError('Shell blocker rotation needs a local unit quaternion')
            x,y,z,w = [number(v,'Shell blocker quaternion',-1,1) for v in rotation]
            if abs(x*x+y*y+z*z+w*w-1) > 1e-4:
                raise ValueError('Shell blocker rotation needs a local unit quaternion')
            angle = math.radians(layout['origin']['yaw']) / 2
            sine, cosine = math.sin(angle), math.cos(angle)
            scene['solids'][-1]['world_orientation'] = [cosine*x-sine*y, cosine*y+sine*x,
                                                       cosine*z+sine*w, cosine*w-sine*z]
    for index, plinth in enumerate(layout.get("shell_plinths", [])):
        from building_features import structural_box
        center, size = point(plinth.get("center")), point(plinth.get("size"))
        if any(v <= 0 or v > 20 for v in size):
            raise ValueError("Shell plinth sizes must be positive and no larger than 20 m")
        level = plinth.get("level", 0)
        walkable = plinth.get('walkable', False)
        if not isinstance(walkable, bool):
            raise ValueError("Plinth walkable flag must be boolean")
        if walkable:
            # A thin inset floor cap covers retained terrain without moving
            # the street, entrance device or original collision geometry.
            from shapely.geometry import box
            from shapely.ops import unary_union
            floor = unary_union([box(r['x'], r['y'], r['x']+r['width'], r['y']+r['depth'])
                                 for r in layout['rooms'] if r['level'] == level])
            footprint = box(center[0]-size[0]/2, center[1]-size[1]/2,
                            center[0]+size[0]/2, center[1]+size[1]/2)
            if size[2] > .2 or not floor.covers(footprint) or abs(center[2]-size[2]/2-level*catalog['storey_height']) > 1e-6:
                raise ValueError("Walkable floor caps must sit on the room floor, stay inside it and be at most 20 cm high")
        structural_box(scene, world_point, "shell:plinth:"+str(index), center, size, level, "plinth")
        solid("shell:plinth:"+str(index), center, size, level, role="floor" if walkable else "module_blocker")


def shell_navigation(scene, radius, height, leaf_obstacles):
    from shapely.geometry import Polygon, box
    from shapely.ops import unary_union
    from shapely import constrained_delaunay_triangles
    from building_navigation import _polygons, _constrain

    triangles = []
    for room in scene.get("shell_rooms", []):
        obstacles=[]
        for solid in scene["solids"]:
            if solid["role"] not in ("wall","guard","module_blocker"):
                continue
            zmin,zmax=solid["center"][2]-solid["size"][2]/2,solid["center"][2]+solid["size"][2]/2
            if zmax <= room["z"]+.01 or zmin >= room["z"]+height:
                continue
            a=math.radians(solid["yaw"]);x,y=solid["center"][:2];w,d=solid["size"][:2]
            obstacles.append(Polygon([(x+u*math.cos(a)-v*math.sin(a),y+u*math.sin(a)+v*math.cos(a)) for u,v in [(-w/2,-d/2),(w/2,-d/2),(w/2,d/2),(-w/2,d/2)]]))
        obstacles.extend(Polygon(leaf["polygon"]) for leaf in leaf_obstacles if leaf["level"]==room["level"])
        usable=unary_union([box(*r) for r in room['footprints']]).difference(unary_union(obstacles)).buffer(-radius,join_style="mitre")
        attachments=[]
        for step in scene.get("shell_steps", []):
            if step["level"] != room["level"]:
                continue
            x,y,w,run=(step[k] for k in ("x","y","width","run"))
            from building_stair_frame import point as stair_point, rectangle
            usable=usable.difference(box(*rectangle(step,[0,0,w,run+step['landing']])))
            attachments.extend([tuple(stair_point(step,u,v,0)[:2]) for u in (radius,w-radius) for v in (0,run+step['landing'])])
        for door in scene.get("doors", []):
            if door.get("gate") and door["level"]==room["level"]:
                usable=usable.difference(box(*door["gate"]))
        for polygon in _polygons(usable):
            for triangle in constrained_delaunay_triangles(_constrain(polygon,attachments)).geoms:
                if triangle.area>1e-8:
                    triangles.append([[x,y,room["z"]] for x,y in list(triangle.exterior.coords)[:3]])
    for step in scene.get("shell_steps", []):
        x,y,z,w,run,rise,landing=(step[k] for k in ("x","y","z","width","run","rise","landing"))
        # A landing is a walk surface too: it must respect open leaves and
        # device gates, rather than reintroducing a corner cut after erosion.
        leaves = unary_union([Polygon(leaf["polygon"]).buffer(radius, join_style="mitre")
                              for leaf in leaf_obstacles if leaf["level"] == step["level"]])
        gates = unary_union([box(*door["gate"]) for door in scene.get("doors", [])
                             if door.get("gate") and door["level"] == step["level"]])
        from building_stair_frame import rectangle
        for low, high, ramp in ((0, run, True), (run, run+landing, False)):
            usable = box(*rectangle(step,[radius,low,w-radius,high])).difference(leaves).difference(gates)
            if not ramp:
                # A landing entering a regular room already has a floor
                # surface there. Do not leave a duplicate isolated overlay.
                floors=[box(r['x'],r['y'],r['x']+r['width'],r['y']+r['depth'])
                        for r in scene['layout']['rooms']
                        if abs(r['level']*scene['kit']['storey_height']-(z+rise))<1e-6]
                usable=usable.difference(unary_union(floors))
            for polygon in _polygons(usable):
                for triangle in constrained_delaunay_triangles(polygon).geoms:
                    if triangle.area > 1e-8:
                        triangles.append([[px, py, z+rise*((px-x) if step['axis']=='x' else (py-y))/run if ramp else z+rise]
                                          for px, py in list(triangle.exterior.coords)[:3]])
    return triangles
