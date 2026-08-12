#!/usr/bin/env python3
"""Synthesize one aligned line from learned templates and compare it with vanilla curves."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path
from typing import Any, Sequence

import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "generated/lipsync-corpus"
METADATA_COLUMNS = {
    "line",
    "locstring_id",
    "text",
    "frame",
    "time",
    "phoneme",
    "previous_phoneme",
    "next_phoneme",
    "phoneme_start",
    "phoneme_end",
    "alignment_score",
}


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def read_original(path: Path) -> tuple[list[str], np.ndarray, np.ndarray, list[str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError(f"Missing CSV header in {path}")
        tracks = [name for name in reader.fieldnames if name not in METADATA_COLUMNS]
        rows = list(reader)
    times = np.asarray([float(row["time"]) for row in rows], dtype=np.float64)
    values = np.asarray([[float(row[track]) for track in tracks] for row in rows], dtype=np.float64)
    phones = [row["phoneme"] for row in rows]
    return tracks, times, values, phones


def interpolate_phase(values: np.ndarray, phase_grid: np.ndarray, phase: float) -> np.ndarray:
    phase = float(np.clip(phase, phase_grid[0], phase_grid[-1]))
    right = int(np.searchsorted(phase_grid, phase, side="right"))
    right = min(max(right, 1), len(phase_grid) - 1)
    left = right - 1
    width = phase_grid[right] - phase_grid[left]
    amount = 0.0 if abs(width) < 1e-12 else (phase - phase_grid[left]) / width
    return values[left] + (values[right] - values[left]) * amount


def smoothstep(value: float) -> float:
    value = float(np.clip(value, 0.0, 1.0))
    return value * value * (3.0 - 2.0 * value)


def transition_seconds(
    boundary: dict[str, Any],
    field: str,
    censored_field: str,
    fallback_ms: float,
    maximum_ms: float,
) -> float:
    value = boundary.get(field)
    if value is None or boundary.get(censored_field):
        value = fallback_ms
    return min(abs(float(value)), maximum_ms) / 1000


def context_lookup(model: dict[str, Any], direction: str) -> dict[tuple[str, str], np.ndarray]:
    return {
        (row["phone"], row["context_phone"]): np.asarray(row["delta_median"], dtype=np.float64)
        for row in model["contexts"][direction]
    }


def aligned_phones(report: dict[str, Any]) -> list[dict[str, Any]]:
    scale = float(report["animation_duration"]) / float(report["audio_duration"])
    rows: list[dict[str, Any]] = []
    alignment = report["alignment"]
    for index, item in enumerate(alignment):
        rows.append(
            {
                "phone": str(item["phone"]),
                "start": float(item["start"]) * scale,
                "end": float(item["end"]) * scale,
                "previous": str(alignment[index - 1]["phone"]) if index else "SIL",
                "next": str(alignment[index + 1]["phone"]) if index + 1 < len(alignment) else "SIL",
            }
        )
    return rows


def spoken_text(report: dict[str, Any]) -> str:
    return str(report.get("text") or report.get("subtitle") or "")


def synthesize(
    model: dict[str, Any],
    report: dict[str, Any],
    times: np.ndarray,
    context_weight: float,
    fallback_transition_ms: float,
    maximum_transition_ms: float,
) -> tuple[np.ndarray, np.ndarray]:
    tracks = model["tracks"]
    phase_grid = np.asarray(model["phase"], dtype=np.float64)
    silence = np.asarray(model["silence"]["median"], dtype=np.float64)
    templates = {
        phone: np.asarray(value["curves"]["median"], dtype=np.float64)
        for phone, value in model["phones"].items()
    }
    previous_effects = context_lookup(model, "previous")
    next_effects = context_lookup(model, "next")
    phones = aligned_phones(report)
    predicted = np.zeros((len(times), len(tracks)), dtype=np.float64)
    phone_only = np.zeros_like(predicted)
    for frame, time in enumerate(times):
        weighted = np.zeros(len(tracks), dtype=np.float64)
        weighted_phone = np.zeros(len(tracks), dtype=np.float64)
        weight_sum = 0.0
        for item in phones:
            phone = item["phone"]
            if phone not in templates:
                continue
            boundary = model["boundaries"][phone]
            anticipation = transition_seconds(
                boundary,
                "anticipation_ms",
                "anticipation_censored",
                fallback_transition_ms,
                maximum_transition_ms,
            )
            release = transition_seconds(
                boundary,
                "release_ms",
                "release_censored",
                fallback_transition_ms,
                maximum_transition_ms,
            )
            start = item["start"]
            end = item["end"]
            if time < start - anticipation or time > end + release:
                continue
            if time < start:
                weight = smoothstep((time - (start - anticipation)) / max(anticipation, 1e-6))
            elif time > end:
                weight = 1.0 - smoothstep((time - end) / max(release, 1e-6))
            else:
                weight = 1.0
            phase = (time - start) / max(end - start, 1e-6)
            base = interpolate_phase(templates[phone], phase_grid, phase)
            pose = base.copy()
            previous = previous_effects.get((phone, item["previous"]))
            following = next_effects.get((phone, item["next"]))
            if previous is not None:
                pose += context_weight * interpolate_phase(previous, phase_grid, phase)
            if following is not None:
                pose += context_weight * interpolate_phase(following, phase_grid, phase)
            weighted += weight * pose
            weighted_phone += weight * base
            weight_sum += weight
        if weight_sum <= 1e-9:
            predicted[frame] = silence
            phone_only[frame] = silence
        elif weight_sum < 1.0:
            predicted[frame] = weighted + (1.0 - weight_sum) * silence
            phone_only[frame] = weighted_phone + (1.0 - weight_sum) * silence
        else:
            predicted[frame] = weighted / weight_sum
            phone_only[frame] = weighted_phone / weight_sum
    return predicted, phone_only


def metric_set(original: np.ndarray, predicted: np.ndarray, tracks: Sequence[str]) -> dict[str, Any]:
    error = predicted - original
    per_track: list[dict[str, Any]] = []
    correlations: list[float] = []
    for index, track in enumerate(tracks):
        left = original[:, index]
        right = predicted[:, index]
        if np.std(left) > 1e-6 and np.std(right) > 1e-6:
            correlation = float(np.corrcoef(left, right)[0, 1])
            correlations.append(correlation)
        else:
            correlation = 0.0
        per_track.append(
            {
                "track": track,
                "mae": round(float(np.mean(np.abs(error[:, index]))), 6),
                "rmse": round(math.sqrt(float(np.mean(error[:, index] ** 2))), 6),
                "correlation": round(correlation, 6),
                "original_std": round(float(np.std(left)), 6),
            }
        )
    return {
        "mae": round(float(np.mean(np.abs(error))), 6),
        "rmse": round(math.sqrt(float(np.mean(error**2))), 6),
        "median_track_correlation": round(float(np.median(correlations)) if correlations else 0.0, 6),
        "per_track": sorted(per_track, key=lambda row: (-row["original_std"], row["track"])),
    }


def comparison_metrics(
    original: np.ndarray,
    predicted: np.ndarray,
    phone_only: np.ndarray,
    silence: np.ndarray,
    frame_phones: Sequence[str],
    tracks: Sequence[str],
) -> dict[str, Any]:
    active = np.asarray([phone != "SIL" for phone in frame_phones])
    silence_prediction = np.broadcast_to(silence, original.shape)
    return {
        "all_frames": {
            "synthesized": metric_set(original, predicted, tracks),
            "phone_only": metric_set(original, phone_only, tracks),
            "silence_baseline": metric_set(original, silence_prediction, tracks),
        },
        "active_frames": {
            "frames": int(np.sum(active)),
            "synthesized": metric_set(original[active], predicted[active], tracks),
            "phone_only": metric_set(original[active], phone_only[active], tracks),
            "silence_baseline": metric_set(original[active], silence_prediction[active], tracks),
        },
    }


def write_prediction_csv(
    path: Path,
    times: np.ndarray,
    frame_phones: Sequence[str],
    tracks: Sequence[str],
    predicted: np.ndarray,
    original: np.ndarray,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    fields = ["frame", "time", "phoneme"]
    fields.extend(f"predicted:{track}" for track in tracks)
    fields.extend(f"original:{track}" for track in tracks)
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(fields)
        for frame, time in enumerate(times):
            writer.writerow(
                [frame, time, frame_phones[frame], *predicted[frame].tolist(), *original[frame].tolist()]
            )
    temporary.replace(path)


def draw_comparison(
    path: Path,
    title: str,
    times: np.ndarray,
    original: np.ndarray,
    predicted: np.ndarray,
    phone_only: np.ndarray,
    tracks: Sequence[str],
    phones: Sequence[dict[str, Any]],
    count: int = 6,
) -> list[str]:
    variance = np.std(original, axis=0)
    selected = np.argsort(variance)[::-1][:count].tolist()
    width = 1500
    panel_height = 190
    top = 70
    left = 180
    right = 30
    image = Image.new("RGB", (width, top + panel_height * count + 45), "#10141b")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((20, 18), title, fill="#f2f5f7", font=font)
    draw.text((20, 38), "vanilla  |  synthesized  |  phone-only", fill="#9aa7b2", font=font)
    duration = max(float(times[-1]), 1e-6)
    plot_width = width - left - right
    for panel, index in enumerate(selected):
        y0 = top + panel * panel_height
        y1 = y0 + panel_height - 35
        draw.rectangle((left, y0, width - right, y1), outline="#34404c")
        draw.text((12, y0 + 5), tracks[index][:26], fill="#d5dde5", font=font)
        values = np.concatenate([original[:, index], predicted[:, index], phone_only[:, index]])
        minimum = float(np.min(values))
        maximum = float(np.max(values))
        if math.isclose(minimum, maximum):
            maximum = minimum + 1.0
        def point(time: float, value: float) -> tuple[int, int]:
            x = left + int(time / duration * plot_width)
            y = y1 - int((value - minimum) / (maximum - minimum) * (y1 - y0))
            return x, y
        for item in phones:
            x, _ = point(float(item["start"]), minimum)
            draw.line((x, y0, x, y1), fill="#27323d")
            if panel == 0:
                draw.text((x + 2, y0 + 2), item["phone"], fill="#7f8d99", font=font)
        for series, color in (
            (phone_only[:, index], "#74808a"),
            (predicted[:, index], "#ff9d3d"),
            (original[:, index], "#46d7e8"),
        ):
            points = [point(float(time), float(value)) for time, value in zip(times, series)]
            if len(points) >= 2:
                draw.line(points, fill=color, width=2)
        draw.text((left + 4, y1 + 7), f"{minimum:.3f}", fill="#71808e", font=font)
        draw.text((width - right - 50, y1 + 7), f"{maximum:.3f}", fill="#71808e", font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)
    return [tracks[index] for index in selected]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Synthesize and evaluate one held-out vanilla lipsync line.")
    parser.add_argument("--templates", required=True)
    parser.add_argument("--alignment", required=True)
    parser.add_argument("--original", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--context-weight", type=float, default=0.7)
    parser.add_argument("--fallback-transition-ms", type=float, default=40.0)
    parser.add_argument("--maximum-transition-ms", type=float, default=120.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        model = read_json(Path(args.templates))
        report = read_json(Path(args.alignment))
        tracks, times, original, frame_phones = read_original(Path(args.original))
        if tracks != model["tracks"]:
            raise ValueError("Original curve tracks do not match the learned model")
        if str(report["locstring_id"]) not in set(model.get("excluded_lines", [])):
            raise ValueError("Evaluation line was not excluded from template training")
        predicted, phone_only = synthesize(
            model,
            report,
            times,
            args.context_weight,
            args.fallback_transition_ms,
            args.maximum_transition_ms,
        )
        output = Path(args.output)
        output.mkdir(parents=True, exist_ok=True)
        metrics = comparison_metrics(
            original,
            predicted,
            phone_only,
            np.asarray(model["silence"]["median"]),
            frame_phones,
            tracks,
        )
        phone_rows = aligned_phones(report)
        plot_tracks = draw_comparison(
            output / "comparison.png",
            f'{spoken_text(report)}  ({report["locstring_id"]})',
            times,
            original,
            predicted,
            phone_only,
            tracks,
            phone_rows,
        )
        write_prediction_csv(
            output / "predicted-vs-original.csv", times, frame_phones, tracks, predicted, original
        )
        result = {
            "schema": "ghostline-lipsync-heldout-evaluation-v1",
            "locstring_id": str(report["locstring_id"]),
            "text": spoken_text(report),
            "templates": str(Path(args.templates).resolve()),
            "alignment": str(Path(args.alignment).resolve()),
            "original": str(Path(args.original).resolve()),
            "context_weight": args.context_weight,
            "fallback_transition_ms": args.fallback_transition_ms,
            "maximum_transition_ms": args.maximum_transition_ms,
            "frames": len(times),
            "plot_tracks": plot_tracks,
            "metrics": metrics,
        }
        write_json(output / "comparison.json", result)
        print(f"Synthesized held-out line {report['locstring_id']} at {output.resolve()}")
        return 0
    except (FileNotFoundError, KeyError, RuntimeError, ValueError) as error:
        parser.exit(2, f"error: {error}{os.linesep}")


if __name__ == "__main__":
    raise SystemExit(main())
