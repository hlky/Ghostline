"""Native workstation fixtures shared by building layouts and quest stages."""
from __future__ import annotations

import copy
import json
import math
import re
from pathlib import Path

from generate_world import (
    Vec3, DeviceRegistryEntry, build_world_documents, cname, device_registry,
    node_data, node_ref, node_ref_hash, node_ref_u64, vector4,
)

ROOT = Path(__file__).resolve().parents[1]


def quest_fragment(contract):
    """Inputs consumable by existing quest blocks; the quest owns its journal."""
    return dict(schema_version=1, kind='building-quest-binding-fragment',
        layout_id=contract['layout_id'], area_trigger=contract['area'],
        actors=[dict(community=w['community'], entry=w['entry'], phase=w['phase'],
                     workspot=w['workspot'], requires_character_spawned_gate=True)
                for w in contract['workstations']],
        terminal_stages=[dict(id='read_'+w['id']+'_file', type='read_terminal_document',
                            computer=w['computer'], completion_fact=w['read_fact'])
                         for w in contract['workstations']],
        required_from_owning_quest=['phase_resource', 'objective journal path',
                                   'activation and completion lifecycle'],
        cleanup_communities=[w['community'] for w in contract['workstations']])


def compile_workstations(scene, world_point):
    from building_builder import ID, number
    layout = scene['layout']
    items = layout.get('workstations', [])
    if not isinstance(items, list) or len(items) > 8:
        raise ValueError('At most eight workstations are supported')
    modules = {m['id']: m for m in layout.get('modules', [])}
    scene['workstations'] = []
    used = set()
    for item in items:
        identity = item.get('id', '')
        if not ID.fullmatch(identity) or identity in used:
            raise ValueError('Workstation IDs must be unique')
        used.add(identity)
        for key in ('desk', 'chair'):
            if item.get(key) not in modules or modules[item[key]].get('reference_only'):
                raise ValueError('Workstations require placed desk and chair modules')
            from building_library import asset
            if asset(modules[item[key]]['asset']).get('furniture_kind') != key:
                raise ValueError('Workstation desk/chair bindings must match the measured furniture type')
        actor = item['actor']
        if not re.fullmatch(r'Character\.[A-Za-z0-9_]+', actor.get('record', '')):
            raise ValueError('Choose a character record for the office worker')
        if not isinstance(actor.get('active_on_start', True), bool):
            raise ValueError('Actor activation must be boolean')
        resource = actor.get('workspot', '')
        if not resource.startswith('base\\workspots\\') or not resource.endswith('.workspot') or '..' in resource:
            raise ValueError('Choose a vanilla workspot resource')
        resolved = {}
        for key, anchor in (('actor', modules[item['chair']]), ('computer', modules[item['desk']])):
            section = item[key]
            offset = section.get('offset', [0, 0, 0])
            if not isinstance(offset, list) or len(offset) != 3:
                raise ValueError('Workstation offsets need XYZ')
            offset = [number(v, 'Workstation offset', -3, 3) for v in offset]
            yaw = math.radians(anchor.get('yaw', 0))
            position = [anchor['position'][0]+offset[0]*math.cos(yaw)-offset[1]*math.sin(yaw),
                        anchor['position'][1]+offset[0]*math.sin(yaw)+offset[1]*math.cos(yaw),
                        anchor['position'][2]+offset[2]]
            resolved[key] = dict(position=position, yaw=anchor.get('yaw',0)+number(section.get('yaw_offset',0), 'Facing offset', -360,360))
        prefix = f"$/mod/building_lab/#{layout['id']}_content"
        fact = layout['id'].replace('-', '_')+'_'+identity.replace('-', '_')+'_file_read'
        compiled = copy.deepcopy(item)
        compiled.update(community=prefix+'/#'+identity+'_community',
                        seat=prefix+'/#'+identity+'_seat', computer_ref=prefix+'/#'+identity+'_computer',
                        read_fact=fact, level=modules[item['chair']].get('level', 0))
        for key in ('actor', 'computer'):
            compiled[key].update(resolved[key])
            compiled[key]['world_position'] = world_point(compiled[key]['position'], layout['origin'])
            compiled[key]['world_yaw'] = compiled[key]['yaw']+layout['origin']['yaw']
        scene['workstations'].append(compiled)
        from building_library import catalog
        for record in catalog()['assets']:
            if record['role'] != 'equipment' or not record['name'].startswith('monitor_device_d'):
                continue
            position = compiled['computer']['position']
            scene['instances'].append(dict(id='preview:'+identity+':'+record['id'], asset=record['id'], role='module',
                kind='device-preview', name='Computer preview · '+record['name'], reference_only=True, reference_role='equipment',
                appearance=record['appearances'][0], position=position, yaw=compiled['computer']['yaw'], scale=[1,1,1],
                world_position=compiled['computer']['world_position'], world_yaw=compiled['computer']['world_yaw'],
                level=compiled['level'], room=None, edge=None, bounds=record['geometry']))


