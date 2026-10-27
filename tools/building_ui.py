#!/usr/bin/env python3
"""Serve Ghostline's local parametric building editor on loopback."""
from __future__ import annotations

import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import subprocess
import threading
from urllib.parse import unquote, urlsplit, parse_qs
import uuid
import zipfile

from artifact_io import atomic_write_json
from building_builder import BuildingError, CACHE, PROJECT, ROOT, compile_layout, export_project, kits, number

UI = ROOT / "tools/building_ui"
EXPORT_LOCK = threading.Lock()


class BuildingHandler(BaseHTTPRequestHandler):
    server_version = "GhostlineBuilding/0.1"

    def log_message(self, format, *args):
        if args and str(args[0]).startswith(("POST", "GET /api")):
            super().log_message(format, *args)

    def send_data(self, content, kind="application/json", status=200):
        if not isinstance(content, bytes):
            content = json.dumps(content, allow_nan=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)

    def local_request(self):
        expected = f"127.0.0.1:{self.server.server_port}"
        host = self.headers.get("Host", "")
        if host not in (expected, f"localhost:{self.server.server_port}"):
            raise BuildingError("Use the local editor address")
        origin = self.headers.get("Origin")
        if origin and origin not in ("http://" + expected, f"http://localhost:{self.server.server_port}"):
            raise BuildingError("Requests must come from the local editor")

    def serve_file(self, root, relative, *, download=False):
        path = (root / unquote(relative)).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            self.send_data({"error": "File not found"}, status=404)
            return
        kind = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        if path.suffix == ".js":
            kind = "text/javascript"
        if path.suffix == ".glb":
            kind = "model/gltf-binary"
        if download:
            kind = "application/zip"
        self.send_data(path.read_bytes(), kind)

    def do_GET(self):
        try:
            self.local_request()
            path = urlsplit(self.path).path
            if path == "/api/library":
                from building_library import search
                values = parse_qs(urlsplit(self.path).query)
                offset = int(values.get("offset", [0])[0])
                if not 0 <= offset <= 100000:
                    raise BuildingError("Invalid library page")
                self.send_data(search(query=values.get("q", [""])[0][:200], family=values.get("family", [""])[0],
                                      role=values.get("role", [""])[0], offset=offset))
            elif path == "/api/library-families":
                from building_library import catalog
                library = catalog()
                self.send_data({"families": library["families"], "counts": library["counts"]})
            elif path.startswith("/library-assets/"):
                from building_library import CACHE as LIBRARY_CACHE, asset
                identity = path.removeprefix("/library-assets/").removesuffix(".glb")
                asset(identity)
                self.serve_file(LIBRARY_CACHE / "assets", identity + ".glb")
            elif path == "/api/project":
                from building_library import catalog
                library = catalog()
                layout = json.loads((PROJECT / "buildings/workshop.building.json").read_bytes())
                files = [{"id": p.name.removesuffix(".building.json"), "name": json.loads(p.read_bytes()).get("name", p.stem)}
                         for p in sorted((PROJECT / "buildings").glob("*.building.json"))]
                self.send_data({"scene": compile_layout(layout), "files": files, "kits": kits(),
                                "library_summary": {"families": len(library["families"]), "prepared": library["counts"].get("prepared", 0)},
                                "assets_ready": all((CACHE / "assets" / catalog["id"] / (key + ".glb")).is_file() for catalog in kits() for key in catalog["pieces"])})
            elif path.startswith("/api/layout/"):
                identity = path.removeprefix("/api/layout/")
                from building_builder import ID
                if not ID.fullmatch(identity):
                    raise BuildingError("Invalid layout id")
                self.send_data(compile_layout(json.loads((PROJECT / "buildings" / (identity + ".building.json")).read_bytes())))
            elif path.startswith("/assets/"):
                self.serve_file(CACHE / "assets", path.removeprefix("/assets/"))
            elif path.startswith("/exports/"):
                self.serve_file(CACHE / "exports", path.removeprefix("/exports/"), download=True)
            elif path.startswith("/vendor/three/"):
                root = UI / "node_modules/three"
                if not root.is_dir():
                    root = ROOT / "tools/character_ui/node_modules/three"
                self.serve_file(root, path.removeprefix("/vendor/three/"))
            else:
                # The React bundle is built locally; API and game-asset routes
                # keep their existing origin and compiler ownership.
                dist = UI / "dist"
                if not (dist / "index.html").is_file():
                    self.send_data({"error": "Build the editor first: npm run build --prefix tools/building_ui"}, status=503)
                else:
                    self.serve_file(dist, path.lstrip("/") or "index.html")
        except (BuildingError, OSError, ValueError) as error:
            self.send_data({"error": str(error)}, status=400)

    def do_POST(self):
        try:
            self.local_request()
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                raise BuildingError("Send the layout as JSON")
            length = int(self.headers.get("Content-Length", 0))
            if not 0 < length <= 512_000:
                raise BuildingError("Layout request is empty or too large")
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                raise BuildingError("Expected a layout request")
            path = urlsplit(self.path).path
            scene = compile_layout(body.get("layout"), reconcile=body.get("reconcile") is True)
            if path == "/api/compile":
                self.send_data(scene)
            elif path == "/api/route":
                from building_navigation import route
                points = []
                for key in ("start", "end"):
                    point = body.get(key)
                    if not isinstance(point, list) or len(point) != 3:
                        raise BuildingError("Route endpoints must be local X/Y/Z triples")
                    points.append([number(value, key, -100, 100) for value in point])
                self.send_data(route(scene["navigation"], *points))
            elif path == "/api/save":
                target = PROJECT / "buildings" / (scene["layout"]["id"] + ".building.json")
                atomic_write_json(target, scene["layout"])
                self.send_data({"path": str(target.relative_to(ROOT)), "scene": scene})
            elif path == "/api/export":
                identity = uuid.uuid4().hex[:12]
                output = CACHE / "exports" / identity
                with EXPORT_LOCK:
                    export_project(scene, output, serialize=True)
                archive = CACHE / "exports" / (identity + ".zip")
                with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as handle:
                    for source in sorted(output.rglob("*")):
                        if source.is_file() and "generated" not in source.relative_to(output).parts:
                            handle.write(source, source.relative_to(output))
                self.send_data({"url": "/exports/" + archive.name, "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                                "project": str(output.relative_to(ROOT)), "stats": scene["stats"]})
            else:
                self.send_data({"error": "Unknown editor action"}, status=404)
        except (BuildingError, OSError, ValueError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
            details = str(error)
            if isinstance(error, subprocess.CalledProcessError):
                details += "\n" + str(error.stderr or error.stdout or "See the editor terminal for serializer output")[-3000:]
            self.send_data({"error": details}, status=422)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8792)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), BuildingHandler)
    print(f"Ghostline Building Lab: http://127.0.0.1:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
