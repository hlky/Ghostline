#!/usr/bin/env python3
"""Align phonemes to dialogue audio and join them with Cyberpunk facial curves."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from itertools import pairwise
from pathlib import Path
from typing import Any, TextIO

from explore_lipsync import DEFAULT_WOLVENKIT, LipsyncExplorer, load_source

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PHONE_MODEL = "mostafaashahin/wav2vec2-base-timit-phoneme-arpa-39-v2"
DEFAULT_WEM_DECODER = ROOT / "tools/convert_wem_to_ogg.ps1"
PHONE_FOLDS = {"AO": "AA"}


@dataclass(frozen=True)
class PhoneAlignment:
    phone: str
    start: float
    end: float
    score: float
    token_start: float
    token_end: float


@dataclass(frozen=True)
class TokenRun:
    token_id: int
    start_frame: int
    end_frame: int
    score: float


class CTCPhoneAligner:
    """Reusable forced aligner that keeps the expensive CTC model resident."""

    def __init__(self, model_id: str = DEFAULT_PHONE_MODEL, device_name: str = "auto") -> None:
        try:
            import torch
            from huggingface_hub import hf_hub_download
            from transformers import AutoFeatureExtractor, AutoModelForCTC
        except ImportError as error:
            raise RuntimeError(
                "CTC alignment requires torch, torchaudio, transformers, huggingface_hub, and soundfile"
            ) from error

        self.torch = torch
        self.model_id = model_id
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(model_id)
        vocabulary_path = hf_hub_download(model_id, "vocab.json")
        with Path(vocabulary_path).open(encoding="utf-8") as stream:
            self.vocabulary = json.load(stream)
        self.normalized_vocabulary = {
            key.strip().upper(): int(value) for key, value in self.vocabulary.items()
        }
        if device_name == "auto":
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = torch.device(device_name)
        self.model = AutoModelForCTC.from_pretrained(model_id).to(self.device)
        self.model.eval()

    def align_batch(
        self,
        audio_paths: Sequence[Path],
        phone_sequences: Sequence[Sequence[str]],
    ) -> list[tuple[list[PhoneAlignment], float, str]]:
        """Align a padded batch while preserving each utterance's true frame length."""
        try:
            import soundfile
            import torchaudio
        except ImportError as error:
            raise RuntimeError("CTC alignment requires torchaudio and soundfile") from error
        if not audio_paths or len(audio_paths) != len(phone_sequences):
            raise ValueError("Audio and phoneme batches must have the same nonzero length")

        expected_rate = int(self.feature_extractor.sampling_rate)
        waveforms = []
        durations = []
        target_rows = []
        for audio_path, phones in zip(audio_paths, phone_sequences):
            waveform, sample_rate = soundfile.read(audio_path, dtype="float32", always_2d=True)
            mono = waveform.mean(axis=1)
            durations.append(len(mono) / sample_rate)
            if sample_rate != expected_rate:
                tensor = self.torch.from_numpy(mono)
                mono = torchaudio.functional.resample(tensor, sample_rate, expected_rate).numpy()
            missing = [phone for phone in phones if phone not in self.normalized_vocabulary]
            if missing:
                raise ValueError(
                    f"Phone model {self.model_id} does not support: {', '.join(missing)}"
                )
            waveforms.append(mono)
            target_rows.append([self.normalized_vocabulary[phone] for phone in phones])

        sample_lengths = self.torch.tensor([len(waveform) for waveform in waveforms])
        inputs = self.feature_extractor(
            waveforms,
            sampling_rate=expected_rate,
            return_attention_mask=True,
            return_tensors="pt",
            padding=True,
        )
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with self.torch.inference_mode():
            emissions = self.model(**inputs).logits.log_softmax(-1)
        emission_lengths = self.model._get_feat_extract_output_lengths(sample_lengths).to(
            dtype=self.torch.int32
        )
        blank = int(self.vocabulary.get("<pad>", 0))
        target_lengths = self.torch.tensor(
            [len(row) for row in target_rows], dtype=self.torch.int32
        )
        padding_token = next(
            token_id for token_id in self.normalized_vocabulary.values() if token_id != blank
        )
        targets = self.torch.full(
            (len(target_rows), int(target_lengths.max())),
            padding_token,
            dtype=self.torch.int32,
        )
        for row_index, target_ids in enumerate(target_rows):
            targets[row_index, : len(target_ids)] = self.torch.tensor(
                target_ids, dtype=self.torch.int32
            )
        # ROCm torchaudio ships the dynamic-programming aligner as a CPU kernel.
        # Keep the expensive acoustic model on the GPU and transfer only its compact logits.
        results = []
        for row_index, (phones, target_ids, duration) in enumerate(
            zip(phone_sequences, target_rows, durations)
        ):
            frame_count = int(emission_lengths[row_index])
            target_count = int(target_lengths[row_index])
            aligned, alignment_scores = torchaudio.functional.forced_align(
                emissions[row_index : row_index + 1, :frame_count].cpu(),
                targets[row_index : row_index + 1, :target_count],
                blank=blank,
            )
            path = aligned[0].detach().cpu().tolist()
            probabilities = alignment_scores[0].exp().detach().cpu().tolist()
            runs = token_runs(path, probabilities, blank)
            if [run.token_id for run in runs] != target_ids:
                raise RuntimeError(
                    "Forced alignment returned a token sequence different from the requested phones"
                )
            seconds_per_frame = duration / frame_count
            results.append(
                (expand_token_runs(phones, runs, seconds_per_frame), duration, str(self.device))
            )
        return results

    def align(self, audio_path: Path, phones: Sequence[str]) -> tuple[list[PhoneAlignment], float, str]:
        return self.align_batch([audio_path], [phones])[0]


