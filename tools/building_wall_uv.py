"""Keep wall finishes at floor-relative height when wall pieces are resized."""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import struct

import numpy as np


def elements(value):
    return value.get('Elements', []) if isinstance(value, dict) else value


def align_document(document, scale_z, offset_z):
    result = copy.deepcopy(document)
    blob = result['Data']['RootChunk']['renderResourceBlob']['Data']
    header = blob['header']
    data = bytearray(base64.b64decode(blob['renderBuffer']['Bytes']))
    original = bytes(data)
    sizes = {'PT_Short4N': 8, 'PT_Float16_2': 4, 'PT_Dec4': 4,
             'PT_Color': 4, 'PT_Float4': 16, 'PT_UByte4': 4, 'PT_UByte4N': 4}
    for chunk in header['renderChunkInfos']:
        vertex = chunk['chunkVertices']
        layout = vertex['vertexLayout']
        strides, offsets = elements(layout['slotStrides']), elements(vertex['byteOffsets'])
        streams, uv_offsets = {}, []
        for item in elements(layout['elements']):
            stream = item.get('streamIndex', 0)
            offset = streams.get(stream, 0)
            if item['usage'] == 'PS_TexCoord':
                if item['type'] != 'PT_Float16_2':
                    raise ValueError('Wall UV alignment requires half-float texture coordinates')
                uv_offsets.append((stream, offset))
            streams[stream] = offset + sizes.get(item['type'], 0)
        count = chunk['numVertices']
        points = np.array([struct.unpack_from('<3h', original, offsets[0]+i*strides[0]) for i in range(count)], dtype=float)
        points /= 32767
        points = points * [header['quantizationScale'][a] for a in 'XYZ'] + [header['quantizationOffset'][a] for a in 'XYZ']
        index_start = header['indexBufferOffset'] + chunk['chunkIndices'].get('teOffset', 0)
        indices = np.array(struct.unpack_from('<'+'H'*chunk['numIndices'], original, index_start)).reshape((-1, 3))
        for stream, offset in uv_offsets:
            addresses = [offsets[stream]+offset+i*strides[stream] for i in range(count)]
            uvs = np.array([struct.unpack_from('<ee', original, a) for a in addresses])
            gradients, weights = np.zeros_like(uvs), np.zeros(count)
            for tri in indices:
                delta = points[tri[1:]]-points[tri[0]]
                area = np.linalg.norm(np.cross(*delta))
                if area < 1e-10:
                    continue
                # Face-local UV derivatives preserve both channels, including
                # rotated UV islands and the multilayer paint mask.
                gradient_z = (np.linalg.pinv(delta) @ (uvs[tri[1:]]-uvs[tri[0]]))[2]
                gradients[tri] += gradient_z * area
                weights[tri] += area
            weights[weights == 0] = 1
            updated = uvs + gradients / weights[:, None] * ((scale_z-1)*points[:, 2]+offset_z)[:, None]
            for address, uv in zip(addresses, updated):
                struct.pack_into('<ee', data, address, *uv)
    blob['renderBuffer']['Bytes'] = base64.b64encode(data).decode()
    return result


def wkit_document(value):
    """Adapt the native reader's scalar/static arrays to WKit JSON syntax."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, list):
        return [wkit_document(v) for v in value]
    if isinstance(value, dict):
        result = {k: wkit_document(v) for k, v in value.items()}
        for field in ('elements', 'slotStrides', 'byteOffsets'):
            if value.get('$type') in ('GpuWrapApiVertexLayoutDesc', 'rendVertexBufferChunk') and isinstance(result.get(field), list):
                result[field] = {'Elements': result[field]}
        return result
    return value


def prepare_documents(scene, root):
    from building_library import CACHE, resource_id
    documents = {}
    for instance in scene['instances']:
        if instance['role'] != 'wall' and not instance.get('align_wall_uv'):
            continue
        sz = instance['scale'][2]
        tz = instance['position'][2]-instance['level']*scene['kit']['storey_height']
        if abs(sz-1) < 1e-8 and abs(tz) < 1e-8:
            continue
        source = instance['mesh']
        key = hashlib.sha256(json.dumps([source, round(sz, 9), round(tz, 9)]).encode()).hexdigest()[:16]
        name = f'wall-uv-{key}.mesh'
        if name not in documents:
            path = (root/'projects/experiments/building-lab/source/raw/mod/building_lab/rancho-window-clear.mesh.json'
                    if source.startswith('mod\\') else CACHE/'raw'/(resource_id(source)+'.mesh.json'))
            document = align_document(json.loads(path.read_bytes()), sz, tz)
            document['Header']['WolvenKitVersion'] = '8.17.4'
            documents[name] = wkit_document(document)
        instance['mesh'] = 'mod\\building_lab\\'+name
    return documents
