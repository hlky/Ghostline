"""Cross-check complete generated race resources before publication."""
from collections import deque

from generate_world import node_ref_hash
from scene_validation import validate_reference_tables


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def validate_phase(document, resources):
    root = document['Data']['RootChunk']
    handles = {item['HandleId']: item['Data'] for item in walk(document)
               if 'HandleId' in item and 'Data' in item}
    nodes = root['graph']['Data']['nodes']
    by_id = {node['Data']['id']: node['Data'] for node in nodes}
    if len(by_id) != len(nodes):
        raise ValueError('Race phase has duplicate quest node IDs')
    sockets = {}
    for wrapper in nodes:
        for socket in wrapper['Data']['sockets']:
            socket_id = socket.get('HandleId', socket.get('HandleRefId'))
            sockets[socket_id] = (wrapper['Data']['id'], handles[socket_id])
    adjacency = {node_id: set() for node_id in by_id}
    connections = {}
    for socket_id, (node_id, socket) in sockets.items():
        for reference in socket['connections']:
            connection_id = reference.get('HandleId', reference.get('HandleRefId'))
            connection = handles[connection_id]
            source_id = connection['source'].get('HandleId', connection['source'].get('HandleRefId'))
            destination_id = connection['destination'].get('HandleId', connection['destination'].get('HandleRefId'))
            if source_id not in sockets or destination_id not in sockets:
                raise ValueError('Race phase connection references a missing socket')
            source_node, source = sockets[source_id]
            destination_node, destination = sockets[destination_id]
            if source['type'] not in ('Output', 'CutSource') or destination['type'] not in ('Input', 'CutDestination'):
                raise ValueError('Race phase connection has incompatible socket directions')
            for endpoint in (source, destination):
                listed = {edge.get('HandleId', edge.get('HandleRefId')) for edge in endpoint['connections']}
                if connection_id not in listed:
                    raise ValueError('Race phase connection is absent from one endpoint')
            connections[connection_id] = (source_node, destination_node)
            if source['type'] != 'CutSource':
                adjacency[source_node].add(destination_node)
    pending = deque(node_id for node_id, node in by_id.items() if node['$type'] == 'questInputNodeDefinition')
    reachable = set(pending)
    while pending:
        for destination in adjacency[pending.popleft()] - reachable:
            reachable.add(destination)
            pending.append(destination)
    if reachable != set(by_id):
        raise ValueError(f'Race phase has unreachable quest nodes: {sorted(set(by_id)-reachable)}')
    for node in by_id.values():
        if node['$type'] == 'questPhaseNodeDefinition':
            depot = node['phaseResource']['DepotPath']['$value']
            if depot not in resources:
                raise ValueError(f'Race phase references missing child resource {depot}')
            child = resources[depot]['Data']['RootChunk']['graph']['Data']['nodes']
            inputs = {item['Data']['socketName']['$value'] for item in child if item['Data']['$type'] == 'questInputNodeDefinition'}
            outputs = {item['Data']['socketName']['$value'] for item in child if item['Data']['$type'] == 'questOutputNodeDefinition'}
        elif node['$type'] == 'questSceneNodeDefinition':
            depot = node['sceneFile']['DepotPath']['$value']
            if depot not in resources:
                raise ValueError(f'Race phase references missing scene resource {depot}')
            scene = resources[depot]['Data']['RootChunk']
            inputs = {point['name']['$value'] for point in scene['entryPoints']}
            outputs = {point['name']['$value'] for point in scene['exitPoints']}
        else:
            continue
        for socket in node['sockets']:
            data = handles[socket.get('HandleId', socket.get('HandleRefId'))]
            if data['type'] == 'Input' and data['name']['$value'] not in inputs:
                raise ValueError('Race phase input does not match its scene/child entry')
            if data['type'] == 'Output' and data['name']['$value'] not in outputs:
                raise ValueError('Race phase output does not match its scene/child exit')
    return {'nodes': len(nodes), 'connections': len(connections), 'reachable_nodes': len(reachable)}


def validate_resources(resources, bindings):
    sectors = [document['Data']['RootChunk'] for document in resources.values()
               if document['Data']['RootChunk']['$type'] == 'worldStreamingSector']
    refs = {reference['$value'] for sector in sectors for reference in sector['nodeRefs']}
    aliases = {reference.rsplit('/', 1)[-1] for reference in refs}
    refs.update(aliases)
    refs.add(bindings['prefab'])
    hashes = {str(node_ref_hash(reference)) for reference in refs}
    # Registry nodes intentionally have an anonymous numeric placement identity
    # instead of a named entry in the sector's nodeRefs table.
    for sector in sectors:
        for placement in sector['nodeData']['Data']:
            identity = placement['QuestPrefabRefHash']
            if identity.get('$storage') == 'uint64' and 0 <= placement['NodeIndex'] < len(sector['nodes']):
                hashes.add(identity['$value'])
    community_entries = {item['entryName']['$value'] for document in resources.values()
                         for item in walk(document) if item.get('$type') == 'communitySpawnEntry'}
    journal_paths = set()
    def visit_entry(wrapper, parent=''):
        entry = wrapper['Data']
        path = '/'.join(part for part in [parent, entry['id']] if part)
        journal_paths.add(path)
        for child in entry.get('entries', []):
            visit_entry(child, path)
    for document in resources.values():
        root = document['Data']['RootChunk']
        if root['$type'] == 'gameJournalResource':
            visit_entry(root['entry'])
    phases = {}
    for depot, document in resources.items():
        root = document['Data']['RootChunk']
        for item in walk(document):
            if item.get('$type') == 'NodeRef':
                value = item['$value']
                if value not in ('0', '', '#player', '#mounted_vehicle', '#owned_vehicle') and value not in refs and value not in hashes:
                    raise ValueError(f'Race resource {depot} has unresolved NodeRef {value}')
            if item.get('$type') == 'gameEntityReference' and item['reference']['$value'] in (bindings['community'],bindings['crowd']):
                if any(name['$value'] not in community_entries for name in item['names']):
                    raise ValueError(f'Race resource {depot} references a missing community entry')
            if item.get('$type') == 'gameJournalPath' and item['realPath'] not in journal_paths:
                raise ValueError(f'Race resource {depot} references a missing journal entry')
        if root['$type'] == 'scnSceneResource':
            errors = validate_reference_tables(root)
            if errors:
                raise ValueError('; '.join(errors))
        if root['$type'] == 'questQuestPhaseResource':
            phases[depot] = validate_phase(document, resources)
    return {'resources': len(resources), 'world_node_refs': len(aliases),
            'community_entries': len(community_entries), 'phases': phases}
