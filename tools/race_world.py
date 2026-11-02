"""Course-owned world variants and native road guidance, authored directly."""
import math
import zlib
from generate_scene import cname, node_ref
from generate_world import node_ref_hash
from race_resources import transform


def checkpoint_instances(documents, world, bindings):
    """Use MQ056's stock template with sector-owned component overrides.

    CRUIDs identify ui_back/ui_front/trigger in the shipped MQ056 template.
    The two widget overrides follow vanilla quest_47de76de8df02b3e; the trigger
    is sized to our authored gate but stays disabled; separate quest areas
    register crossings, so the stock device cannot duplicate the counter.
    No entity template or ArchiveXL resource patch is emitted.
    """
    placements = {item['ref']:item for item in world['entities']
                  if 'checkpoint_direction' in item}
    triggers = {item['ref']:item for item in world['triggers']}
    def walk(value):
        if isinstance(value,dict):
            yield value
            for child in value.values():
                yield from walk(child)
        elif isinstance(value,list):
            for child in value:
                yield from walk(child)
    for document in documents.values():
        sector = document['Data']['RootChunk']
        if sector.get('$type') != 'worldStreamingSector':
            continue
        handle = max((int(item['HandleId']) for item in walk(document)
                      if 'HandleId' in item),default=0)
        buffer_id = max((int(item['BufferId']) for item in walk(document)
                         if 'BufferId' in item),default=0)
        def wrap(data):
            nonlocal handle
            handle += 1
            return {'HandleId':str(handle),'Data':data}
        for node,reference in zip(sector['nodes'],sector['nodeRefs']):
            placement = placements.get(reference['$value'].rsplit('/',1)[-1])
            if placement is None:
                continue
            direction = placement['checkpoint_direction']
            record = 'LCDScreens.RaceFinish' if direction=='Finish' else 'LCDScreens.RaceCheckpoint'+direction
            chunks = [{'$type':'StreetSignWidgetComponent','signSelector':wrap({
                '$type':'RaceCheckpointSelector','recordID':{
                    '$type':'TweakDBID','$storage':'string','$value':record}})} for _ in range(2)]
            outline = triggers[placement['checkpoint_trigger']]['outline']
            width,depth = outline['width']/2,outline['depth']/2
            chunks.append({'$type':'gameStaticTriggerAreaComponent','isEnabled':0,
                'localTransform':transform(-2), 'outline':wrap({
                    '$type':'AreaShapeOutline','buffer':'','height':outline['height'],
                    'points':[{'$type':'Vector3','X':x,'Y':y,'Z':0}
                              for x,y in [(-width,-depth),(width,-depth),(width,depth),(-width,depth)]]})})
            buffer_id += 1
            node['Data']['instanceData'] = wrap({'$type':'entEntityInstanceData','buffer':{
                'BufferId':str(buffer_id),'Flags':4063232,
                'Type':'WolvenKit.RED4.Archive.Buffer.RedPackage, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null',
                'Data':{'Version':4,'Sections':7,'CruidIndex':-1,
                    'CruidDict':{'0':'2451685433260048384','1':'2451685433209716736',
                                 '2':'1734314053524791296'},'Chunks':chunks}}})


