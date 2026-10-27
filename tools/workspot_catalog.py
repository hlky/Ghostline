#!/usr/bin/env python3
"""Read-only workspot extraction, structural catalog, search and review report."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys

from artifact_io import atomic_write_json
from ghostline_red import DEFAULT_RED_CLI, ensure_schema
from toolchain import default_tool_path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "generated/workspots"
DEFAULT_ANNOTATIONS = ROOT / "reference/workspots/annotations.json"
ANIMATION_FIELDS = (
    "animName", "idleAnim", "idleName", "turnAnimName",
    "facialIdleMaleAnimation", "facialIdleFemaleAnimation",
    "facialIdleKey_MaleAnimation", "facialIdleKey_FemaleAnimation",
)


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def scalar(value):
    if isinstance(value, dict):
        return value.get("$value", value.get("id"))
    return value


def walk(value, pointer=""):
    if isinstance(value, dict):
        yield pointer, value
        for key, child in value.items():
            yield from walk(child, pointer + "/" + key.replace("~", "~0").replace("/", "~1"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + f"/{index}")


def depot(value):
    return str(value).replace("/", "\\").lower()


def paths(value, suffix=None):
    found = set()
    for _, node in walk(value):
        if "DepotPath" in node:
            name = scalar(node["DepotPath"])
            if name and name != "0" and (suffix is None or str(name).lower().endswith(suffix)):
                found.add(depot(name))
    return sorted(found)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def annotations(path):
    doc = read(path)
    if doc.get("schema_version") != 1 or not isinstance(doc.get("workspots"), dict):
        raise ValueError("Annotations require schema_version 1 and a workspots object")
    result = {}
    for name, record in doc["workspots"].items():
        if not name.lower().endswith(".workspot") or not isinstance(record, dict):
            raise ValueError(f"Invalid annotation: {name}")
        if record.get("status", "unreviewed") not in ("unreviewed", "structure_reviewed", "visually_reviewed", "runtime_verified", "rejected"):
            raise ValueError(f"Invalid review status: {name}")
        for field in ("tags", "evidence"):
            if field in record and (not isinstance(record[field], list) or any(not isinstance(item, str) for item in record[field])):
                raise ValueError(f"{name}: {field} must be a string list")
        for field in ("label", "description", "notes", "source_sha256"):
            if field in record and not isinstance(record[field], str):
                raise ValueError(f"{name}: {field} must be a string")
        if record.get("status") in ("visually_reviewed", "runtime_verified") and not (record.get("evidence") and record.get("source_sha256")):
            raise ValueError(f"{name}: visual/runtime review requires evidence and source_sha256")
        result[depot(name)] = record
    return result


def inspect_workspot(path, raw_root, binary_root=None):
    document = read(path)
    root = document.get("Data", {}).get("RootChunk", {})
    if root.get("$type") != "workWorkspotResource":
        raise ValueError(f"Not a workWorkspotResource: {path}")
    relative = path.relative_to(raw_root).as_posix().removesuffix(".json")
    if not relative.endswith(".workspot"):
        raise ValueError(f"Expected mirrored .workspot.json: {path}")
    name = depot(relative)
    handles = {str(n["HandleId"]): n["Data"] for _, n in walk(root) if "HandleId" in n and isinstance(n.get("Data"), dict)}

    def resolve(value):
        if isinstance(value, dict):
            if "HandleRefId" in value:
                key = str(value["HandleRefId"])
                if key not in handles:
                    raise ValueError(f"{path}: unresolved handle {key}")
                return handles[key]
            return value.get("Data", value)
        return {}

    tree = resolve(root.get("workspotTree"))
    if tree.get("$type") != "workWorkspotTree":
        raise ValueError(f"{path}: missing decoded workspot tree")
    if any("$rawData" in node for _, node in walk(tree)):
        raise ValueError(f"{path}: opaque workspot data requires serializer investigation")
    entries = []
    seen = set()

    def visit(value, parent=None):
        node = resolve(value)
        if not node or id(node) in seen:
            return
        seen.add(id(node))
        entry = {"type": node.get("$type"), "id": scalar(node.get("id")), "parent_id": parent}
        # Preserve exact authored settings, including offsets and item actions.
        entry["settings"] = {key: val for key, val in node.items() if key not in ("$type", "id", "list")}
        entries.append(entry)
        for child in node.get("list", []):
            visit(child, entry["id"])

    visit(tree.get("rootEntry"))
    # Custom transitions are outside the root entry hierarchy.
    for transition in tree.get("customTransitionAnims", []):
        visit(transition)
    animations = sorted({str(scalar(n[key])) for entry in entries for _, n in walk(entry["settings"])
                         for key in ANIMATION_FIELDS
                         if key in n and scalar(n[key]) not in (None, "None", "", "0", "<no_auto_transition>")})
    entry_counts = dict(sorted(Counter(e["type"] for e in entries).items()))
    binary = binary_root / relative if binary_root else None
    result = {
        "depot_path": name,
        "source": {"raw_sha256": digest(path), "binary_sha256": digest(binary) if binary and binary.is_file() else None},
        "rigs": paths(tree, ".rig"), "animsets": paths(tree, ".anims"),
        "resource_references": paths(root), "animations": animations,
        "entry_counts": entry_counts, "entries": entries,
        "tree_settings": {key: value for key, value in tree.items() if key not in ("rootEntry", "finalAnimsets", "customTransitionAnims", "$type")},
        "loop_entry_ids": [e["id"] for e in entries if scalar(e["settings"].get("loopInfinitely")) in (1, True)],
        "entry_animation_ids": [e["id"] for e in entries if e["type"] in ("workEntryAnim", "workSyncMasterEntryAnim")],
        "exit_animation_ids": [e["id"] for e in entries if e["type"] in ("workExitAnim", "workFastExit")],
        "name_hints": re.sub(r"[_\\.]+", " ", name.removesuffix(".workspot")).split(),
    }
    return result


def usage_index(roots):
    usage = defaultdict(list)
    for root in roots:
        for path in sorted(root.rglob("*.json")):
            if not any(path.name.endswith(ext + ".json") for ext in (".scene", ".streamingsector", ".ent", ".app", ".community", ".questphase")):
                continue
            doc = read(path)
            refs = []
            for pointer, node in walk(doc):
                name = scalar(node.get("DepotPath"))
                if isinstance(name, str) and name.lower().endswith(".workspot"):
                    refs.append((name, pointer))
            if refs:
                source = str(path.resolve().relative_to(ROOT)) if path.resolve().is_relative_to(ROOT) else str(path.resolve())
                sha = digest(path)
                for name, pointer in refs:
                    usage[depot(name)].append({"source": source, "sha256": sha, "pointer": pointer})
    return usage


def build(raw_root, output, annotation_path, binary_root=None, usage_roots=()):
    reviewed = annotations(annotation_path)
    usage = usage_index(usage_roots)
    records, failures = [], []
    raw_files = sorted(raw_root.rglob("*.workspot.json"))
    if binary_root and binary_root.is_dir():
        decoded = {p.relative_to(raw_root).as_posix().removesuffix(".json") for p in raw_files}
        for binary in sorted(binary_root.rglob("*.workspot")):
            if binary.relative_to(binary_root).as_posix() not in decoded:
                failures.append({"source": str(binary), "error": "Missing decoded .workspot.json"})
    for path in raw_files:
        try:
            record = inspect_workspot(path, raw_root, binary_root)
            note = dict(reviewed.get(record["depot_path"], {}))
            expected = note.get("source_sha256")
            actual = record["source"]["binary_sha256"] or record["source"]["raw_sha256"]
            record["annotation_stale"] = bool(expected and expected != actual)
            record["annotation"] = note
            record["review_status"] = "stale" if record["annotation_stale"] else note.get("status", "unreviewed")
            record["usage"] = usage.get(record["depot_path"], [])
            records.append(record)
        except (ValueError, KeyError, TypeError, RecursionError) as error:
            failures.append({"source": str(path), "error": str(error)})
    if not records:
        raise ValueError(f"No decoded workspots in {raw_root}; failures: {failures[:3]}")
    summary = {
        "resources": len(records), "failures": len(failures),
        "distinct_animation_names": len({a for r in records for a in r["animations"]}),
        "with_usage": sum(bool(r["usage"]) for r in records),
        "review_status": dict(Counter(r["review_status"] for r in records)),
        "entry_types": dict(Counter(t for r in records for t in r["entry_counts"] for _ in range(r["entry_counts"][t]))),
    }
    catalog = {"schema_version": 1, "summary": summary, "coverage": {"raw_root": str(raw_root.resolve()), "usage_roots": [str(p.resolve()) for p in usage_roots], "scope": "Extracted resources only; not proof of rig compatibility or runtime behavior"}, "failures": failures, "workspots": records}
    output.mkdir(parents=True, exist_ok=True)
    atomic_write_json(output / "catalog.json", catalog)
    atomic_write_json(output / "summary.json", {key: val for key, val in catalog.items() if key != "workspots"})
    # Replace the database only after a complete transaction; preserve the old DB on failure.
    candidate = output / "workspots.next.sqlite3"
    candidate.unlink(missing_ok=True)
    with closing(sqlite3.connect(candidate)) as db, db:
        db.execute("CREATE TABLE workspots (depot_path TEXT PRIMARY KEY, label TEXT, review_status TEXT, animation_count INTEGER, usage_count INTEGER, data TEXT)")
        db.execute("CREATE VIRTUAL TABLE search USING fts5(depot_path UNINDEXED, text, tokenize='unicode61')")
        for r in records:
            data = json.dumps(r, ensure_ascii=False)
            db.execute("INSERT INTO workspots VALUES (?,?,?,?,?,?)", (r["depot_path"], r["annotation"].get("label", ""), r["review_status"], len(r["animations"]), len(r["usage"]), data))
            # Tokenize underscores/backslashes too: 'hands knees' finds clip names.
            searchable = json.dumps({k: r[k] for k in ("depot_path", "animations", "rigs", "animsets", "resource_references", "tree_settings", "entries", "name_hints", "annotation", "entry_counts")}, ensure_ascii=False)
            db.execute("INSERT INTO search VALUES (?,?)", (r["depot_path"], re.sub(r"[_\\]+", " ", searchable)))
        db.execute("CREATE TABLE metadata (data TEXT)")
        db.execute("INSERT INTO metadata VALUES (?)", (json.dumps(summary),))
    candidate.replace(output / "workspots.sqlite3")
    return catalog


def extract(game, output, wolvenkit):
    directories = [game / "archive/pc/content", game / "archive/pc/ep1"]
    directories = [d for d in directories if d.is_dir()]
    if not directories:
        raise ValueError(f"No vanilla archive directories beneath {game}")
    output.mkdir(parents=True, exist_ok=True)
    command = [str(wolvenkit), "unbundle", *map(str, directories), "-o", str(output), "-r", r"\.workspot$", "-v", "Minimal"]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    atomic_write_json(output.parent / "extraction.json", {
        "command": command, "scope": "Vanilla content and ep1 only; installed mod overrides excluded",
        "archives": [{"path": str(a), "size": a.stat().st_size, "mtime_ns": a.stat().st_mtime_ns} for d in directories for a in sorted(d.glob("*.archive"))],
        "log": result.stdout + result.stderr,
        "resources": len(list(output.rglob("*.workspot"))),
    })
    return len(list(output.rglob("*.workspot")))


def serialize_tree(binary_root, output, workers=4):
    schema = ensure_schema()
    inputs = sorted(binary_root.rglob("*.workspot"))
    if not inputs:
        raise ValueError(f"No .workspot binaries in {binary_root}")
    failures = []

    def convert(source):
        target = output / (source.relative_to(binary_root).as_posix() + ".json")
        receipt = target.with_suffix(target.suffix + ".receipt")
        identity = {"binary": digest(source), "writer": writer_hash, "schema": schema_hash}
        if target.is_file() and receipt.is_file() and read(receipt) == {**identity, "raw": digest(target)}:
            return None
        target.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run([str(DEFAULT_RED_CLI), "cr2w-serialize", str(source), str(target), "--schema", str(schema)], capture_output=True, text=True)
        if result.returncode:
            target.unlink(missing_ok=True)
            return {"source": str(source), "error": result.stderr or result.stdout}
        atomic_write_json(receipt, {**identity, "raw": digest(target)})
        return None

    writer_hash, schema_hash = digest(DEFAULT_RED_CLI), digest(schema)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for index, failure in enumerate(pool.map(convert, inputs), 1):
            if failure:
                failures.append(failure)
            if index % 250 == 0:
                print(f"Serialized {index}/{len(inputs)}", flush=True)
    output.mkdir(parents=True, exist_ok=True)
    atomic_write_json(output / "serialization.json", {"inputs": len(inputs), "failures": failures, "writer_sha256": writer_hash, "schema_sha256": schema_hash})
    return {"inputs": len(inputs), "failures": len(failures)}


def search(database, query, limit=30, status=None):
    words = re.findall(r"[^\W_]+", query, flags=re.UNICODE)
    expression = " AND ".join('"' + word + '"*' for word in words)
    if not database.is_file():
        raise ValueError(f"Build the workspot database first: {database}")
    with closing(sqlite3.connect(database)) as db:
        sql = "SELECT w.data FROM workspots w"
        params = []
        conditions = []
        if expression:
            sql += " JOIN search s ON w.depot_path=s.depot_path"
            conditions.append("search MATCH ?")
            params.append(expression)
        if status:
            conditions.append("w.review_status=?")
            params.append(status)
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY w.depot_path LIMIT ?"
        params.append(limit if limit else -1)
        return [json.loads(row[0]) for row in db.execute(sql, params)]


def review(catalog, target):
    # Embedded catalog data with optional neighboring preview media.
    # User text is always assigned through textContent.
    plan_path = target.parent / "preview-plan.json"
    results_path = target.parent / "previews/results.json"
    previews = defaultdict(list)
    if plan_path.is_file() and results_path.is_file():
        jobs = {j["id"]: j for j in read(plan_path)["jobs"]}
        for result in read(results_path):
            key = result["id"]
            if result.get("status") != "rendered_proxy" or key not in jobs or not re.fullmatch(r"[a-f0-9]{20}", key):
                continue
            folder = target.parent / "previews" / key
            if not all((folder / name).is_file() and digest(folder / name) == sha for name, sha in result.get("outputs", {}).items()) or len(result.get("outputs", {})) != 2:
                continue
            for use in jobs[key]["uses"]:
                previews[use["workspot"]].append({"id": key, "animation_name": jobs[key]["animation_name"], "role": use["role"], "workspot_sha256": use["workspot_sha256"], "renderer": result.get("renderer", "mannequin"), "limitations": result.get("limitations", [])})
    catalog = {**catalog, "workspots": [{**r, "preview_clips": [p for p in previews[r["depot_path"]] if p["workspot_sha256"] == (r["source"]["binary_sha256"] or r["source"]["raw_sha256"])]} for r in catalog["workspots"]]}
    data = json.dumps(catalog, ensure_ascii=False).replace("<", "\\u003c")
    page = '''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ghostline workspots</title><style>
body{margin:0;background:#10151d;color:#e0e6f0;font:15px system-ui}header{padding:24px 32px;border-bottom:1px solid #354154}h1{margin:0 0 8px}p{color:#aab9cb;max-width:1000px}input,select,button{background:#202b3b;color:inherit;padding:10px;border:1px solid #637188;border-radius:4px}input{width:45%}main{display:grid;grid-template-columns:minmax(320px,38%) 1fr;height:75vh}#list,#detail{overflow:auto;padding:16px}#list button{display:block;text-align:left;width:100%;margin-bottom:8px;overflow-wrap:anywhere}#detail{border-left:1px solid #354154}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}code{overflow-wrap:anywhere}h2{font-size:19px}#count{margin:12px 0} @media(max-width:700px){main{display:block;height:auto}#list{max-height:40vh}input{width:85%}}
</style><header><h1>Ghostline / Workspots</h1><p>Search animation names, entry types, rig paths, props and reviewed descriptions. Names are clues. Visual meaning and runtime compatibility require evidence.</p>
<input id="q" aria-label="Search workspots" placeholder="Try: hands knees, tablet, exit, chair"><select id="status" aria-label="Review status"><option value="">All review states</option><option>unreviewed</option><option>structure_reviewed</option><option>visually_reviewed</option><option>runtime_verified</option><option>stale</option><option>rejected</option></select><div id="count"></div></header><main><div id="list"></div><article id="detail">Select a workspot to inspect its contents.</article></main>
<script>const catalog=__DATA__;const all=catalog.workspots;const q=document.querySelector('#q'),status=document.querySelector('#status'),list=document.querySelector('#list'),detail=document.querySelector('#detail');
const indexed=all.map(r=>({r,text:JSON.stringify(r).replaceAll('_',' ').replaceAll('\\\\',' ').toLowerCase()}));
function add(tag,text,parent=detail){let e=document.createElement(tag);e.textContent=text;parent.append(e);return e;}
function show(r){detail.replaceChildren();add('h2',r.annotation.label||r.depot_path.split('\\\\').pop());add('code',r.depot_path);add('p','Review: '+r.review_status+(r.annotation_stale?' — source changed; re-review required':''));if(r.annotation.description)add('p',r.annotation.description);if(r.annotation.notes)add('p',r.annotation.notes);
if(r.preview_clips.length){add('h2','Rendered body clips');add('p','Individual clip excerpts. Props, furniture, facial performance and synchronization partners are omitted.');for(const p of r.preview_clips){let d=document.createElement('details');detail.append(d);let s=document.createElement('summary');s.textContent=p.role+' — '+p.animation_name+' ('+p.renderer+')';d.append(s);add('p',p.limitations.join('; '),d);let v=document.createElement('video');v.controls=true;v.preload='none';v.style.width='100%';v.src='previews/'+p.id+'/preview.mp4';d.append(v);let img=document.createElement('img');img.alt='Six timestamped samples';img.loading='lazy';img.style.width='100%';img.src='previews/'+p.id+'/contact.png';d.append(img);}}
add('h2','Contents');add('p',r.animations.length+' animation names · '+r.entries.length+' entries · '+r.usage.length+' references');add('pre',r.animations.join('\\n'));for(const [title,value] of [['Rigs',r.rigs],['Animation sets',r.animsets],['Entry / loop / exit IDs',{entry:r.entry_animation_ids,loop:r.loop_entry_ids,exit:r.exit_animation_ids}],['Usage evidence',r.usage],['Full structure and provenance',r]]){let d=document.createElement('details');detail.append(d);let s=document.createElement('summary');s.textContent=title;d.append(s);add('pre',JSON.stringify(value,null,2),d);}}
function filter(){const terms=q.value.toLowerCase().split(/\\s+/).filter(Boolean);let found=indexed.filter(x=>(!status.value||x.r.review_status===status.value)&&terms.every(t=>x.text.includes(t)));document.querySelector('#count').textContent=found.length+' / '+all.length+' workspots · '+catalog.summary.failures+' parse failures · showing first 200';list.replaceChildren();for(const {r} of found.slice(0,200)){let b=add('button',(r.annotation.label||r.depot_path.split('\\\\').pop())+' · '+r.animations.length+' anims · '+r.review_status,list);b.onclick=()=>show(r);}}
q.oninput=filter;status.onchange=filter;filter();</script>'''
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page.replace("__DATA__", data), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("extract")
    p.add_argument("--game-root", type=Path, default=default_tool_path("game"))
    p.add_argument("--wolvenkit", type=Path, default=default_tool_path("wolvenkit"))
    p = sub.add_parser("serialize")
    p.add_argument("--binary-root", type=Path)
    p.add_argument("--workers", type=int, default=4)
    p = sub.add_parser("build")
    p.add_argument("--raw-root", type=Path)
    p.add_argument("--binary-root", type=Path)
    p.add_argument("--annotations", type=Path, default=DEFAULT_ANNOTATIONS)
    p.add_argument("--usage-root", type=Path, action="append", default=[])
    p = sub.add_parser("search")
    p.add_argument("query", nargs="?", default="")
    p.add_argument("--limit", type=int, default=30)
    p.add_argument("--status")
    p.add_argument("--json", action="store_true")
    sub.add_parser("review")
    args = parser.parse_args(argv)
    out = args.output
    if args.command == "extract":
        print(json.dumps({"extracted": extract(args.game_root, out / "binary", args.wolvenkit)}))
    elif args.command == "serialize":
        if args.workers < 1:
            parser.error("--workers must be positive")
        result = serialize_tree(args.binary_root or out / "binary", out / "raw", args.workers)
        print(json.dumps(result))
        return int(bool(result["failures"]))
    elif args.command == "build":
        result = build(args.raw_root or out / "raw", out, args.annotations, args.binary_root or out / "binary", args.usage_root)
        print(json.dumps(result["summary"]))
        return int(bool(result["failures"]))
    elif args.command == "search":
        if args.limit < 0:
            parser.error("--limit must be nonnegative (0 means all)")
        result = search(out / "workspots.sqlite3", args.query, args.limit, args.status)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            for r in result:
                print(f"{r['depot_path']} [{r['review_status']}]\n  " + ", ".join(r["animations"][:8]))
    elif args.command == "review":
        review(read(out / "catalog.json"), out / "review.html")
        print(out / "review.html")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, sqlite3.Error, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
