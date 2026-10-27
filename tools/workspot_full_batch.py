#!/usr/bin/env python3
"""Resume full base-human workspot rendering, deduplicated by resolved source motion."""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

from artifact_io import atomic_write_json
from toolchain import default_tool_path
from workspot_catalog import DEFAULT_OUTPUT, ROOT, depot, digest, read, scalar
from workspot_preview import decode_job, handle_resolver, make_plan, raw_path, render_job
from workspot_preview_batch import caption_jobs, prepare_missing


def now():
    return datetime.now(timezone.utc).isoformat()


def prepare_female_skin(out, game, wolvenkit):
    """Export the matching NPC female source body, head and deformation contract."""
    import re
    import numpy as np
    from import_braindance_rig_contract import build_contract
    from workspot_skin import load_parts, skin_vertices

    folder = out / "skinned-assets-female"
    target = folder / "skin.json"
    if target.is_file():
        saved = read(target)
        if all(Path(p).is_file() and digest(Path(p)) == h for p, h in saved["files"].items()):
            return target
    names = [r"base\characters\common\base_bodies\woman_average\t0_000_wa_base__full.mesh",
             r"base\characters\head\wa\h0_000_wa_c__basehead\h0_000_wa__basehead.mesh",
             r"base\characters\base_entities\woman_base\deformations_rigs\woman_base_deformations.rig"]
    binary, export = folder / "vanilla", folder / "export"
    binary.mkdir(parents=True, exist_ok=True)
    export.mkdir(parents=True, exist_ok=True)
    sources = [binary / n.replace("\\", "/") for n in names]
    pattern = "(?i)^(?:" + "|".join(re.escape(n) for n in names) + ")$"
    with (folder / "prepare-skin.log").open("w") as log:
        subprocess.run([str(wolvenkit), "unbundle", str(game / "archive/pc/content"), "-o", str(binary), "-r", pattern, "-v", "Minimal"], check=True, stdout=log, stderr=subprocess.STDOUT)
        subprocess.run([str(wolvenkit), "convert", "serialize", str(sources[-1]), "-v", "Minimal"], check=True, stdout=log, stderr=subprocess.STDOUT)
        subprocess.run([str(wolvenkit), "export", *map(str, sources[:2]), "-o", str(export), "-v", "Minimal"], check=True, stdout=log, stderr=subprocess.STDOUT,
                       env={**os.environ, "MeshExportArgs__withMaterials": "false"})
    raw = raw_path(binary, names[-1])
    contract = folder / "deformation.skeleton.json"
    data = build_contract(read(raw), digest(raw))
    atomic_write_json(contract, data)
    glbs = [export / (p.stem + ".glb") for p in sources[:2]]
    deltas = {b["name"]: np.eye(4) for b in data["bones"]}
    for i, path in enumerate(glbs):
        for part in load_parts(path, rigid_head=i == 1):
            if not np.allclose(skin_vertices(part, deltas, np.eye(4)), part["vertices"]):
                raise ValueError("Female skin rest-pose validation failed")
    manifest = {"schema_version": 1, "rig": r"base\characters\base_entities\woman_base\woman_base.rig",
                "deform_contract": str(contract), "meshes": [{"path": str(p), "rigid_head": i == 1} for i, p in enumerate(glbs)],
                "depot_resources": names, "files": {str(p): digest(p) for p in [contract, raw, *glbs, *sources]},
                "limitations": ["Neutral head follows Head rigidly; no facial animation",
                                "Deformation helper bones follow authored rest hierarchy; engine muscle/IK solvers omitted"]}
    atomic_write_json(target, manifest)
    return target


def source_index(plan, assets, progress=None):
    """Inspect each serialized set once; preserve exact registration priority later."""
    index = {}
    names = sorted({name for job in plan["jobs"] for name in job["animsets"]})
    for number, name in enumerate(names, 1):
        path = raw_path(assets / "raw", name)
        try:
            document = read(path)
            root = document["Data"]["RootChunk"]
            resolve = handle_resolver(document)
            animations = {}
            for entry in root.get("animations", []):
                animation = resolve(resolve(entry).get("animation"))
                key = scalar(animation.get("name"))
                animations.setdefault(key, {"type": animation.get("animationType", "Normal")})
            index[name] = {"sha256": digest(path), "rig": depot(scalar(root.get("rig", {}).get("DepotPath"))) if root.get("rig") else None,
                           "animations": animations}
        except (OSError, ValueError, KeyError, TypeError) as error:
            index[name] = {"error": str(error)}
        if progress:
            progress(number, len(names))
    return index


