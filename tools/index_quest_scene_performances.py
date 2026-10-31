"""Preserve scene section events, timing and bindings as queryable evidence."""
from collections import Counter, defaultdict
from dataclasses import asdict
import argparse
import hashlib
import json
from pathlib import Path

from build_quest_deep_dive_evidence import compact, pointer
from build_sidequest_catalogue import dump, esc, packed
from explore_scene import SceneExplorer


def resolve(document, path):
    value = document
    for part in path.split('/')[1:]:
        key = part.replace('~1', '/').replace('~0', '~')
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--docs', type=Path, required=True)
    parser.add_argument('--raw-root', type=Path, required=True)
    parser.add_argument('--extract-only', action='store_true')
    parser.add_argument('--append-only', action='store_true')
    args = parser.parse_args()
    if args.append_only:
        summaries = json.loads((args.data / 'performance-summary.json').read_text(encoding='utf-8'))['resources']
        append_dossiers(args, summaries)
        return
    resources = json.loads((args.data / 'resources.json').read_text(encoding='utf-8'))['resources']
    groups, summaries, all_types = defaultdict(list), {}, Counter()
    event_count = 0
    for meta in resources:
        depot = meta['depot']
        if not depot.endswith('.scene'):
            continue
        raw = args.raw_root / (depot.replace('\\', '/') + '.json')
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == meta['raw_sha256']
        explorer = SceneExplorer(raw)
        events = []
        speech = {(e.node_id, e.handle): asdict(e) for e in explorer.events()}
        for node in explorer.graph_nodes:
            node_data = explorer.resolve_data(node)
            if not isinstance(node_data, dict):
                continue
            nid = str(node_data.get('nodeId', {}).get('id', ''))
            for event in node_data.get('events', []):
                if not isinstance(event, dict):
                    continue
                handle = str(event.get('HandleId', event.get('HandleRefId', '')))
                data = explorer.resolve_data(event)
                if not isinstance(data, dict):
                    continue
                source_pointer = pointer(explorer.handle_paths[handle])
                assert resolve(explorer.data, source_pointer).get('Data') == data
                events.append({'node': nid, 'handle': handle, 'pointer': source_pointer,
                               'data': compact(data, explorer), 'timeline': speech.get((nid, handle), {})})
        types = Counter(event['data'].get('$type', 'unknown') for event in events)
        all_types.update(types)
        event_count += len(events)
        record = {'depot': depot, 'raw_sha256': meta['raw_sha256'], 'binary_sha256': meta['binary_sha256'],
                  'events': events,
                  'screenplay_lines': compact(explorer.root_chunk.get('screenplayStore', {}).get('lines', []), explorer),
                  'interruption_scenarios': compact(explorer.root_chunk.get('interruptionScenarios', []), explorer)}
        groups[meta['family']].append(record)
        summaries[depot] = {'events': len(events), 'types': dict(sorted(types.items())),
                            'event_nodes': len({e['node'] for e in events}), 'family': meta['family']}
        if len(summaries) % 100 == 0:
            print('Scenes', len(summaries), 'events', event_count, flush=True)
    manifest = []
    for family, records in sorted(groups.items()):
        target = args.data / 'performances' / (family + '.json.gz')
        packed(target, {'family': family, 'scenes': records})
        manifest.append({'family': family, 'path': target.as_posix(), 'scenes': len(records),
                         'events': sum(len(r['events']) for r in records),
                         'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    dump(args.data / 'performance-manifest.json', {'shards': manifest})
    dump(args.data / 'performance-summary.json', {'scenes': len(summaries), 'events': event_count,
        'event_types': dict(all_types.most_common()), 'resources': summaries,
        'verification': 'All source hashes and event handle pointers checked against raw Data; not runtime timing proof.'})
    if not args.extract_only:
        append_dossiers(args, summaries)
    print(json.dumps({'scenes': len(summaries), 'events': event_count, 'event_types': len(all_types), 'shards': len(manifest)}))


def append_dossiers(args, summaries):
    quests = json.loads((args.data / 'catalogue.json').read_text(encoding='utf-8'))['quests']
    for quest in quests:
        scenes = [d for d in quest['scope_resources'] if d in summaries]
        path = args.docs / quest['document']
        original = path.read_text(encoding='utf-8').split('\n## Scene performance events\n')[0].rstrip()
        lines = ['', '## Scene performance events', '',
            'Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. '
            'Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. '
            'Animation/voice payloads and installed timing are not validated by this extraction.', '',
            '| Scene | Event sections / events | Stored event types |', '| --- | --- | --- |']
        for scene in scenes:
            info = summaries[scene]
            types = '; '.join(t + ': ' + str(n) for t, n in info['types'].items())
            lines.append(f"| `{scene}` | {info['event_nodes']} / {info['events']} | {esc(types)} |")
        if not scenes:
            lines.append('| No resolved scene in this quest context | — | No performance inference |')
        lines += ['', 'Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests '
                  '--quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or '
                  '`--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.', '']
        path.write_text(original + '\n' + '\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    main()
