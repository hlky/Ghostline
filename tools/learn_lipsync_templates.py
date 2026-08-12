#!/usr/bin/env python3
"""Learn robust phoneme, context, and reduced-viseme templates from a lipsync corpus."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import cdist


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


@dataclass(frozen=True)
class Occurrence:
    line_id: str
    phone: str
    previous: str
    following: str
    duration: float
    score: float
    trajectory: np.ndarray
    start_window: np.ndarray
    end_window: np.ndarray


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def rounded(values: np.ndarray | Sequence[float], digits: int = 6) -> list[Any]:
    array = np.asarray(values)
    return np.round(array, digits).tolist()


def sample_matrix(times: np.ndarray, values: np.ndarray, targets: np.ndarray) -> np.ndarray:
    """Linearly sample every curve at target times, clamping at line boundaries."""
    if len(times) == 0:
        raise ValueError("Cannot sample an empty curve matrix")
    right = np.searchsorted(times, targets, side="right")
    right = np.clip(right, 1, len(times) - 1)
    left = right - 1
    left_time = times[left]
    right_time = times[right]
    denominator = right_time - left_time
    amount = np.divide(
        targets - left_time,
        denominator,
        out=np.zeros_like(targets, dtype=np.float64),
        where=np.abs(denominator) > 1e-12,
    )
    amount = np.clip(amount, 0.0, 1.0)
    sampled = values[left] + (values[right] - values[left]) * amount[:, None]
    sampled[targets <= times[0]] = values[0]
    sampled[targets >= times[-1]] = values[-1]
    return sampled.astype(np.float32)


def load_curve_csv(path: Path) -> tuple[list[str], np.ndarray, np.ndarray, np.ndarray]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError(f"Missing CSV header in {path}")
        tracks = [name for name in reader.fieldnames if name not in METADATA_COLUMNS]
        rows = list(reader)
    if len(rows) < 2:
        raise ValueError(f"Expected at least two curve rows in {path}")
    times = np.asarray([float(row["time"]) for row in rows], dtype=np.float64)
    curves = np.asarray([[float(row[name]) for name in tracks] for row in rows], dtype=np.float32)
    silence = np.asarray(
        [[float(row[name]) for name in tracks] for row in rows if row["phoneme"] == "SIL"],
        dtype=np.float32,
    )
    return tracks, times, curves, silence


def collect_occurrences(
    lines_dir: Path,
    phase_grid: np.ndarray,
    boundary_offsets: np.ndarray,
    minimum_score: float,
    excluded_lines: set[str] | None = None,
) -> tuple[list[str], list[Occurrence], np.ndarray, dict[str, int]]:
    occurrences: list[Occurrence] = []
    silence_parts: list[np.ndarray] = []
    expected_tracks: list[str] | None = None
    skipped = Counter()
    reports = sorted(lines_dir.glob("*.alignment.json"))
    if not reports:
        raise FileNotFoundError(f"No alignment reports found under {lines_dir}")
    for report_path in reports:
        report = read_json(report_path)
        line_id = str(report["locstring_id"])
        if excluded_lines and line_id in excluded_lines:
            skipped["held_out_line"] += 1
            continue
        csv_path = lines_dir / f"{line_id}.csv"
        if not csv_path.is_file():
            skipped["missing_csv"] += 1
            continue
        tracks, times, curves, silence = load_curve_csv(csv_path)
        if expected_tracks is None:
            expected_tracks = tracks
        elif tracks != expected_tracks:
            raise ValueError(f"Curve track order differs in {csv_path}")
        if silence.size:
            silence_parts.append(silence)
        audio_duration = float(report["audio_duration"])
        animation_duration = float(report["animation_duration"])
        if audio_duration <= 0 or animation_duration <= 0:
            skipped["invalid_duration"] += 1
            continue
        scale = animation_duration / audio_duration
        alignment = report["alignment"]
        for index, phone_row in enumerate(alignment):
            score = float(phone_row["score"])
            if score < minimum_score:
                skipped["low_confidence"] += 1
                continue
            start = float(phone_row["start"]) * scale
            end = float(phone_row["end"]) * scale
            duration = end - start
            if duration <= 1e-5:
                skipped["zero_duration"] += 1
                continue
            trajectory_times = start + phase_grid * duration
            previous = str(alignment[index - 1]["phone"]) if index else "SIL"
            following = str(alignment[index + 1]["phone"]) if index + 1 < len(alignment) else "SIL"
            occurrences.append(
                Occurrence(
                    line_id=line_id,
                    phone=str(phone_row["phone"]),
                    previous=previous,
                    following=following,
                    duration=duration,
                    score=score,
                    trajectory=sample_matrix(times, curves, trajectory_times),
                    start_window=sample_matrix(times, curves, start + boundary_offsets),
                    end_window=sample_matrix(times, curves, end + boundary_offsets),
                )
            )
    if expected_tracks is None:
        raise RuntimeError("No usable aligned lines were found")
    silence_samples = (
        np.concatenate(silence_parts, axis=0)
        if silence_parts
        else np.zeros((1, len(expected_tracks)), dtype=np.float32)
    )
    return expected_tracks, occurrences, silence_samples, dict(skipped)


def array_statistics(values: np.ndarray) -> dict[str, Any]:
    return {
        "median": rounded(np.median(values, axis=0)),
        "q25": rounded(np.quantile(values, 0.25, axis=0)),
        "q75": rounded(np.quantile(values, 0.75, axis=0)),
        "std": rounded(np.std(values, axis=0)),
    }


def summarize_phones(
    occurrences: Sequence[Occurrence],
    phase_grid: np.ndarray,
) -> tuple[dict[str, dict[str, Any]], dict[str, np.ndarray]]:
    grouped: dict[str, list[Occurrence]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence.phone].append(occurrence)
    summaries: dict[str, dict[str, Any]] = {}
    medians: dict[str, np.ndarray] = {}
    for phone in sorted(grouped):
        values = grouped[phone]
        trajectories = np.stack([item.trajectory for item in values])
        medians[phone] = np.median(trajectories, axis=0)
        durations = np.asarray([item.duration * 1000 for item in values])
        scores = np.asarray([item.score for item in values])
        summaries[phone] = {
            "occurrences": len(values),
            "lines": len({item.line_id for item in values}),
            "duration_ms": {
                "median": round(float(np.median(durations)), 3),
                "q25": round(float(np.quantile(durations, 0.25)), 3),
                "q75": round(float(np.quantile(durations, 0.75)), 3),
            },
            "alignment_score": {
                "median": round(float(np.median(scores)), 6),
                "q25": round(float(np.quantile(scores, 0.25)), 6),
            },
            "phase": rounded(phase_grid),
            "curves": array_statistics(trajectories),
        }
    return summaries, medians


def standardized_centers(medians: dict[str, np.ndarray]) -> tuple[list[str], np.ndarray, np.ndarray]:
    phones = sorted(medians)
    centers = np.stack([np.mean(medians[phone][2:-2], axis=0) for phone in phones])
    scale = np.std(centers, axis=0)
    scale = np.maximum(scale, 0.02)
    standardized = (centers - np.median(centers, axis=0)) / scale
    return phones, standardized, scale


def silhouette_values(values: np.ndarray, labels: np.ndarray) -> np.ndarray:
    distances = cdist(values, values)
    result = np.zeros(len(values), dtype=np.float64)
    for index, label in enumerate(labels):
        own = np.where(labels == label)[0]
        own = own[own != index]
        if not len(own):
            continue
        within = float(np.mean(distances[index, own]))
        outside = [
            float(np.mean(distances[index, np.where(labels == other)[0]]))
            for other in set(labels)
            if other != label
        ]
        nearest = min(outside)
        result[index] = (nearest - within) / max(nearest, within, 1e-9)
    return result


def rebalance_clusters(
    values: np.ndarray,
    labels: np.ndarray,
    counts: np.ndarray,
    target_count: int,
    minimum_occurrences: int,
) -> list[list[int]]:
    clusters = [np.where(labels == label)[0].tolist() for label in sorted(set(labels))]
    while len(clusters) > 1:
        totals = [int(np.sum(counts[members])) for members in clusters]
        undersized = [index for index, total in enumerate(totals) if total < minimum_occurrences]
        if not undersized:
            break
        source = min(undersized, key=lambda index: (totals[index], index))
        source_center = np.mean(values[clusters[source]], axis=0)
        destinations = [index for index in range(len(clusters)) if index != source]
        destination = min(
            destinations,
            key=lambda index: float(
                np.linalg.norm(source_center - np.mean(values[clusters[index]], axis=0))
            ),
        )
        clusters[destination].extend(clusters[source])
        del clusters[source]
    while len(clusters) < target_count:
        candidates: list[tuple[float, int, list[int], list[int]]] = []
        for index, members in enumerate(clusters):
            if len(members) < 2:
                continue
            subset = values[members]
            split_labels = fcluster(linkage(subset, method="ward"), 2, criterion="maxclust")
            left = [member for member, label in zip(members, split_labels) if label == 1]
            right = [member for member, label in zip(members, split_labels) if label == 2]
            if not left or not right:
                continue
            if min(int(np.sum(counts[left])), int(np.sum(counts[right]))) < minimum_occurrences:
                continue
            center = np.mean(subset, axis=0)
            error = float(np.sum((subset - center) ** 2))
            candidates.append((error, index, left, right))
        if not candidates:
            break
        _error, index, left, right = max(candidates, key=lambda item: (item[0], -item[1]))
        clusters[index] = left
        clusters.append(right)
    while len(clusters) > target_count:
        pairs: list[tuple[float, int, int]] = []
        for left in range(len(clusters)):
            for right in range(left + 1, len(clusters)):
                distance = float(
                    np.linalg.norm(
                        np.mean(values[clusters[left]], axis=0)
                        - np.mean(values[clusters[right]], axis=0)
                    )
                )
                pairs.append((distance, left, right))
        _distance, left, right = min(pairs)
        clusters[left].extend(clusters[right])
        del clusters[right]
    return clusters


def cluster_visemes(
    medians: dict[str, np.ndarray],
    phone_counts: dict[str, int],
    cluster_count: int,
    tracks: Sequence[str],
    minimum_occurrences: int,
) -> tuple[list[dict[str, Any]], dict[str, str], float, np.ndarray]:
    phones, _standardized, track_scale = standardized_centers(medians)
    centers = np.stack([np.mean(medians[phone][2:-2], axis=0) for phone in phones])
    visual_mask = np.asarray(
        [
            name in {"jaliJaw", "jaliLips", "muzzleLips"}
            or (
                name.startswith(("jaw_", "lips_", "tongue_"))
                and "sticky" not in name.lower()
            )
            for name in tracks
        ]
    )
    values = centers[:, visual_mask]
    if not 2 <= cluster_count <= len(phones):
        raise ValueError(f"--visemes must be between 2 and {len(phones)}")
    labels = fcluster(linkage(values, method="ward"), cluster_count, criterion="maxclust")
    counts = np.asarray([phone_counts[phone] for phone in phones])
    member_groups = rebalance_clusters(
        values, labels, counts, cluster_count, minimum_occurrences
    )
    labels = np.zeros(len(phones), dtype=np.int32)
    for label, members in enumerate(member_groups, 1):
        labels[members] = label
    silhouettes = silhouette_values(values, labels)
    provisional: list[tuple[str, list[int], int]] = []
    for label in sorted(set(labels)):
        members = np.where(labels == label)[0].tolist()
        distances = cdist(values[members], values[members])
        medoid_index = members[int(np.argmin(np.mean(distances, axis=1)))]
        provisional.append((phones[medoid_index], members, label))
    provisional.sort(key=lambda item: item[0])
    clusters: list[dict[str, Any]] = []
    phone_to_viseme: dict[str, str] = {}
    for number, (medoid, members, _label) in enumerate(provisional):
        name = f"V{number:02d}_{medoid}"
        member_phones = [phones[index] for index in members]
        for phone in member_phones:
            phone_to_viseme[phone] = name
        member_templates = np.stack([medians[phone] for phone in member_phones])
        clusters.append(
            {
                "name": name,
                "medoid": medoid,
                "phones": sorted(member_phones),
                "occurrences": sum(phone_counts[phone] for phone in member_phones),
                "silhouette": round(float(np.mean(silhouettes[members])), 6),
                "curves": array_statistics(member_templates),
            }
        )
    return clusters, phone_to_viseme, float(np.mean(silhouettes)), track_scale


def top_tracks(delta: np.ndarray, tracks: Sequence[str], limit: int = 8) -> list[dict[str, Any]]:
    magnitude = np.mean(np.abs(delta), axis=0)
    indices = np.argsort(magnitude)[::-1][:limit]
    return [{"track": tracks[index], "mean_abs_delta": round(float(magnitude[index]), 6)} for index in indices]


def context_effects(
    occurrences: Sequence[Occurrence],
    medians: dict[str, np.ndarray],
    tracks: Sequence[str],
    track_scale: np.ndarray,
    minimum_count: int,
) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for direction, attribute in (("previous", "previous"), ("next", "following")):
        grouped: dict[tuple[str, str], list[np.ndarray]] = defaultdict(list)
        for occurrence in occurrences:
            context_phone = getattr(occurrence, attribute)
            if occurrence.phone in medians:
                grouped[(occurrence.phone, context_phone)].append(
                    occurrence.trajectory - medians[occurrence.phone]
                )
        rows: list[dict[str, Any]] = []
        for (phone, context_phone), values in sorted(grouped.items()):
            if len(values) < minimum_count:
                continue
            deltas = np.stack(values)
            median_delta = np.median(deltas, axis=0)
            scaled_rms = math.sqrt(float(np.mean((median_delta / track_scale[None, :]) ** 2)))
            rows.append(
                {
                    "phone": phone,
                    "context_phone": context_phone,
                    "occurrences": len(values),
                    "scaled_rms": round(scaled_rms, 6),
                    "top_tracks": top_tracks(median_delta, tracks),
                    "delta_median": rounded(median_delta),
                }
            )
        result[direction] = sorted(rows, key=lambda row: (-row["scaled_rms"], row["phone"], row["context_phone"]))
    return result


def threshold_offset(offsets: np.ndarray, values: np.ndarray, threshold: float, earliest: bool) -> int | None:
    candidates = offsets[values >= threshold]
    if not len(candidates):
        return None
    selected = np.min(candidates) if earliest else np.max(candidates)
    return int(round(float(selected * 1000)))


def boundary_profiles(
    occurrences: Sequence[Occurrence],
    medians: dict[str, np.ndarray],
    silence_center: np.ndarray,
    boundary_offsets: np.ndarray,
    track_scale: np.ndarray,
    threshold: float,
) -> dict[str, dict[str, Any]]:
    grouped: dict[str, list[Occurrence]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence.phone].append(occurrence)
    centers = {phone: np.mean(template[2:-2], axis=0) for phone, template in medians.items()}
    centers["SIL"] = silence_center
    start_mask = boundary_offsets <= 0
    end_mask = boundary_offsets >= 0
    profiles: dict[str, dict[str, Any]] = {}
    for phone in sorted(grouped):
        start_strengths: list[np.ndarray] = []
        end_strengths: list[np.ndarray] = []
        values = grouped[phone]
        current = centers[phone]
        for occurrence in values:
            previous = centers.get(occurrence.previous, silence_center)
            following = centers.get(occurrence.following, silence_center)
            previous_delta = (current - previous) / track_scale
            following_delta = (current - following) / track_scale
            previous_energy = float(np.dot(previous_delta, previous_delta))
            following_energy = float(np.dot(following_delta, following_delta))
            if previous_energy > 0.0625:
                relative = (occurrence.start_window[start_mask] - previous) / track_scale[None, :]
                projected = relative @ previous_delta / previous_energy
                start_strengths.append(np.clip(projected, 0.0, 1.0))
            if following_energy > 0.0625:
                relative = (occurrence.end_window[end_mask] - following) / track_scale[None, :]
                projected = relative @ following_delta / following_energy
                end_strengths.append(np.clip(projected, 0.0, 1.0))
        start_array = np.stack(start_strengths) if start_strengths else np.zeros((1, int(start_mask.sum())))
        end_array = np.stack(end_strengths) if end_strengths else np.zeros((1, int(end_mask.sum())))
        start_median = np.median(start_array, axis=0)
        end_median = np.median(end_array, axis=0)
        anticipation = threshold_offset(
            boundary_offsets[start_mask], start_median, threshold, earliest=True
        )
        release = threshold_offset(boundary_offsets[end_mask], end_median, threshold, earliest=False)
        profiles[phone] = {
            "start_window_occurrences": len(start_strengths),
            "end_window_occurrences": len(end_strengths),
            "anticipation_ms": anticipation,
            "anticipation_censored": anticipation == int(round(float(boundary_offsets[start_mask][0] * 1000))),
            "release_ms": release,
            "release_censored": release == int(round(float(boundary_offsets[end_mask][-1] * 1000))),
            "start_offsets_ms": rounded(boundary_offsets[start_mask] * 1000, 3),
            "activation_median": rounded(start_median),
            "activation_q25": rounded(np.quantile(start_array, 0.25, axis=0)),
            "activation_q75": rounded(np.quantile(start_array, 0.75, axis=0)),
            "end_offsets_ms": rounded(boundary_offsets[end_mask] * 1000, 3),
            "retention_median": rounded(end_median),
            "retention_q25": rounded(np.quantile(end_array, 0.25, axis=0)),
            "retention_q75": rounded(np.quantile(end_array, 0.75, axis=0)),
            "start_curves": array_statistics(np.stack([item.start_window for item in values])),
            "end_curves": array_statistics(np.stack([item.end_window for item in values])),
        }
    return profiles


def write_phone_csv(path: Path, phones: dict[str, dict[str, Any]], mapping: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["phone", "viseme", "occurrences", "lines", "duration_ms", "alignment_score"],
            lineterminator="\n",
        )
        writer.writeheader()
        for phone, summary in phones.items():
            writer.writerow(
                {
                    "phone": phone,
                    "viseme": mapping[phone],
                    "occurrences": summary["occurrences"],
                    "lines": summary["lines"],
                    "duration_ms": summary["duration_ms"]["median"],
                    "alignment_score": summary["alignment_score"]["median"],
                }
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Learn phoneme, context, and viseme templates from a corpus.")
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    parser.add_argument("--output", help="Output directory; defaults to <corpus>/templates.")
    parser.add_argument("--visemes", type=int, default=13)
    parser.add_argument("--phase-bins", type=int, default=9)
    parser.add_argument("--boundary-ms", default="-200,-160,-120,-80,-40,0,40,80,120,160,200")
    parser.add_argument("--minimum-score", type=float, default=0.5)
    parser.add_argument("--minimum-context", type=int, default=8)
    parser.add_argument("--minimum-viseme-occurrences", type=int, default=100)
    parser.add_argument("--activation-threshold", type=float, default=0.5)
    parser.add_argument("--exclude-line", action="append", default=[], help="Locstring ID held out of training.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.phase_bins < 5:
        parser.error("--phase-bins must be at least 5")
    if not 0 <= args.minimum_score <= 1 or not 0 < args.activation_threshold < 1:
        parser.error("score and activation thresholds must be between zero and one")
    corpus = Path(args.corpus)
    output = Path(args.output) if args.output else corpus / "templates"
    try:
        phase_grid = np.linspace(0.0, 1.0, args.phase_bins)
        boundary_offsets = np.asarray(
            [float(value.strip()) / 1000 for value in args.boundary_ms.split(",")], dtype=np.float64
        )
        if 0.0 not in boundary_offsets or not np.all(np.diff(boundary_offsets) > 0):
            raise ValueError("--boundary-ms must be increasing and include zero")
        tracks, occurrences, silence, skipped = collect_occurrences(
            corpus / "lines",
            phase_grid,
            boundary_offsets,
            args.minimum_score,
            set(args.exclude_line),
        )
        phones, medians = summarize_phones(occurrences, phase_grid)
        phone_counts = {phone: int(summary["occurrences"]) for phone, summary in phones.items()}
        visemes, mapping, silhouette, track_scale = cluster_visemes(
            medians,
            phone_counts,
            args.visemes,
            tracks,
            args.minimum_viseme_occurrences,
        )
        contexts = context_effects(
            occurrences, medians, tracks, track_scale, args.minimum_context
        )
        silence_center = np.median(silence, axis=0)
        boundaries = boundary_profiles(
            occurrences,
            medians,
            silence_center,
            boundary_offsets,
            track_scale,
            args.activation_threshold,
        )
        model = {
            "schema": "ghostline-lipsync-templates-v1",
            "source": str(corpus.resolve()),
            "tracks": tracks,
            "phase": rounded(phase_grid),
            "boundary_offsets_ms": rounded(boundary_offsets * 1000, 3),
            "minimum_alignment_score": args.minimum_score,
            "excluded_lines": sorted(set(args.exclude_line)),
            "occurrences": len(occurrences),
            "skipped": skipped,
            "silence": array_statistics(silence),
            "phones": phones,
            "viseme_count": len(visemes),
            "viseme_silhouette": round(silhouette, 6),
            "phone_to_viseme": mapping,
            "visemes": visemes,
            "contexts": contexts,
            "boundaries": boundaries,
        }
        write_json(output / "lipsync-templates.json", model)
        write_phone_csv(output / "phone-summary.csv", phones, mapping)
        write_json(
            output / "summary.json",
            {
                "phones": len(phones),
                "visemes": len(visemes),
                "occurrences": len(occurrences),
                "tracks": len(tracks),
                "silence_frames": len(silence),
                "context_previous": len(contexts["previous"]),
                "context_next": len(contexts["next"]),
                "viseme_silhouette": round(silhouette, 6),
                "skipped": skipped,
                "output": str((output / "lipsync-templates.json").resolve()),
            },
        )
        print(f"Learned {len(phones)} phones into {len(visemes)} visemes at {output.resolve()}")
        return 0
    except (FileNotFoundError, KeyError, RuntimeError, ValueError) as error:
        parser.exit(2, f"error: {error}{os.linesep}")


if __name__ == "__main__":
    raise SystemExit(main())
