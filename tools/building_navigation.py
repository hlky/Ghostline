"""Human navigation surfaces and experimental native VAND v8 tiles.

The wire format follows measured vanilla tiles and WolvenKit TilesReader.
Detour supplies the interpretation of polygon/detail/BV records. This is a
parametric surface compiler, not a general mesh voxelizer or a runtime proof.
"""
from __future__ import annotations

import base64
from collections import defaultdict, deque
import math
import struct

from shapely import constrained_delaunay_triangles
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

TILE_SIZE = 32.4


def transform(point, origin):
    x, y, z = point
    angle = math.radians(origin["yaw"])
    return [origin["x"] + x * math.cos(angle) - y * math.sin(angle),
            origin["y"] + x * math.sin(angle) + y * math.cos(angle), origin["z"] + z]


def _ring_with_points(ring, points):
    result = []
    coords = list(ring.coords)
    for a, b in zip(coords, coords[1:]):
        result.append(a)
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = dx * dx + dy * dy
        if not length:
            continue
        interior = []
        for p in points:
            t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / length
            if 1e-8 < t < 1 - 1e-8 and abs((p[0] - a[0]) * dy - (p[1] - a[1]) * dx) < 1e-7:
                interior.append((t, p))
        result.extend(p for _, p in sorted(set(interior)))
    return result


def _constrain(polygon, points):
    return Polygon(_ring_with_points(polygon.exterior, points),
                   [_ring_with_points(ring, points) for ring in polygon.interiors])


def _polygons(geometry):
    if geometry.geom_type == "Polygon":
        return [geometry] if geometry.area > 1e-8 else []
    return [part for item in getattr(geometry, "geoms", []) for part in _polygons(item)]


