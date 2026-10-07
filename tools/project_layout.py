"""Resolve repository tooling separately from independently owned mod projects.

Depot names are game identities and never include the workspace project path.
The catalog routes existing resources; a project's declared dependencies are
the only additional source trees available to its package builder.
"""
from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def catalog(root: Path = REPO_ROOT) -> dict:
    path = root / "projects/catalog.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def project_root(value: str | Path, *, root: Path = REPO_ROOT) -> Path:
    entries = catalog(root).get("projects", {})
    path = root / entries[str(value)] if str(value) in entries else Path(value)
    if not path.is_absolute():
        path = root / path
    if path.suffix == ".cpmodproj":
        path = path.parent
    path = path.resolve()
    if not (path / "project.json").is_file():
        raise ValueError(f"No project.json at {path}")
    return path


def project_config(path: Path) -> dict:
    data = json.loads((path / "project.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError(f"Unsupported project configuration: {path}")
    return data


def resource_project(depot: str, *, root: Path = REPO_ROOT) -> Path:
    """Find the owner of an existing depot namespace, or the default project.

    A root without a catalog is itself a standalone project. This also supports
    temporary projects and library callers without assuming a monorepo layout.
    """
    data = catalog(root)
    if not data:
        return root.resolve()
    normalized = depot.replace("\\", "/").casefold()
    candidates = []
    for relative in [*data["projects"].values(), *data.get("template_roots", [])]:
        path = root / relative
        for prefix in project_config(path).get("depot_prefixes", []):
            if normalized.startswith(prefix.casefold()):
                candidates.append((len(prefix), path))
    if candidates:
        length = max(item[0] for item in candidates)
        owners = {item[1] for item in candidates if item[0] == length}
        if len(owners) != 1:
            raise ValueError(f"Multiple project owners for {depot}: {owners}")
        return owners.pop().resolve()
    return project_root(data["default_project"], root=root)


def source_path(depot: str, kind: str, *, root: Path = REPO_ROOT) -> Path:
    if kind not in {"raw", "archive"}:
        raise ValueError(f"Unknown resource source kind: {kind}")
    relative = Path(depot.replace("\\", "/"))
    if relative.is_absolute() or any(part in {".", ".."} for part in relative.parts) or ":" in str(relative):
        raise ValueError(f"Unsafe depot path: {depot}")
    return resource_project(depot, root=root) / "source" / kind / (str(relative) + (".json" if kind == "raw" else ""))


def project_sources(path: Path) -> list[Path]:
    """Return the declared dependency closure; reject cycles and missing projects."""
    ordered: list[Path] = []
    visiting: set[Path] = set()

    def visit(candidate: Path) -> None:
        candidate = candidate.resolve()
        if candidate in visiting:
            raise ValueError(f"Project dependency cycle at {candidate}")
        if candidate in ordered:
            return
        visiting.add(candidate)
        data = project_config(candidate)
        for dependency in data.get("dependencies", []):
            visit(candidate / dependency)
        visiting.remove(candidate)
        ordered.append(candidate)

    visit(path)
    return ordered


def owning_project(path: Path, *, fallback: Path = REPO_ROOT) -> Path:
    """Locate a project from an authoring file or a not-yet-created resource."""
    path = path.resolve()
    for parent in (path, *path.parents):
        if (parent / "project.json").is_file():
            return parent
    return fallback.resolve()