def canonical_plan(plan, index, previous):
    """Only identical resolved rig/set bytes/name share a render, never name alone."""
    preferred = {j["id"]: i for i, j in enumerate(previous["jobs"])}
    groups, failures = {}, []
    for job in sorted(plan["jobs"], key=lambda j: preferred.get(j["id"], len(preferred))):
        selected = None
        for name in job["animsets"]:
            item = index.get(name, {})
            if item.get("error") or item.get("rig") not in (None, "none", "0", job["rig"]):
                continue
            if job["animation_name"] in item.get("animations", {}):
                selected = name
                break
        if selected is None:
            failures.append({"id": job["id"], "animation_name": job["animation_name"], "uses": job["uses"],
                             "reason": "Named motion unavailable in prepared rig-specific registrations"})
            continue
        key = (job["rig"], index[selected]["sha256"], job["animation_name"])
        if key not in groups:
            groups[key] = {**job, "uses": [], "resolved_animset": selected, "aliases": []}
        target = groups[key]
        target["aliases"].append(job["id"])
        target["uses"].extend(u for u in job["uses"] if u not in target["uses"])
    return {**plan, "jobs": list(groups.values()), "unresolved": failures,
            "registered_jobs": len(plan["jobs"]), "deduplication": "Exact rig + resolved animation-set SHA256 + animation name"}


def cleanup_frames(folder):
    """Remove only reproducible PNGs in the explicitly validated clip frame directory."""
    parent = folder.resolve()
    target = (parent / "frames").resolve()
    if target.parent != parent or target.name != "frames" or (parent / "frames").is_symlink():
        raise ValueError("Unsafe frame cleanup path")
    if target.is_dir():
        for path in target.iterdir():
            if path.is_file() and path.name.startswith("frame_") and path.suffix == ".png":
                path.unlink()
        if not any(target.iterdir()):
            target.rmdir()


def fingerprint(job, skin, assets, blender, decoder_hash=None):
    inputs = {"rig": cached_digest(raw_path(assets / "raw", job["rig"])),
              "animset": cached_digest(raw_path(assets / "raw", job["resolved_animset"])),
              "animation": job["animation_name"], "skin": skin, "fps": 12, "seconds": 8,
              "blender": cached_digest(blender),
              "tools": {name: cached_digest(ROOT / "tools" / name) for name in (
                  "workspot_preview.py", "workspot_preview_blender.py", "workspot_skin.py",
                  "sex_rid_preview.py", "sex_rid_preview_blender.py")}}
    if decoder_hash is not None:
        inputs["tools"]["workspot_preview.py"] = decoder_hash
    return hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()


@lru_cache(maxsize=1)
def legacy_extent_decoder_hash():
    """Admit old successes only across this exact rejection-guard-only change.

    Reversing just these two lines reconstructs the complete old source hash.
    Any other decoder edit therefore fails to match old receipts. Coordinates,
    frame selection, skinning and rendering are untouched by this migration.
    """
    data = (ROOT / "tools/workspot_preview.py").read_bytes()
    current = b'    if max(bounds["max"][i] - bounds["min"][i] for i in range(3)) < 0.3:\n        raise ValueError("Decoded body has implausibly small spatial extent")'
    old = b'    if bounds["max"][2] - bounds["min"][2] < 0.3:\n        raise ValueError("Decoded body has implausibly small vertical extent")'
    if data.count(current) != 1:
        return None
    return hashlib.sha256(data.replace(current, old, 1)).hexdigest()


@lru_cache(maxsize=2048)
def stat_digest(path, size, modified):
    return digest(path)


def cached_digest(path):
    stat = path.stat()
    return stat_digest(path, stat.st_size, stat.st_mtime_ns)