def compile_navigation(scene):
    """Build clearance-aware floor surfaces and stair ramps from compiled solids."""
    layout, catalog = scene["layout"], scene["kit"]
    settings = layout.get("navigation", {})
    radius = settings.get("radius", .3)
    height = settings.get("height", 1.8)
    if isinstance(radius, bool) or not isinstance(radius, (float, int)) or not math.isfinite(radius) or not .2 <= radius <= .65:
        raise ValueError("Navigation radius must be between 0.2 and 0.65 m")
    if isinstance(height, bool) or not isinstance(height, (float, int)) or not math.isfinite(height) or not 1.2 <= height <= 2.4:
        raise ValueError("Navigation height must be between 1.2 and 2.4 m")
    triangles = []
    reserve_leaves = settings.get("reserve_open_door_leaves", True)
    if not isinstance(reserve_leaves, bool):
        raise ValueError("Open door leaf clearance must be enabled or disabled")
    from building_features import open_door_leaf
    leaf_obstacles = [{"id": d["id"], "level": d["level"], "polygon": polygon}
                      for d in scene.get("doors", []) if reserve_leaves and (polygon := open_door_leaf(d))]
    stairs = scene.get("stairs", [])
    for level in sorted({room["level"] for room in layout["rooms"]}):
        rooms = [box(r["x"], r["y"], r["x"] + r["width"], r["y"] + r["depth"])
                 for r in layout["rooms"] if r["level"] == level]
        obstacles = []
        for solid in scene["solids"]:
            if solid["role"] not in ("wall", "guard", "module_blocker"):
                continue
            floor_z = level * catalog["storey_height"]
            if solid["role"] != "module_blocker" and solid["level"] != level:
                continue
            if solid["role"] == "module_blocker" and solid["center"][2] + solid["size"][2] / 2 <= floor_z + .01:
                continue
            # Lintels above the agent are not obstacles at floor height.
            if solid["center"][2] - solid["size"][2] / 2 >= level * catalog["storey_height"] + height:
                continue
            x, y = solid["center"][:2]
            w, d = solid["size"][:2]
            a = math.radians(solid["yaw"])
            obstacles.append(Polygon([(x + u * math.cos(a) - v * math.sin(a), y + u * math.sin(a) + v * math.cos(a))
                                      for u, v in [(-w / 2, -d / 2), (w / 2, -d / 2), (w / 2, d / 2), (-w / 2, d / 2)]]))
        # Device links gate locked/closed doors, but do not carve an open
        # physical leaf from additive navigation. Reserve its measured pose
        # before agent-radius erosion, so later steering cannot cut through it.
        obstacles.extend(Polygon(leaf["polygon"]) for leaf in leaf_obstacles if leaf["level"] == level)
        usable = unary_union(rooms).difference(unary_union(obstacles)).buffer(-radius, join_style="mitre")
        # A device-controlled door must be crossed through its off-mesh link,
        # not through an always-connected ground polygon beneath a locked leaf.
        for door in scene.get("doors", []):
            if door["level"] != level:
                continue
            if door.get("gate"):
                usable = usable.difference(box(*door["gate"]))
                continue
            edge = next(e for e in scene["edges"] if e["id"] == door["id"])
            if edge["axis"] == "x":
                gate = box(edge["x"] + .5, edge["y"] - .04, edge["x"] + 2.5, edge["y"] + .04)
            else:
                gate = box(edge["x"] - .04, edge["y"] + .5, edge["x"] + .04, edge["y"] + 2.5)
            usable = usable.difference(gate)
        attachments = []
        for stair in stairs:
            if level not in (stair["level"], stair["level"] + 1):
                continue
            x, y, w, run = (stair[k] for k in ("x", "y", "width", "run"))
            if stair.get('type') == 'return':
                from building_return_stairs import bounds, flight_edges
                usable = usable.difference(box(*bounds(stair)))
                wall_clearance = max(0, catalog['wall_thickness'] - catalog.get('wall_facing_depth', catalog['wall_thickness']))
                attachments.extend([(v, y+run) for v in flight_edges(stair, radius, wall_clearance)])
                continue
            from building_stair_frame import shaft, point
            usable = usable.difference(box(*shaft(stair)))
            attachments.extend([tuple(point(stair,u,v,0)[:2]) for u,v in ((radius,0),(w-radius,0),(radius,run),(w-radius,run))])
        for polygon in _polygons(usable):
            for triangle in constrained_delaunay_triangles(_constrain(polygon, attachments)).geoms:
                if triangle.area > 1e-8:
                    triangles.append([[x, y, level * catalog["storey_height"]] for x, y in list(triangle.exterior.coords)[:3]])
    for stair in stairs:
        if stair.get('type') == 'return':
            from building_return_stairs import navigation
            wall_clearance = max(0, catalog['wall_thickness'] - catalog.get('wall_facing_depth', catalog['wall_thickness']))
            triangles.extend(navigation(stair, catalog['storey_height'], radius, wall_clearance))
            continue
        x, y, w, run = (stair[k] for k in ("x", "y", "width", "run"))
        z = stair["level"] * catalog["storey_height"]
        rise = catalog["storey_height"]
        a, b = [x + radius, y, z], [x + w - radius, y, z]
        c, d = [x + w - radius, y + run, z + rise], [x + radius, y + run, z + rise]
        if stair.get("reverse"):
            a[2] = b[2] = z + rise
            c[2] = d[2] = z
        if stair.get('axis')=='x':
            from building_stair_frame import point
            a,b,c,d=[point(stair,p[0]-x,p[1]-y,p[2]) for p in (a,b,c,d)]
        triangles.extend([[a, b, c], [a, c, d]])
    # Surveyed retained porches/stairs can contribute explicit walk surfaces.
    # These do not create physical geometry: source collision must be retained.
    surfaces = settings.get("surfaces", [])
    if not isinstance(surfaces, list) or len(surfaces) > 128:
        raise ValueError("At most 128 surveyed navigation triangles are supported")
    for triangle in surfaces:
        if not isinstance(triangle, list) or len(triangle) != 3 or any(
                not isinstance(p, list) or len(p) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or abs(v) > 100 for v in p) for p in triangle):
            raise ValueError("Surveyed navigation surfaces need three finite local XYZ vertices")
        u, v = [[triangle[i][j] - triangle[0][j] for j in range(3)] for i in (1, 2)]
        normal = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
        if abs(normal[2]) < 1e-8 or math.degrees(math.atan2(math.hypot(*normal[:2]), abs(normal[2]))) > 35:
            raise ValueError("Surveyed navigation triangles must have area and slope at most 35 degrees")
        triangles.append(triangle)
    # Nav coordinates are baked in world space; node placement never rebakes them.
    from building_shell_rooms import shell_navigation
    triangles.extend(shell_navigation(scene, radius, height, leaf_obstacles))
    world_triangles = [[transform(p, layout["origin"]) for p in triangle] for triangle in triangles]
    graph = adjacency(triangles)
    links = []
    from generate_world import node_ref_hash
    for door in scene.get("doors", []):
        first, last = (locate_face(triangles, p) for p in door["endpoints"])
        if first is None and last is not None:
            # Detour attaches an off-mesh start to its owning tile. For a
            # street entrance the inside endpoint must therefore come first.
            door["endpoints"] = list(reversed(door["endpoints"]))
            door["world_endpoints"] = list(reversed(door["world_endpoints"]))
            first, last = last, first
        if first is None and door["id"] in settings.get("door_connections", {}):
            raise ValueError("An explicit door connection must touch this building's walkable surface")
        link = {"id": str(node_ref_hash(door["connection_ref"])), "ref": door["connection_ref"],
                "endpoints": door["endpoints"], "world_endpoints": door["world_endpoints"], "radius": .75,
                "enabled": door["state"] != "LOCKED", "area": 10, "external": last is None}
        links.append(link)
        if link["enabled"]:
            a, b = (locate_face(triangles, p) for p in link["endpoints"])
            if a is not None and b is not None:
                graph[a] = sorted(set(graph[a]) | {b})
                graph[b] = sorted(set(graph[b]) | {a})
    connections = settings.get("connections", [])
    if not isinstance(connections, list) or len(connections) > 32:
        raise ValueError("At most 32 navigation entrance connections are supported")
    used = set()
    import re
    for connection in connections:
        if not isinstance(connection, dict) or not isinstance(connection.get("id"), str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,47}", connection["id"]) or connection["id"] in used:
            raise ValueError("Navigation connection ids must be unique lowercase identifiers")
        used.add(connection["id"])
        endpoints = [connection.get("from"), connection.get("to")]
        if any(not isinstance(p, list) or len(p) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or abs(v) > 100 for v in p) for p in endpoints):
            raise ValueError("Navigation connections need local X/Y/Z endpoint triples")
        if math.dist(*endpoints) > 4 or abs(endpoints[0][2] - endpoints[1][2]) > .600001:
            raise ValueError("Entrance connections must span at most 4 m and 0.6 m vertically; use physical stairs for larger height changes")
        first, last = [locate_face(triangles, p) for p in endpoints]
        if first is None:
            raise ValueError("Entrance connection must start on this building's walkable surface")
        reference = "$/03_night_city/#building_" + layout["id"] + "_entrance_" + connection["id"]
        links.append({"id": str(node_ref_hash(reference)), "ref": reference, "endpoints": endpoints,
                      "world_endpoints": [transform(p, layout["origin"]) for p in endpoints],
                      "radius": .5, "enabled": True, "area": 3, "kind": "entrance", "external": last is None})
        if last is not None:
            graph[first] = sorted(set(graph[first]) | {last})
            graph[last] = sorted(set(graph[last]) | {first})
    seen, islands = set(), []
    for start in range(len(triangles)):
        if start in seen:
            continue
        queue, island = [start], []
        seen.add(start)
        while queue:
            face = queue.pop()
            island.append(face)
            for neighbor in graph[face]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        islands.append(island)
    return {"status": "experimental-native", "radius": radius, "height": height, "climb": .6,
            "door_leaf_obstacles": leaf_obstacles,
            "triangles": triangles, "world_triangles": world_triangles,
            "adjacency": graph, "islands": islands, "links": links,
            "stats": {"triangles": len(triangles), "islands": len(islands)},
            "runtime_verified": False}


