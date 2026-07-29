from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PureWindowsPath
from typing import Any, Callable, Iterable, Iterator, Mapping, Sequence


PIPELINE_VERSION = "world-location-archive-dependencies-v2"
BLENDER_WOLVENKIT_COMPAT_VERSION = "8.17-compatible (ghostline-red staged JSON)"
SERIALIZABLE_EXTENSIONS = frozenset({".app", ".ent"})
RESOURCE_KINDS = {
    ".app": "appearance",
    ".ent": "entity",
    ".inkatlas": "ink_atlas",
    ".mesh": "mesh",
    ".mi": "material_instance",
    ".mlmask": "multilayer_mask",
    ".mlsetup": "multilayer_setup",
    ".mt": "material_template",
    ".streamingblock": "streaming_block",
    ".streamingsector": "streaming_sector",
    ".xbm": "texture",
}


class DependencyStagingError(RuntimeError):
    """Raised when the dependency pipeline cannot produce an honest report."""


@dataclass(frozen=True)
class ResourceClassification:
    resource: str
    extension: str
    kind: str
    serializable: bool

    @property
    def resource_type(self) -> str:
        return self.extension.removeprefix(".") or "unknown"


@dataclass(frozen=True)
class DependencyResource:
    resource: str
    extension: str
    kind: str
    serializable: bool
    status: str
    dependencies: tuple[str, ...]
    cache_fingerprint: str = ""
    json_path: Path | None = None
    cache_hit: bool = False
    error: str = ""

    @property
    def resource_type(self) -> str:
        return self.extension.removeprefix(".") or "unknown"

    def to_report(self) -> dict[str, Any]:
        return {
            "resource": self.resource,
            "extension": self.extension,
            "resource_type": self.resource_type,
            "kind": self.kind,
            "serializable": self.serializable,
            "status": self.status,
            "dependencies": list(self.dependencies),
            "cache_fingerprint": self.cache_fingerprint,
            "json_path": str(self.json_path.resolve()) if self.json_path else "",
            "cache_hit": self.cache_hit,
            "error": self.error,
        }


@dataclass(frozen=True)
class BatchJob:
    resource: str
    output: Path


@dataclass(frozen=True)
class BatchInvocation:
    fingerprint: str
    jobs: tuple[BatchJob, ...]
    manifest_path: Path
    report_path: Path
    command: tuple[str, ...]
    cwd: Path


@dataclass(frozen=True)
class BatchRunResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""


@dataclass(frozen=True)
class BatchSummary:
    fingerprint: str
    resources: tuple[str, ...]
    returncode: int
    failures: tuple[str, ...]

    def to_report(self) -> dict[str, Any]:
        return {
            "fingerprint": self.fingerprint,
            "resources": list(self.resources),
            "returncode": self.returncode,
            "failures": list(self.failures),
        }


@dataclass(frozen=True)
class DependencyClosure:
    roots: tuple[str, ...]
    resources: tuple[DependencyResource, ...]
    batches: tuple[BatchSummary, ...]
    identity_fingerprint: str

    @property
    def graph(self) -> dict[str, tuple[str, ...]]:
        return {resource.resource: resource.dependencies for resource in self.resources}

    @property
    def failures(self) -> tuple[DependencyResource, ...]:
        return tuple(resource for resource in self.resources if resource.error)

    @property
    def successes(self) -> tuple[DependencyResource, ...]:
        return tuple(
            resource
            for resource in self.resources
            if resource.serializable and resource.status == "ready"
        )

    def successful_json_sources(self) -> dict[str, Path]:
        return {
            resource.resource: resource.json_path
            for resource in self.resources
            if resource.serializable
            and resource.status == "ready"
            and resource.json_path is not None
        }

    def successful_documents(self) -> dict[str, Any]:
        return {
            resource.resource: read_json(resource.json_path)
            for resource in self.successes
            if resource.json_path is not None
        }

    def raise_for_failures(self) -> None:
        if not self.failures:
            return
        details = "; ".join(
            f"{failure.resource}: {failure.error}" for failure in self.failures
        )
        raise DependencyStagingError(
            f"{len(self.failures)} archive dependencies failed: {details}"
        )

    def to_report(self) -> dict[str, Any]:
        serializable = sum(resource.serializable for resource in self.resources)
        ready = sum(resource.status == "ready" for resource in self.resources)
        return {
            "schema_version": 1,
            "pipeline": PIPELINE_VERSION,
            "identity_fingerprint": self.identity_fingerprint,
            "roots": list(self.roots),
            "summary": {
                "resources": len(self.resources),
                "serializable": serializable,
                "ready_json": ready,
                "leaf_resources": len(self.resources) - serializable,
                "failures": len(self.failures),
                "batch_invocations": len(self.batches),
            },
            "graph": [
                {
                    "resource": resource.resource,
                    "dependencies": list(resource.dependencies),
                }
                for resource in self.resources
            ],
            "resources": [resource.to_report() for resource in self.resources],
            "batches": [batch.to_report() for batch in self.batches],
        }


