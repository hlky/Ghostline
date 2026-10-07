#!/usr/bin/env python3
"""Build a review CSV for a Qwen voice-audition directory."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import wave
from pathlib import Path


def duration_seconds(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        return audio.getnframes() / audio.getframerate()


def report_rows(manifest: dict, report_path: Path) -> list[dict[str, str]]:
    """Build review rows from the renderer's versioned candidate inventory."""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("schema_version") != 1:
        raise ValueError("Unsupported render report schema")
    spoken = {line["key"]: line for line in manifest["spoken_lines"]}
    root = report_path.parent.resolve()
    rows = []
    identities = set()
    for candidate in report["candidates"]:
        key = candidate["line_key"]
        if key not in spoken:
            continue  # A production report can cover more than the selected dialogue.
        line = spoken[key]
        if candidate["speaker"] != line["speaker"]:
            raise ValueError(f"Speaker mismatch in render report: {key}")
        path = (root / candidate["wav"]).resolve()
        if not path.is_relative_to(root):
            raise ValueError(f"Candidate path escapes its output root: {path}")
        with path.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        if digest != candidate["sha256"]:
            raise ValueError(f"Candidate changed after rendering: {path}")
        identity = (key, candidate["version"], candidate.get("design", ""))
        if identity in identities:
            raise ValueError(f"Duplicate candidate identity: {identity}")
        identities.add(identity)
        rows.append(
            {
                "selected": "",
                "speaker": line["speaker"],
                "design": candidate.get("design") or f"legacy-{line['speaker']}",
                "line_key": key,
                "take": str(candidate["version"]),
                "text": line["text"],
                "duration_seconds": f"{duration_seconds(path):.3f}",
                "file": str(path),
                "sha256": digest,
            }
        )
    if not rows:
        raise ValueError("Render report contains no candidates for this manifest")
    return rows


def legacy_rows(
    manifest: dict,
    auditions: Path,
    reference_speaker: str | None = None,
    reference_text: str = "",
) -> list[dict[str, str]]:
    """Adapt historical design/line/take directories explicitly."""
    text_by_key = {
        line["key"]: (line["speaker"], line["text"])
        for line in manifest["spoken_lines"]
    }
    rows: list[dict[str, str]] = []

    for design_dir in sorted(auditions.iterdir()):
        if not design_dir.is_dir():
            continue
        design = design_dir.name
        reference = design_dir / "reference.wav"
        if reference.is_file():
            if not reference_speaker:
                raise ValueError(
                    "Historical reference.wav requires --reference-speaker"
                )
            rows.append(
                {
                    "selected": "",
                    "speaker": reference_speaker,
                    "design": design,
                    "line_key": "__voice_design_reference__",
                    "take": "reference",
                    "text": reference_text,
                    "duration_seconds": f"{duration_seconds(reference):.3f}",
                    "file": str(reference.resolve()),
                }
            )
        for line_dir in sorted(path for path in design_dir.iterdir() if path.is_dir()):
            if line_dir.name not in text_by_key:
                continue
            speaker, text = text_by_key[line_dir.name]
            for wav in sorted(line_dir.glob("take-*.wav")):
                rows.append(
                    {
                        "selected": "",
                        "speaker": speaker,
                        "design": design,
                        "line_key": line_dir.name,
                        "take": wav.stem.removeprefix("take-"),
                        "text": text,
                        "duration_seconds": f"{duration_seconds(wav):.3f}",
                        "file": str(wav.resolve()),
                    }
                )

    if not rows:
        raise ValueError("Historical audition directory contains no matching takes")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--report", type=Path)
    source.add_argument(
        "--auditions", type=Path, help="Directory containing render-report.json"
    )
    parser.add_argument(
        "--legacy-layout",
        action="store_true",
        help="Read historical design/line/take-*.wav directories",
    )
    parser.add_argument("--reference-speaker")
    parser.add_argument("--reference-text", default="")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    if args.legacy_layout:
        if args.auditions is None:
            parser.error("--legacy-layout requires --auditions")
        rows = legacy_rows(
            manifest, args.auditions, args.reference_speaker, args.reference_text
        )
    else:
        rows = report_rows(
            manifest, args.report or args.auditions / "render-report.json"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "selected",
                "speaker",
                "design",
                "line_key",
                "take",
                "text",
                "duration_seconds",
                "file",
                "sha256",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"{args.output}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
