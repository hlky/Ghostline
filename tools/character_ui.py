#!/usr/bin/env python3
"""Serve the local Ghostline character creator UI."""

from __future__ import annotations

import argparse
import ipaddress
import json
import mimetypes
import re
import shutil
import sys
import tempfile
import threading
import webbrowser
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlsplit

import character_builder
import character_asset_index
import character_full_preview


ROOT = Path(__file__).resolve().parents[1]
STATIC_ROOT = Path(__file__).with_name("character_ui")
DEFAULT_MANIFEST = ROOT / "characters/patch.character.json"
PREVIEW_ROOT = ROOT / "converted/characters"
ASSET_INDEX_PATH = ROOT / "converted/character-index/assets.json"
BUILD_LOCK = threading.Lock()


def clean_manifest(value: dict[str, Any]) -> dict[str, Any]:
    return {key: child for key, child in value.items() if not key.startswith("_")}


def player_frame_token(manifest: dict[str, Any]) -> str:
    return str(character_builder.frame_profile(manifest)["player_token"])


def catalog_assignment_support(
    manifest: dict[str, Any],
    support: dict[str, Any],
    manifest_category: str | None = None,
) -> dict[str, Any]:
    constrained = dict(support)
    constrained["reasons"] = list(support.get("reasons", []))
    if not constrained.get("supported"):
        return constrained
    catalog = character_builder.load_catalog(manifest)
    categories = catalog.get("categories", {})
    candidates = constrained.get("manifest_categories") or [
        constrained.get("manifest_category")
    ]
    valid_categories: list[str] = []
    for category_id in candidates:
        category = categories.get(category_id) if isinstance(categories, dict) else None
        config = category.get("indexed_override") if isinstance(category, dict) else None
        if (
            isinstance(config, dict)
            and str(config.get("frame_token", "")).casefold() == player_frame_token(manifest)
            and config.get("asset_slot") == constrained.get("asset_slot")
        ):
            valid_categories.append(category_id)
    constrained["manifest_categories"] = valid_categories
    if manifest_category is not None and manifest_category not in valid_categories:
        constrained["supported"] = False
        constrained["reasons"].append(
            f"the active character catalog does not support indexed {manifest_category} assignment"
        )
    elif not valid_categories:
        constrained["supported"] = False
        constrained["reasons"].append("the active character catalog has no compatible destination slot")
    else:
        constrained["manifest_category"] = manifest_category or valid_categories[0]
    return constrained


def editable_manifest(value: dict[str, Any]) -> dict[str, Any]:
    """Copy UI-editable values onto server-owned templates and build paths."""
    trusted = clean_manifest(character_builder.load_manifest(DEFAULT_MANIFEST))
    for key in ("id", "display_name", "namespace"):
        if key in value:
            trusted[key] = value[key]
    for section, keys in (
        ("tweak", ("record", "display_name", "affiliation", "voice_tag")),
        ("localization", ("secondary_key", "female_variant", "male_variant")),
    ):
        incoming = value.get(section)
        if isinstance(incoming, dict):
            for key in keys:
                if key in incoming:
                    trusted[section][key] = incoming[key]
    head = value.get("head")
    if isinstance(head, dict) and isinstance(head.get("shapes"), dict):
        trusted["head"]["shapes"] = {
            name: head["shapes"].get(name) for name in character_builder.SHAPE_NAMES
        }
    appearance = value.get("appearance")
    if isinstance(appearance, dict) and isinstance(appearance.get("selections"), dict):
        trusted["appearance"]["selections"] = dict(appearance["selections"])
    trusted["appearance"]["indexed_overrides"] = {}
    if isinstance(appearance, dict) and isinstance(appearance.get("indexed_overrides"), dict):
        catalog = character_builder.load_catalog(trusted)
        categories = catalog.get("categories", {})
        for category_id, override in appearance["indexed_overrides"].items():
            category = categories.get(category_id) if isinstance(categories, dict) else None
            if not isinstance(category, dict) or not isinstance(category.get("indexed_override"), dict):
                continue
            if not isinstance(override, dict):
                continue
            depot_path = override.get("depot_path")
            mesh_appearance = override.get("mesh_appearance")
            if isinstance(depot_path, str) and isinstance(mesh_appearance, str):
                trusted["appearance"]["indexed_overrides"][category_id] = {
                    "depot_path": depot_path,
                    "mesh_appearance": mesh_appearance,
                }
    return trusted


