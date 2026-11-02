"""Vehicle records and performance metadata from the installed REDmod snapshot."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import re
import sqlite3

from artifact_io import atomic_write_json
from item_catalog import balanced_block, load_localizations, localized_value
from vehicle_performance import extract_curve_data, performance_stats


class VehicleError(RuntimeError):
    pass


HEADER = re.compile(r"(?m)^\s*([A-Za-z_]\w*)\s*(?::\s*([A-Za-z_][\w.]*))?\s*\{")
TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?f?|[A-Za-z_][\w.]*|\+=|[^\s]')


def scalar(token):
    if token.startswith('"'):
        return token[1:-1].replace('\\"', '"')  # Preserve depot-path backslashes.
    if token in ('true', 'false'):
        return token == 'true'
    try:
        value = float(token.rstrip('f'))
        if math.isfinite(value):
            return value
    except ValueError:
        pass
    return token


def parse_members(tokens, start=0, stop=None):
    result = {}
    i = start
    while i < len(tokens) and tokens[i] != stop:
        if tokens[i] in (';', ','):
            i += 1
            continue
        field = []
        while i < len(tokens) and tokens[i] not in ('=', '+=', ';', stop):
            field.append(tokens[i]); i += 1
        if i == len(tokens) or tokens[i] == stop:
            break
        if tokens[i] == ';':
            i += 1
            continue
        operation = tokens[i]
        key = field[-1]
        value, i = parse_value(tokens, i + 1)
        if operation == '+=' and isinstance(value, list):
            result.setdefault('$append', {}).setdefault(key, []).extend(value)
        else:
            result[key] = value
    return result, i + (stop is not None)


def parse_value(tokens, i):
    opening = tokens[i]
    if opening == '{':
        value, i = parse_members(tokens, i + 1, '}')
        if i < len(tokens) and tokens[i] == ':':
            value['$parent'] = tokens[i + 1]; i += 2
        return value, i
    if opening in ('[', '('):
        closing = ']' if opening == '[' else ')'
        values = []
        i += 1
        while i < len(tokens) and tokens[i] != closing:
            if tokens[i] == ',':
                i += 1
                continue
            value, i = parse_value(tokens, i)
            values.append(value)
        if i == len(tokens):
            raise VehicleError(f'Unclosed {opening} in tweak data')
        return values, i + 1
    return scalar(opening), i + 1


def parse_file(path):
    text = path.read_text(encoding='utf-8-sig')
    text = re.sub(r'"(?:\\.|[^"\\])*"|//[^\n]*|/\*.*?\*/',
                  lambda m: m[0] if m[0].startswith('"') else ' ', text, flags=re.S)
    package = re.search(r'(?m)^\s*package\s+([\w.]+)', text)
    package = package[1] if package else 'Vehicle'
    result = {}
    cursor = 0
    while match := HEADER.search(text, cursor):
        body, cursor = balanced_block(text, match.end() - 1)
        try:
            values, _ = parse_members(TOKEN.findall(body))
        except (IndexError, KeyError) as exc:
            raise VehicleError(f'Unable to parse {path}: {match[1]}') from exc
        result[f'{package}.{match[1]}'] = {
            'parent': match[2], 'package': package, 'values': values, 'source': str(path.resolve()),
        }
    return result


def merge(base, child):
    result = copy.deepcopy(base)
    for key, value in child.items():
        if not key.startswith('$'):
            result[key] = copy.deepcopy(value)
    for key, values in child.get('$append', {}).items():
        result[key] = list(result.get(key, [])) + copy.deepcopy(values)
    return result


class Records:
    def __init__(self, records):
        self.records, self.cache = records, {}

    def resolve(self, record_id, active=()):
        if record_id in self.cache:
            return copy.deepcopy(self.cache[record_id])
        if record_id in active:
            raise VehicleError(f'Inheritance cycle: {" -> ".join((*active, record_id))}')
        record = self.records.get(record_id)
        if not record:
            return {}
        parent = record['parent']
        if parent and '.' not in parent:
            parent = record['package'] + '.' + parent
        result = merge(self.resolve(parent, (*active, record_id)), record['values'])
        self.cache[record_id] = result
        return copy.deepcopy(result)

    def expand(self, value, package='Vehicle'):
        if isinstance(value, str):
            return self.resolve(value if '.' in value else package + '.' + value)
        if isinstance(value, dict):
            parent = value.get('$parent')
            return merge(self.expand(parent, package) if parent else {}, value)
        return {}


def load_records(game):
    records, sources = {}, []
    for content in ('base', 'ep1'):
        root = game / f'tools/redmod/tweaks/{content}/gameplay/static_data/database'
        for folder in ('vehicles', 'ui/icons'):
            for path in sorted((root / folder).rglob('*.tweak')):
                records.update(parse_file(path))
                sources.append({'path': str(path.resolve()), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    if not records:
        raise VehicleError('No REDmod vehicle tweak sources found in the selected game')
    return Records(records), sources


def vehicle_rows(records, localizations):
    rows = []
    for record_id, source in sorted(records.records.items()):
        if not record_id.startswith('Vehicle.'):
            continue
        values = records.resolve(record_id)
        template = values.get('entityTemplatePath')
        if not isinstance(template, str) or not template.endswith('.ent'):
            continue
        ui = records.expand(values.get('vehicleUIData'))
        engine = records.expand(values.get('vehEngineData'))
        drive = records.expand(values.get('vehDriveModelData'))
        gears = [records.expand(g) for g in engine.get('gears', [])]
        speeds = [g['maxSpeed'] for g in gears if isinstance(g.get('maxSpeed'), (int, float))]
        icon_id = values.get('icon', '')
        icon = records.expand(icon_id, 'UIIcon')
        manufacturer = records.expand(values.get('manufacturer')).get('enumName', '')
        title = localized_value(values.get('displayName'), localizations)
        year_raw = str(ui.get('productionYear', ''))
        year = localized_value(year_raw, localizations) if year_raw.startswith('LocKey#') else year_raw
        fallback = record_id.split('.')[-1].replace('_', ' ')
        stats = {
            'horsepower': ui.get('horsepower'), 'mass_kg': ui.get('mass'),
            'physics_mass_kg': drive.get('total_mass'), 'engine_torque': engine.get('engineMaxTorque'),
            'max_rpm': engine.get('maxRPM'), 'gear_speed_limit_raw': max(speeds) if speeds else None,
            'gear_count_including_reverse': len(gears) or None,
        }
        rows.append({
            'record_id': record_id, 'title': title or fallback, 'localized_title': bool(title),
            'description': localized_value(ui.get('info'), localizations),
            'manufacturer': manufacturer, 'vehicle_type': str(values.get('type', '')).split('.')[-1],
            'year': year, 'year_raw': year_raw,
            'drivetrain': localized_value(ui.get('driveLayout'), localizations),
            'appearance': values.get('appearanceName', ''), 'template': template,
            'tags': values.get('tags', []), 'armored': bool(values.get('isArmoredVehicle', False)),
            'weapons': values.get('weapons', []), 'player_vehicle': '_player' in record_id,
            'expansion': 'ep1' if '/ep1/' in source['source'].replace('\\', '/') else 'base',
            'source': source['source'], 'parent': source['parent'], 'icon_id': icon_id,
            'atlas': icon.get('atlasResourcePath', ''), 'atlas_part': icon.get('atlasPartName', ''),
            'stats': stats, 'engine': engine, 'gears': gears, 'drive_model': drive,
            'ui_data': ui, 'values': values,
            'stats_note': 'REDmod authored snapshot; UI specs and raw physics parameters, not measured performance or live mod overrides.',
        })
    return rows


class Connection(sqlite3.Connection):
    def __exit__(self, *args):
        try:
            return super().__exit__(*args)
        finally:
            self.close()


def connect(path):
    db = sqlite3.connect(path, factory=Connection)
    db.row_factory = sqlite3.Row
    return db


def build(game, output, localization_paths, *, speed_tools=None):
    output.mkdir(parents=True, exist_ok=True)
    records, sources = load_records(game)
    rows = vehicle_rows(records, load_localizations(localization_paths))
    curve_data = None
    if speed_tools:
        curve_data = extract_curve_data(game, output, [r['engine'].get('gearCurvesPath') for r in rows], **speed_tools)
    for row in rows:
        row['performance'] = performance_stats(row['engine'], row['gears'], curve_data)
        for key in ('top_speed_mph', 'top_speed_kmh', 'hud_top_speed_mph', 'hud_top_speed_kmh'):
            row['stats'][key] = row['performance'][key]
    database = output / 'vehicles.sqlite3'
    with connect(database) as db:
        db.execute('CREATE TABLE IF NOT EXISTS vehicles(record_id TEXT PRIMARY KEY, title TEXT, manufacturer TEXT, vehicle_type TEXT, horsepower REAL, mass REAL, speed REAL, data TEXT)')
        db.execute('CREATE TABLE IF NOT EXISTS previews(record_id TEXT PRIMARY KEY, path TEXT, kind TEXT, metadata TEXT)')
        db.execute('CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY, data TEXT)')
        db.execute('DELETE FROM vehicles')
        db.executemany('INSERT INTO vehicles VALUES(?,?,?,?,?,?,?,?)', [
            (r['record_id'], r['title'], r['manufacturer'], r['vehicle_type'], r['stats']['horsepower'],
             r['stats']['mass_kg'], r['stats']['hud_top_speed_mph'], json.dumps(r, allow_nan=False)) for r in rows])
        provenance = {'game': str(game.resolve()), 'sources': sources, 'localization': [
            {'path': str(p.resolve()), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in localization_paths]}
        if curve_data:
            provenance['performance'] = {key: value for key, value in curve_data.items() if key != 'curves'}
        db.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('source', json.dumps(provenance)))
    atomic_write_json(output / 'catalog.json', {'schema_version': 1, 'provenance': provenance, 'vehicles': rows})
    return {'vehicles': len(rows), 'sources': len(sources), 'database': str(database.resolve())}


def query(db, q='', manufacturer='', vehicle_type='', player=False, rendered=False, sort='name', limit=48, offset=0,
          preview_kind=''):
    order = {'name': 'v.title COLLATE NOCASE', 'horsepower': 'v.horsepower DESC NULLS LAST',
             'mass': 'v.mass DESC NULLS LAST', 'speed': 'v.speed DESC NULLS LAST'}.get(sort)
    if order is None:
        raise VehicleError('Unknown sort order')
    searchable = ('v.record_id || " " || v.title || " " || v.manufacturer || " " || '
                  'coalesce(json_extract(v.data,"$.description"),"") || " " || '
                  'coalesce(json_extract(v.data,"$.appearance"),"") || " " || '
                  'coalesce(json_extract(v.data,"$.template"),"") || " " || '
                  'coalesce(json_extract(v.data,"$.tags"),"")')
    where = (f'WHERE (?="" OR instr(lower({searchable}),lower(?))>0) AND (?="" OR v.manufacturer=?) '
             'AND (?="" OR v.vehicle_type=?) AND (?=0 OR json_extract(v.data,"$.player_vehicle")=1) '
             'AND (?=0 OR p.path IS NOT NULL) AND (?="" OR p.kind=?)')
    args = (q, q, manufacturer, manufacturer, vehicle_type, vehicle_type, int(player), int(rendered),
            preview_kind, preview_kind)
    join = 'FROM vehicles v LEFT JOIN previews p USING(record_id) '
    total = db.execute('SELECT count(*) ' + join + where, args).fetchone()[0]
    results = db.execute('SELECT v.data,p.path,p.kind,p.metadata ' + join + where + f' ORDER BY {order},v.record_id LIMIT ? OFFSET ?',
                         (*args, limit, offset)).fetchall()
    rows = []
    for row in results:
        data = json.loads(row['data'])
        data.pop('values', None); data.pop('drive_model', None)
        data['preview_path'], data['preview_kind'] = row['path'], row['kind']
        data['preview_metadata'] = json.loads(row['metadata']) if row['metadata'] else None
        rows.append(data)
    return {'vehicles': rows, 'total': total, 'limit': limit, 'offset': offset}


def summary(db):
    return {'vehicles': db.execute('SELECT count(*) FROM vehicles').fetchone()[0],
            'previews': db.execute('SELECT count(*) FROM previews JOIN vehicles USING(record_id)').fetchone()[0],
            'studio_renders': db.execute('SELECT count(*) FROM previews JOIN vehicles USING(record_id) WHERE kind="studio"').fetchone()[0],
            'manufacturers': [r[0] for r in db.execute('SELECT DISTINCT manufacturer FROM vehicles WHERE manufacturer!="" ORDER BY manufacturer')],
            'types': [r[0] for r in db.execute('SELECT DISTINCT vehicle_type FROM vehicles WHERE vehicle_type!="" ORDER BY vehicle_type')],
            'source': json.loads(db.execute('SELECT data FROM metadata WHERE key="source"').fetchone()[0])}
