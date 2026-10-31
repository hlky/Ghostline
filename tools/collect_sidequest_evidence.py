"""Replay the checked side-quest resource selection into an ignored scratch tree."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import subprocess

from ghostline_red import DEFAULT_RED_CLI, ensure_schema
from toolchain import resolve_tool


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def collect(job):
    item, game, scratch, schema, wolvenkit = job
    game, scratch = Path(game), Path(scratch)
    binary = scratch / "cr2w" / item["depot"].replace("\\", "/")
    archive = game / "archive/pc" / item["archive_relative"]
    if not binary.exists() or digest(binary) != item["binary_sha256"]:
        subprocess.run([str(DEFAULT_RED_CLI), "extract", str(archive), "--output", str(scratch / "cr2w"), "--path", item["depot"]], check=True, capture_output=True)
    if digest(binary) != item["binary_sha256"]:
        raise ValueError(f"Source payload changed: {item['depot']}")
    raw = scratch / "raw" / (item["depot"].replace("\\", "/") + ".json")
    raw.parent.mkdir(parents=True, exist_ok=True)
    if not raw.exists() or digest(raw) != item["raw_sha256"]:
        if item["serializer"] == "wolvenkit":
            subprocess.run([wolvenkit, "convert", "serialize", str(binary), "-o", str(raw.parent), "-v", "Minimal"], check=True, capture_output=True)
        else:
            subprocess.run([str(DEFAULT_RED_CLI), "cr2w-serialize", str(binary), str(raw), "--schema", schema], check=True, capture_output=True)
        # Paths/timestamps are serializer diagnostics, not game payload. Restore
        # the recorded header bytes so replay in another scratch directory can
        # reproduce the frozen JSON identity without altering Data.
        if "header_prefix" in item:
            payload = raw.read_bytes()
            boundary = payload.index(b'\n  "Data":')
            raw.write_bytes(item["header_prefix"].encode("utf-8") + payload[boundary:])
    return {"depot": item["depot"], "binary_sha256": digest(binary), "raw_sha256": digest(raw),
            "raw_matches_original": digest(raw) == item["raw_sha256"], "serializer": item["serializer"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, default=Path("reference/quests/deep-dives/catalogue/source-selection.json"))
    parser.add_argument("--game-root", type=Path)
    parser.add_argument("--scratch", type=Path, default=Path(".tmp/quest-deep-dives/replay"))
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    selection = json.loads(args.selection.read_text(encoding="utf-8"))["resources"]
    game = resolve_tool("game", args.game_root)
    schema = str(ensure_schema())
    wolvenkit = str(resolve_tool("wolvenkit"))
    args.scratch.mkdir(parents=True, exist_ok=True)
    results, failures = [], []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(collect, (item, str(game), str(args.scratch), schema, wolvenkit)): item for item in selection}
        for job in as_completed(jobs):
            try:
                results.append(job.result())
            except Exception as error:
                failures.append({"depot": jobs[job]["depot"], "error": str(error)})
    (args.scratch / "replay-report.json").write_text(json.dumps({"resources": sorted(results, key=lambda r: r["depot"]), "failures": failures}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"resources": len(results), "failures": failures, "raw_metadata_differences": sum(not r["raw_matches_original"] for r in results)}))
    if failures or any(not r["raw_matches_original"] for r in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
