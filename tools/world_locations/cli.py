"""Command-line surface for indexing, planning, capture, review, and export."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import sqlite3
import sys
from typing import Any, Iterable, Mapping

from artifact_io import publish_json_artifacts

from .capture import CaptureController
from .capture_evidence import assess_capture, capture_rows, check_report_destinations
from .config import DEFAULT_CONFIG, load_config, output_paths, resolve_project_path
from .database import (
    connect,
    connect_readonly,
    requeue_places,
    require_idle,
    status_counts,
    utc_now,
)
from .extract import index_sectors
from .planning import plan_locations
from .protocol import atomic_write_json


class CliError(RuntimeError):
    pass


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
        require_idle(connection)
        _materialize(paths, config)
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
    connection = _connection(args, paths)
    try:
        require_idle(connection)
        _materialize(paths, config)
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
        selection = {}
        if args.location_id:
            selection["location_ids"] = args.location_id
        if args.category:
            selection["categories"] = args.category
        return controller.run(limit=args.limit, **selection)
    finally:
        connection.close()


def command_status(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    connection = connect_readonly(paths["database"])
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
    if not paths["database"].is_file():
        raise CliError(f"World location database does not exist: {paths['database']}")
    connection = _connection(args, paths)
    try:
        count = requeue_places(
            connection,
            location_ids=args.location_id,
            failure_codes=args.failure_code,
            categories=args.category,
            recapture=args.recapture,
        )
        return {"requeued": count}
    finally:
        connection.close()


def command_export(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    name = _report_name(args.name)
    connection = connect_readonly(paths["database"])
    try:
        rows = capture_rows(connection)
        exported: list[dict[str, Any]] = []
        rejected: list[dict[str, Any]] = []
        for row in rows:
            assessment = assess_capture(row)
            errors = (
                assessment["integrity_errors"]
                if args.include_unpublishable
                else assessment["blockers"]
            )
            if errors:
                rejected.append(
                    {
                        "location_id": row["location_id"],
                        "capture_id": row["capture_id"],
                        "errors": errors,
                    }
                )
                continue
            value = dict(row)
            sidecar = assessment["sidecar"]
            actual = sidecar.get("actual_pose", {})
            for axis in ("x", "y", "z", "yaw", "pitch", "roll"):
                value[f"actual_{axis}"] = (
                    actual.get(axis) if isinstance(actual, dict) else None
                )
            value["actual_fov"] = sidecar.get("actual_fov")
            value["capture_planned_pose"] = sidecar.get(
                "planned_pose", sidecar.get("requested_pose")
            )
            value["effective_pose"] = sidecar.get("effective_pose")
            value["capture_profile"] = sidecar.get("capture_profile")
            value["game_profile"] = sidecar.get("game_profile", row.get("game_profile"))
            value["capture_location_metadata"] = sidecar.get("location_metadata", {})
            value["publishable"] = int(assessment["publishable"])
            value["publication_blockers"] = assessment["blockers"]
            value["current_capture"] = assessment["current"]
            value["validation"] = assessment["validation"]
            value.pop("validation_json", None)
            value["provenance"] = json.loads(value.pop("provenance_json"))
            anchor_metadata = json.loads(value.pop("anchor_metadata_json") or "{}")
            value["anchor_tags"] = str(value.get("anchor_tags") or "").split()
            value["anchor_roles"] = [
                str(role) for role in anchor_metadata.get("anchor_roles", [])
            ]
            exported.append(value)
        json_path = paths["exports"] / (name + ".json")
        jsonl_path = paths["exports"] / (name + ".jsonl")
        report_path = paths["reports"] / (name + "-export-report.json")
        check_report_destinations(connection, (json_path, jsonl_path, report_path))
        publish_json_artifacts(
            {
                json_path: {
                    "schema_version": 1,
                    "generated_at": utc_now(),
                    "count": len(exported),
                    "places": exported,
                },
                report_path: {
                    "exported": len(exported),
                    "rejected": rejected,
                    "json": str(json_path),
                    "jsonl": str(jsonl_path),
                },
            },
            binary_artifacts={
                jsonl_path: "".join(
                    json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n"
                    for value in exported
                ).encode("utf-8")
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


def command_review(
    args: argparse.Namespace, _config: dict[str, Any], paths: Mapping[str, Path]
) -> dict[str, Any]:
    from .review import build_review

    connection = connect_readonly(paths["database"])
    try:
        return build_review(
            connection,
            args.output or paths["reports"] / "capture-review.html",
            limit=args.limit,
            categories=args.category,
            location_ids=args.location_id,
            verify_files=args.verify_files,
        )
    finally:
        connection.close()


def _positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def _nonnegative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be zero or a positive integer")
    return number


def _report_name(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}", value):
        raise ValueError(
            "Report name must contain only letters, digits, hyphens or underscores"
        )
    return value


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
    capture.add_argument("--limit", type=_positive_int)
    capture.add_argument(
        "--location-id", action="append", help="Capture only these pending location IDs"
    )
    capture.add_argument(
        "--category", action="append", help="Capture only these anchor categories"
    )
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
    retry.add_argument(
        "--recapture",
        action="store_true",
        help="Requeue captured views selected by explicit location IDs",
    )
    retry.set_defaults(handler=command_retry)

    export = commands.add_parser(
        "export", help="Verify and export JSON plus JSONL manifests"
    )
    export.add_argument("--name", default="world-locations")
    export.add_argument("--include-unpublishable", action="store_true")
    export.set_defaults(handler=command_export)

    review = commands.add_parser(
        "review",
        help="Build a visual capture and failure review page without changing the database",
    )
    review.add_argument("--output", type=Path)
    review.add_argument(
        "--limit",
        type=_nonnegative_int,
        default=300,
        help="Maximum locations to review; 0 includes all",
    )
    review.add_argument("--category", action="append")
    review.add_argument("--location-id", action="append")
    review.add_argument(
        "--verify-files",
        action="store_true",
        help="Also verify full image hashes; may read many gigabytes",
    )
    review.set_defaults(handler=command_review)

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
