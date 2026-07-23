#!/usr/bin/env python3
"""Generate labelled GQ001 V and Iris voice audition sets.

This tool intentionally writes audition WAVs only. It never replaces selected
WAVs or packed WEM files.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import soundfile
import torch
from faster_qwen3_tts import FasterQwen3TTS


IRIS_DESIGNS = {
    "iris-a-warm-editor": (
        "Woman, early 30s, warm low alto, calm and precise, quietly empathetic, "
        "neutral Night City accent, measured braindance-editor delivery, "
        "controlled emotion with a faintly dangerous composure."
    ),
    "iris-b-cool-clinical": (
        "Woman, early 30s, cool contralto, restrained and analytical, crisp "
        "diction, understated Night City accent, speaks like a memory technician "
        "who notices every detail, dry confidence without hostility."
    ),
    "iris-c-soft-haunted": (
        "Woman, early 30s, soft smoky alto, intimate and unhurried, compassionate "
        "but guarded, subtle fatigue beneath precise speech, neutral Night City "
        "accent, the voice of someone accustomed to handling damaged memories."
    ),
}

REFERENCE_TEXT = (
    "The memory is intact, but that doesn't mean it's honest. "
    "Give me a minute and I'll show you where it was cut."
)


def write_audio(path: Path, result: tuple[list, int]) -> None:
    audio, sample_rate = result
    path.parent.mkdir(parents=True, exist_ok=True)
    soundfile.write(path, audio[0], sample_rate)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--v-embedding", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--takes", type=int, default=3)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    lines = manifest["spoken_lines"]
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "iris-design-prompts.json").write_text(
        json.dumps(IRIS_DESIGNS, indent=2) + "\n", encoding="utf-8"
    )

    clone = FasterQwen3TTS.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base")
    design = FasterQwen3TTS.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
    )

    v_embedding = torch.load(args.v_embedding, weights_only=True).to(clone.device)
    prompts = {"v-original-embed": {"ref_spk_embedding": [v_embedding]}}

    for label, instruction in IRIS_DESIGNS.items():
        reference_path = args.output / label / "reference.wav"
        write_audio(
            reference_path,
            design.generate_voice_design(
                text=REFERENCE_TEXT,
                language="English",
                instruct=instruction,
                temperature=0.95,
                top_p=0.98,
                repetition_penalty=1.0,
            ),
        )
        prompt_items = clone.model.create_voice_clone_prompt(
            ref_audio=str(reference_path),
            ref_text=REFERENCE_TEXT,
            x_vector_only_mode=True,
        )
        prompts[label] = {
            "ref_spk_embedding": [prompt_items[0].ref_spk_embedding]
        }

    for line in lines:
        speaker = str(line["speaker"]).lower()
        labels = ["v-original-embed"] if speaker == "v" else list(IRIS_DESIGNS)
        for label in labels:
            line_dir = args.output / label / line["key"]
            for take in range(args.takes):
                write_audio(
                    line_dir / f"take-{take + 1:02d}.wav",
                    clone.generate_voice_clone(
                        text=line["text"],
                        language="English",
                        voice_clone_prompt=prompts[label],
                        instruct=None,
                        temperature=0.95,
                        top_p=0.98,
                        repetition_penalty=1.0,
                        xvec_only=True,
                    ),
                )
                print(label, line["key"], take + 1, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
