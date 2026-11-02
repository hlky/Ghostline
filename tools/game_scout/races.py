"""Persistent race surveys and portable world-generator geometry exports."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

from .core import ScoutError, atomic_json, distance, identifier, now, number, point


ROLES = {
    'spline_point', 'checkpoint', 'start_grid', 'player_start', 'staging', 'activation', 'finish',
    'opponent_exit', 'recovery', 'reward', 'spectator', 'hazard', 'boundary', 'gps',
    'prop', 'speed_change', 'width_change',
}
AREAS = {'checkpoint', 'staging', 'finish', 'hazard', 'boundary'}


def mark_options(role, options):
    if not isinstance(options, dict):
        raise ScoutError('options must be an object')
    allowed = {'width_m', 'depth_m', 'height_m'} if role in AREAS else set()
    required = set()
    if role == 'speed_change':
        allowed = required = {'speed_mps'}
    elif role == 'width_change':
        allowed = required = {'left_m', 'right_m'}
    elif role == 'prop':
        allowed = {'entity_template'}
    if set(options) - allowed:
        raise ScoutError(f'Unsupported options for {role}: {sorted(set(options) - allowed)}')
    if required - set(options):
        raise ScoutError(f'{role} requires {sorted(required)}')
    result = {}
    for key, value in options.items():
        if key == 'entity_template':
            if not isinstance(value, str) or not value.strip() or '..' in value or ':' in value or value.startswith(('/', '\\')):
                raise ScoutError('entity_template must be a relative depot path')
            result[key] = value.replace('/', '\\')
        else:
            result[key] = number(value, 0.01 if key in {'width_m', 'depth_m', 'height_m'} else 0, 1000, key)
    return result


def station(position, points):
    """Nearest 3D station on the exported piecewise-straight centreline."""
    best = None
    travelled = 0.0
    for a, b in zip(points, points[1:]):
        length = distance(a, b)
        if length == 0:
            continue
        t = max(0, min(1, sum((position[k]-a[k])*(b[k]-a[k]) for k in 'xyz') / length**2))
        projected = {k: a[k] + t*(b[k]-a[k]) for k in 'xyz'}
        candidate = (distance(position, projected), travelled+t*length)
        if best is None or candidate < best:
            best = candidate
        travelled += length
    if best is None:
        raise ScoutError('Spline points must describe a non-zero route')
    return best[1], best[0]


class RacePlans:
    def __init__(self, library):
        self.library = library

    def get(self, race_id):
        record = self.library.get(race_id)
        if record['kind'] != 'race':
            raise ScoutError('race_id must identify a race plan')
        return record

    def create(self, name, prefix, description='', looped=False, width_default=5, speed_mps=10):
        if not isinstance(prefix, str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,63}', prefix):
            raise ScoutError('prefix must be 1–64 lowercase letters/digits/underscores, starting with a letter')
        if not isinstance(name, str) or not name.strip():
            raise ScoutError('Race name must not be empty')
        if not isinstance(looped, bool):
            raise ScoutError('looped must be a boolean')
        return self.library.put('race', name.strip(), {
            'schema_version': 1, 'prefix': prefix, 'description': description, 'looped': looped,
            'width_default': number(width_default, 0, 1000, 'width_default'),
            'speed_mps': number(speed_mps, 0, 1000, 'speed_mps'), 'marks': [],
        })

    def _mutate(self, race_id, change):
        # One row is one survey. Serialize read/modify/write across MCP processes.
        with self.library.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT kind,data FROM records WHERE id=?', (race_id,)).fetchone()
            if row is None or row[0] != 'race':
                raise ScoutError('race_id must identify a race plan')
            data = json.loads(row[1])
            change(data)
            db.execute('UPDATE records SET data=?,updated_at=? WHERE id=?',
                       (json.dumps(data, allow_nan=False), now(), race_id))
        return self.get(race_id)

    def mark(self, race_id, role, position, yaw, *, name='', notes='', options=None,
             order=None, mark_id=None, evidence=None):
        if role not in ROLES:
            raise ScoutError(f'Unknown race role; choose one of {sorted(ROLES)}')
        position = point(position)
        yaw = number(yaw, -36000, 36000, 'yaw') % 360
        options = mark_options(role, options if options is not None else {})
        if order is not None:
            if isinstance(order, bool) or not isinstance(order, int) or not 0 <= order <= 10000:
                raise ScoutError('order must be an integer between 0 and 10000')
        result_id = mark_id or identifier('race_mark')

        def change(data):
            marks = data['marks']
            existing = next((m for m in marks if m['id'] == result_id), None)
            if mark_id and existing is None:
                raise ScoutError('mark_id does not belong to this race')
            if existing is None and len(marks) >= 2000:
                raise ScoutError('A race survey is limited to 2000 marks')
            ordinal = order
            if ordinal is None:
                ordinal = existing['order'] if existing and existing['role'] == role else (
                    max((m['order'] for m in marks if m['role'] == role), default=-1) + 1)
            if ordinal > 10000:
                raise ScoutError('No automatic order remains; edit/reorder existing marks')
            if any(m['id'] != result_id and m['role'] == role and m['order'] == ordinal for m in marks):
                raise ScoutError('Another mark has this role/order; use an unused order')
            mark = {'id': result_id, 'role': role, 'order': ordinal, 'name': name,
                    'notes': notes, 'position': position, 'yaw': yaw,
                    'options': options, 'evidence': evidence or {'source': 'manual'}}
            if existing:
                marks[marks.index(existing)] = mark
            else:
                marks.append(mark)
        record = self._mutate(race_id, change)
        return {'race_id': race_id, 'mark': next(m for m in record['data']['marks'] if m['id'] == result_id)}

    def remove(self, race_id, mark_id):
        def change(data):
            mark = next((m for m in data['marks'] if m['id'] == mark_id), None)
            if mark is None:
                raise ScoutError('mark_id does not belong to this race')
            data['marks'].remove(mark)
        return self._mutate(race_id, change)

    def edit(self, race_id, mark_id, *, order=None, name=None, notes=None, options=None,
             position=None, yaw=None):
        def change(data):
            mark = next((m for m in data['marks'] if m['id'] == mark_id), None)
            if mark is None:
                raise ScoutError('mark_id does not belong to this race')
            if order is not None:
                if isinstance(order, bool) or not isinstance(order, int) or not 0 <= order <= 10000:
                    raise ScoutError('order must be an integer between 0 and 10000')
                if any(m['id'] != mark_id and m['role'] == mark['role'] and m['order'] == order for m in data['marks']):
                    raise ScoutError('Another mark has this role/order; use an unused order')
                mark['order'] = order
            for key, value in [('name',name), ('notes',notes)]:
                if value is not None:
                    mark[key] = value
            if options is not None:
                mark['options'] = mark_options(mark['role'], options)
            if position is not None or yaw is not None:
                mark['evidence'] = {'source':'manual_edit','captured_evidence':
                                    mark['evidence'].get('captured_evidence',mark['evidence'])}
                if position is not None:
                    mark['position'] = point(position)
                if yaw is not None:
                    mark['yaw'] = number(yaw,-36000,36000,'yaw') % 360
        return self._mutate(race_id, change)

    def configure(self, race_id, *, description=None, looped=None, width_default=None, speed_mps=None):
        def change(data):
            if description is not None:
                data['description'] = description
            if looped is not None:
                if not isinstance(looped,bool):
                    raise ScoutError('looped must be a boolean')
                data['looped'] = looped
            for key, value in [('width_default',width_default), ('speed_mps',speed_mps)]:
                if value is not None:
                    data[key] = number(value,0,1000,key)
        return self._mutate(race_id, change)

    def export(self, race_id, require_complete=True):
        record = self.get(race_id)
        data = record['data']
        groups = {role: sorted((m for m in data['marks'] if m['role'] == role), key=lambda m: m['order']) for role in ROLES}
        missing = []
        minimum = 3 if data['looped'] else 2
        if len(groups['spline_point']) < minimum:
            missing.append(f'at least {minimum} spline_point marks')
        for role in ('checkpoint', 'start_grid', 'player_start', 'staging', 'activation', 'finish'):
            if not groups[role]:
                missing.append(role)
        if len(groups['finish']) > 1 or len(groups['player_start']) > 1:
            raise ScoutError('A race must have exactly one finish and player_start; remove extra marks')
        if require_complete and missing:
            raise ScoutError('Incomplete race survey: ' + ', '.join(missing))
        points = [m['position'] for m in groups['spline_point']]
        origin = points[0] if points else {'x': 0, 'y': 0, 'z': 0}
        prefix = data['prefix']
        # Separate plans with the same human prefix must not share world identities.
        namespace = prefix + '_' + race_id.removeprefix('race_')
        depot_root = f'mod\\{prefix}\\races\\{race_id.removeprefix("race_")}'
        world = {'name': namespace, 'prefab_root': '$/' + depot_root.replace('\\','/') + f'/#{namespace}_course',
                 'block_path': depot_root + '\\world\\all.streamingblock',
                 'quest_sector_path': depot_root + '\\world\\course.streamingsector',
                 'origin': {**origin, 'yaw': 0}, 'streaming_box': {'padding': 100},
                 'race_splines': [], 'markers': [], 'triggers': [], 'entities': []}
        warnings = []
        bindings = []
        course_points = points + [points[0]] if data['looped'] and points else points
        length = sum(distance(a, b) for a, b in zip(course_points, course_points[1:]))
        if len(points) >= minimum:
            if any(distance(a, b) < 0.05 for a, b in zip(course_points, course_points[1:])):
                raise ScoutError('Adjacent spline points must be at least 0.05 m apart')
            speeds = [{'speed_mps': data['speed_mps']}]
            widths = []
            for role in ('speed_change', 'width_change'):
                stationed = []
                for mark in groups[role]:
                    s, deviation = station(mark['position'], course_points)
                    if deviation > 5:
                        warnings.append(f"{mark['id']} is {deviation:.1f} m from the centreline")
                    stationed.append((s, mark))
                stationed.sort(key=lambda pair: pair[0])
                if any(abs(a[0]-b[0]) < 0.01 for a, b in zip(stationed, stationed[1:])):
                    raise ScoutError(f'{role} marks project to the same route station')
                for i, (s, mark) in enumerate(stationed):
                    if role == 'speed_change':
                        if s < 0.01:
                            speeds[0]['speed_mps'] = mark['options']['speed_mps']
                        else:
                            speeds.append({'start': s, 'end': s, 'speed_mps': mark['options']['speed_mps']})
                    else:
                        end = stationed[i+1][0] if i+1 < len(stationed) else length
                        if end <= s:
                            raise ScoutError('A width_change must precede the course end')
                        widths.append({'from': s, 'to': end, 'left': mark['options']['left_m'], 'right': mark['options']['right_m']})
            world['race_splines'] = [{'ref': f'#{namespace}_route', 'position': origin, 'yaw': 0,
                'points': [[p[k]-origin[k] for k in 'xyz'] for p in points], 'looped': data['looped'],
                'width_default': data['width_default'], 'speed_sections': speeds, 'width_sections': widths}]
        for mark in sorted(data['marks'], key=lambda m: (m['role'], m['order'])):
            ref = f"#{namespace}_{mark['role']}_{mark['id'].removeprefix('race_mark_')}"
            # Native camera yaw is the same Z rotation as the node quaternion.
            # Use absolute positions; generator relative-offset bearings differ.
            yaw = mark['yaw']
            base = {'ref': ref, 'position': mark['position'], 'yaw': yaw}
            binding = {'mark_id': mark['id'], 'role': mark['role'], 'order': mark['order'], 'ref': ref}
            if mark['role'] in {'spline_point', 'speed_change', 'width_change'}:
                binding['ref'] = f'#{namespace}_route' if world['race_splines'] else None
                if world['race_splines']:
                    binding['station_m'] = station(mark['position'], course_points)[0]
            if mark['role'] not in {'spline_point', 'speed_change', 'width_change'}:
                marker = dict(base)
                if mark['role'] in {'start_grid', 'player_start', 'recovery'}:
                    marker['marker_type'] = 'spawn_point'
                world['markers'].append(marker)
                if mark['role'] in AREAS:
                    opts = mark['options']
                    trigger_ref = ref + '_trigger'
                    world['triggers'].append({**base, 'ref': trigger_ref, 'outline': {
                        'type': 'box', 'width': opts.get('width_m', 10),
                        'depth': opts.get('depth_m', 2), 'height': opts.get('height_m', 4)}})
                    binding['trigger_ref'] = trigger_ref
                if mark['role'] == 'prop' and mark['options'].get('entity_template'):
                    world['entities'].append({**base, 'ref': ref+'_entity', 'entity_template': mark['options']['entity_template']})
            bindings.append(binding)
            if mark.get('evidence', {}).get('source') == 'camera':
                warnings.append(f"{mark['id']} uses camera height; verify its ground placement")
        manifest = {'schema_version': 1, 'status': 'geometry_complete' if not missing else 'draft',
                    'race': copy.deepcopy(record), 'world_spec': world, 'bindings': bindings,
                    'missing': missing, 'warnings': warnings, 'centreline_length_m': length,
                    'distance_basis': 'piecewise-straight centreline; re-station tuning if tangents are smoothed',
                    'required_quest_work': ['spawn entrants and assign seats', 'stage and count down',
                        'activate ordered checkpoint gates and increment progress', 'connect checkpoint visuals and stock HUD facts',
                        'resolve player/opponent finish exactly once', 'bind recovery and opponent exit routes',
                        'deliver reward and retire owned race state']}
        destination = self.library.root / 'exports' / identifier('race_export')
        atomic_json(destination/'world.json', world)
        atomic_json(destination/'race-plan.json', manifest)
        return {'race_id': race_id, 'world_spec_path': str((destination/'world.json').resolve()),
                'manifest_path': str((destination/'race-plan.json').resolve()),
                'status': manifest['status'], 'missing': missing, 'warnings': warnings,
                'mark_count': len(data['marks']), 'centreline_length_m': length}

    def build(self, race_id, entrants, *, project=None, output_root=None, settings=None):
        """Compile a fresh survey snapshot into a project-owned preview, never install."""
        import race_builder
        record = self.get(race_id)
        settings = {} if settings is None else settings
        allowed = {'countdown_seconds','timeout_seconds','winning_places','reward','off_course','rubberband'}
        if not isinstance(settings,dict) or set(settings)-allowed:
            raise ScoutError('Unsupported race builder settings')
        spec = {'schema_version':1,'id':record['data']['prefix']+'_race_'+race_id[-8:],
                'title':record['name'],'description':record['data']['description'],
                'survey':'race-plan.json','entrants':entrants,**settings}
        race_builder.normalize(spec)  # Refuse invalid entrants/settings before exporting.
        export = self.export(race_id)
        path = Path(export['manifest_path']).with_name('builder.spec.json')
        atomic_json(path,spec)
        return race_builder.build(path,project=project,output_root=output_root)
