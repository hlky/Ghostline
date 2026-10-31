"""Build the isolated native interaction lab; never install from this command."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

import building_builder as building  # noqa: E402
import generate_scene as scenes  # noqa: E402
import generate_world as world  # noqa: E402
import quest_authoring  # noqa: E402
import quest_build  # noqa: E402
from artifact_io import atomic_write_json, publish_json_artifacts  # noqa: E402
from cr2w_validation import compare_documents  # noqa: E402
from ghostline_red import ensure_schema  # noqa: E402
from toolchain import resolve_tool  # noqa: E402
from phase_graph import (  # noqa: E402
    PhaseGraphBuilder, input_node, output_node, phase_document, cname,
    community_action_node, character_spawned_node, trigger_condition_node,
    objective_node, mappin_node, fact_node, quest_completion_node, logical_and_node,
)
from quest_compiler import (  # noqa: E402
    QuestArtifact, artifact_documents, phase_node, validate_handle_graph, validate_no_forward_handle_refs,
)
from quest_encounter import (  # noqa: E402
    scene_flow_node, character_attitude_group_node, character_mortality_node,
)
from quest_native_lifecycle import fact_branch, tick_delay  # noqa: E402

COMMUNITY = '#gqt008_com_barry'
PREFAB = '#gqt008_pr_interaction'
MAIN_SCENE = r'mod\gqt008\scenes\gqt008_interaction.scene'
RESTORE_SCENE = r'mod\gqt008\scenes\gqt008_restore.scene'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def artifact(depot, document):
    relative = Path(depot.replace('\\', '/'))
    archive = PROJECT / 'source/archive' / relative
    document['Header']['ArchiveFileName'] = str(archive)
    return QuestArtifact(PROJECT / 'source/raw' / (relative.as_posix() + '.json'), archive, document)


def scene_call(b, number, scene, *, entry='start', exit='end', extra=()):
    return scene_flow_node(b, number, dict(scene=scene, origin='#gqt008_sm_barry',
        entry=entry, exit=exit, completion_exits=list(extra)))


def attempt(entry):
    """A terminating child owns both the scene and the physical departure wait."""
    b = PhaseGraphBuilder()
    start = input_node(b)
    ends = {name: b.node(i, 'questOutputNodeDefinition', input_names=('In',), output_names=(),
            properties={'socketName': cname(name), 'type': 'Terminating'})
            for i, name in enumerate(('Complete', 'Deferred', 'Away'), 1)}
    scene = scene_call(b, 10, MAIN_SCENE, entry=entry, exit='job_accept', extra=('end',))
    outside = trigger_condition_node(b, 11, '#gqt008_tr_setup', 'IsOutside')
    b.connect(start, scene, destination_socket=entry)
    b.connect(start, outside)
    b.connect_to_earlier_output(scene, ends['Complete'], source_socket='job_accept')
    b.connect_to_earlier_output(scene, ends['Deferred'], source_socket='end')
    b.connect_to_earlier_output(outside, ends['Away'])
    return phase_document(b, PROJECT / 'source/archive/mod/gqt008/phases' / f'attempt_{entry}.questphase')


def root_phase(bindings):
    b = PhaseGraphBuilder()
    start, end = input_node(b), output_node(b)
    objective = bindings['objectives']['interaction']
    fresh = fact_branch(b, 10, 'gqt008_completed')
    nearby = trigger_condition_node(b, 11, '#gqt008_tr_cleanup', 'IsInside')
    activate = community_action_node(b, 12, COMMUNITY, 'Activate')
    activate.data['actions'][0]['type']['Data'].update(communityEntryName=cname('barry'), communityEntryPhaseName=cname('default'))
    ready = character_spawned_node(b, 13, COMMUNITY)
    friendly = character_attitude_group_node(b, 14, COMMUNITY, 'barry', group_name='friendly')
    protect = character_mortality_node(b, 15, COMMUNITY, 'barry', state='Invulnerable', source='gqt008_performance')
    show = objective_node(b, 16, objective['path'])
    pin = mappin_node(b, 17, objective['mappins']['barry']['path'])
    initial_activity = scene_call(b, 18, RESTORE_SCENE)
    setup = trigger_condition_node(b, 20, '#gqt008_tr_setup', 'IsInside')
    returning = fact_branch(b, 21, 'gqt008_deferred')
    first = phase_node(b, 22, r'mod\gqt008\phases\attempt_start.questphase', outputs=('Complete', 'Deferred', 'Away'))
    resumed = phase_node(b, 23, r'mod\gqt008\phases\attempt_resume.questphase', outputs=('Complete', 'Deferred', 'Away'))
    # Child termination retires its scene and departure listener. Two ticks
    # separate cancellation from issuing new workspot commands.
    deferred = fact_node(b, 30, 'gqt008_deferred')
    away = fact_node(b, 31, 'gqt008_deferred')
    settle_defer, settle_away, settle_done = [tick_delay(b, i) for i in (32, 33, 34)]
    restore_defer = scene_call(b, 35, RESTORE_SCENE)
    restore_away = scene_call(b, 36, RESTORE_SCENE)
    restore_done = scene_call(b, 37, RESTORE_SCENE)
    rearm = trigger_condition_node(b, 38, '#gqt008_tr_engage', 'IsOutside')
    joined = logical_and_node(b, 39, 2)
    restored = fact_node(b, 40, 'gqt008_activity_restored')
    done = objective_node(b, 41, objective['path'])
    hide = mappin_node(b, 42, objective['mappins']['barry']['path'])
    complete = quest_completion_node(b, 43, bindings['quest']['path'])
    committed = fact_node(b, 44, 'gqt008_completed')
    departure = trigger_condition_node(b, 45, '#gqt008_tr_cleanup', 'IsOutside')
    release = community_action_node(b, 46, COMMUNITY, 'Deactivate')
    cleaned = fact_node(b, 47, 'gqt008_cleaned_up')
    b.connect(start, fresh)
    b.connect_to_earlier_output(fresh, end, source_socket='True')
    b.connect(fresh, nearby, source_socket='False')
    for left, right in ((nearby, activate), (activate, ready), (ready, friendly), (friendly, protect)):
        b.connect(left, right)
    b.connect(protect, show, destination_socket='Active')
    b.connect(show, pin, destination_socket='Active')
    b.connect(pin, initial_activity, destination_socket='start')
    b.connect(initial_activity, setup, source_socket='end')
    b.connect(setup, returning)
    b.connect(returning, first, source_socket='False', destination_socket='In1')
    b.connect(returning, resumed, source_socket='True', destination_socket='In1')
    for child in (first, resumed):
        connect = b.connect if child is first else b.connect_to_earlier_input
        connect(child, deferred, source_socket='Deferred')
        connect(child, away, source_socket='Away')
        connect(child, settle_done, source_socket='Complete')
    b.connect(deferred, settle_defer)
    # Subscribe before restoration so a rapid leave/return is latched.
    b.connect(deferred, rearm)
    b.connect(settle_defer, restore_defer, destination_socket='start')
    b.connect(restore_defer, joined, source_socket='end', destination_socket='In1')
    b.connect(rearm, joined, destination_socket='In2')
    b.connect_to_earlier_input(joined, setup, source_socket='Out1')
    b.connect(away, settle_away)
    b.connect(settle_away, restore_away, destination_socket='start')
    # Away already observed departure: do not require a second step outside.
    b.connect_to_earlier_input(restore_away, setup, source_socket='end')
    b.connect(settle_done, restore_done, destination_socket='start')
    b.connect(restore_done, restored, source_socket='end')
    b.connect(restored, done, destination_socket='Succeeded')
    b.connect(done, hide, destination_socket='Inactive')
    b.connect(hide, complete, destination_socket='Succeeded')
    b.connect(complete, committed)
    b.connect(committed, departure)
    b.connect(departure, release)
    b.connect(release, cleaned)
    b.connect_to_earlier_output(cleaned, end)
    return phase_document(b, PROJECT / 'source/archive/mod/gqt008/phases/gqt008_interaction.questphase', phase_prefabs=(PREFAB,))


def building_artifacts():
    """Geometry-only export: the quest world owns its actor and activity.

    No hashed NodeRefs may be remapped here. This layout has no devices,
    doors or workstation registry; its only namespace uses are resource paths.
    """
    layout = read(PROJECT / 'implementation/world/interaction-lab.building.json')
    scene = building.compile_layout(layout)
    with tempfile.TemporaryDirectory(prefix='gqt008-building-') as directory:
        out = Path(directory)
        building.export_project(scene, out)
        result = []
        for raw in sorted((out / 'source/raw/mod/building_lab').glob('*.json')):
            document = read(raw)
            root = document['Data']['RootChunk']
            if root.get('nodeRefs') or any(n['Data']['$type'] in ('worldDeviceNode', 'worldCommunityRegistryNode') for n in root.get('nodes', [])):
                raise ValueError('Geometry export unexpectedly owns runtime NodeRefs')
            document = json.loads(json.dumps(document).replace('mod\\\\building_lab\\\\', 'mod\\\\gqt008\\\\'))
            result.append(artifact('mod\\gqt008\\' + raw.name.removesuffix('.json'), document))
    return result


def localization_artifacts():
    """Use the existing, unmodified vanilla Barry playback from GQT007."""
    original = PROJECT / 'implementation/donors/localization'
    result = []
    for name in ('gqt007.lipmap.json', 'subtitles/gqt007.json.json', 'subtitles/gqt007_subtitles_map.json.json', 'vo/gqt007.json.json'):
        doc = json.loads(json.dumps(read(original / name)).replace('gqt007', 'gqt008').replace('barry_lipsync', 'interaction'))
        root = doc['Data']['RootChunk']
        if name.endswith('lipmap.json'):
            root['scenePaths'] = [str(scenes.fnv1a64(MAIN_SCENE))]
            # WolvenKit's editor-only extension is emitted as explicit null,
            # as in the current story lipmaps. Keep strict typed readback.
            root['scenePreviewPaths'] = None
        else:
            data = root['root']['Data']
            if 'entries' in data and data['entries'] and 'stringId' in data['entries'][0]:
                data['entries'] = data['entries'][:1]
                data['entries'][0]['stringId'] = '17800800000000000001'
        result.append(artifact('mod\\gqt008\\localization\\en-us\\' + name.removesuffix('.json').replace('/', '\\').replace('gqt007', 'gqt008'), doc))
    return result


def build_artifacts():
    composed = quest_authoring.compose(read(PROJECT / 'interaction.composition.json'))
    artifacts = [artifact(depot, doc) for depot, doc in composed.documents.items()]
    for name in ('interaction', 'restore'):
        spec = read(PROJECT / f'implementation/scenes/{name}.scene-spec.json')
        doc = scenes.build_scene(spec)
        errors = scenes.validate_scene(doc, spec)
        if errors:
            raise ValueError('\n'.join(errors))
        artifacts.append(artifact(MAIN_SCENE if name == 'interaction' else RESTORE_SCENE, doc))
    artifacts.extend(localization_artifacts())
    outputs, documents = world.build_world_documents(read(PROJECT / 'implementation/world/interaction.world.json'), PROJECT / 'source/raw', PROJECT / 'source/archive')
    artifacts.extend(QuestArtifact(item.raw_path, item.archive_path, documents[item.raw_path]) for item in outputs)
    artifacts.extend(building_artifacts())
    for entry in ('start', 'resume'):
        artifacts.append(artifact(f'mod\\gqt008\\phases\\attempt_{entry}.questphase', attempt(entry)))
    artifacts.append(artifact(r'mod\gqt008\phases\gqt008_interaction.questphase', root_phase(composed.bindings)))
    for item in artifacts:
        if item.archive_path.suffix == '.questphase':
            validate_handle_graph(item.document, context=item.archive_path.name)
            validate_no_forward_handle_refs(item.document, context=item.archive_path.name)
    return artifacts


def publish_native(artifacts, media):
    """Batch conversion, with the building verifier for collision/nav buffers.

    WolvenKit exposes collision bytes as parsed CollisionBuffer data; the
    Building Lab verifier reads them independently with ghostline-red and
    checks original bytes, placements, resources and embedded navigation.
    The other resources use the shared strict typed comparison.
    """
    staging = PROJECT / 'generated/native-builds'
    staging.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='candidate-', dir=staging) as directory:
        out = Path(directory)
        binary_dir, readback_dir = out / 'binary', out / 'readback'
        binary_dir.mkdir()
        readback_dir.mkdir()
        inputs, candidates = [], []
        for index, item in enumerate(artifacts):
            raw = out / 'input' / f'{index}_{item.archive_path.name}.json'
            atomic_write_json(raw, item.document)
            inputs.append(raw)
            candidates.append(binary_dir / raw.name.removesuffix('.json'))
        tool = str(resolve_tool('wolvenkit'))
        subprocess.run([tool, 'convert', 'deserialize', *map(str, inputs), '-o', str(binary_dir)], check=True)
        subprocess.run([tool, 'convert', 'serialize', *map(str, candidates), '-o', str(readback_dir)], check=True)
        schema = read(ensure_schema())
        binaries, geometry_paths = {}, []
        geometry_names = {'gqt008-lab.streamingblock', 'gqt008-lab.streamingsector', 'gqt008-lab_navigation.streamingsector'}
        for item, candidate in zip(artifacts, candidates, strict=True):
            content = candidate.read_bytes()
            if content[:4] != b'CR2W':
                raise ValueError(f'Invalid native resource: {candidate.name}')
            decoded = read(readback_dir / (candidate.name + '.json'))
            is_geometry = item.archive_path.name in geometry_names
            if not is_geometry or item.archive_path.suffix == '.streamingblock':
                comparison = compare_documents(item.document, decoded, schema=schema, fresh_wolvenkit_defaults=decoded)
                if not comparison.ok:
                    raise ValueError(f'{item.archive_path.name}: {comparison.errors[:8]}')
            if is_geometry:
                raw = out / 'building-check/source/raw/mod/building_lab' / (item.archive_path.name + '.json')
                atomic_write_json(raw, item.document)
                target = out / 'building-check/source/archive/mod/building_lab' / item.archive_path.name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(candidate, target)
                geometry_paths.append(raw)
            binaries[item.archive_path] = content
        if len(geometry_paths) != len(geometry_names):
            raise ValueError('Expected the complete three-resource geometry export')
        scene = building.compile_layout(read(PROJECT / 'implementation/world/interaction-lab.building.json'))
        atomic_write_json(out / 'building-check/building-report.json', {'stats': scene['stats'], 'warnings': scene['warnings']})
        building.verify_native_project(scene, out / 'building-check', geometry_paths)
        atomic_write_json(PROJECT / 'generated/building-readback.json', read(out / 'building-check/building-report.json'))
        binaries.update({target: source.read_bytes() for target, source in media.items()})
        publish_json_artifacts(artifact_documents(artifacts), binary_artifacts=binaries,
            ownership_path=PROJECT / 'generated/quest-builds/gqt008/outputs.json')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--deserialize', action='store_true')
    args = parser.parse_args()
    artifacts = build_artifacts()
    donor = PROJECT / 'implementation/donors'
    for name, expected in read(donor / 'provenance.json')['sha256'].items():
        if hashlib.sha256((donor / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Changed donor input: {name}')
    target_anim = Path('base/localization/en-us/lipsync/mod/gqt008/scenes/gqt008_interaction/civ_low_m_11_enus_40_fat.anims')
    audio = Path('mod/gqt008/localization/en-us/vo/barry_who_is_it.wem')
    if args.deserialize:
        publish_native(artifacts, {
            PROJECT / 'source/archive' / target_anim: donor / 'civ_low_m_11_enus_40_fat.anims',
            PROJECT / 'source/archive' / audio: donor / 'barry_who_is_it.wem',
        })
    else:
        quest_build.publish_build(artifacts, namespace='gqt008', project_root=PROJECT)
    report = dict(native_readback_verified=args.deserialize, installed=False, runtime_tested=False,
        resources=len(artifacts), actor='Character.mq010_barry', workspot_entry=2,
        source_layout_sha256=hashlib.sha256((PROJECT/'implementation/world/interaction-lab.building.json').read_bytes()).hexdigest())
    atomic_write_json(PROJECT/'generated/build-report.json', report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
