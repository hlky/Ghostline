"""HTTP adapter for the local equipment gallery."""

from __future__ import annotations
import contextlib
import http.server
import json
import sys
import urllib.parse
import webbrowser
from pathlib import Path
from typing import Any

from item_common import (
    GALLERY_ROOT,
    ItemDatabaseError,
)
from item_catalog import (
    connect,
    count_variants,
    database_summary,
    query_variants,
)


class GalleryHandler(http.server.SimpleHTTPRequestHandler):
    database: Path
    output_root: Path

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(GALLERY_ROOT), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write(f"[item-gallery] {format % args}\n")

    def send_json(self, value: Any, status: int = 200) -> None:
        body = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/summary":
            with contextlib.closing(connect(self.database)) as connection:
                self.send_json(database_summary(connection))
            return
        if parsed.path == "/api/items":
            query = urllib.parse.parse_qs(parsed.query)
            query_text = query.get("q", [""])[0]
            slot = query.get("slot", [""])[0]
            frame = query.get("frame", [""])[0]
            tag = query.get("tag", [""])[0]
            rendered = query.get("rendered", [""])[0]
            limit = max(1, min(int(query.get("limit", ["48"])[0]), 500))
            offset = max(0, int(query.get("offset", ["0"])[0]))
            with contextlib.closing(connect(self.database)) as connection:
                items = query_variants(
                    connection,
                    query_text,
                    slot,
                    frame,
                    tag,
                    limit,
                    offset,
                    rendered,
                )
                total = count_variants(
                    connection, query_text, slot, frame, tag, rendered
                )
            for item in items:
                view_urls: dict[str, str] = {}
                for view_path in item.get("views", []):
                    resolved_view = Path(view_path).resolve()
                    try:
                        relative_view = resolved_view.relative_to(
                            self.output_root.resolve()
                        )
                    except ValueError:
                        continue
                    view_urls[resolved_view.stem] = (
                        "/images/"
                        + urllib.parse.quote(str(relative_view).replace("\\", "/"))
                    )
                item["view_urls"] = view_urls
                if item.get("hero_path"):
                    item["image_url"] = "/images/" + urllib.parse.quote(
                        str(Path(item["hero_path"]).resolve().relative_to(self.output_root.resolve())).replace(
                            "\\", "/"
                        )
                    )
            self.send_json(
                {
                    "items": items,
                    "total": total,
                    "limit": limit,
                    "offset": offset,
                }
            )
            return
        if parsed.path.startswith("/images/"):
            relative = urllib.parse.unquote(parsed.path.removeprefix("/images/"))
            target = (self.output_root / Path(relative)).resolve()
            try:
                target.relative_to(self.output_root.resolve())
            except ValueError:
                self.send_error(403)
                return
            if not target.is_file():
                self.send_error(404)
                return
            body = target.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

def serve(database: Path, output: Path, host: str, port: int, open_browser: bool) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise ItemDatabaseError("The item gallery only binds to a loopback host")
    if not database.is_file():
        raise ItemDatabaseError(f"Item database was not found: {database}")
    handler = type(
        "ConfiguredGalleryHandler",
        (GalleryHandler,),
        {"database": database.resolve(), "output_root": output.resolve()},
    )
    server = http.server.ThreadingHTTPServer((host, port), handler)
    address = f"http://{host}:{server.server_address[1]}"
    print(f"Item gallery: {address}")
    if open_browser:
        webbrowser.open(address)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