def normalize_phones(raw: str | Sequence[str]) -> list[str]:
    values = raw.split() if isinstance(raw, str) else list(raw)
    unstressed = [phone.upper().rstrip("012") for phone in values if phone.strip()]
    phones = [PHONE_FOLDS.get(phone, phone) for phone in unstressed]
    if not phones:
        raise ValueError("At least one phoneme is required")
    return phones


def token_runs(path: Sequence[int], scores: Sequence[float], blank: int = 0) -> list[TokenRun]:
    if len(path) != len(scores):
        raise ValueError("Alignment path and score lengths differ")
    runs: list[TokenRun] = []
    start = 0
    while start < len(path):
        end = start + 1
        while end < len(path) and path[end] == path[start]:
            end += 1
        token_id = int(path[start])
        if token_id != blank:
            runs.append(
                TokenRun(
                    token_id=token_id,
                    start_frame=start,
                    end_frame=end,
                    score=sum(float(value) for value in scores[start:end]) / (end - start),
                )
            )
        start = end
    return runs


def expand_token_runs(
    phones: Sequence[str],
    runs: Sequence[TokenRun],
    seconds_per_frame: float,
) -> list[PhoneAlignment]:
    if len(phones) != len(runs):
        raise ValueError(f"Expected {len(phones)} aligned token runs, found {len(runs)}")
    centers = [((run.start_frame + run.end_frame) / 2) * seconds_per_frame for run in runs]
    boundaries = [runs[0].start_frame * seconds_per_frame]
    boundaries.extend((left + right) / 2 for left, right in pairwise(centers))
    boundaries.append(runs[-1].end_frame * seconds_per_frame)
    return [
        PhoneAlignment(
            phone=phone,
            start=boundaries[index],
            end=boundaries[index + 1],
            score=run.score,
            token_start=run.start_frame * seconds_per_frame,
            token_end=run.end_frame * seconds_per_frame,
        )
        for index, (phone, run) in enumerate(zip(phones, runs))
    ]


def align_phones_ctc(
    audio_path: Path,
    phones: Sequence[str],
    model_id: str = DEFAULT_PHONE_MODEL,
    device_name: str = "auto",
) -> tuple[list[PhoneAlignment], float, str]:
    return CTCPhoneAligner(model_id, device_name).align(audio_path, phones)


