#!/usr/bin/env python3
"""Explore WolvenKit-deserialized .ent and .app CR2W-JSON files."""

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
    first_scalar_label,
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


DEFAULT_FILES = [
    Path("source/raw/mod/ghostline/characters/patch/patch.ent.json"),
    Path("source/raw/mod/ghostline/characters/patch/patch.app.json"),
]


@dataclass(frozen=True)
class FileInfo:
    file_id: str
    file: str
    archive_file: str
    root_type: str
    appearances: int
    root_components: int
    appearance_components: int
    handles: int
    resolved_dependencies: int
    loose_dependencies: int
    includes: int
    inplace_resources: int


@dataclass(frozen=True)
class AppearanceInfo:
    appearance_id: str
    file_id: str
    file: str
    index: int
    handle: str
    type: str
    name: str
    appearance_name: str
    parent: str
    resource: str
    components: int
    parts_values: int
    parts_overrides: int
    resolved_dependencies: int
    loose_dependencies: int
    path: str


@dataclass(frozen=True)
class ComponentInfo:
    component_id: str
    file_id: str
    file: str
    owner: str
    index: int
    handle: str
    type: str
    short_type: str
    name: str
    resources: str
    mesh_appearance: str
    path: str


@dataclass(frozen=True)
class RefInfo:
    kind: str
    value: str
    file_id: str
    file: str
    owner: str
    path: str


