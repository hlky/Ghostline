"""Record archive-index evidence for direct resource ownership without extraction.

The index reports all matching vanilla providers, not installed load order.
Resource paths are matched using RED's case-insensitive FNV-1a64 depot hash.
"""
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
from pathlib import Path
import subprocess

from ghostline_red import DEFAULT_RED_CLI
from toolchain import resolve_tool


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--game-root', type=Path)
    args = parser.parse_args()
    game = resolve_tool('game', args.game_root)
    args.out.mkdir(parents=True, exist_ok=True)
    archives = sorted(p for folder in ('content', 'ep1') for p in (game / 'archive/pc' / folder).glob('*.archive')
                      if not p.name.startswith(('lang_', 'audio_')) or p.name in ('lang_en_text.archive', 'lang_en_voice.archive'))

    def inspect(archive):
        relative = archive.relative_to(game / 'archive/pc').as_posix()
        target = args.out / (relative.replace('/', '--') + '.json')
        stat = archive.stat()
        if target.exists():
            previous = json.loads(target.read_text(encoding='utf-8'))
            if previous.get('archive_size') == stat.st_size and previous.get('archive_mtime_ns') == stat.st_mtime_ns:
                return relative, len(previous['entries'])
        result = subprocess.run([str(DEFAULT_RED_CLI), 'archive-list', str(archive), '--json'], capture_output=True, check=True)
        data = json.loads(result.stdout)
        receipt = {'archive_relative': relative, 'archive_size': stat.st_size,
                   'archive_mtime_ns': stat.st_mtime_ns,
                   'entries': [{k: r[k] for k in ('name_hash', 'size', 'sha1')} for r in data['entries']]}
        target.write_text(json.dumps(receipt, separators=(',', ':')) + '\n', encoding='utf-8')
        return relative, len(receipt['entries'])

    with ThreadPoolExecutor(max_workers=3) as pool:
        for archive, count in pool.map(inspect, archives):
            print(archive, count, flush=True)


if __name__ == '__main__':
    main()
