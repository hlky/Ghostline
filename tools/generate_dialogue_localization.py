#!/usr/bin/env python3
"""Compatibility CLI for the canonical Rust dialogue-localization writer."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from ghostline_red import deserialize as deserialize_cr2w
from toolchain import resolve_tool

ROOT = Path(__file__).resolve().parents[1]


def voice_command() -> list[str]:
    """Use a current native build, or compile the model-free CLI with Cargo."""
    binary = resolve_tool("ghostline_voice", required=False)
    crate = ROOT / "tools/ghostline-voice"
    inputs = [crate / "Cargo.toml", crate / "Cargo.lock", *crate.glob("src/*.rs")]
    default_binary = crate / "target/release/ghostline-voice.exe"
    if binary.is_file() and (
        binary.resolve() != default_binary.resolve()
        or binary.stat().st_mtime_ns >= max(p.stat().st_mtime_ns for p in inputs)
    ):
        return [str(binary)]
    return [
        "cargo",
        "run",
        "--quiet",
        "--locked",
        "--no-default-features",
        "--manifest-path",
        str(crate / "Cargo.toml"),
        "--",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--quest", required=True)
    parser.add_argument("--dialogue", required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    completed = subprocess.run(
        [
            *voice_command(),
            "localize-manifest",
            "--manifest",
            str(args.manifest.resolve()),
            "--repo-root",
            str(args.repo_root.resolve()),
            "--quest",
            args.quest,
            "--dialogue",
            args.dialogue,
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    outputs = json.loads(completed.stdout)
    if args.deserialize:
        from project_layout import resource_project
        for key in ("subtitles", "voiceover_map", "subtitle_map"):
            raw = Path(outputs[key])
            project = resource_project(f"mod/{args.quest}/", root=args.repo_root)
            relative = raw.relative_to(project / "source/raw")
            binary = project / "source/archive" / relative
            deserialize_cr2w(raw, binary.with_suffix(""))
    print(json.dumps(outputs, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
