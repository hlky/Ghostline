"""Explicit interior ambience, based on reviewed vanilla residential corridors.

Donor: exterior_4_-29_-1_0.streamingsector, definitions 76 (upper) and
77 (ground). This supplies ambient mixing, not a rebuilt acoustic graph.
"""
from __future__ import annotations

PRESETS = {
    'residential-ground': (.9800000190734863, 'amb_int_roomtone_apartment_large_warm_airy_01'),
    'residential-upper': (.8999999761581421, 'amb_int_roomtone_appartment_med_warm_02'),
}


def compile_audio_areas(scene, world_point):
    from building_builder import ID, number
    areas = scene['layout'].get('audio_areas', [])
    if not isinstance(areas, list) or len(areas) > 32:
        raise ValueError('A building supports at most 32 audio areas')
    result, used = [], set()
    for area in areas:
        if not isinstance(area, dict) or not isinstance(area.get('id'), str) or not ID.fullmatch(area['id']) or area['id'] in used:
            raise ValueError('Audio area ids must be unique lowercase identifiers')
        used.add(area['id'])
        if area.get('preset') not in PRESETS:
            raise ValueError('Unknown residential audio preset')
        position, size = area.get('position'), area.get('size')
        if not isinstance(position, list) or len(position)!=3 or not isinstance(size,list) or len(size)!=3:
            raise ValueError('Audio area needs local XYZ position and three dimensions')
        position=[number(v,'Audio area position',-8000,8000) for v in position]
        size=[number(v,'Audio area size',.1,100) for v in size]
        result.append(dict(id=area['id'],preset=area['preset'],position=position,size=size,
                           world_position=world_point(position,scene['layout']['origin'])))
    scene['audio_areas']=result


def audio_area_node(area, handles):
    from generate_world import cname, area_outline
    value,event=PRESETS[area['preset']]
    width,depth,height=area['size']
    return {'HandleId':handles.take(),'Data':{
        '$type':'worldAmbientAreaNode','debugName':cname('interior_audio_'+area['id']),
        'outline':area_outline(dict(type='box',width=width,depth=depth,height=height),handles),
        'notifiers':[{'HandleId':handles.take(),'Data':{
            '$type':'audioAmbientAreaNotifier','includeChannels':'TC_SoundAmbientArea',
            'isEnabled':1,'occlusionEnabled':1,
            'Settings':{'HandleId':handles.take(),'Data':{
                '$type':'audioAmbientAreaSettings',
                'MetadataParent':cname('amb_area_int_default_corridors'),'Priority':10,
                'EventsOnActive':[{'$type':'audioAudEventStruct','event':cname(event)}],
                'Parameters':[{'$type':'audioAudParameter','name':cname('amb_interior'),'value':value}],
                'Reverb':cname('revb_interior_room_medium'),
            }},
        }}],
    }}


def verify_audio_area(wanted, restored):
    """Check audio routing and trigger shape after native serialization."""
    import math
    if wanted['outline']['Data']['buffer']!=restored['outline']['Data'].get('buffer'):
        raise ValueError('Readback changed interior audio outline')
    if len(restored.get('notifiers',[]))!=1:
        raise ValueError('Readback changed interior audio notifier count')
    a,b=wanted['notifiers'][0]['Data'],restored['notifiers'][0]['Data']
    if b['$type']!=a['$type'] or b.get('includeChannels')!=a['includeChannels'] or not b.get('isEnabled',True) or not b.get('occlusionEnabled',False):
        raise ValueError('Readback changed interior audio notifier')
    a,b=a['Settings']['Data'],b['Settings']['Data']
    for key in ('MetadataParent','Priority','Reverb','EventsOnActive'):
        if a[key]!=b.get(key): raise ValueError('Readback changed interior audio '+key)
    if len(b.get('Parameters',[]))!=1 or b['Parameters'][0]['name']!=a['Parameters'][0]['name'] or not math.isclose(b['Parameters'][0]['value'],a['Parameters'][0]['value'],abs_tol=1e-6):
        raise ValueError('Readback changed amb_interior parameter')
