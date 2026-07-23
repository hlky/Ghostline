#!/usr/bin/env python3
"""Generate deterministic-layout Qwen3-TTS candidates for a dialogue manifest.

This is an offline authoring tool. It writes audition candidates and cached
speaker embeddings; it does not select takes or modify packed mod resources.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import soundfile
import torch
from faster_qwen3_tts import FasterQwen3TTS


V_REFERENCE_TEXT = (
    "Just worked out that way. Came to Night City, got my first job, "
    "then another... And so on, and so forth"
)
IRIS_REFERENCE_TEXT = (
    "You have the cache. Good. Keep it isolated—I don't know what it tries "
    "to shake hands with yet."
)
IRIS_VOICE_DESIGN = (
    "Woman in her early thirties with a warm low alto voice. Measured, calm "
    "and precise, with the quiet empathy of someone accustomed to handling "
    "other people's damaged memories. Neutral Night City accent, restrained "
    "emotion, slight fatigue, crisp consonants, never theatrical or breathy."
)


def load_manifest(path: Path) -> list[dict[str, str]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    lines = value.get("spoken_lines")
    if not isinstance(lines, list) or not lines:
        raise SystemExit(f"{path} has no spoken_lines")
    return lines


def speaker_embedding(
    model: FasterQwen3TTS,
    reference_audio: Path,
    reference_text: str,
    cache_path: Path,
) -> dict[str, list[torch.Tensor]]:
    if not cache_path.exists():
        prompt_items = model.model.create_voice_clone_prompt(
            ref_audio=str(reference_audio),
            ref_text=reference_text,
            x_vector_only_mode=True,
        )
        embedding = prompt_items[0].ref_spk_embedding
        torch.save(embedding.detach().cpu(), cache_path)
    embedding = torch.load(
        cache_path, map_location=model.device, weights_only=True
    ).to(model.device)
    return {"ref_spk_embedding": [embedding]}


def design_iris_reference(output: Path) -> None:
    voice_design = FasterQwen3TTS.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
    )
    audio, sample_rate = voice_design.generate_voice_design(
        text=IRIS_REFERENCE_TEXT,
        language="English",
        instruct=IRIS_VOICE_DESIGN,
        temperature=0.92,
        top_p=0.98,
        repetition_penalty=1.0,
    )
    soundfile.write(output, audio[0], sample_rate)
    del voice_design
    torch.cuda.empty_cache()


def generate_candidate(
    model: FasterQwen3TTS,
    output: Path,
    text: str,
    prompt: dict[str, list[torch.Tensor]],
) -> None:
    audio, sample_rate = model.generate_voice_clone(
        text=text,
        language="English",
        voice_clone_prompt=prompt,
        instruct=None,
        temperature=0.95,
        top_p=0.98,
        repetition_penalty=1.0,
        xvec_only=True,
    )
    soundfile.write(output, audio[0], sample_rate)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--v-reference", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--iris-reference", type=Path)
    parser.add_argument("--candidates", type=int, default=3)
    args = parser.parse_args()

    if args.candidates < 1:
        parser.error("--candidates must be positive")
    args.output.mkdir(parents=True, exist_ok=True)
    embedding_dir = args.output / "embeddings"
    embedding_dir.mkdir(exist_ok=True)

    iris_reference = args.iris_reference or args.output / "iris_reference.wav"
    if not iris_reference.exists():
        design_iris_reference(iris_reference)

    model = FasterQwen3TTS.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base")
    prompts = {
        "v": speaker_embedding(
            model,
            args.v_reference,
            V_REFERENCE_TEXT,
            embedding_dir / "v.pt",
        ),
        "iris": speaker_embedding(
            model,
            iris_reference,
            IRIS_REFERENCE_TEXT,
            embedding_dir / "iris.pt",
        ),
    }

    for line in load_manifest(args.manifest):
        speaker = str(line["speaker"]).lower()
        if speaker not in prompts:
            raise SystemExit(f"No reference configured for speaker {line['speaker']}")
        for candidate in range(args.candidates):
            output = args.output / f"{line['key']}-version{candidate:02d}.wav"
            generate_candidate(model, output, str(line["text"]), prompts[speaker])
            print(output, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
