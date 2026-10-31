"""Mine connected quest patterns and dependency bindings from checked evidence.

Patterns are exact typed, socket-labelled, three-node paths, not behavioral
equivalence proofs. Full occurrences preserve graph namespaces and boundaries.
The generated supplements distinguish quest scopes from shared context.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from build_sidequest_catalogue import dump, esc, node_rows, packed, values
from quest_research_facts import fact_name, fact_role
from quest_research_cache import MINED_ARTIFACTS, mining_identity, sha


def resource_hash(path):
    value = 0xCBF29CE484222325
    for byte in path.replace('/', '\\').casefold().encode('utf-8'):
        value = ((value ^ byte) * 0x100000001B3) & 0xffffffffffffffff
    return value


def node_signature(data):
    core = data.get('questNode', data)
    root = core.get('$type', '')
    nested = sorted(set(t for t in values(core, '$type') if t != root and
                        t.startswith(('quest', 'scn'))))
    return root + ('[' + ','.join(nested) + ']' if nested else '')


def normalized_edges(scope, edges):
    if scope == 'scene':
        return [{'from': e['source_node'], 'to': e['destination_node'],
                 'output': e['source_socket'], 'input': e['destination_socket']} for e in edges]
    return edges


def purpose(path):
    extension = Path(path).suffix.casefold()
    return {'.questphase': 'phase flow', '.quest': 'quest root flow', '.gamedef': 'launch definition', '.scene': 'scene flow', '.community': 'spawn/schedule',
            '.ent': 'entity/controller binding', '.app': 'appearance binding',
            '.workspot': 'performance binding', '.animset': 'animation binding',
            '.streamingblock': 'world streaming', '.streamingsector': 'world node definitions',
            '.prefab': 'world composition', '.journal': 'journal content',
            '.json': 'typed JSON/localization resource', '.wem': 'voice/audio',
            '.inkwidget': 'UI', '.inkanim': 'UI animation'}.get(extension, 'asset binding ' + extension)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--docs', type=Path, required=True)
    parser.add_argument('--archive-indexes', type=Path, required=True)
    parser.add_argument('--reuse-mined', action='store_true', help='Reuse independently verified global mining results after source identity checks')
    args = parser.parse_args()
    quests = json.loads((args.data / 'catalogue.json').read_text(encoding='utf-8'))['quests']
    metadata = {r['depot']: r for r in json.loads((args.data / 'resources.json').read_text(encoding='utf-8'))['resources']}
    owners = defaultdict(list)
    inventory_receipts = []
    for path in sorted(args.archive_indexes.glob('*.json')):
        inventory = json.loads(path.read_text(encoding='utf-8'))
        relative = inventory['archive_relative']
        inventory_receipts.append({'archive_relative': relative, 'archive_size': inventory['archive_size'],
                                   'archive_mtime_ns': inventory['archive_mtime_ns'],
                                   'entries': len(inventory['entries']),
                                   'inventory_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        for entry in inventory['entries']:
            owners[entry['name_hash']].append({'archive': relative, 'size': entry['size'], 'archive_sha1': entry['sha1']})
    summaries = {}
    patterns = {}
    occurrences = defaultdict(list)
    global_facts = defaultdict(lambda: {'writers': [], 'readers': [], 'other_uses': []})
    all_types = Counter()
    embedded = []
    launch_definitions = []
    if args.reuse_mined:
        receipt = json.loads((args.data / 'verified-mining-cache.json').read_text())
        assert receipt['input_identity'] == mining_identity(args.data, metadata.values()), 'Mining inputs changed'
        assert all(sha(args.data / name) == receipt['artifacts'][name] for name in MINED_ARTIFACTS), 'Mined evidence changed'
        def unpack(name):
            return json.loads(gzip.decompress((args.data / name).read_bytes()))
        summaries = unpack('resource-binding-dependencies.json.gz')
        global_facts = unpack('global-fact-dependencies.json.gz')
        all_types = Counter(receipt['node_types'])
        embedded = json.loads((args.data / 'embedded-handoffs.json').read_text())['handoffs']
        launch_definitions = json.loads((args.data / 'launch-definitions.json').read_text())['definitions']
    for shard in ([] if args.reuse_mined else json.loads((args.data / 'evidence-manifest.json').read_text())['shards']):
        records = json.loads(gzip.decompress(Path(shard['path']).read_bytes()))['resources']
        for record in records:
            depot = record['depot']
            rows = list(node_rows(record))
            by_scope = defaultdict(list)
            facts = defaultdict(lambda: {'writers': [], 'readers': [], 'other_uses': []})
            node_owners = {node['pointer']: (scope, nid) for scope, nid, node, _ in rows}
            def pointer_owner(pointer):
                prefix = pointer
                while '/' in prefix:
                    prefix = prefix.rsplit('/', 1)[0]
                    if prefix in node_owners:
                        return node_owners[prefix]
                return None
            for scope, nid, node, edges in rows:
                by_scope[scope].append((nid, node, edges))
                all_types.update(values(node['data'], '$type'))
            for fact in record['fact_uses']:
                # Resolve the nearest containing graph node. Do not attribute
                # an embedded child's facts to its enclosing phase node.
                owner = pointer_owner(fact['pointer'])
                if owner is None:
                    continue
                scope, nid = owner
                data = fact['data']
                name = fact_name(data)
                if not name:
                    continue
                kind = fact_role(data)
                use = {'depot': depot, 'scope': scope, 'node': nid, 'pointer': fact['pointer'], 'data': data}
                facts[name][kind].append(use)
                global_facts[name][kind].append(use)
            for graph in record.get('graphs', []):
                candidates = [(s, n, node) for s, n, node, _ in rows if graph['pointer'].startswith(node['pointer'] + '/')]
                if candidates:
                    s, n, owner = max(candidates, key=lambda row: len(row[2]['pointer']))
                    interface = [node['data'] for node in graph['nodes'] if node['data'].get('$type') in
                                 {'questInputNodeDefinition', 'questOutputNodeDefinition'}]
                    embedded.append({'depot': depot, 'parent_scope': s, 'parent_node': n,
                                     'child_scope': 'h' + graph['handle'], 'pointer': graph['pointer'], 'interface': interface})
            annotated = []
            for ref in record['references']:
                owner = pointer_owner(ref['pointer'])
                annotated.append({**ref, **({'scope': owner[0], 'node': owner[1]} if owner else {})})
            refs = [r for r in annotated if r['kind'] == 'ResourcePath']
            if 'launch_definition' in record:
                launch_definitions.append({'depot': depot, 'role': metadata[depot]['role'],
                                           'definition': record['launch_definition'], 'references': refs})
            summaries[depot] = {'references': refs, 'facts': dict(facts),
                                 'node_types': dict(Counter(node_signature(node['data']) for _, _, node, _ in rows)),
                                 'graph_counts': {'quest': len(record.get('graphs', [])), 'scene_nodes': len(record.get('nodes', []))},
                                 'noderefs': [r for r in annotated if r['kind'] == 'NodeRef'],
                                 'tweakdb': [r for r in annotated if r['kind'] == 'TweakDBID']}
            for scope, nodes in by_scope.items():
                lookup = {nid: node for nid, node, _ in nodes}
                edges = normalized_edges(scope, nodes[0][2])
                incoming, outgoing = defaultdict(list), defaultdict(list)
                for edge in edges:
                    incoming[edge['to']].append(edge)
                    outgoing[edge['from']].append(edge)
                signatures = {n: node_signature(node['data']) for n, node in lookup.items()}
                for mid in sorted(lookup):
                    for first, second in itertools.product(incoming[mid], outgoing[mid]):
                        ids = [first['from'], mid, second['to']]
                        if len(set(ids)) != 3:
                            continue
                        signature = {'shape': 'path2', 'node_types': [signatures[n] for n in ids],
                                     'edges': [{'from': 0, 'to': 1, 'output': first['output'], 'input': first['input']},
                                               {'from': 1, 'to': 2, 'output': second['output'], 'input': second['input']}]}
                        key = hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()[:20]
                        patterns[key] = signature
                        boundary = {tuple(e.items()): e for n in ids for e in incoming[n] + outgoing[n]
                                    if (e['from'] in ids) != (e['to'] in ids)}
                        occurrences[key].append({'depot': depot, 'scope': scope, 'nodes': ids,
                            'pointers': [lookup[n]['pointer'] for n in ids],
                            'boundary': list(boundary.values())})
        print('Analyzed', len(summaries), '/', len(metadata), flush=True)
    selected = unpack('connected-patterns.json.gz')['patterns'] if args.reuse_mined else {}
    for key, uses in occurrences.items():
        resources = {u['depot'] for u in uses}
        if len(resources) < 2:
            continue
        types = patterns[key]['node_types']
        if not any('[' in typ or typ.startswith(('scnChoice', 'scnRewindable', 'questScene', 'questLogicalAnd', 'questCutControl')) for typ in types):
            continue
        selected[key] = {**patterns[key], 'occurrences': uses, 'distinct_resources': len(resources),
                         'distinct_families': len({metadata[d]['family'] for d in resources}),
                         'resource_roles': dict(Counter(metadata[u['depot']]['role'] for u in uses))}
    packed(args.data / 'connected-patterns.json.gz', {'method': 'Exact three-node directed paths, typed nodes and labelled sockets; all external edges retained. No semantic/runtime equivalence claim.',
                                                     'patterns': dict(sorted(selected.items()))})
    packed(args.data / 'global-fact-dependencies.json.gz', dict(sorted(global_facts.items())))
    packed(args.data / 'resource-binding-dependencies.json.gz', summaries)
    dump(args.data / 'embedded-handoffs.json', {'handoffs': embedded})
    dump(args.data / 'launch-definitions.json', {'definitions': launch_definitions})
    dump(args.data / 'archive-inventories.json', {'note': 'All matching vanilla provider indexes; not load order. SHA1 is stored archive metadata, not a newly computed payload hash.', 'archives': inventory_receipts})
    direct = sorted({r['value'] for s in summaries.values() for r in s['references'] if isinstance(r['value'], str)})
    ownership = {path: {'purpose': purpose(path), 'providers': owners.get(resource_hash(path), []),
                        'structurally_indexed': path in metadata} for path in direct}
    packed(args.data / 'dependency-ownership.json.gz', ownership)
    # Free archive tables and rejected paths before building per-quest reports.
    del owners, occurrences, patterns
    by_depot = defaultdict(list)
    for key, pattern in selected.items():
        for occurrence in pattern['occurrences']:
            by_depot[occurrence['depot']].append((key, occurrence))
    families = defaultdict(list)
    for depot, meta in metadata.items():
        families[meta['family']].append(depot)
    anchor_families = {metadata[n['depot']]['family'] for quest in quests for n in quest['anchor_nodes']}
    family_docs = args.docs.parent / 'implementation-families'
    family_docs.mkdir(parents=True, exist_ok=True)
    family_index = ['# Implementation families beyond the journal inventory', '',
        'This indexes every extracted resource family, including ambient, shared, test, repair and unjournaled implementations. '
        'A family is a depot grouping, not necessarily one playable quest. Exact journal attribution stays in the 416-entry catalogue.', '',
        '| Family | Resources | Exact journal anchor in export |', '| --- | --- | --- |']
    for family, depots in sorted(families.items()):
        lines = [f'# {family}', '',
            'Depot-family structural inventory. Resources can be shared or belong to test/repair paths. '
            'No playable-quest identity or runtime reachability is inferred from the directory.', '',
            '| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |', '| --- | --- | --- | --- |']
        types = Counter()
        for depot in sorted(depots):
            counts = summaries[depot]['graph_counts']
            types.update(summaries[depot]['node_types'])
            calls = '; '.join(metadata[depot].get('call_resources', []))
            lines.append(f"| `{depot}` | {metadata[depot]['role']} | {counts['quest']} / {counts['scene_nodes']} | {esc(calls)} |")
        lines += ['', '## Journal paths observed in these resources', '']
        journal_paths = sorted({p for d in depots for p in metadata[d]['journal_paths']})
        lines += ['- `' + p + '`' for p in journal_paths] or ['No stored journal path in this family.']
        lines += ['', '## Stored mechanisms', '', '| Type signature | Nodes |', '| --- | --- |']
        lines += [f'| `{esc(t)}` | {count} |' for t, count in sorted(types.items())]
        lines += ['', '## Recurrent connected paths', '', '| Signature | Occurrences in family | Example |', '| --- | --- | --- |']
        uses = defaultdict(list)
        for depot in depots:
            for key, use in by_depot[depot]:
                uses[key].append(use)
        for key in sorted(uses, key=lambda k: (-len(uses[k]), k))[:20]:
            example = uses[key][0]
            lines.append(f"| `{key}` | {len(uses[key])} | `{example['depot']}` / {example['scope']} / {' -> '.join(example['nodes'])} |")
        lines += ['', 'Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. '
            'See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).', '']
        (family_docs / (family + '.md')).write_text('\n'.join(lines), encoding='utf-8')
        family_index.append(f"| [{family}]({family}.md) | {len(depots)} | {'yes' if family in anchor_families else 'no; dependency or unresolved/unjournaled context'} |")
    (family_docs / 'README.md').write_text('\n'.join(family_index) + '\n', encoding='utf-8')
    per_quest = []
    overview = ['# Connected patterns and dependency findings', '',
        'Every catalogue entry receives a supplement below. Exact three-node paths are structural candidates, not complete lifecycle templates. '
        'Instances include ordinary, shared, test and repair context, with path roles preserved. '
        'Bindings remain concrete in evidence; matching type/socket shapes does not prove matching behavior.', '',
        '## Quest coverage', '', '| Quest | Stored type | Source-backed paths / bindings |', '| --- | --- | --- |']
    for quest in quests:
        scope_resources = quest['scope_resources']
        scope_rules = quest.get('anchor_graph_scopes', {})
        node_rules = quest.get('anchor_node_selection', {})
        found = defaultdict(list)
        for depot in scope_resources:
            for key, use in by_depot[depot]:
                if depot in scope_rules and use['scope'] not in scope_rules[depot]:
                    continue
                if depot in node_rules and not all(n in node_rules[depot].get(use['scope'], []) for n in use['nodes']):
                    continue
                found[key].append(use)
        ranked = sorted(found, key=lambda k: (-selected[k]['distinct_families'], -selected[k]['distinct_resources'], k))
        examples = []
        seen_shapes = set()
        for key in ranked:
            shape = tuple(selected[key]['node_types'])
            if shape not in seen_shapes:
                examples.append(key)
                seen_shapes.add(shape)
            if len(examples) == 12:
                break
        def in_scope(depot, ref):
            if depot in scope_rules and 'scope' in ref and ref['scope'] not in scope_rules[depot]:
                return False
            return depot not in node_rules or 'node' not in ref or ref['node'] in node_rules[depot].get(ref['scope'], [])
        bindings = sorted({r['value'] for d in scope_resources for r in summaries[d]['references']
                           if isinstance(r['value'], str) and in_scope(d, r)})
        fact_names = sorted({f for d in scope_resources for f, kinds in summaries[d]['facts'].items()
                             if any(in_scope(d, use) for uses in kinds.values() for use in uses)})
        external_facts = []
        scope_set = set(scope_resources)
        for fact in fact_names:
            producers = [u for u in global_facts[fact]['writers'] if u['depot'] not in scope_set or not in_scope(u['depot'], u)]
            if producers:
                external_facts.append({'fact': fact, 'external_writers': producers})
        bridges = [h for h in embedded if h['depot'] in scope_set and
                   (h['depot'] not in scope_rules or h['parent_scope'] in scope_rules[h['depot']]) and
                   (h['depot'] not in node_rules or h['parent_node'] in node_rules[h['depot']].get(h['parent_scope'], []))]
        ancestor_resources = scope_set | set(quest.get('parent_context_resources', []))
        launches = [definition for definition in launch_definitions
                    if any(ref['value'] in ancestor_resources for ref in definition['references'])]
        item = {'journal_path': quest['journal_path'], 'quest_type': quest['quest_type'],
                'patterns': {k: found[k] for k in ranked}, 'direct_bindings': bindings,
                'external_fact_producers': external_facts, 'embedded_handoffs': bridges,
                'launch_definitions': [definition['depot'] for definition in launches],
                'noderef_count': sum(in_scope(d, r) for d in scope_resources for r in summaries[d]['noderefs']),
                'tweakdb_count': sum(in_scope(d, r) for d in scope_resources for r in summaries[d]['tweakdb'])}
        per_quest.append(item)
        path = args.docs / quest['document']
        original = path.read_text(encoding='utf-8').split('\n## Connected paths and supporting bindings\n')[0].rstrip()
        original = original.replace('Readers/conditions in context', 'Readers and other fact bindings in context')
        if quest['status'].startswith('POI-linked'):
            original = original.replace('exact journal-linked nodes', 'exact POI-linked nodes')
        lines = ['', '## Connected paths and supporting bindings', '',
            f'{len(found)} repeated typed/socket path signatures in this selected graph context; '
            f'{len(bindings)} distinct direct resource identities; {len(bridges)} embedded graph handoffs. '
            'The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. '
            'Shared forward dependencies can serve several quests; these are context counts.', '',
            '### Connected block candidates', '',
            'These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, '
            'not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.', '',
            '| Pattern | Actual occurrence | Typed path and bound sockets |', '| --- | --- | --- |']
        for key in examples:
            pattern = selected[key]
            use = found[key][0]
            types = ' -> '.join(pattern['node_types'])
            sockets = '; '.join(e['output'] + ' -> ' + e['input'] for e in pattern['edges'])
            lines.append(f"| `{key}` | `{use['depot']}` / {use['scope']} / {' -> '.join(use['nodes'])} | {esc(types)}; {esc(sockets)} |")
        if not ranked:
            lines.append('| No recurrent path attributed | Missing attribution or no matching signature | Do not infer a lifecycle from the title |')
        lines += ['', '### Embedded phase interfaces', '', '| Owning node | Child graph | Authored interface |', '| --- | --- | --- |']
        for bridge in bridges:
            lines.append(f"| `{bridge['depot']}` / {bridge['parent_scope']} / {bridge['parent_node']} | `{bridge['child_scope']}` | {esc(json.dumps(bridge['interface'], ensure_ascii=False, separators=(',', ':')))} |")
        if not bridges:
            lines.append('| No embedded handoff in resolved context | — | External calls remain in the main dossier |')
        lines += ['', '### Launch definition context', '',
            'These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; '
            'their presence does not establish that the installed game selects them.', '',
            '| Definition | Path role | Referenced context |', '| --- | --- | --- |']
        for definition in launches:
            refs = '; '.join(ref['value'] for ref in definition['references'] if ref['value'] in ancestor_resources)
            lines.append(f"| `{definition['depot']}` | {definition['role']} | {esc(refs)} |")
        if not launches:
            lines.append('| No direct launch-definition reference to this resolved context | Unresolved activation ownership | — |')
        lines += ['', '### Supporting resource ownership', '',
            'Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, '
            'not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; '
            'other bindings require their own controller, world, performance or localization validation.', '',
            '| Resource | Binding role | Providers / inspection |', '| --- | --- | --- |']
        for binding in bindings:
            info = ownership[binding]
            providers = '; '.join(p['archive'] for p in info['providers']) or 'No match in inspected vanilla indexes'
            lines.append(f"| `{binding}` | {info['purpose']} | {esc(providers)}; {'structurally indexed' if info['structurally_indexed'] else 'index evidence only'} |")
        if not bindings:
            lines.append('| No attributed direct resource binding | Attribution unresolved | — |')
        lines += ['', '### Fact producers outside the forward context', '',
            'These are indexed writer locations, not proof that they execute before this quest. '
            'Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.', '',
            '| Fact | External writer examples |', '| --- | --- |']
        for fact in external_facts:
            samples = fact['external_writers'][:4]
            locations = '; '.join(u['depot'] + ' / ' + u['scope'] + ' / ' + u['node'] for u in samples)
            lines.append(f"| `{fact['fact']}` | {esc(locations)}; {len(fact['external_writers'])} total source locations in compressed evidence |")
        if not external_facts:
            lines.append('| No external graph writer located | External engine/device/script production remains possible |')
        lines += ['', f"NodeRef uses: {item['noderef_count']}; TweakDB binding uses: {item['tweakdb_count']}. "
            'Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; '
            'numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.', '']
        path.write_text(original + '\n' + '\n'.join(lines), encoding='utf-8')
        overview.append(f"| [{esc(quest['title'])}](all-quests/{quest['document']}) | {quest['quest_type']} | {len(found)} / {len(bindings)} |")
    packed(args.data / 'quest-analysis.json.gz', {'quests': per_quest})
    overview += ['', '## Broadly recurring connected paths', '', '| Signature | Path | Resources / families |', '| --- | --- | --- |']
    top = sorted(selected, key=lambda k: (-selected[k]['distinct_families'], -selected[k]['distinct_resources'], k))[:60]
    for key in top:
        pattern = selected[key]
        overview.append(f"| `{key}` | {esc(' -> '.join(pattern['node_types']))} | {pattern['distinct_resources']} / {pattern['distinct_families']} |")
    (args.docs.parent / 'all-quest-findings.md').write_text('\n'.join(overview) + '\n', encoding='utf-8')
    gaps = ['# Coverage and unresolved attribution', '',
        'All exported identities have a dossier. Journal links, POI associations and missing attribution are separate evidence states. '
        'A journal-linked deactivation or repair operation does not establish an active playable route.', '',
        '| Stored type | Journal-linked | POI only | Unresolved | Total |', '| --- | --- | --- | --- | --- |']
    for kind in sorted({q['quest_type'] for q in quests}):
        group = [q for q in quests if q['quest_type'] == kind]
        counts = Counter(q['status'] for q in group)
        gaps.append(f"| {kind} | {counts['journal-linked']} | {sum(n for s, n in counts.items() if s.startswith('POI-linked'))} | {counts['unresolved attribution']} | {len(group)} |")
    gaps += ['', '## Unresolved journal identities', '',
        'Paths in version-tracking, template, demo or generic namespaces are retained as exported. '
        'Their names are evidence hints, not a declaration that content is cut. Likewise, a current implementation using another journal '
        'path does not transfer attribution to an older or duplicate-looking identity.', '',
        '| Entry | Type | Journal identity |', '| --- | --- | --- |']
    for quest in quests:
        if quest['status'] == 'unresolved attribution':
            gaps.append(f"| [{esc(quest['title'])}](all-quests/{quest['document']}) | {quest['quest_type']} | `{quest['journal_path']}` |")
    gaps += ['', '## POI associations without established quest activation', '', '| Entry | Journal identity |', '| --- | --- |']
    for quest in quests:
        if quest['status'].startswith('POI-linked'):
            gaps.append(f"| [{esc(quest['title'])}](all-quests/{quest['document']}) | `{quest['journal_path']}` |")
    (args.docs.parent / 'all-quest-gaps.md').write_text('\n'.join(gaps) + '\n', encoding='utf-8')
    dump(args.data / 'analysis-summary.json', {'quests': len(quests), 'resources': len(metadata),
        'implementation_families': len(families), 'families_without_exported_journal_anchor': len(set(families) - anchor_families),
        'repeated_connected_patterns': len(selected), 'direct_resource_identities': len(direct),
        'bindings_with_archive_provider': sum(bool(v['providers']) for v in ownership.values()),
        'embedded_handoffs': len(embedded), 'named_facts': len(global_facts), 'node_types': dict(all_types.most_common()),
        'per_quest': [{'journal_path': q['journal_path'], 'patterns': len(q['patterns']),
                       'bindings': len(q['direct_bindings']), 'external_facts': len(q['external_fact_producers'])} for q in per_quest]})
    print(json.dumps({'quests': len(quests), 'patterns': len(selected), 'bindings': len(direct), 'facts': len(global_facts)}))


if __name__ == '__main__':
    main()
