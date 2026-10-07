"""Install and retrieve the Black Lantern CET world-scout log."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CET_SOURCE = ROOT / "tools/gq003_black_lantern_scout_cet/init.lua"
CET_MOD_NAME = "ghostline_gq003_scout"
LOG_NAME = "black-lantern-locations.json"
DEFAULT_OUTPUT = ROOT / "projects/ghostline/quests/gq003/implementation/world-candidates.json"


def cet_mod_directory(game_root: Path) -> Path:
    cet_root = game_root.resolve() / "bin/x64/plugins/cyber_engine_tweaks"
    if not cet_root.is_dir():
        raise SystemExit(f"Cyber Engine Tweaks directory not found: {cet_root}")
    return cet_root / "mods" / CET_MOD_NAME


def validate_log(document: Any) -> dict[str, Any]:
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise ValueError("expected Black Lantern scout schema_version 1")
    if document.get("quest") != "gq003" or not isinstance(document.get("captures"), list):
        raise ValueError("expected a gq003 scout log with a captures array")
    for index, capture in enumerate(document["captures"]):
        if not isinstance(capture, dict):
            raise ValueError(f"capture {index} is not an object")
        if not isinstance(capture.get("slot_id"), str):
            raise ValueError(f"capture {index} has no slot_id")
        if not isinstance(capture.get("target_id"), str):
            raise ValueError(f"capture {index} has no target_id")
        if "role_id" in capture and not isinstance(capture["role_id"], str):
            raise ValueError(f"capture {index} has an invalid role_id")
        position = capture.get("position")
        if not isinstance(position, dict) or not all(
            isinstance(position.get(axis), (int, float)) for axis in ("x", "y", "z")
        ):
            raise ValueError(f"capture {index} has no numeric XYZ position")
    return document


def install(game_root: Path, *, force: bool = False) -> Path:
    destination = cet_mod_directory(game_root)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "init.lua"
    if target.exists() and not force and target.read_bytes() != CET_SOURCE.read_bytes():
        raise SystemExit(f"refusing to overwrite modified CET file without --force: {target}")
    shutil.copyfile(CET_SOURCE, target)
    return destination


def import_log(source: Path, output: Path, *, force: bool = False) -> dict[str, Any]:
    if not source.is_file():
        raise SystemExit(f"CET scout log not found: {source}")
    try:
        document = validate_log(json.loads(source.read_text(encoding="utf-8")))
    except (json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"invalid CET scout log: {error}") from error
    if output.exists() and not force:
        raise SystemExit(f"refusing to overwrite existing import without --force: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return document


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install-cet", help="Install the scout into an existing CET installation.")
    install_parser.add_argument("--game-root", type=Path, required=True)
    install_parser.add_argument("--force", action="store_true")

    import_parser = subparsers.add_parser("import-log", help="Copy and validate the CET scout log into gq003 authoring.")
    import_parser.add_argument("--game-root", type=Path, help="Cyberpunk 2077 root containing the installed scout.")
    import_parser.add_argument("--input", type=Path, help="Explicit black-lantern-locations.json path.")
    import_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    import_parser.add_argument("--force", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "install-cet":
        destination = install(args.game_root, force=args.force)
        print(json.dumps({"cet_mod": str(destination), "log": str(destination / LOG_NAME)}, indent=2))
        return

    if bool(args.game_root) == bool(args.input):
        raise SystemExit("import-log requires exactly one of --game-root or --input")
    source = args.input or (cet_mod_directory(args.game_root) / LOG_NAME)
    document = import_log(source, args.output.resolve(), force=args.force)
    print(json.dumps({"output": str(args.output.resolve()), "captures": len(document["captures"])}, indent=2))


if __name__ == "__main__":
    main()
