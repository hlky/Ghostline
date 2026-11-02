"""Index actual entity/app appearances independently of repeated vehicle UI icons."""
from __future__ import annotations

import hashlib
import json
import subprocess

from artifact_io import atomic_write_json
from vehicle_catalog import VehicleError, connect
from vehicle_previews import identity
from vehicle_studio import resource, value


def variant_id(template, appearance):
    return hashlib.sha256((template + '\0' + appearance).encode()).hexdigest()[:32]


def bindings_for_record(row, entity):
    appearances = entity.get('appearances', [])
    requested = row['appearance']
    if requested and requested != 'random':
        appearances = [a for a in appearances if value(a.get('name')) == requested]
        if len(appearances) != 1:
            raise VehicleError(f'Exact appearance {requested!r} is not present in {row["template"]}')
    return appearances


def create_tables(db):
    db.execute('CREATE TABLE IF NOT EXISTS vehicle_variants(variant_id TEXT PRIMARY KEY,template TEXT,appearance TEXT,data TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS vehicle_variant_records(variant_id TEXT,record_id TEXT,explicit INTEGER,PRIMARY KEY(variant_id,record_id))')
    db.execute('CREATE TABLE IF NOT EXISTS variant_previews(variant_id TEXT PRIMARY KEY,path TEXT,kind TEXT,metadata TEXT)')
    db.execute('CREATE INDEX IF NOT EXISTS vehicle_variant_record_lookup ON vehicle_variant_records(record_id)')


def build_variants(output, game, red, schema):
    archives = sorted((game / 'archive/pc').rglob('*.archive'))
    fingerprint = hashlib.sha256(json.dumps([*[identity(p) for p in archives],
        hashlib.sha256(red.read_bytes()).hexdigest(), hashlib.sha256(schema.read_bytes()).hexdigest()]).encode()).hexdigest()[:24]
    folder = output / 'cache/variant-index' / fingerprint
    folder.mkdir(parents=True, exist_ok=True)
    database = output / 'vehicles.sqlite3'
    with connect(database) as db:
        rows = [json.loads(r[0]) for r in db.execute('SELECT data FROM vehicles ORDER BY record_id')]
    def decoded_path(depot):
        return folder / (hashlib.sha256(depot.encode()).hexdigest()[:24] + '.json')
    def decode(depots, stage):
        jobs = [{'resource': depot, 'output': str(decoded_path(depot))} for depot in sorted(set(depots))
                if depot and not decoded_path(depot).is_file()]
        if not jobs:
            return
        manifest, report = folder / (stage + '-jobs.json'), folder / (stage + '-report.json')
        atomic_write_json(manifest, {'jobs': jobs})
        print(f'Indexing {len(jobs)} {stage} resources', flush=True)
        with (folder / (stage + '.log')).open('w', encoding='utf-8') as log:
            subprocess.run([str(red), 'cr2w-serialize-batch', str(manifest), '--schema', str(schema),
                            '--archives-root', str(game / 'archive/pc'), '--report', str(report), '--threads', '4'],
                           stdout=log, stderr=subprocess.STDOUT)
        if not report.exists():
            raise VehicleError(f'Could not index {stage}; see {folder}')
    roots = {}
    def root(depot):
        if depot not in roots:
            roots[depot] = json.loads(decoded_path(depot).read_text(encoding='utf-8'))['Data']['RootChunk']
        return roots[depot]
    decode([row['template'] for row in rows], 'entities')
    variants, links, failures = {}, [], []
    for row in rows:
        try:
            entity = root(row['template'])
            bindings = bindings_for_record(row, entity)
            if not bindings:
                raise VehicleError('Entity has no authored appearance bindings')
            for binding in bindings:
                appearance = value(binding['name'])
                key = variant_id(row['template'], appearance)
                variants.setdefault(key, {'variant_id': key, 'template': row['template'], 'appearance': appearance,
                    'app_resource': resource(binding.get('appearanceResource')),
                    'app_appearance': value(binding.get('appearanceName')), 'records': [],
                    'decoded_root': str(folder), 'fingerprint': fingerprint})['records'].append(row['record_id'])
                links.append((key, row['record_id'], int(bool(row['appearance'] and row['appearance'] != 'random'))))
        except (OSError, ValueError, KeyError, VehicleError) as exc:
            failures.append({'record_id': row['record_id'], 'stage': 'entity', 'error': str(exc)})
    decode([v['app_resource'] for v in variants.values()], 'appearances')
    valid = {}
    for key, variant in variants.items():
        try:
            definitions = [a.get('Data', a) for a in root(variant['app_resource']).get('appearances', [])
                           if value(a.get('Data', a).get('name')) == variant['app_appearance']]
            if len(definitions) != 1:
                raise VehicleError(f'No exact app definition for {variant["app_appearance"]!r}')
            variant['visual_tags'] = [value(t) for t in definitions[0].get('visualTags', {}).get('tags', [])]
            variant['status'] = 'pending'
            valid[key] = variant
        except (OSError, ValueError, KeyError, VehicleError) as exc:
            failures.append({'variant_id': key, 'appearance': variant['appearance'], 'stage': 'appearance', 'error': str(exc)})
    with connect(database) as db:
        create_tables(db)
        db.execute('DELETE FROM vehicle_variants')
        db.execute('DELETE FROM vehicle_variant_records')
        db.executemany('INSERT INTO vehicle_variants VALUES(?,?,?,?)',
                       [(k, v['template'], v['appearance'], json.dumps(v)) for k, v in valid.items()])
        db.executemany('INSERT INTO vehicle_variant_records VALUES(?,?,?)', [r for r in links if r[0] in valid])
        # Existing exact-appearance renders remain that appearance's render only.
        for preview in db.execute('SELECT path,kind,metadata FROM previews WHERE kind="studio"').fetchall():
            metadata = json.loads(preview['metadata'])
            key = variant_id(metadata.get('template', ''), metadata.get('appearance', ''))
            if key in valid and metadata.get('geometry') == 'game_full_detail':
                db.execute('INSERT OR IGNORE INTO variant_previews VALUES(?,?,?,?)',
                           (key, preview['path'], preview['kind'], preview['metadata']))
    report = {'vehicle_records': len(rows), 'appearance_variants': len(valid), 'bindings': len(links),
              'failures': failures, 'fingerprint': fingerprint, 'decoded_root': str(folder)}
    atomic_write_json(output / 'variant-index-report.json', report)
    return report


