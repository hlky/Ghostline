"""Validated render-cache reuse and Blender batch orchestration."""

from __future__ import annotations
import collections
import concurrent.futures
import hashlib
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from item_common import (
    BLENDER_SCRIPT,
    ItemDatabaseError,
    ROOT,
    file_identity,
    read_json,
    sha1_text,
    write_json,
)
from item_catalog import (
    connect,
)
from item_assets import (
    prepare_material_exports_bulk,
)


def render_fingerprint(
    export: dict[str, Any],
    appearance: str,
    blender: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
) -> str:
    payload = {
        "asset": export["fingerprint"],
        "appearance": appearance,
        "blender": file_identity(blender),
        "script": file_identity(BLENDER_SCRIPT),
        "resolution": resolution,
        "samples": samples,
        "engine": engine,
        "views": views,
    }
    return sha1_text(json.dumps(payload, sort_keys=True))


def validate_render_report(
    report_path: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
    *,
    glb: str | Path | None = None,
    appearance: str | None = None,
) -> dict[str, Any]:
    """Accept a cache receipt only when every requested image still exists."""
    report = read_json(report_path)
    if not isinstance(report, dict):
        raise ItemDatabaseError(f"Render report must be an object: {report_path}")
    paths = report.get("images")
    if (
        not isinstance(paths, list)
        or not paths
        or any(not isinstance(p, str) for p in paths)
    ):
        raise ItemDatabaseError(f"Render report has no valid image list: {report_path}")
    images = [Path(p) for p in paths]
    if (
        report.get("resolution") != resolution
        or report.get("samples") != samples
        or report.get("engine") != engine
        or [p.stem for p in images] != views
        or not all(p.is_file() and p.stat().st_size > 0 for p in images)
        or not isinstance(report.get("glb"), str)
        or not isinstance(report.get("appearance"), str)
        or (glb is not None and Path(report["glb"]).resolve() != Path(glb).resolve())
        or (appearance is not None and report["appearance"] != appearance)
    ):
        raise ItemDatabaseError(
            f"Incomplete or incompatible render report: {report_path}"
        )
    return report


def reusable_render_report(
    report_path: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
    **identity: Any,
) -> bool:
    try:
        validate_render_report(
            report_path, resolution, samples, engine, views, **identity
        )
        return True
    except (ItemDatabaseError, OSError, ValueError):
        return False


def compatible_render_reports(
    render_root: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
) -> dict[tuple[str, str], Path]:
    compatible: dict[tuple[str, str], Path] = {}
    for report_path in render_root.glob("*/render-report.json"):
        try:
            report = validate_render_report(
                report_path, resolution, samples, engine, views
            )
            key = (
                os.path.normcase(str(Path(report["glb"]).resolve())),
                report["appearance"],
            )
            previous = compatible.get(key)
            if (
                previous is None
                or report_path.stat().st_mtime_ns > previous.stat().st_mtime_ns
            ):
                compatible[key] = report_path
        except (ItemDatabaseError, OSError, ValueError):
            continue
    return compatible


