#!/usr/bin/env python3
"""Build a resumable vanilla Cyberpunk dialogue/lipsync research corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterable, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from dataclasses import asdict
from functools import lru_cache
from pathlib import Path, PureWindowsPath
from queue import SimpleQueue
from threading import local
from typing import Any

from build_lipsync_dataset import (
    DEFAULT_PHONE_MODEL,
    CTCPhoneAligner,
    dataset_rows,
    decode_wem,
    normalize_phones,
    write_csv,
)
from explore_lipsync import DEFAULT_WOLVENKIT, LipsyncExplorer, read_glb_json

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORK = ROOT / "generated/lipsync-corpus"
DEFAULT_GAME = Path(r"H:\Cyberpunk 2077")
VOICE_MAPS = (
    r"base\localization\en-us\voiceovermap.json",
    r"base\localization\en-us\voiceovermap_1.json",
    r"base\localization\en-us\voiceovermap_rewinded.json",
    r"base\localization\en-us\voiceovermap_holocall.json",
    r"base\localization\en-us\voiceovermap_helmet.json",
)
LIPMAP = r"base\localization\en-us.lipmap"
DEFAULT_ANIM_PREFIX = "base\\localization\\en-us\\lipsync\\base\\quest\\"
ARPABET = re.compile(r"^[A-Z]+[012]?$")


def run(command: Sequence[str], description: str) -> str:
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode:
        details = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
        raise RuntimeError(f"{description} failed ({completed.returncode}).{os.linesep}{details}".rstrip())
    return completed.stdout


def cache_key(value: str) -> str:
    return hashlib.sha256(value.lower().encode("utf-8")).hexdigest()[:16]


def depot_file(root: Path, depot_path: str) -> Path:
    return root.joinpath(*PureWindowsPath(depot_path).parts)


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(path)


@contextmanager
def alignment_lock(path: Path) -> Iterable[None]:
    """Prevent two batch writers from corrupting the same alignment checkpoint."""
    import msvcrt

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as stream:
        stream.seek(0)
        if not stream.read(1):
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
        try:
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError as error:
            raise RuntimeError(f"Another alignment process already owns {path}") from error
        try:
            yield
        finally:
            stream.seek(0)
            msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)


def archive_inventory(wkit: Path, archive: Path, cache: Path) -> list[str]:
    if not cache.is_file():
        output = run(
            [str(wkit), "archiveinfo", str(archive), "-l", "-v", "minimal"],
            f"inventory of {archive.name}",
        )
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(output, encoding="utf-8")
    return [line.strip() for line in cache.read_text(encoding="utf-8-sig").splitlines() if "\\" in line]


def extraction_chunks(
    paths: Sequence[str],
    maximum_pattern_chars: int = 24000,
    maximum_paths: int = 250,
) -> list[list[str]]:
    """Group exact depot paths without exceeding a practical Windows command length."""
    chunks: list[list[str]] = []
    current: list[str] = []
    current_chars = len("^(?:)$")
    for path in paths:
        escaped_chars = len(re.escape(path)) + (1 if current else 0)
        if current and (
            len(current) >= maximum_paths
            or current_chars + escaped_chars > maximum_pattern_chars
        ):
            chunks.append(current)
            current = []
            current_chars = len("^(?:)$")
            escaped_chars = len(re.escape(path))
        current.append(path)
        current_chars += escaped_chars
    if current:
        chunks.append(current)
    return chunks


def extract_paths(wkit: Path, archive: Path, paths: Sequence[str], destination: Path) -> None:
    missing = [path for path in paths if not depot_file(destination, path).is_file()]
    for chunk in extraction_chunks(missing):
        pattern = "^(?:" + "|".join(re.escape(path) for path in chunk) + ")$"
        run(
            [
                str(wkit),
                "extract",
                str(archive),
                "-o",
                str(destination),
                "-r",
                pattern,
                "-v",
                "minimal",
            ],
            f"extracting {len(chunk)} resources from {archive.name}",
        )
    still_missing = [path for path in paths if not depot_file(destination, path).is_file()]
    if still_missing:
        raise FileNotFoundError(f"Archive extraction did not produce: {still_missing[0]}")


def serialized_resource(wkit: Path, binary: Path, depot_path: str, cache: Path) -> Path:
    output_dir = cache / cache_key(depot_path)
    candidates = [path for path in output_dir.glob("*.json") if path.stat().st_size]
    if not candidates:
        output_dir.mkdir(parents=True, exist_ok=True)
        run(
            [str(wkit), "convert", "serialize", str(binary), "-o", str(output_dir), "-v", "minimal"],
            f"serializing {depot_path}",
        )
        candidates = [path for path in output_dir.glob("*.json") if path.stat().st_size]
    if len(candidates) != 1:
        raise RuntimeError(f"Expected one serialized resource for {depot_path}, found {len(candidates)}")
    return candidates[0]


def exported_animset(wkit: Path, game: Path, binary: Path, depot_path: str, cache: Path) -> Path:
    output_dir = cache / cache_key(depot_path)
    candidates = [path for path in output_dir.glob("*.glb") if path.stat().st_size]
    if not candidates:
        output_dir.mkdir(parents=True, exist_ok=True)
        run(
            [
                str(wkit),
                "export",
                str(binary),
                "-o",
                str(output_dir),
                "-gp",
                str(game),
                "-v",
                "minimal",
            ],
            f"exporting {depot_path}",
        )
        candidates = [path for path in output_dir.glob("*.glb") if path.stat().st_size]
    if len(candidates) != 1:
        raise RuntimeError(f"Expected one exported GLB for {depot_path}, found {len(candidates)}")
    return candidates[0]


def cache_resources(
    paths: Sequence[str],
    operation: Callable[[str], Path],
    workers: int,
    label: str,
) -> dict[str, Path]:
    """Populate independent resource caches concurrently and preserve path lookup."""
    unique_paths = list(dict.fromkeys(paths))
    results: dict[str, Path] = {}
    failures: list[tuple[str, Exception]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        pending = {executor.submit(operation, path): path for path in unique_paths}
        for number, future in enumerate(as_completed(pending), 1):
            path = pending[future]
            try:
                results[path] = future.result()
                print(f"[{number}/{len(unique_paths)}] cached {label} {path}", file=sys.stderr)
            except Exception as error:  # noqa: BLE001 - retry external-tool failures serially.
                failures.append((path, error))
                print(
                    f"warning: parallel {label} cache failed for {path}; retrying serially: {error}",
                    file=sys.stderr,
                )
    for number, (path, _) in enumerate(failures, 1):
        results[path] = operation(path)
        print(f"[{number}/{len(failures)}] recovered {label} {path}", file=sys.stderr)
    return results


def resource_data(document: dict[str, Any]) -> dict[str, Any]:
    root = document["Data"]["RootChunk"]
    wrapped = root.get("root")
    if isinstance(wrapped, dict) and isinstance(wrapped.get("Data"), dict):
        return wrapped["Data"]
    return root


def resource_path(value: Any) -> str:
    try:
        return str(value["DepotPath"]["$value"])
    except (KeyError, TypeError):
        return ""


def lipmap_rows(document: dict[str, Any]) -> list[dict[str, str]]:
    data = resource_data(document)
    scene_paths = data.get("scenePaths", [])
    entries = data.get("sceneEntries", [])
    if len(scene_paths) != len(entries):
        raise ValueError("Lipmap scenePaths and sceneEntries lengths differ")
    rows: list[dict[str, str]] = []
    for scene_hash, entry in zip(scene_paths, entries):
        voice_tags = [str(value) for value in entry.get("actorVoiceTags", [])]
        animsets = [resource_path(value) for value in entry.get("animSets", [])]
        for index, animset in enumerate(animsets):
            if animset:
                rows.append(
                    {
                        "scene_hash": str(scene_hash),
                        "actor_voice_tag": voice_tags[index] if index < len(voice_tags) else "",
                        "animset_depot_path": animset,
                    }
                )
    return rows


def subtitle_index(documents: Iterable[tuple[str, dict[str, Any]]]) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for depot_path, document in documents:
        for entry in resource_data(document).get("entries", []):
            string_id = str(entry.get("stringId", ""))
            female = str(entry.get("femaleVariant", "")).strip()
            male = str(entry.get("maleVariant", "")).strip()
            if string_id and (female or male):
                result[string_id] = {
                    "text": female or male,
                    "female_text": female,
                    "male_text": male,
                    "subtitle_depot_path": depot_path,
                }
    return result


def voiceover_index(documents: Iterable[dict[str, Any]]) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for document in documents:
        for entry in resource_data(document).get("entries", []):
            string_id = str(entry.get("stringId", ""))
            female = resource_path(entry.get("femaleResPath"))
            male = resource_path(entry.get("maleResPath"))
            if string_id and (female or male):
                result[string_id] = {
                    "audio_depot_path": female or male,
                    "female_audio_depot_path": female,
                    "male_audio_depot_path": male,
                }
    return result


def subtitle_candidates(animset_path: str, text_inventory: Sequence[str]) -> list[str]:
    scene_name = PureWindowsPath(animset_path).parent.name.lower()
    exact = [path for path in text_inventory if PureWindowsPath(path).stem.lower() == scene_name]
    return sorted(exact, key=lambda path: ("\\subtitles\\quest\\" not in path.lower(), len(path), path))


def clean_line(text: str, duration: float, minimum: float, maximum: float) -> bool:
    return (
        minimum <= duration <= maximum
        and any(character.isalpha() for character in text)
        and len(text) <= 300
        and "<" not in text
        and ">" not in text
        and "lockey" not in text.lower()
    )


def text_to_phones(text: str) -> list[str]:
    try:
        from g2p_en import G2p
    except ImportError as error:
        raise RuntimeError("Automatic phonemization requires g2p_en (pip install g2p_en)") from error
    values = [value for value in G2p()(text) if ARPABET.fullmatch(value)]
    return normalize_phones(values)


def build_catalog(args: argparse.Namespace) -> list[dict[str, Any]]:
    work = Path(args.work)
    game = Path(args.game_path)
    wkit = Path(args.wolvenkit)
    voice_archive = game / "archive/pc/content/lang_en_voice.archive"
    text_archive = game / "archive/pc/content/lang_en_text.archive"
    inventory_dir = work / "cache/inventory"
    voice_paths = archive_inventory(wkit, voice_archive, inventory_dir / "lang_en_voice.txt")
    text_paths = archive_inventory(wkit, text_archive, inventory_dir / "lang_en_text.txt")
    voice_lookup = {path.lower(): path for path in voice_paths}

    required_voice = [voice_lookup[path.lower()] for path in (LIPMAP, *VOICE_MAPS) if path.lower() in voice_lookup]
    if LIPMAP.lower() not in voice_lookup:
        raise FileNotFoundError(f"{LIPMAP} is absent from {voice_archive}")
    extracted_voice = work / "cache/extracted/voice"
    extracted_text = work / "cache/extracted/text"
    serialized = work / "cache/serialized"
    extract_paths(wkit, voice_archive, required_voice, extracted_voice)
    lipmap_json = serialized_resource(
        wkit,
        depot_file(extracted_voice, voice_lookup[LIPMAP.lower()]),
        LIPMAP,
        serialized,
    )
    vo_documents: list[dict[str, Any]] = []
    for path in required_voice:
        if not (path.lower().endswith("voiceovermap.json") or "voiceovermap_" in path.lower()):
            continue
        try:
            output = serialized_resource(wkit, depot_file(extracted_voice, path), path, serialized)
            vo_documents.append(read_json(output))
        except (RuntimeError, ValueError) as error:
            print(f"warning: skipping unreadable VO map {path}: {error}", file=sys.stderr)
    if not vo_documents:
        raise RuntimeError("No readable English voiceover maps were found")
    vo_index = voiceover_index(vo_documents)

    mapped = [
        row
        for row in lipmap_rows(read_json(lipmap_json))
        if row["animset_depot_path"].lower().startswith(args.anim_prefix.lower())
        and not PureWindowsPath(row["animset_depot_path"]).name.lower().startswith("v.")
        and row["animset_depot_path"].lower() in voice_lookup
    ]
    seen_animsets: set[str] = set()
    total_mapped_animsets = len({row["animset_depot_path"].lower() for row in mapped})
    selected: list[dict[str, str]] = []
    for row in mapped:
        key = row["animset_depot_path"].lower()
        if key not in seen_animsets:
            selected.append(row)
            seen_animsets.add(key)
        if args.max_animsets and len(selected) >= args.max_animsets:
            break

    animset_paths = [voice_lookup[row["animset_depot_path"].lower()] for row in selected]
    extract_paths(wkit, voice_archive, animset_paths, extracted_voice)
    subtitle_by_animset = {
        animset_path: (subtitle_candidates(animset_path, text_paths) or [None])[0]
        for animset_path in animset_paths
    }
    subtitle_paths = [path for path in subtitle_by_animset.values() if path is not None]
    extract_paths(wkit, text_archive, list(dict.fromkeys(subtitle_paths)), extracted_text)
    serialized_subtitles = cache_resources(
        subtitle_paths,
        lambda path: serialized_resource(
            wkit,
            depot_file(extracted_text, path),
            path,
            serialized,
        ),
        args.resource_workers,
        "subtitle",
    )
    exported_animsets = cache_resources(
        animset_paths,
        lambda path: exported_animset(
            wkit,
            game,
            depot_file(extracted_voice, path),
            path,
            work / "cache/exports",
        ),
        args.resource_workers,
        "animset",
    )
    catalog: list[dict[str, Any]] = []
    subtitle_cache: dict[str, dict[str, dict[str, str]]] = {}
    for number, (mapping, animset_path) in enumerate(zip(selected, animset_paths), 1):
        subtitle_path = subtitle_by_animset[animset_path]
        if subtitle_path is None:
            continue
        if subtitle_path not in subtitle_cache:
            subtitle_json = serialized_subtitles[subtitle_path]
            subtitle_cache[subtitle_path] = subtitle_index([(subtitle_path, read_json(subtitle_json))])
        subtitles = subtitle_cache[subtitle_path]
        glb = exported_animsets[animset_path]
        explorer = LipsyncExplorer(read_glb_json(glb), str(glb))
        for line in explorer.lines():
            subtitle = subtitles.get(line.locstring_id)
            voiceover = vo_index.get(line.locstring_id)
            if not subtitle or not voiceover:
                continue
            if not clean_line(subtitle["text"], line.duration, args.min_duration, args.max_duration):
                continue
            catalog.append(
                {
                    "animation_name": line.name,
                    "locstring_id": line.locstring_id,
                    "subtitle": subtitle["text"],
                    "female_subtitle": subtitle["female_text"],
                    "male_subtitle": subtitle["male_text"],
                    **voiceover,
                    "subtitle_depot_path": subtitle_path,
                    "animset_depot_path": animset_path,
                    "scene_hash": mapping["scene_hash"],
                    "actor_voice_tag": mapping["actor_voice_tag"],
                    "animation_duration": line.duration,
                    "glb_path": str(glb.resolve()),
                }
            )
            if len(catalog) >= args.max_lines:
                break
        print(f"[{number}/{len(selected)}] {animset_path}: {len(catalog)} usable lines", file=sys.stderr)
        if len(catalog) >= args.max_lines:
            break
    catalog = catalog[: args.max_lines]
    audio_paths = sorted(
        {
            voice_lookup[row["audio_depot_path"].lower()]
            for row in catalog
            if row["audio_depot_path"].lower() in voice_lookup
        }
    )
    extract_paths(wkit, voice_archive, audio_paths, extracted_voice)
    for row in catalog:
        row["wem_path"] = str(depot_file(extracted_voice, row["audio_depot_path"]).resolve())
    write_jsonl(work / "catalog.jsonl", catalog)
    used_animsets = len({row["animset_depot_path"] for row in catalog})
    write_json(
        work / "catalog.summary.json",
        {
            "lines": len(catalog),
            "eligible_mapped_animsets": total_mapped_animsets,
            "animsets_considered": len(selected),
            "animsets_considered_percent": round(
                100.0 * len(selected) / total_mapped_animsets, 3
            ),
            "animsets_used": used_animsets,
            "animsets_used_percent": round(100.0 * used_animsets / total_mapped_animsets, 3),
            "anim_prefix": args.anim_prefix,
            "voice_maps": len(vo_documents),
            "catalog": str((work / "catalog.jsonl").resolve()),
        },
    )
    return catalog


def align_catalog(args: argparse.Namespace, catalog: Sequence[dict[str, Any]]) -> None:
    work = Path(args.work)
    output_dir = work / "lines"
    stale_dir = work / "stale-lines"
    status_path = work / "alignment.status.json"
    alignment_profile = (
        f"{args.model}|attention-mask|group=animset|batch={args.alignment_batch_size}"
    )
    status = read_json(status_path) if status_path.is_file() else {"completed": {}, "failed": {}}
    catalog_ids = {row["locstring_id"] for row in catalog}
    status["completed"] = {
        line_id: value for line_id, value in status["completed"].items() if line_id in catalog_ids
    }
    status["failed"] = {
        line_id: value for line_id, value in status["failed"].items() if line_id in catalog_ids
    }
    for alignment_path in output_dir.glob("*.alignment.json"):
        line_id = alignment_path.name.removesuffix(".alignment.json")
        if line_id in catalog_ids:
            continue
        stale_dir.mkdir(parents=True, exist_ok=True)
        alignment_path.replace(stale_dir / alignment_path.name)
        csv_path = output_dir / f"{line_id}.csv"
        if csv_path.is_file():
            csv_path.replace(stale_dir / csv_path.name)
    current_completed: dict[str, dict[str, str]] = {}
    for line_id in catalog_ids:
        csv_path = output_dir / f"{line_id}.csv"
        alignment_path = output_dir / f"{line_id}.alignment.json"
        if csv_path.is_file() and alignment_path.is_file():
            try:
                report = read_json(alignment_path)
            except (OSError, ValueError):
                continue
            if report.get("alignment_profile") == alignment_profile:
                current_completed[line_id] = {
                    "csv": str(csv_path.resolve()),
                    "alignment": str(alignment_path.resolve()),
                }
                status["failed"].pop(line_id, None)
    status["completed"] = current_completed
    write_json(status_path, status)
    pending = sorted(
        (row for row in catalog if row["locstring_id"] not in status["completed"]),
        key=lambda row: (
            row["glb_path"],
            float(row["animation_duration"]),
            row["locstring_id"],
        ),
    )
    if not pending:
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    worker_state = local()
    aligner_pool: SimpleQueue[CTCPhoneAligner] = SimpleQueue()
    for _ in range(args.alignment_workers):
        aligner_pool.put(CTCPhoneAligner(args.model, args.device))

    @lru_cache(maxsize=32)
    def cached_explorer(glb_path: str) -> LipsyncExplorer:
        return LipsyncExplorer(read_glb_json(Path(glb_path)), glb_path)

    with tempfile.TemporaryDirectory(prefix="ghostline-corpus-audio-") as temporary:
        temporary_dir = Path(temporary)

        def write_aligned_row(
            row: dict[str, Any],
            phones: Sequence[str],
            result: tuple[list[Any], float, str],
        ) -> tuple[str, dict[str, str]]:
            line_id = row["locstring_id"]
            alignments, audio_duration, device = result
            explorer = cached_explorer(row["glb_path"])
            rows, curves = dataset_rows(
                explorer,
                line_id,
                row["subtitle"],
                alignments,
                audio_duration,
                args.fps,
                args.track_set,
            )
            csv_path = output_dir / f"{line_id}.csv"
            temporary_csv = csv_path.with_suffix(".csv.tmp")
            with temporary_csv.open("w", encoding="utf-8", newline="") as stream:
                write_csv(rows, stream)
            temporary_csv.replace(csv_path)
            report = {
                **row,
                "phones": phones,
                "audio_duration": audio_duration,
                "device": device,
                "model": args.model,
                "alignment_profile": alignment_profile,
                "tracks": list(curves),
                "alignment": [asdict(item) for item in alignments],
            }
            alignment_path = output_dir / f"{line_id}.alignment.json"
            write_json(alignment_path, report)
            return line_id, {
                "csv": str(csv_path.resolve()),
                "alignment": str(alignment_path.resolve()),
            }

        def align_rows(
            batch: Sequence[dict[str, Any]],
        ) -> list[tuple[dict[str, Any], dict[str, str] | None, Exception | None]]:
            aligner = getattr(worker_state, "aligner", None)
            if aligner is None:
                aligner = aligner_pool.get()
                worker_state.aligner = aligner
            prepared: list[tuple[dict[str, Any], list[str], Path]] = []
            outcomes: list[tuple[dict[str, Any], dict[str, str] | None, Exception | None]] = []
            for row in batch:
                try:
                    phones = text_to_phones(row["subtitle"])
                    decoded = temporary_dir / f'{row["locstring_id"]}.ogg'
                    decode_wem(Path(row["wem_path"]), decoded)
                    prepared.append((row, phones, decoded))
                except Exception as error:  # noqa: BLE001 - isolate malformed corpus rows.
                    outcomes.append((row, None, error))
            if not prepared:
                return outcomes
            try:
                aligned = aligner.align_batch(
                    [item[2] for item in prepared],
                    [item[1] for item in prepared],
                )
            except Exception:  # noqa: BLE001 - retry a failed batch one row at a time.
                aligned = []
                for row, phones, decoded in prepared:
                    try:
                        result = aligner.align(decoded, phones)
                        _, paths = write_aligned_row(row, phones, result)
                        outcomes.append((row, paths, None))
                    except Exception as error:  # noqa: BLE001 - record and continue long runs.
                        outcomes.append((row, None, error))
                return outcomes
            for (row, phones, _), result in zip(prepared, aligned):
                try:
                    _, paths = write_aligned_row(row, phones, result)
                    outcomes.append((row, paths, None))
                except Exception as error:  # noqa: BLE001 - record and continue long runs.
                    outcomes.append((row, None, error))
            return outcomes

        batches = [
            pending[offset : offset + args.alignment_batch_size]
            for offset in range(0, len(pending), args.alignment_batch_size)
        ]
        with ThreadPoolExecutor(max_workers=args.alignment_workers) as executor:
            futures = {executor.submit(align_rows, batch): batch for batch in batches}
            processed = 0
            for future in as_completed(futures):
                batch = futures[future]
                try:
                    outcomes = future.result()
                except Exception as error:  # noqa: BLE001 - worker boundary must preserve progress.
                    outcomes = [(row, None, error) for row in batch]
                for row, completed_paths, error in outcomes:
                    line_id = row["locstring_id"]
                    processed += 1
                    if error is None and completed_paths is not None:
                        status["completed"][line_id] = completed_paths
                        status["failed"].pop(line_id, None)
                        outcome = "aligned"
                    else:
                        status["failed"][line_id] = str(error)
                        outcome = "failed"
                    print(f"[{processed}/{len(pending)}] {outcome} {line_id}", file=sys.stderr)
                write_json(status_path, status)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolve vanilla lipsync animations through subtitles/audio and optionally align them."
    )
    parser.add_argument("--work", default=str(DEFAULT_WORK))
    parser.add_argument("--game-path", default=str(DEFAULT_GAME))
    parser.add_argument("--wolvenkit", default=str(DEFAULT_WOLVENKIT))
    parser.add_argument("--anim-prefix", default=DEFAULT_ANIM_PREFIX)
    parser.add_argument("--max-lines", type=int, default=500)
    parser.add_argument("--max-animsets", type=int, default=50)
    parser.add_argument("--min-duration", type=float, default=0.35)
    parser.add_argument("--max-duration", type=float, default=15.0)
    parser.add_argument(
        "--resource-workers",
        type=int,
        default=2,
        help="Concurrent WolvenKit serialization/export workers.",
    )
    parser.add_argument("--align", action="store_true")
    parser.add_argument(
        "--alignment-workers",
        type=int,
        default=1,
        help="Independent resident phoneme aligners; use 2 on a sufficiently large GPU.",
    )
    parser.add_argument(
        "--alignment-batch-size",
        type=int,
        default=1,
        help="Duration-sorted utterances per padded CTC model pass.",
    )
    parser.add_argument("--device", default="auto")
    parser.add_argument("--model", default=DEFAULT_PHONE_MODEL)
    parser.add_argument("--fps", type=float, default=30.0)
    parser.add_argument("--track-set", choices=["mouth", "all-lipsync", "all-dynamic"], default="mouth")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if (
        args.max_lines <= 0
        or args.max_animsets < 0
        or args.resource_workers <= 0
        or args.alignment_workers <= 0
        or args.alignment_batch_size <= 0
    ):
        parser.error(
            "--max-lines and all worker/batch sizes must be positive; "
            "--max-animsets cannot be negative"
        )
    try:
        catalog = build_catalog(args)
        if args.align:
            with alignment_lock(Path(args.work) / ".alignment.lock"):
                align_catalog(args, catalog)
        print(f"Built {len(catalog)} catalog rows at {Path(args.work).resolve()}")
        return 0
    except (FileNotFoundError, KeyError, RuntimeError, ValueError) as error:
        parser.exit(2, f"error: {error}{os.linesep}")


if __name__ == "__main__":
    raise SystemExit(main())
