"""Read-only checks for unattended capture and a scoped Windows power request."""

from __future__ import annotations

from contextlib import contextmanager
import ctypes
from ctypes import wintypes
import importlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
from typing import Any, Iterator, Mapping

from .capture import GameWindow
from .database import connect_readonly, status_counts
from .protocol import RuntimeProtocol


@contextmanager
def keep_awake() -> Iterator[None]:
    """Hold system/display awake only on the controller's calling thread."""
    if sys.platform != "win32":
        yield
        return
    request = ctypes.windll.kernel32.SetThreadExecutionState
    request.argtypes = [wintypes.DWORD]
    request.restype = wintypes.DWORD
    previous = request(0x80000003)  # CONTINUOUS | SYSTEM_REQUIRED | DISPLAY_REQUIRED
    if not previous:
        raise OSError("Could not prevent Windows sleep for capture")
    try:
        yield
    finally:
        request(previous)


def check_preflight(
    config: Mapping[str, Any], paths: Mapping[str, Path], runtime: Path,
    *, game_root: Path | None = None,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def record(name: str, status: str, detail: Any) -> None:
        checks.append({"name": name, "status": status, "detail": detail})

    for module in ("PIL.Image", "numpy", "cv2", "ijson", "windows_capture"):
        try:
            importlib.import_module(module)
        except (ImportError, OSError) as error:
            record(module, "blocked", str(error))
        else:
            record(module, "ok", "importable")
    try:
        connection = connect_readonly(paths["database"])
        try:
            record("database", "ok", status_counts(connection))
            result = connection.execute("PRAGMA quick_check").fetchall()
            messages = [row[0] for row in result]
            record("database_integrity", "ok" if messages == ["ok"] else "blocked", messages)
        finally:
            connection.close()
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as error:
        record("database", "blocked", str(error))

    ancestor = paths["captures"].resolve()
    while not ancestor.exists() and ancestor != ancestor.parent:
        ancestor = ancestor.parent
    free = shutil.disk_usage(ancestor).free
    record("disk", "ok" if free >= 10 * 1024**3 else "blocked", {
        "free_gib": round(free / 1024**3, 1),
        "note": "10 GiB startup floor; full-queue space depends on image sizes",
    })
    descriptor = paths["runtime"] / "cet-runtime.json"
    if descriptor.is_file():
        value = json.loads(descriptor.read_text(encoding="utf-8"))
        mod = Path(value["cet_mod_path"])
        record("installed_bridge", "ok" if (mod / "init.lua").is_file() else "blocked", str(mod))
        record("runtime_descriptor", "ok" if Path(value["runtime_path"]).is_dir() else "blocked", value)
    else:
        record("runtime_descriptor", "blocked", "Run install-cet for the current game directory")
    if game_root is not None:
        mod = game_root / "bin/x64/plugins/cyber_engine_tweaks/mods/world_location_capture"
        source = Path(__file__).resolve().parents[1] / "world_location_capture_cet"
        for name, expected in (("init.lua", "init.lua"), ("config.json", "config.example.json")):
            target = mod / name
            matches = target.is_file() and target.read_bytes() == (source / expected).read_bytes()
            record(f"installed_{name}", "ok" if matches else "blocked", str(target))
        if (mod / "init.lua.disabled").is_file() and not (mod / "init.lua").is_file():
            record("disabled_runtime", "warning", "Disabled runtime retained; install-cet enables capture")
    capture = config["capture"]
    try:
        heartbeat = RuntimeProtocol(runtime).assert_runtime_alive(
            maximum_age_seconds=float(capture.get("heartbeat_timeout_seconds", 5)),
        )
        idle = (
            heartbeat.get("stage") == "idle"
            and heartbeat.get("capture_mode_active") is False
            and heartbeat.get("restoration_verified") is True
            and heartbeat.get("protection_contract_version") == 1
        )
        record("cet_heartbeat", "ok" if idle else "blocked", heartbeat)
        record("freefly", "ok" if heartbeat.get("freefly_active") is True else "blocked", "Activate FreeFly before capture; keep it active")
    except (OSError, RuntimeError) as error:
        record("cet_heartbeat", "blocked", str(error))
    try:
        window = GameWindow(capture["window_title_contains"], capture["window_process_name"])
        hwnd = window.find()
        left, top, right, bottom = window.client_rectangle(hwnd)
        size = [right - left, bottom - top]
        record("game_client", "ok" if size == [capture["width"], capture["height"]] else "blocked", size)
    except (OSError, RuntimeError) as error:
        record("game_client", "blocked", str(error))
    if not capture.get("validation", {}).get("hud_templates"):
        record("hud_templates", "warning", "Captures require UI review before publication")
    return {
        "ready": not any(check["status"] == "blocked" for check in checks),
        "python": sys.executable, "runtime": str(runtime), "checks": checks,
    }
