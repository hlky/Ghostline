"""Prepare complete high-detail vehicle assemblies for the offline renderer."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import threading

_HASH_LOCK = threading.Lock()
_MESH_PATHS = {}
_EXPORT_LOCKS = {}
_DOCUMENTS = {}

from artifact_io import atomic_write_json
from vehicle_catalog import VehicleError, connect
from vehicle_previews import Resources, depot_hash, identity
from vehicle_studio import ROOT, appearance_binding, resource, run_batch, value


def chunks(root):
    result = root.get('compiledData', {}).get('Data', {}).get('Chunks')
    if not isinstance(result, list):
        raise VehicleError('Resource has no decoded component package')
    return result


def mesh_components(components):
    """Omit proxy/shadow/FX-only components from the close-up assembly."""
    return [dict(c) for c in components if c.get('mesh') and c.get('name')
            and c.get('isEnabled', 1) != 0
            and c.get('$type') != 'entAppearanceProxyMeshComponent'
            and not any(token in value(c['name']).lower() for token in
                        ('shadow', 'fx_cutout', 'engine_overheating'))]


def resolve_hashes(paths, folder, wolvenkit):
    needed = {str(p) for p in paths if str(p).isdigit()}
    if not needed:
        return {}
    source = ROOT / 'WolvenKit/WolvenKit.Common/Resources/usedhashes.kark'
    hashes = folder.parent / 'usedhashes.bin'
    with _HASH_LOCK:
        cache_key = str(hashes)
        if cache_key not in _MESH_PATHS:
            if not hashes.exists():
                completed = subprocess.run([str(wolvenkit), 'oodle', 'decompress', str(source),
                                            str(hashes.with_suffix('')), '-v', 'Minimal'], capture_output=True)
                if not hashes.is_file() or not hashes.stat().st_size:
                    raise VehicleError(f'Could not decode resource paths: {completed.stderr[-1000:]!r}')
            index = {}
            with hashes.open(encoding='utf-8') as stream:
                for line in stream:
                    path = line.strip()
                    if path.endswith('.mesh'):
                        index[str(depot_hash(path))] = path
            _MESH_PATHS[cache_key] = index
        index = _MESH_PATHS[cache_key]
    missing = needed - index.keys()
    if missing:
        raise VehicleError('Unresolved mesh resource hashes: ' + ', '.join(sorted(missing)))
    return {key: index[key] for key in needed}


def prepare_vehicle(row, folder, resources, game, red, schema, wolvenkit):
    def decoded(depot):
        filename = hashlib.sha256(depot.encode()).hexdigest()[:24] + '.json'
        shared = Path(row.get('_decoded_root', str(folder))) / filename
        path = shared if shared.is_file() else folder / filename
        if not path.exists():
            run_batch(red, schema, game, folder, 'decode', [{'resource': depot, 'output': str(path)}])
        with _HASH_LOCK:
            if str(path) not in _DOCUMENTS:
                _DOCUMENTS[str(path)] = json.loads(path.read_text(encoding='utf-8'))['Data']['RootChunk']
            return _DOCUMENTS[str(path)]

    entity = decoded(row['template'])
    app_path, name = appearance_binding(entity, row['appearance'])
    definitions = [a.get('Data', a) for a in decoded(app_path)['appearances']
                   if value(a.get('Data', a).get('name')) == name]
    if len(definitions) != 1:
        raise VehicleError(f'No exact appearance definition for {name}')
    entity_components = chunks(entity)
    appearance_components = chunks(definitions[0])
    components = mesh_components([*entity_components, *appearance_components])
    if not components:
        raise VehicleError('Appearance has no detailed mesh components')
    paths = [resource(c['mesh']) for c in components]
    resolved = resolve_hashes(paths, folder, wolvenkit)
    short_cache = ROOT / 'converted/vr' / folder.parent.name[:8]
    rigs = {}
    for c in [*entity_components, *appearance_components]:
        if c.get('rig'):
            depot = resource(c['rig'])
            rig_output = short_cache / 'rigs' / f'{depot_hash(depot):016x}'
            rig_output.mkdir(parents=True, exist_ok=True)
            binary, _ = resources.payload(depot)
            raw = rig_output / (binary.name + '.json')
            with _HASH_LOCK:
                rig_lock = _EXPORT_LOCKS.setdefault('rig:' + str(raw), threading.Lock())
            with rig_lock:
                try:
                    json.loads(raw.read_text(encoding='utf-8'))['Data']['RootChunk']['boneNames']
                except (OSError, ValueError, KeyError):
                    staging = rig_output / 'serialize'
                    staging.mkdir(exist_ok=True)
                    subprocess.run([str(wolvenkit), 'convert', 'serialize', str(binary), '-o', str(staging),
                                    '-v', 'Minimal'], check=True, capture_output=True)
                    result = json.loads((staging / raw.name).read_text(encoding='utf-8'))
                    if not result['Data']['RootChunk'].get('boneNames'):
                        raise VehicleError(f'Rig serialization is incomplete: {depot}')
                    atomic_write_json(raw, result)
            rigs[value(c['name'])] = str(raw)
    asset_folder = short_cache / hashlib.sha256(app_path.encode()).hexdigest()[:12]
    asset_folder.mkdir(parents=True, exist_ok=True)
    for c in components:
        depot = resource(c['mesh'])
        c['resolved_mesh'] = resolved.get(depot, depot)
        c['resolved_glb'] = str((asset_folder / 'raw').joinpath(*c['resolved_mesh'].split('\\')).with_suffix('.glb'))
        c['native_pbr'] = False
    export_paths = {c['resolved_mesh'] for c in components}
    # The exported GLBs retain their authored material sets. Include all app mesh
    # dependencies in the export, then select each variant's exact mesh appearance
    # in the unchanged Cyberpunk importer at render time.
    for definition in decoded(app_path)['appearances']:
        definition = definition.get('Data', definition)
        for component in mesh_components(definition.get('compiledData', {}).get('Data', {}).get('Chunks', [])):
            depot = resource(component['mesh'])
            if depot.isdigit():
                depot = _MESH_PATHS.get(str(folder.parent / 'usedhashes.bin'), {}).get(depot, '')
            if depot and depot.endswith('.mesh'):
                export_paths.add(depot)
    with _HASH_LOCK:
        export_lock = _EXPORT_LOCKS.setdefault(str(asset_folder), threading.Lock())
    archives = [game / 'archive/pc/content']
    if (game / 'archive/pc/ep1').is_dir():
        archives.append(game / 'archive/pc/ep1')
    if any((game / 'archive/pc/mod').glob('*.archive')):
        archives.append(game / 'archive/pc/mod')
    from character_full_preview import run_checked
    with export_lock:
        missing = [depot for depot in sorted(export_paths)
                   if not (asset_folder / 'raw').joinpath(*depot.split('\\')).with_suffix('.glb').is_file()
                   or not (asset_folder / 'raw').joinpath(*depot.split('\\')).with_suffix('.Material.json').is_file()]
        batches, current, length = [], [], 0
        for depot in missing:
            escaped = re.escape(depot)
            if length + len(escaped) > 12000 and current:
                batches.append(current); current, length = [], 0
            current.append(escaped); length += len(escaped) + 1
        if current:
            batches.append(current)
        for number, batch in enumerate(batches):
            pattern = '^(?:' + '|'.join(batch) + ')$'
            result = run_checked([str(wolvenkit), 'extract-and-export', *(str(p) for p in archives),
                '-o', str(asset_folder / 'cooked'), '-or', str(asset_folder / 'raw'), '--gamepath', str(game),
                '-r', pattern, '--mesh-export-material-repo', str(asset_folder / 'textures'),
                '--mesh-export-lod-filter', '--uext', 'png', '-v', 'Minimal'],
                'Vehicle material export', timeout=1200)
            (asset_folder / f'export-{number}.log').write_text(result.stdout + result.stderr, encoding='utf-8')
    for c in components:
        glb = Path(c['resolved_glb'])
        if not glb.is_file() or not glb.with_suffix('.Material.json').is_file():
            raise VehicleError(f'Incomplete vehicle material export: {glb}')
    # Preserve non-rendering parents/slots for transform resolution, without duplicating mesh entries.
    mesh_names = {value(c['name']) for c in components}
    parents = [c for c in [*entity_components, *appearance_components] if value(c.get('name')) not in mesh_names]
    return {'components': [*parents, *components], 'rigs': rigs, 'app': app_path, 'app_appearance': name,
            'asset_schema': 2}


def render_full_vehicles(output, game, red, schema, blender, wolvenkit, *, records=(),
                         all_vehicles=False, resolution=1536, views='hero,front,back,left'):
    if not 128 <= resolution <= 4096 or not views or any(v not in ('hero', 'front', 'back', 'left', 'right') for v in views.split(',')):
        raise VehicleError('Invalid render resolution or views')
    with connect(output / 'vehicles.sqlite3') as db:
        rows = [json.loads(r[0]) for r in db.execute('SELECT data FROM vehicles ORDER BY record_id')]
    if records:
        missing = set(records) - {r['record_id'] for r in rows}
        if missing:
            raise VehicleError('Unknown vehicle records: ' + ', '.join(sorted(missing)))
        rows = [r for r in rows if r['record_id'] in records]
    elif not all_vehicles:
        rows = [r for r in rows if r['player_vehicle']]
    archives = sorted((game / 'archive/pc').rglob('*.archive'))
    signature = hashlib.sha256(json.dumps([identity(p) for p in [*archives, red, schema, blender, wolvenkit,
        Path(__file__), ROOT / 'tools/item_render_blender.py', ROOT / 'tools/vehicle_assembly.py',
        ROOT / 'WolvenKit/WolvenKit.Common/Resources/usedhashes.kark']]).encode()).hexdigest()[:24]
    base = output / 'cache/full-studio' / signature
    base.mkdir(parents=True, exist_ok=True)
    resources = Resources(game, output, red, schema, wolvenkit)
    resources.archives = list(reversed(archives))
    resources.cache = base / 'resources'
    failures, count = [], 0
    for i, row in enumerate(rows):
        print(f'[{i+1}/{len(rows)}] Full-detail {row["record_id"]}', flush=True)
        key = hashlib.sha256((row['template'] + ':' + row['appearance']).encode()).hexdigest()[:24]
        folder = base / key
        folder.mkdir(exist_ok=True)
        destination = output / 'renders/full' / signature / key
        receipt = destination / 'render-report.json'
        try:
            cached = json.loads(receipt.read_text(encoding='utf-8')) if receipt.exists() else {}
            if cached.get('resolution') != resolution or any(not Path({Path(p).stem: p for p in cached.get('images', [])}.get(v, '')).is_file() for v in views.split(',')):
                job_path = folder / 'assembly.json'
                if job_path.exists():
                    assembly = json.loads(job_path.read_text(encoding='utf-8'))
                else:
                    assembly = prepare_vehicle(row, folder, resources, game, red, schema, wolvenkit)
                    atomic_write_json(job_path, assembly)
                with (folder / 'blender.log').open('w', encoding='utf-8') as log:
                    primary = next(c['resolved_glb'] for c in assembly['components'] if c.get('resolved_glb'))
                    subprocess.run([str(blender), '-b', '--python-exit-code', '1', '--python', str(ROOT / 'tools/item_render_blender.py'),
                        '--', '--glb', primary, '--appearance', row['appearance'], '--assembly', str(job_path),
                        '--output', str(destination), '--cpu', '--resolution', str(resolution),
                        '--samples', '64', '--views', views], check=True, stdout=log, stderr=subprocess.STDOUT)
            if not receipt.exists():
                raise VehicleError(f'No completed render; see {folder / "blender.log"}')
            result = json.loads(receipt.read_text(encoding='utf-8'))
            images = {Path(p).stem: p for p in result['images']}
            result['images'] = images
            if not images or not all(Path(p).is_file() for p in images.values()):
                raise VehicleError('Incomplete render images')
            render_summary = {key: result[key] for key in ('geometry', 'vertices', 'resolution', 'samples', 'engine', 'images')}
            metadata = {**render_summary, 'template': row['template'], 'appearance': row['appearance'],
                        'receipt': str(receipt), 'renderer': 'tools/item_render_blender.py',
                        'fingerprint': signature, 'source_archive_root': str(game / 'archive/pc'),
                        'note': 'Full-detail game component meshes, exact appearance materials, rig/slot assembly. '
                                'Offline studio lighting; engine-specific shaders may differ from the game.'}
            with connect(output / 'vehicles.sqlite3') as db:
                db.execute('INSERT OR REPLACE INTO previews VALUES(?,?,?,?)',
                    (row['record_id'], images.get('hero', next(iter(images.values()))), 'studio', json.dumps(metadata)))
            count += 1
        except (VehicleError, OSError, KeyError, ValueError, subprocess.CalledProcessError) as exc:
            failures.append({'record_id': row['record_id'], 'error': str(exc)})
            print(f'Failed: {exc}', flush=True)
        atomic_write_json(output / 'studio-report.json', {'requested': len(rows), 'rendered_records': count,
            'failures': failures, 'geometry': 'game_full_detail', 'cache': str(base)})
    return {'requested': len(rows), 'rendered_records': count, 'failures': failures, 'cache': str(base)}
