"""Verify selected depot paths and payloads against their archive index entries."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from analyze_quest_corpus import resource_hash


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    args = parser.parse_args()
    inventories = {}
    for path in (args.scratch / 'archive-indexes').glob('*.json'):
        data = json.loads(path.read_text())
        inventories[data['archive_relative']] = {r['name_hash']: r for r in data['entries']}
    rows = json.loads((args.data / 'source-selection.json').read_text())['resources']
    providers = Counter()
    for row in rows:
        archive = row['archive_relative']
        entry = inventories[archive][resource_hash(row['depot'])]
        payload = (args.scratch / 'cr2w' / row['depot'].replace('\\', '/')).read_bytes()
        assert hashlib.sha1(payload).hexdigest() == entry['sha1'], 'Archive payload mismatch: ' + row['depot']
        assert hashlib.sha256(payload).hexdigest() == row['binary_sha256']
        assert len(payload) == entry['size']
        providers[archive] += 1
    report = {'status': 'passed', 'selected_payloads': len(rows), 'providers': dict(sorted(providers.items())),
              'checks': 'Exact normalized depot FNV64, archive entry size/SHA1, extracted payload SHA256'}
    (args.data / 'archive-selection-verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