def vertex_key(point):
    return tuple(round(x, 5) for x in point)


def adjacency(triangles):
    edges = defaultdict(list)
    result = [set() for _ in triangles]
    for index, triangle in enumerate(triangles):
        for a, b in zip(triangle, triangle[1:] + triangle[:1]):
            edges[tuple(sorted((vertex_key(a), vertex_key(b))))].append(index)
    for faces in edges.values():
        for face in faces:
            result[face].update(other for other in faces if other != face)
    return [sorted(neighbors) for neighbors in result]


def locate_face(triangles, point):
    from shapely.geometry import Point
    for i, triangle in enumerate(triangles):
        polygon = Polygon([p[:2] for p in triangle])
        if polygon.buffer(1e-7).covers(Point(point[:2])):
            a, b, c = triangle
            # Height on the triangular surface, including ramps.
            denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
            if abs(denominator) < 1e-10:
                continue
            u = ((b[1] - c[1]) * (point[0] - c[0]) + (c[0] - b[0]) * (point[1] - c[1])) / denominator
            v = ((c[1] - a[1]) * (point[0] - c[0]) + (a[0] - c[0]) * (point[1] - c[1])) / denominator
            z = u * a[2] + v * b[2] + (1 - u - v) * c[2]
            if abs(z - point[2]) <= .35:
                return i
    return None


