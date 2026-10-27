#!/usr/bin/env python3
"""Build and serve a source-bound local workspot caption review workspace."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import threading
from urllib.parse import urlsplit

from artifact_io import atomic_write_json
from workspot_catalog import ROOT, DEFAULT_OUTPUT, digest, read

DEFAULT_REVIEWS = ROOT / "reference/workspots/caption-reviews.json"
DECISIONS = {"unreviewed", "approved", "needs_fix", "rejected"}


def load_captions(output):
    rows = {}
    catalog = {r["depot_path"]: r for r in read(output / "catalog.json")["workspots"]}
    for line in (output / "caption-results/captions.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["status"] != "captioned":
            continue
        key = row["id"]
        if not re.fullmatch(r"[a-f0-9]{20}", key):
            raise ValueError(f"Invalid clip ID: {key}")
        for name, expected in row["input"]["media_sha256"].items():
            if name not in {"preview.mp4", "contact.png"} or digest(output / "previews" / key / name) != expected:
                raise ValueError(f"Media changed: {key}/{name}")
        for spot in row["input"]["context"]["workspots"]:
            source = catalog[spot["workspot_path"]]["source"]
            if (source["binary_sha256"] or source["raw_sha256"]) != spot["source_sha256"]:
                raise ValueError(f"Workspot context changed: {spot['workspot_path']}")
        rows[key] = row
    return rows


def build(output):
    rows = load_captions(output)
    template = Path(__file__).with_suffix(".html").read_text(encoding="utf-8")
    payload = {"clips": list(rows.values())}
    data = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    target = output / "caption-results/review.html"
    if len(rows) > 200:
        target.with_name("review-data.json").write_text(data, encoding="utf-8")
        data = json.dumps({"clips": [], "data_url": "review-data.json"})
    target.write_text(template.replace("__CAPTION_DATA__", data), encoding="utf-8")
    return rows, target


class ReviewStore:
    def __init__(self, path, captions, output):
        self.path, self.captions, self.output = path, captions, output
        self.lock = threading.Lock()

    def read(self):
        return read(self.path) if self.path.exists() else {"schema_version": 1, "reviews": {}}

    def save(self, key, value):
        row = self.captions.get(key)
        if row is None or value.get("input_identity") != row["input_identity"]:
            raise ValueError("Caption changed; reload before reviewing")
        if value.get("decision") not in DECISIONS:
            raise ValueError("Unknown review decision")
        for field in ("notes", "summary"):
            if not isinstance(value.get(field, ""), str) or len(value.get(field, "")) > 20000:
                raise ValueError(f"Invalid {field}")
        for name, expected in row["input"]["media_sha256"].items():
            if digest(self.output / "previews" / key / name) != expected:
                raise ValueError("Preview changed; rebuild before reviewing")
        record = {"id": key, "input_identity": row["input_identity"],
                  "decision": value["decision"], "notes": value.get("notes", ""),
                  "summary": value.get("summary", ""), "media_sha256": row["input"]["media_sha256"],
                  "workspot_sources": [{"path": s["workspot_path"], "sha256": s["source_sha256"]} for s in row["input"]["context"]["workspots"]],
                  "reviewed_at": datetime.now(timezone.utc).isoformat(),
                  "scope": "Caption evidence and wording; not engine runtime verification"}
        with self.lock:
            data = self.read()
            data["reviews"][key] = record
            atomic_write_json(self.path, data)
        return record


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory, store, **kwargs):
        self.store = store
        super().__init__(*args, directory=str(directory), **kwargs)

    def send_json(self, status, data):
        payload = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if urlsplit(self.path).path == "/api/caption-reviews":
            self.send_json(200, self.store.read())
        else:
            super().do_GET()

    def do_POST(self):
        match = re.fullmatch(r"/api/caption-reviews/([a-f0-9]{20})", urlsplit(self.path).path)
        origin = self.headers.get("Origin")
        if origin and origin != f"http://127.0.0.1:{self.server.server_port}":
            self.send_json(403, {"error": "Use the local review page"})
            return
        if not match or self.headers.get_content_type() != "application/json":
            self.send_json(400, {"error": "Invalid review request"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 65536:
                raise ValueError("Invalid request size")
            value = json.loads(self.rfile.read(size))
            if not isinstance(value, dict):
                raise ValueError("Review must be an object")
            self.send_json(200, self.store.save(match[1], value))
        except (ValueError, KeyError) as error:
            self.send_json(409, {"error": str(error)})


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--reviews", type=Path, default=DEFAULT_REVIEWS)
    p.add_argument("--port", type=int, default=8877)
    p.add_argument("--build-only", action="store_true")
    args = p.parse_args(argv)
    output = args.output.resolve()
    captions, page = build(output)
    print(json.dumps({"clips": len(captions), "page": str(page), "reviews": str(args.reviews.resolve())}), flush=True)
    if not args.build_only:
        store = ReviewStore(args.reviews.resolve(), captions, output)
        server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=output, store=store))
        print(f"http://127.0.0.1:{args.port}/caption-results/review.html", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
