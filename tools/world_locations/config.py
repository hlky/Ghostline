"""Versioned configuration loading and path resolution."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "world-location-capture-v1.json"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config(path: Path | None = None) -> dict[str, Any]:
    selected = (path or DEFAULT_CONFIG).resolve()
    config = json.loads(selected.read_text(encoding="utf-8"))
    if config.get("schema_version") != 1:
        raise ValueError(f"unsupported config schema: {config.get('schema_version')!r}")
    config["_config_path"] = str(selected)
    return config


def resolve_project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (PROJECT_ROOT / path).resolve()


def output_paths(config: dict[str, Any]) -> dict[str, Path]:
    root = resolve_project_path(config["output_root"])
    return {
        "root": root,
        "database": root / config.get("database", "locations.sqlite3"),
        "runtime": root / config.get("runtime", "runtime"),
        "captures": root / config.get("captures", "captures"),
        "reports": root / config.get("reports", "reports"),
        "exports": root / config.get("exports", "exports"),
    }