class EntAppFile:
    def __init__(self, file_id: str, path: Path) -> None:
        self.file_id = file_id
        self.path = path
        self.data = load_json(path)
        self.handle_map: dict[str, dict[str, Any]] = {}
        self.handle_paths: dict[str, tuple[Any, ...]] = {}
        self.owner_by_path: dict[tuple[Any, ...], str] = {}
        self.appearance_raw_by_id: dict[str, Any] = {}
        self.component_raw_by_id: dict[str, Any] = {}
        self._index_handles()

    def _index_handles(self) -> None:
        for path, value in walk(self.data):
            if isinstance(value, dict) and "HandleId" in value:
                handle = str(value["HandleId"])
                self.handle_map[handle] = value
                self.handle_paths[handle] = path

    @property
    def root_chunk(self) -> dict[str, Any]:
        root = self.data.get("Data", {}).get("RootChunk", {})
        return root if isinstance(root, dict) else {}

    @property
    def archive_file_name(self) -> str:
        header = self.data.get("Header", {})
        return str(header.get("ArchiveFileName", "")) if isinstance(header, dict) else ""

    def resolve_data(self, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if "HandleRefId" in value:
            value = self.handle_map.get(str(value["HandleRefId"]), value)
        if isinstance(value, dict) and "Data" in value:
            return value["Data"]
        return value

    def wrapper_data_path(self, wrapper: Any, wrapper_path: tuple[Any, ...]) -> tuple[Any, ...]:
        if isinstance(wrapper, dict) and "Data" in wrapper:
            return wrapper_path + ("Data",)
        return wrapper_path

    def appearances(self, start_index: int = 0) -> list[AppearanceInfo]:
        rows: list[AppearanceInfo] = []
        appearances = self.root_chunk.get("appearances", [])
        if not isinstance(appearances, list):
            return rows

        for index, appearance in enumerate(appearances):
            appearance_id = f"a{start_index + len(rows)}"
            data = self.resolve_data(appearance)
            if not isinstance(data, dict):
                continue
            base_path = ("$", "Data", "RootChunk", "appearances", index)
            data_path = self.wrapper_data_path(appearance, base_path)
            name = scalar_name(data.get("name"))
            appearance_name = scalar_name(data.get("appearanceName"))
            parent = scalar_name(data.get("parentAppearance"))
            resource = first_resource_value(data.get("appearanceResource"))
            components = len(data.get("components", [])) if isinstance(data.get("components"), list) else 0
            parts_values = len(data.get("partsValues", [])) if isinstance(data.get("partsValues"), list) else 0
            parts_overrides = len(data.get("partsOverrides", [])) if isinstance(data.get("partsOverrides"), list) else 0
            resolved_dependencies = (
                len(data.get("resolvedDependencies", []))
                if isinstance(data.get("resolvedDependencies"), list)
                else 0
            )
            loose_dependencies = (
                len(data.get("looseDependencies", []))
                if isinstance(data.get("looseDependencies"), list)
                else 0
            )
            handle = object_handle(appearance) or ""
            info = AppearanceInfo(
                appearance_id=appearance_id,
                file_id=self.file_id,
                file=str(self.path),
                index=index,
                handle=handle,
                type=str(data.get("$type", "")),
                name=name,
                appearance_name=appearance_name,
                parent=parent,
                resource=resource,
                components=components,
                parts_values=parts_values,
                parts_overrides=parts_overrides,
                resolved_dependencies=resolved_dependencies,
                loose_dependencies=loose_dependencies,
                path=path_to_string(base_path),
            )
            rows.append(info)
            self.appearance_raw_by_id[appearance_id] = appearance
            owner = appearance_display(info)
            for child_path, _ in walk(data, data_path):
                self.owner_by_path.setdefault(child_path, owner)

        return rows

    def components(
        self,
        appearances: list[AppearanceInfo],
        start_index: int = 0,
    ) -> list[ComponentInfo]:
        rows: list[ComponentInfo] = []

        root_components = self.root_chunk.get("components", [])
        if isinstance(root_components, list):
            rows.extend(
                self._component_rows(
                    root_components,
                    ("$", "Data", "RootChunk", "components"),
                    "root",
                    start_index,
                )
            )

        appearance_by_index = {appearance.index: appearance for appearance in appearances}
        raw_appearances = self.root_chunk.get("appearances", [])
        if isinstance(raw_appearances, list):
            for appearance_index, appearance in enumerate(raw_appearances):
                data = self.resolve_data(appearance)
                if not isinstance(data, dict):
                    continue
                components = data.get("components", [])
                if not isinstance(components, list):
                    continue
                base_path = ("$", "Data", "RootChunk", "appearances", appearance_index)
                data_path = self.wrapper_data_path(appearance, base_path)
                owner_info = appearance_by_index.get(appearance_index)
                owner = appearance_display(owner_info) if owner_info else f"appearance[{appearance_index}]"
                rows.extend(
                    self._component_rows(
                        components,
                        data_path + ("components",),
                        owner,
                        start_index + len(rows),
                    )
                )

        return rows

    def _component_rows(
        self,
        components: list[Any],
        components_path: tuple[Any, ...],
        owner: str,
        start_index: int,
    ) -> list[ComponentInfo]:
        rows: list[ComponentInfo] = []
        for index, component in enumerate(components):
            component_id = f"c{start_index + len(rows)}"
            data = self.resolve_data(component)
            if not isinstance(data, dict):
                continue
            base_path = components_path + (index,)
            data_path = self.wrapper_data_path(component, base_path)
            resources = unique_resource_values(data)
            name = scalar_name(data.get("name")) or first_scalar_label(data)
            mesh_appearance = scalar_name(data.get("meshAppearance"))
            handle = object_handle(component) or ""
            info = ComponentInfo(
                component_id=component_id,
                file_id=self.file_id,
                file=str(self.path),
                owner=owner,
                index=index,
                handle=handle,
                type=str(data.get("$type", "")),
                short_type=short_type(str(data.get("$type", ""))),
                name=name,
                resources=", ".join(resources[:3]) + (" ..." if len(resources) > 3 else ""),
                mesh_appearance=mesh_appearance,
                path=path_to_string(base_path),
            )
            rows.append(info)
            self.component_raw_by_id[component_id] = component
            component_owner = component_display(info)
            for child_path, _ in walk(data, data_path):
                self.owner_by_path[child_path] = component_owner
        return rows

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for path, value in walk(self.data):
            if not isinstance(value, dict):
                continue
            kind = ""
            ref_value: Any = None
            value_type = value.get("$type")
            if value_type in ("ResourcePath", "TweakDBID", "NodeRef"):
                kind = str(value_type)
                ref_value = value.get("$value")
            elif "DepotPath" in value and isinstance(value.get("DepotPath"), dict):
                kind = "DepotPath"
                ref_value = value["DepotPath"].get("$value")

            if kind and ref_value not in (None, "", "0", "None"):
                refs.append(
                    RefInfo(
                        kind=kind,
                        value=str(ref_value),
                        file_id=self.file_id,
                        file=str(self.path),
                        owner=self.owner_for_path(path),
                        path=path_to_string(path),
                    )
                )
        return refs

    def owner_for_path(self, path: tuple[Any, ...]) -> str:
        for length in range(len(path), 0, -1):
            owner = self.owner_by_path.get(path[:length])
            if owner:
                return owner
        return ""

    def summary(self, appearances: list[AppearanceInfo], components: list[ComponentInfo]) -> FileInfo:
        root = self.root_chunk
        resolved = len(root.get("resolvedDependencies", [])) if isinstance(root.get("resolvedDependencies"), list) else 0
        loose = len(root.get("looseDependencies", [])) if isinstance(root.get("looseDependencies"), list) else 0
        includes = len(root.get("includes", [])) if isinstance(root.get("includes"), list) else 0
        inplace = len(root.get("inplaceResources", [])) if isinstance(root.get("inplaceResources"), list) else 0
        root_components = len(root.get("components", [])) if isinstance(root.get("components"), list) else 0
        appearance_components = sum(
            component.owner.startswith("a") or component.owner.startswith("appearance[")
            for component in components
        )
        return FileInfo(
            file_id=self.file_id,
            file=str(self.path),
            archive_file=self.archive_file_name,
            root_type=str(root.get("$type", "")),
            appearances=len(appearances),
            root_components=root_components,
            appearance_components=appearance_components,
            handles=len(self.handle_map),
            resolved_dependencies=resolved,
            loose_dependencies=loose,
            includes=includes,
            inplace_resources=inplace,
        )

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


class EntAppExplorer:
    def __init__(self, paths: list[Path]) -> None:
        self.files = [EntAppFile(f"f{index}", path) for index, path in enumerate(paths)]
        self.appearances: list[AppearanceInfo] = []
        self.components: list[ComponentInfo] = []
        self.appearance_raw_by_id: dict[str, Any] = {}
        self.component_raw_by_id: dict[str, Any] = {}
        self._index()

    def _index(self) -> None:
        appearance_index = 0
        component_index = 0
        for file in self.files:
            file_appearances = file.appearances(appearance_index)
            appearance_index += len(file_appearances)
            file_components = file.components(file_appearances, component_index)
            component_index += len(file_components)
            self.appearances.extend(file_appearances)
            self.components.extend(file_components)
            self.appearance_raw_by_id.update(file.appearance_raw_by_id)
            self.component_raw_by_id.update(file.component_raw_by_id)

    def summaries(self) -> list[FileInfo]:
        return [
            file.summary(
                [appearance for appearance in self.appearances if appearance.file_id == file.file_id],
                [component for component in self.components if component.file_id == file.file_id],
            )
            for file in self.files
        ]

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for file in self.files:
            refs.extend(file.refs())
        return refs

    def search(self, terms: list[str], limit: int) -> list[dict[str, str]]:
        matches: list[dict[str, str]] = []
        remaining = limit
        for file in self.files:
            file_limit = remaining if limit > 0 else 0
            for path, value in file.search(terms, file_limit):
                matches.append({"file_id": file.file_id, "file": str(file.path), "path": path, "value": value})
                if limit > 0:
                    remaining -= 1
                    if remaining <= 0:
                        return matches
        return matches

    def appearance_by_selector(self, selector: str) -> AppearanceInfo:
        appearance_id = normalize_prefixed_selector(selector, "a")
        for appearance in self.appearances:
            if appearance.appearance_id == appearance_id:
                return appearance
        raise SystemExit(f"No appearance with id {selector}")

    def component_by_selector(self, selector: str) -> ComponentInfo:
        component_id = normalize_prefixed_selector(selector, "c")
        for component in self.components:
            if component.component_id == component_id:
                return component
        raise SystemExit(f"No component with id {selector}")

    def handle_json(self, file_id: str, handle: str) -> Any:
        file = self.file_by_id(file_id)
        wrapper = file.handle_map.get(str(handle))
        if wrapper is None:
            raise SystemExit(f"No HandleId {handle} in {file_id}")
        return wrapper

    def file_by_id(self, file_id: str) -> EntAppFile:
        for file in self.files:
            if file.file_id == file_id:
                return file
        raise SystemExit(f"No file id {file_id}")


def scalar_name(value: Any) -> str:
    if isinstance(value, dict):
        unwrapped = typed_value(value, None)
        if unwrapped is not None:
            return str(unwrapped)
        if "id" in value:
            return str(value["id"])
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return ""


def first_resource_value(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    values = unique_resource_values(value)
    return values[0] if values else ""


def unique_resource_values(value: Any) -> list[str]:
    values: list[str] = []
    for _, child in walk(value):
        if not isinstance(child, dict):
            continue
        if child.get("$type") == "ResourcePath":
            resource = child.get("$value")
            if resource not in (None, "", "0", "None"):
                text = str(resource)
                if text not in values:
                    values.append(text)
    return values


def appearance_display(info: AppearanceInfo | None) -> str:
    if info is None:
        return ""
    label = info.name or info.appearance_name or info.type
    return f"{info.appearance_id} {label}".strip()


def component_display(info: ComponentInfo) -> str:
    pieces = [info.component_id, info.short_type]
    if info.name:
        pieces.append(info.name)
    return " ".join(pieces)


def normalize_prefixed_selector(selector: str, prefix: str) -> str:
    text = selector.strip()
    if text.startswith(prefix):
        return text
    return f"{prefix}{text}"


def default_paths() -> list[Path]:
    return [path for path in DEFAULT_FILES if path.exists()]


def command_summary(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    summaries = explorer.summaries()
    if args.json:
        print_json([asdict(summary) for summary in summaries])
        return
    print_table(
        [
            {
                "id": summary.file_id,
                "root": short_type(summary.root_type),
                "appearances": summary.appearances,
                "root_components": summary.root_components,
                "appearance_components": summary.appearance_components,
                "handles": summary.handles,
                "resolved": summary.resolved_dependencies,
                "loose": summary.loose_dependencies,
                "file": summary.file,
            }
            for summary in summaries
        ],
        [
            ("id", "ID"),
            ("root", "Root"),
            ("appearances", "Apps"),
            ("root_components", "Root Cmp"),
            ("appearance_components", "App Cmp"),
            ("handles", "Handles"),
            ("resolved", "Resolved"),
            ("loose", "Loose"),
            ("file", "File"),
        ],
    )

    component_counts = Counter(component.short_type for component in explorer.components)
    ref_counts = Counter(ref.kind for ref in explorer.refs())
    if component_counts:
        print()
        print("Component types:")
        for name, count in sorted(component_counts.items()):
            print(f"  {name}: {count}")
    if ref_counts:
        print()
        print("References:")
        for name, count in sorted(ref_counts.items()):
            print(f"  {name}: {count}")


def command_appearances(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    rows = explorer.appearances
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json([asdict(row) for row in selected])
        return
    print_table(
        [
            {
                "id": row.appearance_id,
                "file": row.file_id,
                "handle": f"h{row.handle}" if row.handle else "",
                "type": short_type(row.type),
                "name": row.name,
                "appearance_name": row.appearance_name,
                "parent": row.parent,
                "resource": row.resource,
                "components": row.components,
            }
            for row in selected
        ],
        [
            ("id", "ID"),
            ("file", "File"),
            ("handle", "Handle"),
            ("type", "Type"),
            ("name", "Name"),
            ("appearance_name", "Appearance"),
            ("parent", "Parent"),
            ("components", "Cmp"),
            ("resource", "Resource"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_appearance(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    appearance = explorer.appearance_by_selector(args.selector)
    if args.raw:
        print_json(explorer.appearance_raw_by_id[appearance.appearance_id])
        return
    print(f"{appearance.appearance_id} {short_type(appearance.type)}")
    print(f"File: {appearance.file}")
    print(f"Path: {appearance.path}")
    if appearance.handle:
        print(f"Handle: h{appearance.handle}")
    print(f"Name: {appearance.name}")
    print(f"Appearance name: {appearance.appearance_name}")
    print(f"Parent: {appearance.parent}")
    print(f"Resource: {appearance.resource}")
    print(f"Components: {appearance.components}")
    print(f"partsValues: {appearance.parts_values}")
    print(f"partsOverrides: {appearance.parts_overrides}")
    print(f"resolvedDependencies: {appearance.resolved_dependencies}")
    print(f"looseDependencies: {appearance.loose_dependencies}")


def command_components(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    rows = explorer.components
    if args.file:
        rows = [row for row in rows if row.file_id == args.file]
    if args.owner:
        owner = args.owner.casefold()
        rows = [row for row in rows if owner in row.owner.casefold()]
    if args.type:
        type_filter = args.type.casefold()
        rows = [
            row
            for row in rows
            if type_filter in row.type.casefold() or type_filter in row.short_type.casefold()
        ]
    if args.resources_only:
        rows = [row for row in rows if row.resources]
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json([asdict(row) for row in selected])
        return
    print_table(
        [
            {
                "id": row.component_id,
                "file": row.file_id,
                "owner": row.owner,
                "type": row.short_type,
                "name": row.name,
                "mesh_app": row.mesh_appearance,
                "resources": row.resources,
            }
            for row in selected
        ],
        [
            ("id", "ID"),
            ("file", "File"),
            ("owner", "Owner"),
            ("type", "Type"),
            ("name", "Name"),
            ("mesh_app", "Mesh App"),
            ("resources", "Resources"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_component(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    component = explorer.component_by_selector(args.selector)
    if args.raw:
        print_json(explorer.component_raw_by_id[component.component_id])
        return
    print(component_display(component))
    print(f"File: {component.file}")
    print(f"Path: {component.path}")
    print(f"Owner: {component.owner}")
    if component.handle:
        print(f"Handle: h{component.handle}")
    print(f"Full type: {component.type}")
    if component.mesh_appearance:
        print(f"Mesh appearance: {component.mesh_appearance}")
    resources = [ref for ref in explorer.refs() if ref.owner == component_display(component) and ref.kind == "ResourcePath"]
    if resources:
        print()
        print("Resource paths:")
        for ref in resources:
            print(f"  {ref.value}")


def command_refs(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    refs = explorer.refs()
    if args.kind:
        refs = [ref for ref in refs if ref.kind == args.kind]
    if args.file:
        refs = [ref for ref in refs if ref.file_id == args.file]
    selected, suffix = bounded(refs, args.limit, args.offset)
    if args.json:
        print_json([asdict(ref) for ref in selected])
        return
    print_table(
        [
            {
                "kind": ref.kind,
                "value": ref.value,
                "file": ref.file_id,
                "owner": ref.owner,
                "path": ref.path,
            }
            for ref in selected
        ],
        [
            ("kind", "Kind"),
            ("value", "Value"),
            ("file", "File"),
            ("owner", "Owner"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_handles(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    rows = []
    for file in explorer.files:
        if args.file and file.file_id != args.file:
            continue
        for handle, wrapper in sorted(file.handle_map.items(), key=lambda item: int_or_text(item[0])):
            data = file.resolve_data(wrapper)
            type_name = str(data.get("$type", "")) if isinstance(data, dict) else ""
            if args.type:
                type_filter = args.type.casefold()
                if type_filter not in type_name.casefold() and type_filter not in short_type(type_name).casefold():
                    continue
            path = file.handle_paths.get(handle, ("$",))
            label = first_scalar_label(data) if isinstance(data, dict) else ""
            rows.append(
                {
                    "file": file.file_id,
                    "handle": f"h{handle}",
                    "type": short_type(type_name),
                    "label": label,
                    "path": path_to_string(path),
                }
            )
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json(selected)
        return
    print_table(
        selected,
        [("file", "File"), ("handle", "Handle"), ("type", "Type"), ("label", "Label"), ("path", "Path")],
    )
    if suffix:
        print()
        print(suffix)


def command_handle(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    wrapper = explorer.handle_json(args.file, args.handle)
    if args.raw:
        print_json(wrapper)
        return
    file = explorer.file_by_id(args.file)
    data = file.resolve_data(wrapper)
    kind = str(data.get("$type", "")) if isinstance(data, dict) else ""
    path = file.handle_paths.get(args.handle)
    print(f"{args.file}:h{args.handle} {kind or '(untyped handle)'}")
    if path:
        print(f"Path: {path_to_string(path)}")
    if isinstance(data, dict):
        label = first_scalar_label(data)
        if label:
            print(f"Label: {label}")


def command_search(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    matches = explorer.search(args.terms, args.limit)
    if args.json:
        print_json(matches)
        return
    print_table(
        matches,
        [("file_id", "File"), ("path", "Path"), ("value", "Value")],
    )
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def command_types(explorer: EntAppExplorer, args: argparse.Namespace) -> None:
    rows = []
    for file in explorer.files:
        for type_name, count in sorted(collect_type_counts(file.data).items()):
            rows.append(
                {
                    "file": file.file_id,
                    "count": count,
                    "short": short_type(type_name),
                    "type": type_name,
                }
            )
    if args.file:
        rows = [row for row in rows if row["file"] == args.file]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("file", "File"), ("count", "Count"), ("short", "Short"), ("type", "Type")])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore WolvenKit-deserialized .ent and .app CR2W-JSON files without dumping the whole file."
    )
    parser.add_argument(
        "-f",
        "--file",
        action="append",
        default=[],
        help="Raw .ent.json or .app.json file. Can be passed more than once. Defaults to Patch ent/app raw files.",
    )
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show high-level file, component, and reference counts.")
    summary.add_argument("--json", action="store_true")
    summary.set_defaults(func=command_summary)

    appearances = subparsers.add_parser("appearances", help="List root-entity and app appearance definitions.")
    appearances.add_argument("--limit", type=int, default=200)
    appearances.add_argument("--offset", type=int, default=0)
    appearances.add_argument("--json", action="store_true")
    appearances.set_defaults(func=command_appearances)

    appearance = subparsers.add_parser("appearance", help="Inspect an appearance by id, for example a0.")
    appearance.add_argument("selector")
    appearance.add_argument("--raw", action="store_true")
    appearance.set_defaults(func=command_appearance)

    components = subparsers.add_parser("components", help="List root and appearance components.")
    components.add_argument("--file", help="Only show one loaded file id, such as f0.")
    components.add_argument("--owner", help="Filter by owner label substring, such as root or a1.")
    components.add_argument("--type", help="Filter by full or short component type substring.")
    components.add_argument("--resources-only", action="store_true", help="Only show components with resource paths.")
    components.add_argument("--limit", type=int, default=200)
    components.add_argument("--offset", type=int, default=0)
    components.add_argument("--json", action="store_true")
    components.set_defaults(func=command_components)

    component = subparsers.add_parser("component", help="Inspect one component by id, for example c37.")
    component.add_argument("selector")
    component.add_argument("--raw", action="store_true")
    component.set_defaults(func=command_component)

    refs = subparsers.add_parser("refs", help="List resource, TweakDBID, and NodeRef references.")
    refs.add_argument("--kind", choices=["ResourcePath", "DepotPath", "TweakDBID", "NodeRef"])
    refs.add_argument("--file", help="Only show one loaded file id, such as f0.")
    refs.add_argument("--limit", type=int, default=200)
    refs.add_argument("--offset", type=int, default=0)
    refs.add_argument("--json", action="store_true")
    refs.set_defaults(func=command_refs)

    handles = subparsers.add_parser("handles", help="List CR2W HandleId wrappers.")
    handles.add_argument("--file", help="Only show one loaded file id, such as f0.")
    handles.add_argument("--type", help="Filter by full or short $type substring.")
    handles.add_argument("--limit", type=int, default=200)
    handles.add_argument("--offset", type=int, default=0)
    handles.add_argument("--json", action="store_true")
    handles.set_defaults(func=command_handles)

    handle = subparsers.add_parser("handle", help="Inspect a handle by file id and HandleId.")
    handle.add_argument("file")
    handle.add_argument("handle")
    handle.add_argument("--raw", action="store_true")
    handle.set_defaults(func=command_handle)

    search = subparsers.add_parser("search", help="Search scalar keys and values by substring.")
    search.add_argument("terms", nargs="+")
    search.add_argument("--limit", type=int, default=50)
    search.add_argument("--json", action="store_true")
    search.set_defaults(func=command_search)

    types = subparsers.add_parser("types", help="Count every CR2W $type in loaded files.")
    types.add_argument("--file", help="Only show one loaded file id, such as f0.")
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
        raise SystemExit("No files were provided and the default Patch ent/app raw files do not exist.")
    explorer = EntAppExplorer(paths)
    args.func(explorer, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