@dataclass(frozen=True)
class StateDependencyClosure:
    closure: DependencyClosure
    state_resources: dict[str, tuple[str, ...]]
    appearance_selections: dict[str, dict[str, tuple[str, ...]]] = field(
        default_factory=dict
    )
    unmatched_appearance_selections: dict[str, dict[str, tuple[str, ...]]] = field(
        default_factory=dict
    )

    def successful_json_sources(self, state_key: str) -> dict[str, Path]:
        selected = set(self.state_resources[state_key])
        return {
            resource: source
            for resource, source in self.closure.successful_json_sources().items()
            if resource in selected
        }

    def to_report(self) -> dict[str, Any]:
        return {
            "closure": self.closure.to_report(),
            "states": [
                {
                    "state_key": state_key,
                    "resources": list(resources),
                    "appearance_selections": [
                        {"resource": resource, "names": list(names)}
                        for resource, names in self.appearance_selections.get(
                            state_key, {}
                        ).items()
                    ],
                    "unmatched_appearance_selections": [
                        {"resource": resource, "names": list(names)}
                        for resource, names in self.unmatched_appearance_selections.get(
                            state_key, {}
                        ).items()
                    ],
                }
                for state_key, resources in self.state_resources.items()
            ],
        }


@dataclass(frozen=True)
class InstalledDependency:
    resource: str
    source: Path
    target: Path
    action: str
    compatibility_defaults: tuple[str, ...] = ()

    def to_report(self) -> dict[str, str]:
        return {
            "resource": self.resource,
            "source": str(self.source.resolve()),
            "target": str(self.target.resolve()),
            "action": self.action,
            "compatibility_defaults": list(self.compatibility_defaults),
        }


BatchRunner = Callable[
    [BatchInvocation], BatchRunResult | subprocess.CompletedProcess[str] | int
]


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(block_size):
            digest.update(chunk)
    return digest.hexdigest()


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
        prefix=f".{path.name}.",
    ) as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DependencyStagingError(f"Unable to read JSON {path}: {exc}") from exc


def normalize_depot_path(resource: str) -> str:
    if not isinstance(resource, str):
        raise DependencyStagingError(
            f"Depot resource must be a string, got {type(resource).__name__}"
        )
    candidate = resource.strip().replace("/", "\\")
    if not candidate or "\x00" in candidate:
        raise DependencyStagingError("Depot resource path is empty or contains NUL")
    path = PureWindowsPath(candidate)
    if path.is_absolute() or path.drive or path.root:
        raise DependencyStagingError(f"Depot resource must be relative: {resource!r}")
    if any(part in {"", ".", ".."} or ":" in part for part in path.parts):
        raise DependencyStagingError(f"Unsafe depot resource path: {resource!r}")
    return "\\".join(part.casefold() for part in path.parts)


def classify_resource(resource: str) -> ResourceClassification:
    normalized = normalize_depot_path(resource)
    extension = PureWindowsPath(normalized).suffix.casefold()
    return ResourceClassification(
        resource=normalized,
        extension=extension,
        kind=RESOURCE_KINDS.get(extension, extension.removeprefix(".") or "unknown"),
        serializable=extension in SERIALIZABLE_EXTENSIONS,
    )


def resource_type(resource: str) -> str:
    return classify_resource(resource).resource_type