def validate_installed_overrides(manifest: dict[str, Any], character_id: str) -> None:
    overrides = manifest.get("appearance", {}).get("indexed_overrides", {})
    if not overrides:
        return
    if not ASSET_INDEX_PATH.is_file():
        raise character_builder.CharacterBuildError(
            "The installed-game asset index is required to validate indexed clothing"
        )
    index = character_asset_index.read_json(ASSET_INDEX_PATH)
    canonical: dict[str, Any] = {}
    for category_id, override in overrides.items():
        depot_path = override.get("depot_path") if isinstance(override, dict) else None
        mesh_appearance = override.get("mesh_appearance") if isinstance(override, dict) else None
        if not isinstance(depot_path, str) or not isinstance(mesh_appearance, str):
            raise character_builder.CharacterBuildError(
                f"Indexed override {category_id!r} is incomplete"
            )
        preview_id = character_asset_index.preview_cache_id(depot_path)
        output = PREVIEW_ROOT / character_id / "asset-previews" / preview_id
        preview = character_asset_index.prepare_mesh_preview(
            index,
            depot_path,
            output,
            character_asset_index.DEFAULT_WOLVENKIT,
            character_asset_index.DEFAULT_GAME,
            player_frame_token(manifest),
        )
        assignment = character_asset_index.canonical_indexed_override(
            preview["asset"],
            mesh_appearance,
            preview["mesh_appearances"],
            player_frame_token(manifest),
            category_id,
        )
        if assignment["manifest_category"] != category_id:
            raise character_builder.CharacterBuildError(
                f"Indexed mesh {depot_path} belongs to {assignment['manifest_category']!r}, not {category_id!r}"
            )
        canonical[category_id] = assignment["override"]
    manifest["appearance"]["indexed_overrides"] = canonical


def is_loopback_host(host: str) -> bool:
    if host.casefold() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def safe_id(value: Any) -> str:
    text = str(value or "")
    if not re.fullmatch(r"[a-z][a-z0-9_]{1,47}", text):
        raise character_builder.CharacterBuildError(
            "Character id must be 2-48 lowercase letters, digits, or underscores and start with a letter"
        )
    return text


def with_temp_manifest(manifest: dict[str, Any], callback: Any) -> Any:
    with tempfile.TemporaryDirectory(prefix="ghostline_character_ui_") as directory:
        path = Path(directory) / "character.json"
        character_builder.write_json(path, clean_manifest(manifest))
        return callback(path)


def preview_file_path(url_path: str) -> Path:
    path = unquote(urlsplit(url_path).path)
    prefix = "/preview/"
    if not path.startswith(prefix):
        raise character_builder.CharacterBuildError("Invalid preview path")
    parts = [part for part in path[len(prefix) :].split("/") if part]
    if len(parts) < 2:
        raise character_builder.CharacterBuildError("Preview path is incomplete")
    character_id = safe_id(parts[0])
    character_root = (PREVIEW_ROOT / character_id).resolve()
    target = character_root.joinpath(*parts[1:]).resolve()
    if target == character_root or character_root not in target.parents:
        raise character_builder.CharacterBuildError("Preview path escapes the character output")
    return target


