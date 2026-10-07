"""Shared checks for a capture's files, current pose, and publication evidence."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sqlite3
from typing import Any, Iterable, Mapping

from .database import transaction


def capture_rows(
    connection: sqlite3.Connection, session_id: str | None = None
) -> list[dict[str, Any]]:
    where = "WHERE a.session_id=?" if session_id is not None else ""
    return [
        dict(row)
        for row in connection.execute(
            f"""SELECT p.*,c.capture_id,c.attempt_id,c.png_path,c.sidecar_path,
                       c.thumbnail_path,c.width,c.height,c.image_sha256,c.metadata_sha256,
                       c.thumbnail_sha256,c.perceptual_hash,c.captured_at,c.validation_status,
                       c.validation_json,a.session_id,a.status AS attempt_status,
                       s.restoration_verified,s.game_profile,f.tags AS anchor_tags,
                       f.metadata_json AS anchor_metadata_json
                FROM captures c JOIN places p ON p.location_id=c.location_id
                JOIN capture_attempts a ON a.attempt_id=c.attempt_id
                JOIN capture_sessions s ON s.session_id=a.session_id
                LEFT JOIN features f ON f.feature_id=p.anchor_feature_id
                {where} ORDER BY p.queue_order,p.location_id,c.captured_at,c.capture_id""",
            (session_id,) if session_id is not None else (),
        )
    ]


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def check_report_destinations(
    connection: sqlite3.Connection,
    outputs: Iterable[Path],
    *,
    extra_inputs: Iterable[Path] = (),
) -> None:
    """A review/export destination must never replace the evidence it reviews."""
    protected = {Path(path).resolve() for path in extra_inputs}
    for row in connection.execute("PRAGMA database_list"):
        if row[2]:
            protected.update(
                Path(row[2] + suffix).resolve()
                for suffix in ("", "-wal", "-shm", "-journal")
            )
    for row in connection.execute(
        "SELECT png_path,sidecar_path,thumbnail_path FROM captures"
    ):
        protected.update(Path(path).resolve() for path in row if path)
    for output in outputs:
        if Path(output).resolve() in protected:
            raise ValueError(
                f"Report output would overwrite capture evidence: {output}"
            )


def capture_integrity(
    row: Mapping[str, Any], *, verify_files: bool = True
) -> list[str]:
    errors = []
    for column, hash_column in (
        ("png_path", "image_sha256"),
        ("sidecar_path", "metadata_sha256"),
        ("thumbnail_path", "thumbnail_sha256"),
    ):
        try:
            path = Path(row[column])
            if not path.is_file():
                errors.append(f"Missing {column}: {path}")
            elif not row.get(hash_column):
                errors.append(f"Missing recorded hash for {column}")
            elif verify_files and hash_file(path) != row[hash_column]:
                errors.append(f"Hash mismatch for {column}: {path}")
        except (KeyError, TypeError, ValueError, OSError) as error:
            errors.append(f"Cannot verify {column}: {error}")
    return errors


def _same_pose(sidecar: Mapping[str, Any], row: Mapping[str, Any]) -> bool:
    pose = sidecar.get("planned_pose", sidecar.get("requested_pose"))
    if not isinstance(pose, dict):
        return False
    for axis in ("x", "y", "z", "yaw", "pitch", "roll"):
        try:
            captured, planned = float(pose[axis]), float(row[f"requested_{axis}"])
        except (KeyError, TypeError, ValueError):
            return False
        if not math.isfinite(captured) or not math.isfinite(planned):
            return False
        delta = captured - planned
        if axis in ("yaw", "pitch", "roll"):
            delta = (delta + 180) % 360 - 180
        if abs(delta) > 1e-6:
            return False
    anchor = sidecar.get("anchor", {})
    return isinstance(anchor, dict) and all(
        anchor.get(key) == row.get(column)
        for key, column in (
            ("category", "category"),
            ("direction", "direction"),
            ("resource", "resource_path"),
            ("source_sector", "source_sector"),
            ("road_id", "road_id"),
        )
    )


def assess_capture(
    row: Mapping[str, Any], *, verify_files: bool = True
) -> dict[str, Any]:
    """Assess this capture independently of the place's cached publishable flag.

    Review may skip expensive image hashing, but cannot turn that preview into
    publication evidence. Export and session publication always verify files.
    """
    row = dict(row)
    integrity_errors = capture_integrity(row, verify_files=verify_files)
    sidecar: dict[str, Any] = {}
    try:
        value = json.loads(Path(row["sidecar_path"]).read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("sidecar must contain an object")
        sidecar = value
    except (KeyError, TypeError, ValueError, OSError) as error:
        integrity_errors.append(f"Cannot read capture sidecar: {error}")
    for key in ("capture_id", "attempt_id", "session_id", "location_id"):
        if sidecar.get(key) != row.get(key):
            integrity_errors.append(f"Sidecar {key} does not match its database record")
    files = sidecar.get("files", {})
    for key, column in (
        ("png", "png_path"),
        ("thumbnail", "thumbnail_path"),
        ("png_sha256", "image_sha256"),
        ("thumbnail_sha256", "thumbnail_sha256"),
    ):
        if not isinstance(files, dict) or files.get(key) != row.get(column):
            integrity_errors.append(
                f"Sidecar {key} does not match its capture file record"
            )
    try:
        validation = json.loads(row.get("validation_json") or "{}")
        if not isinstance(validation, dict):
            raise ValueError("validation must contain an object")
    except (TypeError, ValueError):
        validation = {}
        integrity_errors.append("Capture validation record is malformed")
    if sidecar.get("validation") != validation:
        integrity_errors.append("Sidecar validation does not match its database record")

    current = _same_pose(sidecar, row)
    blockers = list(integrity_errors)
    if not current:
        blockers.append("Capture belongs to an older pose or anchor")
    if row.get("queue_status") != "captured":
        blockers.append(f"Location is {row.get('queue_status', 'unknown')}")
    if row.get("scope_status") != "in_scope":
        blockers.append("Location is outside the capture scope")
    if row.get("review_status") != "resolved":
        blockers.append(
            f"Location metadata is {row.get('review_status', 'unresolved')}"
        )
    if row.get("restoration_verified") != 1:
        blockers.append("This capture's session did not verify game restoration")
    if row.get("attempt_status") != "captured":
        blockers.append("Capture attempt did not complete image publication")
    if (
        row.get("validation_status") != "valid"
        or validation.get("valid") is not True
        or validation.get("publication_ready") is not True
        or validation.get("errors")
    ):
        blockers.append("Image validation still requires review")
    readiness = sidecar.get("readiness", {})
    if not isinstance(readiness, dict):
        readiness = {}
    for key in ("ui_suppressed", "weapon_suppressed"):
        if readiness.get(key) is not True:
            blockers.append(f"Runtime did not verify {key.replace('_', ' ')}")
    return {
        "current": current,
        "integrity_errors": integrity_errors,
        "blockers": blockers,
        "publishable": verify_files and not blockers,
        "hashes_verified": verify_files and not integrity_errors,
        "validation": validation,
        "sidecar": sidecar,
    }


def refresh_session_publication(connection: sqlite3.Connection, session_id: str) -> int:
    """Refresh only locations captured in this session, after restoration commits."""
    eligible: dict[str, bool] = {}
    for row in capture_rows(connection, session_id):
        assessment = assess_capture(row)
        location = row["location_id"]
        eligible[location] = eligible.get(location, False) or assessment["publishable"]
    with transaction(connection):
        connection.executemany(
            "UPDATE places SET publishable=? WHERE location_id=?",
            [(int(value), location) for location, value in eligible.items()],
        )
    return sum(eligible.values())
