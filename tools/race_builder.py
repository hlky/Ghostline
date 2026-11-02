"""Build native race resources from a Game Scout survey and explicit entrants.

Builds are preview-only unless --publish is requested. Never installs into the game.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import subprocess
import struct
import math

import generate_world
import race_graph
import race_resources
import race_presentation
import race_world
from race_validation import validate_resources
from artifact_io import publish_json_artifacts
from game_scout.core import number as scout_number, ScoutError
from project_layout import project_root, resource_project
from quest_compiler import QuestArtifact, validate_handle_graph, validate_no_forward_handle_refs
from quest_build import _destination_root
from ghostline_red import deserialize as red_deserialize, serialize as red_serialize, ensure_schema
from ghostline_red import DEFAULT_RED_CLI, DEFAULT_RED_SCHEMA
from cr2w_validation import compare_documents

ROOT = Path(__file__).resolve().parents[1]
VANILLA_CHECKPOINT = r'base\quest\minor_quests\mq056\entities\mq056_checkpoint_marker.ent'


def number(value, minimum, maximum, name):
    try:
        return scout_number(value,minimum,maximum,name)
    except ScoutError as error:
        raise ValueError(str(error)) from error


def walk(value):
    if isinstance(value,dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value,list):
        for child in value:
            yield from walk(child)


def checkpoint_comparison(document):
    """Compare package outlines as reflected fields, not world custom buffers.

    The reviewed entity's RedPackage outline has an empty custom buffer and
    stores its real points/height as properties. Keep every field/value in the
    comparison; only bypass the world-node buffer decoder for this layout.
    """
    if document['Data']['RootChunk'].get('$type') != 'entEntityTemplate':
        raise ValueError('Checkpoint readback adapter requires an entity template')
    document = copy.deepcopy(document)
    package = document['Data']['RootChunk'].get('compiledData',{}).get('Data',{})
    for item in walk(package):
        if item.get('$type') == 'AreaShapeOutline' and item.get('buffer','') == '':
            item['$type'] = 'RaceCheckpointPackageOutline'
            item.pop('buffer',None)
    if not any(item.get('$type') == 'DeviceOperationsContainer' for item in walk(document)):
        raise ValueError('Race sign readback requires its device operations container')
    return inline_value_handles(document)


def inline_value_handles(document):
    """Expand acyclic value aliases without dropping fields or wrapper metadata."""
    definitions = {}
    for item in walk(document):
        if 'HandleId' in item:
            key = str(item['HandleId'])
            if key in definitions:
                raise ValueError('Duplicate resource value handle')
            definitions[key] = item['Data']
    def expand(value, active=()):
        if isinstance(value,dict):
            key = value.get('HandleId',value.get('HandleRefId'))
            if key is not None:
                key = str(key)
                if key in {'-1','0'} and key not in definitions:
                    return None
                if key in active or key not in definitions:
                    raise ValueError('Cyclic or unresolved resource value handle')
                data = expand(definitions[key],active+(key,))
                metadata = {k:expand(v,active) for k,v in value.items() if k not in {'HandleId','HandleRefId','Data'}}
                return {'value':data,'wrapper':metadata} if metadata else data
            return {k:expand(v,active) for k,v in value.items()}
        if isinstance(value,list):
            return [expand(v,active) for v in value]
        return value
    # Like the existing access-point clone adapter, compare all inline typed
    # values even when WKit coalesces entity component handles on readback.
    return expand(document)


def activation_comparison(document):
    if document['Data']['RootChunk'].get('$type') != 'scnSceneResource':
        raise ValueError('Activation readback adapter requires a scene resource')
    return inline_value_handles(document)


def native_comparison(document, schema):
    """Canonicalize reader representations without discarding authored values."""
    document=copy.deepcopy(document)
    document['Data'].setdefault('EmbeddedFiles',[])
    root=document['Data']['RootChunk']
    kind=root['$type']
    if kind=='entEntityTemplate':
        # WolvenKit's entity/components views mirror the serialized compiledData.
        root.pop('entity',None)
        root.pop('components',None)
        document=checkpoint_comparison(document)
    elif kind=='scnSceneResource':
        document=activation_comparison(document)
    if kind=='worldStreamingSector':
        # This is a reader-derived view of the authored nodeData/variantIndices,
        # not an additional serialized copy of the world placements.
        root.pop('variantNodes',None)
        # Entity-instance RedPackages store component outlines as properties,
        # unlike world-node outlines whose geometry lives in a custom buffer.
        # Retain every point/height while using the same comparison adapter as
        # standalone entity packages; never decode an empty package buffer.
        for package in walk(root):
            if 'RedPackage' in package.get('Type',''):
                for outline in walk(package.get('Data',{})):
                    if outline.get('$type')=='AreaShapeOutline' and outline.get('buffer','')=='':
                        outline['$type']='RaceCheckpointPackageOutline'
                        outline.pop('buffer',None)
        for name,default in [('persistentNodes',[]),('variantNodes',[]),('cookingPlatform','PLATFORM_None')]:
            root.setdefault(name,default)
        for entry in root.get('nodeData',{}).get('Data',[]):
            for name in ('QuestPrefabRefHash','UkHash1'):
                ref=entry.get(name,{})
                if ref.get('$storage')=='string':
                    ref.update({'$storage':'uint64','$value':str(generate_world.node_ref_hash(ref['$value']))})
            for name in ('MaxStreamingDistance','UkFloat1'):
                if name in entry:entry[name]=struct.unpack('<f',struct.pack('<f',entry[name]))[0]
    def properties(kind):
        fields={}
        visited=set()
        while kind in schema and kind not in visited:
            visited.add(kind)
            definition=schema[kind]
            fields.update(definition.get('properties',{}))
            kind=definition.get('base')
        return fields
    for item in walk(document):
        if item.get('$type')=='NodeRef' and item.get('$storage')=='uint64' and item.get('$value')=='0':
            item.update({'$storage':'string','$value':''})
        if item.get('DepotPath',{}).get('$value')=='0':
            item['Flags']='Default'
        if item.get('BufferId')=='-1' and item.get('Bytes')=='':
            item.pop('BufferId')
        for name,field in properties(item.get('$type')).items():
            if name not in item:continue
            cs=field['cs_type']
            if cs.startswith('CArray<') and item[name] is None:item[name]=[]
            elif cs.startswith('CEnum<') and item[name] in ('true_','false_'):item[name]=item[name][:-1]
            elif item[name] is None and cs in schema:item.pop(name)
    return document


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def identifier(value, label):
    if not isinstance(value,str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,95}',value):
        raise ValueError(f'{label} must be a lowercase identifier')
    return value


def normalize(raw):
    if raw.get('schema_version') != 1:
        raise ValueError('Race builder schema_version must be 1')
    config = copy.deepcopy(raw)
    if config.get('checkpoint_mode', 'custom') not in ('custom', 'vanilla'):
        raise ValueError('checkpoint_mode must be custom or vanilla')
    identifier(config.get('id'),'id')
    if not isinstance(config.get('title'),str) or not config['title'].strip():
        raise ValueError('title is required')
    entrants = config.get('entrants')
    if not isinstance(entrants,list) or not 1 <= len(entrants) <= 12:
        raise ValueError('entrants must contain 1–12 driver/vehicle pairs')
    names,grids = set(),set()
    for entrant in entrants:
        if not isinstance(entrant,dict):
            raise ValueError('Every entrant must be an object')
        eid = identifier(entrant.get('id'),'entrant.id')
        if eid in names:
            raise ValueError('Entrant IDs must be unique')
        names.add(eid)
        entrant.setdefault('passenger',entrant.get('driver'))
        for field,prefix in [('vehicle','Vehicle.'),('driver','Character.'),('passenger','Character.')]:
            if not isinstance(entrant.get(field),str) or not re.fullmatch(re.escape(prefix)+r'[A-Za-z0-9_]+',entrant[field]):
                raise ValueError(f'entrant.{field} must be an explicit {prefix} record')
        grid = entrant.get('grid')
        if isinstance(grid,bool) or not isinstance(grid,int) or grid < 0 or grid in grids:
            raise ValueError('Each entrant needs a distinct non-negative grid order')
        grids.add(grid)
    config['checkpoint_spacing_m'] = number(config.get('checkpoint_spacing_m',40),25,1000,'checkpoint_spacing_m')
    config['countdown_seconds'] = number(config.get('countdown_seconds',3),1,30,'countdown_seconds')
    config['timeout_seconds'] = number(config.get('timeout_seconds',300),10,7200,'timeout_seconds')
    places = config.get('winning_places',1)
    if isinstance(places,bool) or not isinstance(places,int) or not 1 <= places <= len(entrants)+1:
        raise ValueError('winning_places must be between 1 and the total entrant count')
    config['winning_places'] = 1
    if config.get('laps',1) != 1:
        raise ValueError('This builder supports a single ordered course/lap per attempt')
    off = config.setdefault('off_course',{'action':'recover','distance_m':50,'grace_seconds':2})
    if not isinstance(off,dict):
        raise ValueError('off_course must be an object')
    off.update(action='recover',distance_m=50,return_distance_m=40,grace_seconds=2)
    off['distance_m'] = number(off.get('distance_m',50),1,500,'off_course.distance_m')
    off['grace_seconds'] = number(off.get('grace_seconds',2),0.1,30,'off_course.grace_seconds')
    rubber = config.setdefault('rubberband',{})
    if not isinstance(rubber,dict):
        raise ValueError('rubberband must be an object')
    rubber['min_distance'] = number(rubber.get('min_distance',20),0,1000,'rubberband.min_distance')
    rubber['max_distance'] = number(rubber.get('max_distance',150),rubber['min_distance'],2000,'rubberband.max_distance')
    rubber.setdefault('stay_in_front',True)
    if not isinstance(rubber['stay_in_front'],bool):
        raise ValueError('rubberband.stay_in_front must be a boolean')
    reward = config['reward'] = {'item':'Items.money','quantity':10000}
    if not isinstance(reward,dict):
        raise ValueError('reward must be an object')
    if not isinstance(reward.get('item'),str) or not re.fullmatch(r'Items\.[A-Za-z0-9_]+',reward['item']):
        raise ValueError('reward.item must be an Items record')
    quantity = reward.get('quantity')
    if isinstance(quantity,bool) or not isinstance(quantity,int) or not 1 <= quantity <= 1000000:
        raise ValueError('reward.quantity must be an integer from 1 to 1000000')
    return config


def route_checkpoints(world, groups, namespace, spacing_m=40):
    """Station gates by travelled distance, independently of spline vertex count."""
    spline = world['race_splines'][0]
    if spline.get('yaw', 0) != 0 or any(isinstance(p, dict) for p in spline['points']):
        raise ValueError('Checkpoint stationing requires the exported straight-segment race spline')
    points, origin = spline['points'], spline['position']
    segments, length = [], 0.0
    for a, z in zip(points, points[1:]):
        distance = math.dist(a,z)
        if distance:
            segments.append((length,length+distance,a,z))
            length += distance
    if not segments:
        raise ValueError('Race course must have nonzero length')
    def sample(station):
        station = min(station,length)
        start,end,a,z = next((s for s in segments if station <= s[1]),segments[-1])
        ratio = (station-start)/(end-start)
        return ([a[i]+(z[i]-a[i])*ratio for i in range(3)],
                [z[i]-a[i] for i in range(3)])
    old = {item['ref'] for item in groups['checkpoint']}
    old.update(item['trigger_ref'] for item in groups['checkpoint'])
    world['markers'] = [m for m in world['markers'] if m['ref'] not in old]
    world['triggers'] = [m for m in world['triggers'] if m['ref'] not in old]
    stations = []
    station = spacing_m
    while station < length-spacing_m*0.35:
        stations.append(station)
        station += spacing_m
    if not stations:
        stations = [length/2]
    gates = []
    for station in stations:
        point,delta = sample(station)
        _,following = sample(station+25)
        turn = math.degrees(math.atan2(delta[0]*following[1]-delta[1]*following[0],
                                      delta[0]*following[0]+delta[1]*following[1]))
        direction = ('Left' if turn > 0 else 'Right') if abs(turn) >= 20 else 'Forward'
        ref = f'#{namespace}_route_checkpoint_{len(gates)+1:03d}'
        position = {axis:origin[axis]+point[i] for i,axis in enumerate(('x','y','z'))}
        yaw = math.degrees(math.atan2(-delta[0],delta[1])) % 360
        world['markers'].append({'ref':ref,'position':position,'yaw':yaw,'marker_type':'null'})
        world['triggers'].append({'ref':ref+'_trigger','position':position,'yaw':yaw,
            'outline':{'type':'box','width':12,'depth':4,'height':6}})
        gates.append({'ref':ref,'trigger_ref':ref+'_trigger','order':len(gates),
                      'direction':direction})
    groups['checkpoint'] = gates


def survey_bindings(survey, config):
    if survey.get('schema_version') != 1 or survey.get('status') != 'geometry_complete' or survey.get('missing'):
        raise ValueError('Build requires a complete Game Scout race-plan.json export')
    world = copy.deepcopy(survey['world_spec'])
    # Explicit null-marker payloads avoid fresh WolvenKit adding implicit static
    # marker fields that were absent from the survey's generic location markers.
    for marker in world.get('markers',[]):
        marker.setdefault('marker_type','null')
    if len(world.get('race_splines',[])) != 1:
        raise ValueError('Survey must contain exactly one race spline')
    groups = {}
    for item in survey['bindings']:
        groups.setdefault(item['role'],[]).append(item)
    for items in groups.values():
        items.sort(key=lambda item:item['order'])
    for role in ('finish','staging','activation','player_start'):
        if len(groups.get(role,[])) != 1:
            raise ValueError(f'Survey must have exactly one {role} binding')
    if not groups.get('checkpoint') or not groups.get('start_grid'):
        raise ValueError('Survey requires checkpoint and start_grid bindings')
    if any('trigger_ref' not in mark for role in ('finish','staging','checkpoint') for mark in groups[role]):
        raise ValueError('Survey is missing checkpoint/staging/finish trigger geometry')
    route_checkpoints(world,groups,config['id'],config.get('checkpoint_spacing_m',40))
    grid_by_order = {b['order']:b for b in groups['start_grid']}
    markers = {m['ref']:m for m in world['markers']}
    if len(markers) != len(world['markers']):
        raise ValueError('Survey has duplicate marker refs')
    # MQ056 spawns and teleports the owned car to a vehicle AISpot, not a
    # worldSpawnPointMarker. Preserve the surveyed transform and identity.
    player_start_ref = groups['player_start'][0]['ref']
    player_start = markers[player_start_ref]
    world['markers'] = [marker for marker in world['markers']
                        if marker['ref'] != player_start_ref]
    world.setdefault('ai_spots',[]).append({
        'ref':player_start_ref,'position':dict(player_start['position']),
        'yaw':player_start['yaw'],'vehicle_spawn':True,
        'is_workspot_infinite':False,
        'node_data':{'max_streaming_distance':15131.8017578125}})
    ns = config['id']
    # MQ056 uses separate regular and racing splines for the same course.
    world['race_splines'][0]['speed_sections'] = [{'speed_mps':100.0}]
    driving_route = copy.deepcopy(world['race_splines'][0])
    driving_route['ref'] = '#'+ns+'_driving_route'
    world.setdefault('splines',[]).append(driving_route)
    layout = race_world.finish_layout(world,ns,markers[groups['finish'][0]['ref']],
        config['entrants'],groups['finish'][0]['trigger_ref'])
    area = '#'+ns+'_entrants'
    community = {'ref':area,'active_on_start':0,'position':world['origin'],
                 'streaming_distance':15131.8017578125,
                 'node_data':{'max_streaming_distance':15131.8017578125,'streaming_distance':15131.8017578125},
                 'entries':[],'always_spawned':'true_','spawn_in_view':'default__true_'}
    entrants = []
    for entry in config['entrants']:
        if entry['grid'] not in grid_by_order:
            raise ValueError(f'No surveyed start_grid at order {entry["grid"]}')
        grid = markers[grid_by_order[entry['grid']]['ref']]
        model = {'id':entry['id'],'vehicle_entry':entry['id']+'_vehicle',
                 'driver_entry':entry['id']+'_driver','passenger_entry':entry['id']+'_passenger'}
        for kind,record in [('vehicle',entry['vehicle']),('driver',entry['driver']),
                            ('passenger',entry.get('passenger',entry['driver']))]:
            spot = {'ref':f'#{ns}_{entry["id"]}_{kind}_spot','position':dict(grid['position']),
                    'yaw':grid['yaw'],'vehicle_spawn':kind=='vehicle',
                    'node_data':{'max_streaming_distance':15131.8017578125,'streaming_distance':15131.8017578125}}
            if kind!='vehicle':
                # Native racers have individual staging workspots outside the
                # car. Never give an unmounted puppet the vehicle centre.
                side = -2.0 if kind=='driver' else 2.0
                heading = math.radians(grid['yaw'])
                spot['position']['x'] += side*math.cos(heading)
                spot['position']['y'] += side*math.sin(heading)
                spot['workspot'] = (
                    r'base\workspots\common\ground\generic__stand_ground__stand_around__07.workspot')
                if placement := entry.get(kind+'_staging'):
                    spot['position'] = dict(placement['position'])
                    spot['yaw'] = placement.get('yaw',grid['yaw'])
                    spot['workspot'] = placement.get('workspot',spot['workspot'])
            finish_spot = world.get('finish_spots',{}).get(entry['id'],markers[groups['finish'][0]['ref']])
            if kind in finish_spot:
                finish_spot = finish_spot[kind]
            else:
                finish_spot = copy.deepcopy(finish_spot.get('vehicle',finish_spot))
                if kind!='vehicle':
                    side = -1.5 if kind=='driver' else 1.5
                    heading = math.radians(finish_spot['yaw'])
                    finish_spot['position']['x'] += side*math.cos(heading)
                    finish_spot['position']['y'] += side*math.sin(heading)
            finish_spot = {'ref':f'#{ns}_{entry["id"]}_{kind}_finish_spot',
                'position':finish_spot['position'],'yaw':finish_spot['yaw'],
                'vehicle_spawn':kind=='vehicle','phase':'finish',
                'node_data':{'max_streaming_distance':15131.8017578125,'streaming_distance':15131.8017578125}}
            community['entries'].append({'entry':model[kind+'_entry'],'character':record,'active_on_start':0,
                'appearance':entry.get(kind+'_appearance','default'),'spots':[spot,finish_spot],
                'additional_phases':['finish']})
        entrants.append(model)
    world.setdefault('communities',[]).append(community)
    root = world['block_path'].replace('/','\\').rsplit('\\world\\',1)[0]
    world['always_loaded_sector_path'] = root+'\\world\\always_loaded.streamingsector'
    activation_ref = groups['activation'][0]['ref']
    if activation_ref not in markers:
        raise ValueError('Activation workspot marker is missing from the world spec')
    markers[activation_ref].pop('marker_type',None)
    markers[activation_ref]['scene_marker'] = True
    markers[activation_ref]['sector'] = 'always_loaded'
    activation_position = dict(markers[activation_ref]['position'])
    map_ref = '#'+ns+'_race_start_map'
    # MQ056's POI and waiting objective attach to a real GameObject. A null
    # marker supplies a map position but cannot host the dynamic street mappin.
    world.setdefault('entities',[]).append({'ref':map_ref,'position':activation_position,
        'yaw':markers[activation_ref]['yaw'],
        'sector':'always_loaded',
        'node_data':{'max_streaming_distance':15131.8017578125},
        'entity_template':r'base\gameplay\devices\empty_visible_object.ent'})
    journal_path = f'quests/minor_quest/{ns}'
    crowd_ref = '#'+ns+'_spectators'
    crowd = {'ref':crowd_ref,'active_on_start':0,'position':activation_position,
        'always_spawned':'true_','spawn_in_view':'default__true_','entries':[]}
    for i,record in enumerate(['Character.sq024_race_announcer',
            *(['Character.mq056_santo_domingo_crowd_male','Character.mq056_santo_domingo_crowd_female']*3),
            'Character.Silverhand']):
        position = dict(activation_position)
        position['x'] += (i%2)*1.2
        position['y'] += (i//2)*1.5
        entry = 'announcer' if i==0 else 'johnny' if record=='Character.Silverhand' else f'spectator_{i}'
        if entry=='announcer':
            # The interaction can sit against a wall; it is not an NPC spawn.
            # Place the announcer toward the surveyed road/grid, with an
            # authored override available for courses with different geometry.
            grid_position = markers[groups['player_start'][0]['ref']]['position']
            dx = grid_position['x']-activation_position['x']
            dy = grid_position['y']-activation_position['y']
            distance = math.hypot(dx,dy)
            if distance:
                step = min(1.5,distance/2)
                position['x'] += dx/distance*step
                position['y'] += dy/distance*step
        if entry=='johnny':
            position = dict(activation_position)
            heading = math.radians(markers[activation_ref]['yaw'])
            position['x'] += 2*math.cos(heading)
            position['y'] += 2*math.sin(heading)
        position = dict(world.get('race_actor_positions',{}).get(entry,position))
        yaw = world.get('race_actor_yaws',{}).get(entry,markers[activation_ref]['yaw'])
        crowd['entries'].append({'entry':entry,'character':record,'active_on_start':0,
            'appearance':'default','spots':[{'ref':f'#{ns}_{entry}_spot','position':position,
                                             'yaw':yaw}]})
    world['communities'].append(crowd)
    null_areas = []
    route = world['race_splines'][0]
    for i,(a,z) in enumerate(zip(route['points'],route['points'][1:])):
        ref = f'#{ns}_race_crowd_null_{i:03d}'
        null_areas.append({'ref':ref,
            'position':{axis:route['position'][axis]+(a[j]+z[j])/2
                        for j,axis in enumerate(('x','y','z'))},
            'yaw':math.degrees(math.atan2(-(z[0]-a[0]),z[1]-a[1])),
            'outline':{'type':'box','width':30,'depth':math.dist(a,z)+10,'height':12}})
    world['crowd_null_areas'] = null_areas
    bindings = {'id':ns,'community':area,'crowd':crowd_ref,
                'crowd_entries':[entry['entry'] for entry in crowd['entries']],
                'prefab':world['prefab_root'],'depot_root':root,
                'activation':activation_ref,'activation_scene':root+f'\\scenes\\{ns}_activation.scene',
                'spline':world['race_splines'][0]['ref'],'driving_spline':driving_route['ref'],
                'staging':groups['staging'][0]['trigger_ref'],
                'player_start':groups['player_start'][0]['ref'],
                # Resolve the spawn spot inside the running phase's prefab,
                # matching MQ056's phaseInstancePrefabs + local NodeRef pair.
                'player_vehicle_spawn':player_start_ref,
                'finish':groups['finish'][0]['trigger_ref'],
                'checkpoints':[m['trigger_ref'] for m in groups['checkpoint']],
                'entrants':entrants,'journal':journal_path,'objective':journal_path+'/race/finish',
                'activation_map_ref':generate_world.full_node_ref(world['prefab_root'],map_ref),
                'activation_map_position':activation_position,
                'activation_objective':journal_path+'/race/01a_wait_for_race',
                'activation_mappin':journal_path+'/race/01a_wait_for_race/waiting_spot',
                'mount_objective':journal_path+'/race/01_get_in',
                'countdown_objective':journal_path+'/race/01a_wait_for_race1',
                'activation_poi':'points_of_interest/street_race/'+ns+'_start'}
    bindings['countdown_scene'] = root+f'\\scenes\\{ns}_countdown.scene'
    bindings['staging_exit'] = world.get('staging_exit_ref')
    if not bindings['staging_exit']:
        # The native left-start area includes the waiting point and the grid;
        # the interaction's small staging trigger cannot serve this purpose.
        bounds = [markers[activation_ref]['position'],
                  markers[bindings['player_start']]['position'],
                  *[markers[item['ref']]['position'] for item in groups['start_grid']]]
        low = {axis:min(point[axis] for point in bounds) for axis in ('x','y','z')}
        high = {axis:max(point[axis] for point in bounds) for axis in ('x','y','z')}
        bindings['staging_exit'] = '#'+ns+'_left_start_area'
        world['triggers'].append({'ref':bindings['staging_exit'],
            'position':{'x':(low['x']+high['x'])/2,'y':(low['y']+high['y'])/2,
                'z':low['z']-2},'yaw':0,
            'outline':{'type':'box','width':high['x']-low['x']+20,
                'depth':high['y']-low['y']+20,'height':high['z']-low['z']+12}})
    bindings['result_scene'] = root+f'\\scenes\\{ns}_result.scene'
    bindings['crowd_null_areas'] = [area['ref'] for area in null_areas]
    bindings['finish_splines'] = layout['finish_splines']
    bindings['end_area'] = layout['end_area']
    bindings['cleanup_area'] = layout['cleanup_area']
    bindings['checkpoint_visuals'] = []
    bindings['checkpoint_mode'] = config.get('checkpoint_mode', 'custom')
    bindings['checkpoint_entity'] = root+'\\entities\\checkpoint_marker.ent'
    bindings['checkpoint_entities'] = {direction:root+f'\\entities\\checkpoint_{direction.lower()}.ent'
                                       for direction in ('Forward','Left','Right','Finish')}
    if bindings['checkpoint_mode'] == 'vanilla':
        bindings['checkpoint_entity'] = VANILLA_CHECKPOINT
        bindings['checkpoint_entities'] = dict.fromkeys(('Forward','Left','Right','Finish'), VANILLA_CHECKPOINT)
    for checkpoint in groups['checkpoint']:
        marker = markers[checkpoint['ref']]
        ref = checkpoint['ref']+'_visual'
        bindings['checkpoint_visuals'].append(ref)
        world['entities'].append({'ref':ref,'position':marker['position'],'yaw':marker['yaw'],
                                 'entity_template':bindings['checkpoint_entities'][checkpoint['direction']],
                                 'checkpoint_direction':checkpoint['direction'],
                                 'checkpoint_trigger':checkpoint['trigger_ref']})
    finish = markers[groups['finish'][0]['ref']]
    drop = layout['reward_drop']
    bindings['reward_crate'] = '#'+ns+'_reward_crate'
    bindings['reward_objective'] = journal_path+'/race/04_get_reward'
    bindings['reward_mappin'] = bindings['reward_objective']+'/reward_crate'
    bindings['courier'] = '#'+ns+'_courier'
    bindings['courier_bike'] = '#'+ns+'_courier_bike'
    bindings['courier_spline'] = layout['courier_spline']
    bindings['courier_trigger'] = layout['courier_trigger']
    bindings['courier_workspot'] = layout['courier_workspot']
    for ref,record,vehicle,appearance in (
            (bindings['courier'],'139946753417',False,None),
            (bindings['courier_bike'],'146084740299',True,'brennan_apollo_basic_adventure_01_1')):
        arrival = layout['courier_bike_start'] if vehicle else layout['courier_start']
        world['entities'].append({'ref':ref,'position':arrival['position'],'yaw':arrival['yaw'],
            'population_record':record,'is_vehicle':vehicle,
            **({'appearance':appearance} if appearance else {})})
    world['entities'].append({'ref':bindings['reward_crate'],
        'position':drop['position'],'yaw':drop['yaw'],
        'entity_template':r'base\gameplay\loot\containers\crates\crate_small.ent',
        'appearance':'crate_small_default'})
    bindings['finish_visual'] = groups['finish'][0]['ref']+'_visual'
    world['entities'].append({'ref':bindings['finish_visual'],'position':finish['position'],
        'yaw':finish['yaw'],'entity_template':bindings['checkpoint_entities']['Finish'],
        'checkpoint_direction':'Finish','checkpoint_trigger':bindings['finish']})
    # Native race splines must remain available after leaving their origin.
    # Default point-sized node bounds and 120 m streaming cut them mid-course.
    for spline in [*world.get('race_splines',[]),*world.get('splines',[])]:
        spline.setdefault('node_data',{}).update(
            max_streaming_distance=15131.8017578125,streaming_distance=15131.8017578125)
    race_world.author(world,bindings)
    bindings['variants']['crate'] = [bindings['reward_crate']]
    # Refuse tampered exports whose bindings do not actually exist in the world spec.
    refs = {x['ref'] for key in ('markers','triggers','race_splines','splines','ai_spots','entities')
            for x in world.get(key,[])}
    for ref in [bindings['spline'],bindings['staging'],bindings['staging_exit'],bindings['finish'],*bindings['checkpoints'],
                *bindings['finish_splines'].values(),bindings['end_area'],bindings['cleanup_area'],bindings['courier_spline'],
                bindings['courier_trigger'],bindings['courier_workspot']]:
        if ref not in refs:
            raise ValueError(f'Survey binding has no world resource: {ref}')
    return world,bindings


def journal(config, bindings, archive):
    return race_resources.journal(config, archive, bindings)


def validate_activation_graph(scene):
    """Check scene boundaries and the actor table used on scene acquisition."""
    root = scene['Data']['RootChunk']
    actors = [*root['actors'], *root['playerActors']]
    actor_ids = [actor['actorId']['id'] for actor in actors]
    if actor_ids != list(range(len(actors))):
        raise ValueError('Activation scene actor IDs must match contiguous table slots starting at zero')
    performers = {actor_id * 256 + 1 for actor_id in actor_ids}
    for item in walk(root):
        if item.get('$type') == 'scnActorId' and item['id'] != 4294967295 and item['id'] not in actor_ids:
            raise ValueError(f'Activation scene references missing actor {item["id"]}')
        if item.get('$type') == 'scnPerformerId' and item['id'] != 4294967040 and item['id'] not in performers:
            raise ValueError(f'Activation scene references missing performer {item["id"]}')
    graph = root['sceneGraph']['Data']
    nodes = {item['Data']['nodeId']['id']: item['Data'] for item in graph['graph']}
    if len(nodes) != len(graph['graph']):
        raise ValueError('Activation scene has duplicate node IDs')
    options = {option['itemId']['id']: option for option in root['screenplayStore']['options']}
    instances = {instance['workspotInstanceId']['id']: instance for instance in root['workspotInstances']}
    workspots = {spot['Data']['dataId']['id'] for spot in root['workspots']}
    event_ids = set()
    for node_id, node in nodes.items():
        sockets = node.get('outputSockets', [])
        socket_stamps = {(socket['stamp']['name'], socket['stamp']['ordinal']) for socket in sockets}
        if len(socket_stamps) != len(sockets):
            raise ValueError(f'Activation node {node_id} has duplicate socket stamps')
        for socket in sockets:
            for destination in socket['destinations']:
                target = nodes.get(destination['nodeId']['id'])
                if target is None:
                    raise ValueError(f'Activation node {node_id} targets a missing node')
                if target['$type'] == 'scnQuestNode':
                    stamp = destination['isockStamp']
                    if stamp['name'] != 0 or not 0 <= stamp['ordinal'] < len(target['isockMappings']):
                        raise ValueError(f'Activation node {node_id} targets an invalid quest input')
        if node['$type'] == 'scnChoiceNode':
            if node['mode'] in ('attachToWorld', 'attachToGameObject'):
                for field, kind in [('shapeParams', 'scnInteractionShapeParams'),
                                    ('lookAtParams', 'scnChoiceNodeNsBasicLookAtParams'),
                                    ('mappinParams', 'scnChoiceNodeNsMappinParams')]:
                    if (node.get(field) or {}).get('Data', {}).get('$type') != kind:
                        raise ValueError(f'World choice {node_id} requires {field} ({kind})')
            if len(sockets) != len(node['options']) + 6:
                raise ValueError(f'Activation choice {node_id} has invalid socket padding')
            for option in node['options']:
                if option['screenplayOptionId']['id'] not in options:
                    raise ValueError(f'Activation choice {node_id} has a missing screenplay option')
        if node['$type'] == 'scnSectionNode':
            duration = node['sectionDuration']['stu']
            for wrapper in node['events']:
                event = wrapper['Data']
                if 'type' in event:
                    raise ValueError('Scene events must not serialize unnamed scnEventType enum values')
                event_id = event['id']['id']
                if event_id in event_ids:
                    raise ValueError('Activation scene has duplicate event IDs')
                event_ids.add(event_id)
                if not 0 <= event['startTime'] < duration or event['startTime'] + event['duration'] > duration:
                    raise ValueError(f'Activation section {node_id} has an event outside its duration')
                if event['$type'] == 'scneventsSocket':
                    stamp = event['osockStamp']
                    if (stamp['name'], stamp['ordinal']) not in socket_stamps:
                        raise ValueError(f'Activation section {node_id} emits an undeclared socket')
        if node['$type'] == 'scnQuestNode':
            quest = node['questNode']['Data']
            if quest['$type'] == 'questUseWorkspotNodeDefinition':
                params = quest['paramsV1']['Data']
                if params.get('function', 'UseWorkspot') == 'UseWorkspot':
                    instance = instances.get(params.get('workspotInstanceId', {}).get('id'))
                    if params['$type'] != 'scnUseSceneWorkspotParamsV1' or instance is None:
                        raise ValueError('Scene workspot start requires valid scene-instance parameters')
                    if instance['dataId']['id'] not in workspots:
                        raise ValueError('Scene workspot instance references missing workspot data')
    for collection, expected in (('startNodes', 'scnStartNode'), ('endNodes', 'scnEndNode')):
        for reference in graph[collection]:
            node_id = reference['id']
            if node_id not in nodes:
                raise ValueError(f'Activation scene {collection} references missing node {node_id}')
            if nodes[node_id]['$type'] != expected:
                raise ValueError(f'Activation scene {collection} node {node_id} must be {expected}')
        declared = {reference['id'] for reference in graph[collection]}
        actual = {node_id for node_id, node in nodes.items() if node['$type'] == expected}
        if declared != actual:
            raise ValueError(f'Activation scene {collection} does not match its graph boundaries')
    for collection, boundary in (('entryPoints', 'startNodes'), ('exitPoints', 'endNodes')):
        declared = {reference['id'] for reference in graph[boundary]}
        for point in root[collection]:
            if point['nodeId']['id'] not in declared:
                raise ValueError(f'Activation scene {collection} references an undeclared boundary')


def documents(raw, survey, project, target):
    config = normalize(raw)
    world,bindings = survey_bindings(survey,config)
    if resource_project(world['block_path']).resolve() != project.resolve():
        raise ValueError('Survey depot ownership does not match the selected project')
    root,ns = bindings['depot_root'],config['id']
    depots = {name:root+f'\\phases\\{ns}_{name}.questphase'
              for name in ('root','lifecycle','preparation','attempt')}
    bindings['preparation_phase'] = depots['preparation']
    archive = lambda depot: target/'source/archive'/depot.replace('\\','/')
    generated,world_docs = generate_world.build_world_documents(world,target/'source/raw',target/'source/archive')
    by_depot = {f.depot_path:world_docs[f.raw_path] for f in generated}
    race_world.variants(by_depot,world,bindings)
    if bindings['checkpoint_mode'] == 'vanilla':
        race_world.checkpoint_instances(by_depot,world,bindings)
    for doc in by_depot.values():
        sector = doc['Data']['RootChunk']
        if sector.get('$type') == 'worldStreamingSector':
            for node,ref in zip(sector['nodes'],sector['nodeRefs']):
                if ref['$value'].split('/')[-1] in [*bindings['checkpoint_visuals'],bindings['finish_visual']]:
                    node['Data']['isVisibleInGame'] = 0
    if bindings['checkpoint_mode'] != 'vanilla':
        for direction,depot in bindings['checkpoint_entities'].items():
            by_depot[depot] = race_resources.checkpoint(config,archive(depot),direction=direction)
    scene = race_resources.activation(config,archive(bindings['activation_scene']),bindings)
    validate_activation_graph(scene)
    by_depot[bindings['activation_scene']] = scene
    for name,result in [('countdown_scene',False),('result_scene',True)]:
        by_depot[bindings[name]] = race_presentation.presentation(config,archive(bindings[name]),bindings,result=result)
    by_depot[depots['attempt']] = race_graph.attempt(config,bindings,archive(depots['attempt']))
    by_depot[depots['preparation']] = race_graph.preparation(config,bindings,archive(depots['preparation']))
    by_depot[depots['lifecycle']] = race_graph.lifecycle(config,bindings,archive(depots['lifecycle']),depots['attempt'])
    by_depot[depots['root']] = race_graph.root(config,bindings,archive(depots['root']),depots['lifecycle'])
    journal_depot = root+f'\\journal\\{ns}.journal'
    onscreens = root+f'\\localization\\en-us\\onscreens\\{ns}.json'
    by_depot[journal_depot] = race_resources.journal(config,archive(journal_depot),bindings)
    by_depot[onscreens] = race_resources.onscreens(config,archive(onscreens))
    for depot,doc in by_depot.items():
        if resource_project(depot).resolve() != project.resolve():
            raise ValueError(f'Generated resource belongs to another project: {depot}')
        validate_handle_graph(doc,context=depot)
        validate_no_forward_handle_refs(doc,context=depot)
    validate_resources(by_depot,bindings)
    registration = {'quest':{'phases':[{'parent':r'base\quest\cyberpunk2077.quest','path':depots['root']}]},
                    'streaming':{'blocks':[world['block_path']]},'journal':[journal_depot],
                    'localization':{'onscreens':{'en-us':[onscreens]}}}
    return config,bindings,by_depot,registration


def convert_resources(artifacts, project, destination, *, red_cli=DEFAULT_RED_CLI, schema=DEFAULT_RED_SCHEMA):
    """Write and verify CR2W with ghostline-red; conversion errors are terminal."""
    schema = ensure_schema(red_cli,schema)
    reflected = load(schema)
    for artifact in artifacts:
        relative = artifact.archive_path.relative_to(project/'source/archive')
        binary = destination/'source/archive'/relative
        raw = destination/'source/raw'/Path(str(relative)+'.json')
        raw.parent.mkdir(parents=True,exist_ok=True)
        raw.write_text(json.dumps(artifact.document),encoding='utf-8')
        red_deserialize(raw,binary,red_cli=red_cli,schema=schema)
        decoded = binary.with_name(binary.name+'.readback.json')
        red_serialize(binary,decoded,red_cli=red_cli,schema=schema)
        comparison = compare_documents(native_comparison(artifact.document,reflected),
                                       native_comparison(load(decoded),reflected),schema=reflected)
        if not comparison.ok:
            details = '; '.join(error['path'] for error in comparison.errors[:8])
            raise ValueError(f'ghostline-red readback differs for {relative}: {details}')


def race_packaging(project, target, depots, tweak_path):
    """Include the generated label records in every profile shipping this race."""
    profiles = load(project/'packaging/profiles.json')
    if profiles.get('schema_version') != 1:
        raise ValueError('Race packaging requires project-local schema_version 1 profiles')
    selected = []
    for name, profile in profiles['profiles'].items():
        quests = [*profile.get('active_quests', []), *profile.get('support_quests', [])]
        prefixes = [f'mod/{quest}/' for quest in quests]
        excluded = profile.get('exclude_prefixes', [])
        includes_race = any(
            (profile.get('include_all') or any(depot.startswith(prefix) for prefix in prefixes))
            and not any(depot.startswith(prefix) for prefix in excluded)
            for depot in (path.replace('\\','/') for path in depots))
        if not includes_race:
            continue
        if tweak_path in profile.get('exclude_loose', []):
            profile['exclude_loose'].remove(tweak_path)
        loose = profile.setdefault('include_loose', [])
        if tweak_path not in loose:
            loose.append(tweak_path)
        selected.append(name)
    if not selected:
        raise ValueError('No project packaging profile includes the generated race resources')
    return target/'packaging/profiles.json', profiles, selected


def build(spec_path, *, project=None, output_root=None, publish=False, deserialize=False,
          red_cli=DEFAULT_RED_CLI, schema=DEFAULT_RED_SCHEMA):
    spec_path = Path(spec_path).resolve()
    raw = load(spec_path)
    survey_path = (spec_path.parent/raw['survey']).resolve()
    survey = load(survey_path)
    project = project_root(project) if project else resource_project(survey['world_spec']['block_path'])
    ns = identifier(raw.get('id'),'id')
    if publish and output_root is not None:
        raise ValueError('Use --publish or --output-root, not both')
    target = project if publish else _destination_root(Path(output_root or project/'generated/races'/ns),project)
    config,bindings,by_depot,registration = documents(raw,survey,project,target)
    tweak_path = f'r6/tweaks/{ns}.yaml'
    packaging_path, packaging, packaging_profiles = race_packaging(project,target,by_depot,tweak_path)
    artifacts = [QuestArtifact(project/'source/raw'/(depot.replace('\\','/')+'.json'),
                               project/'source/archive'/depot.replace('\\','/'),doc) for depot,doc in by_depot.items()]
    loose = {
        # JSON is valid YAML and requires no extra dependency in Game Scout's environment.
        target/f'source/resources/{ns}.archive.xl':(json.dumps(registration,indent=2)+'\n').encode(),
        target/'source/resources'/tweak_path:(json.dumps({
            'Mappins.'+ns+'_start':{'$type':'RacingMappin','title':ns+'_title',
                                    'description':ns+'_description'}},indent=2)+'\n').encode(),
    }
    receipt = {'schema_version':1,'id':ns,'project':str(project),'output_root':str(target),
               'survey_sha256':hashlib.sha256(survey_path.read_bytes()).hexdigest(),
               'spec_sha256':hashlib.sha256(spec_path.read_bytes()).hexdigest(),
               'resources':list(by_depot),'bindings':bindings,'binary_conversion':deserialize,
               'serializer':'ghostline-red',
               'runtime_verified':False,'dependencies':['ArchiveXL','TweakXL'],
               'packaging':{'profiles':packaging_profiles,'include_loose':[tweak_path]},
               'facts':{'abort':ns+'_abort','result':ns+'_result','settled':ns+'_settled'},
               'result_values':{'success':1,'failure':2,'aborted':3},
               'shared_interfaces':['sq024_current_race_checkpoint_fact_add',
                   'mq056_johnny_talking','mq056_johnny_speed_vo','mq056_johnny_you_ready',
                                    'sq024_current_race_player_position','RacePlayerDistanceFromSpline'],
               'scope':'MQ056 replay lifecycle; phase-owned preparation, gated countdown, native device checkpoints, recovery, result commentary, cleanup and immediate initial/replay availability',
               'remaining_runtime_checks':['opponent spawn/mount and registration',
                   'checkpoint progression and finish ordering','unmount/abort/prevention cleanup and replay reset',
                   'save/load and reward delivery']}
    if deserialize:
        staging = project/'generated/race-conversion'
        staging.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=staging,prefix=ns+'-') as folder:
            candidate = Path(folder)
            convert_resources(artifacts,project,candidate,red_cli=red_cli,schema=schema)
            for depot in by_depot:
                relative = depot.replace('\\','/')
                loose[target/'source/archive'/relative] = (candidate/'source/archive'/relative).read_bytes()
    final_docs = {target/'source/raw'/(depot.replace('\\','/')+'.json'):doc for depot,doc in by_depot.items()}
    final_docs.update({target/'race-build.json':receipt,target/'race.world.json':survey_bindings(survey,config)[0]})
    final_docs[packaging_path] = packaging
    publish_json_artifacts(final_docs,binary_artifacts=loose,
                           ownership_path=target/'generated/race-builds'/ns/'ownership.json')
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('validate','build'))
    parser.add_argument('--spec',required=True,type=Path)
    parser.add_argument('--project')
    parser.add_argument('--output-root',type=Path)
    parser.add_argument('--publish',action='store_true')
    parser.add_argument('--deserialize',action='store_true')
    parser.add_argument('--red-cli',type=Path,default=DEFAULT_RED_CLI)
    parser.add_argument('--schema',type=Path,default=DEFAULT_RED_SCHEMA)
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate':
            spec = load(args.spec)
            survey = load(args.spec.resolve().parent/spec['survey'])
            project = project_root(args.project) if args.project else resource_project(survey['world_spec']['block_path'])
            config,bindings,docs,_ = documents(spec,survey,project,project/'generated/races/validation')
            result = {'valid':True,'id':config['id'],'resource_count':len(docs),'bindings':bindings}
        else:
            result = build(args.spec,project=args.project,output_root=args.output_root,publish=args.publish,
                           deserialize=args.deserialize,red_cli=args.red_cli,schema=args.schema)
        print(json.dumps(result,indent=2))
        return 0
    except (ValueError,KeyError,OSError,TypeError,subprocess.CalledProcessError) as error:
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
