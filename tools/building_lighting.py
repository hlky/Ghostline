"""Explicit practical light positions for authored building fixtures."""
from __future__ import annotations


def compile_lights(scene, world_point):
    from building_builder import ID, number

    lights = scene['layout'].get('lights', [])
    if not isinstance(lights, list) or len(lights) > 64:
        raise ValueError('A building supports at most 64 practical lights')
    result, used = [], set()
    for item in lights:
        if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not ID.fullmatch(item['id']) or item['id'] in used:
            raise ValueError('Practical light ids must be unique lowercase identifiers')
        used.add(item['id'])
        point, color = item.get('position'), item.get('color', [255, 224, 190])
        if not isinstance(point, list) or len(point) != 3:
            raise ValueError('Practical light position needs local XYZ')
        point = [number(v, 'Practical light position', -8000, 8000) for v in point]
        if not isinstance(color, list) or len(color) != 3 or any(isinstance(v, bool) or not isinstance(v, int) or not 0 <= v <= 255 for v in color):
            raise ValueError('Practical light color needs three integer RGB channels')
        result.append(dict(id=item['id'], position=point, world_position=world_point(point, scene['layout']['origin']),
                           color=color, radius=number(item.get('radius', 4), 'Practical light radius', .1, 20),
                           intensity=number(item.get('intensity', 45), 'Practical light intensity', .1, 1000)))
    scene['lights'] = result


def light_node(light, handles, cname):
    return {'HandleId': handles.take(), 'Data': {'$type': 'worldStaticLightNode',
            'debugName': cname('practical_light_' + light['id']),
            'color': {'$type': 'Color', **dict(zip(('Red', 'Green', 'Blue'), light['color'])), 'Alpha': 255},
            'radius': light['radius'], 'intensity': light['intensity'], 'autoHideDistance': 100.0}}