def query_variants(db, q='', manufacturer='', vehicle_type='', player=False, rendered=False,
                   sort='name', limit=48, offset=0, preview_kind=''):
    create_tables(db)
    ordering = {'name': 'v.title COLLATE NOCASE,a.appearance', 'horsepower': 'v.horsepower DESC NULLS LAST',
                'mass': 'v.mass DESC NULLS LAST', 'speed': 'v.speed DESC NULLS LAST'}.get(sort)
    if ordering is None:
        raise VehicleError('Unknown sort order')
    # Prefer an explicitly bound spawn record for stats/ID, keeping all compatible IDs visible.
    join = '''FROM vehicle_variants a JOIN vehicle_variant_records r ON r.variant_id=a.variant_id
        AND r.record_id=(SELECT x.record_id FROM vehicle_variant_records x WHERE x.variant_id=a.variant_id
                        ORDER BY x.explicit DESC,length(x.record_id),x.record_id LIMIT 1)
        JOIN vehicles v ON v.record_id=r.record_id LEFT JOIN variant_previews p ON p.variant_id=a.variant_id '''
    where = '''WHERE (?='' OR instr(lower(v.title||' '||a.appearance||' '||v.record_id||' '||v.manufacturer),lower(?))>0)
        AND (?='' OR v.manufacturer=?) AND (?='' OR v.vehicle_type=?)
        AND (?=0 OR EXISTS(SELECT 1 FROM vehicle_variant_records x JOIN vehicles z ON z.record_id=x.record_id
                          WHERE x.variant_id=a.variant_id AND x.explicit=1 AND json_extract(z.data,'$.player_vehicle')=1))
        AND (?=0 OR p.path IS NOT NULL) AND (?='' OR p.kind=?)'''
    args = (q, q, manufacturer, manufacturer, vehicle_type, vehicle_type, int(player), int(rendered), preview_kind, preview_kind)
    total = db.execute('SELECT count(*) ' + join + where, args).fetchone()[0]
    result = db.execute('SELECT v.data,a.data AS variant,p.path,p.kind,p.metadata ' + join + where +
                        f' ORDER BY {ordering},a.variant_id LIMIT ? OFFSET ?', (*args, limit, offset))
    rows = []
    for record in result:
        row, variant = json.loads(record['data']), json.loads(record['variant'])
        row.pop('values', None); row.pop('drive_model', None)
        row['record_appearance'] = row['appearance']
        row['appearance'] = variant['appearance']
        row['variant_id'] = variant['variant_id']
        row['appearance_resource'] = variant['app_resource']
        row['appearance_definition'] = variant['app_appearance']
        row['compatible_records'] = variant['records']
        row['appearance_visual_tags'] = variant['visual_tags']
        row['preview_path'], row['preview_kind'] = record['path'], record['kind']
        row['preview_metadata'] = json.loads(record['metadata']) if record['metadata'] else None
        row['render_status'] = variant.get('status', 'pending')
        rows.append(row)
    return {'vehicles': rows, 'total': total, 'limit': limit, 'offset': offset, 'mode': 'appearances'}
