"""Build the configurable native meeting/link/reward template into an isolated preview."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
from types import SimpleNamespace

from artifact_io import atomic_write_json
from quest_authoring import compose
from quest_build import publish_build
from quest_compiler import QuestArtifact, validate_handle_graph, validate_no_forward_handle_refs
from project_layout import catalog as project_catalog
import quest_native_lifecycle as native

ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = re.compile(r'^[a-z][a-z0-9_]*$')


def fields(value, required, optional=(), *, context):
    if not isinstance(value, dict):
        raise ValueError(f'{context} must be an object')
    missing, unknown = set(required) - value.keys(), value.keys() - set(required) - set(optional)
    if missing or unknown:
        raise ValueError(f'{context}: missing {sorted(missing)}, unknown {sorted(unknown)}')


def text(value, context):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{context} must be a nonempty string')
    return value


def resource(value, suffix):
    text(value, 'resource')
    parts = value.replace('\\', '/').split('/')
    if parts[0] not in {'mod', 'base', 'ep1'} or any(p in {'', '.', '..'} for p in parts) or not value.endswith(suffix):
        raise ValueError(f'Invalid {suffix} resource: {value}')


def noderef(value):
    text(value, 'NodeRef')
    if not value.startswith(('#', '$/')):
        raise ValueError(f'Expected string NodeRef: {value}')


def positive_integer(value, context):
    if type(value) is not int or value <= 0:
        raise ValueError(f'{context} must be a positive integer')


def scene(value):
    fields(value, {'scene', 'origin', 'entry', 'exit'}, context='scene')
    resource(value['scene'], '.scene')
    noderef(value['origin'])
    for key in ('entry', 'exit'):
        text(value[key], key)


def validate(config):
    fields(config, {'schema_version', 'namespace', 'title', 'phase_prefabs', 'giver',
                    'objectives', 'transfers', 'reward'}, {'epilogue', 'audio_call'}, context='template')
    if type(config['schema_version']) is not int or config['schema_version'] != 1:
        raise ValueError('Expected template schema_version 1')
    if not isinstance(config['namespace'], str) or not IDENTIFIER.fullmatch(config['namespace']):
        raise ValueError('namespace must be a lowercase identifier')
    text(config['title'], 'title')
    if not isinstance(config['phase_prefabs'], list) or not config['phase_prefabs']:
        raise ValueError('phase_prefabs must list the world prefabs retained by the root')
    for ref in config['phase_prefabs']:
        noderef(ref)
    giver = config['giver']
    fields(giver, {'community', 'entry', 'scene_origin', 'setup_trigger', 'rearm_trigger',
                   'cleanup_trigger', 'meeting_scene', 'return_scene'}, context='giver')
    text(giver['entry'], 'giver.entry')
    for key in ('community', 'scene_origin', 'setup_trigger', 'rearm_trigger', 'cleanup_trigger'):
        noderef(giver[key])
    for key in ('meeting_scene', 'return_scene'):
        resource(giver[key], '.scene')
    transfers = config['transfers']
    if not isinstance(transfers, list) or not 1 <= len(transfers) <= 16:
        raise ValueError('transfers must contain one to sixteen entries')
    ids = ['meet', 'return']
    for transfer in transfers:
        fields(transfer, {'id', 'device', 'label', 'duration_seconds'},
               {'connected_scene', 'intro_scene', 'retry_scene', 'success_scene', 'interaction_record'}, context='transfer')
        if not isinstance(transfer['id'], str) or not IDENTIFIER.fullmatch(transfer['id']):
            raise ValueError('transfer.id must be a lowercase identifier')
        ids.append(transfer['id'])
        noderef(transfer['device'])
        text(transfer['label'], 'transfer.label')
        positive_integer(transfer['duration_seconds'], 'transfer.duration_seconds')
        if 'interaction_record' in transfer and not text(transfer['interaction_record'], 'interaction_record').startswith('Interactions.'):
            raise ValueError('interaction_record must name an Interactions.* record')
        for key in ('connected_scene', 'intro_scene', 'retry_scene', 'success_scene'):
            if key in transfer:
                scene(transfer[key])
    reserved = {'root', 'finish', 'reward_repair'}
    if len(set(ids)) != len(ids) or set(ids) & reserved:
        raise ValueError('Stage IDs must be distinct and cannot use root/finish/reward_repair')
    resources = ids + [t['id'] + '_attempt' for t in transfers] + list(reserved)
    if len(set(resources)) != len(resources):
        raise ValueError('Stage and generated attempt resource names collide')
    if len({t['device'] for t in transfers}) != len(transfers):
        raise ValueError('Each transfer requires a distinct device; completed devices are disabled')
    if not isinstance(config['objectives'], dict) or set(config['objectives']) != set(ids):
        raise ValueError('objectives must match meet, return, and every transfer ID')
    for objective in config['objectives'].values():
        fields(objective, {'text', 'description', 'marker'}, context='objective')
        text(objective['text'], 'objective.text')
        text(objective['description'], 'objective.description')
        noderef(objective['marker'])
    fields(config['reward'], {'item', 'quantity', 'repair_completed_saves'}, context='reward')
    item = text(config['reward']['item'], 'reward.item')
    if not item.startswith('Items.') or len(item) <= len('Items.'):
        raise ValueError('reward.item must name an Items.* record')
    positive_integer(config['reward']['quantity'], 'reward.quantity')
    if type(config['reward']['repair_completed_saves']) is not bool:
        raise ValueError('reward.repair_completed_saves must be Boolean')
    if 'epilogue' in config:
        fields(config['epilogue'], {'phase', 'delay_seconds'}, context='epilogue')
        resource(config['epilogue']['phase'], '.questphase')
        positive_integer(config['epilogue']['delay_seconds'], 'epilogue.delay_seconds')
        owned = {rf'mod\{config["namespace"]}\phases\{config["namespace"]}_{name}.questphase' for name in resources}
        if config['epilogue']['phase'].replace('/', '\\') in owned:
            raise ValueError('Epilogue must be a separate caller-owned phase')
    if 'audio_call' in config:
        call = config['audio_call']
        fields(call, {'caller', 'addressee', 'prefab', 'start_before', 'end_before'}, context='audio_call')
        for key in ('caller', 'addressee'):
            if not text(call[key], key).startswith('contacts/'):
                raise ValueError(f'audio_call.{key} must be a contact journal path')
        noderef(call['prefab'])
        order = ['meet'] + [t['id'] for t in transfers] + ['return']
        if call['start_before'] not in order or call['end_before'] not in order or order.index(call['start_before']) >= order.index(call['end_before']):
            raise ValueError('Call start/end must be ordered stage IDs')
        if call['prefab'] not in config['phase_prefabs']:
            raise ValueError('Call prefab must be retained in phase_prefabs')


def access_point_values(document):
    """Compare inline values in our cloned controllers despite WKit coalescing.

    This opt-in adapter is limited to the template's AccessPoint entity clones.
    It retains all typed values/wrapper metadata and rejects malformed handles;
    graph resources keep the shared validator's strict alias policy.
    """
    root = document['Data']['RootChunk']
    if root.get('$type') != 'entEntityTemplate':
        raise ValueError('Access-point readback adapter requires an entity template')
    definitions = {}
    classes = set()
    def index(value):
        if isinstance(value, dict):
            if '$type' in value:
                classes.add(value['$type'])
            if 'HandleId' in value:
                key = str(value['HandleId'])
                if key in definitions:
                    raise ValueError('Duplicate access-point value handle')
                definitions[key] = value['Data']
            for child in value.values():
                index(child)
        elif isinstance(value, list):
            for child in value:
                index(child)
    index(document)
    if 'AccessPointControllerPS' not in classes:
        raise ValueError('Access-point readback adapter requires AccessPointControllerPS')
    def expand(value, active=()):
        if isinstance(value, dict):
            key = value.get('HandleId', value.get('HandleRefId'))
            if key is not None:
                key = str(key)
                if key in active or key not in definitions:
                    raise ValueError('Cyclic or unresolved access-point value handle')
                data = expand(definitions[key], active + (key,))
                metadata = {k: expand(v, active) for k, v in value.items() if k not in {'HandleId', 'HandleRefId', 'Data'}}
                return {'value': data, 'wrapper': metadata} if metadata else data
            return {k: expand(v, active) for k, v in value.items()}
        if isinstance(value, list):
            return [expand(v, active) for v in value]
        return value
    return expand(document)


def compile_template(config, output):
    """Return isolated raw artifacts and explicit integration contracts; no live writes."""
    config = copy.deepcopy(config)
    validate(config)
    namespace = config['namespace']
    output = Path(output).resolve()
    layout = project_catalog(ROOT)
    owners = [ROOT, *[ROOT / value for value in layout['projects'].values()],
              *[ROOT / value for value in layout.get('template_roots', [])]]
    if any(output == owner.resolve() or output.is_relative_to((owner / 'source').resolve()) for owner in owners):
        raise ValueError('Template output must be an isolated preview outside project roots and source trees')
    giver, reward = config['giver'], config['reward']
    prefabs = tuple(config['phase_prefabs'])
    phase = lambda name: rf'mod\{namespace}\phases\{namespace}_{name}.questphase'  # noqa: E731
    facts = {name: f'{namespace}_{name}' for name in (
        'job_accepted', 'meet_deferred', 'debrief_done', 'completed', 'reward_granted', 'reward_delivery_verified')}
    content = compose({'schema_version': 1, 'id': namespace, 'title': config['title'],
        'composition': {'objectives': {name: {'text': obj['text'], 'description': obj['description'],
            'mappins': {'target': {'ref': obj['marker'], 'text': obj['text']}}}
            for name, obj in config['objectives'].items()}}, 'stages': []})
    artifacts = []

    def add(depot, document):
        relative = Path(depot.replace('\\', '/'))
        archive = output / 'source/archive' / relative
        document['Header']['ArchiveFileName'] = str(archive)
        artifacts.append(QuestArtifact(output / 'source/raw' / (relative.as_posix() + '.json'), archive, document))

    def emit(name, builder, *args, **kwargs):
        depot = phase(name)
        archive = output / 'source/archive' / Path(depot.replace('\\', '/'))
        document = builder(*args, archive, **kwargs)
        validate_handle_graph(document, context=name)
        validate_no_forward_handle_refs(document, context=name)
        add(depot, document)

    def stage(name, **extra):
        obj = content.bindings['objectives'][name]
        return SimpleNamespace(id=name, phase_resource=phase(name), data={
            'objective': obj['path'], 'description_entry': obj['description_entry'],
            'mappin': obj['mappins']['target']['path'], **extra})

    meeting_args = dict(setup_trigger=giver['setup_trigger'], rearm_trigger=giver['rearm_trigger'],
        scene_origin=giver['scene_origin'], protection_source=f'{namespace}_giver_protection', phase_prefabs=prefabs)
    meet = stage('meet', community=giver['community'], contact=giver['entry'], scene=giver['meeting_scene'])
    emit('meet', native.meeting, meet, success_fact=facts['job_accepted'], deferred_fact=facts['meet_deferred'], **meeting_args)
    stages = [meet]
    for transfer in config['transfers']:
        name = transfer['id']
        facts[name + '_done'] = f'{namespace}_{name}_done'
        current = stage(name, device=transfer['device'], success_fact=facts[name + '_done'])
        # attempt's positional order is device, archive, label.
        emit(name + '_attempt', lambda device, archive: native.attempt(device, archive,
             transfer['label'], duration_seconds=transfer['duration_seconds'],
             connected_scene=transfer.get('connected_scene')), transfer['device'])
        emit(name, native.transfer, current, attempt_resource=phase(name + '_attempt'), phase_prefabs=prefabs,
             **{key: transfer[key] for key in ('intro_scene', 'retry_scene', 'success_scene') if key in transfer})
        donor = ROOT / 'quests/templates/source/raw/mod/ghostline/quest_blocks/native_personal_link/access_point.ent.json'
        catalog = json.loads((ROOT / 'quests/templates/donors/catalog.json').read_text(encoding='utf-8'))
        expected = next(row['sha256'] for row in catalog['templates'] if row['path'] == donor.relative_to(ROOT).as_posix())
        if hashlib.sha256(donor.read_bytes()).hexdigest() != expected:
            raise ValueError('Native access-point donor differs from its reviewed hash')
        document = json.loads(donor.read_text(encoding='utf-8'))
        state = document['Data']['RootChunk']['compiledData']['Data']['Chunks'][4]['persistentState']['Data']
        state['personalLinkCustomInteraction']['$value'] = transfer.get('interaction_record', 'Interactions.ConnectPersonalLink')
        add(rf'mod\{namespace}\devices\{name}.ent', document)
        stages.append(current)
    returning = stage('return', community=giver['community'], contact=giver['entry'], scene=giver['return_scene'])
    emit('return', native.meeting, returning, success_fact=facts['debrief_done'],
         reward_item=reward['item'], reward_quantity=reward['quantity'], **meeting_args)
    stages.append(returning)
    emit('root', native.root, SimpleNamespace(stages=stages, phase_prefabs=prefabs),
         completed_fact=facts['completed'], cleanup_trigger=giver['cleanup_trigger'],
         cleanup_community=giver['community'], call=config.get('audio_call'))
    finish_args = dict(completed_fact=facts['completed'], debrief_fact=facts['debrief_done'],
        reward_item=reward['item'], reward_quantity=reward['quantity'],
        verified_fact=facts['reward_delivery_verified'], granted_fact=facts['reward_granted'])
    emit('finish', native.finish_and_epilogue, quest_path=content.bindings['quest']['path'],
         epilogue_phase=config.get('epilogue', {}).get('phase'),
         epilogue_delay_seconds=config.get('epilogue', {}).get('delay_seconds', 45), **finish_args)
    if reward['repair_completed_saves']:
        emit('reward_repair', native.reward_repair, **finish_args)
    for depot, document in content.documents.items():
        add(depot, document)
    roots = [phase('root'), phase('finish')]
    if reward['repair_completed_saves']:
        roots.append(phase('reward_repair'))
    contracts = {
        'schema_version': 1, 'namespace': namespace,
        'evidence': 'Authoring template extracted from playtested GQ004; this binding set is not game-tested.',
        'facts': facts, 'required_world': {'phase_prefabs': list(prefabs), 'giver': giver,
            'devices': [{'ref': t['device'], 'template': rf'mod\{namespace}\devices\{t["id"]}.ent'} for t in config['transfers']],
            'markers': [o['marker'] for o in config['objectives'].values()]},
        'meeting_scene': {'resource': giver['meeting_scene'], 'entries': ['start', 'resume'],
            'exits': ['job_accept', 'end'], 'actor': {'community': giver['community'], 'entry': giver['entry']},
            'policy': 'resume skips introduction; scene owns inner proximity and combat gates'},
        'return_scene': {'resource': giver['return_scene'], 'entries': ['start'], 'exits': ['job_accept', 'end']},
        'device_policy': {'controller': 'AccessPointControllerPS', 'hacking_skill_check': 'NONE/inactive',
            'skip_minigame': True, 'registry': 'register clones in the actual Night City devices registry'},
        'required_reward': reward,
        'optional_epilogue': config.get('epilogue'), 'optional_audio_call': config.get('audio_call'),
        'transfer_scenes': [{key: t[key] for key in ('id', 'connected_scene', 'intro_scene', 'retry_scene', 'success_scene') if key in t}
                            for t in config['transfers']],
        'scene_policy': 'Wait for speakers to spawn before time-zero speech; transfer scenes are caller-owned.',
        'registration_fragment': {'quest': {'phases': [{'path': p, 'parent': 'base\\quest\\cyberpunk2077.quest'} for p in roots]},
            'journal': [content.bindings['resources']['journal']],
            'localization': {'onscreens': {'en-us': [content.bindings['resources']['onscreens']]}}},
        'profile_additional_root_phases': roots[1:],
        'integration_status': 'Requires supplied world, scene, character and item resources before packaging.'}
    return artifacts, contracts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, required=True)
    parser.add_argument('--out-root', type=Path, required=True)
    parser.add_argument('--deserialize', action='store_true')
    args = parser.parse_args()
    config = json.loads(args.spec.read_text(encoding='utf-8'))
    artifacts, contracts = compile_template(config, args.out_root)
    donor = ROOT / 'quests/templates/source/archive/mod/ghostline/quest_blocks/native_personal_link/access_point.ent'
    catalog = json.loads((ROOT / 'quests/templates/donors/catalog.json').read_text(encoding='utf-8'))
    expected = next(row['sha256'] for row in catalog['templates'] if row['path'] == donor.relative_to(ROOT).as_posix())
    if hashlib.sha256(donor.read_bytes()).hexdigest() != expected:
        raise ValueError('Binary access-point donor differs from its reviewed hash')
    artifacts.sort(key=lambda artifact: (artifact.archive_path.suffix != '.ent', artifact.archive_path.name))
    publish_build(artifacts, namespace=config['namespace'], output_root=args.out_root,
                  deserialize=args.deserialize, project_root=args.out_root.resolve(),
                  binary_templates={a.archive_path: donor for a in artifacts if a.archive_path.suffix == '.ent'},
                  value_normalizers={a.archive_path: access_point_values for a in artifacts if a.archive_path.suffix == '.ent'})
    atomic_write_json(args.out_root / 'native-contract.json', contracts)
    print(json.dumps({'artifacts': len(artifacts), 'output': str(args.out_root.resolve()),
                      'status': contracts['integration_status']}, indent=2))


if __name__ == '__main__':
    main()
