"""Serialize an extracted research corpus, reusing identical earlier payloads.

Research only. Archive extraction order is explicit: base gamedata then ep1
gamedata. Freeze the resulting per-payload identities with --freeze after
indexing; external graph dependencies can supply --extra-origins receipts.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from ghostline_red import DEFAULT_RED_CLI, ensure_schema
from toolchain import resolve_tool


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument('--reuse', type=Path)
    parser.add_argument('--freeze', type=Path)
    parser.add_argument('--extra-origins', type=Path)
    parser.add_argument('--base-paths', type=Path, required=True)
    parser.add_argument('--ep1-paths', type=Path, required=True)
    args = parser.parse_args()
    root = args.scratch
    if args.freeze:
        index = json.loads((root / 'indexed/index.json').read_text())['resources']
        base = set(args.base_paths.read_text(encoding='utf-8-sig').splitlines())
        ep1 = set(args.ep1_paths.read_text(encoding='utf-8-sig').splitlines())
        origins = {}
        if args.extra_origins:
            origins = json.loads(args.extra_origins.read_text(encoding='utf-8'))
        rows = []
        for item in index:
            if item['status'] == 'failed':
                raise ValueError(item)
            depot = item['depot']
            archive = origins.get(depot)
            if archive is None:
                archive = ('ep1/ep1_2_gamedata.archive' if depot in ep1 else
                           'content/basegame_4_gamedata.archive' if depot in base else None)
            if archive is None:
                raise ValueError('Missing archive provenance: ' + depot)
            raw = root / 'raw' / (depot.replace('\\', '/') + '.json')
            payload = raw.read_bytes()
            header = payload.split(b'\n  "Data":', 1)[0].decode('utf-8')
            version = re.search(r'"WolvenKitVersion":\s*"([^"]+)"', header).group(1)
            rows.append({'depot': depot, 'archive_relative': archive,
                         'serializer': 'native' if 'ghostline-red' in version else 'wolvenkit',
                         'serializer_header': version, 'header_prefix': header,
                         'binary_sha256': item['binary_sha256'], 'raw_sha256': item['raw_sha256']})
        args.freeze.parent.mkdir(parents=True, exist_ok=True)
        args.freeze.write_text(json.dumps({'schema_version': 1,
            'selection_note': 'All nonhistorical phase/scene/community resources in base and ep1 gamedata, plus recorded exact-path dependencies. Ep1 wins duplicate depot paths. Research selection, not installed archive precedence.',
            'resources': rows}, indent=2) + '\n', encoding='utf-8')
        print('Frozen', len(rows), 'resources')
        return
    schema = str(ensure_schema())
    wolvenkit = str(resolve_tool('wolvenkit'))
    files = sorted(p for p in (root / 'cr2w').rglob('*') if p.is_file())

    def convert(binary):
        rel = binary.relative_to(root / 'cr2w')
        raw = root / 'raw' / (rel.as_posix() + '.json')
        raw.parent.mkdir(parents=True, exist_ok=True)
        if raw.exists() and raw.stat().st_mtime >= binary.stat().st_mtime:
            return {'depot': str(rel), 'status': 'cached'}
        if args.reuse:
            old_binary = args.reuse / 'cr2w' / rel
            old_raw = args.reuse / 'raw' / (rel.as_posix() + '.json')
            if old_raw.exists() and old_binary.exists() and digest(old_binary) == digest(binary):
                shutil.copyfile(old_raw, raw)
                return {'depot': str(rel), 'status': 'reused-identical-payload'}
        result = subprocess.run([str(DEFAULT_RED_CLI), 'cr2w-serialize', str(binary), str(raw), '--schema', schema], capture_output=True)
        serializer = 'native'
        if result.returncode:
            serializer = 'wolvenkit'
            # A failed native conversion may leave an incomplete file.
            if raw.exists():
                raw.unlink()
            result = subprocess.run([wolvenkit, 'convert', 'serialize', str(binary), '-o', str(raw.parent), '-v', 'Minimal'], capture_output=True)
        return {'depot': str(rel), 'status': 'serialized' if result.returncode == 0 and raw.exists() else 'failed',
                'serializer': serializer, 'error': result.stderr.decode(errors='replace')[-600:] if result.returncode else ''}

    rows = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for row in pool.map(convert, files):
            rows.append(row)
            if len(rows) % 250 == 0 or row['status'] == 'failed':
                print(len(rows), '/', len(files), row['status'], flush=True)
    (root / 'serialization-report.json').write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
    failures = [r for r in rows if r['status'] == 'failed']
    print(json.dumps({'resources': len(rows), 'failures': failures}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