def finish_layout(world, namespace, finish, entrants, finish_trigger):
    """Give each native finish role its own resource, including unspecialised surveys."""
    origin = dict(finish['position'])
    angle = math.radians(finish['yaw'])
    forward = (-math.sin(angle),math.cos(angle))
    right = (math.cos(angle),math.sin(angle))
    width = float(world['race_splines'][0].get('width_default',8.0))
    # A stopping area must be surveyed independently of the cleanup volume.
    # Never invent one from the finish position or reuse the finish trigger.
    stopping = world.get('finish_vehicle_forbidden_area')
    if stopping is not None:
        values = [float(stopping['position'][axis]) for axis in ('x','y','z')]
        values.extend((float(stopping['yaw']),float(stopping.get('speed_limit',20.0))))
        for key in ('outline','inner_outline'):
            outline = stopping[key]
            if outline.get('type') != 'box':
                raise ValueError('Finish vehicle-forbidden outlines must be surveyed boxes')
            dimensions = [float(outline[axis]) for axis in ('width','depth','height')]
            if any(not math.isfinite(value) or value <= 0 for value in dimensions):
                raise ValueError('Finish vehicle-forbidden dimensions must be finite and positive')
        if not all(math.isfinite(value) for value in values) or values[-1] <= 0:
            raise ValueError('Finish vehicle-forbidden transform and speed limit must be finite; speed must be positive')
        if any(float(stopping['inner_outline'][axis]) > float(stopping['outline'][axis])
               for axis in ('width','depth','height')):
            raise ValueError('Finish inner stopping box must fit inside its outer box')
        relative = math.radians(float(stopping['yaw'])-float(finish['yaw']))
        half_extent = (abs(math.sin(relative))*float(stopping['outline']['width'])
                       +abs(math.cos(relative))*float(stopping['outline']['depth']))/2
        ahead = sum((float(stopping['position'][axis])-origin[axis])*forward[i]
                    for i,axis in enumerate(('x','y')))
        crossing = next(item for item in world['triggers'] if item['ref']==finish_trigger)
        crossing_outline = crossing['outline']
        if crossing_outline.get('type') != 'box':
            raise ValueError('Finish stopping-area clearance requires a box finish trigger')
        crossing_angle = math.radians(float(crossing.get('yaw',0))-float(finish['yaw']))
        crossing_edge = sum((crossing['position'][axis]-origin[axis])*forward[i]
                            for i,axis in enumerate(('x','y')))
        crossing_edge += (abs(math.sin(crossing_angle))*float(crossing_outline['width'])
                          +abs(math.cos(crossing_angle))*float(crossing_outline['depth']))/2
        if ahead-half_extent <= crossing_edge:
            raise ValueError('The entire finish stopping area must be beyond the finish crossing in its forward direction')
    def position(ahead, side=0):
        return {'x':origin['x']+ahead*forward[0]+side*right[0],
                'y':origin['y']+ahead*forward[1]+side*right[1],'z':origin['z']}
    def spline(ref, positions, speed_sections=None):
        item = {'ref':ref,'position':dict(origin),'yaw':0,
            'points':[[p[axis]-origin[axis] for axis in ('x','y','z')] for p in positions],
            'looped':False}
        if speed_sections is not None:
            item['speed_sections'] = speed_sections
        world.setdefault('splines',[]).append(item)
    def area(ref, centre, area_width, depth):
        world['triggers'].append({'ref':ref,'position':centre,'yaw':finish['yaw'],
            'outline':{'type':'box','width':area_width,'depth':depth,'height':12}})
    parking = world.setdefault('finish_spots',{})
    routes = dict(world.get('finish_splines',{}))
    for i,entrant in enumerate(entrants):
        name = entrant['id']
        if name not in parking:
            parking[name] = {'position':position(10*(i+1),(-1 if i%2 else 1)*width/4),
                             'yaw':finish['yaw']}
        endpoint = parking[name].get('vehicle',parking[name])['position']
        if name not in routes:
            ref = f'#{namespace}_{name}_finish_parking'
            middle = {axis:(origin[axis]+endpoint[axis])/2 for axis in ('x','y','z')}
            spline(ref,[origin,middle,endpoint])
            routes[name] = ref
    if any(ref==world['race_splines'][0]['ref'] for ref in routes.values()):
        raise ValueError('Finish parking must have its own spline, not the race spline')
    if len(set(routes.values()))!=len(routes):
        raise ValueError('Each entrant must have its own finish parking spline')
    end_area = world.get('end_area_ref')
    if not end_area:
        end_area = f'#{namespace}_finish_cleanup_area'
        depth = max(80.0,len(entrants)*10.0+40.0)
        area(end_area,position(depth/2-20),width*2+12,depth)
    cleanup_area = world.get('final_cleanup_area_ref')
    if not cleanup_area:
        cleanup_area = f'#{namespace}_final_cleanup_area'
        exit_area = next(item for item in world['triggers'] if item['ref']==end_area)
        outline = exit_area['outline']
        centre = dict(exit_area['position'])
        centre['z'] -= 2
        world['triggers'].append({'ref':cleanup_area,'position':centre,
            'yaw':exit_area.get('yaw',finish['yaw']),
            'outline':{'type':'box','width':float(outline.get('width',width*2+12))+20,
                'depth':float(outline.get('depth',max(80,len(entrants)*10+40)))+20,
                'height':float(outline.get('height',12))+4}})
    drop = world.get('reward_drop',{'position':position(0,width/2),'yaw':finish['yaw']})
    courier = world.get('courier_start',{'position':{
        axis:drop['position'][axis]+(forward[j] if j<2 else 0)
        for j,axis in enumerate(('x','y','z'))},'yaw':finish['yaw']})
    bike = world.get('courier_bike_start',{'position':position(8,width/2),
                                         'yaw':finish['yaw']})
    delivery_area = world.get('courier_trigger_ref')
    if not delivery_area:
        delivery_area = f'#{namespace}_reward_pickup_area'
        area(delivery_area,dict(drop['position']),8.0,8.0)
    departure = world.get('courier_spline')
    if not departure:
        departure = f'#{namespace}_courier_departure'
        points = [bike['position'],position(20,width/4),position(max(80,len(entrants)*10+30),width/4)]
        length = sum(math.dist([a[k] for k in ('x','y','z')],[z[k] for k in ('x','y','z')])
                     for a,z in zip(points,points[1:]))
        spline(departure,points,[{'start':0,'end':10,'speed_mps':5.555555820465088},
            {'start':10,'end':length,'speed_mps':25.000001907348633}])
    if departure==world['race_splines'][0]['ref'] or departure in routes.values():
        raise ValueError('Courier departure must be separate from race and parking splines')
    if len({finish_trigger,end_area,cleanup_area,delivery_area})!=4:
        raise ValueError('Finish crossing, finish exit, final cleanup and reward pickup must use separate areas')
    workspot = f'#{namespace}_courier_wait'
    world.setdefault('ai_spots',[]).append({'ref':workspot,'position':courier['position'],
        'yaw':courier['yaw'],'workspot':
        r'base\workspots\archetype\dirt\common\wall\dirt__stand_wall_lean_back__stand_around__01.workspot'})
    return {'finish_splines':routes,'end_area':end_area,'cleanup_area':cleanup_area,'reward_drop':drop,
            'courier_start':courier,'courier_bike_start':bike,'courier_spline':departure,
            'courier_trigger':delivery_area,'courier_workspot':workspot}


