"""Prepare quest-owned localization, field VO and isolated package selection."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import shutil
import sys
import yaml

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from generate_scene import fnv1a64


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    native_inputs()
    animset = r'base\localization\en-us\lipsync\mod\gq004\gq004.anims'
    scenes = []
    for path in sorted((HERE / 'scenes').glob('*.scene-spec.json')):
        spec = json.loads(path.read_text())
        for actor in spec['actors']:
            actor['lipsync'] = 0 if actor['key'] == 'velvet' else 1
            if actor['key'] == 'velvet': actor['voicetag'] = str(fnv1a64('gq_velvet'))
        spec['lipsync_animset'] = animset
        write(path, spec)
        scenes.append(spec)
    for path in sorted((HERE.parent / 'script').glob('*_manifest.json')):
        manifest = json.loads(path.read_text(encoding='utf-8'))
        for line in manifest['spoken_lines']:
            line['female_lipsync_animation'] = f"f_{int(line['string_id']):016X}"
            line['male_lipsync_animation'] = f"m_{int(line['string_id']):016X}"
        write(path, manifest)
    character = PROJECT / 'generated/characters/velvet'
    authored = character / 'projects/ghostline/source'
    for source_root in (authored, character / 'source'):
        for tree in ('raw', 'archive'):
            folder = source_root / tree
            if not folder.is_dir(): continue
            for source in folder.rglob('*'):
                if not source.is_file() or any(p.startswith('verify-') for p in source.parts): continue
                relative = source.relative_to(folder)
                if str(relative).replace('\\', '/') == 'mod/ghostline/characters/velvet/body/t0_000_pwa_base__full.mesh' + ('.json' if tree == 'raw' else ''):
                    continue  # Authored body repair owns its material paths and textures.
                if tree == 'archive' and source.read_bytes()[:4] != b'CR2W': continue
                shared = ROOT / 'projects/shared/ghostline-runtime/source' / tree / relative
                if shared.is_file():
                    if shared.read_bytes() != source.read_bytes(): raise ValueError(f'Shared dependency differs: {relative}')
                    continue
                destination = PROJECT / 'source' / tree / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)
    tweak = Path('resources/r6/tweaks/ghostline/character_velvet.yaml')
    protection = json.loads((PROJECT / 'characters/velvet.character.json').read_text(encoding='utf-8'))['tweak']['protection']
    text = (authored / tweak).read_text(encoding='utf-8')
    text += f"  baseAttitudeGroup: {protection['attitude_group']}\n"
    if protection['invulnerable']:
        text += '  tags:\n    - !append Invulnerable\n'
    (PROJECT / 'source' / tweak).write_text(text, encoding='utf-8')
    loc_relative = Path('raw/mod/gq004/localization/en-us/onscreens/velvet.json.json')
    loc = json.loads((authored / loc_relative).read_text())
    entries = loc['Data']['RootChunk']['root']['Data']['entries']
    entries[:] = [e for e in entries if e['secondaryKey'] == 'gq_npc_velvet']
    entries.append(dict(entries[0], secondaryKey='gl_gq004_heartbreaker_name', femaleVariant='Heartbreaker Protocol'))
    entries.append(dict(entries[0], secondaryKey='gl_gq004_heartbreaker_description',
        femaleVariant="Velvet Kade's one-of-a-kind Heartbreaker build. Velvet Crash interrupts combat cyberware for six seconds, with pink pixel hearts and tiny black bows. Restores nobody's affections. Respects everybody's right to refuse."))
    entries.append(dict(entries[0], secondaryKey='gl_gq004_heartbreaker_effect',
        femaleVariant="Disrupts the target's optics for 6 seconds with pink pixel hearts and tiny black bows, ending in a burst of glitch confetti. Velvet calls it flirting. Your target may disagree."))
    for key, text in [('gl_gq004_recover_link', 'Recover Heartbreaker + archived messages'),
                      ('gl_gq004_upload_link', 'Upload Velvet Crash')]:
        entries.append(dict(entries[0], secondaryKey=key, femaleVariant=text))
    write(PROJECT / 'source' / loc_relative, loc)
    lipmap = copy.deepcopy(loc)
    depot = r'mod\gq004\localization\en-us\gq004.lipmap'
    lipmap['Header']['ArchiveFileName'] = str(PROJECT / 'source/archive' / Path(depot.replace('\\', '/')))
    lipmap['Data']['RootChunk'] = dict(
        **{'$type': 'animLipsyncMapping'}, cookingPlatform='PLATFORM_PC',
        languageCodeName={'$type': 'CName', '$storage': 'string', '$value': 'en-us'},
        scenePaths=[str(fnv1a64('mod\\gq004\\scenes\\' + s['name'] + '.scene')) for s in scenes],
        sceneEntries=[dict(**{'$type': 'animLipsyncMappingSceneEntry'},
            actorVoiceTags=[str(fnv1a64('gq_velvet')), '1103967280742240864'],
            animSets=[{'DepotPath': {'$type': 'ResourcePath', '$storage': 'string', '$value': animset}, 'Flags': 'Soft'}] * 2)
            for _ in scenes])
    write(PROJECT / 'source/raw/mod/gq004/localization/en-us/gq004.lipmap.json', lipmap)
    world = json.loads((HERE / 'world/love-actually.world.json').read_text())
    p = PROJECT / 'project.json'
    config = json.loads(p.read_text())
    dependency = '../experiments/velvet-crash'
    if dependency not in config['dependencies']: config['dependencies'].append(dependency)
    write(p, config)
    p = PROJECT / 'packaging/profiles.json'
    config = json.loads(p.read_text())
    loose = []
    config['profiles']['love-actually'] = dict(archive_name='Ghostline_LoveActually', active_quests=['gq004'],
        support_quests=['velvet_crash'], characters=['velvet'],
        additional_root_phases=[r'mod\gq004\phases\gq004_reward_repair.questphase',
                                r'mod\gq004\phases\gq004_finish_and_epilogue.questphase'],
        tweaks=['character_velvet', 'faction_ghostline', 'gq004_love_actually', 'velvet_crash_protocol',
                'z_gq004_heartbreaker_icon'],
        external_patch_targets=['mod/ghostline/characters/goth_baddie/goth_baddie.ent'],
        include_loose=loose, deduplicate_meshes=False)
    write(p, config)
    p = PROJECT / 'source/resources/Ghostline.archive.xl'
    registration = yaml.safe_load(p.read_text())
    phase = {'path': r'mod\gq004\phases\gq004.questphase', 'parent': r'base\quest\cyberpunk2077.quest'}
    if phase not in registration['quest']['phases']: registration['quest']['phases'].append(phase)
    repair = dict(phase, path=r'mod\gq004\phases\gq004_reward_repair.questphase')
    if repair not in registration['quest']['phases']: registration['quest']['phases'].append(repair)
    finish = dict(phase, path=r'mod\gq004\phases\gq004_finish_and_epilogue.questphase')
    if finish not in registration['quest']['phases']: registration['quest']['phases'].append(finish)
    for section, value in [('journal', r'mod\gq004\journal\gq004.journal')]:
        if value not in registration[section]: registration[section].append(value)
    block = world['block_path']
    if block not in registration['streaming']['blocks']: registration['streaming']['blocks'].append(block)
    patch = registration.setdefault('resource', {}).setdefault('patch', {})
    patch[world['device_registry_path']] = [r'base\worlds\03_night_city\_compiled\default\03_night_city.devices']
    for category, values in {
        'onscreens': [r'mod\gq004\localization\en-us\onscreens\gq004.json', r'mod\gq004\localization\en-us\onscreens\velvet.json'],
        'lipmaps': [depot],
        'subtitles': [rf'mod\gq004\localization\en-us\subtitles\gq004_{i:02}_subtitles_map.json' for i in (1,2,3)],
        'vomaps': [rf'mod\gq004\localization\en-us\vo\gq004_{i:02}.json' for i in (1,2,3)],
    }.items():
        target = registration['localization'].setdefault(category, {}).setdefault('en-us', [])
        target.extend(v for v in values if v not in target)
    p.write_text(yaml.safe_dump(registration, sort_keys=False), encoding='utf-8')


def native_inputs():
    field_path = HERE.parent / 'script/gq004_02_manifest.json'
    field = json.loads(field_path.read_text(encoding='utf-8'))
    for line in field['spoken_lines']:
        line['holocall_speaker'] = line['speaker'] == 'Velvet'
    write(field_path, field)
    shell = json.loads((HERE / 'scenes/gq004_01.scene-spec.json').read_text())
    groups = {'arrive': ['approach', 'recover'], 'recovered': ['recovered'],
              'evidence': ['evidence'], 'archive': ['archive'],
              'upload': ['upload'], 'brand': ['brand'],
              'success': ['success', 'exit'], 'retry': ['interrupted']}
    for name, beats in groups.items():
        spec = copy.deepcopy(shell)
        # Only the physical intro has a deferred-conversation resume entry.
        spec.pop('start_nodes', None)
        spec.pop('entry_points', None)
        spec.update(name=f'gq004_02_{name}', manifest=str(field_path.relative_to(ROOT)).replace('\\', '/'),
            spoken_line_order=[line['key'] for line in field['spoken_lines'] if line['beat'] in beats],
            choice_line_order=[], choices=[], quest_nodes=[], xor_nodes=[],
            sections=[dict(key='field', node_id=2,
                lines=[line['key'] for line in field['spoken_lines'] if line['beat'] in beats], on_end=[dict(node_id=3)])],
            start_node=dict(node_id=1, on_start=[dict(node_id=2)]),
            exit_points=[dict(name='end', node_id=3)], end_nodes=[dict(node_id=3)])
        spec['actors'][0] = dict(key='velvet', name='Velvet', kind='spawn', id=0,
            record='Character.GhostlineVelvet', dynamic_name=f'gq004_field_velvet_{name}',
            # Native mq007_01_gun_found's remote speaker uses this studio
            # marker. The transfer phase keeps its prefab loaded. Kabuki's
            # unstreamed navigation cannot validate a remote field spawn.
            spawn_marker='#holocall_marker', appearance='ghostline_velvet_default', lipsync=0,
            validate_spawn_position=False,
            voicetag=str(fnv1a64('gq_velvet')),
            force_max_visibility=True, always_spawned=True, keep_alive=False)
        if name == 'brand':
            spec.update(line_gap_ms=100, section_tail_padding_ms=100)
        if name == 'success':
            # This starts immediately after the terminating upload attempt.
            # Do not fire its time-zero line while the new remote puppet is
            # still spawning; later lines can otherwise play without it.
            spec['start_node']['on_start'] = [dict(node_id=4, input_name=0, input_ordinal=1)]
            spec['quest_nodes'] = [dict(kind='wait_actor_spawned', node_id=4,
                dynamic_name=f'gq004_field_velvet_{name}', on_out=[dict(node_id=2)])]
        for key, tree in [('raw_path', 'raw'), ('archive_path', 'archive')]:
            spec[key] = f'projects/ghostline/source/{tree}/mod/gq004/scenes/{spec["name"]}.scene' + ('.json' if tree == 'raw' else '')
        write(HERE / f'scenes/gq004_02_{name}.scene-spec.json', spec)
    world_path = HERE / 'world/love-actually.world.json'
    world = json.loads(world_path.read_text())
    from scout import sync_device_markers
    sync_device_markers(world)
    original = json.loads((PROJECT / 'generated/gq004-native-device/accesspoint.ent.json').read_text())
    def patch(value, interaction):
        if isinstance(value, dict):
            if value.get('$type') == 'AccessPointControllerPS':
                value.update(hasPersonalLinkSlot=1, shouldSkipNetrunnerMinigame=1, personalLinkForced=1,
                    personalLinkCustomInteraction={'$type': 'TweakDBID', '$storage': 'string', '$value': interaction})
            if value.get('$type') == 'HackingSkillCheck':
                # An active hacking slot substitutes ActionHacking for the link
                # action, even when the custom caption says Recover/Upload.
                value.update(difficulty='NONE', isActive=0, wasPassed=0)
            for child in list(value.values()): patch(child, interaction)
        elif isinstance(value, list):
            for child in value: patch(child, interaction)
    for device, name in zip(world['devices'], ('recover', 'upload'), strict=True):
        document = copy.deepcopy(original)
        document['Header']['WolvenKitVersion'] = '8.17.4'
        patch(document, 'Interactions.GhostlineLove' + name.title())
        depot = rf'mod\gq004\devices\{name}.ent'
        document['Header']['ArchiveFileName'] = str(PROJECT / 'source/archive' / Path(depot.replace('\\', '/')))
        write(PROJECT / 'source/raw/mod/gq004/devices' / f'{name}.ent.json', document)
        device['entity_template'] = depot
    write(world_path, world)
    tweak = PROJECT / 'source/resources/r6/tweaks/ghostline/gq004_love_actually.yaml'
    text = tweak.read_text()
    if 'Interactions.GhostlineLoveRecover:' not in text:
        text += '\nInteractions.GhostlineLoveRecover:\n  $base: Interactions.ConnectPersonalLink\n  caption: gl_gq004_recover_link\n'
        text += '\nInteractions.GhostlineLoveUpload:\n  $base: Interactions.ConnectPersonalLink\n  caption: gl_gq004_upload_link\n'
        tweak.write_text(text)


if __name__ == '__main__':
    main()
