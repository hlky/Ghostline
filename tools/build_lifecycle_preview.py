#!/usr/bin/env python3
"""Build an isolated, explicitly non-shipping owned-block library preview."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from artifact_io import atomic_write_json, publish_json_artifacts
from quest_build import publish_build
from quest_compiler import (
    audit_resources,
    compile_artifacts,
    load_spec,
    artifact_documents,
)

ROOT = Path(__file__).resolve().parents[1]


def convert_batch(artifacts, output):
    """Fresh scratch graphs share two CLI startups; verify every typed result."""
    from cr2w_validation import compare_documents
    from ghostline_red import ensure_schema
    from toolchain import resolve_tool

    schema = json.loads(ensure_schema().read_text(encoding="utf-8"))
    staging = output / "generated/conversion"
    staging.mkdir(parents=True, exist_ok=True)
    binaries = {}
    with tempfile.TemporaryDirectory(dir=staging) as directory:
        scratch = Path(directory)
        raw, packed, readback = [
            scratch / name for name in ("raw", "packed", "readback")
        ]
        for folder in (raw, packed, readback):
            folder.mkdir()
        names = []
        for index, artifact in enumerate(artifacts):
            name = f"{index:03d}-{artifact.archive_path.name}"
            names.append(name)
            atomic_write_json(raw / (name + ".json"), artifact.document)
        cli = str(resolve_tool("wolvenkit"))
        subprocess.run([cli, "cr2w", "-d", str(raw), "-o", str(packed)], check=True)
        subprocess.run(
            [cli, "cr2w", "-s", str(packed), "-o", str(readback)], check=True
        )
        for name, artifact in zip(names, artifacts, strict=True):
            binary = packed / name
            serialized = readback / (name + ".json")
            if (
                not binary.is_file()
                or binary.read_bytes()[:4] != b"CR2W"
                or not serialized.is_file()
            ):
                raise RuntimeError(
                    f"Missing CR2W binary/readback for {artifact.stage_id or '$root'}"
                )
            decoded = json.loads(serialized.read_text(encoding="utf-8"))
            comparison = compare_documents(
                artifact.document,
                decoded,
                schema=schema,
                fresh_wolvenkit_defaults=decoded,
            )
            if not comparison.ok:
                raise RuntimeError(
                    f"Typed readback failed for {artifact.stage_id or '$root'}: "
                    + json.dumps(comparison.errors[:8])
                )
            binaries[artifact.archive_path] = binary.read_bytes()
    return binaries


def build(spec_path, output, *, deserialize=False):
    from quest_catalog import compiler_source_files

    sources = compiler_source_files(ROOT) | {
        Path(__file__).resolve(),
        spec_path.resolve(),
    }
    input_hashes = {
        path: hashlib.sha256(path.read_bytes()).hexdigest() for path in sources
    }
    output = output.resolve()
    if not output.is_relative_to(ROOT / "generated") or output == ROOT / "generated":
        raise ValueError(
            "Lifecycle previews require a dedicated directory below repository generated/"
        )
    spec, diagnostics = load_spec(spec_path)
    if spec is None:
        raise ValueError(
            "Invalid lifecycle preview manifest: "
            + "; ".join(d.message for d in diagnostics)
        )
    diagnostics.extend(audit_resources(spec))
    if any(d.level == "error" for d in diagnostics):
        raise ValueError(
            "Lifecycle preview audit failed: "
            + "; ".join(d.message for d in diagnostics if d.level == "error")
        )
    relative = Path("mod", spec.id, "phases", "root.questphase")
    artifacts = compile_artifacts(
        spec,
        output / "source/raw" / Path(str(relative) + ".json"),
        output / "source/archive" / relative,
        project_root=output,
    )
    if deserialize:
        binaries = convert_batch(artifacts, output)
        if any(
            hashlib.sha256(path.read_bytes()).hexdigest() != digest
            for path, digest in input_hashes.items()
        ):
            raise RuntimeError(
                "Preview inputs changed during conversion; no outputs published"
            )
        publish_json_artifacts(
            artifact_documents(artifacts),
            binary_artifacts=binaries,
            ownership_path=output / "generated/quest-builds" / spec.id / "outputs.json",
        )
    else:
        publish_build(artifacts, namespace=spec.id, project_root=output)
    report = {
        "schema_version": 1,
        "manifest": str(spec_path.resolve()),
        "manifest_sha256": input_hashes[spec_path.resolve()],
        "source_sha256": {
            str(path.relative_to(ROOT)): digest
            for path, digest in sorted(input_hashes.items())
            if path != spec_path.resolve()
        },
        "artifact_count": len(artifacts),
        "typed_readback": deserialize,
        "resource_diagnostics": [d.as_dict() for d in diagnostics],
        "outputs": {
            str(path.relative_to(output)): hashlib.sha256(path.read_bytes()).hexdigest()
            for artifact in artifacts
            for path in (artifact.raw_path, artifact.archive_path)
            if path.is_file()
        },
        "status": "Authoring/serialization preview; placeholder bindings; not packaged, installed or game-tested.",
    }
    atomic_write_json(output / "preview-report.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--spec",
        type=Path,
        default=ROOT / "quests/examples/owned-lifecycle-blocks.quest.json",
    )
    parser.add_argument(
        "--out-root", type=Path, default=ROOT / "generated/lifecycle-blocks-preview"
    )
    parser.add_argument(
        "--deserialize",
        action="store_true",
        help="Require CR2W conversion and typed WolvenKit readback",
    )
    args = parser.parse_args()
    report = build(args.spec, args.out_root, deserialize=args.deserialize)
    print(
        json.dumps(
            {
                "artifacts": report["artifact_count"],
                "typed_readback": report["typed_readback"],
                "report": str((args.out_root / "preview-report.json").resolve()),
                "status": report["status"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
