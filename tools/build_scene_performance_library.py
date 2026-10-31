"""Freeze reviewed vanilla event slices and their cinematic animation bindings."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


OUT = Path("quests/templates/performances")
SELECTIONS = [
    ("seated_sad_reply", "mq010", "mq010_02_barry_talk", 68,
     [221, 227, 228, 229, 230, 233, 238], {"speaker": 0, "listener": 1}, {},
     "Seated, both hands on lap; source male_big body/facial graph. Body gestures, gaze and expression transitions; head gesture clips excluded."),
    ("seated_explanation", "mq010", "mq010_02_barry_talk", 72,
     [246, 252, 256, 261], {"speaker": 0, "listener": 1}, {},
     "Seated, both hands on lap; source male_big. Two explanatory gestures plus gaze and facial idle; source dialogue and head clips excluded."),
    ("arrive_and_sit", "mq010", "mq010_02_barry_talk", 484,
     [580, 586, 587, 588, 589, 590, 591], {"speaker": 0, "listener": 1}, {"settled": 591},
     "Walking approach into a chair; source male_big. Requires reviewed chair placement and explicit root-motion origin/offset; includes source arm/spine corrections."),
    ("stand_from_chair", "mq010", "mq010_02_barry_talk", 768,
     [816, 822, 823, 824, 825], {"speaker": 0, "listener": 1}, {"idle_only": 822, "standing": 825},
     "Seated, both hands on lap; source male_big. Requires explicit root-motion placement and a consumer for idle-only/standing signals; idle-only is not StopWorkspot."),
    ("group_side_exchange", "mq003", "mq003_01_homeless", 6,
     [4, 8, 10, 13], {"smoker": 1, "table_listener": 2}, {},
     "Two NPCs: wall lean with right-hand cigarette and two-hands-on-table lean. Furniture, cigarette and source body rigs must already be compatible. Static world-gaze event excluded."),
]


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def expand(value, handles, active=()):
    """Make donor handle dependencies self-contained, without opaque payloads."""
    if isinstance(value, list):
        return [expand(v, handles, active) for v in value]
    if not isinstance(value, dict):
        return value
    if "$rawTail" in value:
        raise ValueError("Opaque donor payload is not a reviewed event shape")
    if "HandleRefId" in value:
        handle = str(value["HandleRefId"])
        if handle == "0":
            return copy.deepcopy(value)
        if handle in active:
            raise ValueError("Cyclic donor handle")
        return expand(handles[handle], handles, (*active, handle))
    return {k: expand(v, handles, active) for k, v in value.items()}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = {"schema_version": 1, "status": "experimental; source-derived, not runtime accepted", "blocks": {}}
    for key, family, stem, nid, wanted, roles, ports, requirements in SELECTIONS:
        path = Path("reference/vanilla_extract_json") / family / (stem + ".scene.json")
        raw = path.read_bytes()
        doc = json.loads(raw)
        root = doc["Data"]["RootChunk"]
        handles = {str(v["HandleId"]): v for v in walk(doc) if "HandleId" in v}
        index, section = next((i, n["Data"]) for i, n in enumerate(root["sceneGraph"]["Data"]["graph"])
                              if n["Data"]["nodeId"]["id"] == nid)
        events, pointers = [], []
        for i, event in enumerate(section["events"]):
            if int(event.get("HandleId", -1)) in wanted:
                events.append(expand(event, handles))
                pointers.append(f"/Data/RootChunk/sceneGraph/Data/graph/{index}/Data/events/{i}")
        assert len(events) == len(wanted)
        actors = {a["actorId"]["id"]: a for a in root["actors"] + root["playerActors"]}
        bindings = []
        refs = root["resouresReferences"]
        for role, aid in roles.items():
            names = {v["$value"] for event in events
                     if event["Data"].get("performer", {}).get("id") == aid * 256 + 1
                     for v in walk(event["Data"].get("animName", {})) if v.get("$type") == "CName" and v.get("$value") != "None"}
            resolved = set()
            for field in ("bodyCinematicAnimSets", "facialCinematicAnimSets"):
                for grant in actors[aid].get(field, []):
                    i = grant["id"]
                    available = {n["$value"] for n in refs["cinematicAnimNames"][i]["animationNames"]}
                    used = names & available
                    if used:
                        bindings.append({"role": role, "actor_field": field, "source_index": i,
                            "reference": refs["cinematicAnimSets"][i],
                            "names": {"$type": "scnAnimSetAnimNames", "animationNames": [n for n in refs["cinematicAnimNames"][i]["animationNames"] if n["$value"] in used]}})
                        resolved.update(used)
            assert names == resolved, (key, role, names - resolved)
        by_handle = {str(e["HandleId"]): e["Data"] for e in events}
        recipe = {"schema_version": 1, "key": key, "requirements": requirements,
            "source": {"path": path.as_posix(), "sha256": hashlib.sha256(raw).hexdigest(),
                "section": nid, "event_pointers": pointers,
                "section_pointer": f"/Data/RootChunk/sceneGraph/Data/graph/{index}"},
            "roles": roles,
            "role_kinds": {role: "player" if any(a["actorId"]["id"] == aid for a in root["playerActors"]) else "npc" for role, aid in roles.items()},
            "duration_ms": section["sectionDuration"]["stu"],
            "events": events, "animation_bindings": bindings,
            "ports": {name: by_handle[str(handle)]["osockStamp"] for name, handle in ports.items()}}
        context_ids = {"arrive_and_sit": {58, 485}, "stand_from_chair": {1011, 1012}}.get(key, set())
        recipe["source_context"] = [{"pointer": f"/Data/RootChunk/sceneGraph/Data/graph/{i}",
            "node": expand(n, handles)} for i, n in enumerate(root["sceneGraph"]["Data"]["graph"])
            if n["Data"]["nodeId"]["id"] in context_ids]
        target = OUT / (key + ".json")
        target.write_text(json.dumps(recipe, indent=2) + "\n", encoding="utf-8")
        catalog["blocks"][key] = {"path": target.as_posix(), "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "requirements": requirements, "source": recipe["source"], "events": len(events)}
    (OUT / "catalog.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(f"Frozen {len(catalog['blocks'])} performance blocks")


if __name__ == "__main__":
    main()