def render_one(job, skin, out, blender, previous):
    folder, assets = out / "previews" / job["id"], out / "preview-assets"
    try:
        identity = fingerprint(job, skin, assets, blender)
        full_receipt = folder / "full-batch.json"
        if full_receipt.is_file():
            saved = read(full_receipt)
            producers_valid = all(Path(p).is_file() and cached_digest(Path(p)) == h for p, h in saved.get("producer_files", {}).items())
            identity_valid = saved.get("identity") == identity or saved.get("accepted_identity") == identity
            if not identity_valid and legacy_extent_decoder_hash() is not None:
                legacy = fingerprint(job, skin, assets, blender, legacy_extent_decoder_hash())
                identity_valid = saved.get("identity") == legacy
            if producers_valid and identity_valid and all((folder / n).is_file() and digest(folder / n) == h for n, h in saved["result"].get("outputs", {}).items()):
                if len(saved["result"].get("outputs", {})) == 2:
                    if saved.get("identity") != identity and saved.get("accepted_identity") != identity:
                        saved.update(accepted_identity=identity, validation_migration="vertical-to-spatial extent guard only; original render identity and media preserved")
                        atomic_write_json(full_receipt, saved)
                    return saved["result"]
        # Pilot inputs stay frozen so new workspot associations don't rerender old media.
        pilot = previous.get(job["id"])
        if pilot and (folder / "decoded.json").is_file() and (folder / "render.json").is_file():
            preview = read(folder / "decoded.json")
            if (preview["provenance"]["animset_sha256"] == digest(raw_path(assets / "raw", job["resolved_animset"]))
                    and preview.get("skin_manifest") == skin):
                result = render_job(pilot, preview, out / "previews", blender)
            else:
                pilot = None
        else:
            pilot = None
        if pilot is None:
            if shutil.disk_usage(out).free < 15 * 1024**3:
                raise RuntimeError("Less than 15 GiB disk free; rendering stopped")
            narrowed = {**job, "animsets": [job["resolved_animset"]]}
            preview = decode_job(narrowed, assets, 12, 8)
            preview["skin_manifest"] = skin
            preview["limitations"] = ["Source body meshes with neutral material; props, furniture and synchronization partners omitted",
                                      "Individual clip excerpt; no tree playback or runtime validation", *skin["limitations"]]
            from workspot_render_fast import render, producer_files
            result = render(job, preview, out / "previews", blender)
        else:
            producer_files = dict
        atomic_write_json(full_receipt, {"identity": identity, "result": result, "producer_files": producer_files()})
        cleanup_frames(folder)
        return result
    except Exception as error:
        return {"id": job["id"], "status": "failed", "error": f"{type(error).__name__}: {error}"}