def decode_wem(source: Path, destination: Path, decoder: Path = DEFAULT_WEM_DECODER) -> None:
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    if powershell is None:
        raise FileNotFoundError("PowerShell was not found; WEM decoding requires PowerShell 7")
    command = [
        powershell,
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(decoder),
        "-InputFile",
        str(source),
        "-OutputFile",
        str(destination),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0 or not destination.is_file():
        details = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
        raise RuntimeError(f"Failed to decode {source}.{os.linesep}{details}".rstrip())


def curve_value(keys: Sequence[tuple[float, float]], time: float) -> float:
    if not keys:
        return 0.0
    if time <= keys[0][0]:
        return keys[0][1]
    if time >= keys[-1][0]:
        return keys[-1][1]
    for (left_time, left_value), (right_time, right_value) in pairwise(keys):
        if left_time <= time <= right_time:
            if math.isclose(left_time, right_time):
                return right_value
            amount = (time - left_time) / (right_time - left_time)
            return left_value + (right_value - left_value) * amount
    return keys[-1][1]


def animation_curves(
    explorer: LipsyncExplorer,
    line_selector: str,
    track_set: str,
) -> dict[str, list[tuple[float, float]]]:
    _, animation = explorer.select_line(line_selector)
    dynamic: dict[int, list[tuple[float, float]]] = {}
    constant: dict[int, list[tuple[float, float]]] = {}
    for field, destination in (("trackKeys", dynamic), ("constTrackKeys", constant)):
        for key in explorer._keys(animation, field):
            index = int(key["trackIndex"])
            destination.setdefault(index, []).append((float(key["time"]), float(key["value"])))

    def included(index: int) -> bool:
        name = explorer.track_name(index)
        lowered = name.lower()
        if track_set == "all-dynamic":
            return index in dynamic
        if track_set == "all-lipsync":
            return "lipsync" in lowered or name in {"jaliJaw", "jaliLips", "muzzleLips"}
        return (
            name in {"lipSyncEnvelope", "jaliJaw", "jaliLips", "muzzleLips"}
            or (
                lowered.endswith("lipsyncposeoutput")
                and lowered.startswith(("jaw_", "lips_", "tongue_", "neck_throat_"))
            )
        )

    curves: dict[str, list[tuple[float, float]]] = {}
    for index in sorted(set(dynamic) | set(constant)):
        if not included(index):
            continue
        keys = dynamic.get(index, constant.get(index, []))
        curves[explorer.track_name(index)] = sorted(keys)
    return curves


def phone_at_time(
    time: float,
    alignments: Sequence[PhoneAlignment],
) -> tuple[str, str, str, float, float, float]:
    for index, alignment in enumerate(alignments):
        if alignment.start <= time < alignment.end or (
            index == len(alignments) - 1 and math.isclose(time, alignment.end)
        ):
            previous = alignments[index - 1].phone if index else "SIL"
            following = alignments[index + 1].phone if index + 1 < len(alignments) else "SIL"
            return (
                alignment.phone,
                previous,
                following,
                alignment.start,
                alignment.end,
                alignment.score,
            )
    return "SIL", "", "", 0.0, 0.0, 1.0


def dataset_rows(
    explorer: LipsyncExplorer,
    line_selector: str,
    text: str,
    alignments: Sequence[PhoneAlignment],
    audio_duration: float,
    fps: float,
    track_set: str,
) -> tuple[list[dict[str, Any]], dict[str, list[tuple[float, float]]]]:
    line, animation = explorer.select_line(line_selector)
    animation_duration = explorer.duration(animation)
    scale = animation_duration / audio_duration
    scaled_alignments = [
        PhoneAlignment(
            phone=item.phone,
            start=item.start * scale,
            end=item.end * scale,
            score=item.score,
            token_start=item.token_start * scale,
            token_end=item.token_end * scale,
        )
        for item in alignments
    ]
    curves = animation_curves(explorer, line_selector, track_set)
    frame_count = math.floor(animation_duration * fps) + 1
    rows: list[dict[str, Any]] = []
    for frame in range(frame_count):
        time = min(frame / fps, animation_duration)
        phone, previous, following, phone_start, phone_end, score = phone_at_time(time, scaled_alignments)
        row: dict[str, Any] = {
            "line": line.name,
            "locstring_id": line.locstring_id,
            "text": text,
            "frame": frame,
            "time": time,
            "phoneme": phone,
            "previous_phoneme": previous,
            "next_phoneme": following,
            "phoneme_start": phone_start,
            "phoneme_end": phone_end,
            "alignment_score": score,
        }
        row.update((name, curve_value(keys, time)) for name, keys in curves.items())
        rows.append(row)
    return rows, curves


def write_csv(rows: Iterable[dict[str, Any]], stream: TextIO) -> None:
    materialized = list(rows)
    if not materialized:
        return
    writer = csv.DictWriter(stream, fieldnames=list(materialized[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(materialized)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Join forced-aligned ARPAbet phonemes to Cyberpunk lipsync facial curves."
    )
    parser.add_argument("-f", "--file", required=True, help="Input lipsync .anims or exported GLB.")
    parser.add_argument("--line", required=True, help="Animation index, name, or locstring ID.")
    parser.add_argument("--audio", required=True, help="Matching WAV, OGG, FLAC, or WEM voiceover.")
    parser.add_argument("--text", default="", help="Spoken transcript retained in the dataset.")
    parser.add_argument("--phones", required=True, help="Space-separated ARPAbet phonemes.")
    parser.add_argument("--output", help="CSV output; stdout when omitted.")
    parser.add_argument("--alignment-output", help="Optional JSON alignment report.")
    parser.add_argument("--fps", type=float, default=30.0)
    parser.add_argument("--track-set", choices=["mouth", "all-lipsync", "all-dynamic"], default="mouth")
    parser.add_argument("--model", default=DEFAULT_PHONE_MODEL)
    parser.add_argument("--device", default="auto", help="Torch device: auto, cpu, or cuda.")
    parser.add_argument("--game-path", help="Cyberpunk directory when --file is .anims.")
    parser.add_argument("--wolvenkit", default=str(DEFAULT_WOLVENKIT))
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.fps <= 0:
        parser.error("--fps must be greater than zero")
    try:
        document, source_label = load_source(
            Path(args.file),
            Path(args.wolvenkit),
            Path(args.game_path) if args.game_path else None,
        )
        explorer = LipsyncExplorer(document, source_label)
        phones = normalize_phones(args.phones)
        audio_path = Path(args.audio)
        with tempfile.TemporaryDirectory(prefix="ghostline-wem-") as temporary:
            if audio_path.suffix.lower() == ".wem":
                decoded = Path(temporary) / f"{audio_path.stem}.ogg"
                decode_wem(audio_path, decoded)
                aligned_audio = decoded
            else:
                aligned_audio = audio_path
            alignments, audio_duration, device = align_phones_ctc(
                aligned_audio,
                phones,
                args.model,
                args.device,
            )
        rows, curves = dataset_rows(
            explorer,
            args.line,
            args.text,
            alignments,
            audio_duration,
            args.fps,
            args.track_set,
        )
        if args.output:
            output = Path(args.output)
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("w", encoding="utf-8", newline="") as stream:
                write_csv(rows, stream)
        else:
            write_csv(rows, sys.stdout)
        if args.alignment_output:
            report = {
                "source": source_label,
                "line": args.line,
                "text": args.text,
                "phones": phones,
                "audio": str(audio_path),
                "audio_duration": audio_duration,
                "animation_duration": explorer.duration(explorer.select_line(args.line)[1]),
                "device": device,
                "model": args.model,
                "tracks": list(curves),
                "alignment": [asdict(item) for item in alignments],
            }
            alignment_output = Path(args.alignment_output)
            alignment_output.parent.mkdir(parents=True, exist_ok=True)
            alignment_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        return 0
    except (FileNotFoundError, KeyError, RuntimeError, ValueError) as error:
        parser.exit(2, f"error: {error}{os.linesep}")


if __name__ == "__main__":
    raise SystemExit(main())
