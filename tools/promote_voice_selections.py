#!/usr/bin/env python3
"""Validate an audition CSV and promote one selected WAV per spoken line."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import wave
from pathlib import Path
from typing import Any


TRUTHY = {"1", "true", "yes", "y", "x", "selected"}
REFERENCE_KEY = "__voice_design_reference__"


def is_selected(value: str) -> bool:
    return value.strip().lower() in TRUTHY


def duration_ms(path: Path) -> int:
    with wave.open(str(path), "rb") as audio:
        return round(audio.getnframes() * 1000 / audio.getframerate())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return str(resolved)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        sample = stream.read(8192)
        stream.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
        return list(csv.DictReader(stream, dialect=dialect))


def validate(
    manifest: dict[str, Any], rows: list[dict[str, str]]
) -> tuple[str, dict[str, dict[str, str]]]:
    selected = [row for row in rows if is_selected(row.get("selected", ""))]
    references = [row for row in selected if row.get("line_key") == REFERENCE_KEY]
    if len(references) > 1:
        raise ValueError(f"Select at most one Cinder design reference; found {len(references)}")
    if references:
        design = references[0]["design"]
    else:
        cinder_designs = {
            row.get("design", "")
            for row in selected
            if row.get("speaker", "").casefold() == "cinder"
            and row.get("line_key") != REFERENCE_KEY
        }
        if len(cinder_designs) != 1:
            raise ValueError(
                "Select one Cinder design reference, or choose all Cinder lines "
                f"from exactly one design; found {len(cinder_designs)} designs"
            )
        design = cinder_designs.pop()

    by_key: dict[str, list[dict[str, str]]] = {}
    for row in selected:
        key = row.get("line_key", "")
        if key != REFERENCE_KEY:
            by_key.setdefault(key, []).append(row)

    spoken = {line["key"]: line for line in manifest["spoken_lines"]}
    unknown = sorted(set(by_key) - set(spoken))
    if unknown:
        raise ValueError(f"Selected unknown spoken line(s): {', '.join(unknown)}")

    choices: dict[str, dict[str, str]] = {}
    for key, line in spoken.items():
        matches = by_key.get(key, [])
        if len(matches) != 1:
            raise ValueError(f"Select exactly one take for {key}; found {len(matches)}")
        row = matches[0]
        if row.get("speaker", "").casefold() != str(line["speaker"]).casefold():
            raise ValueError(f"Speaker mismatch for {key}")
        if str(line["speaker"]).casefold() == "cinder" and row.get("design") != design:
            raise ValueError(f"{key} uses {row.get('design')}, not selected design {design}")
        source = Path(row["file"])
        if not source.is_file() or source.stat().st_size == 0:
            raise ValueError(f"Missing or empty selected WAV for {key}: {source}")
        choices[key] = row
    return design, choices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--update-manifest", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    design, choices = validate(manifest, read_rows(args.csv))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    receipt: dict[str, Any] = {"voice_design": design, "lines": []}
    for line in manifest["spoken_lines"]:
        key = line["key"]
        row = choices[key]
        source = Path(row["file"])
        audio_name = Path(line["audio_path"]).with_suffix(".wav").name
        target = args.output_dir / audio_name
        shutil.copy2(source, target)
        measured_ms = duration_ms(target)
        if args.update_manifest:
            line["duration_ms"] = measured_ms
        receipt["lines"].append(
            {
                "key": key,
                "speaker": line["speaker"],
                "design": row["design"],
                "take": row["take"],
                "source": portable_path(source),
                "output": portable_path(target),
                "duration_ms": measured_ms,
                "sha256": sha256(target),
            }
        )

    if args.update_manifest:
        args.manifest.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    receipt_path = args.receipt or args.output_dir / "selection-receipt.json"
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Promoted {len(receipt['lines'])} lines using {design} to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