def run(args):
    out = args.output.resolve()
    state_path = out / "full-batch/state.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()

    def status(stage, **values):
        state = {"stage": stage, "updated_at": now(), "pid": __import__("os").getpid(),
                 "elapsed_seconds": time.monotonic() - started, **values}
        atomic_write_json(state_path, state)
        print(json.dumps(state), flush=True)

    catalog, previous = read(out / "catalog.json"), read(out / "preview-plan.json")
    if args.resume_plan:
        plan = read(out / "full-batch/plan.json")
        prep_errors = read(out / "full-batch/preparation-errors.json")
        status("resuming", total=len(plan["jobs"]))
    else:
        status("planning")
        plan = make_plan(catalog, out / "raw", [], all_workspots=True, max_clips=0)
        atomic_write_json(out / "full-batch/registered-plan.json", plan)
        names = sorted({n for j in plan["jobs"] for n in [j["rig"], *j["animsets"]]})
        prep_errors = []
        for start in range(0, len(names), 30):
            if shutil.disk_usage(out).free < 30 * 1024**3:
                raise RuntimeError("Less than 30 GiB disk free; preparation stopped")
            group = names[start:start + 30]
            subset = {"jobs": [{"rig": n, "animsets": []} for n in group]}
            status("preparing", resources_checked=start, total_resources=len(names), preparation_errors=len(prep_errors))
            try:
                prepare_missing(subset, out / "preview-assets", args.game_root, args.wolvenkit)
            except Exception as error:
                prep_errors.append({"resources": group, "error": str(error)})
                # One absent registration must not suppress the other extracted sets.
                binaries = [out / "preview-assets/binary" / n.replace("\\", "/") for n in group]
                pending = [p for p in binaries if p.is_file() and not p.with_suffix(p.suffix + ".json").is_file()]
                if pending:
                    with (out / f"full-batch/serialize-recovery-{start:04}.log").open("w") as log:
                        subprocess.run([str(args.wolvenkit), "convert", "serialize", *map(str, pending), "-v", "Minimal"],
                                       stdout=log, stderr=subprocess.STDOUT, check=False)
                for n in group:
                    source = raw_path(out / "preview-assets/binary", n)
                    target = raw_path(out / "preview-assets/raw", n)
                    if source.is_file() and not target.exists():
                        try:
                            read(source)
                            target.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copyfile(source, target)
                        except (OSError, ValueError):
                            pass
            log = out / "preview-assets/batch-prepare.log"
            if log.exists():
                shutil.copyfile(log, out / f"full-batch/prepare-{start:04}.log")
        atomic_write_json(out / "full-batch/preparation-errors.json", prep_errors)
        status("indexing")
        index = source_index(plan, out / "preview-assets", lambda n, total: status("indexing", indexed=n, total=total) if n % 20 == 0 else None)
        atomic_write_json(out / "full-batch/source-index.json", index)
        plan = canonical_plan(plan, index, previous)
        atomic_write_json(out / "full-batch/plan.json", plan)
    prepare_female_skin(out, args.game_root, args.wolvenkit)
    skins = {}
    for path in [out / "skinned-assets/skin.json", out / "skinned-assets-female/skin.json"]:
        if path.is_file():
            skin = read(path)
            if not all(Path(p).is_file() and digest(Path(p)) == h for p, h in skin["files"].items()):
                raise ValueError(f"Skin assets changed: {path}")
            skins[skin["rig"]] = skin
    missing_rigs = {j["rig"] for j in plan["jobs"]} - skins.keys()
    if missing_rigs:
        raise ValueError(f"Missing source skins: {sorted(missing_rigs)}")
    previous_jobs = {j["id"]: j for j in previous["jobs"]}
    results = {}
    journal = out / "full-batch/render-results.jsonl"
    last_checkpoint = time.monotonic()
    with journal.open("a", encoding="utf-8") as stream, ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(render_one, job, skins[job["rig"]], out, args.blender, previous_jobs): job for job in plan["jobs"]}
        for future in as_completed(futures):
            result = future.result()
            results[result["id"]] = result
            stream.write(json.dumps(result) + "\n")
            stream.flush()
            if len(results) % 10 == 0 or time.monotonic() - last_checkpoint > 30:
                counts = Counter(r["status"] for r in results.values())
                status("rendering", completed=len(results), total=len(futures), counts=counts,
                       unresolved=len(plan["unresolved"]), skipped_workspots=len(plan["skipped"]))
                atomic_write_json(out / "full-batch/results.json", list(results.values()))
                last_checkpoint = time.monotonic()
    ordered = [results[j["id"]] for j in plan["jobs"]]
    atomic_write_json(out / "full-batch/results.json", ordered)
    rows = caption_jobs(plan, ordered, catalog)
    target = out / "previews/full-caption-jobs.jsonl"
    target.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    counts = Counter(r["status"] for r in ordered)
    status("ready_for_captioning", completed=len(results), total=len(plan["jobs"]), counts=counts,
           caption_jobs=len(rows), jobs_path=str(target), unresolved=len(plan["unresolved"]),
           skipped_workspots=len(plan["skipped"]), preparation_errors=len(prep_errors))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--game-root", type=Path, default=default_tool_path("game"))
    p.add_argument("--wolvenkit", type=Path, default=default_tool_path("wolvenkit"))
    p.add_argument("--blender", type=Path, default=default_tool_path("blender"))
    p.add_argument("--workers", type=int, default=2)
    p.add_argument("--prepare-female-skin", action="store_true")
    p.add_argument("--resume-plan", action="store_true", help="Reuse the completed full-batch source plan")
    args = p.parse_args(argv)
    if args.workers < 1:
        p.error("workers must be positive")
    if args.prepare_female_skin:
        print(prepare_female_skin(args.output.resolve(), args.game_root, args.wolvenkit))
        return 0
    try:
        run(args)
    except Exception as error:
        atomic_write_json(args.output / "full-batch/state.json", {"stage": "failed", "updated_at": now(), "error": f"{type(error).__name__}: {error}"})
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
