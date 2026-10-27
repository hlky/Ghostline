"""Versioned, archive-free speech data consumed by the NPC feasibility harness."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import wave
from pathlib import Path

import numpy as np

from build_lipsync_dataset import PhoneAlignment
from lipsync_compiler import AlignedLine, CompileSettings, read_json, synthesize_aligned_line, write_json


def audio_identity(path: Path) -> tuple[float, str]:
    with wave.open(str(path), "rb") as wav:
        if wav.getcomptype() != "NONE" or wav.getnchannels() != 1:
            raise ValueError("Runtime prototype requires mono PCM WAV audio")
        duration = wav.getnframes() / wav.getframerate()
    return duration, hashlib.sha256(path.read_bytes()).hexdigest()


def export_utterance(audio: Path, alignment: dict, model: dict, *, utterance_id: str,
                     npc_id: str, audio_file: str) -> dict:
    if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", utterance_id):
        raise ValueError("Utterance ID must be a short lowercase identifier")
    duration, digest = audio_identity(audio)
    if abs(duration - float(alignment["audio_duration"])) > 0.002:
        raise ValueError("Alignment duration does not match the WAV")
    if Path(alignment["audio_path"].replace("\\", "/")).name != audio.name:
        raise ValueError("Alignment names a different audio source")
    phones = [PhoneAlignment(**item) for item in alignment["alignment"]]
    if any(not np.isfinite(p.start) or not np.isfinite(p.end) or p.start < 0
           or p.end < p.start or p.end > duration + 0.002 for p in phones):
        raise ValueError("Alignment timestamps must be within the WAV")
    line = AlignedLine(int(alignment["locstring_id"]), alignment["text"], audio,
                       alignment["phones"], phones, duration, alignment.get("device", "cached"))
    settings = CompileSettings(**alignment.get("settings", {}))
    report, times, values = synthesize_aligned_line(model, line, settings)
    if values.shape != (len(times), len(model["tracks"])) or not np.isfinite(values).all():
        raise ValueError("Invalid synthesized curve matrix")
    tracks = list(model["tracks"])
    columns = [values[:, i] for i in range(len(tracks))]
    for i, name in enumerate(list(tracks)):
        if name.endswith("LipsyncPoseOutput"):
            paired = name[:-len("LipsyncPoseOutput")] + "AnimOverrideWeight"
            if paired not in tracks:
                tracks.append(paired)
                columns.append(-values[:, i])
    matrix = np.column_stack(columns)
    return {
        "schema_version": 1, "utterance_id": utterance_id, "npc_id": npc_id,
        "audio": {"file": audio_file, "sha256": digest, "duration": duration},
        "curves": {"tracks": tracks, "times": times.tolist(), "values": matrix.tolist()},
        "subtitles": [{"start": 0.0, "end": duration, "text": line.text}],
        "provenance": {"alignment_score": report["alignment_score"],
                       "alignment_source": "cached authoring report; no historical WAV digest",
                       "alignment_sha256": hashlib.sha256(json.dumps(alignment, sort_keys=True).encode("utf-8")).hexdigest(),
                       "model_sha256": hashlib.sha256(json.dumps(model, sort_keys=True).encode("utf-8")).hexdigest(),
                       "settings": report["settings"]},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("alignment", type=Path)
    parser.add_argument("model", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--id", required=True)
    parser.add_argument("--npc", default="runtime_patch")
    parser.add_argument("--audio-file", required=True)
    args = parser.parse_args()
    result = export_utterance(args.audio, read_json(args.alignment), read_json(args.model),
                              utterance_id=args.id, npc_id=args.npc, audio_file=args.audio_file)
    write_json(args.output, result)
    print(json.dumps({"output": str(args.output), "duration": result["audio"]["duration"],
                      "tracks": len(result["curves"]["tracks"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
