"""SQLite publication of already validated capture files and their sidecar."""

from __future__ import annotations
from pathlib import Path
import sqlite3
from typing import Any, Mapping
from .database import json_text, transaction, utc_now


def persist_capture(
    connection: sqlite3.Connection,
    sidecar: Mapping[str, Any],
    sidecar_path: Path,
    metadata_hash: str,
    event: Mapping[str, Any],
) -> None:
    capture_id, attempt_id = sidecar["capture_id"], sidecar["attempt_id"]
    validation, actual_pose = sidecar["validation"], sidecar["actual_pose"]
    resolved = sidecar["location_metadata"]
    review_status = resolved["review_status"]
    png_path, thumbnail_path = sidecar["files"]["png"], sidecar["files"]["thumbnail"]
    image_hash, thumbnail_hash = (
        sidecar["files"]["png_sha256"],
        sidecar["files"]["thumbnail_sha256"],
    )
    validation_status = (
        "valid" if validation.get("publication_ready") else "needs_ui_review"
    )
    with transaction(connection):
        connection.execute(
            """UPDATE capture_attempts SET status='captured',ready_at=?,captured_at=?,finished_at=?,
                   teleport_to_ready_ms=?,ready_to_capture_ms=?,total_capture_ms=?,
                   ready_event_json=?,actual_pose_json=? WHERE attempt_id=?""",
            (
                event.get("timestamp"),
                sidecar["captured_at"],
                sidecar["captured_at"],
                event.get("teleport_to_ready_ms"),
                sidecar["latency"]["ready_to_capture_ms"],
                sidecar["latency"]["total_capture_ms"],
                json_text(event),
                json_text(actual_pose),
                attempt_id,
            ),
        )
        connection.execute(
            """INSERT INTO captures(capture_id,attempt_id,location_id,png_path,sidecar_path,
                   thumbnail_path,width,height,image_sha256,metadata_sha256,thumbnail_sha256,
                   captured_at,validation_status,validation_json,perceptual_hash)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                capture_id,
                attempt_id,
                sidecar["location_id"],
                str(png_path),
                str(sidecar_path),
                str(thumbnail_path),
                sidecar["dimensions"]["width"],
                sidecar["dimensions"]["height"],
                image_hash,
                metadata_hash,
                thumbnail_hash,
                sidecar["captured_at"],
                validation_status,
                json_text(validation),
                validation.get("perceptual_hash"),
            ),
        )
        connection.execute(
            """UPDATE places SET actual_x=?,actual_y=?,actual_z=?,actual_yaw=?,actual_pitch=?,
                   actual_roll=?,actual_fov=?,district=coalesce(?,district),
                   subdistrict=coalesce(?,subdistrict),named_area=coalesce(?,named_area),
                   interior_state=coalesce(?,interior_state),review_status=?,queue_status='captured',
                   provenance_json=?,publishable=0,failure_code=NULL,failure_detail=NULL,updated_at=?
               WHERE location_id=?""",
            (
                actual_pose.get("x"),
                actual_pose.get("y"),
                actual_pose.get("z"),
                actual_pose.get("yaw"),
                actual_pose.get("pitch"),
                actual_pose.get("roll"),
                event.get("actual_fov"),
                resolved.get("district"),
                resolved.get("subdistrict"),
                resolved.get("named_area"),
                resolved.get("interior_state"),
                review_status,
                json_text(sidecar["metadata_provenance"]),
                utc_now(),
                sidecar["location_id"],
            ),
        )