class CharacterUIHandler(SimpleHTTPRequestHandler):
    server_version = "GhostlineCharacterUI/1"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(STATIC_ROOT), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        sys.stdout.write(f"character-ui: {format % args}\n")

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, value: Any, status: HTTPStatus = HTTPStatus.OK) -> None:
        payload = json.dumps(value, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0 or length > 2_000_000:
            raise character_builder.CharacterBuildError("Request body is missing or too large")
        value = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(value, dict):
            raise character_builder.CharacterBuildError("Expected a JSON object")
        return value

    def do_GET(self) -> None:
        route = urlsplit(self.path).path
        if route == "/api/bootstrap":
            manifest = character_builder.load_manifest(DEFAULT_MANIFEST)
            catalog = character_builder.load_catalog(manifest)
            report = character_builder.validate_manifest(manifest, catalog)
            character_id = safe_id(manifest.get("id"))
            preview_manifest = PREVIEW_ROOT / character_id / "preview" / "preview-manifest.json"
            full_preview_manifest = (
                PREVIEW_ROOT / character_id / "full-preview" / "preview-manifest.json"
            )
            asset_index = (
                character_asset_index.read_json(ASSET_INDEX_PATH)
                if ASSET_INDEX_PATH.is_file()
                else None
            )
            self.send_json(
                {
                    "manifest": clean_manifest(manifest),
                    "catalog": catalog,
                    "validation": report.as_dict(),
                    "output_base": str(PREVIEW_ROOT.resolve()),
                    "preview_url": (
                        f"/preview/{character_id}/preview/preview-manifest.json"
                        if preview_manifest.is_file()
                        else None
                    ),
                    "full_preview_url": (
                        f"/preview/{character_id}/full-preview/preview-manifest.json"
                        if full_preview_manifest.is_file()
                        else None
                    ),
                    "asset_index": {
                        "available": asset_index is not None,
                        "summary": asset_index.get("summary", {}) if asset_index else {},
                    },
                    "frame_profile": {
                        **character_builder.frame_profile(manifest),
                        "preview_morphtargets": list(
                            character_builder.frame_profile(manifest)["preview_morphtargets"]
                        ),
                        "unresolved_documented_values": list(
                            character_builder.frame_profile(manifest)[
                                "unresolved_documented_values"
                            ]
                        ),
                    },
                }
            )
            return
        if route == "/api/assets":
            if not ASSET_INDEX_PATH.is_file():
                self.send_json(
                    {"ok": False, "error": "Asset index has not been generated"},
                    HTTPStatus.NOT_FOUND,
                )
                return
            parameters = parse_qs(urlsplit(self.path).query)
            value = character_asset_index.read_json(ASSET_INDEX_PATH)
            try:
                limit = int(parameters.get("limit", ["80"])[0])
            except ValueError:
                limit = 80
            assets = character_asset_index.search_assets(
                value,
                parameters.get("query", [""])[0],
                parameters.get("category", [""])[0],
                parameters.get("slot", [""])[0],
                parameters.get("frame", [""])[0],
                limit,
            )
            self.send_json({"ok": True, "summary": value.get("summary", {}), "assets": assets})
            return
        if route.startswith("/preview/"):
            try:
                target = preview_file_path(route)
                if not target.is_file():
                    self.send_error(HTTPStatus.NOT_FOUND, "Preview file not found")
                    return
                content_type = "model/gltf-binary" if target.suffix == ".glb" else mimetypes.guess_type(target)[0]
                size = target.stat().st_size
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", content_type or "application/octet-stream")
                self.send_header("Content-Length", str(size))
                self.end_headers()
                with target.open("rb") as stream:
                    shutil.copyfileobj(stream, self.wfile)
            except (character_builder.CharacterBuildError, OSError) as exc:
                self.send_error(HTTPStatus.BAD_REQUEST, str(exc))
            return
        if route in {"/", "/index.html"}:
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        try:
            request = self.read_json()
            posted_manifest = request.get("manifest")
            if not isinstance(posted_manifest, dict):
                raise character_builder.CharacterBuildError("Request is missing manifest")
            manifest = editable_manifest(posted_manifest)
            character_id = safe_id(manifest.get("id"))

            if self.path == "/api/validate":
                manifest["_manifest_path"] = "<character-ui>"
                with BUILD_LOCK:
                    validate_installed_overrides(manifest, character_id)
                    report = character_builder.validate_manifest(
                        manifest, character_builder.load_catalog(manifest)
                    )
                self.send_json(report.as_dict(), HTTPStatus.OK if report.ok else HTTPStatus.BAD_REQUEST)
                return

            if self.path == "/api/generate":
                output = ROOT / "converted/characters" / character_id
                with BUILD_LOCK:
                    validate_installed_overrides(manifest, character_id)
                    result = with_temp_manifest(
                        manifest, lambda path: character_builder.generate(path, output)
                    )
                self.send_json(result)
                return

            if self.path in {"/api/head/plan", "/api/head/build"}:
                workspace = ROOT / "converted/characters" / character_id / "head-build"
                dry_run = self.path.endswith("/plan")
                with BUILD_LOCK:
                    result = with_temp_manifest(
                        manifest,
                        lambda path: character_builder.head_build(
                            path,
                            workspace,
                            {},
                            character_builder.DEFAULT_WOLVENKIT,
                            character_builder.DEFAULT_BLENDER,
                            character_builder.DEFAULT_GAME,
                            dry_run,
                        ),
                    )
                self.send_json(result, HTTPStatus.OK if result["ok"] else HTTPStatus.BAD_REQUEST)
                return

            if self.path == "/api/preview/prepare":
                output = PREVIEW_ROOT / character_id / "preview"
                include_all = bool(request.get("include_all_head_parts", False))
                with BUILD_LOCK:
                    result = with_temp_manifest(
                        manifest,
                        lambda path: character_builder.prepare_head_preview(
                            path,
                            output,
                            character_builder.DEFAULT_WOLVENKIT,
                            character_builder.DEFAULT_GAME,
                            include_all,
                        ),
                    )
                result["preview_url"] = f"/preview/{character_id}/preview/preview-manifest.json"
                self.send_json(result)
                return

            if self.path == "/api/preview/full":
                character_root = PREVIEW_ROOT / character_id
                head_output = character_root / "preview"
                full_output = character_root / "full-preview"
                with BUILD_LOCK:
                    validate_installed_overrides(manifest, character_id)
                    generation = with_temp_manifest(
                        manifest,
                        lambda path: character_builder.generate(path, character_root),
                    )
                    with_temp_manifest(
                        manifest,
                        lambda path: character_builder.prepare_head_preview(
                            path,
                            head_output,
                            character_builder.DEFAULT_WOLVENKIT,
                            character_builder.DEFAULT_GAME,
                            True,
                        ),
                    )
                    app_path = character_builder.output_path(
                        character_root, manifest["outputs"]["appearance_raw"]
                    )
                    app_document = character_builder.read_json(app_path)
                    result = character_full_preview.prepare_full_preview(
                        manifest,
                        app_document,
                        character_root,
                        head_output / "preview-manifest.json",
                        full_output,
                        character_builder.DEFAULT_WOLVENKIT,
                        character_builder.DEFAULT_GAME,
                    )
                result["generation_validation"] = generation["validation"]
                result["preview_url"] = (
                    f"/preview/{character_id}/full-preview/preview-manifest.json"
                )
                self.send_json(result)
                return

            if self.path == "/api/assets/index":
                with BUILD_LOCK:
                    index = character_asset_index.build_asset_index(
                        character_asset_index.DEFAULT_GAME,
                        character_asset_index.DEFAULT_WOLVENKIT,
                    )
                    character_asset_index.write_json(ASSET_INDEX_PATH, index)
                self.send_json({"ok": True, "summary": index["summary"]})
                return

            if self.path == "/api/assets/preview":
                depot_path = request.get("depot_path")
                if not isinstance(depot_path, str) or not depot_path:
                    raise character_builder.CharacterBuildError("Asset preview requires a depot_path")
                if not ASSET_INDEX_PATH.is_file():
                    raise character_builder.CharacterBuildError("Asset index has not been generated")
                index = character_asset_index.read_json(ASSET_INDEX_PATH)
                preview_id = character_asset_index.preview_cache_id(depot_path)
                output = PREVIEW_ROOT / character_id / "asset-previews" / preview_id
                with BUILD_LOCK:
                    result = character_asset_index.prepare_mesh_preview(
                        index,
                        depot_path,
                        output,
                        character_asset_index.DEFAULT_WOLVENKIT,
                        character_asset_index.DEFAULT_GAME,
                        player_frame_token(manifest),
                    )
                result["assignment"] = catalog_assignment_support(
                    manifest, result["assignment"]
                )
                result["preview_url"] = (
                    f"/preview/{character_id}/asset-previews/{preview_id}/preview-manifest.json"
                )
                self.send_json(result)
                return

            if self.path == "/api/assets/assign":
                depot_path = request.get("depot_path")
                mesh_appearance = request.get("mesh_appearance")
                manifest_category = request.get("manifest_category")
                if not isinstance(depot_path, str) or not depot_path:
                    raise character_builder.CharacterBuildError("Asset assignment requires a depot_path")
                if not isinstance(mesh_appearance, str) or not mesh_appearance:
                    raise character_builder.CharacterBuildError(
                        "Asset assignment requires a mesh_appearance"
                    )
                if manifest_category is not None and not isinstance(manifest_category, str):
                    raise character_builder.CharacterBuildError(
                        "Asset assignment manifest_category must be a string"
                    )
                if not ASSET_INDEX_PATH.is_file():
                    raise character_builder.CharacterBuildError("Asset index has not been generated")
                index = character_asset_index.read_json(ASSET_INDEX_PATH)
                preview_id = character_asset_index.preview_cache_id(depot_path)
                output = PREVIEW_ROOT / character_id / "asset-previews" / preview_id
                with BUILD_LOCK:
                    preview = character_asset_index.prepare_mesh_preview(
                        index,
                        depot_path,
                        output,
                        character_asset_index.DEFAULT_WOLVENKIT,
                        character_asset_index.DEFAULT_GAME,
                        player_frame_token(manifest),
                    )
                    assignment = character_asset_index.canonical_indexed_override(
                        preview["asset"],
                        mesh_appearance,
                        preview["mesh_appearances"],
                        player_frame_token(manifest),
                        manifest_category,
                    )
                    constrained = catalog_assignment_support(
                        manifest,
                        character_asset_index.selection_support(
                            preview["asset"], player_frame_token(manifest)
                        ),
                        assignment["manifest_category"],
                    )
                    if not constrained["supported"]:
                        raise character_asset_index.CharacterAssetIndexError(
                            "Asset cannot be assigned: " + "; ".join(constrained["reasons"])
                        )
                catalog = character_builder.load_catalog(manifest)
                category = catalog["categories"][assignment["manifest_category"]]
                assignment["anchor_option"] = category["indexed_override"]["anchor_option"]
                assignment["asset"] = preview["asset"]
                assignment["warnings"] = preview["warnings"]
                self.send_json({"ok": True, **assignment})
                return

            self.send_json({"error": "Unknown API route"}, HTTPStatus.NOT_FOUND)
        except (
            character_builder.CharacterBuildError,
            character_asset_index.CharacterAssetIndexError,
            character_full_preview.CharacterFullPreviewError,
            json.JSONDecodeError,
            OSError,
        ) as exc:
            self.send_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--open", action="store_true", dest="open_browser")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Trusted character manifest/profile to edit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    global DEFAULT_MANIFEST
    args = build_parser().parse_args(argv)
    DEFAULT_MANIFEST = args.manifest.resolve()
    if not DEFAULT_MANIFEST.is_file():
        print(f"error: character manifest not found: {DEFAULT_MANIFEST}", file=sys.stderr)
        return 1
    if not STATIC_ROOT.joinpath("index.html").is_file():
        print(f"error: UI assets not found under {STATIC_ROOT}", file=sys.stderr)
        return 1
    if not is_loopback_host(args.host):
        print("error: the character creator may only bind to a loopback host", file=sys.stderr)
        return 1
    server = ThreadingHTTPServer((args.host, args.port), CharacterUIHandler)
    url = f"http://{args.host}:{server.server_port}/"
    print(f"Ghostline character creator: {url}")
    print("Generated files are isolated under converted/characters.")
    if args.open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