def route(navigation, start, end):
    """Return an offline polygon route; it does not query the game's AI system."""
    triangles = navigation["triangles"]
    first, last = locate_face(triangles, start), locate_face(triangles, end)
    if first is None or last is None:
        return {"reachable": False, "reason": "An endpoint is outside agent clearance or on another floor", "faces": []}
    previous, queue = {first: None}, deque([first])
    while queue:
        face = queue.popleft()
        if face == last:
            path = []
            while face is not None:
                path.append(face)
                face = previous[face]
            return {"reachable": True, "faces": path[::-1], "reason": "Offline surface connectivity only"}
        for neighbor in navigation["adjacency"][face]:
            if neighbor not in previous:
                previous[neighbor] = face
                queue.append(neighbor)
    return {"reachable": False, "reason": "Endpoints are on disconnected walkable islands", "faces": []}


def _tile_triangles(triangles):
    """Clip triangles to vanilla's 32.4 m world grid, retaining interpolated Z."""
    groups = defaultdict(list)
    for triangle in triangles:
        polygon = Polygon([p[:2] for p in triangle])
        xmin, ymin, xmax, ymax = polygon.bounds
        a, b, c = triangle
        denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
        for tx in range(math.floor(xmin / TILE_SIZE), math.floor(xmax / TILE_SIZE) + 1):
            for ty in range(math.floor(ymin / TILE_SIZE), math.floor(ymax / TILE_SIZE) + 1):
                clipped = polygon.intersection(box(tx * TILE_SIZE, ty * TILE_SIZE, (tx + 1) * TILE_SIZE, (ty + 1) * TILE_SIZE))
                for part in _polygons(clipped):
                    for t in constrained_delaunay_triangles(part).geoms:
                        points = []
                        for x, y in list(t.exterior.coords)[:3]:
                            u = ((b[1] - c[1]) * (x - c[0]) + (c[0] - b[0]) * (y - c[1])) / denominator
                            v = ((c[1] - a[1]) * (x - c[0]) + (a[0] - c[0]) * (y - c[1])) / denominator
                            points.append([x, y, u * a[2] + v * b[2] + (1 - u - v) * c[2]])
                        groups[tx, ty].append(points)
    return groups


def _bv_tree(vertices, faces, bounds_min, quantization=10):
    """Encode Detour's quantized polygon BV tree, as present in vanilla tiles.

    Use VAND X/Z/Y axes, pre-order nodes and negative subtree escape indexes.
    The allocated table has 2*N slots, including its final zero padding slot.
    """
    items = []
    for index, face in enumerate(faces):
        points = [[vertices[v][0], vertices[v][2], vertices[v][1]] for v in face]
        quantize = lambda value, axis: max(0, min(65535, int((value - bounds_min[axis]) * quantization)))
        lower = [quantize(min(p[a] for p in points), a) for a in range(3)]
        upper = [quantize(max(p[a] for p in points), a) for a in range(3)]
        items.append((lower, upper, index))
    nodes = []

    def subdivide(group):
        current = len(nodes)
        lower = [min(item[0][a] for item in group) for a in range(3)]
        upper = [max(item[1][a] for item in group) for a in range(3)]
        nodes.append((lower, upper, group[0][2]))
        if len(group) > 1:
            axis = max(range(3), key=lambda a: upper[a] - lower[a])
            ordered = sorted(group, key=lambda item: (item[0][axis], item[2]))
            split = len(group) // 2
            subdivide(ordered[:split])
            subdivide(ordered[split:])
            nodes[current] = (lower, upper, -(len(nodes) - current))

    if items:
        subdivide(items)
        nodes.append(([0, 0, 0], [0, 0, 0], 0))
    return b"".join(struct.pack("<6Hi", *lower, *upper, index) for lower, upper, index in nodes)


