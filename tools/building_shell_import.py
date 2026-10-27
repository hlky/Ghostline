"""Import reviewed, source-pinned vanilla shell placements as editor references.

The specification supplies one measured room and explicit placement/instance
selections. This does not infer a footprint, remove collision or install a mod.
"""
from __future__ import annotations

import argparse
import base64
import copy
import json
import math
from pathlib import Path

from artifact_io import atomic_write_json
from building_builder import compile_layout
from building_library import catalog, asset
from building_retrofit import _integer, _source
from world_location_world import _decode_world_transforms


def import_shell(spec):
    layout = copy.deepcopy(spec['layout'])
    origin = layout['origin']
    angle = math.radians(origin['yaw'])
    cosine, sine = math.cos(angle), math.sin(angle)
    half_c, half_s = math.cos(angle/2), math.sin(angle/2)
    assets = {v['path']: v for v in catalog()['assets']}
    modules = []
    for source in spec['sources']:
        root = _source(source)
        placements = root['nodeData']['Data']
        if source['expectedNodes'] != len(placements):
            raise ValueError('Shell source placement count changed')
        handles = {}

        def collect(value):
            if isinstance(value, dict):
                if 'HandleId' in value and 'Data' in value:
                    handles[value['HandleId']] = value['Data']
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(root)
        for selection in source['placements']:
            index = _integer(selection['index'], 'Shell placement', 0, len(placements)-1)
            placement = placements[index]
            node = root['nodes'][placement['NodeIndex']]['Data']
            path = node.get('mesh', {}).get('DepotPath', {}).get('$value')
            if path != selection['mesh']:
                raise ValueError('Selected shell mesh changed')
            if node['$type'] == 'worldInstancedMeshNode':
                transforms = node['worldTransformsBuffer']
                shared = transforms['sharedDataBuffer']
                buffer = shared.get('Data', handles.get(shared.get('HandleRefId'), {}))['buffer']
                decoded = _decode_world_transforms(base64.b64decode(buffer['Bytes']), 'shell')
                index = _integer(selection['instance'], 'Shell render instance', 0, transforms['numElements']-1)
                transform = decoded[transforms.get('startIndex', 0)+index]
                position, rotation, scale = (transform[k] for k in ('translation', 'rotation', 'scale'))
            elif node['$type'] in ('worldMeshNode', 'worldStaticMeshNode') and 'instance' not in selection:
                position, rotation, scale = (placement[k] for k in ('Position', 'Orientation', 'Scale'))
            else:
                raise ValueError('Select an explicit static mesh or render instance')
            point = [position[k] for k in 'XYZ']
            dx, dy = point[0]-origin['x'], point[1]-origin['y']
            local = [dx*cosine+dy*sine, -dx*sine+dy*cosine, point[2]-origin['z']]
            i, j, k, r = [rotation[k] for k in ('i', 'j', 'k', 'r')]
            quaternion = [half_c*i+half_s*j, half_c*j-half_s*i,
                          half_c*k-half_s*r, half_c*r+half_s*k]
            norm = math.sqrt(sum(v*v for v in quaternion))
            quaternion = [v/norm for v in quaternion]
            record = assets[path]
            if selection.get('replacement_asset'):
                record = asset(selection['replacement_asset'])
            appearance = node.get('meshAppearance', {}).get('$value', 'default')
            # Some vanilla placements name an appearance absent from their
            # mesh. Keep that source fact; preview with a measured appearance.
            preview_appearance = appearance if appearance in record['appearances'] else record['appearances'][0]
            modules.append(dict(id=selection['id'], asset=record['id'], appearance=preview_appearance,
                position=local, rotation=quaternion, scale=[scale[k] for k in 'XYZ'],
                yaw=((math.degrees(2*math.atan2(quaternion[2],quaternion[3]))+180)%360)-180,
                level=selection.get('level', 0), anchor='pivot', collision='none',
                reference_only=not bool(selection.get('replacement_asset')), reference_side=selection.get('side'),
                source_appearance=appearance,
                source_placement={'sector':source['path'], 'index':selection['index'],
                                  'instance':selection.get('instance'), 'world_position':point}))
    layout['modules'] = modules + layout.get('modules', [])
    layout['shell_import'] = {'name':spec['name'], 'status':'authoring-reference-only',
                             'notes':spec.get('notes', [])}
    scene = compile_layout(layout)
    return scene['layout']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    layout = import_shell(json.loads(args.spec.read_bytes()))
    atomic_write_json(args.out, layout)
    print(json.dumps({'layout':str(args.out), 'rooms':len(layout['rooms']),
                      'reference_modules':len(layout['modules']), 'installed':False}))


if __name__ == '__main__':
    main()
