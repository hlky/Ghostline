#!/usr/bin/env python3
"""Generate the quest block catalog and record hash-bound structural build evidence."""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from types import SimpleNamespace
from typing import Any

from artifact_io import atomic_write_json
from quest_stages import SCHEMA, STAGE_REGISTRY

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "projects/test-quests/evidence/quest-blocks.json"
HASH = re.compile(r"^[a-f0-9]{64}$")


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def compiler_source_files(root: Path) -> set[Path]:
    """Conservatively bind local imports, including imports inside builder functions."""
    directory = root / "tools"
    pending = [directory / "quest_compiler.py"]
    sources: set[Path] = set()
    while pending:
        path = pending.pop()
        if path in sources:
            continue
        sources.add(path)
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8-sig"))):
            if isinstance(node, ast.Import):
                modules = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module]
            else:
                continue
            for module in modules:
                dependency = directory / (module.split(".")[0] + ".py")
                if dependency.is_file() and dependency not in sources:
                    pending.append(dependency)
    return sources


def bound_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("Evidence paths must be repository-relative POSIX paths")
    relative = PurePosixPath(value)
    if (
        relative.is_absolute()
        or ":" in value
        or any(part in {"", ".", ".."} for part in value.split("/"))
    ):
        raise ValueError(f"Unsafe evidence path: {value}")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Evidence path escapes repository: {value}")
    return path


def assess_evidence(entry: Any, *, root: Path = ROOT) -> dict:
    """Check bindings; this does not independently authenticate a recorded game run."""
    result = (
        {**entry, "binding_status": "invalid", "binding_errors": []}
        if isinstance(entry, dict)
        else {"binding_status": "invalid", "binding_errors": []}
    )
    try:
        if (
            not isinstance(entry, dict)
            or not isinstance(entry.get("id"), str)
            or not entry["id"]
        ):
            raise ValueError("Evidence requires a nonempty id")
        if entry.get("level") not in {"build", "in_game"} or not isinstance(
            entry.get("passed"), bool
        ):
            raise ValueError("Evidence requires level build/in_game and boolean passed")
        stage_types = entry.get("stage_types")
        if (
            not isinstance(stage_types, list)
            or not stage_types
            or any(name not in STAGE_REGISTRY for name in stage_types)
        ):
            raise ValueError("Evidence must name registered stage types")
        if not isinstance(entry.get("summary"), str) or not entry["summary"].strip():
            raise ValueError("Evidence requires a summary")
        resources = entry.get("resources")
        if not isinstance(resources, dict) or not resources:
            raise ValueError("Evidence requires content-hash resource bindings")
        if entry["level"] == "build":
            outputs = entry.get("outputs")
            if (
                not isinstance(outputs, dict)
                or not outputs
                or any(
                    not isinstance(digest, str) or not HASH.fullmatch(digest)
                    for digest in outputs.values()
                )
            ):
                raise ValueError("Build evidence requires compiled output hashes")
        else:
            report = entry.get("run_report")
            if not isinstance(report, str) or report not in resources:
                raise ValueError("In-game evidence requires a hash-bound run_report")
            if (
                not isinstance(entry.get("observations"), list)
                or not entry["observations"]
                or any(
                    not isinstance(item, str) or not item.strip()
                    for item in entry["observations"]
                )
            ):
                raise ValueError("In-game evidence requires concrete observations")
            if not any(
                name.startswith("source/archive/") or "/source/archive/" in name or name.endswith(".archive")
                for name in resources
            ):
                raise ValueError(
                    "In-game evidence must bind tested packed resources or archive"
                )
        stale = []
        for name, digest in resources.items():
            path = bound_path(root, name)
            if not isinstance(digest, str) or not HASH.fullmatch(digest):
                raise ValueError(f"Invalid SHA-256 for {name}")
            if not path.is_file():
                stale.append(f"Missing bound resource: {name}")
            elif sha256(path) != digest:
                stale.append(f"Changed bound resource: {name}")
        result["binding_status"] = "stale" if stale else "current"
        result["binding_errors"] = stale
    except (ValueError, OSError, TypeError) as exc:
        result["binding_errors"] = [str(exc)]
    return result


def read_evidence(paths: list[Path], *, root: Path = ROOT) -> list[dict]:
    result = []
    identifiers: set[str] = set()
    for path in paths:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
        if (
            not isinstance(value, dict)
            or value.get("schema_version") != 1
            or not isinstance(value.get("entries"), list)
        ):
            raise ValueError(f"Invalid evidence document: {path}")
        for entry in value["entries"]:
            assessed = assess_evidence(entry, root=root)
            identifier = assessed.get("id")
            if isinstance(identifier, str):
                if identifier in identifiers:
                    raise ValueError(f"Duplicate evidence ID: {identifier}")
                identifiers.add(identifier)
            assessed["evidence_file"] = (
                str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
            )
            result.append(assessed)
    return result