def content_documents(scene, output):
    """Reuse native community generation; emit independent device registry."""
    items = scene.get('workstations', [])
    if not items:
        return {}, None, None
    layout = scene['layout']
    stem = layout['id']+'_content'
    depot = 'mod\\building_lab\\'+stem
    prefix = '$/mod/building_lab/#'+stem
    from building_builder import world_point
    rooms = layout['rooms']
    xmin,ymin = min(r['x'] for r in rooms),min(r['y'] for r in rooms)
    xmax,ymax = max(r['x']+r['width'] for r in rooms),max(r['y']+r['depth'] for r in rooms)
    zmin = min(r['level']*scene['kit']['storey_height'] for r in rooms)
    zmax = max(r['level']*scene['kit']['storey_height']+r.get('ceiling_height',scene['kit']['wall_height']) for r in rooms)
    centre = world_point([(xmin+xmax)/2,(ymin+ymax)/2,zmin], layout['origin'])
    spec = dict(name=stem, prefab_root=prefix, origin=layout['origin'],
                block_path=depot+'.streamingblock', quest_sector_path=depot+'.streamingsector',
                always_loaded_sector_path=depot+'_always.streamingsector', communities=[],
                triggers=[dict(ref='#office_area', position=centre,
                               yaw=layout['origin']['yaw'], outline=dict(type='rectangle', width=xmax-xmin, depth=ymax-ymin, height=zmax-zmin))])
    for item in items:
        actor = item['actor']
        spec['communities'].append(dict(ref=item['community'], position=actor['world_position'],
            entry='worker', phase='default', period='Day', character=actor['record'],
            appearance=actor['appearance'], active_on_start=actor.get('active_on_start', True),
            always_spawned='true_', spawn_in_view='default__true_',
            spot=dict(ref=item['seat'], position=actor['world_position'], yaw=actor['world_yaw'],
                      workspot=actor['workspot'], is_workspot_infinite=1, is_workspot_static=1,
                      snap_to_ground=0)))
    _, docs = build_world_documents(spec, output/'source/raw', output/'source/archive')
    documents = {p.name.removesuffix('.json'): d for p,d in docs.items()}
    root = documents[stem+'.streamingsector']['Data']['RootChunk']
    # These fixtures stream with the building. A Quest sector is dormant
    # until a quest explicitly enables its prefab, including for active-on-start
    # communities; the shared quest generator intentionally emits that shape.
    root.update(category='Exterior', level=0, cookingPlatform='PLATFORM_PC')
    block_root = documents[stem+'.streamingblock']['Data']['RootChunk']
    block_root['cookingPlatform'] = 'PLATFORM_PC'
    fixture_descriptor = block_root['descriptors'][0]
    fixture_descriptor.update(category='Exterior', level=0, questPrefabNodeRef=node_ref_u64(0))
    documents[stem+'_always.streamingsector']['Data']['RootChunk']['cookingPlatform'] = 'PLATFORM_PC'
    registry = []
    for index,item in enumerate(items):
        # Reviewed vanilla component layout, stripped of all donor quest data.
        donor = ROOT/'projects/experiments/building-lab/encounters/computer-donor.json'
        node = json.loads(donor.read_bytes())
        node['debugName'] = cname(item['id']+'_computer')
        node['appearanceName'] = cname('computer_computer_1')
        def remap(value):
            if isinstance(value, dict):
                for key,child in list(value.items()):
                    if key in ('HandleId','HandleRefId'):
                        value[key] = str(int(child)+index*100000)
                    elif key == 'BufferId':
                        value[key] = str(700+index)
                    else:
                        remap(child)
            elif isinstance(value, list):
                for child in value:
                    remap(child)
        remap(node)
        package = node['instanceData']['Data']['buffer']['Data']
        ps = package['Chunks'][1]['persistentState']['Data']
        ps['computerSetup'] = {'$type':'ComputerSetup','mailsStructure':[], 'filesStructure':[
            {'$type':'gamedeviceGenericDataContent','name':'AKPP Logistics','content':[
                {'$type':'gamedeviceDataElement','title':'Office workstation test',
                 'content':'AKPP Logistics workstation is online. This test file exposes a read fact for quest building blocks.',
                 'wasRead':0,'questInfo':{'$type':'gamedeviceQuestInfo','isHighlighted':1,
                                       'factName':cname(item['read_fact'])}}]}]}
        # Instance handles live in a distinct sector and do not share the
        # architectural/door sector's handle or RedPackage buffer identities.
        holder = {'HandleId':str(10000+index), 'Data':node}
        placement = node_data(len(root['nodes']), node_ref_hash(item['computer_ref']),
                              Vec3(*item['computer']['world_position']), item['computer']['world_yaw'])
        placement['QuestPrefabRefHash'] = node_ref(item['computer_ref'])
        root['nodes'].append(holder)
        root['nodeData']['Data'].append(placement)
        # NodeRef registry is generated in the same format as the community refs.
        root['nodeRefs'].append(node_ref(item['computer_ref']))
        registry.append(DeviceRegistryEntry(item['computer_ref'], node_ref_hash(item['computer_ref']),
                                             'ComputerControllerPS', Vec3(*item['computer']['world_position'])))
    # Bound the descriptor after appending computer placements so every fixture
    # is in its streaming region, including desks moved outside the room bounds.
    positions = [p['Position'] for p in root['nodeData']['Data']]
    fixture_descriptor['streamingBox'] = {'$type':'Box',
        'Min':vector4(Vec3(*(min(p[a] for p in positions)-80 for a in ('X','Y','Z')))),
        'Max':vector4(Vec3(*(max(p[a] for p in positions)+80 for a in ('X','Y','Z'))))}
    name = stem+'.devices'
    documents[name] = device_registry(output/'source/archive/mod/building_lab'/name, registry)
    contract = dict(schema_version=1, layout_id=layout['id'],
        area=prefix+'/#office_area', workstations=[dict(id=i['id'], community=i['community'], entry='worker',
            phase='default', character=i['actor']['record'], workspot=i['seat'], computer=i['computer_ref'],
            controller_class='ComputerControllerPS', read_fact=i['read_fact'],
            active_on_start=i['actor'].get('active_on_start',True)) for i in items])
    return documents, depot+'.streamingblock', contract
