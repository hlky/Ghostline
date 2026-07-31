"""Windows capture controller driven exclusively by CET readiness events."""

from __future__ import annotations

import ctypes
from ctypes import wintypes
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
import sys
import threading
import time
from typing import Any, Mapping
import uuid

from . import PROTOCOL_SCHEMA_VERSION
from .database import json_text, transaction, utc_now
from .model import stable_id
from .planning import REQUIRED_NAME_FIELDS, resolve_metadata
from .protocol import ProtocolError, RuntimeProtocol, RuntimeTimeout, atomic_write_json


class CaptureError(RuntimeError):
    pass


class SessionProtocolError(RuntimeError):
    """A command lifecycle did not terminate; later work must not be sent."""


class ValidationError(CaptureError):
    def __init__(self, report: Mapping[str, Any]):
        self.report = dict(report)
        super().__init__(
            "; ".join(self.report.get("errors", [])) or "capture validation failed"
        )


def _angle_delta(left: float, right: float) -> float:
    return abs((left - right + 180.0) % 360.0 - 180.0)


def validate_ready_event(
    event: Mapping[str, Any],
    place: Mapping[str, Any],
    capture_config: Mapping[str, Any],
) -> dict[str, Any]:
    evidence = event.get("readiness")
    if not isinstance(evidence, Mapping):
        evidence = event
    required_true = (
        "streaming_complete",
        "player_attached",
        "camera_attached",
        "position_valid",
        "position_stable",
        "ground_probe",
    )
    errors = [
        f"readiness predicate is false: {name}"
        for name in required_true
        if evidence.get(name) is not True
    ]
    if evidence.get("loading_screen") is not False:
        errors.append("loading screen predicate is not false")
    if evidence.get("menu_open") is not False:
        errors.append("menu predicate is not false")
    if evidence.get("paused") is not False:
        errors.append("paused predicate is not false")
    if not isinstance(evidence.get("presented_frame"), int):
        errors.append("ready event has no presented frame identifier")
    effective = event.get("effective_pose")
    if not isinstance(effective, Mapping):
        effective = {
            "x": place["requested_x"],
            "y": place["requested_y"],
            "z": place["requested_z"],
            "yaw": place["requested_yaw"],
            "pitch": place["requested_pitch"],
            "roll": place["requested_roll"],
        }
    actual = event.get("actual_pose")
    if not isinstance(actual, Mapping):
        errors.append("ready event has no actual pose")
        actual = {}
    try:
        distance = math.sqrt(
            (float(actual["x"]) - float(effective["x"])) ** 2
            + (float(actual["y"]) - float(effective["y"])) ** 2
            + (float(actual["z"]) - float(effective["z"])) ** 2
        )
    except (KeyError, TypeError, ValueError):
        distance = math.inf
    heading_delta = _angle_delta(
        float(actual.get("yaw", math.inf)), float(effective["yaw"])
    )
    expected_fov = capture_config.get("profile", {}).get("fov")
    actual_fov = event.get("actual_fov")
    if expected_fov is not None:
        try:
            fov_delta = abs(float(actual_fov) - float(expected_fov))
        except (TypeError, ValueError):
            fov_delta = math.inf
    else:
        fov_delta = 0.0
    return {
        "valid": not errors,
        "errors": errors,
        "position_delta_m": distance,
        "heading_delta_degrees": heading_delta,
        "fov_delta_degrees": fov_delta,
        "evidence": dict(evidence),
        "effective_pose": dict(effective),
    }


