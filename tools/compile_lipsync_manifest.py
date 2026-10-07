#!/usr/bin/env python3
"""Compile a spoken manifest using the shared audio-to-animation operation."""

from __future__ import annotations
import argparse
from pathlib import Path, PureWindowsPath
from build_lipsync_corpus import text_to_phones
from build_lipsync_dataset import CTCPhoneAligner, normalize_phones
from lipsync_compiler import (
    DEFAULT_MODEL,
    DEFAULT_PHONE_MODEL,
    AlignedLine,
    CompileSettings,
    add_compile_options,
    compile_aligned_line,
    read_json,
    write_json,
)
from lipsync_glb import read_glb, write_glb


def compile_manifest(args: argparse.Namespace) -> None:
    settings = CompileSettings.from_args(args)
    manifest = read_json(args.manifest)
    model = read_json(args.model)
    document, chunks = read_glb(args.donor_glb)
    # Preflight identities and all audio paths before loading the expensive model.
    inputs = []
    identities = set()
    for line in manifest["spoken_lines"]:
        locstring = int(line["string_id"])
        if locstring in identities or not 0 <= locstring <= 0xFFFFFFFFFFFFFFFF:
            raise ValueError(f"Duplicate or invalid locstring: {locstring}")
        identities.add(locstring)
        if Path(line["key"]).name != line["key"] or any(
            c in line["key"] for c in "\\/:"
        ):
            raise ValueError("Line keys must be safe filenames")
        name = (
            PureWindowsPath(line.get("audio_path", line["key"] + ".wem"))
            .with_suffix(".wav")
            .name
        )
        audio = args.audio_dir / name
        if not audio.is_file():
            raise FileNotFoundError(audio)
        inputs.append((line, audio, locstring))
    if not inputs:
        raise ValueError("Manifest has no spoken_lines")
    aligner = CTCPhoneAligner(args.phone_model, args.device)
    reports = []
    for line, audio, locstring in inputs:
        phones = (
            normalize_phones(line["phones"])
            if line.get("phones")
            else text_to_phones(line["text"])
        )
        alignment, duration, device = aligner.align(audio, phones)
        report = compile_aligned_line(
            document,
            chunks,
            model,
            AlignedLine(
                locstring, line["text"], audio, phones, alignment, duration, device
            ),
            settings,
            args.source,
            {
                "phone_model": args.phone_model,
                "template_model": str(args.model.resolve()),
                "donor_glb": str(args.donor_glb.resolve()),
                "output_glb": str(args.output_glb.resolve()),
            },
        )
        reports.append((args.reports / f"{line['key']}.alignment.json", report))
    write_glb(args.output_glb, document, chunks)
    for path, report in reports:
        write_json(path, report)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("audio_dir", type=Path)
    parser.add_argument("donor_glb", type=Path)
    parser.add_argument("output_glb", type=Path)
    parser.add_argument("--source", required=True)
    parser.add_argument("--reports", required=True, type=Path)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--phone-model", default=DEFAULT_PHONE_MODEL)
    parser.add_argument("--device", default="auto")
    add_compile_options(parser, clear_donor_controls=True)
    return parser


def main() -> int:
    compile_manifest(build_parser().parse_args())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
