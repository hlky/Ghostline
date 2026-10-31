"""Verify every mined path and external port against checked source evidence."""
from collections import defaultdict
import argparse
import gzip
import hashlib
import json
from pathlib import Path

from analyze_quest_corpus import node_signature, normalized_edges
from build_sidequest_catalogue import node_rows
from quest_research_facts import fact_name, fact_role
from quest_research_cache import MINED_ARTIFACTS, mining_identity, sha


def load(path):
    payload = path.read_bytes()
    return json.loads(gzip.decompress(payload) if path.suffix == '.gz' else payload)


def edge_key(edge):
    return tuple(edge[k] for k in ('from', 'to', 'output', 'input'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    args = parser.parse_args()
    data = args.data
    patterns = load(data / 'connected-patterns.json.gz')['patterns']
    wanted = defaultdict(list)
    for key, pattern in patterns.items():
        signature = {k: pattern[k] for k in ('shape', 'node_types', 'edges')}
        assert hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()[:20] == key
        for use in pattern['occurrences']:
            wanted[use['depot']].append((pattern, use))
    uses_checked, ports_checked = 0, 0
    fact_checks = defaultdict(list)
    for fact, kinds in load(data / 'global-fact-dependencies.json.gz').items():
        for kind, uses in kinds.items():
            for use in uses:
                assert fact_name(use['data']) == fact
                assert kind == fact_role(use['data'])
                fact_checks[use['depot']].append(use)
    for shard in load(data / 'evidence-manifest.json')['shards']:
        for record in load(Path(shard['path']))['resources']:
            depot = record['depot']
            rows = list(node_rows(record))
            nodes = {(s, n): node for s, n, node, _ in rows}
            edges = {s: normalized_edges(s, es) for s, _, _, es in rows}
            edge_sets = {s: {edge_key(e) for e in es} for s, es in edges.items()}
            signatures = {}
            incoming = defaultdict(list)
            outgoing = defaultdict(list)
            for scope, es in edges.items():
                for edge in es:
                    incoming[(scope, edge['to'])].append(edge)
                    outgoing[(scope, edge['from'])].append(edge)
            for pattern, use in wanted.pop(depot, []):
                scope, ids = use['scope'], use['nodes']
                assert len(set(ids)) == 3
                for i, nid in enumerate(ids):
                    node = nodes[(scope, nid)]
                    assert node['pointer'] == use['pointers'][i]
                    if (scope, nid) not in signatures:
                        signatures[(scope, nid)] = node_signature(node['data'])
                    assert signatures[(scope, nid)] == pattern['node_types'][i]
                for edge in pattern['edges']:
                    actual = (ids[edge['from']], ids[edge['to']], edge['output'], edge['input'])
                    assert actual in edge_sets[scope]
                actual_ports = {edge_key(e) for n in ids for e in incoming[(scope, n)] + outgoing[(scope, n)]
                                if (e['from'] in ids) != (e['to'] in ids)}
                assert actual_ports == {edge_key(e) for e in use['boundary']}
                ports_checked += len(actual_ports)
                uses_checked += 1
            facts_by_pointer = {f['pointer']: f['data'] for f in record['fact_uses']}
            for use in fact_checks.pop(depot, []):
                assert facts_by_pointer[use['pointer']] == use['data']
                owner = nodes[(use['scope'], use['node'])]
                assert use['pointer'].startswith(owner['pointer'] + '/')
    assert not wanted and not fact_checks
    quests = load(data / 'catalogue.json')['quests']
    analysis = load(data / 'quest-analysis.json.gz')['quests']
    assert {q['journal_path'] for q in quests} == {q['journal_path'] for q in analysis}
    by_quest = {q['journal_path']: q for q in quests}
    for item in analysis:
        quest = by_quest[item['journal_path']]
        scopes = quest.get('anchor_graph_scopes', {})
        selected_nodes = quest.get('anchor_node_selection', {})
        for key, uses in item['patterns'].items():
            for use in uses:
                assert use['depot'] in quest['scope_resources']
                assert use['depot'] not in scopes or use['scope'] in scopes[use['depot']]
                assert use['depot'] not in selected_nodes or all(n in selected_nodes[use['depot']].get(use['scope'], []) for n in use['nodes'])
    report = {'status': 'passed', 'quests': len(quests), 'patterns': len(patterns),
              'connected_occurrences_checked': uses_checked, 'external_ports_checked': ports_checked,
              'checks': 'Typed paths, exact sockets, source pointers, full boundary ports, fact ownership and quest graph scope'}
    (data / 'analysis-verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    resources = load(data / 'resources.json')['resources']
    receipt = {'input_identity': mining_identity(data, resources),
               'artifacts': {name: sha(data / name) for name in MINED_ARTIFACTS},
               'node_types': load(data / 'analysis-summary.json')['node_types'],
               'verification': 'Every mined occurrence, boundary port and classified fact use checked against source evidence.'}
    (data / 'verified-mining-cache.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
