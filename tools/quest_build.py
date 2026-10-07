"""Shared quest build publication, isolated previews, and staged CR2W conversion."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path
import subprocess
import tempfile
from typing import Mapping

from artifact_io import publish_json_artifacts
from ghostline_red import deserialize as native_deserialize
from quest_compiler import (
    QuestArtifact, artifact_documents, compile_manifest_artifacts, resource_paths,
)
from toolchain import resolve_tool
from project_layout import catalog, owning_project, resource_project, project_root as resolve_project

ROOT = Path(__file__).resolve().parents[1]


def _destination_root(output_root: Path | None, project: Path | None = None) -> Path:
    project = (project or ROOT).resolve()
    root = (output_root or project).resolve()
    sources = [project / "source", ROOT.resolve() / "source"]
    sources.extend(ROOT / path / "source" for path in catalog(ROOT).get("projects", {}).values())
    sources.extend(ROOT / path / "source" for path in catalog(ROOT).get("template_roots", []))
    if output_root is not None and any(root.is_relative_to(source.resolve()) for source in sources):
        raise ValueError("Build output root must be outside the project's source tree")
    return root


def _within(path: Path, root: Path, label: str) -> Path:
    resolved = path.resolve()
    if resolved == root or not resolved.is_relative_to(root):
        raise ValueError(f"{label} destination must stay within {root}: {path}")
    return resolved


def _relocate(path: Path, source: Path, output: Path) -> Path:
    path = path.resolve()
    if path.is_relative_to(output):
        return path
    _within(path, source, "Source artifact")
    return _within(output / path.relative_to(source), output, "Relocated artifact")


def relocate_artifacts(
    artifacts: list[QuestArtifact], output_root: Path | None = None,
) -> list[QuestArtifact]:
    """Retain depot paths while moving raw/binary destinations into a preview root."""
    if output_root is None:
        return artifacts
    output_root = _destination_root(output_root)
    result = []
    for artifact in artifacts:
        project = owning_project(artifact.raw_path, fallback=ROOT)
        raw = _relocate(artifact.raw_path, project / "source/raw", output_root / "source/raw")
        archive = _relocate(artifact.archive_path, project / "source/archive", output_root / "source/archive")
        document = copy.deepcopy(artifact.document)
        document["Header"]["ArchiveFileName"] = str(archive)
        result.append(QuestArtifact(raw, archive, document, artifact.stage_id))
    return result


def _source_archive(path: Path, output_root: Path | None, project: Path) -> Path:
    path = path.resolve()
    if output_root is not None:
        scratch = output_root.resolve() / "source/archive"
        if path.is_relative_to(scratch):
            return project / "source/archive" / path.relative_to(scratch)
    return path


def _convert(
    raw: Path, candidate: Path, template: Path | None, *,
    serializer: str, wolvenkit: Path | None,
    red_cli: Path | None = None, schema_path: Path | None = None,
) -> None:
    """Require typed read-back parity; native layout loss triggers a fresh writer."""
    import json
    from cr2w_validation import compare_documents
    from ghostline_red import DEFAULT_RED_CLI, DEFAULT_RED_SCHEMA, ensure_schema

    expected = json.loads(raw.read_text(encoding="utf-8"))
    schema_file = (
        ensure_schema(red_cli or DEFAULT_RED_CLI, schema_path or DEFAULT_RED_SCHEMA)
        if red_cli is not None or schema_path is not None else ensure_schema()
    )
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    executable = wolvenkit or resolve_tool("wolvenkit")
    if template is not None and candidate.resolve() == template.resolve():
        raise ValueError("CR2W conversion candidate must be separate from its template")
    candidate.unlink(missing_ok=True)

    def read_back(label: str):
        output = candidate.parent / f"verify-{label}"
        output.mkdir(parents=True, exist_ok=True)
        serialized = output / f"{candidate.name}.json"
        serialized.unlink(missing_ok=True)
        subprocess.run(
            [str(executable), "cr2w", "-s", str(candidate), "-o", str(output)],
            check=True,
        )
        if not serialized.is_file():
            raise RuntimeError(f"Missing WolvenKit read-back: {candidate}")
        return json.loads(serialized.read_text(encoding="utf-8"))

    if serializer == "native" and template is not None and template.is_file():
        try:
            native_options = {}
            if red_cli is not None:
                native_options["red_cli"] = red_cli
            if schema_path is not None:
                native_options["schema"] = schema_path
            native_deserialize(raw, candidate, template=template, **native_options)
            if candidate.is_file() and candidate.read_bytes()[:4] == b"CR2W":
                decoded = read_back("native")
                if compare_documents(expected, decoded, schema=schema).ok:
                    return
        except (subprocess.CalledProcessError, FileNotFoundError, RuntimeError, ValueError, KeyError):
            # Unsupported native layouts and failed semantic reads need the
            # reflected writer. Neither candidate has reached source yet.
            pass
        candidate.unlink(missing_ok=True)

    subprocess.run(
        [str(executable), "cr2w", "-d", str(raw), "-o", str(candidate.parent)],
        check=True,
    )
    if not candidate.is_file() or candidate.read_bytes()[:4] != b"CR2W":
        raise RuntimeError(f"Missing or invalid WolvenKit CR2W output: {candidate}")
    decoded = read_back("wolvenkit")
    comparison = compare_documents(
        expected, decoded, schema=schema, fresh_wolvenkit_defaults=decoded,
    )
    if not comparison.ok:
        details = "; ".join(item["path"] for item in comparison.errors[:8])
        raise RuntimeError(f"CR2W semantic verification failed for {candidate}: {details}")


convert_resource = _convert


def publish_build(
    artifacts: list[QuestArtifact], *, namespace: str,
    output_root: Path | None = None, deserialize: bool = False,
    binary_templates: Mapping[Path, Path] | None = None,
    serializer: str = "native", wolvenkit: Path | None = None,
    binary_assets: Mapping[Path, Path] | None = None,
    project_root: Path | None = None,
) -> list[tuple[Path, Path]]:
    """Convert everything first, then publish raw/binary assets with rollback.

    binary_assets maps archive destinations to already built source binaries.
    It is used for quest-owned animation/rig prerequisites, never game installs.
    """
    if serializer not in {"native", "wolvenkit"}:
        raise ValueError(f"Unknown CR2W serializer: {serializer}")
    if not namespace or any(char not in "abcdefghijklmnopqrstuvwxyz0123456789_" for char in namespace):
        raise ValueError("Build namespace must be a lowercase identifier")
    artifacts = relocate_artifacts(artifacts, output_root)
    documents = artifact_documents(artifacts)
    archives = [artifact.archive_path.resolve() for artifact in artifacts]
    if len(set(archives)) != len(archives):
        raise ValueError("Quest build contains duplicate archive destinations")
    project = (project_root or resource_project(f"mod/{namespace}/", root=ROOT)).resolve()
    destination_root = _destination_root(output_root, project)
    raw_root, archive_root = destination_root / "source/raw", destination_root / "source/archive"
    for artifact in artifacts:
        _within(artifact.raw_path, raw_root, "Raw artifact")
        _within(artifact.archive_path, archive_root, "Archive artifact")
    ownership_path = _within(
        destination_root / "generated/quest-builds" / namespace / "outputs.json",
        destination_root / "generated/quest-builds", "Ownership record",
    )
    staging_root = _within(
        project / "generated/quest-builds" / namespace,
        project / "generated/quest-builds", "Conversion staging",
    )
    binary_output: dict[Path, bytes] = {}
    templates = {path.resolve(): donor for path, donor in (binary_templates or {}).items()}
    if deserialize:
        for archive, source in (binary_assets or {}).items():
            destination = archive.resolve()
            if output_root is not None:
                destination = _relocate(destination, project / "source/archive", archive_root)
            if destination in binary_output or destination in archives:
                raise ValueError(f"Duplicate binary asset destination: {destination}")
            content = source.read_bytes()
            if content[:4] != b"CR2W":
                raise ValueError(f"Binary prerequisite is not a CR2W resource: {source}")
            _within(destination, archive_root, "Binary asset")
            binary_output[destination] = content
        staging_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="conversion-", dir=staging_root) as directory:
            for index, artifact in enumerate(artifacts):
                target = artifact.archive_path.resolve()
                work = Path(directory) / str(index)
                raw = work / f"{target.name}.json"
                candidate = work / target.name
                # The staged input cannot replace authored raw files on failure.
                publish_json_artifacts({raw: artifact.document})
                original = _source_archive(target, output_root, project)
                template = templates.get(original, original if original.is_file() else None)
                _convert(raw, candidate, template, serializer=serializer, wolvenkit=wolvenkit)
                binary_output[target] = candidate.read_bytes()
    report = publish_json_artifacts(
        documents,
        ownership_path=ownership_path,
        binary_artifacts=binary_output,
    )
    if report.obsolete_paths:
        print("Retired generated outputs retained: " + ", ".join(map(str, report.obsolete_paths)))
    return [(artifact.raw_path, artifact.archive_path) for artifact in artifacts]


def main(manifest: Path, root_resource: str, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build quest phases, journal, and localization from one manifest.")
    parser.add_argument("--out-root", type=Path)
    parser.add_argument("--project", help="Target project ID or directory; defaults to the manifest's owner")
    parser.add_argument("--allow-planned", action="store_true", help="Build a planned prototype into --out-root only")
    parser.add_argument("--deserialize", action="store_true")
    parser.add_argument("--serializer", choices=("native", "wolvenkit"), default="native")
    parser.add_argument("--wolvenkit", type=Path)
    args = parser.parse_args(argv)
    project = resolve_project(args.project) if args.project else owning_project(
        manifest, fallback=resource_project(root_resource, root=ROOT),
    )
    if args.out_root is not None:
        try:
            _destination_root(args.out_root, project)
        except ValueError as exc:
            parser.error(str(exc))
    if args.allow_planned and (
        args.out_root is None or args.out_root.resolve() in {ROOT, project}
        or args.out_root.resolve().is_relative_to(ROOT / "source")
        or ROOT.is_relative_to(args.out_root.resolve())
    ):
        parser.error("--allow-planned requires an isolated --out-root outside source")
    raw, archive = resource_paths(root_resource, project_root=project)
    artifacts = compile_manifest_artifacts(manifest, raw, archive, allow_planned=args.allow_planned, project_root=project)
    namespace = root_resource.replace("\\", "/").split("/")[1]
    outputs = publish_build(
        artifacts, namespace=namespace, output_root=args.out_root,
        deserialize=args.deserialize, serializer=args.serializer, wolvenkit=args.wolvenkit,
        project_root=project,
    )
    for raw, _ in outputs:
        print(raw)
    return 0
