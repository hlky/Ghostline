"""Lower reviewed performance blocks into a scene, preserving donor event shapes.

The library supplies choreography, not actor readiness, navigation meshes or
runtime compatibility. World placement and every timed output are explicit.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path

from build_scene_performance_library import walk

CATALOG = Path(__file__).resolve().parents[1] / "quests/templates/performances/catalog.json"
ACTOR_TABLES = {"bodyCinematicAnimSets", "facialCinematicAnimSets"}


def integer(value, label, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum}")
    return value


def recipe(key):
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    if key not in catalog["blocks"]:
        raise ValueError(f"Unknown performance preset: {key}")
    meta = catalog["blocks"][key]
    path = CATALOG.parent / Path(meta["path"]).name
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != meta["sha256"]:
        raise ValueError(f"Performance preset hash mismatch: {key}")
    return json.loads(data)


def expand_moves(spec):
    """Use native workspot lifecycle nodes; never disguise teleport as walking."""
    if not spec.get("performance_blocks"):
        return spec
    spec = copy.deepcopy(spec)
    keys = set()
    for block in spec["performance_blocks"]:
        key = block.get("key")
        if not isinstance(key, str) or not key or key in keys:
            raise ValueError("Performance block keys must be nonempty and unique")
        keys.add(key)
        kind = block.get("kind")
        if kind == "pose_beat":
            continue
        if kind not in {"workspot_move", "workspot_exit", "workspot_idle"}:
            raise ValueError(f"Unsupported performance block kind: {kind}")
        actor = next((a for a in spec["actors"] if a["key"] == block.get("actor")), None)
        if actor is None or actor["kind"] != "community":
            raise ValueError(f"{key}: workspot blocks require a community actor")
        required = ("node_id", "on_success") + (() if kind == "workspot_idle" else ("workspot_ref",))
        for field in required:
            if field not in block:
                raise ValueError(f"{key}: missing {field}")
        integer(block["node_id"], "workspot node_id")
        if kind != "workspot_idle" and (not isinstance(block["workspot_ref"], str) or not block["workspot_ref"].startswith("#")):
            raise ValueError(f"{key}: workspot_ref must be an explicit world NodeRef")
        if kind == "workspot_move":
            if "on_work_started" not in block or type(block.get("is_workspot_infinite")) is not bool:
                raise ValueError(f"{key}: declare on_work_started and is_workspot_infinite")
        elif kind == "workspot_exit" and "exit_entry_id" not in block:
            raise ValueError(f"{key}: workspot_exit requires exit_entry_id")
        node = {"key": key, "kind": "stop_workspot" if kind == "workspot_exit" else "use_workspot",
            "node_id": block["node_id"], "entity_ref": actor["community_ref"], "entry": actor["entry"],
            "workspot_ref": block.get("workspot_ref", 0), "teleport": False, "instant": False,
            "repeat_on_interrupt": False, "finish_animation": True,
            "movement_type": "Walk", "is_workspot_infinite": block.get("is_workspot_infinite", False),
            "on_success": block["on_success"], "on_work_started": block.get("on_work_started", [])}
        if kind == "workspot_idle":
            # mq010 node 1012 targets the actor's current activity, not a new spot.
            node.update(function="IdleOnlyMode", enable_idle_mode=True,
                        is_workspot_infinite=True, repeat_on_interrupt=True, teleport=True)
        allowed = {"key", "kind", "actor", *required, "on_work_started", "is_workspot_infinite",
                   "entry_id", "exit_entry_id", "exit_animation", "movement_type", "repeat_on_interrupt"}
        unknown = set(block) - allowed
        if unknown:
            raise ValueError(f"{key}: unsupported fields {sorted(unknown)}")
        for field in ("entry_id", "exit_entry_id"):
            if field in block:
                integer(block[field], field)
        for field in ("entry_id", "exit_entry_id", "exit_animation", "movement_type", "repeat_on_interrupt"):
            if field in block:
                node[field] = block[field]
        spec.setdefault("quest_nodes", []).append(node)
    return spec


def rehandle(value, alloc):
    """Each expanded donor subtree gets fresh scene-global handles."""
    if isinstance(value, list):
        return [rehandle(v, alloc) for v in value]
    if not isinstance(value, dict):
        return value
    if "HandleRefId" in value and str(value["HandleRefId"]) != "0":
        raise ValueError("Performance recipe contains an external handle")
    result = {k: rehandle(v, alloc) for k, v in value.items() if k != "HandleId"}
    if "HandleId" in value:
        result["HandleId"] = alloc.take()
    return result


def placement(value):
    if set(value) != {"origin", "offset"} or not isinstance(value["origin"], str) or not value["origin"].startswith("#"):
        raise ValueError("Root-motion placement requires origin NodeRef and full offset Transform")
    offset = value["offset"]
    if offset.get("$type") != "Transform":
        raise ValueError("Root-motion offset must be a Transform")
    for group, fields in (("position", ("X", "Y", "Z", "W")), ("orientation", ("i", "j", "k", "r"))):
        for field in fields:
            number = offset.get(group, {}).get(field)
            if type(number) not in (int, float) or not math.isfinite(number):
                raise ValueError(f"Root-motion offset missing finite {group}.{field}")
    norm = sum(offset["orientation"][k] ** 2 for k in ("i", "j", "k", "r"))
    if not math.isclose(norm, 1, abs_tol=0.002):
        raise ValueError("Root-motion orientation quaternion must be normalized")


def apply_blocks(root, spec, alloc, event_id, socket):
    actors = {a["key"]: a for a in spec["actors"]}
    actual = {a["actorId"]["id"]: a for a in root["actors"] + root["playerActors"]}
    sections = {s["key"]: s["node_id"] for s in spec.get("sections", [])}
    nodes = {n["Data"]["nodeId"]["id"]: n["Data"] for n in root["sceneGraph"]["Data"]["graph"]}
    refs = root["resouresReferences"]
    for block in spec.get("performance_blocks", []):
        if block["kind"] != "pose_beat":
            continue
        unknown = set(block) - {"key", "kind", "preset", "section", "actors", "start_ms", "anchor_line", "root_motion", "on", "ignore_ports"}
        if unknown:
            raise ValueError(f"{block['key']}: unsupported fields {sorted(unknown)}")
        donor = recipe(block["preset"])
        if block.get("section") not in sections:
            raise ValueError(f"{block['key']}: unknown target section")
        section = nodes[sections[block["section"]]]
        if set(block.get("actors", {})) != set(donor["roles"]):
            raise ValueError(f"{block['key']}: bind exactly the preset roles {sorted(donor['roles'])}")
        role_actors = {}
        for role, target in block["actors"].items():
            expected_player = donor["role_kinds"][role] == "player"
            if target not in actors or (actors[target]["kind"] == "player") != expected_player:
                raise ValueError(f"{block['key']}: role {role} requires its donor NPC/player kind")
            role_actors[role] = actors[target]
        if len({a["id"] for a in role_actors.values()}) != len(role_actors):
            raise ValueError("Different performance roles must bind different actors")
        performers = {source * 256 + 1: role_actors[role]["id"] * 256 + 1 for role, source in donor["roles"].items()}
        offset = integer(block.get("start_ms", 0), "start_ms")
        if "anchor_line" in block:
            key = block["anchor_line"]
            if key not in spec["spoken_line_order"]:
                raise ValueError(f"Unknown anchor line: {key}")
            line_id = 1 + spec["spoken_line_order"].index(key) * 256
            anchors = [e["Data"] for e in section["events"] if e["Data"].get("screenplayLineId", {}).get("id") == line_id]
            if len(anchors) != 1:
                raise ValueError("Anchor line must occur exactly once in the target section")
            offset += anchors[0]["startTime"]
        bound_ports = block.get("on", {})
        ignored = block.get("ignore_ports", [])
        if len(ignored) != len(set(ignored)) or set(bound_ports) & set(ignored) or set(bound_ports) | set(ignored) != set(donor["ports"]):
            raise ValueError(f"{block['key']}: bind or explicitly ignore every preset port")
        for name, destinations in bound_ports.items():
            if not isinstance(destinations, list) or not destinations:
                raise ValueError(f"{block['key']}: port {name} needs destinations; use ignore_ports to discard it")
            for dest in destinations:
                integer(dest.get("node_id"), "port destination node_id")
                integer(dest.get("input_name", 0), "port destination input_name")
                integer(dest.get("input_ordinal", 0), "port destination input_ordinal")
                target = nodes.get(dest.get("node_id"))
                if target is None:
                    raise ValueError(f"{block['key']}: missing port destination {dest.get('node_id')}")
                if target.get("$type") == "scnQuestNode" and dest.get("input_ordinal", 0) != 1:
                    raise ValueError("Performance port must enter a quest node's executable input")
        events = rehandle(donor["events"], alloc)
        root_roles = set()
        for index, wrapper in enumerate(events):
            event = wrapper["Data"]
            for value in walk(event):
                if value.get("$type") == "scnPerformerId" and value.get("id") not in (4294967040, 4294967295):
                    if value["id"] not in performers:
                        raise ValueError("Unbound donor performer")
                    value["id"] = performers[value["id"]]
                if value.get("$type") == "scnActorId" and value.get("id") != 4294967295:
                    role = next((r for r, aid in donor["roles"].items() if aid == value["id"]), None)
                    if role is None:
                        raise ValueError("Unbound donor actor ID")
                    value["id"] = role_actors[role]["id"]
            event["id"]["id"] = event_id(str(spec["name"]), block["key"], "performance", index)
            event["startTime"] = integer(event.get("startTime", 0), "donor startTime") + offset
            integer(event.get("duration", 0), "donor duration")
            for value in walk(event.get("scalingData")):
                if value.get("$type") == "scnSceneTime":
                    value["stu"] += offset
            motion = event.get("rootMotionData", {})
            if motion.get("enabled"):
                aid = (event["performer"]["id"] - 1) // 256
                role = next(r for r, a in role_actors.items() if a["id"] == aid)
                binding = block.get("root_motion", {}).get(role)
                if binding is None:
                    raise ValueError(f"{block['key']}: explicit root_motion placement required for {role}")
                placement(binding)
                motion["originMarker"]["nodeRef"] = {"$type": "NodeRef", "$storage": "string", "$value": binding["origin"]}
                motion["originOffset"] = copy.deepcopy(binding["offset"])
                root_roles.add(role)
            for value in walk(event):
                if value.get("$type") == "NodeRef" and str(value.get("$value")) != "0":
                    if value.get("$value") not in {p["origin"] for p in block.get("root_motion", {}).values()}:
                        raise ValueError("Unbound donor world NodeRef")
            if event["$type"] == "scneventsSocket":
                port = next(name for name, stamp in donor["ports"].items() if stamp == event["osockStamp"])
                if port in ignored:
                    continue
                stamps = {(s["stamp"]["name"], s["stamp"]["ordinal"]) for s in section["outputSockets"]}
                name = 2
                while (name, 0) in stamps:
                    name += 1
                event["osockStamp"] = {"$type": "scnOutputSocketStamp", "name": name, "ordinal": 0}
                section["outputSockets"].append(socket(name, 0, [(d["node_id"], d.get("input_name", 0), d.get("input_ordinal", 0)) for d in bound_ports[port]]))
            if event["$type"] == "scnPlaySkAnimEvent" and event.get("actorComponent", {}).get("$value") == "body":
                for existing in section["events"]:
                    other = existing["Data"]
                    if other.get("$type") == "scnPlaySkAnimEvent" and other.get("performer") == event.get("performer") and other.get("actorComponent") == event.get("actorComponent"):
                        if max(other.get("startTime", 0), event["startTime"]) < min(other.get("startTime", 0) + other.get("duration", 0), event["startTime"] + event.get("duration", 0)):
                            raise ValueError(f"{block['key']}: overlapping full-body performances")
            section["events"].append(wrapper)
        if set(block.get("root_motion", {})) != root_roles:
            raise ValueError("Unused root_motion placement bindings")
        section["sectionDuration"]["stu"] = max(section["sectionDuration"]["stu"], offset + donor["duration_ms"])
        for binding in donor["animation_bindings"]:
            pair = (binding["reference"], binding["names"])
            found = next((i for i, ref in enumerate(refs["cinematicAnimSets"]) if ref == pair[0]), None)
            if found is None:
                found = len(refs["cinematicAnimSets"])
                refs["cinematicAnimSets"].append(copy.deepcopy(pair[0]))
                refs["cinematicAnimNames"].append(copy.deepcopy(pair[1]))
            else:
                names = refs["cinematicAnimNames"][found]["animationNames"]
                for name in pair[1]["animationNames"]:
                    if name not in names:
                        names.append(copy.deepcopy(name))
            target = actual[role_actors[binding["role"]]["id"]]
            grant = {"$type": "scnCinematicAnimSetSRRefId", "id": found}
            if grant not in target[binding["actor_field"]]:
                target[binding["actor_field"]].append(grant)


def validate_blocks(root, spec):
    """Check emitted bindings independently of how a preset was lowered."""
    if not spec.get("performance_blocks"):
        return []
    errors = []
    actors = {a["actorId"]["id"]: a for a in root.get("actors", []) + root.get("playerActors", [])}
    performers = {aid * 256 + 1 for aid in actors}
    refs = root.get("resouresReferences", {})
    handles = [str(v["HandleId"]) for v in walk(root) if "HandleId" in v]
    if len(handles) != len(set(handles)):
        errors.append("Performance scene contains duplicate handle definitions")
    for value in walk(root):
        if value.get("$type") == "scnPerformerId" and value.get("id") not in performers | {4294967040, 4294967295}:
            errors.append(f"Unbound performance actor: {value.get('id')}")
    for wrapper in root.get("sceneGraph", {}).get("Data", {}).get("graph", []):
        node = wrapper["Data"]
        if node.get("$type") != "scnSectionNode":
            continue
        duration = node.get("sectionDuration", {}).get("stu", 0)
        stamps = [(s["stamp"]["name"], s["stamp"]["ordinal"]) for s in node["outputSockets"]]
        if len(stamps) != len(set(stamps)):
            errors.append("Duplicate performance section socket stamps")
        for event in node.get("events", []):
            data = event["Data"]
            start, length = data.get("startTime", 0), data.get("duration", 0)
            if type(start) is not int or type(length) is not int or start < 0 or length < 0 or start + length > duration:
                errors.append(f"Event exceeds performance section {node['nodeId']['id']} timeline")
            if data.get("$type") == "scneventsSocket":
                stamp = data.get("osockStamp", {})
                if (stamp.get("name"), stamp.get("ordinal")) not in stamps:
                    errors.append("Timed performance event has no matching output socket")
            if data.get("$type") != "scnPlaySkAnimEvent" or data.get("actorComponent", {}).get("$value") != "body":
                continue
            actor = actors.get((data.get("performer", {}).get("id", 0) - 1) // 256, {})
            available = set()
            for grant in actor.get("bodyCinematicAnimSets", []):
                index = grant.get("id", -1)
                if type(index) is int and 0 <= index < len(refs.get("cinematicAnimNames", [])):
                    available.update(n.get("$value") for n in refs["cinematicAnimNames"][index].get("animationNames", []))
            names = {v["$value"] for v in walk(data.get("animName", {})) if v.get("$type") == "CName" and v.get("$value") != "None"}
            if not names or not names <= available:
                errors.append("Body performance animation lacks its actor's cinematic resource/name binding")
    return errors