def encode_tile(triangles, tx, ty, navigation, layer=0, links=None):
    """Write the vanilla triangle variant of Detour, including device/entrance links."""
    links = links or []
    vertices, indices, lookup = [], [], {}
    for triangle in triangles:
        # Detour expects clockwise X/Z polygons when viewed in its X/Y/Z axes.
        triangle = list(triangle)
        if Polygon([p[:2] for p in triangle]).exterior.is_ccw:
            triangle.reverse()
        face = []
        for point in triangle:
            key = vertex_key(point)
            if key not in lookup:
                lookup[key] = len(vertices)
                vertices.append(point)
            face.append(lookup[key])
        indices.append(face)
    count = len(indices)
    if count >= 32768 or len(vertices) >= 65535:
        raise ValueError("Native navigation tile exceeds triangle/index limits")
    bounds_min = [tx * TILE_SIZE, min(p[2] for p in vertices) - 1, ty * TILE_SIZE]
    bounds_max = [(tx + 1) * TILE_SIZE, max(p[2] for p in vertices) + navigation["height"], (ty + 1) * TILE_SIZE]
    edges = defaultdict(list)
    for i, face in enumerate(indices):
        for slot in range(3):
            edges[tuple(sorted((face[slot], face[(slot + 1) % 3])))].append((i, slot))
    neighbors = [[0] * 3 for _ in indices]
    portals = 0
    for edge, owners in edges.items():
        if len(owners) > 2:
            raise ValueError("Non-manifold navigation edge")
        if len(owners) == 2:
            (a, sa), (b, sb) = owners
            neighbors[a][sa], neighbors[b][sb] = b + 1, a + 1
        else:
            i, slot = owners[0]
            a, b = [vertices[v] for v in edge]
            for axis, boundary, side in ((0, bounds_min[0], 4), (0, bounds_max[0], 0), (1, bounds_min[2], 6), (1, bounds_max[2], 2)):
                if abs(a[axis] - boundary) < 1e-5 and abs(b[axis] - boundary) < 1e-5:
                    neighbors[i][slot] = 0x8000 | side
                    portals += 1
                    break
    link_capacity = count * 3 + portals * 2 + len(links) * 4
    offmesh_indices = []
    for link in links:
        face = []
        for point in link["world_endpoints"]:
            face.append(len(vertices))
            vertices.append(point)
        offmesh_indices.append(face)
    # Version 8, layer, userId, poly/vertex/link/detail counts, BV count, offmesh.
    header = struct.pack("<4s14I", b"VAND", 8, tx & 0xffffffff, ty & 0xffffffff, layer, 0,
                         count + len(links), len(vertices), link_capacity, count, 0, count, count * 2, len(links), count)
    raw = bytearray(header + struct.pack("<10f", navigation["height"], navigation["radius"], navigation["climb"], *bounds_min, *bounds_max, 10))
    raw.extend(b"".join(struct.pack("<3f", p[0], p[2], p[1]) for p in vertices))
    for face, adjacent in zip(indices, neighbors):
        raw.extend(struct.pack("<I3H3HHBB", 0, *face, *adjacent, 3, 3, 1))
    for face, link in zip(offmesh_indices, links):
        raw.extend(struct.pack("<I3H3HHBB", 0, face[0], face[1], 0, 0, 0, 0, 3 if link["enabled"] else 0, 2, 64 | link.get("area", 10)))
    raw.extend(bytes(link_capacity * 16))  # Runtime fills link slots on load.
    raw.extend(b"".join(struct.pack("<IIBB2x", 0, i, 0, 1) for i in range(count)))
    raw.extend(bytes([0, 1, 2, 21]) * count)
    # Vanilla includes this index. Generic Detour permits a linear fallback,
    # but the game's off-mesh attachment path has not been shown to support it.
    raw.extend(_bv_tree(vertices, indices, bounds_min))
    for index, link in enumerate(links):
        a, b = link["world_endpoints"]
        dx = -1 if b[0] < bounds_min[0] else (1 if b[0] >= bounds_max[0] else 0)
        dy = -1 if b[1] < bounds_min[2] else (1 if b[1] >= bounds_max[2] else 0)
        side = {(0, 0): 255, (1, 0): 0, (1, 1): 1, (0, 1): 2, (-1, 1): 3,
                (-1, 0): 4, (-1, -1): 5, (0, -1): 6, (1, -1): 7}[dx, dy]
        raw.extend(struct.pack("<7fHBBQ", a[0], a[2], a[1], b[0], b[2], b[1], link["radius"], count + index, 1, side, int(link["id"])))
    return bytes(raw)


