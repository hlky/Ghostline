"""Extract game-rendered vehicle previews using their exact UIIcon atlas bindings."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

from PIL import Image

from artifact_io import atomic_write_json
from vehicle_catalog import VehicleError, connect


def depot_hash(depot):
    value = 0xcbf29ce484222325
    for byte in depot.lower().replace('/', '\\').encode('utf-8'):
        value = ((value ^ byte) * 0x100000001b3) & 0xffffffffffffffff
    return value


def identity(path):
    stat = path.stat()
    return [str(path.resolve()), stat.st_size, stat.st_mtime_ns]


class Resources:
    def __init__(self, game, output, red, schema, wolvenkit):
        self.game, self.output = game, output
        self.red, self.schema, self.wolvenkit = red, schema, wolvenkit
        # Explicit vanilla providers; do not accidentally mix in installed mods.
        self.archives = sorted((game / 'archive/pc/ep1').glob('*gamedata.archive'))
        self.archives += sorted((game / 'archive/pc/content').glob('*gamedata.archive'))
        self.archives += sorted((game / 'archive/pc/ep1').glob('*nightcity.archive'))
        self.archives += sorted((game / 'archive/pc/content').glob('*nightcity.archive'))
        self.archives += sorted((game / 'archive/pc/content').glob('*engine.archive'))
        self.archives += sorted((game / 'archive/pc/content').glob('*mainmenu.archive'))
        self.fingerprint = hashlib.sha256(json.dumps(
            [identity(p) for p in [*self.archives, red, schema, wolvenkit]]).encode()).hexdigest()[:24]
        self.cache = output / 'cache/previews' / self.fingerprint
        self.cache.mkdir(parents=True, exist_ok=True)

    def payload(self, depot):
        key = f'{depot_hash(depot):016x}'
        folder = self.cache / key
        binary = folder / 'cooked' / Path(depot.replace('\\', '/'))
        receipt = folder / 'source.json'
        if binary.exists() and receipt.exists():
            source = json.loads(receipt.read_text())
            if hashlib.sha256(binary.read_bytes()).hexdigest() == source['sha256']:
                return binary, Path(source['archive'])
        for archive in self.archives:
            completed = subprocess.run([str(self.red), 'extract', str(archive), '--output',
                                        str(folder / 'cooked'), '--path', depot], capture_output=True, text=True)
            if completed.returncode == 0 and binary.is_file():
                atomic_write_json(receipt, {'archive': str(archive.resolve()), 'depot': depot,
                                           'sha256': hashlib.sha256(binary.read_bytes()).hexdigest()})
                return binary, archive
        raise VehicleError(f'No selected vanilla archive contains {depot}')

    def atlas(self, depot):
        binary, _ = self.payload(depot)
        raw = binary.parent / (binary.name + '.json')
        if not raw.exists():
            subprocess.run([str(self.red), 'cr2w-serialize', str(binary), str(raw), '--schema', str(self.schema)], check=True, capture_output=True)
        return json.loads(raw.read_text(encoding='utf-8'))['Data']['RootChunk']

    def texture(self, depot):
        binary, archive = self.payload(depot)
        destination = self.cache / f'{depot_hash(depot):016x}' / 'png'
        png = destination / Path(depot.replace('\\', '/')).with_suffix('.png')
        if not png.exists():
            destination.mkdir(parents=True, exist_ok=True)
            subprocess.run([str(self.wolvenkit), 'uncook', str(archive), '--hash', str(depot_hash(depot)),
                            '-o', str(destination), '--uext', 'png', '-v', 'Minimal'], check=True, capture_output=True)
        if not png.exists():
            raise VehicleError(f'Texture export did not produce {png}')
        return png


def crop_part(image, part):
    uv = part.get('clippingRectInUVCoords')
    if uv:
        coordinates = [uv[key] for key in ('Left', 'Top', 'Right', 'Bottom')]
        if not all(isinstance(v, (int, float)) and 0 <= v <= 1 for v in coordinates):
            raise VehicleError('Invalid atlas UV rectangle')
        box = tuple(round(v * size) for v, size in zip(coordinates, (image.width, image.height, image.width, image.height)))
    else:
        rect = part.get('clippingRectInPixels', {})
        box = tuple(int(rect.get(key, 0)) for key in ('Left', 'Top', 'Right', 'Bottom'))
    if not (0 <= box[0] < box[2] <= image.width and 0 <= box[1] < box[3] <= image.height):
        raise VehicleError('Atlas part has an empty or out-of-bounds rectangle')
    return image.crop(box)


def extract_previews(database, output, resources):
    with connect(database) as db:
        rows = [json.loads(r[0]) for r in db.execute('SELECT data FROM vehicles')]
    atlases = {}
    failures = []
    for depot in sorted({r['atlas'] for r in rows if r['atlas']}):
        try:
            atlas = resources.atlas(depot)
            slots = atlas.get('slots', {}).get('Elements', [])
            if atlas.get('texture') and atlas.get('parts'):
                slots = [atlas, *slots]
            parts = {}
            # Slot 0 is the highest-resolution authored preview sheet.
            for slot in slots:
                texture = slot.get('texture', {}).get('DepotPath', {}).get('$value')
                if not texture or not slot.get('parts'):
                    continue
                with Image.open(resources.texture(texture)) as image:
                    for part in slot['parts']:
                        name = part['partName']['$value']
                        if name in parts:
                            continue
                        cropped = crop_part(image, part)
                        destination = output / 'previews' / (hashlib.sha256((resources.fingerprint + depot + name).encode()).hexdigest()[:32] + '.png')
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        cropped.save(destination)
                        parts[name] = {'path': str(destination.resolve()), 'atlas': depot, 'part': name,
                                       'texture': texture, 'size': list(cropped.size),
                                       'fingerprint': resources.fingerprint}
                break
            atlases[depot] = parts
        except (VehicleError, OSError, subprocess.CalledProcessError, KeyError) as exc:
            failures.append({'atlas': depot, 'error': str(exc)})
    model_previews = {}
    for row in rows:
        preview = atlases.get(row['atlas'], {}).get(row['atlas_part'])
        if preview:
            model_previews.setdefault(row['template'], preview)
    completed = missing = 0
    with connect(database) as db:
        for row in rows:
            preview = atlases.get(row['atlas'], {}).get(row['atlas_part'])
            fallback = preview is None
            preview = preview or model_previews.get(row['template'])
            if preview:
                metadata = {**preview, 'model_fallback': fallback,
                            'note': 'Game-rendered record icon; paint and equipment may differ from this spawn appearance.'}
                # A generated icon refresh must not replace an explicitly attached studio render.
                db.execute('INSERT INTO previews VALUES(?,?,?,?) ON CONFLICT(record_id) DO UPDATE '
                           'SET path=excluded.path,kind=excluded.kind,metadata=excluded.metadata WHERE previews.kind="game"',
                           (row['record_id'], preview['path'], 'game', json.dumps(metadata)))
                completed += 1
            else:
                db.execute('DELETE FROM previews WHERE record_id=? AND kind="game"', (row['record_id'],))
                missing += 1
    report = {'previews': completed, 'missing': missing, 'failures': failures,
              'source_fingerprint': resources.fingerprint}
    atomic_write_json(output / 'preview-report.json', report)
    return report
