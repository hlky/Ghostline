"""Open the measured AKPP shop recess without replacing its detailed facade."""
from __future__ import annotations

import base64
import copy
import struct
import hashlib

import numpy as np

from building_wall_uv import elements


def open_shop_panel(document, cut_x=-3.10):
    """Shrink the isolated back panel's left edge in every render LOD.

    This is a planar edit, not an arbitrary Boolean. Refuse shared vertices
    that would deform the surrounding facade. Preserve indices, normals,
    material assignments and untouched streams; translate both UV channels
    with the original face derivatives so the remaining panel keeps its finish.
    """
    result=copy.deepcopy(document)
    root=result['Data']['RootChunk']
    blob=root['renderResourceBlob']['Data']
    header=blob['header']
    original=base64.b64decode(blob['renderBuffer']['Bytes'])
    data=bytearray(original)
    scale=np.array([header['quantizationScale'][a] for a in 'XYZ'])
    offset=np.array([header['quantizationOffset'][a] for a in 'XYZ'])
    sizes={'PT_Short4N':8,'PT_Float16_2':4,'PT_Dec4':4,'PT_Color':4,
           'PT_Float4':16,'PT_UByte4':4,'PT_UByte4N':4,'PT_Invalid':0}
    report=[]
    changed_addresses=set()
    outside_addresses=set()
    for chunk in header['renderChunkInfos']:
        vertex=chunk['chunkVertices']; layout=vertex['vertexLayout']
        strides, offsets=elements(layout['slotStrides']),elements(vertex['byteOffsets'])
        points=np.array([struct.unpack_from('<3h',original,offsets[0]+i*strides[0])
                         for i in range(chunk['numVertices'])],dtype=float)/32767*scale+offset
        index_start=header['indexBufferOffset']+chunk['chunkIndices'].get('teOffset',0)
        indices=np.array(struct.unpack_from('<'+'H'*chunk['numIndices'],original,index_start)).reshape((-1,3))
        panel=np.array([all(abs(p[1]+1.654931545)<.002 and -4.62<p[0]<-1.38 and p[2]<2.52
                            for p in points[tri]) for tri in indices])
        outside_addresses.update(offsets[0]+int(i)*strides[0] for i in indices[~panel].flat)
        if not panel.any():
            continue
        selected=np.unique(indices[panel])
        moved=[int(i) for i in selected if points[i,0]<cut_x]
        streams,uv_offsets={},[]
        for item in elements(layout['elements']):
            stream=item.get('streamIndex',0); byte=streams.get(stream,0)
            if item['usage']=='PS_TexCoord':
                if item['type']!='PT_Float16_2':
                    raise ValueError('Panel edit requires half-float UV streams')
                uv_offsets.append((stream,byte))
            if item['type'] not in sizes:
                raise ValueError('Unsupported panel vertex element '+item['type'])
            streams[stream]=byte+sizes[item['type']]
        quantized=round((cut_x-offset[0])/scale[0]*32767)
        actual_x=quantized/32767*scale[0]+offset[0]
        for i in moved:
            address=offsets[0]+i*strides[0]
            changed_addresses.add(address)
            struct.pack_into('<h',data,address,quantized)
        for stream,byte in uv_offsets:
            uvs=np.array([struct.unpack_from('<ee',original,offsets[stream]+byte+i*strides[stream])
                          for i in range(chunk['numVertices'])])
            gradients=np.zeros_like(uvs);weights=np.zeros(len(points))
            for tri in indices[panel]:
                delta=points[tri[1:]]-points[tri[0]]
                area=np.linalg.norm(np.cross(*delta))
                if area<1e-10:
                    continue
                gradients[tri]+=(np.linalg.pinv(delta)@(uvs[tri[1:]]-uvs[tri[0]]))[0]*area
                weights[tri]+=area
            for i in moved:
                if weights[i]>0:
                    uv=uvs[i]+gradients[i]/weights[i]*(actual_x-points[i,0])
                    struct.pack_into('<ee',data,offsets[stream]+byte+i*strides[stream],*uv)
        report.append({'lod_mask':chunk.get('lodMask'),'panel_triangles':int(panel.sum()),
                       'moved_vertices':len(moved),'cut_x':actual_x})
    if changed_addresses&outside_addresses:
        raise ValueError('Panel vertices are shared with the surrounding facade')
    if {r['lod_mask'] for r in report}!={1,2,4} or not all(r['moved_vertices'] for r in report):
        raise ValueError('Expected isolated back panel in all three shop LODs')
    blob['renderBuffer']['Bytes']=base64.b64encode(data).decode()
    root['geometryHash']=str(int.from_bytes(hashlib.sha256(data).digest()[:8],'little'))
    # The original baked occluder still describes the sealed panel.
    root['parameters']=[p for p in root.get('parameters',[]) if p.get('Data',{}).get('$type')!='meshMeshParamOccluderData']
    return result,report
