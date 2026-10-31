"""Follow every current graph-resource reference using recorded archive indexes."""
from concurrent.futures import ThreadPoolExecutor
import argparse
from collections import defaultdict
import json
from pathlib import Path
import subprocess

from analyze_quest_corpus import resource_hash
from build_quest_deep_dive_evidence import walk
from ghostline_red import DEFAULT_RED_CLI, ensure_schema
from toolchain import resolve_tool


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scratch', type=Path, required=True)
    args = parser.parse_args()
    root = args.scratch
    game = resolve_tool('game')
    schema, wolvenkit = str(ensure_schema()), str(resolve_tool('wolvenkit'))
    owners = defaultdict(list)
    for path in sorted((root / 'archive-indexes').glob('*.json')):
        data = json.loads(path.read_text())
        for entry in data['entries']:
            owners[entry['name_hash']].append(data['archive_relative'])
    def priority(path):
        return (0 if path == 'ep1/ep1_2_gamedata.archive' else
                1 if path == 'content/basegame_4_gamedata.archive' else 2, path)
    index = json.loads((root / 'indexed/index.json').read_text())['resources']
    available = {r['depot'] for r in index if r['status'] != 'failed'}
    pending = {d for r in index if r['status'] != 'failed' for d in r['graph_resources']}
    historical = {p for p in pending if '\\versions\\' in p}
    pending -= historical | available
    visited, receipts, origins = set(), [], {}
    def visit(depot):
        providers = sorted(owners.get(resource_hash(depot), []), key=priority)
        if not providers:
            return {'depot': depot, 'status': 'no archive-index match'}, set()
        archive = providers[0]
        binary = root / 'cr2w' / depot.replace('\\', '/')
        result = subprocess.run([str(DEFAULT_RED_CLI), 'extract', str(game / 'archive/pc' / archive),
                                 '--output', str(root / 'cr2w'), '--path', depot], capture_output=True)
        if result.returncode or not binary.exists():
            return {'depot': depot, 'status': 'extraction failed', 'archive_relative': archive,
                    'error': result.stderr.decode(errors='replace')[-600:]}, set()
        raw = root / 'raw' / (depot.replace('\\', '/') + '.json')
        raw.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run([str(DEFAULT_RED_CLI), 'cr2w-serialize', str(binary), str(raw), '--schema', schema], capture_output=True)
        serializer = 'native'
        if result.returncode:
            serializer = 'wolvenkit'
            if raw.exists():
                raw.unlink()
            result = subprocess.run([wolvenkit, 'convert', 'serialize', str(binary), '-o', str(raw.parent), '-v', 'Minimal'], capture_output=True)
        if result.returncode or not raw.exists():
            return {'depot': depot, 'status': 'serialization failed', 'archive_relative': archive,
                    'error': result.stderr.decode(errors='replace')[-600:]}, set()
        doc = json.loads(raw.read_text(encoding='utf-8-sig'))
        refs = {v['$value'] for _, v in walk(doc) if isinstance(v, dict) and v.get('$type') == 'ResourcePath'
                and isinstance(v.get('$value'), str) and v['$value'].endswith(('.questphase', '.quest', '.gamedef', '.scene', '.community'))}
        return {'depot': depot, 'status': 'resolved', 'archive_relative': archive, 'serializer': serializer}, refs
    with ThreadPoolExecutor(max_workers=4) as pool:
        while pending:
            batch = sorted(pending - visited - available)
            pending = set()
            if not batch:
                break
            visited.update(batch)
            for receipt, refs in pool.map(visit, batch):
                receipts.append(receipt)
                if receipt['status'] == 'resolved':
                    available.add(receipt['depot'])
                    origins[receipt['depot']] = receipt['archive_relative']
                historical.update(p for p in refs if '\\versions\\' in p)
                pending.update(p for p in refs if '\\versions\\' not in p)
            print('Visited', len(visited), 'resolved', len(origins), 'next', len(pending - available - visited), flush=True)
    # Merge origin receipts to preserve provenance on resumed runs.
    target = root / 'extra-origins.json'
    previous = json.loads(target.read_text()) if target.exists() else {}
    previous.update(origins)
    target.write_text(json.dumps(previous, indent=2) + '\n', encoding='utf-8')
    (root / 'closure-report.json').write_text(json.dumps({'resources': receipts, 'historical_references': sorted(historical)}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'resolved': len(origins), 'unresolved': [r for r in receipts if r['status'] != 'resolved']}))


if __name__ == '__main__':
    main()
