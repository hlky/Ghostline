"""Resolve workstation tools once, without requiring them for pure authoring imports."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import shutil
from types import MappingProxyType
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "toolchain.local.json"
ENVIRONMENT = {
    "blender": "GHOSTLINE_BLENDER",
    "wolvenkit": "GHOSTLINE_WOLVENKIT",
    "game": "GHOSTLINE_GAME",
    "kraken": "GHOSTLINE_KRAKEN",
    "ghostline_red": "GHOSTLINE_RED",
    "ghostline_voice": "GHOSTLINE_VOICE",
}
COMMANDS = {
    "blender": "blender",
    "wolvenkit": "WolvenKit.CLI",
    "ghostline_red": "ghostline-red",
    "ghostline_voice": "ghostline-voice",
}


def _configuration() -> dict[str, str]:
    if not CONFIG_PATH.is_file():
        return {}
    value = json.loads(CONFIG_PATH.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict) or any(
        key not in ENVIRONMENT or not isinstance(path, str) or not path.strip()
        for key, path in value.items()
    ):
        raise ValueError(f"{CONFIG_PATH} must map known tool names to nonempty paths")
    return value


def _installed_candidates(name: str) -> list[Path]:
    suffix = ".exe" if os.name == "nt" else ""
    if name.startswith("ghostline_"):
        return [ROOT / "tools" / name.replace("_", "-") / "target/release" / (name.replace("_", "-") + suffix)]
    if name == "blender":
        foundation = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Blender Foundation"
        versions = sorted(foundation.glob("Blender */blender.exe"), reverse=True)
        return versions + [
            foundation / "Blender 5.1/blender.exe",
            Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Steam/steamapps/common/Blender/blender.exe",
        ]
    if name == "wolvenkit":
        return [Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")]
    if name == "game":
        return [Path(r"H:\Cyberpunk 2077")]
    if name == "kraken":
        return [resolve_tool("wolvenkit", required=False).parent / "kraken.dll"]
    raise ValueError(f"Unknown tool: {name}")


def _valid(name: str, path: Path) -> bool:
    if name == "game":
        return path.is_dir() and (path / "bin/x64/Cyberpunk2077.exe").is_file()
    return path.is_file()


def resolve_tool(name: str, explicit: Path | str | None = None, *, required: bool = True) -> Path:
    """Explicit, environment and local config choices never silently fall back.

    ``required=False`` resolves defaults for argument parsers and optional adapters;
    call with ``required=True`` at the boundary that actually needs the tool.
    """
    if name not in ENVIRONMENT:
        raise ValueError(f"Unknown tool: {name}")
    configured = explicit if explicit is not None else os.environ.get(ENVIRONMENT[name])
    if configured is None:
        configured = _configuration().get(name)
    if configured is not None:
        selected = Path(configured).expanduser()
        if not selected.is_absolute():
            selected = ROOT / selected
    else:
        discovered = shutil.which(COMMANDS[name]) if name in COMMANDS else None
        candidates = ([Path(discovered)] if discovered else []) + _installed_candidates(name)
        selected = next((path for path in candidates if _valid(name, path)), candidates[0])
    selected = selected.resolve()
    if required and not _valid(name, selected):
        raise FileNotFoundError(f"{name} was not found at {selected}; pass an explicit path or set {ENVIRONMENT[name]}")
    return selected


def default_tool_path(name: str) -> Path:
    return resolve_tool(name, required=False)


@dataclass(frozen=True)
class Toolchain:
    """An immutable operation-scoped snapshot; resolve only the tools it uses."""

    paths: Mapping[str, Path]

    @classmethod
    def resolve(cls, **tools: Path | str | None) -> "Toolchain":
        return cls(MappingProxyType({name: resolve_tool(name, path) for name, path in tools.items()}))

    def __getitem__(self, name: str) -> Path:
        return self.paths[name]
