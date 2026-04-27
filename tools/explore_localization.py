#!/usr/bin/env python3
"""Explore deserialized subtitle and voiceover-map CR2W-JSON files."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from cr2w_helpers import (
    bounded,
    collect_type_counts,
    depot_path_value,
    load_json,
    path_to_string,
    print_json,
    print_table,
    short_type,
)


DEFAULT_SUBTITLES = Path("source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json")
DEFAULT_VO = Path("source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json")


@dataclass(frozen=True)
class SubtitleEntry:
    string_id: str
    female_variant: str
    male_variant: str
    source: str


@dataclass(frozen=True)
class VoiceoverEntry:
    string_id: str
    female_path: str
    male_path: str
    source: str


@dataclass(frozen=True)
class CombinedEntry:
    string_id: str
    subtitle: str
    male_subtitle: str
    female_vo: str
    male_vo: str
    status: str


@dataclass(frozen=True)
class RefInfo:
    kind: str
    string_id: str
    value: str
    source: str
    path: str


class LocalizationExplorer:
    def __init__(self, paths: list[Path]) -> None:
        self.paths = paths
        self.files: list[tuple[Path, dict[str, Any]]] = [(path, load_json(path)) for path in paths]
        self.subtitles: list[SubtitleEntry] = []
        self.voiceovers: list[VoiceoverEntry] = []
        self._index_entries()

    def _index_entries(self) -> None:
        for path, data in self.files:
            root_data = root_payload(data)
            root_type = root_data.get("$type", "") if isinstance(root_data, dict) else ""
            entries = root_data.get("entries", []) if isinstance(root_data, dict) else []
            if not isinstance(entries, list):
                continue
            if root_type == "localizationPersistenceSubtitleEntries":
                for entry in entries:
                    if isinstance(entry, dict):
                        self.subtitles.append(
                            SubtitleEntry(
                                string_id=str(entry.get("stringId", "")),
                                female_variant=str(entry.get("femaleVariant", "")),
                                male_variant=str(entry.get("maleVariant", "")),
                                source=str(path),
                            )
                        )
            elif root_type == "locVoiceoverMap":
                for entry in entries:
                    if isinstance(entry, dict):
                        self.voiceovers.append(
                            VoiceoverEntry(
                                string_id=str(entry.get("stringId", "")),
                                female_path=depot_path_value(entry.get("femaleResPath")),
                                male_path=depot_path_value(entry.get("maleResPath")),
                                source=str(path),
                            )
                        )

    def summary(self) -> dict[str, Any]:
        files = []
        for path, data in self.files:
            payload = root_payload(data)
            entries = payload.get("entries", []) if isinstance(payload, dict) else []
            header = data.get("Header", {})
            files.append(
                {
                    "file": str(path),
                    "archive_file": header.get("ArchiveFileName", "") if isinstance(header, dict) else "",
                    "root_type": payload.get("$type", "") if isinstance(payload, dict) else "",
                    "entries": len(entries) if isinstance(entries, list) else 0,
                    "duplicate_string_ids": duplicate_ids([str(entry.get("stringId", "")) for entry in entries if isinstance(entry, dict)]),
                }
            )
        combined = self.combined_entries()
        status_counts = Counter(entry.status for entry in combined)
        return {
            "files": files,
            "subtitle_entries": len(self.subtitles),
            "voiceover_entries": len(self.voiceovers),
            "combined_string_ids": len(combined),
            "status_counts": dict(sorted(status_counts.items())),
            "all_types": dict(sorted(sum_type_counts(data for _, data in self.files).items())),
        }

    def combined_entries(self) -> list[CombinedEntry]:
        subtitles_by_id = group_first(self.subtitles, "string_id")
        voiceovers_by_id = group_first(self.voiceovers, "string_id")
        ids = sorted(set(subtitles_by_id) | set(voiceovers_by_id), key=int_or_text)
        entries = []
        for string_id in ids:
            subtitle = subtitles_by_id.get(string_id)
            voiceover = voiceovers_by_id.get(string_id)
            statuses = []
            if subtitle is None:
                statuses.append("missing_subtitle")
            if voiceover is None:
                statuses.append("missing_vo")
            if subtitle and subtitle.female_variant != subtitle.male_variant:
                statuses.append("subtitle_gender_diff")
            if voiceover and voiceover.female_path != voiceover.male_path:
                statuses.append("vo_gender_diff")
            if not statuses:
                statuses.append("ok")
            entries.append(
                CombinedEntry(
                    string_id=string_id,
                    subtitle=subtitle.female_variant if subtitle else "",
                    male_subtitle=subtitle.male_variant if subtitle else "",
                    female_vo=voiceover.female_path if voiceover else "",
                    male_vo=voiceover.male_path if voiceover else "",
                    status=",".join(statuses),
                )
            )
        return entries

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for path, data in self.files:
            payload = root_payload(data)
            entries = payload.get("entries", []) if isinstance(payload, dict) else []
            for index, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    continue
                string_id = str(entry.get("stringId", ""))
                for field in ("femaleResPath", "maleResPath"):
                    path_value = entry.get(field)
                    ref_value = depot_path_value(path_value)
                    if ref_value not in ("", "0"):
                        base_path = ("$", "Data", "RootChunk", "root", "Data", "entries", index, field)
                        refs.append(
                            RefInfo(
                                kind="DepotPath",
                                string_id=string_id,
                                value=ref_value,
                                source=str(path),
                                path=path_to_string(base_path),
                            )
                        )
                        refs.append(
                            RefInfo(
                                kind="ResourcePath",
                                string_id=string_id,
                                value=ref_value,
                                source=str(path),
                                path=path_to_string(base_path + ("DepotPath",)),
                            )
                        )
        return refs

    def search(self, terms: list[str], limit: int) -> list[CombinedEntry]:
        normalized_terms = [term.casefold() for term in terms if term]
        matches = []
        for entry in self.combined_entries():
            haystack = " ".join(
                [
                    entry.string_id,
                    entry.subtitle,
                    entry.male_subtitle,
                    entry.female_vo,
                    entry.male_vo,
                    entry.status,
                ]
            ).casefold()
            if all(term in haystack for term in normalized_terms):
                matches.append(entry)
                if limit > 0 and len(matches) >= limit:
                    break
        return matches

    def entry(self, string_id: str) -> CombinedEntry:
        for entry in self.combined_entries():
            if entry.string_id == string_id:
                return entry
        raise SystemExit(f"No subtitle or VO entry for stringId {string_id}")

    def raw_entry(self, string_id: str) -> dict[str, Any]:
        matches = []
        for path, data in self.files:
            payload = root_payload(data)
            entries = payload.get("entries", []) if isinstance(payload, dict) else []
            for entry in entries:
                if isinstance(entry, dict) and str(entry.get("stringId", "")) == string_id:
                    matches.append({"source": str(path), "entry": entry})
        if not matches:
            raise SystemExit(f"No raw entry for stringId {string_id}")
        return {"stringId": string_id, "matches": matches}


def root_payload(data: dict[str, Any]) -> dict[str, Any]:
    payload = data.get("Data", {}).get("RootChunk", {}).get("root", {}).get("Data", {})
    return payload if isinstance(payload, dict) else {}


def duplicate_ids(ids: list[str]) -> list[str]:
    counts = Counter(item for item in ids if item)
    return sorted([item for item, count in counts.items() if count > 1], key=int_or_text)


def group_first(entries: list[Any], attr: str) -> dict[str, Any]:
    grouped: dict[str, Any] = {}
    for entry in entries:
        key = getattr(entry, attr)
        grouped.setdefault(key, entry)
    return grouped


def sum_type_counts(values: Any) -> Counter[str]:
    counts: Counter[str] = Counter()
    for value in values:
        counts.update(collect_type_counts(value))
    return counts


def int_or_text(value: str) -> tuple[int, int | str]:
    try:
        return (0, int(value))
    except ValueError:
        return (1, value)


def default_paths() -> list[Path]:
    paths = []
    for path in (DEFAULT_SUBTITLES, DEFAULT_VO):
        if path.exists():
            paths.append(path)
    return paths


def entry_rows(entries: list[CombinedEntry]) -> list[dict[str, Any]]:
    return [
        {
            "string_id": entry.string_id,
            "status": entry.status,
            "subtitle": entry.subtitle,
            "female_vo": entry.female_vo,
            "male_vo": entry.male_vo,
        }
        for entry in entries
    ]


def command_summary(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    summary = explorer.summary()
    if args.json:
        print_json(summary)
        return
    print("Files:")
    print_table(
        [
            {
                "file": item["file"],
                "type": short_type(item["root_type"]),
                "entries": item["entries"],
                "duplicates": ", ".join(item["duplicate_string_ids"]),
                "archive": item["archive_file"],
            }
            for item in summary["files"]
        ],
        [
            ("type", "Type"),
            ("entries", "Entries"),
            ("duplicates", "Duplicate IDs"),
            ("file", "File"),
            ("archive", "ArchiveFileName"),
        ],
    )
    print()
    print(f"Subtitle entries: {summary['subtitle_entries']}")
    print(f"Voiceover entries: {summary['voiceover_entries']}")
    print(f"Combined stringIds: {summary['combined_string_ids']}")
    print()
    print("Status:")
    for status, count in summary["status_counts"].items():
        print(f"  {status}: {count}")


def command_entries(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    entries = explorer.combined_entries()
    if args.status:
        entries = [entry for entry in entries if args.status in entry.status.split(",")]
    selected, suffix = bounded(entries, args.limit, args.offset)
    if args.json:
        print_json([asdict(entry) for entry in selected])
        return
    print_table(
        entry_rows(selected),
        [
            ("string_id", "String ID"),
            ("status", "Status"),
            ("subtitle", "Subtitle"),
            ("female_vo", "Female VO"),
            ("male_vo", "Male VO"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_entry(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    if args.raw:
        print_json(explorer.raw_entry(args.string_id))
        return
    entry = explorer.entry(args.string_id)
    if args.json:
        print_json(asdict(entry))
        return
    print(f"String ID: {entry.string_id}")
    print(f"Status: {entry.status}")
    print(f"Female subtitle: {entry.subtitle}")
    print(f"Male subtitle: {entry.male_subtitle}")
    print(f"Female VO: {entry.female_vo}")
    print(f"Male VO: {entry.male_vo}")


def command_search(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    matches = explorer.search(args.terms, args.limit)
    if args.json:
        print_json([asdict(entry) for entry in matches])
        return
    print_table(
        entry_rows(matches),
        [
            ("string_id", "String ID"),
            ("status", "Status"),
            ("subtitle", "Subtitle"),
            ("female_vo", "Female VO"),
            ("male_vo", "Male VO"),
        ],
    )
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def command_refs(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    refs = explorer.refs()
    selected, suffix = bounded(refs, args.limit, args.offset)
    if args.json:
        print_json([asdict(ref) for ref in selected])
        return
    print_table(
        [
            {
                "kind": ref.kind,
                "string_id": ref.string_id,
                "value": ref.value,
                "source": ref.source,
                "path": ref.path,
            }
            for ref in selected
        ],
        [
            ("kind", "Kind"),
            ("string_id", "String ID"),
            ("value", "Value"),
            ("source", "Source"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_check(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    problem_entries = [entry for entry in explorer.combined_entries() if entry.status != "ok"]
    duplicate_rows = []
    for item in explorer.summary()["files"]:
        for string_id in item["duplicate_string_ids"]:
            duplicate_rows.append({"source": item["file"], "string_id": string_id})
    if args.json:
        print_json(
            {
                "problems": [asdict(entry) for entry in problem_entries],
                "duplicates": duplicate_rows,
            }
        )
        return
    if not problem_entries and not duplicate_rows:
        print("No subtitle/VO coverage problems found.")
        return
    if problem_entries:
        print("Coverage/status problems:")
        print_table(
            entry_rows(problem_entries),
            [
                ("string_id", "String ID"),
                ("status", "Status"),
                ("subtitle", "Subtitle"),
                ("female_vo", "Female VO"),
                ("male_vo", "Male VO"),
            ],
        )
    if duplicate_rows:
        if problem_entries:
            print()
        print("Duplicate stringIds:")
        print_table(duplicate_rows, [("string_id", "String ID"), ("source", "Source")])


def command_types(explorer: LocalizationExplorer, args: argparse.Namespace) -> None:
    rows = [
        {"count": count, "short": short_type(type_name), "type": type_name}
        for type_name, count in sorted(explorer.summary()["all_types"].items())
    ]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("count", "Count"), ("short", "Short"), ("type", "Type")])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Explore deserialized subtitle and VO-map CR2W-JSON files.")
    parser.add_argument(
        "-f",
        "--file",
        action="append",
        default=[],
        help="Localization CR2W-JSON file. Can be passed more than once. Defaults to current gq000 subtitles and VO.",
    )
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show file, entry, and coverage counts.")
    summary.add_argument("--json", action="store_true")
    summary.set_defaults(func=command_summary)

    entries = subparsers.add_parser("entries", help="List combined subtitle/VO entries by stringId.")
    entries.add_argument("--status", choices=["ok", "missing_subtitle", "missing_vo", "subtitle_gender_diff", "vo_gender_diff"])
    entries.add_argument("--limit", type=int, default=200)
    entries.add_argument("--offset", type=int, default=0)
    entries.add_argument("--json", action="store_true")
    entries.set_defaults(func=command_entries)

    entry = subparsers.add_parser("entry", help="Inspect one stringId.")
    entry.add_argument("string_id")
    entry.add_argument("--raw", action="store_true")
    entry.add_argument("--json", action="store_true")
    entry.set_defaults(func=command_entry)

    search = subparsers.add_parser("search", help="Search stringIds, subtitles, VO paths, and statuses.")
    search.add_argument("terms", nargs="+")
    search.add_argument("--limit", type=int, default=50)
    search.add_argument("--json", action="store_true")
    search.set_defaults(func=command_search)

    refs = subparsers.add_parser("refs", help="List VO resource/depot path references.")
    refs.add_argument("--limit", type=int, default=200)
    refs.add_argument("--offset", type=int, default=0)
    refs.add_argument("--json", action="store_true")
    refs.set_defaults(func=command_refs)

    check = subparsers.add_parser("check", help="Report missing subtitle/VO pairs and duplicate stringIds.")
    check.add_argument("--json", action="store_true")
    check.set_defaults(func=command_check)

    types = subparsers.add_parser("types", help="Count every CR2W $type across loaded files.")
    types.add_argument("--json", action="store_true")
    types.set_defaults(func=command_types)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary
    paths = [Path(path) for path in args.file] if args.file else default_paths()
    if not paths:
        raise SystemExit("No localization files were provided and no defaults exist.")
    explorer = LocalizationExplorer(paths)
    args.func(explorer, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
