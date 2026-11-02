"""Calculate configured vehicle speeds using authored gears and the game's HUD curve."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import subprocess
import tempfile

from artifact_io import atomic_write_json

HUD_RESOURCE = r'base\gameplay\curves\vehicle\vehicle_ui.curveset'
MPH_PER_MPS = 3600 / 1609.344
HUD_KMH_PER_MPH = 1.60934  # Exact constant used by hudCarController.OnSpeedValueChanged.


def evaluate_curve(curve, x):
    """Evaluate RED legacy Bezier controls, not straight lines between handles."""
    points = [(float(p['Point']), float(p['Value'])) for p in curve['Elements']]
    if not points or not math.isfinite(x) or any(not math.isfinite(v) for p in points for v in p):
        raise ValueError('Curve requires finite points and input')
    if any(a[0] > b[0] for a, b in zip(points, points[1:])):
        raise ValueError('Curve control times must be monotonic')
    kind = curve['InterpolationType']
    degree = {'BezierCubic': 3, 'BezierQuadratic': 2, 'Linear': 1, 'Constant': 1}.get(kind)
    if degree is None or (len(points) - 1) % degree:
        raise ValueError(f'Unsupported or malformed {kind} curve')
    if x <= points[0][0]:
        return points[0][1]
    if x >= points[-1][0]:
        return points[-1][1]
    for i in range(0, len(points) - 1, degree):
        controls = points[i:i + degree + 1]
        if x > controls[-1][0]:
            continue
        if kind == 'Constant':
            return controls[-1][1] if x == controls[-1][0] else controls[0][1]

        def bezier(t, axis):
            values = [p[axis] for p in controls]
            while len(values) > 1:
                values = [(1 - t) * a + t * b for a, b in zip(values, values[1:])]
            return values[0]

        # The time axis is itself Bezier-shaped. Solve x(t), then evaluate y(t).
        low, high = 0.0, 1.0
        for _ in range(60):
            middle = (low + high) / 2
            if bezier(middle, 0) < x:
                low = middle
            else:
                high = middle
        return bezier((low + high) / 2, 1)
    raise ValueError('Curve does not cover its input')


def speed_values(mps, hud_curve=None):
    if not isinstance(mps, (int, float)) or isinstance(mps, bool) or not math.isfinite(mps) or mps < 0:
        return {'mps': None, 'mph': None, 'kmh': None, 'hud_mph': None, 'hud_kmh': None}
    hud_mph = mps * evaluate_curve(hud_curve, mps) if hud_curve else None
    return {'mps': mps, 'mph': mps * MPH_PER_MPS, 'kmh': mps * 3.6,
            'hud_mph': hud_mph, 'hud_kmh': hud_mph * HUD_KMH_PER_MPH if hud_mph is not None else None}


def performance_stats(engine, gears, curve_data=None):
    curve_data = curve_data or {}
    hud = curve_data.get('curves', {}).get(HUD_RESOURCE, {}).get('speed_to_multiplier')
    forward = [(i, g) for i, g in enumerate(gears) if i > 0 and
               isinstance(g.get('maxSpeed'), (int, float)) and not isinstance(g['maxSpeed'], bool) and
               math.isfinite(g['maxSpeed']) and g['maxSpeed'] > 0]
    gear_index, top = max(forward, key=lambda pair: pair[1]['maxSpeed']) if forward else (None, {})
    speed = speed_values(top.get('maxSpeed'), hud)
    torque_path = engine.get('gearCurvesPath')
    torque_curves = curve_data.get('curves', {}).get(torque_path, {})
    endpoint = {name: evaluate_curve(curve, 1.0) for name, curve in torque_curves.items()}
    return {
        'model': 'configured_forward_gear_limit', 'gear_index': gear_index,
        'top_speed_mps': speed['mps'], 'top_speed_mph': speed['mph'], 'top_speed_kmh': speed['kmh'],
        'hud_top_speed_mph': speed['hud_mph'], 'hud_top_speed_kmh': speed['hud_kmh'],
        'gears': [{'index': i, 'reverse': i == 0, **speed_values(g.get('maxSpeed'), hud)} for i, g in enumerate(gears)],
        'hud_curve_resource': HUD_RESOURCE if hud else None,
        'torque_curve_resource': torque_path, 'torque_curve_at_normalized_rpm_1': endpoint,
        'note': 'Calculated at the highest authored forward-gear maxSpeed. HUD values use the game speedometer curve; '
                'world-space values use m/s conversions. This is a configured gearing ceiling, not a drag/traction simulation '
                'or measured sustained speed. Race AI, slopes and runtime mods can change achieved speed.',
    }


def extract_curve_data(game, output, paths, red, schema):
    resources = sorted({HUD_RESOURCE, *[p for p in paths if p]})
    cache = output / 'cache/performance'
    cache.mkdir(parents=True, exist_ok=True)
    curves, sources = {}, []
    with tempfile.TemporaryDirectory(dir=cache, prefix='.extract-') as directory:
        staging = Path(directory)
        jobs = [{'resource': resource, 'output': str(staging / f'{i}.json')} for i, resource in enumerate(resources)]
        atomic_write_json(staging / 'jobs.json', {'jobs': jobs})
        completed = subprocess.run([str(red), 'cr2w-serialize-batch', str(staging / 'jobs.json'),
                                    '--schema', str(schema), '--archives-root', str(game / 'archive/pc'),
                                    '--report', str(staging / 'report.json')], capture_output=True, text=True)
        if completed.returncode:
            raise ValueError(f'Vehicle curve extraction failed: {completed.stderr.strip()}')
        reports = json.loads((staging / 'report.json').read_text(encoding='utf-8'))
        errors = [r for r in reports if r.get('error')]
        if errors:
            raise ValueError(f'Unable to decode vehicle speed/torque curves: {errors}')
        for job in jobs:
            document = json.loads(Path(job['output']).read_text(encoding='utf-8'))
            entries = document['Data']['RootChunk']['curves']
            parsed = {entry['name']['$value']: entry['curve'] for entry in entries}
            for curve in parsed.values():
                evaluate_curve(curve, 0.0)
            curves[job['resource']] = parsed
            payload = json.dumps(document['Data'], sort_keys=True).encode()
            sources.append({'resource': job['resource'], 'data_sha256': hashlib.sha256(payload).hexdigest()})
    archives = [{'path': str(p.resolve()), 'size': p.stat().st_size, 'mtime_ns': p.stat().st_mtime_ns}
                for p in sorted((game / 'archive/pc').rglob('*.archive'))]
    result = {'schema_version': 1, 'curves': curves, 'sources': sources, 'archives': archives,
              'exporter_sha256': hashlib.sha256(red.read_bytes()).hexdigest(),
              'schema_sha256': hashlib.sha256(schema.read_bytes()).hexdigest(),
              'hud_formula': 'speed_mps * Bezier(vehicle_ui.speed_to_multiplier, speed_mps); kmh = hud_mph * 1.60934'}
    bundle = game / 'r6/cache/final.redscripts'
    if bundle.is_file():
        result['hud_script_bundle_sha256'] = hashlib.sha256(bundle.read_bytes()).hexdigest()
    atomic_write_json(cache / 'curves.json', result)
    return result
