#!/usr/bin/env python3
"""Plan and render rig-matched workspot clip evidence before VLM captioning."""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
import hashlib
import html
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess

from artifact_io import atomic_write_json
from import_braindance_rig_contract import build_contract
from sex_rid_preview import decode_compressed_buffer, decode_simd_buffer, _model_positions
from toolchain import default_tool_path
from workspot_catalog import ROOT, DEFAULT_OUTPUT, read, scalar, depot, walk, digest

VERSION = 1
BODY_FIELDS = ("idleAnim", "animName", "turnAnimName")
PILOT = (
    r"base\workspots\quest\main_quests\prologue\q000\q000_corpo_04_lizzies_club\corpo__stand_lean_front_hands_on_knees__01.workspot",
    r"base\cinematics\workspots\male\ma_stand__phone__talk.workspot",
    r"base\workspots\common\ground\generic__stand_ground__wait__01.workspot",
    r"base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot",
)


def handle_resolver(document):
    handles = {str(n["HandleId"]): n["Data"] for _, n in walk(document) if "HandleId" in n and isinstance(n.get("Data"), dict)}

    def resolve(node):
        if not isinstance(node, dict):
            return {}
        if "HandleRefId" in node:
            return handles[str(node["HandleRefId"])]
        return node.get("Data", node)
    return resolve


def raw_path(root, resource):
    parts = depot(resource).split("\\")
    if any(p in ("", ".", "..") or ":" in p for p in parts):
        raise ValueError(f"Invalid depot path: {resource}")
    return root.joinpath(*parts).with_suffix(Path(parts[-1]).suffix + ".json")


def registrations(document, rig):
    resolve = handle_resolver(document)
    tree = resolve(document["Data"]["RootChunk"]["workspotTree"])
    candidates = []
    for group in tree.get("finalAnimsets", []):
        name = scalar(group.get("rig", {}).get("DepotPath"))
        if depot(name) != depot(rig):
            continue
        for channel in ("cinematics", "gameplay"):
            for entry in group.get("animations", {}).get(channel, []):
                resource = scalar(entry.get("animSet", {}).get("DepotPath"))
                if resource and resource != "0":
                    candidates.append((int(entry.get("priority", 128)), depot(resource)))
    # Highest explicit priority first; stable registration order breaks ties.
    return list(dict.fromkeys(name for _, name in sorted(candidates, key=lambda x: -x[0])))


def make_plan(catalog, raw_root, selected, *, all_workspots=False, max_clips=6):
    jobs, skipped = {}, []
    wanted = set(map(depot, selected or PILOT))
    records = [r for r in catalog["workspots"] if all_workspots or r["depot_path"] in wanted]
    if not all_workspots and wanted - {r["depot_path"] for r in records}:
        raise ValueError(f"Unknown workspots: {sorted(wanted - {r['depot_path'] for r in records})}")
    for record in records:
        human = [r for r in record["rigs"] if r in (
            r"base\characters\base_entities\man_base\man_base.rig",
            r"base\characters\base_entities\woman_base\woman_base.rig")]
        if not human:
            skipped.append({"workspot": record["depot_path"], "reason": "No supported base human rig registration"})
            continue
        rig = human[0]
        source = raw_path(raw_root, record["depot_path"])
        sets = registrations(read(source), rig)
        if not sets:
            skipped.append({"workspot": record["depot_path"], "reason": "No explicit rig-matched animation sets"})
            continue
        groups = defaultdict(list)
        for entry in record["entries"]:
            for field in BODY_FIELDS:
                name = scalar(entry["settings"].get(field))
                if not name or name in ("None", "0", "<no_auto_transition>"):
                    continue
                role = "idle" if field == "idleAnim" else "entry" if entry["type"] in ("workEntryAnim", "workSyncMasterEntryAnim") else "exit" if entry["type"] in ("workExitAnim", "workFastExit") else "clip"
                groups[role].append((name, entry["id"], field, entry["type"]))
        # Include one of each lifecycle role before taking extra variations.
        choices = []
        for role in ("idle", "clip", "entry", "exit"):
            if groups[role]:
                choices.append((role, groups[role].pop(0)))
        choices += [(role, item) for role, items in groups.items() for item in items]
        unique = {}
        for role, (name, entry_id, field, entry_type) in choices:
            unique.setdefault(name, {"role": role, "entry_id": entry_id, "field": field, "entry_type": entry_type})
        for name, usage in list(unique.items())[:max_clips or None]:
            identity = json.dumps([rig, sets, name], separators=(",", ":"))
            key = hashlib.sha256(identity.encode()).hexdigest()[:20]
            job = jobs.setdefault(key, {"id": key, "rig": rig, "animsets": sets, "animation_name": name, "uses": []})
            job["uses"].append({"workspot": record["depot_path"], "workspot_sha256": record["source"]["binary_sha256"] or record["source"]["raw_sha256"], **usage})
    return {"schema_version": VERSION, "scope": "Individual body clips; not workspot-tree simulation", "jobs": list(jobs.values()), "skipped": skipped, "selected_workspots": len(records)}


