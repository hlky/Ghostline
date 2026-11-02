"""Run the existing full-detail renderer separately for each indexed appearance."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import nullcontext
import hashlib
import json
from pathlib import Path
import subprocess
import traceback
import threading

from PIL import Image

from artifact_io import atomic_write_json
from vehicle_catalog import VehicleError, connect
from vehicle_full_studio import ROOT, prepare_vehicle
from vehicle_previews import Resources, identity
from vehicle_variants import build_variants, create_tables
from vehicle_render_environment import blender_environment
from vehicle_tool_snapshot import snapshot_tools


def valid_images(metadata, variant, resolution, views):
    if metadata.get('template') != variant['template'] or metadata.get('appearance') != variant['appearance']:
        return False
    if metadata.get('geometry') != 'game_full_detail' or metadata.get('resolution') != resolution:
        return False
    return all(Path(metadata.get('images', {}).get(view, '')).is_file() for view in views)


def render_variant_batch(output, game, red, schema, blender, wolvenkit, *, records=(),
                         all_vehicles=False, resolution=1536, views='hero,front,back,left', workers=4, device='cpu'):
    view_names = views.split(',')
    if not 128 <= resolution <= 4096 or any(v not in ('hero', 'front', 'back', 'left', 'right') for v in view_names):
        raise VehicleError('Invalid resolution or views')
    database = output / 'vehicles.sqlite3'
    red, schema = snapshot_tools(output, red, schema)
    with connect(database) as db:
        create_tables(db)
        has_variants = db.execute('SELECT count(*) FROM vehicle_variants').fetchone()[0] > 0
    if not has_variants or all_vehicles:
        build_variants(output, game, red, schema)
    with connect(database) as db:
        source_rows = {r['record_id']: json.loads(r['data']) for r in db.execute('SELECT record_id,data FROM vehicles')}
        variants = [json.loads(r[0]) for r in db.execute('SELECT data FROM vehicle_variants ORDER BY appearance')]
        approved = {r['variant_id']: json.loads(r['metadata']) for r in db.execute('SELECT variant_id,metadata FROM variant_previews')}
    if records:
        unknown = set(records) - source_rows.keys()
        if unknown:
            raise VehicleError('Unknown records: ' + ', '.join(sorted(unknown)))
        variants = [v for v in variants if set(v['records']) & set(records)]
    elif not all_vehicles:
        variants = [v for v in variants if any(source_rows[r]['player_vehicle'] and source_rows[r]['appearance'] == v['appearance']
                                              for r in v['records'])]
    variants.sort(key=lambda v: (0 if 'aerondight' in v['template'] else
                                1 if any(source_rows[r]['player_vehicle'] and source_rows[r]['appearance'] == v['appearance']
                                         for r in v['records']) else 2, v['appearance']))
    archives = sorted((game / 'archive/pc').rglob('*.archive'))
    signature = hashlib.sha256(json.dumps([identity(p) for p in [*archives, red, schema, blender, wolvenkit,
        ROOT / 'tools/item_render_blender.py', ROOT / 'tools/vehicle_assembly.py']]).encode()).hexdigest()[:24]
    index_report = json.loads((output / 'variant-index-report.json').read_text(encoding='utf-8'))
    asset_signature = hashlib.sha256(json.dumps([[identity(p) for p in archives], identity(wolvenkit), 2]).encode()).hexdigest()[:24]
    ledger_path = output / 'cache/variant-asset-cache.json'
    ledger = json.loads(ledger_path.read_text(encoding='utf-8')) if ledger_path.exists() else {}
    base = Path(ledger.get('root', '')) if ledger.get('signature') == asset_signature else output / 'cache/variant-renders' / asset_signature
    if not base.resolve().is_relative_to((output / 'cache/variant-renders').resolve()):
        raise VehicleError('Invalid asset cache location')
    base.mkdir(parents=True, exist_ok=True)
    atomic_write_json(ledger_path, {'signature': asset_signature, 'root': str(base)})
    resources = Resources(game, output, red, schema, wolvenkit)
    resources.archives = list(reversed(archives))
    resources.cache = base / 'resources'
    resource_lock = threading.Lock()
    original_payload = resources.payload
    def locked_payload(depot):
        with resource_lock:
            return original_payload(depot)
    resources.payload = locked_payload
    gpu_slot = threading.Semaphore(1)
    render_env = blender_environment()
    progress_path = output / 'variant-render-progress.json'
    states = {v['variant_id']: 'rendered' if valid_images(approved.get(v['variant_id'], {}), v, resolution, view_names)
              else 'pending' for v in variants}
    failures = []

    def publish_progress():
        report = {'total_variants': len(variants), 'rendered_variants': sum(s == 'rendered' for s in states.values()),
                  'pending_variants': sum(s == 'pending' for s in states.values()),
                  'failed_variants': sum(s == 'failed' for s in states.values()), 'failures': failures,
                  'renderer': 'tools/item_render_blender.py', 'workers': workers, 'cache': str(base)}
        atomic_write_json(progress_path, report)
        return report

    def render(variant):
        key = variant['variant_id']
        row = dict(min((source_rows[r] for r in variant['records']),
                       key=lambda r: (r['appearance'] != variant['appearance'], len(r['record_id']))))
        row['appearance'] = variant['appearance']
        row['_decoded_root'] = variant['decoded_root']
        folder = base / key
        folder.mkdir(parents=True, exist_ok=True)
        destination = output / 'renders/variants' / signature / key
        receipt = destination / 'render-report.json'
        try:
            if not valid_images(approved.get(key, {}), variant, resolution, view_names):
                assembly_path = folder / 'assembly.json'
                if assembly_path.exists():
                    assembly = json.loads(assembly_path.read_text(encoding='utf-8'))
                else:
                    assembly = {}
                if assembly.get('asset_schema') != 2:
                    print(f'Preparing {variant["appearance"]}', flush=True)
                    assembly = prepare_vehicle(row, folder, resources, game, red, schema, wolvenkit)
                    atomic_write_json(assembly_path, assembly)
                with (gpu_slot if device == 'hip' else nullcontext()), (folder / 'blender.log').open('w', encoding='utf-8') as log:
                    primary = next(c['resolved_glb'] for c in assembly['components'] if c.get('resolved_glb'))
                    subprocess.run([str(blender), '-b', '-t', '8', '--python-exit-code', '1', '--python',
                        str(ROOT / 'tools/item_render_blender.py'), '--', '--glb', primary,
                        '--appearance', variant['appearance'], '--assembly', str(assembly_path),
                        '--output', str(destination), *(['--cpu'] if device == 'cpu' else []), '--resolution', str(resolution),
                        '--samples', '64', '--views', views], check=True, stdout=log, stderr=subprocess.STDOUT,
                        env=render_env)
                result = json.loads(receipt.read_text(encoding='utf-8'))
                images = {Path(p).stem: p for p in result['images']}
                if set(images) != set(view_names):
                    raise VehicleError('Missing requested variant views')
                for filename in images.values():
                    with Image.open(filename) as image:
                        image.load()
                        if image.size != (resolution, round(resolution / 1.6)) or not image.getbbox():
                            raise VehicleError('Invalid variant render dimensions or empty render')
                metadata = {k: result[k] for k in ('geometry', 'vertices', 'resolution', 'samples', 'engine')}
                metadata.update(images=images, template=variant['template'], appearance=variant['appearance'],
                    app_resource=variant['app_resource'], app_appearance=variant['app_appearance'],
                    renderer='tools/item_render_blender.py', receipt=str(receipt),
                    note='This exact authored appearance, with its own component meshes and materials. Offline studio lighting.')
                with connect(database) as db:
                    db.execute('PRAGMA busy_timeout=30000')
                    db.execute('INSERT OR REPLACE INTO variant_previews VALUES(?,?,?,?)',
                               (key, images['hero'] if 'hero' in images else next(iter(images.values())), 'studio', json.dumps(metadata)))
            with connect(database) as db:
                db.execute('PRAGMA busy_timeout=30000')
                db.execute("UPDATE vehicle_variants SET data=json_set(data,'$.status','rendered') WHERE variant_id=?", (key,))
            return key, None
        except Exception as exc:
            (folder / 'failure.log').write_text(traceback.format_exc(), encoding='utf-8')
            with connect(database) as db:
                db.execute('PRAGMA busy_timeout=30000')
                db.execute("UPDATE vehicle_variants SET data=json_set(data,'$.status','failed','$.render_error',?) WHERE variant_id=?",
                           (str(exc), key))
            return key, {'variant_id': key, 'appearance': variant['appearance'], 'template': variant['template'],
                         'error': str(exc), 'log': str(folder / 'failure.log')}

    publish_progress()
    print(f'Rendering {len(variants)} exact authored appearances with {workers} workers', flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        jobs = {pool.submit(render, variant): variant for variant in variants}
        for future in as_completed(jobs):
            key, failure = future.result()
            states[key] = 'failed' if failure else 'rendered'
            if failure:
                failures.append(failure)
                print(f'FAILED {failure["appearance"]}: {failure["error"]}', flush=True)
            report = publish_progress()
            print(f'{report["rendered_variants"]}/{len(variants)} rendered; {len(failures)} failed', flush=True)
    return {**publish_progress(), 'rendered_records': sum(s == 'rendered' for s in states.values())}