def manifest_examples(root: Path) -> tuple[dict[str, list[dict]], list[dict]]:
    from quest_authoring import normalize_spec

    examples: dict[str, list[dict]] = {name: [] for name in STAGE_REGISTRY}
    errors = []
    paths = set((root / "quests").rglob("*.quest.json"))
    paths.update((root / "projects").rglob("*.quest.json"))
    paths.update((root / "projects/ghostline/quests").glob("**/implementation/quest.json"))
    for path in sorted(paths):
        try:
            manifest = normalize_spec(json.loads(path.read_text(encoding="utf-8-sig")))
            for stage in manifest["stages"]:
                if stage.get("type") in examples:
                    examples[stage["type"]].append(
                        {
                            "manifest": path.relative_to(root).as_posix(),
                            "id": stage.get("id"),
                            "status": stage.get("status", "ready"),
                            "data": stage,
                        }
                    )
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(
                {"manifest": path.relative_to(root).as_posix(), "error": str(exc)}
            )
    return examples, errors


def build_catalog(
    *, root: Path = ROOT, evidence_paths: list[Path] | None = None
) -> dict:
    from quest_flow import stage_inputs, stage_outcomes

    evidence = read_evidence(
        evidence_paths
        if evidence_paths is not None
        else [root / DEFAULT_EVIDENCE.relative_to(ROOT)],
        root=root,
    )
    examples, errors = manifest_examples(root)
    common = SCHEMA["$defs"]["baseStage"]
    blocks = []
    for name, definition in STAGE_REGISTRY.items():
        relevant = [
            entry
            for entry in evidence
            if isinstance(entry.get("stage_types"), list)
            and name in entry["stage_types"]
        ]
        current = [entry for entry in relevant if entry["binding_status"] == "current"]
        properties = {**common["properties"], **definition.structure["properties"]}
        required = set(common.get("required", [])) | set(
            definition.structure.get("required", [])
        )
        template = definition.template({})
        stage = SimpleNamespace(data={})
        blocks.append(
            {
                "type": name,
                "implementation": {
                    "default_mode": definition.mode({}),
                    "builder": definition.builder({}),
                    "template": template,
                    "requires_explicit_template": definition.builder({}) is None
                    and template is None,
                },
                "fields": {
                    field: {
                        "required": field in required,
                        "schema": schema,
                        "supported_by_default_template": field
                        not in definition.implementation.unsupported_fields,
                    }
                    for field, schema in sorted(properties.items())
                },
                "inputs": stage_inputs(stage),
                "outcomes": stage_outcomes(stage),
                "limits": {
                    "unsupported_default_template_fields": sorted(
                        definition.implementation.unsupported_fields
                    ),
                    "scope": "Availability and structural build evidence do not prove engine behavior; explicit templates require socket/contract validation.",
                },
                "examples": examples[name],
                "evidence": relevant,
                "structural_build_recorded": any(
                    entry["level"] == "build" and entry["passed"] for entry in current
                ),
                "in_game_pass_recorded": any(
                    entry["level"] == "in_game" and entry["passed"] for entry in current
                ),
            }
        )
    return {
        "schema_version": 1,
        "scope": "Registry-derived capabilities; recorded evidence is valid only for its listed hashes and scope, never every configuration of a block.",
        "blocks": blocks,
        "example_errors": errors,
        "evidence_errors": [
            entry for entry in evidence if entry["binding_status"] != "current"
        ],
    }


