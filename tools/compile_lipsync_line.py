#!/usr/bin/env python3
"""Align dialogue audio and compile facial curves into a WolvenKit GLB."""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from build_lipsync_corpus import text_to_phones
from build_lipsync_dataset import CTCPhoneAligner, normalize_phones
from lipsync_compiler import (
    DEFAULT_MODEL,
    DEFAULT_PHONE_MODEL,
    BIN_CHUNK,
    AlignedLine,
    CompileSettings,
    add_compile_options,
    compile_aligned_line,
    read_json,
    write_json,
    frame_times,
    apply_speech_window,
    zero_track_prefixes,
    keep_duration_marker_channel,
    append_float_accessor,
    build_neutral_skeletal_channels,
    replace_lipsync_tracks,
    set_animation_duration,
)
from lipsync_glb import read_glb, write_glb

# Historical import surface; new integrations should import lipsync_compiler directly.
__all__ = [
    "BIN_CHUNK",
    "frame_times",
    "apply_speech_window",
    "zero_track_prefixes",
    "keep_duration_marker_channel",
    "append_float_accessor",
    "build_neutral_skeletal_channels",
    "replace_lipsync_tracks",
    "set_animation_duration",
    "build_parser",
    "main",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("donor_glb", type=Path)
    parser.add_argument("output_glb", type=Path)
    parser.add_argument("--text", required=True)
    parser.add_argument(
        "--phones",
        help="Optional space-separated ARPAbet pronunciation overriding automatic G2P",
    )
    parser.add_argument("--locstring", required=True, type=int)
    parser.add_argument("--source", required=True, help="Donor animation name")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--phone-model", default=DEFAULT_PHONE_MODEL)
    parser.add_argument("--device", default="auto")
    add_compile_options(parser)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    settings = CompileSettings.from_args(args)
    phones = (
        normalize_phones(args.phones.split())
        if args.phones
        else text_to_phones(args.text)
    )
    alignment, duration, device = CTCPhoneAligner(args.phone_model, args.device).align(
        args.audio, phones
    )
    document, chunks = read_glb(args.donor_glb)
    report = compile_aligned_line(
        document,
        chunks,
        read_json(args.model),
        AlignedLine(
            args.locstring, args.text, args.audio, phones, alignment, duration, device
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
    write_glb(args.output_glb, document, chunks)
    write_json(args.report or args.output_glb.with_suffix(".alignment.json"), report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
