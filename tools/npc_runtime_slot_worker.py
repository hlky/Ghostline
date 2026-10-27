"""Publish completed prototype WAVs to one loose Audioware slot, outside CET's sandbox."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
import wave
from pathlib import Path

MOD_PATH = "bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime"
SLOT_PATH = "r6/audioware/GhostlineNPCRuntime/slot_0.wav"
LINE_IDS = {"why_you", "client"}


def publish(game: Path, request: dict) -> dict:
    token = request.get("token")
    if not isinstance(token, str) or not 1 <= len(token) <= 128:
        raise ValueError("Invalid request token")
    line_id = request.get("utterance_id")
    if line_id not in LINE_IDS:
        raise ValueError("Unknown prototype utterance")
    mod = game / MOD_PATH
    utterance = json.loads((mod / f"utterances/{line_id}.json").read_text(encoding="utf-8"))
    audio = mod / f"audio/{line_id}.wav"
    data = audio.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != utterance["audio"]["sha256"]:
        raise ValueError("WAV digest does not match the utterance")
    with wave.open(str(audio), "rb") as wav:
        duration = wav.getnframes() / wav.getframerate()
        if wav.getcomptype() != "NONE" or wav.getnchannels() != 1:
            raise ValueError("Expected mono PCM audio")
    if abs(duration - utterance["audio"]["duration"]) > 0.002:
        raise ValueError("WAV duration does not match the utterance")
    slot = game / SLOT_PATH
    if not slot.is_file():
        raise FileNotFoundError("Install the valid placeholder slot before starting the worker")
    temporary = slot.with_suffix(".wav.tmp")
    temporary.write_bytes(data)
    os.replace(temporary, slot)
    return {"token": token, "status": "ready", "utterance_id": line_id,
            "sha256": digest, "duration": duration}


def process_request(game: Path, request: dict) -> dict:
    try:
        return publish(game, request)
    except (ValueError, OSError, KeyError, wave.Error) as error:
        return {"token": request.get("token"), "status": "error", "error": str(error)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", type=Path, required=True,
                        help="Game root, or a verified install-stage root for offline checks")
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    mod = args.game / MOD_PATH
    if not mod.is_dir() or not (args.game / SLOT_PATH).is_file():
        parser.error("Install/stage the NPC experiment first")
    last_token = None
    print("NPC slot worker ready. Ctrl+C stops it.", flush=True)
    try:
        while True:
            try:
                request = json.loads((mod / "slot-request.json").read_text(encoding="utf-8"))
                if request.get("token") != last_token:
                    last_token = request.get("token")
                    response = process_request(args.game, request)
                    temporary = mod / "slot-ready.json.tmp"
                    temporary.write_text(json.dumps(response), encoding="utf-8")
                    os.replace(temporary, mod / "slot-ready.json")
                    print(json.dumps(response), flush=True)
                    if args.once:
                        return
            except (FileNotFoundError, json.JSONDecodeError):
                if args.once:
                    parser.error("No complete slot-request.json is available")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("NPC slot worker stopped.")


if __name__ == "__main__":
    main()
