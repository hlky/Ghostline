"""Read-only capture review reports with local images and explicit retry commands."""

from __future__ import annotations

from collections import Counter
from datetime import UTC, datetime
import json
import math
import os
from pathlib import Path
import sqlite3
from typing import Any, Iterable, Mapping
from urllib.parse import quote

from artifact_io import publish_json_artifacts

from .capture_evidence import assess_capture, capture_rows, check_report_destinations

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = Path(__file__).with_name("review.html")


def _query_rows(connection: sqlite3.Connection, query: str) -> list[dict[str, Any]]:
    cursor = connection.execute(query)
    names = [column[0] for column in cursor.description]
    return [dict(zip(names, row, strict=True)) for row in cursor]


def _failed_rows(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    return _query_rows(
        connection,
        """SELECT p.*, a.attempt_id AS latest_attempt_id,
                  a.error_code AS latest_error_code, a.error_detail AS latest_error_detail,
                  a.ready_event_json AS latest_ready_event_json,
                  a.finished_at AS latest_failure_at
           FROM places p LEFT JOIN capture_attempts a ON a.attempt_id=(
               SELECT recent.attempt_id FROM capture_attempts recent
               WHERE recent.location_id=p.location_id
               ORDER BY COALESCE(recent.finished_at,recent.captured_at,
                                 recent.ready_at,recent.accepted_at,'') DESC,
                        recent.attempt_number DESC,recent.attempt_id DESC LIMIT 1
           ) WHERE p.queue_status='failed' ORDER BY p.location_id""",
    )


def _selection(values: Iterable[str] | None) -> set[str] | None:
    if values is None:
        return None
    return {values} if isinstance(values, str) else set(values)


def _json_object(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    try:
        parsed = json.loads(value or "{}")
        return parsed if isinstance(parsed, dict) else {}
    except (TypeError, ValueError):
        return {}


def _json_safe(value: Any) -> Any:
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, Mapping):
        return {str(key): _json_safe(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(child) for child in value]
    return value


def _local_link(value: Any, output: Path) -> str | None:
    """Use encoded relative links for both file:// and project-root HTTP serving."""
    if (
        not isinstance(value, str)
        or not value
        or "://" in value
        or value.startswith(("\\\\", "//"))
    ):
        return None
    try:
        path = Path(value).expanduser()
        path = path.resolve() if path.is_absolute() else (ROOT / path).resolve()
        if not path.is_file():
            return None
        return quote(Path(os.path.relpath(path, output.parent)).as_posix(), safe="/")
    except (OSError, ValueError):
        # Cross-drive resources cannot have links that work under both serving
        # modes. Keep the row visible and report the missing review link.
        return None


def _powershell_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _retry_command(location_id: str, database: str | None) -> str:
    command = r"py -B .\tools\world_location_capture.py"
    if database:
        command += " --database " + _powershell_literal(database)
    return (
        command + " retry --recapture --location-id " + _powershell_literal(location_id)
    )


def _quality(
    assessment: Mapping[str, Any],
    has_capture: bool,
    rejected_validation: Mapping[str, Any] | None = None,
) -> str:
    if not has_capture and not rejected_validation:
        return "No image"
    if not rejected_validation and assessment.get("integrity_errors"):
        return "File problem"
    if not rejected_validation and not assessment.get("current"):
        return "Older pose"
    validation = rejected_validation or assessment.get("validation", {})
    codes = validation.get("error_codes")
    codes = codes if isinstance(codes, list) else []
    if "blurred_frame" in codes:
        return "Blurred"
    if "black_frame" in codes:
        return "Black frame"
    if "hud_visible" in codes:
        return "HUD visible"
    if validation.get("errors") or validation.get("valid") is False:
        return "Validation failed"
    if validation.get("publication_ready") is not True or validation.get("warnings"):
        return "Needs image review"
    return "Checks passed"


def _review_row(
    row: dict[str, Any], output: Path, database: str | None, *, verify_files: bool
) -> dict[str, Any]:
    has_capture = bool(row.get("capture_id"))
    assessment = (
        assess_capture(row, verify_files=verify_files)
        if has_capture
        else {
            "current": False,
            "integrity_errors": [],
            "blockers": ["No captured image for this location"],
            "publishable": False,
            "hashes_verified": False,
            "validation": {},
            "sidecar": {},
        }
    )
    status = str(row.get("queue_status") or "unknown")
    in_scope = row.get("scope_status") == "in_scope"
    failure_code = row.get("latest_error_code") or row.get("failure_code")
    failure_detail = row.get("latest_error_detail") or row.get("failure_detail")
    failure_evidence = _json_object(failure_detail) if status == "failed" else {}
    rejected_validation = _json_object(failure_evidence.get("validation"))
    rejected_image = _json_object(failure_evidence.get("rejected_image"))
    if failure_evidence:
        failure_detail = failure_evidence.get("message") or failure_code
    links = {
        name: _local_link(row.get(column), output)
        for name, column in (
            ("image", "png_path"),
            ("thumbnail", "thumbnail_path"),
            ("sidecar", "sidecar_path"),
        )
    }
    links["rejected_preview"] = _local_link(rejected_image.get("path"), output)
    blockers = list(assessment["blockers"])
    if not has_capture and not in_scope:
        blockers.append("Location is outside the capture scope")
    if not has_capture and row.get("review_status") != "resolved":
        blockers.append(
            "Location metadata is " + str(row.get("review_status") or "unresolved")
        )
    link_warnings = [
        f"Cannot link {name} from this report"
        for name, link in links.items()
        if name != "rejected_preview" and has_capture and link is None
    ]
    if rejected_image and not links["rejected_preview"]:
        link_warnings.append(
            "Rejected preview is missing or cannot be linked from this report"
        )
    if assessment["publishable"]:
        publication = "Evidence checks passed"
    elif blockers:
        publication = "Publication blocked"
    else:
        publication = "Ready for hash verification"
    validation = rejected_validation or assessment["validation"]
    return _json_safe(
        {
            "id": str(row["location_id"]),
            "capture_id": row.get("capture_id"),
            "category": str(row.get("category") or "Unknown category"),
            "area": str(
                row.get("named_area")
                or row.get("subdistrict")
                or row.get("district")
                or "Unknown area"
            ),
            "district": row.get("district"),
            "subdistrict": row.get("subdistrict"),
            "status": status,
            "quality": _quality(assessment, has_capture, rejected_validation),
            "has_capture": has_capture,
            "captured_at": row.get("captured_at"),
            "updated_at": row.get("updated_at"),
            "direction": row.get("direction"),
            "resource": row.get("resource_path"),
            "sector": row.get("source_sector"),
            "fast_travel": row.get("nearest_fast_travel_name"),
            "street": row.get("nearest_street_name"),
            "interior": row.get("interior_state"),
            "position": {
                axis: row.get(f"requested_{axis}") for axis in ("x", "y", "z", "yaw")
            },
            "dimensions": {"width": row.get("width"), "height": row.get("height")},
            "links": links,
            "link_warnings": link_warnings,
            "publication": publication,
            "blockers": blockers,
            "current": assessment["current"],
            "hashes_verified": assessment.get("hashes_verified", False),
            "validation": validation,
            "validation_source": "rejected_attempt"
            if rejected_validation
            else "capture",
            "failure_code": failure_code,
            "failure_detail": failure_detail,
            "ready_event": _json_object(row.get("latest_ready_event_json")),
            "retry_command": _retry_command(str(row["location_id"]), database)
            if status in {"captured", "failed"}
            and in_scope
            and row.get("review_status") != "rejected"
            else None,
        }
    )


def build_review(
    connection: sqlite3.Connection,
    output: Path,
    *,
    limit: int = 300,
    categories: Iterable[str] | None = None,
    location_ids: Iterable[str] | None = None,
    verify_files: bool = False,
) -> dict[str, Any]:
    """Write a self-contained gallery without changing database state.

    ``limit=0`` includes every matching location. The newest capture is selected
    before filtering/limiting; failed locations without images remain reviewable.
    Fast review checks files and sidecars, but never grants publication approval.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer (0 means all)")
    output = Path(output).expanduser().resolve()
    if output.suffix.casefold() != ".html":
        raise ValueError("Review output must be an .html file")
    data_path = output.with_suffix(".json")
    rejected_paths = [
        _json_object(_json_object(row[0]).get("rejected_image")).get("path")
        for row in connection.execute(
            "SELECT error_detail FROM capture_attempts WHERE error_detail IS NOT NULL"
        )
    ]
    check_report_destinations(
        connection,
        [output, data_path],
        extra_inputs=[
            value for value in rejected_paths if isinstance(value, str) and value
        ],
    )
    latest: dict[str, dict[str, Any]] = {}
    for row in capture_rows(connection):
        key = str(row["location_id"])
        previous = latest.get(key)
        if previous is None or (
            row.get("captured_at") or "",
            row.get("capture_id") or "",
        ) > (previous.get("captured_at") or "", previous.get("capture_id") or ""):
            latest[key] = row
    for failed in _failed_rows(connection):
        key = str(failed["location_id"])
        if key in latest:
            latest[key].update(
                {
                    name: value
                    for name, value in failed.items()
                    if name.startswith("latest_")
                }
            )
        else:
            latest[key] = failed
    category_filter, id_filter = _selection(categories), _selection(location_ids)
    selected = [
        row
        for row in latest.values()
        if (category_filter is None or row["category"] in category_filter)
        and (id_filter is None or row["location_id"] in id_filter)
    ]
    selected.sort(
        key=lambda row: (
            max(
                str(row.get("captured_at") or ""),
                str(row.get("latest_failure_at") or ""),
                str(row.get("updated_at") or ""),
            ),
            str(row["location_id"]),
        ),
        reverse=True,
    )
    total = len(selected)
    if limit:
        selected = selected[:limit]
    databases = connection.execute("PRAGMA database_list").fetchall()
    database = next(
        (str(row[2]) for row in databases if row[1] == "main" and row[2]), None
    )
    rows = [
        _review_row(row, output, database, verify_files=verify_files)
        for row in selected
    ]
    summary = {
        "output": str(output),
        "data": str(data_path),
        "database": database,
        "locations": len(rows),
        "matched_locations": total,
        "omitted": total - len(rows),
        "captures": sum(row["has_capture"] for row in rows),
        "failed": sum(row["status"] == "failed" for row in rows),
        "verify_files": verify_files,
        "quality_counts": dict(sorted(Counter(row["quality"] for row in rows).items())),
    }
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "summary": summary,
        "rows": rows,
    }
    embedded = (
        json.dumps(payload, ensure_ascii=False, allow_nan=False)
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    html = TEMPLATE.read_text(encoding="utf-8").replace("__REVIEW_DATA__", embedded)
    publish_json_artifacts(
        {data_path: payload}, binary_artifacts={output: html.encode("utf-8")}
    )
    return summary