class GameWindow:
    """Locate and capture the exact Win32 client rectangle."""

    def __init__(self, title_contains: str, process_name: str):
        if sys.platform != "win32":
            raise CaptureError("the in-game capture controller requires Windows")
        self.title_contains = title_contains.lower()
        self.process_name = process_name.lower()
        self.user32 = ctypes.windll.user32
        self.kernel32 = ctypes.windll.kernel32

    def _process_matches(self, hwnd: int) -> bool:
        process_id = wintypes.DWORD()
        self.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(process_id))
        if not process_id.value:
            return False
        handle = self.kernel32.OpenProcess(0x1000, False, process_id.value)
        if not handle:
            return False
        try:
            size = wintypes.DWORD(32768)
            buffer = ctypes.create_unicode_buffer(size.value)
            if not self.kernel32.QueryFullProcessImageNameW(
                handle, 0, buffer, ctypes.byref(size)
            ):
                return False
            return Path(buffer.value).name.lower() == self.process_name
        finally:
            self.kernel32.CloseHandle(handle)

    def find(self) -> int:
        matches: list[int] = []
        callback_type = ctypes.WINFUNCTYPE(
            wintypes.BOOL, wintypes.HWND, wintypes.LPARAM
        )

        @callback_type
        def callback(hwnd: int, _parameter: int) -> bool:
            if not self.user32.IsWindowVisible(hwnd):
                return True
            length = self.user32.GetWindowTextLengthW(hwnd)
            if length <= 0:
                return True
            buffer = ctypes.create_unicode_buffer(length + 1)
            self.user32.GetWindowTextW(hwnd, buffer, len(buffer))
            if (
                self.title_contains in buffer.value.lower()
                and self._process_matches(hwnd)
            ):
                matches.append(int(hwnd))
            return True

        self.user32.EnumWindows(callback, 0)
        if not matches:
            raise CaptureError(
                f"no visible {self.process_name!r} window contains "
                f"{self.title_contains!r}"
            )
        if len(matches) > 1:
            raise CaptureError(
                f"multiple visible {self.process_name!r} windows contain "
                f"{self.title_contains!r}"
            )
        return matches[0]

    def client_rectangle(self, hwnd: int) -> tuple[int, int, int, int]:
        rectangle = wintypes.RECT()
        if not self.user32.GetClientRect(hwnd, ctypes.byref(rectangle)):
            raise CaptureError("GetClientRect failed")
        origin = wintypes.POINT(0, 0)
        if not self.user32.ClientToScreen(hwnd, ctypes.byref(origin)):
            raise CaptureError("ClientToScreen failed")
        width = rectangle.right - rectangle.left
        height = rectangle.bottom - rectangle.top
        return origin.x, origin.y, origin.x + width, origin.y + height

    def capture(
        self,
        expected_width: int,
        expected_height: int,
        *,
        visual_settle_seconds: float = 2.0,
        visual_timeout_seconds: float = 45.0,
        black_pixel_threshold: int = 8,
        black_fraction_threshold: float = 0.98,
    ) -> Any:
        hwnd = self.find()
        try:
            from PIL import Image  # type: ignore[import-not-found]
            from windows_capture import WindowsCapture  # type: ignore[import-not-found]
        except ImportError as error:
            raise CaptureError(
                "window capture backend is unavailable; install "
                "tools/requirements-world-locations.txt"
            ) from error

        image: Any | None = None
        capture_error: str | None = None
        started = time.monotonic()
        visible_since: float | None = None
        capture = WindowsCapture(
            cursor_capture=False,
            draw_border=None,
            secondary_window=None,
            window_hwnd=hwnd,
        )

        @capture.event
        def on_frame_arrived(frame: Any, capture_control: Any) -> None:
            nonlocal image, capture_error, visible_since
            now = time.monotonic()
            if (frame.width, frame.height) != (expected_width, expected_height):
                capture_error = (
                    f"game capture is {frame.width}x{frame.height}; required "
                    f"{expected_width}x{expected_height}"
                )
                capture_control.stop()
                return
            bgr = frame.frame_buffer[:, :, :3]
            black_fraction = float(
                (bgr.max(axis=2) <= black_pixel_threshold).mean()
            )
            if black_fraction >= black_fraction_threshold:
                visible_since = None
            elif visible_since is None:
                visible_since = now
            elif now - visible_since >= visual_settle_seconds:
                # Windows Graphics Capture supplies BGRA pixels. Copy them
                # while the callback owns the native frame buffer.
                rgb = frame.frame_buffer[:, :, [2, 1, 0]].copy()
                image = Image.fromarray(rgb, "RGB")
                capture_control.stop()
                return
            if now - started >= visual_timeout_seconds:
                capture_error = (
                    "game window remained loading-like for "
                    f"{visual_timeout_seconds:.1f} seconds"
                )
                capture_control.stop()

        @capture.event
        def on_closed() -> None:
            nonlocal capture_error
            if image is None and capture_error is None:
                capture_error = "Cyberpunk 2077 closed before a frame arrived"

        try:
            capture.start()
        except Exception as error:
            raise CaptureError(f"Windows Graphics Capture failed: {error}") from error
        if capture_error:
            raise CaptureError(capture_error)
        if image is None:
            raise CaptureError("Windows Graphics Capture returned no frame")
        return image


