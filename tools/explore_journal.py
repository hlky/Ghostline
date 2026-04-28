#!/usr/bin/env python3
"""Explore WolvenKit-deserialized .journal JSON files.

The reference cooked journal exports are too large to inspect directly. This
read-only helper prints bounded summaries of the entry tree, entry types, and
resource/path references so custom journal files can be shaped from small
representative examples.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from cr2w_helpers import (
    bounded,
    collect_type_counts,
    depot_path_value,
    int_or_text,
    load_json,
    object_handle,
    path_to_string,
    print_json,
    print_table,
    short_type,
    typed_value,
    walk,
)


DEFAULT_JOURNAL = Path("reference/journal/quests.minor_quest.mq003_orbitals.journal.json")
DEFAULT_REFERENCE_DIR = Path("reference/journal")


@dataclass(frozen=True)
class EntryInfo:
    handle: str
    parent: str
    depth: int
    type: str
    short_type: str
    id: str
    path: str
    title: str
    description: str
    entry_count: int
    file_path: str


@dataclass(frozen=True)
class RefInfo:
    kind: str
    value: str
    owner: str
    path: str


class JournalExplorer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.data = load_json(path)
        self.handle_map: dict[str, dict[str, Any]] = {}
        self.handle_paths: dict[str, tuple[Any, ...]] = {}
        self.parent_by_handle: dict[str, str] = {}
        self.entries_by_handle: dict[str, EntryInfo] = {}
        self._index_handles()
        self._index_entries()

    def _index_handles(self) -> None:
        for path, value in walk(self.data):
            if not isinstance(value, dict) or "HandleId" not in value:
                continue
            handle = str(value["HandleId"])
            self.handle_map[handle] = value
            self.handle_paths[handle] = path

    def _index_entries(self) -> None:
        root_handle = object_handle(self.root_entry)
        if root_handle is None:
            return
        self._visit_entry(self.root_entry, "", 0, [])

    def _visit_entry(self, wrapper: Any, parent: str, depth: int, path_parts: list[str]) -> None:
        handle = object_handle(wrapper)
        data = self.resolve_data(wrapper)
        if handle is None or not isinstance(data, dict):
            return

        entry_id = str(data.get("id", ""))
        current_path_parts = [*path_parts]
        if entry_id:
            current_path_parts.append(entry_id)
        entry_path = "/".join(current_path_parts)
        child_entries = data.get("entries", [])
        entry_count = len(child_entries) if isinstance(child_entries, list) else 0
        title = loc_key(data.get("title"))
        description = loc_key(data.get("description"))
        if not description:
            description = loc_key(data.get("content"))

        self.parent_by_handle[handle] = parent
        self.entries_by_handle[handle] = EntryInfo(
            handle=handle,
            parent=parent,
            depth=depth,
            type=str(data.get("$type", "")),
            short_type=short_type(str(data.get("$type", ""))),
            id=entry_id,
            path=entry_path,
            title=title,
            description=description,
            entry_count=entry_count,
            file_path=path_to_string(self.handle_paths.get(handle, ("$",))),
        )

        if not isinstance(child_entries, list):
            return
        for child in child_entries:
            self._visit_entry(child, handle, depth + 1, current_path_parts)

    @property
    def header(self) -> dict[str, Any]:
        header = self.data.get("Header", {})
        return header if isinstance(header, dict) else {}

    @property
    def root_chunk(self) -> dict[str, Any]:
        root = self.data.get("Data", {}).get("RootChunk", {})
        return root if isinstance(root, dict) else {}

    @property
    def root_entry(self) -> Any:
        return self.root_chunk.get("entry")

    @property
    def archive_file_name(self) -> str:
        return str(self.header.get("ArchiveFileName", ""))

    @property
    def prefix(self) -> str:
        return journal_prefix(self.path)

    def resolve_data(self, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if "HandleRefId" in value:
            value = self.handle_map.get(str(value["HandleRefId"]), value)
        if isinstance(value, dict) and "Data" in value:
            return value["Data"]
        return value

    def owner_for_path(self, path: tuple[Any, ...]) -> str:
        best_handle = ""
        best_length = -1
        for handle, handle_path in self.handle_paths.items():
            if handle not in self.entries_by_handle:
                continue
            if len(handle_path) > best_length and path[: len(handle_path)] == handle_path:
                best_handle = handle
                best_length = len(handle_path)
        if best_handle:
            return entry_display(self.entries_by_handle.get(best_handle))
        return ""

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for path, value in walk(self.data):
            if not isinstance(value, dict):
                continue
            kind = ""
            ref_value: Any = None
            value_type = value.get("$type")
            if value_type == "ResourcePath":
                kind = "resource"
                ref_value = value.get("$value")
            elif value_type == "NodeRef":
                kind = "node_ref"
                ref_value = value.get("$value")
            elif value_type == "TweakDBID":
                kind = "tweakdb"
                ref_value = value.get("$value")
            elif "DepotPath" in value:
                depot = value.get("DepotPath")
                if isinstance(depot, dict):
                    kind = "depot_path"
                    ref_value = depot.get("$value")
            elif "realPath" in value and "className" in value:
                kind = "journal_path"
                ref_value = value.get("realPath")
            elif "value" in value and str(value.get("value", "")).startswith("LocKey#"):
                kind = "loc_key"
                ref_value = value.get("value")

            if kind and ref_value not in (None, "", "0"):
                refs.append(
                    RefInfo(
                        kind=kind,
                        value=str(ref_value),
                        owner=self.owner_for_path(path),
                        path=path_to_string(path),
                    )
                )
        return refs

    def search(self, terms: list[str], limit: int) -> list[tuple[str, str]]:
        normalized_terms = [term.casefold() for term in terms if term]
        matches: list[tuple[str, str]] = []
        for path, value in walk(self.data):
            if isinstance(value, (dict, list)):
                continue
            path_text = path_to_string(path)
            value_text = str(value)
            haystack = f"{path_text} {value_text}".casefold()
            if all(term in haystack for term in normalized_terms):
                matches.append((path_text, value_text))
                if limit > 0 and len(matches) >= limit:
                    break
        return matches

    def summary(self) -> dict[str, Any]:
        entries = list(self.entries_by_handle.values())
        entry_type_counts = Counter(entry.short_type for entry in entries)
        ref_counts = Counter(ref.kind for ref in self.refs())
        top_entries = [entry for entry in entries if entry.depth <= 2]
        return {
            "file": str(self.path),
            "prefix": self.prefix,
            "archive_file": self.archive_file_name,
            "root_type": self.root_chunk.get("$type", ""),
            "entry_count": len(entries),
            "handles": len(self.handle_map),
            "max_depth": max((entry.depth for entry in entries), default=0),
            "entry_types": dict(sorted(entry_type_counts.items())),
            "reference_types": dict(sorted(ref_counts.items())),
            "top_entries": [
                {
                    "depth": entry.depth,
                    "handle": f"h{entry.handle}",
                    "type": entry.short_type,
                    "id": entry.id,
                    "children": entry.entry_count,
                    "path": entry.path,
                }
                for entry in top_entries
            ],
            "all_types": dict(sorted(collect_type_counts(self.data).items())),
        }


def loc_key(value: Any) -> str:
    if isinstance(value, dict):
        if "value" in value:
            return str(value.get("value", ""))
        unwrapped = typed_value(value, "")
        if unwrapped:
            return str(unwrapped)
    return ""


def entry_display(entry: EntryInfo | None) -> str:
    if entry is None:
        return ""
    label = f"h{entry.handle} {entry.short_type}"
    if entry.id:
        label += f" id={entry.id}"
    if entry.path:
        label += f" path={entry.path}"
    return label


def journal_prefix(path: Path) -> str:
    name = path.name
    if "." not in name:
        return ""
    return name.split(".", 1)[0]


def choose_representative(files: list[Path], prefix: str) -> Path:
    if prefix == "quests":
        for path in files:
            if path.name == "quests.minor_quest.mq003_orbitals.journal.json":
                return path
    return sorted(files, key=lambda path: (path.stat().st_size, path.name))[0]


def command_summary(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    summary = explorer.summary()
    if args.json:
        print_json(summary)
        return
    print(f"File: {summary['file']}")
    print(f"Prefix: {summary['prefix']}")
    print(f"ArchiveFileName: {summary['archive_file']}")
    print(f"Root type: {summary['root_type']}")
    print(f"Journal entries: {summary['entry_count']}")
    print(f"CR2W handles: {summary['handles']}")
    print(f"Max depth: {summary['max_depth']}")
    print()
    print("Entry types:")
    for name, count in summary["entry_types"].items():
        print(f"  {name}: {count}")
    print()
    print("References:")
    for name, count in summary["reference_types"].items():
        print(f"  {name}: {count}")
    print()
    print("Top entries:")
    print_table(
        summary["top_entries"],
        [
            ("handle", "Handle"),
            ("depth", "Depth"),
            ("type", "Type"),
            ("id", "ID"),
            ("children", "Children"),
            ("path", "Path"),
        ],
    )


def command_entries(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    entries = list(explorer.entries_by_handle.values())
    if args.type:
        type_filter = args.type.casefold()
        entries = [
            entry
            for entry in entries
            if type_filter in entry.type.casefold() or type_filter in entry.short_type.casefold()
        ]
    if args.id:
        id_filter = args.id.casefold()
        entries = [
            entry
            for entry in entries
            if id_filter in entry.id.casefold() or id_filter in entry.path.casefold()
        ]
    if args.max_depth is not None:
        entries = [entry for entry in entries if entry.depth <= args.max_depth]
    entries, suffix = bounded(entries, args.limit, args.offset)

    if args.json:
        print_json([asdict(entry) for entry in entries])
        return

    print_table(
        [
            {
                "handle": f"h{entry.handle}",
                "depth": entry.depth,
                "type": entry.short_type,
                "id": entry.id,
                "children": entry.entry_count,
                "title": entry.title,
                "description": entry.description,
                "path": entry.path,
            }
            for entry in entries
        ],
        [
            ("handle", "Handle"),
            ("depth", "Depth"),
            ("type", "Type"),
            ("id", "ID"),
            ("children", "Children"),
            ("title", "Title"),
            ("description", "Description"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_entry(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    selector = args.selector
    selected: EntryInfo | None = None
    if selector.lower().startswith(("handle:", "h:")):
        handle = selector.split(":", 1)[1]
        selected = explorer.entries_by_handle.get(handle)
    else:
        matches = [
            entry
            for entry in explorer.entries_by_handle.values()
            if entry.handle == selector or entry.id == selector or entry.path == selector
        ]
        if len(matches) > 1:
            handles = ", ".join(f"h{entry.handle}:{entry.path}" for entry in matches)
            raise SystemExit(f"Selector {selector!r} matched multiple entries. Use handle:<id>. Matches: {handles}")
        if matches:
            selected = matches[0]

    if selected is None:
        raise SystemExit(f"No journal entry matched {selector!r}")
    wrapper = explorer.handle_map.get(selected.handle)
    if args.raw:
        print_json(wrapper)
        return
    print(entry_display(selected))
    print(f"Full type: {selected.type}")
    print(f"Depth: {selected.depth}")
    print(f"Children: {selected.entry_count}")
    if selected.title:
        print(f"Title: {selected.title}")
    if selected.description:
        print(f"Description: {selected.description}")
    print(f"Path: {selected.path}")
    handle_path = explorer.handle_paths.get(selected.handle)
    if handle_path:
        print(f"JSON path: {path_to_string(handle_path)}")
    owner_prefix = f"h{selected.handle} "
    entry_refs = [ref for ref in explorer.refs() if ref.owner.startswith(owner_prefix)]
    if entry_refs:
        print()
        print("References:")
        for ref in entry_refs:
            print(f"  {ref.kind}: {ref.value}")


def command_tree(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    entries = list(explorer.entries_by_handle.values())
    if args.max_depth is not None:
        entries = [entry for entry in entries if entry.depth <= args.max_depth]
    if args.json:
        print_json([asdict(entry) for entry in entries])
        return
    for entry in entries:
        indent = "  " * entry.depth
        pieces = [f"h{entry.handle}", entry.short_type]
        if entry.id:
            pieces.append(f"id={entry.id}")
        if entry.title:
            pieces.append(f"title={entry.title}")
        if entry.description:
            pieces.append(f"description={entry.description}")
        if entry.entry_count:
            pieces.append(f"children={entry.entry_count}")
        print(indent + " ".join(pieces))


def command_refs(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    refs = explorer.refs()
    if args.kind:
        refs = [ref for ref in refs if ref.kind == args.kind]
    refs, suffix = bounded(refs, args.limit, args.offset)
    if args.json:
        print_json([asdict(ref) for ref in refs])
        return
    print_table(
        [
            {
                "kind": ref.kind,
                "value": ref.value,
                "owner": ref.owner,
                "path": ref.path,
            }
            for ref in refs
        ],
        [
            ("kind", "Kind"),
            ("value", "Value"),
            ("owner", "Owner Entry"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_types(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    counts = collect_type_counts(explorer.data)
    rows = [
        {"type": type_name, "short": short_type(type_name), "count": count}
        for type_name, count in sorted(counts.items())
    ]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("count", "Count"), ("short", "Short"), ("type", "Type")])


def command_search(explorer: JournalExplorer, args: argparse.Namespace) -> None:
    matches = explorer.search(args.terms, args.limit)
    if args.json:
        print_json([{"path": path, "value": value} for path, value in matches])
        return
    print_table(
        [{"path": path, "value": value} for path, value in matches],
        [("path", "Path"), ("value", "Value")],
    )
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def command_prefixes(args: argparse.Namespace) -> None:
    files = sorted(args.reference_dir.glob("*.journal.json"))
    groups: dict[str, list[Path]] = defaultdict(list)
    for file_path in files:
        groups[journal_prefix(file_path)].append(file_path)

    rows = []
    for prefix, prefix_files in sorted(groups.items()):
        sizes = [path.stat().st_size for path in prefix_files]
        representative = choose_representative(prefix_files, prefix)
        if args.with_types:
            explorer = JournalExplorer(representative)
            entry_types = ", ".join(
                f"{name}:{count}" for name, count in explorer.summary()["entry_types"].items()
            )
        else:
            entry_types = ""
        rows.append(
            {
                "prefix": prefix,
                "count": len(prefix_files),
                "min": min(sizes),
                "max": max(sizes),
                "representative": str(representative),
                "entry_types": entry_types,
            }
        )

    if args.json:
        print_json(rows)
        return
    print_table(
        rows,
        [
            ("prefix", "Prefix"),
            ("count", "Files"),
            ("min", "MinBytes"),
            ("max", "MaxBytes"),
            ("representative", "Representative"),
            ("entry_types", "Representative Entry Types"),
        ],
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore a WolvenKit-deserialized .journal JSON without dumping the full file."
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        default=None,
        help=f"Deserialized journal JSON. Default: {DEFAULT_JOURNAL}",
    )
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show high-level entry, handle, and reference counts.")
    summary.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    summary.set_defaults(func=command_summary, needs_file=True)

    entries = subparsers.add_parser("entries", help="List journal entries.")
    entries.add_argument("--type", help="Filter by full or short entry type substring.")
    entries.add_argument("--id", help="Filter by entry id or computed id path substring.")
    entries.add_argument("--max-depth", type=int, default=None, help="Only show entries at or above this depth.")
    entries.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    entries.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    entries.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    entries.set_defaults(func=command_entries, needs_file=True)

    entry = subparsers.add_parser("entry", help="Inspect one journal entry by handle, id, or computed id path.")
    entry.add_argument("selector", help="HandleId, handle:<HandleId>, entry id, or computed id path.")
    entry.add_argument("--raw", action="store_true", help="Dump the raw handle JSON for this entry.")
    entry.set_defaults(func=command_entry, needs_file=True)

    tree = subparsers.add_parser("tree", help="Print the journal entry hierarchy.")
    tree.add_argument("--max-depth", type=int, default=6, help="Only show entries at or above this depth.")
    tree.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    tree.set_defaults(func=command_tree, needs_file=True)

    refs = subparsers.add_parser("refs", help="List ResourcePath, NodeRef, TweakDBID, journal path, and LocKey refs.")
    refs.add_argument("--kind", choices=["resource", "node_ref", "tweakdb", "depot_path", "journal_path", "loc_key"])
    refs.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    refs.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    refs.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    refs.set_defaults(func=command_refs, needs_file=True)

    search = subparsers.add_parser("search", help="Search scalar keys and values by substring.")
    search.add_argument("terms", nargs="+", help="Case-insensitive terms. All terms must match.")
    search.add_argument("--limit", type=int, default=50, help="Maximum matches to print. Use 0 for all.")
    search.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    search.set_defaults(func=command_search, needs_file=True)

    types = subparsers.add_parser("types", help="Count every CR2W $type in the file.")
    types.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    types.set_defaults(func=command_types, needs_file=True)

    prefixes = subparsers.add_parser("prefixes", help="Summarize first-dot journal file prefixes in a reference dir.")
    prefixes.add_argument(
        "--reference-dir",
        type=Path,
        default=DEFAULT_REFERENCE_DIR,
        help=f"Directory of *.journal.json files. Default: {DEFAULT_REFERENCE_DIR}",
    )
    prefixes.add_argument("--with-types", action="store_true", help="Also inspect one representative file per prefix.")
    prefixes.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    prefixes.set_defaults(func=command_prefixes, needs_file=False)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary
        args.needs_file = True

    if args.needs_file:
        file_path = Path(args.file) if args.file else DEFAULT_JOURNAL
        explorer = JournalExplorer(file_path)
        args.func(explorer, args)
    else:
        args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
