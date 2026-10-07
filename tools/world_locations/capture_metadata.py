"""Capture evidence construction, independent of the Windows controller."""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping
import json
from .database import utc_now


@dataclass(frozen=True)
class CaptureContext:
    capture_id: str
    session_id: str
    attempt_id: str
    command_id: str
    place: Mapping[str, Any]
    event: Mapping[str, Any]
    validation: Mapping[str, Any]
    game_profile: str
    capture_profile: Mapping[str, Any]
    resolved: Mapping[str, Any]
    runtime_provenance: Mapping[str, Any]
    actual_pose: Mapping[str, Any]
    effective_pose: Mapping[str, Any]
    review_status: str
    anchor_tags: list[str]
    anchor_roles: list[str]
    width: int
    height: int
    png_path: Path
    thumbnail_path: Path
    image_hash: str
    thumbnail_hash: str
    sent_monotonic: float
    ready_monotonic: float
    captured_monotonic: float


def build_sidecar(context: CaptureContext) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "capture_id": context.capture_id,
        "session_id": context.session_id,
        "attempt_id": context.attempt_id,
        "command_id": context.command_id,
        "location_id": context.place["location_id"],
        "planned_pose": {
            "x": context.place["requested_x"],
            "y": context.place["requested_y"],
            "z": context.place["requested_z"],
            "yaw": context.place["requested_yaw"],
            "pitch": context.place["requested_pitch"],
            "roll": context.place["requested_roll"],
            "forward": {
                "x": context.place["forward_x"],
                "y": context.place["forward_y"],
                "z": context.place["forward_z"],
            },
        },
        "requested_pose": {
            "x": context.place["requested_x"],
            "y": context.place["requested_y"],
            "z": context.place["requested_z"],
            "yaw": context.place["requested_yaw"],
            "pitch": context.place["requested_pitch"],
            "roll": context.place["requested_roll"],
        },
        "effective_pose": dict(context.effective_pose),
        "actual_pose": context.actual_pose,
        "actual_fov": context.event.get("actual_fov"),
        "runtime_location": context.event.get("runtime_location", {}),
        "readiness": context.event.get("readiness", {}),
        "validation": context.validation,
        "game_profile": context.game_profile,
        "capture_profile": context.capture_profile,
        "dimensions": {"width": context.width, "height": context.height},
        "anchor": {
            "category": context.place["category"],
            "direction": context.place["direction"],
            "feature_id": context.place["anchor_feature_id"],
            "resource": context.place["resource_path"],
            "source_sector": context.place["source_sector"],
            "road_id": context.place["road_id"],
            "tags": context.anchor_tags,
            "roles": context.anchor_roles,
        },
        "location_metadata": {
            "nearest_fast_travel": {
                "stable_id": context.place["nearest_fast_travel_id"],
                "name": context.resolved.get("nearest_fast_travel_name"),
                "x": context.place["nearest_fast_travel_x"],
                "y": context.place["nearest_fast_travel_y"],
                "z": context.place["nearest_fast_travel_z"],
                "horizontal_distance_m": context.place[
                    "nearest_fast_travel_distance_m"
                ],
            },
            "nearest_street": {
                "road_id": context.place["nearest_street_road_id"],
                "name": context.resolved.get("nearest_street_name"),
                "closest_x": context.place["nearest_street_x"],
                "closest_y": context.place["nearest_street_y"],
                "closest_z": context.place["nearest_street_z"],
                "horizontal_distance_m": context.place["nearest_street_distance_m"],
            },
            "district": context.resolved.get("district"),
            "subdistrict": context.resolved.get("subdistrict"),
            "named_area": context.resolved.get("named_area"),
            "interior_state": context.resolved.get("interior_state"),
            "review_status": context.review_status,
        },
        "rules": {
            "extraction": context.place["extraction_rule_version"],
            "placement": context.place["placement_rule_version"],
        },
        "metadata_provenance": {
            **json.loads(context.place["provenance_json"]),
            **context.runtime_provenance,
        },
        "files": {
            "png": str(context.png_path),
            "thumbnail": str(context.thumbnail_path),
            "png_sha256": context.image_hash,
            "thumbnail_sha256": context.thumbnail_hash,
        },
        "captured_at": utc_now(),
        "latency": {
            "teleport_to_ready_ms": context.event.get("teleport_to_ready_ms"),
            "ready_to_capture_ms": (
                context.captured_monotonic - context.ready_monotonic
            )
            * 1000.0,
            "total_capture_ms": (context.captured_monotonic - context.sent_monotonic)
            * 1000.0,
        },
    }