def render_variants(
    database: Path,
    index_path: Path,
    output: Path,
    ghostline_red: Path,
    red_schema: Path,
    blender: Path,
    game: Path,
    item: str,
    frame: str,
    slot: str,
    limit: int,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
    batch_size: int,
    workers: int,
    export_workers: int,
    reuse_compatible: bool,
    kraken: Path | None = None,
) -> dict[str, Any]:
    if not database.is_file():
        raise ItemDatabaseError(f"Item database was not found: {database}")
    if not index_path.is_file():
        raise ItemDatabaseError(f"Character asset index was not found: {index_path}")
    if not ghostline_red.is_file() or not red_schema.is_file() or not blender.is_file():
        raise ItemDatabaseError(
            "ghostline-red release binary, RED schema, and Blender 5.1 are required for rendering"
        )
    index = read_json(index_path)
    connection = connect(database)
    clauses: list[str] = []
    parameters: list[Any] = []
    if item:
        clauses.append("(i.record_id = ? OR i.record_id LIKE ?)")
        parameters.extend([item, f"%{item}%"])
    if frame:
        clauses.append("v.frame = ?")
        parameters.append(frame)
    if slot:
        clauses.append("i.slot = ?")
        parameters.append(slot)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    parameters.append(max(1, limit))
    candidates = connection.execute(
        f"""
        SELECT i.record_id, i.title, v.*
        FROM variants v JOIN items i ON i.record_id = v.item_id
        {where}
        ORDER BY i.title, v.frame LIMIT ?
        """,
        parameters,
    ).fetchall()
    export_requests = [
        (str(row["primary_mesh"]), str(row["mesh_appearance"])) for row in candidates
    ]
    print(
        f"Bulk-exporting {len(dict.fromkeys(export_requests))} unique mesh appearances",
        flush=True,
    )
    exports, export_errors = prepare_material_exports_bulk(
        index,
        export_requests,
        output / "asset-cache",
        ghostline_red,
        red_schema,
        game,
        export_workers,
        kraken=kraken,
    )
    rendered = 0
    reused = 0
    failures: list[dict[str, str]] = []
    prepared: list[dict[str, Any]] = []
    compatible = (
        compatible_render_reports(
            output / "renders",
            resolution,
            samples,
            engine,
            views,
        )
        if reuse_compatible
        else {}
    )
    for position, row in enumerate(candidates, start=1):
        variant = dict(row)
        started = time.monotonic()
        print(
            f"[{position}/{len(candidates)}] {variant['variant_id']} "
            f"({variant['mesh_appearance']})",
            flush=True,
        )
        try:
            export_key = (variant["primary_mesh"], variant["mesh_appearance"])
            if export_key in export_errors:
                raise ItemDatabaseError(export_errors[export_key])
            export = exports[export_key]
            fingerprint = render_fingerprint(
                export,
                variant["mesh_appearance"],
                blender,
                resolution,
                samples,
                engine,
                views,
            )
            render_root = output / "renders" / fingerprint
            report_path = render_root / "render-report.json"
            if reusable_render_report(
                report_path,
                resolution,
                samples,
                engine,
                views,
                glb=export["glb"],
                appearance=variant["mesh_appearance"],
            ):
                reused += 1
                state = "reused"
            elif compatible_report := compatible.get(
                (
                    os.path.normcase(str(Path(export["glb"]).resolve())),
                    variant["mesh_appearance"],
                )
            ):
                report_path = compatible_report
                render_root = compatible_report.parent
                fingerprint = render_root.name
                reused += 1
                state = "reused"
            else:
                render_root.mkdir(parents=True, exist_ok=True)
                # A failed new render must never inherit an invalid old receipt.
                report_path.unlink(missing_ok=True)
                state = "pending"
            prepared.append(
                {
                    "variant": variant,
                    "export": export,
                    "fingerprint": fingerprint,
                    "render_root": render_root,
                    "report_path": report_path,
                    "state": state,
                }
            )
            print(
                f"[{position}/{len(candidates)}] prepared ({state}) in "
                f"{time.monotonic() - started:.1f}s",
                flush=True,
            )
        except Exception as exc:
            failures.append({"variant_id": variant["variant_id"], "error": str(exc)})
            print(
                f"[{position}/{len(candidates)}] failed in "
                f"{time.monotonic() - started:.1f}s: {exc}",
                flush=True,
            )

    pending_by_fingerprint: dict[str, dict[str, Any]] = {}
    for entry in prepared:
        if entry["state"] == "pending":
            pending_by_fingerprint.setdefault(entry["fingerprint"], entry)
    pending = list(pending_by_fingerprint.values())
    duplicate_count = sum(entry["state"] == "pending" for entry in prepared) - len(
        pending
    )
    if duplicate_count:
        print(
            f"Reusing {duplicate_count} duplicate variant renders within this run",
            flush=True,
        )
    batch_size = max(1, batch_size)
    workers = max(1, workers)
    render_errors: dict[str, str] = {}
    with tempfile.TemporaryDirectory(dir=output, prefix=".render-batch.") as directory:
        batch_directory = Path(directory)
        batch_count = (len(pending) + batch_size - 1) // batch_size
        batches: list[dict[str, Any]] = []
        for batch_start in range(0, len(pending), batch_size):
            batch = pending[batch_start : batch_start + batch_size]
            batch_number = batch_start // batch_size + 1
            jobs_path = batch_directory / f"jobs-{batch_number}.json"
            batch_report = batch_directory / f"report-{batch_number}.json"
            write_json(
                jobs_path,
                {
                    "jobs": [
                        {
                            "glb": entry["export"]["glb"],
                            "appearance": entry["variant"]["mesh_appearance"],
                            "output": str(entry["render_root"]),
                            "native_pbr": bool(entry["export"].get("native_pbr")),
                        }
                        for entry in batch
                    ]
                },
            )
            command = [
                str(blender),
                "--background",
                "--python",
                str(BLENDER_SCRIPT),
                "--",
                "--jobs",
                str(jobs_path),
                "--batch-report",
                str(batch_report),
                "--resolution",
                str(resolution),
                "--samples",
                str(samples),
                "--engine",
                engine,
                "--views",
                ",".join(views),
            ]
            batches.append(
                {
                    "number": batch_number,
                    "entries": batch,
                    "command": command,
                    "report": batch_report,
                }
            )

        def run_batch(
            batch: dict[str, Any],
        ) -> tuple[dict[str, Any], subprocess.CompletedProcess[str]]:
            print(
                f"[batch {batch['number']}/{batch_count}] rendering "
                f"{len(batch['entries'])} variants",
                flush=True,
            )
            try:
                process = subprocess.Popen(
                    batch["command"],
                    cwd=ROOT,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    bufsize=1,
                )
            except OSError as error:
                return batch, subprocess.CompletedProcess(
                    batch["command"], -1, "", str(error)
                )
            diagnostic_lines: collections.deque[str] = collections.deque(maxlen=200)
            if process.stdout is None:
                raise ItemDatabaseError("Blender did not provide a progress stream")
            for line in process.stdout:
                diagnostic_lines.append(line)
                message = line.strip()
                if message.startswith(
                    (
                        "GHOSTLINE_BATCH_DONE",
                        "GHOSTLINE_BATCH_FAILED",
                        "GHOSTLINE_BATCH_OK",
                    )
                ):
                    print(
                        f"[batch {batch['number']}/{batch_count}] {message}", flush=True
                    )
            return_code = process.wait()
            completed = subprocess.CompletedProcess(
                args=batch["command"],
                returncode=return_code,
                stdout="".join(diagnostic_lines),
                stderr="",
            )
            return batch, completed

        print(
            f"Rendering {len(pending)} unique variants with "
            f"{min(workers, max(1, len(batches)))} Blender workers",
            flush=True,
        )
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(run_batch, batch): batch for batch in batches}
            for future in concurrent.futures.as_completed(futures):
                try:
                    batch, completed = future.result()
                except Exception as error:
                    batch = futures[future]
                    completed = subprocess.CompletedProcess(
                        batch["command"], -1, "", str(error)
                    )
                diagnostic = f"{completed.stdout}\n{completed.stderr}"[-8000:]
                print(
                    f"[batch {batch['number']}/{batch_count}] finished "
                    f"(exit {completed.returncode})",
                    flush=True,
                )
                try:
                    batch_receipt = read_json(batch["report"])
                    if (
                        not isinstance(batch_receipt, dict)
                        or not isinstance(batch_receipt.get("completed", []), list)
                        or not isinstance(batch_receipt.get("failures", []), list)
                    ):
                        batch_receipt = {}
                except (ItemDatabaseError, OSError, ValueError):
                    batch_receipt = {}
                completed_outputs = {
                    os.path.normcase(str(Path(path).resolve()))
                    for path in batch_receipt.get("completed", [])
                    if isinstance(path, str)
                }
                failed_outputs = {
                    os.path.normcase(str(Path(failure["output"]).resolve())): str(
                        failure.get("error", "Renderer reported failure")
                    )
                    for failure in batch_receipt.get("failures", [])
                    if isinstance(failure, dict)
                    and isinstance(failure.get("output"), str)
                }
                for entry in batch["entries"]:
                    report_path = entry["report_path"]
                    output_identity = os.path.normcase(
                        str(entry["render_root"].resolve())
                    )
                    if output_identity in failed_outputs:
                        render_errors[entry["fingerprint"]] = failed_outputs[
                            output_identity
                        ]
                    elif (
                        completed.returncode
                        and output_identity not in completed_outputs
                    ) or not report_path.is_file():
                        render_errors[entry["fingerprint"]] = (
                            f"Blender batch render failed ({completed.returncode}):\n"
                            f"{diagnostic}"
                        )

    for entry in prepared:
        try:
            if entry["fingerprint"] in render_errors:
                raise ItemDatabaseError(render_errors[entry["fingerprint"]])
            report = validate_render_report(
                entry["report_path"],
                resolution,
                samples,
                engine,
                views,
                glb=entry["export"]["glb"],
                appearance=entry["variant"]["mesh_appearance"],
            )
        except (ItemDatabaseError, OSError, ValueError) as exc:
            error = render_errors.get(entry["fingerprint"], str(exc))
            if entry["state"] == "pending" and entry["report_path"].is_file():
                # Retain failure evidence without allowing the next run to reuse it.
                failed_report = entry["report_path"].with_name(
                    f"render-report.failed-{time.time_ns()}.json"
                )
                entry["report_path"].replace(failed_report)
            failures.append(
                {"variant_id": entry["variant"]["variant_id"], "error": error}
            )
            connection.execute(
                "UPDATE renders SET status='failed', error=? WHERE variant_id=?",
                (error, entry["variant"]["variant_id"]),
            )
            if entry["state"] == "reused":
                reused -= 1
            continue
        if entry["state"] == "pending":
            rendered += 1
        image_paths = [str(Path(path).resolve()) for path in report["images"]]
        hero = next(
            (path for path in image_paths if Path(path).stem == "hero"),
            image_paths[0],
        )
        connection.execute(
            """
            INSERT INTO renders VALUES (?, ?, ?, ?, ?, ?, 'complete', '')
            ON CONFLICT(variant_id) DO UPDATE SET
                render_id=excluded.render_id,
                hero_path=excluded.hero_path,
                views_json=excluded.views_json,
                fingerprint=excluded.fingerprint,
                renderer=excluded.renderer,
                status=excluded.status,
                error=excluded.error
            """,
            (
                hashlib.sha1(
                    f"{entry['fingerprint']}:{entry['variant']['variant_id']}".encode()
                ).hexdigest(),
                entry["variant"]["variant_id"],
                hero,
                json.dumps(image_paths),
                entry["fingerprint"],
                f"Blender {engine}",
            ),
        )
    connection.commit()
    connection.close()
    return {
        "selected": len(candidates),
        "rendered": rendered,
        "reused": reused,
        "failures": failures,
    }
