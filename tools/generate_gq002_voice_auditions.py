#!/usr/bin/env python3
"""Generate three-take GQ002 V/Cinder voice audition sets.

V always uses the supplied cached v.pt x-vector. Cinder is intentionally
rendered from three nearby voice designs so a stable character voice can be
chosen before selected takes are promoted to the authored WAV bank.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import soundfile
import torch
from faster_qwen3_tts import FasterQwen3TTS


CINDER_DESIGNS = {
    "cinder-a-grounded-medic": (
        "Woman, late 30s, low dry alto, calm and controlled, former emergency "
        "medical worker, practical and unsentimental, precise consonants, "
        "subtle fatigue, neutral Night City accent, anger expressed through "
        "quiet focus rather than volume, natural conversational delivery."
    ),
    "cinder-b-organizer": (
        "Woman, late 30s, steady smoky contralto, community organizer used to "
        "being obeyed in a crisis, restrained warmth beneath blunt pragmatism, "
        "measured Night City cadence, slightly rough texture, never theatrical "
        "or breathy, confident without sounding corporate."
    ),
    "cinder-c-field-tech": (
        "Woman, late 30s, compact low mezzo voice, dry and incisive, veteran "
        "field technician with medical experience, clipped phrasing when "
        "explaining risks, guarded empathy, understated urban accent, natural "
        "speech with controlled intensity and no melodrama."
    ),
}

REFERENCE_TEXT = (
    "A clean shutdown is a luxury. First we trace every dependency, then we "
    "decide what can break without taking somebody with it."
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
    (args.output / "cinder-design-prompts.json").write_text(
        json.dumps(CINDER_DESIGNS, indent=2) + "\n", encoding="utf-8"
    )

    clone = FasterQwen3TTS.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base")
    design = FasterQwen3TTS.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
    )
    v_embedding = torch.load(args.v_embedding, weights_only=True).to(clone.device)
    prompts = {"v-original-embed": {"ref_spk_embedding": [v_embedding]}}

    for label, instruction in CINDER_DESIGNS.items():
        reference_path = args.output / label / "reference.wav"
        write_audio(
            reference_path,
            design.generate_voice_design(
                text=REFERENCE_TEXT,
                language="English",
                instruct=instruction,
                temperature=0.92,
                top_p=0.98,
                repetition_penalty=1.0,
            ),
        )
        prompt_items = clone.model.create_voice_clone_prompt(
            ref_audio=str(reference_path),
            ref_text=REFERENCE_TEXT,
            x_vector_only_mode=True,
        )
        embedding = prompt_items[0].ref_spk_embedding.detach().cpu()
        torch.save(embedding, args.output / label / "cinder.pt")
        prompts[label] = {"ref_spk_embedding": [embedding.to(clone.device)]}

    for line in lines:
        speaker = str(line["speaker"]).lower()
        labels = ["v-original-embed"] if speaker == "v" else list(CINDER_DESIGNS)
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
