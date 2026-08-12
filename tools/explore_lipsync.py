#!/usr/bin/env python3
"""Inspect Cyberpunk 2077 lipsync animation sets exported as WolvenKit GLB."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, TextIO

from cr2w_helpers import bounded, print_json, print_table


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WOLVENKIT = ROOT / "WolvenKit/WolvenKit.CLI/bin/Release/net8.0/WolvenKit.CLI.exe"
GLB_MAGIC = b"glTF"
GLB_JSON_CHUNK = 0x4E4F534A
LINE_NAME = re.compile(r"^f_([0-9a-fA-F]{1,16})$")


@dataclass(frozen=True)
class LineInfo:
    index: int
    name: str
    locstring_id: str
    duration: float
    dynamic_tracks: int
    dynamic_keys: int
    const_tracks: int


@dataclass(frozen=True)
class TrackInfo:
    index: int
    name: str
    kind: str
    keys: int
    minimum: float
    maximum: float


@dataclass(frozen=True)
class TrackSample:
    line: str
    locstring_id: str
    track_index: int
    track_name: str
    kind: str
    time: float
    value: float


def read_glb_json(path: Path) -> dict[str, Any]:
    with path.open("rb") as stream:
        header = stream.read(12)
        if len(header) != 12:
            raise ValueError(f"{path}: truncated GLB header")
        magic, version, total_length = struct.unpack("<4sII", header)
        if magic != GLB_MAGIC or version != 2:
            raise ValueError(f"{path}: expected a glTF 2.0 GLB")
        if total_length != path.stat().st_size:
            raise ValueError(
                f"{path}: header length {total_length} does not match file size {path.stat().st_size}"
            )

        while stream.tell() < total_length:
            chunk_header = stream.read(8)
            if len(chunk_header) != 8:
                raise ValueError(f"{path}: truncated GLB chunk header")
            chunk_length, chunk_type = struct.unpack("<II", chunk_header)
            payload = stream.read(chunk_length)
            if len(payload) != chunk_length:
                raise ValueError(f"{path}: truncated GLB chunk")
            if chunk_type == GLB_JSON_CHUNK:
                return json.loads(payload.rstrip(b"\x00 \t\r\n"))
    raise ValueError(f"{path}: no JSON chunk found")


def discover_game_path() -> Path | None:
    configured = os.environ.get("CYBERPUNK_2077_PATH")
    if configured:
        candidate = Path(configured)
        if candidate.is_dir():
            return candidate
    if sys.platform != "win32":
        return None
    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\WOW6432Node\GOG.com\Games\1423049311",
        ) as key:
            candidate = Path(winreg.QueryValueEx(key, "path")[0])
            return candidate if candidate.is_dir() else None
    except (FileNotFoundError, OSError):
        return None


def export_anims(source: Path, output_dir: Path, wolvenkit: Path, game_path: Path) -> Path:
    if not wolvenkit.is_file():
        raise FileNotFoundError(f"WolvenKit CLI not found: {wolvenkit}")
    if not game_path.is_dir():
        raise FileNotFoundError(f"Cyberpunk game directory not found: {game_path}")
    command = [
        str(wolvenkit),
        "export",
        str(source),
        "-o",
        str(output_dir),
        "-gp",
        str(game_path),
        "-v",
        "Minimal",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    exported = output_dir / f"{source.name}.glb"
    if completed.returncode != 0 or not exported.is_file():
        details = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
        raise RuntimeError(f"WolvenKit failed to export {source}.{os.linesep}{details}".rstrip())
    return exported


def load_source(
    source: Path,
    wolvenkit: Path = DEFAULT_WOLVENKIT,
    game_path: Path | None = None,
) -> tuple[dict[str, Any], str]:
    if not source.is_file():
        raise FileNotFoundError(source)
    if source.suffix.lower() == ".glb":
        return read_glb_json(source), str(source)
    if source.suffix.lower() != ".anims":
        raise ValueError(f"Unsupported input {source}; expected .anims or .glb")
    resolved_game = game_path or discover_game_path()
    if resolved_game is None:
        raise FileNotFoundError(
            "Cyberpunk game directory was not found; pass --game-path or set CYBERPUNK_2077_PATH"
        )
    with tempfile.TemporaryDirectory(prefix="ghostline-lipsync-") as temporary:
        exported = export_anims(source, Path(temporary), wolvenkit, resolved_game)
        return read_glb_json(exported), f"{source} (exported through {wolvenkit})"


class LipsyncExplorer:
    def __init__(self, document: dict[str, Any], source_label: str = "<memory>") -> None:
        self.document = document
        self.source_label = source_label
        skins = document.get("skins", [])
        skin_extras = skins[0].get("extras", {}) if skins else {}
        self.rig_path = str(skin_extras.get("rigPath", ""))
        self.bone_names = [str(value) for value in skin_extras.get("boneNames", [])]
        self.track_names = [str(value) for value in skin_extras.get("trackNames", [])]
        self.animations = document.get("animations", [])

    def track_name(self, index: int) -> str:
        if 0 <= index < len(self.track_names):
            return self.track_names[index]
        return f"track_{index}"

    def locstring_id(self, animation: dict[str, Any]) -> str:
        match = LINE_NAME.fullmatch(str(animation.get("name", "")))
        return str(int(match.group(1), 16)) if match else ""

    @staticmethod
    def _keys(animation: dict[str, Any], field: str) -> list[dict[str, Any]]:
        extras = animation.get("extras", {})
        values = extras.get(field, []) if isinstance(extras, dict) else []
        return values if isinstance(values, list) else []

    def duration(self, animation: dict[str, Any]) -> float:
        times = [
            float(key.get("time", 0.0))
            for field in ("trackKeys", "constTrackKeys")
            for key in self._keys(animation, field)
        ]
        accessors = self.document.get("accessors", [])
        for sampler in animation.get("samplers", []):
            accessor_index = sampler.get("input")
            if not isinstance(accessor_index, int) or not 0 <= accessor_index < len(accessors):
                continue
            maximum = accessors[accessor_index].get("max", [])
            if maximum:
                times.append(float(maximum[0]))
        return max(times, default=0.0)

    def lines(self) -> list[LineInfo]:
        rows: list[LineInfo] = []
        for index, animation in enumerate(self.animations):
            dynamic = self._keys(animation, "trackKeys")
            constant = self._keys(animation, "constTrackKeys")
            rows.append(
                LineInfo(
                    index=index,
                    name=str(animation.get("name", f"animation_{index}")),
                    locstring_id=self.locstring_id(animation),
                    duration=self.duration(animation),
                    dynamic_tracks=len({int(key["trackIndex"]) for key in dynamic}),
                    dynamic_keys=len(dynamic),
                    const_tracks=len({int(key["trackIndex"]) for key in constant}),
                )
            )
        return rows

    def select_line(self, selector: str) -> tuple[LineInfo, dict[str, Any]]:
        lowered = selector.lower()
        for line, animation in zip(self.lines(), self.animations):
            candidates = {str(line.index), line.name.lower(), line.locstring_id}
            if lowered in candidates:
                return line, animation
            if lowered.startswith("0x") and line.locstring_id:
                if int(lowered, 16) == int(line.locstring_id):
                    return line, animation
        raise KeyError(f"No animation matches {selector!r}")

    def tracks(self, selector: str, query: str | None = None) -> list[TrackInfo]:
        _, animation = self.select_line(selector)
        rows: list[TrackInfo] = []
        for field, kind in (("trackKeys", "dynamic"), ("constTrackKeys", "constant")):
            grouped: dict[int, list[float]] = defaultdict(list)
            for key in self._keys(animation, field):
                grouped[int(key["trackIndex"])].append(float(key["value"]))
            for index, values in grouped.items():
                name = self.track_name(index)
                if query and query.lower() not in name.lower():
                    continue
                rows.append(TrackInfo(index, name, kind, len(values), min(values), max(values)))
        return sorted(rows, key=lambda row: (row.index, row.kind))

    def samples(self, line_selector: str, track_selector: str) -> list[TrackSample]:
        line, animation = self.select_line(line_selector)
        indices: set[int] = set()
        if track_selector.isdecimal():
            indices.add(int(track_selector))
        else:
            lowered = track_selector.lower()
            indices.update(index for index, name in enumerate(self.track_names) if lowered in name.lower())
        if not indices:
            raise KeyError(f"No track matches {track_selector!r}")

        rows: list[TrackSample] = []
        for field, kind in (("trackKeys", "dynamic"), ("constTrackKeys", "constant")):
            for key in self._keys(animation, field):
                index = int(key["trackIndex"])
                if index in indices:
                    rows.append(
                        TrackSample(
                            line=line.name,
                            locstring_id=line.locstring_id,
                            track_index=index,
                            track_name=self.track_name(index),
                            kind=kind,
                            time=float(key["time"]),
                            value=float(key["value"]),
                        )
                    )
        return sorted(rows, key=lambda row: (row.track_index, row.time, row.kind))


def write_csv(rows: Iterable[dict[str, Any]], stream: TextIO) -> None:
    materialized = list(rows)
    if not materialized:
        return
    writer = csv.DictWriter(stream, fieldnames=list(materialized[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(materialized)


def command_summary(explorer: LipsyncExplorer, args: argparse.Namespace) -> None:
    lines = explorer.lines()
    payload = {
        "source": explorer.source_label,
        "rig": explorer.rig_path,
        "animations": len(lines),
        "locstring_keyed_animations": sum(bool(line.locstring_id) for line in lines),
        "bones": len(explorer.bone_names),
        "tracks": len(explorer.track_names),
        "lipsync_pose_output_tracks": sum("LipsyncPoseOutput" in name for name in explorer.track_names),
        "animation_override_tracks": sum("AnimOverrideWeight" in name for name in explorer.track_names),
        "total_dynamic_keys": sum(line.dynamic_keys for line in lines),
    }
    if args.json:
        print_json(payload)
        return
    for key, value in payload.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def command_lines(explorer: LipsyncExplorer, args: argparse.Namespace) -> None:
    rows, suffix = bounded(explorer.lines(), args.limit, args.offset)
    payload = [asdict(row) for row in rows]
    if args.json:
        print_json(payload)
        return
    print_table(
        payload,
        [
            ("index", "Index"),
            ("name", "Name"),
            ("locstring_id", "Locstring"),
            ("duration", "Duration"),
            ("dynamic_tracks", "Dynamic Tracks"),
            ("dynamic_keys", "Dynamic Keys"),
            ("const_tracks", "Const Tracks"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_tracks(explorer: LipsyncExplorer, args: argparse.Namespace) -> None:
    rows, suffix = bounded(explorer.tracks(args.line, args.query), args.limit, args.offset)
    payload = [asdict(row) for row in rows]
    if args.json:
        print_json(payload)
        return
    print_table(
        payload,
        [
            ("index", "Index"),
            ("name", "Name"),
            ("kind", "Kind"),
            ("keys", "Keys"),
            ("minimum", "Min"),
            ("maximum", "Max"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_track(explorer: LipsyncExplorer, args: argparse.Namespace) -> None:
    payload = [asdict(row) for row in explorer.samples(args.line, args.track)]
    if args.format == "json":
        print_json(payload)
    elif args.format == "csv":
        write_csv(payload, sys.stdout)
    else:
        print_table(
            payload,
            [
                ("track_index", "Index"),
                ("track_name", "Track"),
                ("kind", "Kind"),
                ("time", "Time"),
                ("value", "Value"),
            ],
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect Cyberpunk lipsync .anims files or WolvenKit-exported animation GLBs."
    )
    parser.add_argument("-f", "--file", required=True, help="Input .anims or exported .glb file.")
    parser.add_argument("--game-path", help="Cyberpunk 2077 directory used when exporting .anims.")
    parser.add_argument("--wolvenkit", default=str(DEFAULT_WOLVENKIT), help="WolvenKit.CLI executable.")
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show rig, animation, and facial-track counts.")
    summary.add_argument("--json", action="store_true")
    summary.set_defaults(func=command_summary)

    lines = subparsers.add_parser("lines", help="List line animations and their locstring IDs.")
    lines.add_argument("--limit", type=int, default=200)
    lines.add_argument("--offset", type=int, default=0)
    lines.add_argument("--json", action="store_true")
    lines.set_defaults(func=command_lines)

    tracks = subparsers.add_parser("tracks", help="List animated tracks for one line.")
    tracks.add_argument("line", help="Animation index, f_<hex> name, decimal locstring ID, or 0x hex ID.")
    tracks.add_argument("--query", help="Filter track names by substring.")
    tracks.add_argument("--limit", type=int, default=200)
    tracks.add_argument("--offset", type=int, default=0)
    tracks.add_argument("--json", action="store_true")
    tracks.set_defaults(func=command_tracks)

    track = subparsers.add_parser("track", help="Print timed samples for a named or numbered track.")
    track.add_argument("line", help="Animation index, f_<hex> name, decimal locstring ID, or 0x hex ID.")
    track.add_argument("track", help="Track index or case-insensitive name substring.")
    track.add_argument("--format", choices=["table", "json", "csv"], default="table")
    track.set_defaults(func=command_track)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary
    try:
        document, source_label = load_source(
            Path(args.file),
            Path(args.wolvenkit),
            Path(args.game_path) if args.game_path else None,
        )
        args.func(LipsyncExplorer(document, source_label), args)
        return 0
    except (FileNotFoundError, KeyError, RuntimeError, ValueError) as error:
        parser.exit(2, f"error: {error}{os.linesep}")


if __name__ == "__main__":
    raise SystemExit(main())