def author(world, bindings):
    ns = bindings['id']
    groups = {'barriers':[], 'gps_path':[],
              'checkpoints':list(bindings['checkpoint_visuals']),
              'checkpoints2':[bindings['finish_visual']]}
    # Preserve authored road edges. GPS points describe a route, not isolated
    # single-arrow placements; tile guidance between them along that route.
    assets = {
        'gps_path':r'base\quest\side_quests\sq024\entities\sq024_gps_path.ent',
        'barriers':r'base\items\interactive\public_utility\int_public_utility_002__road_barrier_a_poor.ent'}
    dressing = world.get('race_dressing')
    if dressing is None:
        route = world['race_splines'][0]
        points,origin = route['points'],route['position']
        guidance = []
        for i,point in enumerate(points):
            a,z = (point,points[i+1]) if i+1<len(points) else (points[i-1],point)
            guidance.append({'position':{axis:origin[axis]+point[j]
                for j,axis in enumerate(('x','y','z'))},
                'yaw':math.degrees(math.atan2(-(z[0]-a[0]),z[1]-a[1]))})
        dressing = {'gps_path':guidance,'barriers':[]}
    for kind,placements in dressing.items():
        if kind not in assets:
            raise ValueError(f'Unsupported race dressing group: {kind}')
        if kind == 'gps_path' and len(placements) > 1:
            spacing = float(world.get('race_guidance_spacing_m',3.0))
            if spacing <= 0:
                raise ValueError('Race guidance spacing must be positive')
            guidance = []
            for start,end in zip(placements,placements[1:]):
                a,z = start['position'],end['position']
                delta = {axis:z[axis]-a[axis] for axis in ('x','y','z')}
                distance = math.sqrt(sum(value*value for value in delta.values()))
                if distance == 0:
                    continue
                count = max(1,math.ceil(distance/spacing))
                yaw = math.degrees(math.atan2(-delta['x'],delta['y']))
                for step in range(count):
                    guidance.append({'position':{axis:a[axis]+delta[axis]*step/count
                        for axis in ('x','y','z')},'yaw':yaw})
            placements = [*guidance,placements[-1]]
        for i,placement in enumerate(placements):
            ref = f'#{ns}_{kind}_{i}'
            world['entities'].append({'ref':ref,'position':dict(placement['position']),
                'yaw':placement['yaw'],'entity_template':assets[kind]})
            groups[kind].append(ref)
    bindings['variants'] = groups
    markers = {marker['ref']:marker for marker in world['markers']}
    for name,placement in (('race_crowd_start',markers[bindings['activation']]),
                           ('race_crowd_finish',world['finish_spots'][bindings['entrants'][0]['id']])):
        placement = placement.get('vehicle',placement)
        # MQ056 has two medium start emitters and four finish emitters.
        sizes = ('medium','medium') if name=='race_crowd_start' else ('medium','big','medium','small')
        angle = math.radians(placement['yaw'])
        defaults = []
        for i,size in enumerate(sizes):
            position = dict(placement['position'])
            side,ahead = (-6 if i%2==0 else 6),(i//2)*12
            position['x'] += side*math.cos(angle)-ahead*math.sin(angle)
            position['y'] += side*math.sin(angle)+ahead*math.cos(angle)
            defaults.append({'position':position,'yaw':placement['yaw'],
                'event':'amb_ext_crowd_sq024_racetrack_'+size})
        groups[name] = []
        for i,audio in enumerate(world.get('race_audio',{}).get(name,defaults)):
            ref = f'#{ns}_{name}_{i}'
            world['entities'].append({'ref':ref,'position':dict(audio['position']),
                'yaw':audio.get('yaw',placement['yaw']),'ambient_event':audio['event'],
                'ambient_outline':{'type':'box','width':2,'depth':2,'height':2}})
            groups[name].append(ref)
    triggers = {trigger['ref']:trigger for trigger in world['triggers']}
    for role,area_ref in (('start',bindings['staging']),
                          ('courier',bindings['courier_trigger'])):
        footprint = triggers[area_ref]
        ref = f'#{ns}_vehicle_forbidden_{role}'
        exclusion = {'ref':ref,'position':dict(footprint['position']),
            'yaw':footprint.get('yaw',0),'vehicle_forbidden_outline':footprint['outline']}
        if role == 'start':
            # MQ056's wait-denied area is separate from the staging trigger
            # and does not cover the starting grid. Activating the staging
            # footprint here also encloses the freshly spawned player car.
            waiting = markers[bindings['activation']]
            vehicle_spots = [spot for spot in world.get('ai_spots',[])
                             if spot.get('vehicle_spawn')]
            vehicle_spots.extend(spot for community in world.get('communities',[])
                for entry in community['entries'] for spot in entry['spots']
                if spot.get('vehicle_spawn') and spot.get('phase') != 'finish')
            clearance = min(math.hypot(spot['position']['x']-waiting['position']['x'],
                                      spot['position']['y']-waiting['position']['y'])
                            for spot in vehicle_spots)
            half_width = min(1.5,(clearance-3.0)/math.sqrt(2))
            if half_width <= 0:
                raise ValueError('Race waiting point must clear vehicle spawn centres by more than 3 metres')
            exclusion.update(position=dict(waiting['position']),yaw=waiting['yaw'],
                vehicle_forbidden_outline={'type':'box','width':2*half_width,
                    'depth':2*half_width,'height':5.0},
                vehicle_forbidden_inner_outline={'type':'box','width':half_width,
                    'depth':half_width,'height':4.0},
                vehicle_forbidden_inner_bound=False,
                vehicle_forbidden_speed_limit=15.0,vehicle_forbidden_null_area=True)
        world['entities'].append(exclusion)
        bindings['forbidden_'+role] = ref
        groups['vehicle_forbidden_'+role] = [ref]
    stopping = world.get('finish_vehicle_forbidden_area')
    if stopping is not None:
        ref = f'#{ns}_vehicle_forbidden_finish'
        world['entities'].append({'ref':ref,'position':dict(stopping['position']),
            'yaw':stopping['yaw'],'vehicle_forbidden_outline':stopping['outline'],
            'vehicle_forbidden_inner_outline':stopping['inner_outline'],
            'vehicle_forbidden_inner_bound':False,
            'vehicle_forbidden_speed_limit':float(stopping.get('speed_limit',20.0)),
            'vehicle_forbidden_null_area':True})
        bindings['forbidden_finish'] = ref
        groups['vehicle_forbidden_finish'] = [ref]
    bindings['water_areas'] = []
    for i,volume in enumerate(world.get('water_areas', [])):
        ref = f'#{ns}_water_hazard_{i}'
        world['triggers'].append({**volume,'ref':ref})
        bindings['water_areas'].append(ref)


def variants(documents, world, bindings):
    sector = next(doc['Data']['RootChunk'] for depot,doc in documents.items()
                  if depot==world['quest_sector_path'])
    full_groups = {name:{ref.rsplit('/',1)[-1] for ref in refs}
                   for name,refs in bindings['variants'].items()}
    grouped = {name:[] for name in ('base',*full_groups)}
    placements = {item['NodeIndex']:item for item in sector['nodeData']['Data']}
    for index,(node,ref) in enumerate(zip(sector['nodes'],sector['nodeRefs'])):
        alias = ref['$value'].rsplit('/',1)[-1]
        group = next((name for name,refs in full_groups.items() if alias in refs),'base')
        grouped[group].append((node,ref,placements[index]))
    sector['nodes'],sector['nodeRefs'],data = [],[],[]
    sector['variantIndices'] = []
    descriptors = []
    for number,(name,items) in enumerate(grouped.items()):
        sector['variantIndices'].append(len(data))
        for node,ref,placement in items:
            placement['NodeIndex'] = len(sector['nodes'])
            node['Data']['sourcePrefabHash'] = str(node_ref_hash(bindings['prefab']))
            sector['nodes'].append(node)
            sector['nodeRefs'].append(ref)
            data.append(placement)
        if name!='base':
            descriptors.append({'$type':'worldStreamingSectorVariant',
                'nodeRef':node_ref(bindings['prefab']),
                'variantId':zlib.crc32((bindings['id']+':'+name).encode()),
                'parentVariantID':0,'name':cname(name),'rangeIndex':number,'enabledByDefault':0})
    sector['nodeData']['Data'] = data
    # VariantNodes is WolvenKit's derived view of nodeData ranges.
    sector['variantNodes'] = []
    block = documents[world['block_path']]['Data']['RootChunk']
    for descriptor in block['descriptors']:
        if descriptor['data']['DepotPath']['$value']==world['quest_sector_path']:
            descriptor['variants'] = descriptors
