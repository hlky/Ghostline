"""Freeze research provenance or compare deterministic generated artifacts."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def identity(path):
    return {'path': path.as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=Path('reference/quests/deep-dives/all-quests'))
    parser.add_argument('--docs', type=Path, default=Path('docs/reference/vanilla-quests/deep-dives'))
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--compare', type=Path)
    args = parser.parse_args()
    files = [p for p in args.data.rglob('*') if p.is_file() and
             p.name not in {'provenance.json', 'verification.json', 'analysis-verification.json', 'archive-selection-verification.json', 'regeneration-verification.json', 'replay-verification.json'}]
    files += list((args.docs / 'all-quests').rglob('*.md'))
    files += list((args.docs / 'implementation-families').rglob('*.md'))
    files += list(args.docs.glob('all-quest*.md'))
    files += [args.docs / 'ghostline-block-roadmap.md', args.docs / 'README.md']
    artifacts = [identity(p) for p in sorted(set(files))]
    if args.baseline:
        args.baseline.write_text(json.dumps({'artifacts': artifacts}, indent=2) + '\n', encoding='utf-8')
        print('Baseline', len(artifacts), 'artifacts')
        return
    if args.compare:
        before = {a['path']: a['sha256'] for a in json.loads(args.compare.read_text())['artifacts']}
        after = {a['path']: a['sha256'] for a in artifacts}
        changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
        report = {'status': 'passed' if not changed else 'failed', 'artifacts': len(after), 'changed': changed,
                  'scope': 'Regenerated full structural dossiers, connected-pattern/family analysis and performance appendices from the same frozen inputs.'}
        (args.data / 'regeneration-verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(report))
        if changed:
            raise SystemExit(1)
        return
    quests = json.loads((args.data / 'catalogue.json').read_text(encoding='utf-8'))['quests']
    resources = json.loads((args.data / 'resources.json').read_text(encoding='utf-8'))['resources']
    selection = json.loads((args.data / 'source-selection.json').read_text())['resources']
    analysis = json.loads((args.data / 'analysis-summary.json').read_text())
    performance = json.loads((args.data / 'performance-summary.json').read_text())
    names = ['build_quest_deep_dive_evidence', 'build_sidequest_catalogue', 'index_sidequest_corpus',
             'query_sidequest_evidence', 'collect_sidequest_evidence', 'prepare_quest_corpus',
             'close_quest_corpus', 'index_quest_archive_owners', 'analyze_quest_corpus',
             'index_quest_scene_performances', 'quest_research_facts', 'quest_research_cache', 'verify_sidequest_catalogue',
             'verify_quest_analysis', 'verify_quest_archive_selection', 'finalize_quest_research',
             'explore_questphase', 'explore_scene', 'cr2w_helpers', 'ghostline_red', 'toolchain']
    tools = [Path('tools') / (n + '.py') for n in names]
    tools += [Path('red-schema.json'), Path('red-schema.json.identity.json'),
              Path('tools/ghostline-red/target/release/ghostline-red.exe'), Path('H:/WolvenKit.Console-8.17.4/WolvenKit.CLI.exe')]
    for path in [args.data / n for n in ('verification.json', 'analysis-verification.json', 'archive-selection-verification.json', 'regeneration-verification.json', 'replay-verification.json')]:
        if path.exists():
            artifacts.append(identity(path))
    provenance = {'inspection_date': '2026-10-27',
        'scope': 'All 416 journal-export identities, every stored type, plus the indexed implementation families. Structural deep dives, manual synthesis and proposals; no installed runtime proof.',
        'repository_revision': subprocess.run(['git', 'rev-parse', 'HEAD'], check=True, capture_output=True, text=True).stdout.strip(),
        'python': sys.version, 'tools': [identity(p) for p in tools if p.exists()], 'artifacts': artifacts,
        'counts': {'quests': len(quests), 'quest_types': dict(Counter(q['quest_type'] for q in quests)),
                   'coverage': dict(Counter(q['status'] for q in quests)), 'resources': len(resources),
                   'archive_providers': dict(Counter(r['archive_relative'] for r in selection)),
                   'serializers': dict(Counter(r['serializer'] for r in selection)),
                   'quest_graphs': sum(r['phase_graphs'] for r in resources),
                   'quest_nodes': sum(r['phase_nodes'] for r in resources),
                   'scene_nodes': sum(r['scene_nodes'] for r in resources),
                   'connected_patterns': analysis['repeated_connected_patterns'],
                   'implementation_families': analysis['implementation_families'],
                   'direct_resource_bindings': analysis['direct_resource_identities'],
                   'performance_events': performance['events'], 'performance_event_types': len(performance['event_types'])},
        'boundaries': ['Explicit vanilla research archive selection; not mod/hotfix load-order simulation.',
                       'Generated structural dossiers and manually checked representative synthesis, not manual narrative/playthrough review of every journal identity.',
                       'Archive-index evidence for supporting assets is distinct from decoded graph/performance evidence.',
                       'No engine-default, reachability, save migration, world alias ownership or installed acceptance claim.']}
    (args.data / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(provenance['counts']))


if __name__ == '__main__':
    main()
