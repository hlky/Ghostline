#!/usr/bin/env python3
"""Build a review CSV for a Qwen voice-audition directory."""

from __future__ import annotations

import argparse
import csv
import json
import wave
from pathlib import Path


REFERENCE_TEXT = (
    "A clean shutdown is a luxury. First we trace every dependency, then we "
    "decide what can break without taking somebody with it."
)


def duration_seconds(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        return audio.getnframes() / audio.getframerate()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--auditions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    text_by_key = {
        line["key"]: (line["speaker"], line["text"])
        for line in manifest["spoken_lines"]
    }
    rows: list[dict[str, str]] = []

    for design_dir in sorted(args.auditions.iterdir()):
        if not design_dir.is_dir():
            continue
        design = design_dir.name
        reference = design_dir / "reference.wav"
        if reference.is_file():
            rows.append(
                {
                    "selected": "",
                    "speaker": "Cinder",
                    "design": design,
                    "line_key": "__voice_design_reference__",
                    "take": "reference",
                    "text": REFERENCE_TEXT,
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
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"{args.output}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