def _depot_value(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        nested = value.get("$value")
        return nested.strip() if isinstance(nested, str) else ""
    return ""


def _walk_depot_values(value: Any) -> Iterator[str]:
    if isinstance(value, dict):
        if "DepotPath" in value:
            depot_path = _depot_value(value["DepotPath"])
            if depot_path:
                yield depot_path
        for child in value.values():
            yield from _walk_depot_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_depot_values(child)


def extract_depot_paths(document: Any) -> tuple[str, ...]:
    return tuple(
        sorted({normalize_depot_path(path) for path in _walk_depot_values(document)})
    )


@dataclass(frozen=True)
class _AppearanceDependencyScan:
    dependencies: tuple[str, ...]
    unfiltered_dependencies: tuple[str, ...]
    propagated_selections: dict[str, tuple[str, ...] | None]
    effective_selections: tuple[str, ...]
    unmatched_selections: tuple[str, ...]


def _scalar_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if not isinstance(value, dict):
        return ""
    nested = value.get("$value")
    if isinstance(nested, str):
        return nested.strip()
    return ""


def _root_chunk(document: Any) -> dict[str, Any]:
    if not isinstance(document, dict):
        return {}
    data = document.get("Data")
    if not isinstance(data, dict):
        return {}
    root = data.get("RootChunk")
    return root if isinstance(root, dict) else {}


def _walk_typed_objects(value: Any, red_type: str) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if value.get("$type") == red_type:
            yield value
            return
        for child in value.values():
            yield from _walk_typed_objects(child, red_type)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_typed_objects(child, red_type)


def _walk_filtered_depot_values(
    value: Any,
    *,
    filtered_type: str,
    name_key: str,
    selected_names: frozenset[str],
    excluded_keys: frozenset[str] = frozenset(),
) -> Iterator[str]:
    if isinstance(value, dict):
        if value.get("$type") == filtered_type:
            name = _scalar_text(value.get(name_key)).casefold()
            if name not in selected_names:
                return
        if "DepotPath" in value:
            depot_path = _depot_value(value["DepotPath"])
            if depot_path:
                yield depot_path
        for key, child in value.items():
            if key.casefold() in excluded_keys:
                continue
            yield from _walk_filtered_depot_values(
                child,
                filtered_type=filtered_type,
                name_key=name_key,
                selected_names=selected_names,
                excluded_keys=excluded_keys,
            )
    elif isinstance(value, list):
        for child in value:
            yield from _walk_filtered_depot_values(
                child,
                filtered_type=filtered_type,
                name_key=name_key,
                selected_names=selected_names,
                excluded_keys=excluded_keys,
            )


def _ordered_names(names: Iterable[str]) -> tuple[str, ...]:
    candidates: list[str] = []
    for name in names:
        if not isinstance(name, str):
            raise DependencyStagingError(
                "Appearance selections must contain only strings"
            )
        candidate = name.strip()
        if not candidate:
            raise DependencyStagingError("Appearance selection names must not be empty")
        candidates.append(candidate)
    normalized: dict[str, str] = {}
    for candidate in sorted(candidates, key=lambda item: (item.casefold(), item)):
        normalized.setdefault(candidate.casefold(), candidate)
    return tuple(normalized[key] for key in sorted(normalized))


def _appearance_filtered_dependencies(
    document: Any,
    extension: str,
    selections: Iterable[str] | None,
) -> _AppearanceDependencyScan:
    if selections is None or extension not in {".ent", ".app"}:
        return _AppearanceDependencyScan(
            dependencies=extract_depot_paths(document),
            unfiltered_dependencies=extract_depot_paths(document),
            propagated_selections={},
            effective_selections=(),
            unmatched_selections=(),
        )

    requested = _ordered_names(selections)
    if extension == ".ent":
        filtered_type = "entTemplateAppearance"
        name_key = "name"
        effective = [name for name in requested if name.casefold() != "default"]
        requested_default = any(name.casefold() == "default" for name in requested)
        default_name = _scalar_text(_root_chunk(document).get("defaultAppearance"))
        if requested_default and default_name and default_name.casefold() != "none":
            effective.append(default_name)
        effective_names = _ordered_names(effective) if effective else ()
    else:
        filtered_type = "appearanceAppearanceDefinition"
        name_key = "name"
        requested_default = False
        default_name = ""
        effective_names = requested

    selected_names = frozenset(name.casefold() for name in effective_names)
    # Appearance proxyMesh resources are low-detail streaming substitutes. The
    # location catalog deliberately resolves the selected definition's LOD0
    # component/compiledData geometry instead of staging those external proxies.
    excluded_keys = frozenset({"proxymesh"}) if extension == ".app" else frozenset()
    dependencies = tuple(
        sorted(
            {
                normalize_depot_path(path)
                for path in _walk_filtered_depot_values(
                    document,
                    filtered_type=filtered_type,
                    name_key=name_key,
                    selected_names=selected_names,
                    excluded_keys=excluded_keys,
                )
            }
        )
    )
    unfiltered_dependencies = tuple(
        sorted(
            {
                normalize_depot_path(path)
                for path in _walk_filtered_depot_values(
                    document,
                    filtered_type=filtered_type,
                    name_key=name_key,
                    selected_names=frozenset(),
                    excluded_keys=excluded_keys,
                )
            }
        )
    )

    matched_names: set[str] = set()
    propagated: dict[str, tuple[str, ...] | None] = {}
    propagated_names: dict[str, set[str]] = {}
    for entry in _walk_typed_objects(document, filtered_type):
        entry_name = _scalar_text(entry.get(name_key))
        if entry_name.casefold() not in selected_names:
            continue
        matched_names.add(entry_name.casefold())
        if extension != ".ent":
            continue
        appearance_name = _scalar_text(entry.get("appearanceName"))
        for depot_path in _walk_depot_values(entry.get("appearanceResource")):
            resource = normalize_depot_path(depot_path)
            if classify_resource(resource).extension != ".app":
                continue
            if not appearance_name:
                propagated[resource] = None
                propagated_names.pop(resource, None)
            elif propagated.get(resource, ()) is not None:
                propagated_names.setdefault(resource, set()).add(appearance_name)

    for resource, names in propagated_names.items():
        propagated[resource] = _ordered_names(names)

    unmatched = [
        name for name in effective_names if name.casefold() not in matched_names
    ]
    if (
        requested_default
        and default_name
        and default_name.casefold() != "none"
        and default_name.casefold() not in matched_names
    ):
        unmatched.append("default")
    return _AppearanceDependencyScan(
        dependencies=dependencies,
        unfiltered_dependencies=unfiltered_dependencies,
        propagated_selections={
            resource: propagated[resource] for resource in sorted(propagated)
        },
        effective_selections=effective_names,
        unmatched_selections=_ordered_names(unmatched) if unmatched else (),
    )


def compute_state_closures(
    graph: Mapping[str, Iterable[str]],
    state_roots: Mapping[str, Iterable[str]],
) -> dict[str, tuple[str, ...]]:
    normalized_graph: dict[str, tuple[str, ...]] = {}
    for resource, dependencies in graph.items():
        key = normalize_depot_path(resource)
        normalized_graph[key] = tuple(
            sorted({normalize_depot_path(dependency) for dependency in dependencies})
        )

    result: dict[str, tuple[str, ...]] = {}
    for state_key in sorted(state_roots):
        if not state_key:
            raise DependencyStagingError("State keys must not be empty")
        pending = list(
            reversed(
                sorted(
                    {
                        normalize_depot_path(resource)
                        for resource in state_roots[state_key]
                    }
                )
            )
        )
        visited: set[str] = set()
        while pending:
            resource = pending.pop()
            if resource in visited:
                continue
            visited.add(resource)
            for dependency in reversed(normalized_graph.get(resource, ())):
                if dependency not in visited:
                    pending.append(dependency)
        result[state_key] = tuple(sorted(visited))
    return result


def _archive_inventory_identity(archives_root: Path) -> dict[str, Any]:
    archive_files = sorted(
        (path for path in archives_root.rglob("*.archive") if path.is_file()),
        key=lambda path: path.relative_to(archives_root).as_posix().casefold(),
    )
    inventory = []
    for path in archive_files:
        stat = path.stat()
        inventory.append(
            {
                "path": path.relative_to(archives_root).as_posix().casefold(),
                "size": stat.st_size,
                "mtime_ns": stat.st_mtime_ns,
            }
        )
    game_root = archives_root.parent.parent
    executable = game_root / "bin/x64/Cyberpunk2077.exe"
    return {
        "archives": inventory,
        "executable": (
            {
                "size": executable.stat().st_size,
                "sha256": sha256_file(executable),
            }
            if executable.is_file()
            else None
        ),
    }


def _atomic_install(source: Path, target: Path) -> str:
    target.parent.mkdir(parents=True, exist_ok=True)
    target_existed = target.exists()
    if target.is_file() and sha256_file(target) == sha256_file(source):
        return "reused"
    with tempfile.NamedTemporaryFile(
        dir=target.parent,
        delete=False,
        prefix=f".{target.name}.",
    ) as handle:
        temporary = Path(handle.name)
    temporary.unlink()
    try:
        try:
            os.link(source, temporary)
            action = "hardlinked"
        except OSError:
            shutil.copy2(source, temporary)
            action = "copied"
        os.replace(temporary, target)
        return "replaced" if target_existed else action
    finally:
        temporary.unlink(missing_ok=True)


def complete_blender_dependency_defaults(
    document: Any, extension: str
) -> tuple[dict[str, Any], tuple[str, ...]]:
    """Fill the narrow CR2W defaults indexed directly by Cyberpunk IO Suite.

    RED serializers may omit class-default fields.  Cyberpunk IO Suite 1.8.0
    accepts that for appearance JSON, but its entity loader indexes five fields
    without fallbacks.  Complete only those fields and the compatible exporter
    marker in the staged copy; the canonical cached serialization is unchanged.
    """

    if not isinstance(document, dict):
        raise DependencyStagingError("Dependency JSON must be an object")
    staged = copy.deepcopy(document)
    inserted: list[str] = []
    header = staged.setdefault("Header", {})
    if not isinstance(header, dict):
        raise DependencyStagingError("Dependency JSON Header must be an object")
    original_version = str(header.get("WolvenKitVersion", ""))
    if "8.17" not in original_version:
        if original_version:
            header.setdefault("GhostlineOriginalExporterVersion", original_version)
        header["WolvenKitVersion"] = BLENDER_WOLVENKIT_COMPAT_VERSION
        inserted.append("Header.WolvenKitVersion")

    if extension.casefold() == ".ent":
        root = _root_chunk(staged)
        if not root:
            raise DependencyStagingError("Entity JSON has no Data.RootChunk object")
        defaults: tuple[tuple[str, Any], ...] = (
            ("appearances", []),
            ("components", []),
            ("compiledData", None),
            ("resolvedDependencies", []),
            (
                "defaultAppearance",
                {"$type": "CName", "$storage": "string", "$value": "None"},
            ),
        )
        for key, value in defaults:
            if key not in root:
                root[key] = copy.deepcopy(value)
                inserted.append(f"entEntityTemplate.{key}")
    return staged, tuple(sorted(inserted))


def install_dependency_jsons(
    closure: DependencyClosure,
    project_raw: Path,
    *,
    resources: Iterable[str] | None = None,
    fail_on_errors: bool = True,
) -> tuple[InstalledDependency, ...]:
    selected = (
        {normalize_depot_path(resource) for resource in resources}
        if resources is not None
        else {resource.resource for resource in closure.resources}
    )
    records = {
        resource.resource: resource
        for resource in closure.resources
        if resource.resource in selected
    }
    unknown = sorted(selected - records.keys())
    if unknown:
        raise DependencyStagingError(
            f"Requested resources are absent from the closure: {', '.join(unknown)}"
        )
    failures = sorted(
        (
            resource
            for resource in records.values()
            if resource.serializable and resource.status != "ready"
        ),
        key=lambda resource: resource.resource,
    )
    if failures and fail_on_errors:
        raise DependencyStagingError(
            "Cannot install failed dependencies: "
            + "; ".join(
                f"{resource.resource}: {resource.error or resource.status}"
                for resource in failures
            )
        )

    installed: list[InstalledDependency] = []
    for resource in sorted(records.values(), key=lambda row: row.resource):
        if not resource.serializable or resource.status != "ready":
            continue
        if resource.json_path is None or not resource.json_path.is_file():
            raise DependencyStagingError(
                f"Cached JSON disappeared for {resource.resource}: {resource.json_path}"
            )
        relative = Path(*PureWindowsPath(resource.resource).parts)
        target = Path(f"{project_raw / relative}.json")
        source_document = read_json(resource.json_path)
        staged_document, compatibility_defaults = complete_blender_dependency_defaults(
            source_document, resource.extension
        )
        if staged_document == source_document:
            action = _atomic_install(resource.json_path, target)
        else:
            target_existed = target.is_file()
            target_matches = False
            if target_existed:
                try:
                    target_matches = read_json(target) == staged_document
                except DependencyStagingError:
                    target_matches = False
            if target_matches:
                action = "reused"
            else:
                write_json_atomic(target, staged_document)
                action = "replaced" if target_existed else "generated"
        installed.append(
            InstalledDependency(
                resource=resource.resource,
                source=resource.json_path,
                target=target,
                action=action,
                compatibility_defaults=compatibility_defaults,
            )
        )
    return tuple(installed)


def _default_batch_runner(invocation: BatchInvocation) -> BatchRunResult:
    completed = subprocess.run(
        invocation.command,
        cwd=invocation.cwd,
        text=True,
        capture_output=True,
        check=False,
    )
    return BatchRunResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def _coerce_run_result(
    result: BatchRunResult | subprocess.CompletedProcess[str] | int,
) -> BatchRunResult:
    if isinstance(result, BatchRunResult):
        return result
    if isinstance(result, int):
        return BatchRunResult(returncode=result)
    if isinstance(result, subprocess.CompletedProcess):
        return BatchRunResult(
            returncode=result.returncode,
            stdout=str(result.stdout or ""),
            stderr=str(result.stderr or ""),
        )
    raise DependencyStagingError(
        f"Batch runner returned unsupported result {type(result).__name__}"
    )


class ArchiveDependencyResolver:
    def __init__(
        self,
        *,
        cache_root: Path,
        ghostline_red: Path,
        schemas: Path | Sequence[Path],
        archives_root: Path,
        game_identity: Any | None = None,
        kraken: Path | None = None,
        threads: int = 8,
        runner: BatchRunner | None = None,
        cwd: Path | None = None,
    ) -> None:
        self.cache_root = cache_root.resolve()
        self.ghostline_red = ghostline_red.resolve()
        if isinstance(schemas, (str, os.PathLike)):
            self.schemas = (Path(schemas).resolve(),)
        else:
            self.schemas = tuple(Path(path).resolve() for path in schemas)
        self.archives_root = archives_root.resolve()
        self.kraken = kraken.resolve() if kraken is not None else None
        if threads < 0:
            raise DependencyStagingError("threads must be zero or greater")
        self.threads = threads
        self.runner = runner or _default_batch_runner
        self.cwd = (cwd or Path(__file__).resolve().parents[1]).resolve()
        self._validate_inputs()
        identity = {
            "pipeline": PIPELINE_VERSION,
            "serializable_extensions": sorted(SERIALIZABLE_EXTENSIONS),
            "ghostline_red": {
                "size": self.ghostline_red.stat().st_size,
                "sha256": sha256_file(self.ghostline_red),
            },
            "schemas": [
                {"size": path.stat().st_size, "sha256": sha256_file(path)}
                for path in self.schemas
            ],
            "game": (
                game_identity
                if game_identity is not None
                else _archive_inventory_identity(self.archives_root)
            ),
            "kraken": (
                {
                    "size": self.kraken.stat().st_size,
                    "sha256": sha256_file(self.kraken),
                }
                if self.kraken is not None
                else None
            ),
        }
        self.identity_document = identity
        self.identity_fingerprint = sha256_text(canonical_json(identity))

    def _validate_inputs(self) -> None:
        if not self.ghostline_red.is_file():
            raise DependencyStagingError(
                f"ghostline-red executable is missing: {self.ghostline_red}"
            )
        if not self.schemas:
            raise DependencyStagingError("At least one RED schema is required")
        for schema in self.schemas:
            if not schema.is_file():
                raise DependencyStagingError(f"RED schema is missing: {schema}")
        if not self.archives_root.is_dir():
            raise DependencyStagingError(
                f"Game archive root is missing: {self.archives_root}"
            )
        if self.kraken is not None and not self.kraken.is_file():
            raise DependencyStagingError(f"Kraken library is missing: {self.kraken}")

    def _resource_fingerprint(self, resource: str) -> str:
        return sha256_text(
            canonical_json(
                {
                    "identity": self.identity_fingerprint,
                    "resource": normalize_depot_path(resource),
                }
            )
        )

    def _cache_paths(self, fingerprint: str) -> tuple[Path, Path]:
        directory = self.cache_root / "archive-json" / fingerprint[:2] / fingerprint
        return directory / "resource.json", directory / "cache-record.json"

    def _cached_json(self, resource: str, fingerprint: str) -> Path | None:
        json_path, record_path = self._cache_paths(fingerprint)
        if not json_path.is_file() or not record_path.is_file():
            return None
        try:
            record = read_json(record_path)
            if not isinstance(record, dict):
                return None
            if record.get("resource") != resource:
                return None
            if record.get("cache_fingerprint") != fingerprint:
                return None
            if record.get("sha256") != sha256_file(json_path):
                return None
            document = read_json(json_path)
            if not isinstance(document, dict):
                return None
        except (DependencyStagingError, OSError):
            return None
        return json_path

    def _command(self, manifest: Path, report: Path) -> tuple[str, ...]:
        command = [str(self.ghostline_red)]
        if self.kraken is not None:
            command.extend(("--kraken", str(self.kraken)))
        command.extend(("cr2w-serialize-batch", str(manifest)))
        for schema in self.schemas:
            command.extend(("--schema", str(schema)))
        command.extend(
            (
                "--archives-root",
                str(self.archives_root),
                "--report",
                str(report),
                "--threads",
                str(self.threads),
            )
        )
        return tuple(command)

    def _run_batch(
        self, resources: Sequence[str]
    ) -> tuple[
        dict[str, tuple[Path | None, str]],
        BatchSummary,
    ]:
        ordered = tuple(sorted({normalize_depot_path(item) for item in resources}))
        batch_fingerprint = sha256_text(
            canonical_json(
                {"identity": self.identity_fingerprint, "resources": ordered}
            )
        )[:24]
        batch_root = self.cache_root / "batches" / batch_fingerprint
        manifest_path = batch_root / "manifest.json"
        report_path = batch_root / "report.json"
        output_root = batch_root / "outputs"
        jobs = tuple(
            BatchJob(
                resource=resource,
                output=output_root / f"{sha256_text(resource)}.json",
            )
            for resource in ordered
        )
        for job in jobs:
            job.output.unlink(missing_ok=True)
        report_path.unlink(missing_ok=True)
        write_json_atomic(
            manifest_path,
            {
                "jobs": [
                    {"resource": job.resource, "output": str(job.output.resolve())}
                    for job in jobs
                ]
            },
        )
        invocation = BatchInvocation(
            fingerprint=batch_fingerprint,
            jobs=jobs,
            manifest_path=manifest_path,
            report_path=report_path,
            command=self._command(manifest_path, report_path),
            cwd=self.cwd,
        )
        try:
            result = _coerce_run_result(self.runner(invocation))
        except DependencyStagingError:
            raise
        except Exception as exc:
            raise DependencyStagingError(
                f"CR2W batch runner failed for {batch_fingerprint}: {exc}"
            ) from exc
        if not report_path.is_file():
            output = (result.stderr or result.stdout).strip()
            suffix = f": {output[-2000:]}" if output else ""
            raise DependencyStagingError(
                "ghostline-red did not write the required CR2W batch report "
                f"{report_path} (exit {result.returncode}){suffix}"
            )
        report = read_json(report_path)
        if not isinstance(report, list):
            raise DependencyStagingError(
                f"CR2W batch report must be an array: {report_path}"
            )
        outcomes: dict[str, dict[str, Any]] = {}
        for raw_outcome in report:
            if not isinstance(raw_outcome, dict):
                raise DependencyStagingError(
                    f"CR2W batch report contains a non-object outcome: {report_path}"
                )
            raw_resource = raw_outcome.get("resource")
            try:
                resource = normalize_depot_path(raw_resource)
            except DependencyStagingError as exc:
                raise DependencyStagingError(
                    f"CR2W batch report has an invalid resource: {raw_resource!r}"
                ) from exc
            if resource in outcomes:
                raise DependencyStagingError(
                    f"CR2W batch report duplicated {resource}: {report_path}"
                )
            outcomes[resource] = raw_outcome
        unexpected = sorted(outcomes.keys() - set(ordered))
        if unexpected:
            raise DependencyStagingError(
                "CR2W batch report contains unexpected resources: "
                + ", ".join(unexpected)
            )

        resolved: dict[str, tuple[Path | None, str]] = {}
        failed: list[str] = []
        for job in jobs:
            outcome = outcomes.get(job.resource)
            error = ""
            if outcome is None:
                error = "native batch report omitted this resource"
            else:
                reported_output = Path(str(outcome.get("output", "")))
                try:
                    output_matches = reported_output.resolve() == job.output.resolve()
                except OSError:
                    output_matches = False
                if not output_matches:
                    error = (
                        "native batch report output mismatch: "
                        f"{reported_output} != {job.output}"
                    )
                elif outcome.get("error"):
                    error = str(outcome["error"])
                elif not job.output.is_file():
                    error = "native batch reported success but created no JSON"
                else:
                    try:
                        document = read_json(job.output)
                        if not isinstance(document, dict):
                            error = "native batch output is not a CR2W JSON object"
                    except DependencyStagingError as exc:
                        error = str(exc)
            if error:
                failed.append(job.resource)
                resolved[job.resource] = (None, error)
                continue
            fingerprint = self._resource_fingerprint(job.resource)
            cache_json, cache_record = self._cache_paths(fingerprint)
            _atomic_install(job.output, cache_json)
            digest = sha256_file(cache_json)
            write_json_atomic(
                cache_record,
                {
                    "schema_version": 1,
                    "pipeline": PIPELINE_VERSION,
                    "resource": job.resource,
                    "cache_fingerprint": fingerprint,
                    "identity_fingerprint": self.identity_fingerprint,
                    "sha256": digest,
                    "bytes": cache_json.stat().st_size,
                },
            )
            resolved[job.resource] = (cache_json, "")

        if result.returncode != 0 and not failed:
            raise DependencyStagingError(
                "ghostline-red returned a nonzero status but its batch report "
                f"declared every job successful (exit {result.returncode})"
            )
        summary = BatchSummary(
            fingerprint=batch_fingerprint,
            resources=ordered,
            returncode=result.returncode,
            failures=tuple(failed),
        )
        return resolved, summary

    def resolve(self, roots: Iterable[str]) -> DependencyClosure:
        normalized_roots = tuple(
            sorted({normalize_depot_path(resource) for resource in roots})
        )
        if not normalized_roots:
            return DependencyClosure(
                roots=(),
                resources=(),
                batches=(),
                identity_fingerprint=self.identity_fingerprint,
            )
        known = set(normalized_roots)
        resolved_serializable: set[str] = set()
        graph: dict[str, tuple[str, ...]] = {}
        outcomes: dict[str, tuple[Path | None, str, bool]] = {}
        batches: list[BatchSummary] = []

        while True:
            frontier = tuple(
                sorted(
                    resource
                    for resource in known - resolved_serializable
                    if classify_resource(resource).serializable
                )
            )
            if not frontier:
                break
            missing: list[str] = []
            for resource in frontier:
                fingerprint = self._resource_fingerprint(resource)
                cached = self._cached_json(resource, fingerprint)
                if cached is None:
                    missing.append(resource)
                else:
                    outcomes[resource] = (cached, "", True)
            if missing:
                batch_outcomes, summary = self._run_batch(missing)
                batches.append(summary)
                for resource, (json_path, error) in batch_outcomes.items():
                    outcomes[resource] = (json_path, error, False)

            for resource in frontier:
                resolved_serializable.add(resource)
                json_path, error, _cache_hit = outcomes[resource]
                if error or json_path is None:
                    graph[resource] = ()
                    continue
                try:
                    dependencies = extract_depot_paths(read_json(json_path))
                except DependencyStagingError as exc:
                    outcomes[resource] = (json_path, str(exc), _cache_hit)
                    graph[resource] = ()
                    continue
                graph[resource] = dependencies
                known.update(dependencies)

        for resource in known:
            graph.setdefault(resource, ())
        records: list[DependencyResource] = []
        for resource in sorted(known):
            classification = classify_resource(resource)
            if not classification.serializable:
                records.append(
                    DependencyResource(
                        resource=resource,
                        extension=classification.extension,
                        kind=classification.kind,
                        serializable=False,
                        status="leaf",
                        dependencies=graph[resource],
                    )
                )
                continue
            json_path, error, cache_hit = outcomes[resource]
            records.append(
                DependencyResource(
                    resource=resource,
                    extension=classification.extension,
                    kind=classification.kind,
                    serializable=True,
                    status="failed" if error else "ready",
                    dependencies=graph[resource],
                    cache_fingerprint=self._resource_fingerprint(resource),
                    json_path=json_path,
                    cache_hit=cache_hit,
                    error=error,
                )
            )
        return DependencyClosure(
            roots=normalized_roots,
            resources=tuple(records),
            batches=tuple(batches),
            identity_fingerprint=self.identity_fingerprint,
        )

    def _resolve_selected_states(
        self,
        normalized_roots: Mapping[str, tuple[str, ...]],
        root_selections: Mapping[str, Mapping[str, tuple[str, ...]]],
    ) -> StateDependencyClosure:
        state_known = {
            state_key: set(resources)
            for state_key, resources in normalized_roots.items()
        }
        state_demands: dict[str, dict[str, tuple[str, ...] | None]] = {}
        for state_key, resources in normalized_roots.items():
            configured = root_selections.get(state_key, {})
            state_demands[state_key] = {
                resource: configured.get(resource) for resource in resources
            }

        state_graph: dict[str, dict[str, tuple[str, ...]]] = {
            state_key: {} for state_key in normalized_roots
        }
        processed: dict[str, dict[str, tuple[str, ...] | None]] = {
            state_key: {} for state_key in normalized_roots
        }
        effective_selections: dict[str, dict[str, tuple[str, ...]]] = {
            state_key: {} for state_key in normalized_roots
        }
        unmatched_selections: dict[str, dict[str, tuple[str, ...]]] = {
            state_key: {} for state_key in normalized_roots
        }
        outcomes: dict[str, tuple[Path | None, str, bool]] = {}
        documents: dict[str, Any] = {}
        batches: list[BatchSummary] = []

        def merge_demand(
            demands: dict[str, tuple[str, ...] | None],
            resource: str,
            incoming: tuple[str, ...] | None,
        ) -> bool:
            if resource not in demands:
                demands[resource] = incoming
                return True
            current = demands[resource]
            if current is None or current == incoming:
                return False
            if incoming is None:
                demands[resource] = None
                return True
            merged = _ordered_names((*current, *incoming))
            if merged == current:
                return False
            demands[resource] = merged
            return True

        while True:
            global_known = {
                resource for resources in state_known.values() for resource in resources
            }
            frontier = tuple(
                sorted(
                    resource
                    for resource in global_known
                    if classify_resource(resource).serializable
                    and resource not in outcomes
                )
            )
            missing: list[str] = []
            for resource in frontier:
                fingerprint = self._resource_fingerprint(resource)
                cached = self._cached_json(resource, fingerprint)
                if cached is None:
                    missing.append(resource)
                else:
                    outcomes[resource] = (cached, "", True)
            if missing:
                batch_outcomes, summary = self._run_batch(missing)
                batches.append(summary)
                for resource, (json_path, error) in batch_outcomes.items():
                    outcomes[resource] = (json_path, error, False)

            changed = False
            for state_key in sorted(state_known):
                known = state_known[state_key]
                demands = state_demands[state_key]
                for resource in sorted(tuple(known)):
                    classification = classify_resource(resource)
                    if not classification.serializable:
                        state_graph[state_key].setdefault(resource, ())
                        continue
                    demand = demands[resource]
                    if (
                        resource in processed[state_key]
                        and processed[state_key][resource] == demand
                    ):
                        continue
                    processed[state_key][resource] = demand
                    json_path, error, cache_hit = outcomes[resource]
                    if error or json_path is None:
                        state_graph[state_key][resource] = ()
                        if demand is not None:
                            effective_selections[state_key][resource] = demand
                        changed = True
                        continue
                    if resource not in documents:
                        try:
                            documents[resource] = read_json(json_path)
                        except DependencyStagingError as exc:
                            outcomes[resource] = (json_path, str(exc), cache_hit)
                            state_graph[state_key][resource] = ()
                            if demand is not None:
                                effective_selections[state_key][resource] = demand
                            changed = True
                            continue
                    scan = _appearance_filtered_dependencies(
                        documents[resource], classification.extension, demand
                    )
                    state_graph[state_key][resource] = scan.dependencies
                    if demand is None:
                        effective_selections[state_key].pop(resource, None)
                        unmatched_selections[state_key].pop(resource, None)
                    else:
                        effective_selections[state_key][resource] = (
                            scan.effective_selections
                        )
                        if scan.unmatched_selections:
                            unmatched_selections[state_key][resource] = (
                                scan.unmatched_selections
                            )
                        else:
                            unmatched_selections[state_key].pop(resource, None)

                    unfiltered = set(scan.unfiltered_dependencies)
                    for dependency in scan.dependencies:
                        if dependency not in known:
                            known.add(dependency)
                            changed = True
                        incoming = (
                            None
                            if dependency in unfiltered
                            else scan.propagated_selections.get(dependency)
                        )
                        if (
                            incoming is None
                            and classify_resource(dependency).extension == ".ent"
                            and dependency not in normalized_roots[state_key]
                        ):
                            # Nested entity templates have no sector-level
                            # appearance selector of their own. Resolve their
                            # authored default instead of exploding every
                            # nested appearance into the tile closure.
                            incoming = ("default",)
                        if merge_demand(demands, dependency, incoming):
                            changed = True
                    changed = True
            if not changed:
                break

        union_graph: dict[str, set[str]] = {}
        for graph in state_graph.values():
            for resource, dependencies in graph.items():
                union_graph.setdefault(resource, set()).update(dependencies)
        global_known = {
            resource for resources in state_known.values() for resource in resources
        }
        for resource in global_known:
            union_graph.setdefault(resource, set())

        records: list[DependencyResource] = []
        for resource in sorted(global_known):
            classification = classify_resource(resource)
            dependencies = tuple(sorted(union_graph[resource]))
            if not classification.serializable:
                records.append(
                    DependencyResource(
                        resource=resource,
                        extension=classification.extension,
                        kind=classification.kind,
                        serializable=False,
                        status="leaf",
                        dependencies=dependencies,
                    )
                )
                continue
            json_path, error, cache_hit = outcomes[resource]
            records.append(
                DependencyResource(
                    resource=resource,
                    extension=classification.extension,
                    kind=classification.kind,
                    serializable=True,
                    status="failed" if error else "ready",
                    dependencies=dependencies,
                    cache_fingerprint=self._resource_fingerprint(resource),
                    json_path=json_path,
                    cache_hit=cache_hit,
                    error=error,
                )
            )

        closure = DependencyClosure(
            roots=tuple(
                sorted(
                    {
                        resource
                        for resources in normalized_roots.values()
                        for resource in resources
                    }
                )
            ),
            resources=tuple(records),
            batches=tuple(batches),
            identity_fingerprint=self.identity_fingerprint,
        )
        return StateDependencyClosure(
            closure=closure,
            state_resources={
                state_key: tuple(sorted(resources))
                for state_key, resources in state_known.items()
            },
            appearance_selections={
                state_key: {
                    resource: names
                    for resource, names in sorted(
                        effective_selections[state_key].items()
                    )
                }
                for state_key in sorted(effective_selections)
            },
            unmatched_appearance_selections={
                state_key: {
                    resource: names
                    for resource, names in sorted(
                        unmatched_selections[state_key].items()
                    )
                }
                for state_key in sorted(unmatched_selections)
            },
        )

    def resolve_states(
        self,
        state_roots: Mapping[str, Iterable[str]],
        *,
        state_appearance_selections: Mapping[str, Mapping[str, Iterable[str]]]
        | None = None,
    ) -> StateDependencyClosure:
        normalized_roots = {
            state_key: tuple(
                sorted({normalize_depot_path(resource) for resource in resources})
            )
            for state_key, resources in sorted(state_roots.items())
        }
        if any(not state_key for state_key in normalized_roots):
            raise DependencyStagingError("State keys must not be empty")
        if state_appearance_selections is not None:
            unknown_states = sorted(
                set(state_appearance_selections) - normalized_roots.keys()
            )
            if unknown_states:
                raise DependencyStagingError(
                    "Appearance selections reference unknown states: "
                    + ", ".join(unknown_states)
                )
            normalized_selections: dict[str, dict[str, tuple[str, ...]]] = {}
            for state_key, selections in sorted(state_appearance_selections.items()):
                normalized_selections[state_key] = {}
                roots = set(normalized_roots[state_key])
                for resource, names in sorted(selections.items()):
                    normalized_resource = normalize_depot_path(resource)
                    if normalized_resource not in roots:
                        raise DependencyStagingError(
                            "Appearance selection resource is not a root for "
                            f"{state_key}: {normalized_resource}"
                        )
                    normalized_selections[state_key][normalized_resource] = (
                        _ordered_names((names,) if isinstance(names, str) else names)
                    )
            return self._resolve_selected_states(
                normalized_roots, normalized_selections
            )
        closure = self.resolve(
            resource
            for resources in normalized_roots.values()
            for resource in resources
        )
        return StateDependencyClosure(
            closure=closure,
            state_resources=compute_state_closures(closure.graph, normalized_roots),
        )


def resolve_archive_dependencies(
    roots: Iterable[str],
    **resolver_options: Any,
) -> DependencyClosure:
    return ArchiveDependencyResolver(**resolver_options).resolve(roots)


def resolve_state_dependencies(
    state_roots: Mapping[str, Iterable[str]],
    *,
    state_appearance_selections: Mapping[str, Mapping[str, Iterable[str]]]
    | None = None,
    **resolver_options: Any,
) -> StateDependencyClosure:
    return ArchiveDependencyResolver(**resolver_options).resolve_states(
        state_roots,
        state_appearance_selections=state_appearance_selections,
    )


__all__ = [
    "ArchiveDependencyResolver",
    "BLENDER_WOLVENKIT_COMPAT_VERSION",
    "BatchInvocation",
    "BatchJob",
    "BatchRunResult",
    "BatchSummary",
    "DependencyClosure",
    "DependencyResource",
    "DependencyStagingError",
    "InstalledDependency",
    "PIPELINE_VERSION",
    "ResourceClassification",
    "SERIALIZABLE_EXTENSIONS",
    "StateDependencyClosure",
    "classify_resource",
    "compute_state_closures",
    "complete_blender_dependency_defaults",
    "extract_depot_paths",
    "install_dependency_jsons",
    "normalize_depot_path",
    "resource_type",
    "resolve_archive_dependencies",
    "resolve_state_dependencies",
]
