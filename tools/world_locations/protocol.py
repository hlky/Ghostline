"""Atomic file protocol shared by the Python controller and CET Lua runtime."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import json
import os
from pathlib import Path
import time
from typing import Any, Iterable, Mapping
import uuid

from . import PROTOCOL_SCHEMA_VERSION


class ProtocolError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "protocol_error",
        event: Mapping[str, Any] | None = None,
    ):
        self.code = code
        self.event = dict(event or {})
        super().__init__(message)


class RuntimeTimeout(ProtocolError):
    pass


def timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds")


def _unlink_protocol_file(path: Path) -> None:
    """Remove a protocol file, tolerating CET's short-lived Windows read lock."""
    deadline = time.monotonic() + 0.25
    while True:
        try:
            path.unlink()
            return
        except FileNotFoundError:
            return
        except PermissionError:
            if time.monotonic() >= deadline:
                raise
            time.sleep(0.001)


def atomic_write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp")
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    # CET opens these tiny files without Windows delete sharing. If its read
    # overlaps this replace, retry only for the lifetime of that sharing
    # violation; successful writes have no minimum delay.
    deadline = time.monotonic() + 0.25
    try:
        while True:
            try:
                os.replace(temporary, path)
                break
            except PermissionError:
                if time.monotonic() >= deadline:
                    raise
                time.sleep(0.001)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        except OSError:
            # Preserve the replace error; a uniquely named orphan is harmless
            # and will never be consumed as a protocol file.
            pass


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
    except FileNotFoundError:
        return None
    except (OSError, json.JSONDecodeError) as error:
        raise ProtocolError(f"malformed protocol file {path}: {error}") from error
    if not isinstance(value, dict):
        raise ProtocolError(f"protocol file must contain an object: {path}")
    return value


