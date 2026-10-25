"""Replay a GQ004 candidate batch through ghostline-voice full-reference synthesis."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', choices=['female', 'male', 'velvet-a'], required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    config = json.loads((HERE / 'toolchain.json').read_text(encoding='utf-8'))
    output = ROOT / 'generated-voices/gq004'
    if args.batch == 'velvet-a':
        speaker = 'Velvet'
        embedding = output / 'embeddings/velvet.safetensors'
        reference = dict(text=config['velvet_reference_text'], codes=str(output / 'reference-codes/velvet.json'))
    else:
        speaker = 'V'
        selected = json.loads((ROOT / config['v_sources']).read_text(encoding='utf-8'))
        source = selected['V ' + ('Female' if args.batch == 'female' else 'Male')]
        embedding = Path(source['embedding'])
        reference = dict(text=source['reference_text'], codes=source['reference_codes'])
    if not embedding.is_file() or not Path(reference['codes']).is_file() or not reference['text'].strip():
        raise ValueError('Full reference requires the exact transcript, encoded audio and speaker embedding')
    output.mkdir(parents=True, exist_ok=True)
    prompts = output / f'{args.batch}-reference-prompts.json'
    command = [str(ROOT / 'tools/ghostline-voice/target/release/ghostline-voice.exe'),
               'render-local', '--index', str(HERE.parent / 'script/voice-production.json'),
               '--checkpoint', config['checkpoint'], '--generation-artifact', config['generation_artifact'],
               '--decoder-artifact', config['decoder_artifact'], '--speaker', speaker,
               '--embedding', f'{speaker}={embedding}', '--reference-prompts', str(prompts),
               '--versions', str(config['versions']), '--seed-base', str(config['seed_base']),
               '--output', str(output / args.batch)]
    if args.force:
        command.append('--force')
    if args.dry_run:
        print(json.dumps(dict(command=command, reference={speaker: reference}), indent=2))
        return 0
    prompts.write_text(json.dumps({speaker: reference}, indent=2) + '\n', encoding='utf-8')
    environment = dict(os.environ, DINOML_NATIVE_LIBRARY_DIR=config['native_library_directory'])
    subprocess.run(command, cwd=ROOT, env=environment, check=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