def _template_matches(
    image: Any, validation: Mapping[str, Any], config_root: Path
) -> tuple[list[str], list[str]]:
    templates = validation.get("hud_templates", [])
    if not templates:
        return [], ["no HUD templates configured; visual UI validation requires review"]
    try:
        import cv2  # type: ignore[import-not-found]
        import numpy  # type: ignore[import-not-found]
    except ImportError as error:
        return [], [f"HUD template matching unavailable: {error}"]
    frame = cv2.cvtColor(numpy.asarray(image.convert("RGB")), cv2.COLOR_RGB2GRAY)
    matches: list[str] = []
    warnings: list[str] = []
    default_threshold = float(validation.get("template_threshold", 0.9))
    for entry in templates:
        if isinstance(entry, str):
            entry = {"path": entry, "name": Path(entry).stem}
        if not isinstance(entry, Mapping) or not entry.get("path"):
            warnings.append("ignored malformed HUD template entry")
            continue
        template_path = Path(str(entry["path"]))
        if not template_path.is_absolute():
            template_path = (config_root / template_path).resolve()
        template = cv2.imread(str(template_path), cv2.IMREAD_GRAYSCALE)
        if template is None:
            warnings.append(f"HUD template is unreadable: {template_path}")
            continue
        region = entry.get("region")
        sample = frame
        if isinstance(region, list) and len(region) == 4:
            x, y, width, height = (int(value) for value in region)
            sample = frame[y : y + height, x : x + width]
        if sample.shape[0] < template.shape[0] or sample.shape[1] < template.shape[1]:
            warnings.append(
                f"HUD template is larger than its search region: {template_path}"
            )
            continue
        score = float(
            cv2.minMaxLoc(cv2.matchTemplate(sample, template, cv2.TM_CCOEFF_NORMED))[1]
        )
        if score >= float(entry.get("threshold", default_threshold)):
            matches.append(f"{entry.get('name', template_path.stem)}:{score:.3f}")
    return matches, warnings


def validate_image(
    image: Any,
    *,
    ready_report: Mapping[str, Any],
    validation_config: Mapping[str, Any],
    config_root: Path,
) -> dict[str, Any]:
    from PIL import ImageStat  # type: ignore[import-not-found]

    grayscale = image.convert("L")
    statistics = ImageStat.Stat(grayscale)
    mean = float(statistics.mean[0])
    stddev = float(statistics.stddev[0])
    histogram = grayscale.histogram()
    pixel_count = grayscale.width * grayscale.height
    black_pixel_threshold = int(validation_config.get("black_pixel_threshold", 8))
    black_fraction = (
        sum(histogram[: black_pixel_threshold + 1]) / pixel_count
        if pixel_count
        else 1.0
    )
    errors = list(ready_report.get("errors", []))
    if (
        black_fraction
        >= float(validation_config.get("black_fraction_threshold", 0.98))
        or (
            mean <= float(validation_config.get("black_mean_threshold", 4.0))
            and stddev
            <= float(validation_config.get("black_stddev_threshold", 3.0))
        )
    ):
        errors.append(
            "frame is black/loading-like "
            f"(black_fraction={black_fraction:.4f}, mean={mean:.2f}, "
            f"stddev={stddev:.2f})"
        )
    sharpness: float | None = None
    sharpness_warning: str | None = None
    try:
        import cv2  # type: ignore[import-not-found]
        import numpy  # type: ignore[import-not-found]

        sharpness = float(
            cv2.Laplacian(numpy.asarray(grayscale), cv2.CV_64F).var()
        )
        minimum_sharpness = float(
            validation_config.get("sharpness_laplacian_threshold", 30.0)
        )
        if sharpness < minimum_sharpness:
            errors.append(
                f"frame is globally blurred (sharpness={sharpness:.2f}, "
                f"minimum={minimum_sharpness:.2f})"
            )
    except ImportError as error:
        sharpness_warning = f"sharpness validation unavailable: {error}"
    hud_matches, hud_warnings = _template_matches(image, validation_config, config_root)
    if sharpness_warning:
        hud_warnings.append(sharpness_warning)
    if hud_matches:
        errors.append(f"HUD template visible: {', '.join(hud_matches)}")
    return {
        "valid": not errors,
        "publication_ready": not errors and not hud_warnings,
        "errors": errors,
        "warnings": hud_warnings,
        "luminance_mean": mean,
        "luminance_stddev": stddev,
        "black_fraction": black_fraction,
        "sharpness_laplacian_variance": sharpness,
        "hud_matches": hud_matches,
        "readiness": dict(ready_report),
    }


def _safe_area_name(value: str | None) -> str:
    text = (value or "_review").strip()
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip(".-")
    return text[:100] or "_review"


