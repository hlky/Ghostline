"""Command-line surface for indexing, planning, capture, review, and export."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import sys
from typing import Any, Iterable, Mapping
import uuid

from .capture import CaptureController
from .config import DEFAULT_CONFIG, load_config, output_paths, resolve_project_path
from .database import connect, status_counts, transaction, utc_now
from .extract import index_sectors
from .planning import plan_locations
from .protocol import atomic_write_json


class CliError(RuntimeError):
    pass


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(text)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def _print(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def _resolved_paths(
    args: argparse.Namespace, config: dict[str, Any]
) -> dict[str, Path]:
    paths = output_paths(config)
    if getattr(args, "database", None):
        paths["database"] = Path(args.database).resolve()
    return paths


def _materialize(paths: Mapping[str, Path], config: Mapping[str, Any]) -> None:
    for path in (
        paths["root"],
        paths["runtime"],
        paths["captures"],
        paths["reports"],
        paths["exports"],
    ):
        path.mkdir(parents=True, exist_ok=True)
    materialized = {
        key: value for key, value in config.items() if not key.startswith("_")
    }
    atomic_write_json(paths["root"] / "capture-config.json", materialized)


def _connection(
    args: argparse.Namespace, paths: Mapping[str, Path]
) -> sqlite3.Connection:
    return connect(paths["database"])


def command_index(
    args: argparse.Namespace, config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, config)
    source_root = (
        Path(args.source_root).resolve()
        if args.source_root
        else resolve_project_path(config["source_root"])
    )
    connection = _connection(args, paths)

    def progress(current: int, total: int, relative: str, status: str) -> None:
        if (
            status == "error"
            or current == total
            or current % int(args.progress_every) == 0
        ):
            print(
                f"[{current}/{total}] {status} {relative}", file=sys.stderr, flush=True
            )

    try:
        return index_sectors(
            connection,
            source_root,
            config,
            content_hash=args.content_hash,
            continue_on_error=not args.fail_fast,
            limit=args.limit,
            progress=progress,
        )
    finally:
        connection.close()


def command_plan(
    args: argparse.Namespace, config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, config)
    connection = _connection(args, paths)
    try:
        return plan_locations(connection, config)
    finally:
        connection.close()


def _runtime_from_descriptor(paths: Mapping[str, Path]) -> Path:
    descriptor = paths["runtime"] / "cet-runtime.json"
    if descriptor.is_file():
        value = json.loads(descriptor.read_text(encoding="utf-8"))
        candidate = Path(value["runtime_path"])
        if candidate.is_dir():
            return candidate.resolve()
    return paths["runtime"]


def command_capture(
    args: argparse.Namespace, config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, config)
    runtime = (
        Path(args.runtime).resolve()
        if args.runtime
        else _runtime_from_descriptor(paths)
    )
    connection = _connection(args, paths)
    try:
        controller = CaptureController(
            connection,
            config,
            runtime_root=runtime,
            captures_root=paths["captures"],
            config_root=Path(config["_config_path"]).parent,
            game_profile=args.game_profile,
        )
        return controller.run(limit=args.limit)
    finally:
        connection.close()


def command_status(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    if not paths["database"].is_file():
        raise CliError(f"location database does not exist: {paths['database']}")
    connection = sqlite3.connect(
        f"file:{paths['database'].as_posix()}?mode=ro", uri=True
    )
    connection.row_factory = sqlite3.Row
    try:
        result = status_counts(connection)
        result["database"] = str(paths["database"])
        result["runtime"] = str(_runtime_from_descriptor(paths))
        failures = connection.execute(
            """SELECT failure_code,COUNT(*) AS count FROM places
               WHERE queue_status='failed' GROUP BY failure_code ORDER BY count DESC"""
        ).fetchall()
        result["failure_codes"] = {
            row["failure_code"] or "unknown": row["count"] for row in failures
        }
        return result
    finally:
        connection.close()


def command_retry(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, _config)
    connection = _connection(args, paths)
    clauses: list[str] = []
    parameters: list[Any] = []
    if args.location_id:
        clauses.append(
            "location_id IN ({})".format(",".join("?" for _ in args.location_id))
        )
        parameters.extend(args.location_id)
    if args.failure_code:
        clauses.append(
            "failure_code IN ({})".format(",".join("?" for _ in args.failure_code))
        )
        parameters.extend(args.failure_code)
    if args.category:
        clauses.append("category IN ({})".format(",".join("?" for _ in args.category)))
        parameters.extend(args.category)
    where = " AND ".join(clauses) if clauses else "queue_status='failed'"
    try:
        with transaction(connection):
            cursor = connection.execute(
                f"""UPDATE places SET queue_status='pending',failure_code=NULL,failure_detail=NULL,
                       publishable=0,updated_at=? WHERE ({where}) AND queue_status!='captured'
                       AND scope_status='in_scope'""",
                (utc_now(), *parameters),
            )
        return {"requeued": cursor.rowcount, "selection": where}
    finally:
        connection.close()


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _capture_integrity(row: Mapping[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for column, hash_column in (
        ("png_path", "image_sha256"),
        ("sidecar_path", "metadata_sha256"),
        ("thumbnail_path", "thumbnail_sha256"),
    ):
        path = Path(row[column])
        if not path.is_file():
            errors.append(f"missing {column}: {path}")
        elif _hash_file(path) != row[hash_column]:
            errors.append(f"hash mismatch for {column}: {path}")
    return not errors, errors


def command_export(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, _config)
    connection = _connection(args, paths)
    try:
        where = "1=1" if args.include_unpublishable else "p.publishable=1"
        rows = connection.execute(
            f"""SELECT p.*,c.capture_id,c.png_path,c.sidecar_path,c.thumbnail_path,c.width,c.height,
                       c.image_sha256,c.metadata_sha256,c.thumbnail_sha256,c.perceptual_hash,
                       c.captured_at,c.validation_status
                FROM places p JOIN captures c ON c.location_id=p.location_id
                WHERE {where} ORDER BY p.queue_order,p.location_id,c.captured_at"""
        ).fetchall()
        exported: list[dict[str, Any]] = []
        rejected: list[dict[str, Any]] = []
        for row in rows:
            valid, errors = _capture_integrity(row)
            if not valid:
                rejected.append(
                    {
                        "location_id": row["location_id"],
                        "capture_id": row["capture_id"],
                        "errors": errors,
                    }
                )
                continue
            value = dict(row)
            value["provenance"] = json.loads(value.pop("provenance_json"))
            exported.append(value)
        json_path = paths["exports"] / (args.name + ".json")
        jsonl_path = paths["exports"] / (args.name + ".jsonl")
        atomic_write_json(
            json_path,
            {
                "schema_version": 1,
                "generated_at": utc_now(),
                "count": len(exported),
                "places": exported,
            },
        )
        _write_text_atomic(
            jsonl_path,
            "".join(
                json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n"
                for value in exported
            ),
        )
        report_path = paths["reports"] / (args.name + "-export-report.json")
        atomic_write_json(
            report_path,
            {
                "exported": len(exported),
                "rejected": rejected,
                "json": str(json_path),
                "jsonl": str(jsonl_path),
            },
        )
        return {
            "exported": len(exported),
            "rejected": len(rejected),
            "json": str(json_path),
            "jsonl": str(jsonl_path),
            "report": str(report_path),
        }
    finally:
        connection.close()


def command_install_cet(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    _materialize(paths, _config)
    game_root = Path(args.game_root).resolve()
    cet_root = game_root / "bin" / "x64" / "plugins" / "cyber_engine_tweaks"
    if not cet_root.is_dir():
        raise CliError(f"Cyber Engine Tweaks directory not found: {cet_root}")
    source = Path(__file__).resolve().parents[1] / "world_location_capture_cet"
    destination = cet_root / "mods" / "world_location_capture"
    destination.mkdir(parents=True, exist_ok=True)
    for source_name, destination_name in (
        ("init.lua", "init.lua"),
        ("config.example.json", "config.json"),
    ):
        target = destination / destination_name
        if target.exists() and not args.force:
            if target.read_bytes() != (source / source_name).read_bytes():
                raise CliError(
                    f"refusing to overwrite modified CET file without --force: {target}"
                )
        shutil.copyfile(source / source_name, target)
    runtime = destination / "runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    descriptor = paths["runtime"] / "cet-runtime.json"
    atomic_write_json(
        descriptor,
        {
            "schema_version": 1,
            "runtime_path": str(runtime),
            "cet_mod_path": str(destination),
            "installed_at": utc_now(),
        },
    )
    return {
        "cet_mod": str(destination),
        "runtime": str(runtime),
        "descriptor": str(descriptor),
    }


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="world-location-capture",
        description="Build and capture a searchable Night City world-location database.",
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument(
        "--database", type=Path, help="Override the configured SQLite path"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    index = commands.add_parser(
        "index", help="Incrementally index changed serialized sectors"
    )
    index.add_argument("--source-root", type=Path)
    index.add_argument(
        "--content-hash",
        action="store_true",
        help="SHA-256 changed source sectors (adds an I/O pass)",
    )
    index.add_argument("--fail-fast", action="store_true")
    index.add_argument(
        "--limit",
        type=int,
        help="Development-only sector limit; disables stale pruning",
    )
    index.add_argument("--progress-every", type=int, default=100)
    index.set_defaults(handler=command_index)

    plan = commands.add_parser(
        "plan", help="Build deterministic object and road capture poses"
    )
    plan.set_defaults(handler=command_plan)

    capture = commands.add_parser(
        "capture", help="Run or resume the CET-driven capture queue"
    )
    capture.add_argument(
        "--runtime", type=Path, help="Installed CET mod runtime directory"
    )
    capture.add_argument("--game-profile", default="capture-free-roam")
    capture.add_argument("--limit", type=int)
    capture.set_defaults(handler=command_capture)

    status = commands.add_parser(
        "status", help="Report index, queue, review, and capture counts"
    )
    status.set_defaults(handler=command_status)

    retry = commands.add_parser(
        "retry", help="Requeue failures or selected location IDs"
    )
    retry.add_argument("--location-id", action="append")
    retry.add_argument("--failure-code", action="append")
    retry.add_argument("--category", action="append")
    retry.set_defaults(handler=command_retry)

    export = commands.add_parser(
        "export", help="Verify and export JSON plus JSONL manifests"
    )
    export.add_argument("--name", default="world-locations")
    export.add_argument("--include-unpublishable", action="store_true")
    export.set_defaults(handler=command_export)

    install = commands.add_parser(
        "install-cet", help="Install the controller bridge into an existing CET install"
    )
    install.add_argument("--game-root", type=Path, required=True)
    install.add_argument("--force", action="store_true")
    install.set_defaults(handler=command_install_cet)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        config = load_config(args.config)
        paths = _resolved_paths(args, config)
        result = args.handler(args, config, paths)
    except (CliError, OSError, RuntimeError, ValueError, sqlite3.Error) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    _print(result)
    return 0