def prepare(plan, assets, game, wolvenkit, force=False):
    names = sorted({name for job in plan["jobs"] for name in [job["rig"], *job["animsets"]]})
    needed = [name for name in names if force or not raw_path(assets / "raw", name).is_file()]
    if not needed:
        return {"dependencies": len(names), "prepared": 0}
    binary = assets / "binary"
    raw = assets / "raw"
    binary.mkdir(parents=True, exist_ok=True)
    raw.mkdir(parents=True, exist_ok=True)
    directories = [p for p in (game / "archive/pc/content", game / "archive/pc/ep1") if p.is_dir()]
    if not directories:
        raise ValueError(f"No vanilla game archives under {game}")
    # Keep Windows command lines below the command-line length limit.
    for start in range(0, len(needed), 40):
        pattern = "(?i)^(?:" + "|".join(re.escape(n) for n in needed[start:start + 40]) + ")$"
        result = subprocess.run([str(wolvenkit), "unbundle", *map(str, directories), "-o", str(binary), "-r", pattern, "-v", "Minimal"], capture_output=True, text=True, check=True)
        (assets / f"extract-{start}.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    # Animation headers and rig parent arrays are opaque to the native reader.
    # WolvenKit is the documented fallback; its TempBuffer resolves shared chunks.
    # Omitting -o preserves the depot hierarchy; -o flattens basenames.
    result = subprocess.run([str(wolvenkit), "convert", "serialize", str(binary), "-v", "Minimal"], capture_output=True, text=True, check=True)
    (assets / "serialize.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    for name in names:
        source = raw_path(binary, name)
        if source.is_file():
            target = raw_path(raw, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    missing = [n for n in names if not raw_path(raw, n).is_file()]
    atomic_write_json(assets / "prepare.json", {"dependencies": names, "missing": missing, "wolvenkit_sha256": digest(wolvenkit)})
    if missing:
        raise ValueError(f"Missing prepared dependencies: {missing}")
    return {"dependencies": len(names), "prepared": len(needed)}


def prepare_skin(output, game, wolvenkit):
    folder = output / "skinned-assets"
    binary, exports = folder / "vanilla", folder / "export"
    manifest_path = folder / "skin.json"
    if manifest_path.is_file():
        previous = read(manifest_path)
        if all(Path(path).is_file() and digest(Path(path)) == sha for path, sha in previous["files"].items()):
            return manifest_path
    names = [r"base\characters\common\base_bodies\man_average\t0_000_ma_base__full.mesh", r"base\characters\head\ma\h0_000_ma_c__basehead\h0_000_ma_c__basehead.mesh", r"base\characters\base_entities\man_base\deformations_rigs\man_base_deformations.rig"]
    binary.mkdir(parents=True, exist_ok=True)
    exports.mkdir(parents=True, exist_ok=True)
    pattern = "(?i)^(?:" + "|".join(re.escape(n) for n in names) + ")$"
    with (folder / "prepare-skin.log").open("w", encoding="utf-8") as log:
        subprocess.run([str(wolvenkit), "unbundle", str(game / "archive/pc/content"), "-o", str(binary), "-r", pattern, "-v", "Minimal"], check=True, stdout=log, stderr=subprocess.STDOUT)
        rig = binary / names[-1].replace("\\", "/")
        subprocess.run([str(wolvenkit), "convert", "serialize", str(rig), "-v", "Minimal"], check=True, stdout=log, stderr=subprocess.STDOUT)
        meshes = [binary / name.replace("\\", "/") for name in names[:2]]
        subprocess.run([str(wolvenkit), "export", *map(str, meshes), "-o", str(exports), "-v", "Minimal"], env={**os.environ, "MeshExportArgs__withMaterials": "false"}, check=True, stdout=log, stderr=subprocess.STDOUT)
    raw_rig = raw_path(binary, names[-1])
    contract = folder / "deformation.skeleton.json"
    atomic_write_json(contract, build_contract(read(raw_rig), digest(raw_rig)))
    glbs = [exports / (Path(name.replace("\\", "/")).stem + ".glb") for name in names[:2]]
    manifest = {"schema_version": 1, "rig": r"base\characters\base_entities\man_base\man_base.rig", "deform_contract": str(contract), "meshes": [{"path": str(p), "rigid_head": index == 1} for index, p in enumerate(glbs)], "depot_resources": names, "files": {str(p): digest(p) for p in [contract, raw_rig, *glbs, *meshes, rig]}, "limitations": ["Neutral head follows Head rigidly; no facial animation", "Deformation helper bones follow authored rest hierarchy; engine muscle/IK solvers omitted"]}
    atomic_write_json(manifest_path, manifest)
    return manifest_path


def animation_buffer(root, animation, resolve):
    buffer = dict(resolve(animation["animBuffer"]))
    if "$rawData" in buffer:
        raise ValueError("Opaque animation header; prepare with WolvenKit")
    if not (buffer.get("defferedBuffer") or buffer.get("inplaceCompressedBuffer")):
        if buffer.get("tempBuffer"):
            buffer["defferedBuffer"] = buffer["tempBuffer"]
        else:
            address = buffer.get("dataAddress", {})
            index = int(address.get("unkIndex", -1))
            offset = int(address.get("fsetInBytes", -1))
            length = int(address.get("zeInBytes", -1))
            chunks = root.get("animationDataChunks", [])
            if index < 0 or index >= len(chunks) or min(offset, length) < 0:
                raise ValueError("Invalid animation chunk address")
            raw = base64.b64decode(chunks[index]["buffer"]["Bytes"], validate=True)
            if offset + length > len(raw):
                raise ValueError("Animation chunk slice is out of bounds")
            buffer["defferedBuffer"] = {"Bytes": base64.b64encode(raw[offset:offset + length]).decode()}
    return buffer


def validate_joint_layout(buffer, skeleton):
    total = int(buffer["numJoints"])
    extra = int(buffer.get("numExtraJoints", 0))
    # WolvenKit's AnimationTools/AnimSpline use numJoints - numExtraJoints
    # for the rig hierarchy. Extra synchronization channels are not body bones.
    if extra < 0 or total - extra != skeleton["bone_count"]:
        raise ValueError(f"Rig/buffer joint mismatch: {skeleton['bone_count']} vs {total} ({extra} declared extra)")
    return {"body_joints": total - extra, "extra_joints_omitted": extra, "extra_data_names": [scalar(n) for n in buffer.get("extraDataNames", [])]}


def decode_job(job, assets, fps=12, seconds=8):
    rig_path = raw_path(assets / "raw", job["rig"])
    skeleton = build_contract(read(rig_path), digest(rig_path))
    selected = None
    # A set's registered priority is respected when the same name occurs twice.
    for name in job["animsets"]:
        path = raw_path(assets / "raw", name)
        document = read(path)
        root = document["Data"]["RootChunk"]
        declared = scalar(root.get("rig", {}).get("DepotPath"))
        if declared and depot(declared) != job["rig"]:
            continue
        resolve = handle_resolver(document)
        for entry in root.get("animations", []):
            animation = resolve(resolve(entry).get("animation"))
            if scalar(animation.get("name")) == job["animation_name"]:
                selected = (path, root, animation, resolve)
                break
        if selected:
            break
    if not selected:
        raise ValueError("Named animation absent from registered rig-specific sets")
    path, root, animation, resolve = selected
    if animation.get("animationType", "Normal") not in ("Normal", "NormalWithTrajectory"):
        raise ValueError(f"Additive animation needs a base pose: {animation.get('animationType')}")
    buffer = animation_buffer(root, animation, resolve)
    decoder = {"animAnimationBufferCompressed": decode_compressed_buffer, "animAnimationBufferSimd": decode_simd_buffer}.get(buffer.get("$type"))
    if decoder is None:
        raise ValueError(f"Unsupported buffer format {buffer.get('$type')}")
    joint_layout = validate_joint_layout(buffer, skeleton)
    decoded = decoder(buffer)
    poses = _model_positions(decoded, [b["parent"] for b in skeleton["bones"]], [0, 0, 0], [0, 0, 0, 1])
    duration = min(decoded.duration, seconds) if seconds else decoded.duration
    if duration <= 0 or not poses:
        raise ValueError("Animation has no positive-duration motion")
    times = [index / fps for index in range(max(2, math.ceil(duration * fps)))]
    sample_indices = [min(round(t / decoded.duration * (decoded.frame_count - 1)), decoded.frame_count - 1) for t in times]
    samples = [poses[index] for index in sample_indices]
    points = [p for frame in samples for p in frame]
    if not all(math.isfinite(x) for p in points for x in p):
        raise ValueError("Animation contains nonfinite coordinates")
    bounds = {"min": [min(p[i] for p in points) for i in range(3)], "max": [max(p[i] for p in points) for i in range(3)]}
    if max(bounds["max"][i] - bounds["min"][i] for i in range(3)) < 0.3:
        raise ValueError("Decoded body has implausibly small spatial extent")
    provenance = {"animset": str(path), "animset_sha256": digest(path), "rig_sha256": digest(rig_path), "buffer_type": buffer["$type"], "joint_layout": joint_layout, "source_duration_seconds": decoded.duration, "source_frames": decoded.frame_count, "preview_start_seconds": 0, "preview_end_seconds": min(duration, times[-1]), "sample_times_seconds": times, "bytes_consumed": decoded.bytes_consumed, "payload_bytes": decoded.payload_bytes}
    return {"schema_version": 1, "kind": "ghostline_workspot_clip_preview", "rid_id": job["id"], "fps": fps, "frame_count": len(samples), "duration_seconds": duration, "coordinate_system": "RED_Z_UP", "bounds": bounds, "skeleton_contract": skeleton, "actors": [{"signature": "body", "animation_name": job["animation_name"], "color": [0.16, 0.72, 0.82, 1], "bone_names": [b["name"] for b in skeleton["bones"]], "parents": [b["parent"] for b in skeleton["bones"]], "frames": samples, "local_translations": [decoded.translations[i][:skeleton['bone_count']] for i in sample_indices], "local_rotations": [decoded.rotations[i][:skeleton['bone_count']] for i in sample_indices], "local_scales": [decoded.scales[i][:skeleton['bone_count']] for i in sample_indices], "source_joint_count": skeleton["bone_count"], "approximate_contract": False}], "provenance": provenance, "limitations": ["Body proxy only; props, furniture, facial animation and synchronization partners omitted", "Approximate mannequin proportions; fingers and head rotation not depicted", "Individual clip excerpt; no tree execution, blending, or runtime validation"]}


def render_job(job, preview, output, blender, force=False):
    from PIL import Image, ImageDraw
    folder = output / job["id"]
    folder.mkdir(parents=True, exist_ok=True)
    receipt = folder / "render.json"
    identity = hashlib.sha256(json.dumps([VERSION, job, preview["provenance"], preview.get("skin_manifest"), digest(Path(__file__)), digest(ROOT / "tools/workspot_preview_blender.py"), digest(ROOT / "tools/workspot_skin.py"), digest(ROOT / "tools/sex_rid_preview_blender.py"), digest(ROOT / "tools/sex_rid_preview.py"), preview["fps"], digest(blender)], sort_keys=True).encode()).hexdigest()
    if not force and receipt.is_file():
        previous = read(receipt)
        if previous.get("identity") == identity and all((folder / name).is_file() and digest(folder / name) == sha for name, sha in previous.get("outputs", {}).items()) and len(previous.get("outputs", {})) == 2:
            return previous
    atomic_write_json(folder / "decoded.json", preview)
    frames = folder / "frames"
    frames.mkdir(exist_ok=True)
    command = [str(blender), "--background", "--python", str(ROOT / "tools/workspot_preview_blender.py"), "--", "--input", str(folder / "decoded.json"), "--video", str(folder / "preview.mp4"), "--frames-dir", str(frames)]
    with (folder / "blender.log").open("w", encoding="utf-8") as log:
        subprocess.run(command, check=True, stdout=log, stderr=subprocess.STDOUT)
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise ValueError("ffmpeg is required to encode previews")
    with (folder / "ffmpeg.log").open("w", encoding="utf-8") as log:
        subprocess.run([ffmpeg, "-y", "-framerate", str(preview["fps"]), "-start_number", "1", "-i", str(frames / "frame_%04d.png"), "-frames:v", str(preview["frame_count"]), "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", str(folder / "preview.mp4")], check=True, stdout=log, stderr=subprocess.STDOUT)
    sheet = Image.new("RGB", (960, 408), "#111820")
    draw = ImageDraw.Draw(sheet)
    for index in range(6):
        sample = round(index * (preview["frame_count"] - 1) / 5)
        with Image.open(frames / f"frame_{sample + 1:04d}.png") as image:
            sheet.paste(image.resize((320, 180)), ((index % 3) * 320, (index // 3) * 204))
        draw.text(((index % 3) * 320 + 8, (index // 3) * 204 + 183), f"t={preview['provenance']['sample_times_seconds'][sample]:.2f}s", fill="white")
    sheet.save(folder / "contact.png")
    result = {"identity": identity, "id": job["id"], "status": "rendered_proxy", "renderer": "skinned_source_mesh" if preview.get("skin_manifest") else "mannequin", "outputs": {n: digest(folder / n) for n in ("preview.mp4", "contact.png")}, "provenance": preview["provenance"], "limitations": preview["limitations"]}
    atomic_write_json(receipt, result)
    return result


def gallery(plan, results, output):
    output.mkdir(parents=True, exist_ok=True)
    page = ['<!doctype html><meta charset="utf-8"><title>Workspot render pilot</title><style>body{background:#111820;color:#e8edf4;font:16px system-ui;max-width:1100px;margin:32px auto}article{padding:24px 0;border-top:1px solid #415064}video,img{width:100%;max-width:960px}code{overflow-wrap:anywhere}p{color:#b5c2d3}</style><h1>Workspot body-clip previews</h1><p>Decoded source motion on an exact rig. Body proxies omit props, furniture, facial performance and synchronization partners. These are individual clip excerpts, not workspot-tree playback.</p>']
    jobs = {j["id"]: j for j in plan["jobs"]}
    caption_jobs = []
    for result in results:
        job = jobs[result["id"]]
        page.append(f'<article><h2>{html.escape(job["animation_name"])}</h2><code>{html.escape(job["uses"][0]["workspot"])}</code>')
        if result.get("status") == "rendered_proxy":
            key = job["id"]
            page.append(f'<p>Roles: {html.escape(", ".join(sorted({u["role"] for u in job["uses"]})))} · Source duration {result["provenance"]["source_duration_seconds"]:.2f}s · preview through {result["provenance"]["preview_end_seconds"]:.2f}s</p><video controls preload="none" src="{key}/preview.mp4"></video><details><summary>Contact sheet</summary><img src="{key}/contact.png"></details>')
            caption_jobs.append({"id": key, "video": f"{key}/preview.mp4", "contact_sheet": f"{key}/contact.png", "media_sha256": result["outputs"], "renderer": result.get("renderer", "mannequin"), "limitations": result["limitations"], "sample_times_seconds": result["provenance"]["sample_times_seconds"], "prompt": "Describe only visible body posture and motion in this neutral proxy animation, respecting the supplied renderer limitations. Furniture, props, facial performance and other actors are omitted: do not invent them or infer an interaction from a hand pose. Report uncertainty. Return JSON with posture, torso_motion, left_hand, right_hand, leg_motion, facing_change, displacement, action_description, visible_evidence, uncertainties. Do not claim a workspot loop, complete entry/exit, prop identity or runtime compatibility from this clip excerpt.", "review_status": "uncaptioned"})
        else:
            page.append(f'<p>Unavailable: {html.escape(result.get("error", "unknown failure"))}</p>')
        page.append('</article>')
    (output / "index.html").write_text("\n".join(page), encoding="utf-8")
    (output / "caption-jobs.jsonl").write_text("".join(json.dumps(j) + "\n" for j in caption_jobs), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--all", action="store_true")
    p.add_argument("--workspot", action="append", default=[])
    p.add_argument("--max-clips", type=int, default=6, help="Per workspot, 0 for all names")
    p = sub.add_parser("prepare")
    p.add_argument("--game-root", type=Path, default=default_tool_path("game"))
    p.add_argument("--wolvenkit", type=Path, default=default_tool_path("wolvenkit"))
    p.add_argument("--force", action="store_true")
    p = sub.add_parser("prepare-skin")
    p.add_argument("--game-root", type=Path, default=default_tool_path("game"))
    p.add_argument("--wolvenkit", type=Path, default=default_tool_path("wolvenkit"))
    p = sub.add_parser("render")
    p.add_argument("--blender", type=Path, default=default_tool_path("blender"))
    p.add_argument("--fps", type=int, default=12)
    p.add_argument("--seconds", type=float, default=8, help="Clip excerpt duration; 0 for full duration")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--force", action="store_true")
    p.add_argument("--skin-manifest", type=Path)
    args = parser.parse_args(argv)
    out = args.output.resolve()
    plan_file = out / "preview-plan.json"
    if args.command == "plan":
        if args.max_clips < 0:
            parser.error("--max-clips must be nonnegative")
        plan = make_plan(read(out / "catalog.json"), out / "raw", args.workspot, all_workspots=args.all, max_clips=args.max_clips)
        atomic_write_json(plan_file, plan)
        print(json.dumps({"jobs": len(plan["jobs"]), "skipped": len(plan["skipped"]), "workspots": plan["selected_workspots"]}))
    elif args.command == "prepare":
        print(json.dumps(prepare(read(plan_file), out / "preview-assets", args.game_root, args.wolvenkit, args.force)))
    elif args.command == "prepare-skin":
        print(prepare_skin(out, args.game_root, args.wolvenkit))
    else:
        if args.fps < 1 or args.seconds < 0 or args.limit < 0:
            parser.error("fps must be positive; seconds and limit must be nonnegative")
        plan = read(plan_file)
        results = []
        folder = out / "previews"
        for job in plan["jobs"][:args.limit or None]:
            try:
                preview = decode_job(job, out / "preview-assets", args.fps, args.seconds)
                if args.skin_manifest:
                    skin = read(args.skin_manifest)
                    if skin["rig"] != job["rig"]:
                        raise ValueError("Skin and animation rig differ; no automatic body retargeting")
                    if not all(Path(path).is_file() and digest(Path(path)) == sha for path, sha in skin["files"].items()):
                        raise ValueError("Skin assets changed; rebuild prepare-skin")
                    preview["skin_manifest"] = skin
                    preview["limitations"] = ["Source body meshes with neutral material; props, furniture and synchronization partners omitted", "Individual clip excerpt; no tree playback or runtime validation", *skin["limitations"]]
                result = render_job(job, preview, folder, args.blender, args.force)
            except (ValueError, KeyError, OSError, RuntimeError, subprocess.CalledProcessError) as error:
                result = {"id": job["id"], "status": "failed", "error": str(error)}
            results.append(result)
            atomic_write_json(folder / "results.json", results)
            gallery(plan, results, folder)
            print(json.dumps({"id": job["id"], "status": result["status"], "error": result.get("error")}), flush=True)
        return int(any(r["status"] == "failed" for r in results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