def _nearest_runtime_area(
    connection: sqlite3.Connection, x: float, y: float, maximum_distance_m: float
) -> dict[str, Any]:
    row = connection.execute(
        """SELECT district,subdistrict,named_area,
                  ((requested_x-?)*(requested_x-?)+(requested_y-?)*(requested_y-?)) AS distance_sq
           FROM places
           WHERE named_area IS NOT NULL AND trim(named_area)!=''
             AND json_extract(provenance_json,'$.named_area')='runtime'
             AND requested_x BETWEEN ? AND ? AND requested_y BETWEEN ? AND ?
           ORDER BY distance_sq LIMIT 1""",
        (
            x,
            x,
            y,
            y,
            x - maximum_distance_m,
            x + maximum_distance_m,
            y - maximum_distance_m,
            y + maximum_distance_m,
        ),
    ).fetchone()
    if not row or float(row["distance_sq"]) > maximum_distance_m**2:
        return {}
    return {
        "district": row["district"],
        "subdistrict": row["subdistrict"],
        "named_area": row["named_area"],
    }


def _atomic_save_image(
    image: Any, path: Path, image_format: str, **options: Any
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    image.save(temporary, format=image_format, **options)
    os.replace(temporary, path)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def recover_interrupted_queue(connection: sqlite3.Connection) -> int:
    """Make destinations abandoned by a terminated controller resumable."""
    with transaction(connection):
        recovered_at = utc_now()
        cursor = connection.execute(
            """UPDATE places SET
                   queue_status=CASE WHEN scope_status='in_scope' THEN 'pending' ELSE 'disabled' END,
                   failure_code='interrupted_session',
                   failure_detail='previous controller ended before committing a capture',updated_at=?
               WHERE queue_status='in_progress'""",
            (recovered_at,),
        )
        connection.execute(
            """UPDATE capture_sessions SET ended_at=?,status='error',
                   error=coalesce(error,'controller ended without finalizing the session')
               WHERE status='running'""",
            (recovered_at,),
        )
    return cursor.rowcount


class CaptureController:
    def __init__(
        self,
        connection: sqlite3.Connection,
        config: Mapping[str, Any],
        *,
        runtime_root: Path,
        captures_root: Path,
        config_root: Path,
        game_profile: str,
    ):
        self.connection = connection
        self.config = config
        self.capture_config = config["capture"]
        self.runtime = RuntimeProtocol(
            runtime_root, float(self.capture_config.get("protocol_poll_seconds", 0.01))
        )
        self.captures_root = captures_root
        self.config_root = config_root
        self.game_profile = game_profile
        self.window = GameWindow(
            str(self.capture_config["window_title_contains"]),
            str(self.capture_config.get("window_process_name", "Cyberpunk2077.exe")),
        )

    def _command(
        self, session_id: str, command_id: str, place: Mapping[str, Any]
    ) -> dict[str, Any]:
        return {
            "schema_version": PROTOCOL_SCHEMA_VERSION,
            "kind": "capture",
            "session_id": session_id,
            "command_id": command_id,
            "location_id": place["location_id"],
            "pose": {
                "x": place["requested_x"],
                "y": place["requested_y"],
                "z": place["requested_z"],
                "yaw": place["requested_yaw"],
                "pitch": place["requested_pitch"],
                "roll": place["requested_roll"],
            },
            "profile": dict(self.capture_config["profile"]),
            "expected": {
                "category": place["category"],
                "anchor_feature_id": place["anchor_feature_id"],
                "road_id": place["road_id"],
                "forward": {
                    "x": place["forward_x"],
                    "y": place["forward_y"],
                    "z": place["forward_z"],
                },
                "position_tolerance_m": self.capture_config.get(
                    "position_tolerance_m", 0.35
                ),
            },
        }

    def _insert_attempt(
        self,
        *,
        attempt_id: str,
        session_id: str,
        location_id: str,
        command_id: str,
        attempt_number: int,
    ) -> None:
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO capture_attempts(
                       attempt_id,session_id,location_id,command_id,attempt_number,status)
                   VALUES(?,?,?,?,?,'sent')""",
                (attempt_id, session_id, location_id, command_id, attempt_number),
            )
            self.connection.execute(
                "UPDATE places SET queue_status='in_progress',updated_at=? WHERE location_id=?",
                (utc_now(), location_id),
            )

    def _failed_attempt(self, attempt_id: str, code: str, detail: str) -> None:
        with transaction(self.connection):
            self.connection.execute(
                """UPDATE capture_attempts SET status='failed',finished_at=?,error_code=?,error_detail=?
                   WHERE attempt_id=?""",
                (utc_now(), code, detail, attempt_id),
            )

    def _accepted_attempt(self, attempt_id: str, event: Mapping[str, Any]) -> None:
        with transaction(self.connection):
            self.connection.execute(
                "UPDATE capture_attempts SET status='accepted',accepted_at=? WHERE attempt_id=?",
                (event.get("timestamp") or utc_now(), attempt_id),
            )

    def _require_completion(
        self,
        *,
        session_id: str,
        command_id: str,
        expected_success: bool,
    ) -> None:
        timeout = float(self.capture_config.get("command_completion_timeout_seconds", 5.0))
        try:
            event = self.runtime.wait_for_completion(
                command_id=command_id,
                timeout_seconds=timeout,
                session_id=session_id,
            )
        except (OSError, ProtocolError, RuntimeTimeout) as error:
            raise SessionProtocolError(
                f"CET did not complete command {command_id}; aborting session: {error}"
            ) from error
        if event.get("success") is not expected_success:
            raise SessionProtocolError(
                f"CET completed command {command_id} with success={event.get('success')!r}; "
                f"expected {expected_success!r}"
            )

    def _save_capture(
        self,
        *,
        session_id: str,
        attempt_id: str,
        command_id: str,
        place: sqlite3.Row,
        image: Any,
        event: Mapping[str, Any],
        validation: Mapping[str, Any],
        sent_monotonic: float,
        ready_monotonic: float,
        captured_monotonic: float,
    ) -> str:
        capture_id = stable_id("capture", session_id, command_id)
        runtime_location = event.get("runtime_location")
        runtime_location = (
            runtime_location if isinstance(runtime_location, Mapping) else {}
        )
        spatial = {
            field: place[field]
            for field in (
                "nearest_fast_travel_name",
                "nearest_street_name",
                "district",
                "subdistrict",
                "named_area",
                "interior_state",
            )
        }
        if not runtime_location.get("named_area") and not spatial.get("named_area"):
            spatial.update(
                _nearest_runtime_area(
                    self.connection,
                    float(place["requested_x"]),
                    float(place["requested_y"]),
                    float(
                        self.config.get("metadata_rules", {}).get(
                            "runtime_area_fallback_m", 500.0
                        )
                    ),
                )
            )
        overrides = {
            row["field_name"]: json.loads(row["value_json"])
            for row in self.connection.execute(
                "SELECT field_name,value_json FROM metadata_overrides WHERE target_type='place' AND target_id=?",
                (place["location_id"],),
            )
        }
        resolved, runtime_provenance = resolve_metadata(
            runtime_location, spatial, overrides
        )
        directory = (
            self.captures_root
            / _safe_area_name(resolved.get("named_area"))
            / place["location_id"]
        )
        png_path = directory / f"{capture_id}.png"
        sidecar_path = directory / f"{capture_id}.json"
        thumbnail_path = directory / f"{capture_id}.webp"
        _atomic_save_image(image, png_path, "PNG", optimize=False)
        thumbnail = image.copy()
        thumbnail.thumbnail(
            (int(self.capture_config.get("thumbnail_width", 480)), 10000)
        )
        _atomic_save_image(thumbnail, thumbnail_path, "WEBP", lossless=True, method=6)
        image_hash = _sha256(png_path)
        thumbnail_hash = _sha256(thumbnail_path)
        review_status = (
            "resolved"
            if all(resolved.get(field) for field in REQUIRED_NAME_FIELDS)
            else "needs_metadata"
        )
        actual_pose = event.get("actual_pose", {})
        effective_pose = event.get("effective_pose")
        if not isinstance(effective_pose, Mapping):
            effective_pose = {
                "x": place["requested_x"],
                "y": place["requested_y"],
                "z": place["requested_z"],
                "yaw": place["requested_yaw"],
                "pitch": place["requested_pitch"],
                "roll": place["requested_roll"],
            }
        anchor_tags: list[str] = []
        anchor_roles: list[str] = []
        if place["anchor_feature_id"]:
            anchor_feature = self.connection.execute(
                "SELECT tags,metadata_json FROM features WHERE feature_id=?",
                (place["anchor_feature_id"],),
            ).fetchone()
            if anchor_feature:
                anchor_tags = str(anchor_feature["tags"] or "").split()
                anchor_metadata = json.loads(anchor_feature["metadata_json"] or "{}")
                anchor_roles = [
                    str(role) for role in anchor_metadata.get("anchor_roles", [])
                ]
        sidecar = {
            "schema_version": 1,
            "capture_id": capture_id,
            "session_id": session_id,
            "attempt_id": attempt_id,
            "command_id": command_id,
            "location_id": place["location_id"],
            "planned_pose": {
                "x": place["requested_x"],
                "y": place["requested_y"],
                "z": place["requested_z"],
                "yaw": place["requested_yaw"],
                "pitch": place["requested_pitch"],
                "roll": place["requested_roll"],
                "forward": {
                    "x": place["forward_x"],
                    "y": place["forward_y"],
                    "z": place["forward_z"],
                },
            },
            "requested_pose": {
                "x": place["requested_x"],
                "y": place["requested_y"],
                "z": place["requested_z"],
                "yaw": place["requested_yaw"],
                "pitch": place["requested_pitch"],
                "roll": place["requested_roll"],
            },
            "effective_pose": dict(effective_pose),
            "actual_pose": actual_pose,
            "actual_fov": event.get("actual_fov"),
            "runtime_location": event.get("runtime_location", {}),
            "readiness": event.get("readiness", {}),
            "validation": validation,
            "game_profile": self.game_profile,
            "capture_profile": self.capture_config["profile"],
            "dimensions": {"width": image.width, "height": image.height},
            "anchor": {
                "category": place["category"],
                "direction": place["direction"],
                "feature_id": place["anchor_feature_id"],
                "resource": place["resource_path"],
                "source_sector": place["source_sector"],
                "road_id": place["road_id"],
                "tags": anchor_tags,
                "roles": anchor_roles,
            },
            "location_metadata": {
                "nearest_fast_travel": {
                    "stable_id": place["nearest_fast_travel_id"],
                    "name": resolved.get("nearest_fast_travel_name"),
                    "x": place["nearest_fast_travel_x"],
                    "y": place["nearest_fast_travel_y"],
                    "z": place["nearest_fast_travel_z"],
                    "horizontal_distance_m": place["nearest_fast_travel_distance_m"],
                },
                "nearest_street": {
                    "road_id": place["nearest_street_road_id"],
                    "name": resolved.get("nearest_street_name"),
                    "closest_x": place["nearest_street_x"],
                    "closest_y": place["nearest_street_y"],
                    "closest_z": place["nearest_street_z"],
                    "horizontal_distance_m": place["nearest_street_distance_m"],
                },
                "district": resolved.get("district"),
                "subdistrict": resolved.get("subdistrict"),
                "named_area": resolved.get("named_area"),
                "interior_state": resolved.get("interior_state"),
                "review_status": review_status,
            },
            "rules": {
                "extraction": place["extraction_rule_version"],
                "placement": place["placement_rule_version"],
            },
            "metadata_provenance": {
                **json.loads(place["provenance_json"]),
                **runtime_provenance,
            },
            "files": {
                "png": str(png_path),
                "thumbnail": str(thumbnail_path),
                "png_sha256": image_hash,
                "thumbnail_sha256": thumbnail_hash,
            },
            "captured_at": utc_now(),
            "latency": {
                "teleport_to_ready_ms": event.get("teleport_to_ready_ms"),
                "ready_to_capture_ms": (captured_monotonic - ready_monotonic) * 1000.0,
                "total_capture_ms": (captured_monotonic - sent_monotonic) * 1000.0,
            },
        }
        atomic_write_json(sidecar_path, sidecar)
        metadata_hash = _sha256(sidecar_path)
        validation_status = (
            "valid" if validation.get("publication_ready") else "needs_ui_review"
        )
        with transaction(self.connection):
            self.connection.execute(
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
            self.connection.execute(
                """INSERT INTO captures(capture_id,attempt_id,location_id,png_path,sidecar_path,
                       thumbnail_path,width,height,image_sha256,metadata_sha256,thumbnail_sha256,
                       captured_at,validation_status,validation_json)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    capture_id,
                    attempt_id,
                    place["location_id"],
                    str(png_path),
                    str(sidecar_path),
                    str(thumbnail_path),
                    image.width,
                    image.height,
                    image_hash,
                    metadata_hash,
                    thumbnail_hash,
                    sidecar["captured_at"],
                    validation_status,
                    json_text(validation),
                ),
            )
            self.connection.execute(
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
                    json_text(
                        {**json.loads(place["provenance_json"]), **runtime_provenance}
                    ),
                    utc_now(),
                    place["location_id"],
                ),
            )
        return capture_id

    def _capture_place(
        self, session_id: str, place: sqlite3.Row
    ) -> tuple[bool, str | None]:
        maximum_attempts = int(self.capture_config.get("maximum_attempts", 1))
        last_error: str | None = None
        for attempt_number in range(1, maximum_attempts + 1):
            attempt_id = f"attempt_{uuid.uuid4().hex}"
            command_id = f"command_{uuid.uuid4().hex}"
            self._insert_attempt(
                attempt_id=attempt_id,
                session_id=session_id,
                location_id=place["location_id"],
                command_id=command_id,
                attempt_number=attempt_number,
            )
            sent = time.monotonic()
            try:
                self.runtime.heartbeat(session_id)
                self.runtime.send(self._command(session_id, command_id, place))
                accepted = self.runtime.wait_for_event(
                    command_id=command_id,
                    accepted_types={"accepted"},
                    timeout_seconds=float(
                        self.capture_config.get("command_accept_timeout_seconds", 5.0)
                    ),
                    session_id=session_id,
                )
                self._accepted_attempt(attempt_id, accepted)
                event = self.runtime.wait_for_event(
                    command_id=command_id,
                    accepted_types={"ready"},
                    timeout_seconds=float(
                        self.capture_config.get("loading_timeout_seconds", 45.0)
                    ),
                    session_id=session_id,
                )
                ready = time.monotonic()
                ready_report = validate_ready_event(event, place, self.capture_config)
                if not ready_report["valid"]:
                    raise ValidationError(ready_report)
                validation_config = self.capture_config.get("validation", {})
                heartbeat_stop = threading.Event()

                def keep_controller_alive() -> None:
                    while not heartbeat_stop.is_set():
                        try:
                            self.runtime.heartbeat(session_id)
                        except OSError:
                            pass
                        heartbeat_stop.wait(0.5)

                heartbeat_thread = threading.Thread(
                    target=keep_controller_alive,
                    name="world-capture-heartbeat",
                    daemon=True,
                )
                heartbeat_thread.start()
                try:
                    image = self.window.capture(
                        int(self.capture_config["width"]),
                        int(self.capture_config["height"]),
                        visual_settle_seconds=float(
                            self.capture_config.get("visual_settle_seconds", 2.0)
                        ),
                        visual_timeout_seconds=float(
                            self.capture_config.get("loading_timeout_seconds", 45.0)
                        ),
                        black_pixel_threshold=int(
                            validation_config.get("black_pixel_threshold", 8)
                        ),
                        black_fraction_threshold=float(
                            validation_config.get("black_fraction_threshold", 0.98)
                        ),
                    )
                finally:
                    heartbeat_stop.set()
                    heartbeat_thread.join(timeout=1.0)
                captured = time.monotonic()
                if image.size != (
                    int(self.capture_config["width"]),
                    int(self.capture_config["height"]),
                ):
                    raise CaptureError(
                        f"captured image has unexpected dimensions {image.size}"
                    )
                validation = validate_image(
                    image,
                    ready_report=ready_report,
                    validation_config=validation_config,
                    config_root=self.config_root,
                )
                if not validation["valid"]:
                    raise ValidationError(validation)
                capture_id = self._save_capture(
                    session_id=session_id,
                    attempt_id=attempt_id,
                    command_id=command_id,
                    place=place,
                    image=image,
                    event=event,
                    validation=validation,
                    sent_monotonic=sent,
                    ready_monotonic=ready,
                    captured_monotonic=captured,
                )
                try:
                    self.runtime.acknowledge(
                        command_id, True, {"capture_id": capture_id}
                    )
                except OSError as error:
                    raise SessionProtocolError(
                        f"could not acknowledge completed capture {command_id}: {error}"
                    ) from error
                # The image and database rows are already committed.  A missing
                # CET completion is fatal to the session, but never converts the
                # committed capture into another location attempt.
                self._require_completion(
                    session_id=session_id,
                    command_id=command_id,
                    expected_success=True,
                )
                return True, None
            except (
                CaptureError,
                ProtocolError,
                RuntimeTimeout,
                ValidationError,
            ) as error:
                last_error = str(error)
                code = type(error).__name__
                self._failed_attempt(attempt_id, code, last_error)
                try:
                    self.runtime.acknowledge(command_id, False, {"error": last_error})
                except OSError as ack_error:
                    raise SessionProtocolError(
                        f"could not reject command {command_id}: {ack_error}"
                    ) from ack_error
                # Do not issue a retry until CET has consumed the negative ack,
                # restored capture mode, and explicitly returned to idle.
                self._require_completion(
                    session_id=session_id,
                    command_id=command_id,
                    expected_success=False,
                )
        with transaction(self.connection):
            self.connection.execute(
                """UPDATE places SET queue_status='failed',failure_code='attempts_exhausted',
                       failure_detail=?,updated_at=? WHERE location_id=?""",
                (last_error, utc_now(), place["location_id"]),
            )
        return False, last_error

    def _restore(self, session_id: str) -> bool:
        command_id = f"command_{uuid.uuid4().hex}"
        command = {
            "schema_version": PROTOCOL_SCHEMA_VERSION,
            "kind": "restore",
            "session_id": session_id,
            "command_id": command_id,
        }
        try:
            self.runtime.send(command)
            event = self.runtime.wait_for_event(
                command_id=command_id,
                accepted_types={"restored"},
                timeout_seconds=5.0,
                session_id=session_id,
            )
            return event.get("restoration_verified") is True
        except (OSError, ProtocolError):
            return False

    def run(self, *, limit: int | None = None) -> dict[str, Any]:
        maximum_age = float(self.capture_config.get("heartbeat_timeout_seconds", 5.0))
        self.runtime.assert_runtime_alive(maximum_age_seconds=maximum_age)
        self.runtime.prepare()
        recover_interrupted_queue(self.connection)
        session_id = f"session_{uuid.uuid4().hex}"
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                       runtime_path,started_at,status) VALUES(?,?,?,?,?,'running')""",
                (
                    session_id,
                    self.game_profile,
                    json_text(self.capture_config["profile"]),
                    str(self.runtime.root),
                    utc_now(),
                ),
            )
        query = """SELECT * FROM places
                   WHERE queue_status='pending' AND scope_status='in_scope'
                   ORDER BY queue_order,location_id"""
        parameters: tuple[Any, ...] = ()
        if limit is not None:
            query += " LIMIT ?"
            parameters = (limit,)
        places = self.connection.execute(query, parameters).fetchall()
        captured = 0
        failed = 0
        fatal_error: str | None = None
        progress_started = time.monotonic()
        progress_width = 0

        def show_progress(completed: int, activity: str, *, final: bool = False) -> None:
            nonlocal progress_width
            total = len(places)
            elapsed = time.monotonic() - progress_started
            percent = (completed / total * 100.0) if total else 100.0
            eta = (
                elapsed / completed * (total - completed)
                if completed and completed < total
                else 0.0
            )
            line = (
                f"[capture] {completed}/{total} ({percent:5.1f}%) "
                f"captured={captured} failed={failed} "
                f"elapsed={elapsed:.1f}s eta={eta:.1f}s | {activity}"
            )
            if sys.stderr.isatty():
                progress_width = max(progress_width, len(line))
                print(
                    "\r" + line.ljust(progress_width),
                    end="\n" if final else "",
                    file=sys.stderr,
                    flush=True,
                )
            else:
                print(line, file=sys.stderr, flush=True)

        try:
            for index, place in enumerate(places, start=1):
                show_progress(
                    index - 1,
                    f"capturing {index}/{len(places)} {place['location_id']}",
                )
                success, _detail = self._capture_place(session_id, place)
                captured += int(success)
                failed += int(not success)
        except BaseException as error:
            fatal_error = f"{type(error).__name__}: {error}"
            raise
        finally:
            show_progress(captured + failed, "restoring game state")
            restored = self._restore(session_id)
            with transaction(self.connection):
                self.connection.execute(
                    """UPDATE capture_sessions SET ended_at=?,status=?,restoration_verified=?,error=?
                       WHERE session_id=?""",
                    (
                        utc_now(),
                        "completed" if restored and fatal_error is None else "error",
                        int(restored),
                        fatal_error,
                        session_id,
                    ),
                )
                if restored:
                    self.connection.execute(
                        """UPDATE places SET publishable=1 WHERE queue_status='captured'
                           AND review_status='resolved' AND EXISTS(
                              SELECT 1 FROM captures c
                              JOIN capture_attempts a ON a.attempt_id=c.attempt_id
                              JOIN capture_sessions s ON s.session_id=a.session_id
                              WHERE c.location_id=places.location_id
                                AND c.validation_status='valid'
                                AND s.restoration_verified=1
                           )"""
                    )
            show_progress(
                captured + failed,
                "complete" if restored else "complete; restoration not verified",
                final=True,
            )
        return {
            "session_id": session_id,
            "selected": len(places),
            "captured": captured,
            "failed": failed,
            "restoration_verified": restored,
        }
