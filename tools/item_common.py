"""Shared item authoring paths, types and file helpers."""

from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from typing import Any



from artifact_io import atomic_write_json
from toolchain import default_tool_path

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_GAME = default_tool_path("game")

DEFAULT_WOLVENKIT = default_tool_path("wolvenkit")

DEFAULT_KRAKEN = default_tool_path("kraken")

DEFAULT_GHOSTLINE_RED = default_tool_path("ghostline_red")

DEFAULT_RED_SCHEMA = ROOT / "red-schema.json"

DEFAULT_BLENDER = default_tool_path("blender")

DEFAULT_OUTPUT = ROOT / "converted/item-database"

DEFAULT_INDEX = ROOT / "converted/character-index/assets.json"

DEFAULT_TWEAK_ROOT = (
    DEFAULT_GAME / "tools/redmod/tweaks/base/gameplay/static_data/database/items"
)

GALLERY_ROOT = ROOT / "tools/item_gallery"

BLENDER_SCRIPT = ROOT / "tools/item_render_blender.py"

SCHEMA_VERSION = 1

RECORD_HEADER = re.compile(
    r"(?m)^[ \t]*(?P<name>[A-Za-z_][A-Za-z0-9_]*)"
    r"[ \t]*:[ \t]*(?P<parent>[A-Za-z_][A-Za-z0-9_.]*)[ \t\r\n]*\{"
)

PACKAGE_LINE = re.compile(r"(?m)^[ \t]*package[ \t]+([A-Za-z_][A-Za-z0-9_.]*)")

ATTRIBUTE_BLOCK = re.compile(r"\[\s*(?P<attrs>[^\]]+)\]\s*$", re.MULTILINE)

STRING_PROPERTY = re.compile(
    r"(?m)^[ \t]*(?:[A-Za-z_][A-Za-z0-9_<>\[\], \t]*[ \t]+)?"
    r"(?P<key>displayName|localizedDescription|appearanceName|entityName|"
    r"equipArea|itemType)[ \t]*=[ \t]*\"(?P<value>[^\"]*)\"[ \t]*;"
)

TAGS_PROPERTY = re.compile(
    r"(?ms)^[ \t]*(?:CName\[\][ \t]+)?tags[ \t]*\+?=\s*\[(?P<body>.*?)\][ \t]*;"
)

QUOTED_STRING = re.compile(r"\"([^\"]+)\"")

LOC_KEY = re.compile(r"^LocKey#(.+)$", re.IGNORECASE)

FRAME_SUFFIX = re.compile(r"_(?P<frame>m|w)$", re.IGNORECASE)

FRAME_TOKEN = re.compile(r"(?:^|_)(?P<frame>pma|pwa|ma|wa)(?:_|$)", re.IGNORECASE)

EQUIPMENT_SLOTS = {
    "EquipmentArea.Feet": "feet",
    "EquipmentArea.LegArmor": "legs",
    "EquipmentArea.InnerChest": "inner_torso",
    "EquipmentArea.ChestArmor": "outer_torso",
    "EquipmentArea.HeadArmor": "head",
    "EquipmentArea.FaceArmor": "face",
    "EquipmentArea.Outfit": "outfit",
    "EquipmentArea.UnderwearTop": "underwear_top",
    "EquipmentArea.UnderwearBottom": "underwear_bottom",
}

FRAME_LABELS = {"m": "pma", "w": "pwa"}

PRIMARY_COMPONENT_TYPES = {
    "entGarmentSkinnedMeshComponent",
    "entSkinnedMeshComponent",
    "entMeshComponent",
}

class ItemDatabaseError(RuntimeError):
    pass

def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ItemDatabaseError(f"Unable to read JSON {path}: {exc}") from exc

def write_json(path: Path, value: Any) -> None:
    atomic_write_json(path, value)

def file_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }

def sha1_text(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()
