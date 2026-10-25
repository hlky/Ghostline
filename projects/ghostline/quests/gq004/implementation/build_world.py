"""Build and verify the isolated GQ004 world without registering it in game."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
sys.path.insert(0, str(ROOT / 'tools'))
from cr2w_validation import compare_documents
from generate_world import build_world
from toolchain import resolve_tool

PREVIEW = ROOT / 'projects/ghostline/generated/love-actually-preview'


def verify_document(expected: dict, actual: dict, schema: dict) -> dict:
    expected = copy.deepcopy(expected)
    root = expected['Data']['RootChunk']
    # WKit reads the custom .devices buffer directly, dropping its JSON buffer envelope.
    if root.get('$type') == 'gameDeviceResource' and isinstance(root.get('data', {}).get('Data'), dict):
        root['data'] = root['data']['Data']
    comparison = compare_documents(expected, actual, schema=schema, fresh_wolvenkit_defaults=actual)
    # Verify every authored field. Reader-added constructor defaults are reported,
    # not treated as authored data or as a guarantee of engine behaviour.
    errors = [error for error in comparison.errors if error.get('expected') != '<missing>']
    return dict(ok=not errors, errors=errors,
                reader_added_fields=[error['path'] for error in comparison.errors if error.get('expected') == '<missing>'],
                normalized_values=len(comparison.normalizations))


def compile_world(output: Path = PREVIEW, verify_only: bool = False) -> dict:
    spec_path = HERE / 'world/love-actually.world.json'
    raw = output / 'source/raw'
    archive = output / 'source/archive'
    files = build_world(json.loads(spec_path.read_text(encoding='utf-8')), raw, archive)
    readback = output / 'world-readback'
    readback.mkdir(parents=True, exist_ok=True)
    if not verify_only:
        writer = resolve_tool('wolvenkit')
        archive.joinpath('mod/gq004/world').mkdir(parents=True, exist_ok=True)
        for mode, source, target in (
            ('-d', raw / 'mod/gq004/world', archive / 'mod/gq004/world'),
            ('-s', archive / 'mod/gq004/world', readback),
        ):
            subprocess.run([str(writer), 'cr2w', str(source), mode, '-o', str(target), '-v', 'Minimal'], cwd=ROOT, check=True)
    schema = json.loads((ROOT / 'red-schema.json').read_text(encoding='utf-8'))
    results = []
    for item in files:
        if item.archive_path.read_bytes()[:4] != b'CR2W':
            raise ValueError(f'Invalid CR2W signature: {item.archive_path}')
        result = verify_document(json.loads(item.raw_path.read_text(encoding='utf-8')),
                                 json.loads((readback / item.raw_path.name).read_text(encoding='utf-8')), schema)
        result.update(resource=item.depot_path, sha256=hashlib.sha256(item.archive_path.read_bytes()).hexdigest())
        results.append(result)
    report = dict(ok=all(row['ok'] for row in results), registered=False, resources=results,
                  validation='All authored fields, array lengths, types and reflected float32 values; reader-added defaults listed separately. Runtime behaviour not established.')
    (output / 'world-validation.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    report = compile_world(verify_only=parser.parse_args().verify_only)
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['ok'] else 1)
