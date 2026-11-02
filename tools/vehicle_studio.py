"""Resolve exact vehicle appearance proxies, export textures and render game models."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import struct
import re

from artifact_io import atomic_write_json
from vehicle_catalog import VehicleError

ROOT = Path(__file__).resolve().parents[1]


def value(item):
    return item.get('$value', '') if isinstance(item, dict) else item


def resource(item):
    return value(item.get('DepotPath', {})) if isinstance(item, dict) else ''


def resolve_slot(component, name):
    matches = {json.dumps(s, sort_keys=True): s for s in component.get('slots', [])
               if value(s.get('slotName')) == name}
    if len(matches) != 1:
        raise VehicleError(f'No unique slot definition for {name!r}')
    return next(iter(matches.values()))


def selected_chunk_materials(sidecar, geometry, appearance=None, chunk_mask=2**64 - 1):
    """Bind the requested mesh appearance to actual visible chunks, without fallback paints."""
    keys = list(sidecar['Appearances'])
    matches = [(i, key) for i, key in enumerate(keys)
               if key == appearance or (appearance is not None and key == appearance + str(i))]
    if not matches and appearance in (None, 'default', 'Default') and keys:
        matches = [(0, keys[0])]
    if len(matches) != 1:
        raise VehicleError(f'No exact mesh material appearance: {appearance!r}')
    index, key = matches[0]
    names = []
    for mesh in geometry['meshes']:
        chunk = re.search(r'submesh_(\d+)', mesh.get('name', ''))
        if chunk and not (int(chunk_mask) & (1 << int(chunk.group(1)))):
            continue
        variants = mesh.get('extras', {}).get('materialNames', [])
        if len(variants) != len(keys):
            raise VehicleError(f'Ambiguous material choices on {mesh.get("name")}')
        names.append(variants[index])
    materials = {m['Name']: m for m in sidecar['Materials']}
    if any(name not in materials for name in names):
        raise VehicleError('Missing authored material for an appearance chunk')
    return [materials[name] for name in dict.fromkeys(names)], key


def glb_metadata(path):
    with path.open('rb') as stream:
        header = stream.read(12)
        if header[:4] != b'glTF':
            raise VehicleError('Invalid glTF asset')
        size, kind = struct.unpack('<II', stream.read(8))
        if kind != 0x4e4f534a:
            raise VehicleError('Missing glTF JSON chunk')
        return json.loads(stream.read(size))


def appearance_binding(entity, appearance):
    """Require an exact .ent appearance binding; never borrow another paint variant."""
    if not appearance or appearance == 'random':
        appearance = value(entity.get('defaultAppearance'))
    matches = [a for a in entity.get('appearances', []) if value(a.get('name')) == appearance]
    if len(matches) != 1:
        raise VehicleError(f'No unique entity appearance binding for {appearance!r}')
    return resource(matches[0].get('appearanceResource')), value(matches[0].get('appearanceName'))


def appearance_proxy(document, name):
    matches = [a.get('Data', a) for a in document.get('appearances', [])
               if value(a.get('Data', a).get('name')) == name]
    if len(matches) != 1:
        raise VehicleError(f'No unique appearance definition for {name!r}')
    proxy = resource(matches[0].get('proxyMesh'))
    if not proxy or not proxy.endswith('.mesh'):
        raise VehicleError(f'Appearance {name!r} has no assembled game proxy mesh')
    return proxy


def run_batch(red, schema, game, folder, stage, jobs, *, export=False):
    manifest, report = folder / f'{stage}-jobs.json', folder / f'{stage}-report.json'
    atomic_write_json(manifest, {'jobs': jobs})
    command = [str(red), 'mesh-export-batch' if export else 'cr2w-serialize-batch',
               str(manifest), '--schema', str(schema), '--archives-root', str(game / 'archive/pc'),
               '--report', str(report), '--threads', '4']
    if export:
        command += ['--material-repo', str(folder / 'materials')]
    if jobs:
        report.unlink(missing_ok=True)
        completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        (folder / f'{stage}.log').write_text(completed.stdout + completed.stderr, encoding='utf-8')
        if not report.exists():
            raise VehicleError(f'{stage} failed: {completed.stderr[-2000:]}')
    return json.loads(report.read_text(encoding='utf-8')) if jobs else []
