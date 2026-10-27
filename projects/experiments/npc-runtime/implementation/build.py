"""Build the isolated fixed-line NPC presentation experiment; never installs it."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import wave
import uuid
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.setrecursionlimit(20000)

from ghostline_red import DEFAULT_RED_CLI, deserialize, ensure_schema, serialize
from runtime_utterance import export_utterance
from lipsync_compiler import read_json, write_json
from runtime_job_plan import build_runtime_plan, config_source

GRAPH_DEPOT = "base/animations/facial/_facial_graphs/pma_paperdoll_sermo.animgraph"
RIG_DEPOT = "base/characters/head/player_base_heads/player_man_average/h0_000_pma_c__basehead/h0_000_pma_c__basehead_skeleton.rig"
MOD_GRAPH = "mod/npc_runtime/animations/runtime_face.animgraph"
CET = PROJECT / "source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def cname(value):
    return {"$type": "CName", "$storage": "string", "$value": value}


def wkit_bools(value):
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, dict):
        return {key: wkit_bools(child) for key, child in value.items()}
    if isinstance(value, list):
        return [wkit_bools(child) for child in value]
    return value


def runtime_graph(document: dict, tracks: list[str]) -> tuple[dict, dict]:
    """Gate an override branch immediately before Sermo; preserve the native branch."""
    result = copy.deepcopy(document)
    nodes = list(walk(result["Data"]["RootChunk"]))
    sermos = [n for n in nodes if n.get("$type") == "animAnimNode_Sermo"]
    if len(sermos) != 1:
        raise ValueError("Expected one Sermo evaluator")
    next_id = max(int(n["HandleId"]) for n in nodes if "HandleId" in n) + 1

    def handle(node):
        nonlocal next_id
        value = {"HandleId": str(next_id), "Data": node}
        next_id += 1
        return value

    def float_input(name):
        return handle({"$type": "animAnimNode_FloatInput", "group": cname("GhostlineRuntime"), "name": cname(name)})

    original = sermos[0]["inputLink"]
    if "HandleId" not in original["node"]:
        raise ValueError("Expected a defined original Sermo input")
    chain = {"$type": "animPoseLink", "node": {"HandleRefId": original["node"]["HandleId"]}}
    mapping = {}
    for index, track in enumerate(tracks):
        name = f"ghostline_rt_{index:03d}"
        mapping[track] = name
        chain = {"$type": "animPoseLink", "node": handle({
            "$type": "animAnimNode_FloatTrackModifier",
            "floatTrack": {"$type": "animNamedTrackIndex", "name": cname(track)},
            "operationType": "Override",
            "inputFloatTrack": {"$type": "animNamedTrackIndex", "name": cname("None")},
            "poseInputNode": chain,
            "floatInputNode": {"$type": "animFloatLink", "node": float_input(name)},
        })}
    gate = "ghostline_rt_enabled"
    sermos[0]["inputLink"] = {"$type": "animPoseLink", "node": handle({
        "$type": "animAnimNode_Switch", "numInputs": 2, "blendTime": 0.0,
        "weightNode": {"$type": "animFloatLink", "node": float_input(gate)},
        "inputNodes": [original, chain],
    })}
    return result, {"schema_version": 1, "gate": gate, "inputs": mapping,
                    "record": "Character.GhostlineRuntimePatch", "component": "face_rig",
                    "graph": MOD_GRAPH, "runtime_tested": False}


def collect_references(game: Path, directory: Path):
    directory.mkdir(parents=True, exist_ok=True)
    jobs = [{"resource": GRAPH_DEPOT, "output": str(directory / "face.animgraph.json")},
            {"resource": RIG_DEPOT, "output": str(directory / "face.rig.json")}]
    write_json(directory / "jobs.json", {"jobs": jobs})
    report = directory / "report.json"
    subprocess.run([str(DEFAULT_RED_CLI), "cr2w-serialize-batch", str(directory / "jobs.json"),
                    "--schema", str(ensure_schema()), "--archives-root", str(game / "archive/pc"),
                    "--report", str(report), "--threads", "1"], check=True)
    if any(row.get("error") for row in read_json(report)):
        raise ValueError(f"Reference extraction failed: {report}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, default=Path("H:/Cyberpunk 2077"))
    parser.add_argument("--wolvenkit", type=Path, default=Path("H:/WolvenKit.Console-8.17.4/WolvenKit.CLI.exe"))
    parser.add_argument("--references", type=Path, help="Directory with face.animgraph.json and face.rig.json")
    parser.add_argument("--job-only", action="store_true", help="Regenerate the loose runtime job contract without rebuilding facial assets")
    args = parser.parse_args()
    job = build_runtime_plan(PROJECT / "implementation/jobs/data-theft.quest.json",
                             PROJECT / "implementation/jobs/data-theft.runtime.json")
    write_json(CET / "job-plan.json", job)
    (PROJECT / "source/resources/r6/scripts/GhostlineNPCRuntime/JobConfig.reds").write_text(config_source(job), encoding="utf-8")
    if args.job_only:
        print(json.dumps({"job": job["job_id"], "revision": job["revision"], "archive_rebuilt": False}))
        return
    references = args.references or PROJECT / "generated/references"
    if args.references is None:
        collect_references(args.game, references)
    spec = read_json(PROJECT / "implementation/utterances.json")
    model = read_json(ROOT / spec["model"])
    utterances = []
    for line in spec["lines"]:
        audio = ROOT / line["audio"]
        utterance = export_utterance(audio, read_json(ROOT / line["alignment"]), model,
                                    utterance_id=line["id"], npc_id=spec["npc_id"],
                                    audio_file=f"audio/{line['id']}.wav")
        write_json(CET / f"utterances/{line['id']}.json", utterance)
        destination = CET / utterance["audio"]["file"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(audio, destination)
        utterances.append(utterance)
    tracks = utterances[0]["curves"]["tracks"]
    if any(u["curves"]["tracks"] != tracks for u in utterances):
        raise ValueError("Both utterances must use the same facial contract")
    rig_tracks = {n["$value"] for n in read_json(references / "face.rig.json")["Data"]["RootChunk"]["trackNames"]}
    if set(tracks) - rig_tracks:
        raise ValueError(f"Curves absent from NPC rig: {sorted(set(tracks) - rig_tracks)}")
    graph, contract = runtime_graph(read_json(references / "face.animgraph.json"), tracks)
    graph_raw = PROJECT / "source/raw" / (MOD_GRAPH + ".json")
    graph_archive = PROJECT / "source/archive" / MOD_GRAPH
    graph["Header"]["ArchiveFileName"] = str(graph_archive)
    graph["Header"]["WolvenKitVersion"] = "8.17.4"
    # The native reader emits JSON booleans; WolvenKit's CBool converter uses 0/1.
    graph = wkit_bools(graph)
    write_json(graph_raw, graph)
    write_json(CET / "graph-contract.json", contract)
    graph_archive.parent.mkdir(parents=True, exist_ok=True)
    # New float-input links and array layouts require WolvenKit's complete writer.
    conversion = PROJECT / "generated/conversion" / uuid.uuid4().hex
    conversion.mkdir(parents=True)
    process = subprocess.run([str(args.wolvenkit), "cr2w", str(graph_raw), "--deserialize",
                              "--outpath", str(conversion)], capture_output=True, text=True)
    (conversion / "convert.log").write_text(process.stdout + process.stderr, encoding="utf-8")
    converted_graph = conversion / graph_archive.name
    if not converted_graph.is_file():
        raise RuntimeError(f"Graph conversion failed; see {conversion / 'convert.log'}")
    shutil.copyfile(converted_graph, graph_archive)
    donor = ROOT / "projects/shared/ghostline-runtime/source"
    for suffix in ["ent", "app"]:
        original_depot = f"mod/ghostline/characters/patch/patch.{suffix}"
        modified_depot = f"mod/npc_runtime/characters/runtime_patch.{suffix}"
        # Clone the currently packed baseline, not an authored JSON with newer layouts.
        donor_json = references / f"patch.{suffix}.json"
        serialize(donor / "archive" / original_depot, donor_json)
        document = read_json(donor_json)
        for node in walk(document):
            value = node.get("$value")
            if value == "mod\\ghostline\\characters\\patch\\patch.app":
                node["$value"] = "mod\\npc_runtime\\characters\\runtime_patch.app"
            if node.get("$type") == "entAnimatedComponent" and node.get("name", {}).get("$value") == "face_rig":
                node["graph"]["DepotPath"] = {"$type": "ResourcePath", "$storage": "string",
                                             "$value": MOD_GRAPH.replace("/", "\\")}
        raw = PROJECT / "source/raw" / (modified_depot + ".json")
        packed = PROJECT / "source/archive" / modified_depot
        document["Header"]["ArchiveFileName"] = str(packed)
        write_json(raw, document)
        deserialize(raw, packed, template=donor / "archive" / original_depot)
    slot = PROJECT / "source/resources/r6/audioware/GhostlineNPCRuntime/slot_0.wav"
    with wave.open(str(slot), "wb") as output:
        output.setparams((1, 2, 48000, 0, "NONE", "not compressed"))
        output.writeframes(b"\0\0" * 4800)
    serialized = PROJECT / "generated/graph-roundtrip.json"
    serialize(graph_archive, serialized)
    roundtrip = read_json(serialized)
    inputs = {n["name"]["$value"] for n in walk(roundtrip) if n.get("$type") == "animAnimNode_FloatInput"}
    if not {contract["gate"], *contract["inputs"].values()} <= inputs:
        raise ValueError("Serialized graph lost runtime inputs")
    evidence = {"schema_version": 1, "runtime_tested": False,
                "utterances": [{"id": u["utterance_id"], "audio": u["audio"]} for u in utterances],
                "tracks": len(tracks), "graph_sha256": hashlib.sha256(graph_archive.read_bytes()).hexdigest(),
                "reference_sha256": hashlib.sha256((references / "face.animgraph.json").read_bytes()).hexdigest()}
    write_json(PROJECT / "generated/build-report.json", evidence)
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
