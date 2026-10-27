#!/usr/bin/env python3
"""Validate collected full-run captions and publish local review/search artifacts."""
from contextlib import closing
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3

from artifact_io import atomic_write_json
from workspot_catalog import DEFAULT_OUTPUT, digest, read
from workspot_caption_review import build
from workspot_preview import raw_path


def lines(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]


def publish(output=DEFAULT_OUTPUT):
    output = Path(output)
    full = output / "full-batch"
    results = output / "caption-results"
    receipt = read(full / "caption-run-receipt.json")
    if receipt["pod"]["desiredStatus"] != "EXITED" or receipt["errors"]:
        raise ValueError("Collection and shutdown must succeed before publication")
    inputs = lines(full / "uploaded-jobs.jsonl")
    jobs = {r["id"]: r for r in inputs}
    if len(jobs) != len(inputs):
        raise ValueError("Duplicate uploaded inputs")
    plan = read(full / "plan.json")
    planned = {r["id"]: r for r in plan["jobs"]}
    catalog = {r["depot_path"]: r for r in read(output / "catalog.json")["workspots"]}
    raw = lines(results / "full-run/captions.jsonl")
    successful = {}
    hashed = lru_cache(maxsize=None)(digest)
    for row in raw:
        key = row["id"]
        if row["input"] != jobs[key]:
            raise ValueError(f"Uploaded input mismatch: {key}")
        identity = hashlib.sha256(json.dumps({"job": row["input"], "settings": row["settings"]}, sort_keys=True).encode()).hexdigest()
        if identity != row["input_identity"]:
            raise ValueError(f"Caption identity mismatch: {key}")
        if row["status"] != "captioned":
            continue
        if row["review_status"] != "model_suggested_unreviewed":
            raise ValueError(f"Unexpected review promotion: {key}")
        for name, expected in row["input"]["media_sha256"].items():
            if name not in {"preview.mp4", "contact.png"} or hashed(output / "previews" / key / name) != expected:
                raise ValueError(f"Media mismatch: {key}/{name}")
        render = read(output / "previews" / key / "render.json")
        source = render["provenance"]
        job = planned[key]
        for resource, expected in ((job["resolved_animset"], source["animset_sha256"]), (job["rig"], source["rig_sha256"])):
            if hashed(raw_path(output / "preview-assets/raw", resource)) != expected:
                raise ValueError(f"Animation source changed: {key}/{resource}")
        for use in job["uses"]:
            spot = catalog[use["workspot"]]["source"]
            if (spot["binary_sha256"] or spot["raw_sha256"]) != use["workspot_sha256"]:
                raise ValueError(f"Workspot source changed: {key}")
        successful[key] = row
    if set(successful) != set(jobs):
        raise ValueError(f"Incomplete captions: {len(successful)}/{len(jobs)}")
    main = results / "captions.jsonl"
    backup = results / "full-run/history/pre-publication-captions.jsonl"
    if not backup.exists():
        shutil.copy2(main, backup)
    original = lines(backup)
    # Preserve pilot identities and any saved human reviews for their clip IDs.
    existing = {r["id"] for r in original if r.get("status") == "captioned"}
    merged = original + [r for key, r in successful.items() if key not in existing]
    temporary = main.with_suffix(".jsonl.tmp")
    temporary.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in merged), encoding="utf-8")
    temporary.replace(main)
    reviewed, page = build(output)
    database = results / "caption-search.sqlite3"
    temp_db = database.with_suffix(".sqlite3.tmp")
    if temp_db.exists():
        temp_db.unlink()
    associations = 0
    with closing(sqlite3.connect(temp_db)) as db:
        db.executescript("""
            CREATE TABLE captions (id TEXT PRIMARY KEY, animation TEXT, rig TEXT, caption_json TEXT, review_status TEXT);
            CREATE TABLE associations (clip_id TEXT, workspot_path TEXT, source_sha256 TEXT, entry_role TEXT, entry_id INTEGER, entry_field TEXT);
            CREATE INDEX associations_workspot ON associations(workspot_path);
            CREATE INDEX associations_clip ON associations(clip_id);
            CREATE VIRTUAL TABLE caption_search USING fts5(clip_id UNINDEXED, animation, workspots, description);
        """)
        for key, row in reviewed.items():
            job = planned.get(key)
            if job is None:
                context = row["input"]["context"]
                job = {"animation_name": context["animation_name"], "rig": context["rig"],
                       "uses": [{"workspot": s["workspot_path"], "workspot_sha256": s["source_sha256"],
                                 "role": s["entry_role"], "entry_id": s["entry_id"], "field": None}
                                for s in context["workspots"]]}
            caption = json.dumps(row["caption"], ensure_ascii=False)
            db.execute("INSERT INTO captions VALUES(?,?,?,?,?)", (key, job["animation_name"], job["rig"], caption, row["review_status"]))
            for use in job["uses"]:
                db.execute("INSERT INTO associations VALUES(?,?,?,?,?,?)", (key, use["workspot"], use["workspot_sha256"], use["role"], use["entry_id"], use["field"]))
                associations += 1
            db.execute("INSERT INTO caption_search VALUES(?,?,?,?)", (key, job["animation_name"], "\n".join(sorted({u["workspot"] for u in job["uses"]})), caption))
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("Search database integrity check failed")
        db.commit()
    temp_db.replace(database)
    report = {"caption_successes": len(successful), "caption_failures": len(set(jobs) - set(successful)),
              "raw_attempts": len(raw), "pilot_records_preserved": len(original), "review_clips": len(reviewed),
              "workspot_associations": associations, "render_successes": len(jobs),
              "render_failures": len(plan["jobs"]) - len(jobs), "unresolved_registration_jobs": len(plan["unresolved"]),
              "skipped_workspots": len(plan["skipped"]), "scope": plan["scope"],
              "review_status": "model_suggested_unreviewed", "runtime_verified": False,
              "hashes": {str(p.relative_to(output)): digest(p) for p in (full / "uploaded-jobs.jsonl", results / "full-run/captions.jsonl", main, database)},
              "page": str(page), "shutdown": receipt["pod"]}
    atomic_write_json(full / "publication.json", report)
    print(json.dumps(report, indent=2), flush=True)
    return report


if __name__ == "__main__":
    publish()