def catalog_markdown(catalog: dict) -> str:
    lines = [
        "# Quest block catalog",
        "",
        catalog["scope"],
        "",
        "Use `docs/authoring/quest-composition.md` for authoring patterns. Fields and implementation limits below come from the compiler registry.",
        "",
    ]
    for block in catalog["blocks"]:
        implementation = block["implementation"]
        lines.extend(
            [
                f"## `{block['type']}`",
                "",
                f"Implementation: `{implementation['default_mode']}`. Structural build recorded: **{str(block['structural_build_recorded']).lower()}**. Current in-game pass recorded: **{str(block['in_game_pass_recorded']).lower()}**.",
                "",
                f"Inputs: `{json.dumps(block['inputs'], sort_keys=True)}`. Outcomes: `{json.dumps(block['outcomes'], sort_keys=True)}`.",
                "",
                "| Field | Required | Default-template support |",
                "| --- | --- | --- |",
            ]
        )
        for name, field in block["fields"].items():
            lines.append(
                f"| `{name}` | {'yes' if field['required'] else 'no'} | {'yes' if field['supported_by_default_template'] else 'unsupported'} |"
            )
        if implementation["requires_explicit_template"]:
            lines.extend(
                [
                    "",
                    "Requires an explicit phase template, or a configured conditional builder.",
                ]
            )
        if block["limits"]["unsupported_default_template_fields"]:
            lines.extend(
                [
                    "",
                    "Unsupported by default template: "
                    + ", ".join(
                        f"`{field}`"
                        for field in block["limits"][
                            "unsupported_default_template_fields"
                        ]
                    )
                    + ".",
                ]
            )
        lines.extend(["", "Examples:", ""])
        lines.extend(
            f"- `{example['manifest']}` → `{example['id']}` ({example['status']})."
            for example in block["examples"]
        )
        if not block["examples"]:
            lines.append("No checked-in example manifest found.")
        if block["evidence"]:
            lines.extend(["", "Evidence:", ""])
            for entry in block["evidence"]:
                lines.append(
                    f"- `{entry.get('id', '?')}`: {entry.get('level', '?')}, {entry['binding_status']}, passed={entry.get('passed', False)}. {entry.get('summary', '')}"
                )
                lines.extend(f"  - {error}" for error in entry["binding_errors"])
        lines.append("")
    if catalog["example_errors"]:
        lines.extend(
            [
                "## Unreadable examples",
                "",
                "```json",
                json.dumps(catalog["example_errors"], indent=2),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def record_build(manifest: Path, *, root: Path = ROOT) -> dict:
    """Compile raw graph artifacts in memory; never publish raw or packed resources."""
    from quest_compiler import (
        compile_artifacts,
        emits_stage_phase,
        load_spec,
        resource_paths,
        stage_template_resource,
    )

    manifest = manifest.resolve()
    if not manifest.is_relative_to(root.resolve()):
        raise ValueError("Build evidence requires a manifest inside the repository")
    spec, diagnostics = load_spec(manifest)
    errors = [item.message for item in diagnostics if item.level == "error"]
    if (
        spec is None
        or errors
        or any(stage.status == "planned" for stage in spec.stages)
    ):
        raise ValueError(
            "Structural build refused: "
            + "; ".join(errors or ["planned or invalid stages"])
        )
    scratch = root / "generated/quest-build-evidence" / spec.id
    artifacts = compile_artifacts(
        spec,
        scratch / "root.questphase.json",
        scratch / "root.questphase",
        child_root=scratch / "children",
    )
    resources = {
        manifest,
        root / "tools/quest-schema-v1.json",
        *compiler_source_files(root),
    }
    # quest_content loads the donor registry at import time, including when
    # compiling a manifest without composition documents.
    resources.add(root / "quests/templates/journal/catalog.json")
    for stage in spec.stages:
        template = stage_template_resource(stage)
        if template:
            raw, _ = resource_paths(template)
            resources.add(raw)
        elif not emits_stage_phase(stage) and set(stage.data) & {
            "inputs",
            "outcomes",
            "contract",
        }:
            raw, _ = resource_paths(stage.phase_resource)
            resources.add(raw)
    if spec.authoring_source is not None:
        from quest_content import journal_template_path
        from quest_journal import template_names

        configuration = spec.authoring_source.get("composition", {})
        for name in template_names(configuration):
            resources.add(journal_template_path(name))
    bindings = {
        path.relative_to(root).as_posix(): sha256(path) for path in sorted(resources)
    }
    entry = {
        "id": f"{spec.id}-structural-build",
        "level": "build",
        "passed": True,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "stage_types": sorted({stage.type for stage in spec.stages}),
        "summary": "Compiled raw phase graphs in memory and passed compiler graph/socket checks. No native serialization, resource/world audit, packaging, or game execution.",
        "resources": bindings,
        "outputs": {
            (
                "$root"
                if index == 0
                else artifact.raw_path.relative_to(root).as_posix()
            ): hashlib.sha256(
                json.dumps(
                    artifact.document, sort_keys=True, separators=(",", ":")
                ).encode()
            ).hexdigest()
            for index, artifact in enumerate(artifacts)
        },
    }
    return {"schema_version": 1, "entries": [entry]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    catalog = commands.add_parser("catalog")
    catalog.add_argument("--format", choices=["json", "markdown"], default="markdown")
    catalog.add_argument("--evidence", type=Path, action="append")
    catalog.add_argument("--output", type=Path)
    evidence = commands.add_parser("record-build")
    evidence.add_argument("--manifest", type=Path, required=True)
    evidence.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "record-build":
            result = record_build(args.manifest)
            atomic_write_json(args.output, result)
            print(
                json.dumps(
                    {
                        "receipt": str(args.output),
                        "scope": result["entries"][0]["summary"],
                    },
                    indent=2,
                )
            )
        else:
            result = build_catalog(evidence_paths=args.evidence)
            content = (
                json.dumps(result, indent=2) + "\n"
                if args.format == "json"
                else catalog_markdown(result)
            )
            if args.output:
                if args.format == "json":
                    atomic_write_json(args.output, result)
                else:
                    args.output.parent.mkdir(parents=True, exist_ok=True)
                    args.output.write_text(content, encoding="utf-8")
            else:
                print(content)
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