def navigation_resource(scene):
    navigation = scene["navigation"]
    groups = _tile_triangles(navigation["world_triangles"])
    buffers, metadata = [], []
    layer = scene["layout"].get("navigation", {}).get("layer", 0)
    if isinstance(layer, bool) or not isinstance(layer, int) or not 0 <= layer <= 255:
        raise ValueError("Navigation tile layer must be an integer from 0 to 255")
    for index, ((tx, ty), triangles) in enumerate(sorted(groups.items())):
        links = [link for link in navigation["links"] if (math.floor(link["world_endpoints"][0][0] / TILE_SIZE), math.floor(link["world_endpoints"][0][1] / TILE_SIZE)) == (tx, ty)]
        raw = encode_tile(triangles, tx, ty, navigation, layer, links)
        buffers.append({"BufferId": str(index), "Flags": 0, "Bytes": base64.b64encode(raw).decode("ascii")})
        metadata.append({"$type": "worldNavigationTileData", "tileX": tx, "tileY": ty, "tileIndex": index,
                         "bufferIndex": index, "agentSize": "Human", "tileRef": "9223372036854775807"})
        if links:
            metadata[-1]["offMeshConnections"] = {"$type": "worldOffMeshConnectionsData",
                "verts": [component for link in links for point in link["world_endpoints"] for component in (point[0], point[2], point[1])],
                "radii": [link["radius"] for link in links], "flags": [3 if link["enabled"] else 0 for link in links], "areas": [link.get("area", 10) for link in links],
                "directions": [1] * len(links), "ids": [link["id"] for link in links], "tagIntervals": [0] * (len(links) * 2),
                "globalNodeIDs": [{"$type": "worldGlobalNodeID", "hash": link["id"]} for link in links],
                "tagsX": [], "userData": [{"HandleId": str(index * 1001 + i + 1), "Data": {"$type": "worldOffMeshUserData"}} for i in range(len(links))]}
    points = [point for triangle in navigation["world_triangles"] for point in triangle]
    origin = scene["layout"]["origin"]
    def vector(values):
        return {"$type": "Vector4", **dict(zip(("X", "Y", "Z"), values)), "W": 0}
    if groups:
        global_min = [min(tx for tx, _ in groups) * TILE_SIZE, min(ty for _, ty in groups) * TILE_SIZE, min(p[2] for p in points) - 1]
        global_max = [(max(tx for tx, _ in groups) + 1) * TILE_SIZE, (max(ty for _, ty in groups) + 1) * TILE_SIZE, max(p[2] for p in points) + navigation["height"]]
        local_min = [global_min[i] - origin[axis] for i, axis in enumerate(("x", "y", "z"))]
        local_max = [global_max[i] - origin[axis] for i, axis in enumerate(("x", "y", "z"))]
    else:
        local_min = local_max = [0, 0, 0]
    return {"$type": "worldNavigationTileResource", "cookingPlatform": "PLATFORM_PC", "agentSize": "Human",
            "localBoundingBox": {"$type": "Box", "Min": vector(local_min), "Max": vector(local_max)},
            "tilesData": metadata, "tileBuffers": buffers}