@dataclass(slots=True)
class RuntimeProtocol:
    root: Path
    poll_seconds: float = 0.01

    @property
    def command_path(self) -> Path:
        return self.root / "command.json"

    @property
    def event_paths(self) -> dict[str, Path]:
        return {
            name: self.root / f"event-{name}.json"
            for name in (
                "accepted",
                "teleported",
                "ready",
                "completed",
                "error",
                "restored",
            )
        }

    @property
    def ack_path(self) -> Path:
        return self.root / "ack.json"

    @property
    def controller_heartbeat_path(self) -> Path:
        return self.root / "controller-heartbeat.json"

    @property
    def cet_heartbeat_path(self) -> Path:
        return self.root / "cet-heartbeat.json"

    def prepare(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        for path in (self.command_path, self.ack_path, *self.event_paths.values()):
            _unlink_protocol_file(path)

    def heartbeat(self, session_id: str) -> None:
        atomic_write_json(
            self.controller_heartbeat_path,
            {
                "schema_version": PROTOCOL_SCHEMA_VERSION,
                "session_id": session_id,
                "timestamp": timestamp(),
                "monotonic_ms": time.monotonic_ns() // 1_000_000,
                "unix_seconds": time.time(),
            },
        )

    def send(self, command: Mapping[str, Any]) -> None:
        if (
            type(command.get("schema_version")) is not int
            or command["schema_version"] != PROTOCOL_SCHEMA_VERSION
        ):
            raise ProtocolError("command has an unsupported schema_version")
        for required in ("session_id", "command_id", "kind"):
            if not command.get(required):
                raise ProtocolError(f"command is missing {required}")
        for path in (self.ack_path, *self.event_paths.values()):
            _unlink_protocol_file(path)
        atomic_write_json(self.command_path, command)

    def acknowledge(
        self,
        command_id: str,
        success: bool,
        detail: Mapping[str, Any] | None = None,
        *,
        session_id: str,
    ) -> None:
        atomic_write_json(
            self.ack_path,
            {
                "schema_version": PROTOCOL_SCHEMA_VERSION,
                "session_id": session_id,
                "command_id": command_id,
                "success": success,
                "detail": dict(detail or {}),
                "timestamp": timestamp(),
            },
        )

    def wait_for_event(
        self,
        *,
        command_id: str,
        accepted_types: Iterable[str],
        timeout_seconds: float,
        session_id: str,
    ) -> dict[str, Any]:
        accepted = set(accepted_types)
        deadline = time.monotonic() + timeout_seconds
        next_heartbeat = 0.0
        last_malformed: str | None = None
        while True:
            now = time.monotonic()
            if now >= next_heartbeat:
                self.heartbeat(session_id)
                next_heartbeat = now + 0.5
            for event_type in ("error", *sorted(accepted)):
                try:
                    event = read_json(self.event_paths[event_type])
                except ProtocolError as error:
                    last_malformed = str(error)
                    event = None
                if not event or event.get("command_id") != command_id:
                    continue
                if event.get("session_id") != session_id:
                    raise ProtocolError(
                        "runtime event belongs to a different session",
                        code="session_mismatch",
                        event=event,
                    )
                if (
                    type(event.get("schema_version")) is not int
                    or event["schema_version"] != PROTOCOL_SCHEMA_VERSION
                ):
                    raise ProtocolError(
                        "runtime event has an unsupported schema_version"
                    )
                if event.get("event") != event_type:
                    raise ProtocolError(
                        f"event filename/type mismatch for {event_type}"
                    )
                if event_type == "error":
                    raise ProtocolError(
                        f"CET runtime error {event.get('error_code', 'unknown')}: "
                        f"{event.get('error_detail', '')}",
                        code=str(event.get("error_code", "runtime_error")),
                        event=event,
                    )
                return event
            if now >= deadline:
                suffix = (
                    f"; last malformed event: {last_malformed}"
                    if last_malformed
                    else ""
                )
                raise RuntimeTimeout(
                    f"timed out waiting for {sorted(accepted)} for command {command_id}{suffix}"
                )
            # This is only file-notification polling. It is not a post-teleport
            # readiness delay: a ready event is consumed on the next poll.
            time.sleep(self.poll_seconds)

    def wait_for_completion(
        self,
        *,
        command_id: str,
        timeout_seconds: float,
        session_id: str,
    ) -> dict[str, Any]:
        """Wait for CET to consume an acknowledgement and become idle.

        An error event for this command is expected to remain present while
        the controller acknowledges a failed attempt.  Reusing
        ``wait_for_event`` would reread that stale error before CET has a
        chance to emit ``completed`` and would let the next command overwrite
        the acknowledgement.  Completion is therefore a separate barrier
        that observes only the matching terminal event.
        """
        deadline = time.monotonic() + timeout_seconds
        next_heartbeat = 0.0
        last_malformed: str | None = None
        path = self.event_paths["completed"]
        while True:
            now = time.monotonic()
            if now >= next_heartbeat:
                self.heartbeat(session_id)
                next_heartbeat = now + 0.5
            try:
                event = read_json(path)
            except ProtocolError as error:
                last_malformed = str(error)
                event = None
            if event and event.get("command_id") == command_id:
                if event.get("session_id") != session_id:
                    raise ProtocolError(
                        "runtime completion belongs to a different session",
                        code="session_mismatch",
                        event=event,
                    )
                if (
                    type(event.get("schema_version")) is not int
                    or event["schema_version"] != PROTOCOL_SCHEMA_VERSION
                ):
                    raise ProtocolError(
                        "runtime completion has an unsupported schema_version"
                    )
                if event.get("event") != "completed":
                    raise ProtocolError("event filename/type mismatch for completed")
                return event
            if now >= deadline:
                suffix = (
                    f"; last malformed event: {last_malformed}"
                    if last_malformed
                    else ""
                )
                raise RuntimeTimeout(
                    f"timed out waiting for completion of command {command_id}{suffix}"
                )
            time.sleep(self.poll_seconds)

    def assert_runtime_alive(self, *, maximum_age_seconds: float) -> dict[str, Any]:
        heartbeat = read_json(self.cet_heartbeat_path)
        # Lua's Windows rename briefly removes the preceding heartbeat. A
        # bounded transport retry prevents that gap from rejecting good frames.
        deadline = time.monotonic() + 0.05
        while heartbeat is None and time.monotonic() < deadline:
            time.sleep(0.001)
            heartbeat = read_json(self.cet_heartbeat_path)
        if not heartbeat:
            raise ProtocolError(f"CET heartbeat not found in {self.root}")
        if (
            type(heartbeat.get("schema_version")) is not int
            or heartbeat["schema_version"] != PROTOCOL_SCHEMA_VERSION
        ):
            raise ProtocolError("CET heartbeat has an unsupported schema_version")
        try:
            age = time.time() - self.cet_heartbeat_path.stat().st_mtime
        except OSError as error:
            raise ProtocolError(f"cannot stat CET heartbeat: {error}") from error
        if age > maximum_age_seconds:
            raise ProtocolError(f"CET heartbeat is stale ({age:.2f}s old)")
        return heartbeat

    def capture_evidence(
        self,
        *,
        session_id: str,
        command_id: str,
        minimum_frame: int,
        maximum_age_seconds: float,
    ) -> dict[str, Any]:
        """Check the same destination is still ready while frames are settling."""
        error = read_json(self.event_paths["error"])
        if error and error.get("command_id") == command_id:
            if error.get("session_id") != session_id:
                raise ProtocolError(
                    "runtime error belongs to a different session",
                    code="session_mismatch",
                    event=error,
                )
            raise ProtocolError(
                f"CET runtime error {error.get('error_code', 'unknown')}: {error.get('error_detail', '')}",
                code=str(error.get("error_code", "runtime_error")),
                event=error,
            )
        heartbeat = self.assert_runtime_alive(maximum_age_seconds=maximum_age_seconds)
        if (
            heartbeat.get("session_id") != session_id
            or heartbeat.get("command_id") != command_id
        ):
            raise ProtocolError(
                "capture heartbeat does not match the active destination",
                code="session_mismatch",
                event=heartbeat,
            )
        frame = heartbeat.get("frame")
        if (
            heartbeat.get("stage") != "ready"
            or type(frame) is not int
            or frame < minimum_frame
        ):
            raise ProtocolError(
                "CET is no longer ready for this capture",
                code="readiness_lost",
                event=heartbeat,
            )
        return heartbeat
