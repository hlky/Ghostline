"""Batch native quest conversion, authored-field readback, then scoped publication."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
PROJECT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from toolchain import resolve_tool
from build_world import verify_document


def device_values(document):
    """Expand the clone's shared value handles while retaining alias topology."""
    definitions, uses = {}, {}
    def index(value, path):
        if isinstance(value, dict):
            identifier = value.get('HandleId', value.get('HandleRefId'))
            if identifier is not None:
                uses.setdefault(identifier, []).append(path)
            if 'HandleId' in value:
                if value['HandleId'] in definitions: raise ValueError('Duplicate device value handle')
                definitions[value['HandleId']] = value['Data']
            for key, child in value.items(): index(child, path + '/' + key)
        elif isinstance(value, list):
            for n, child in enumerate(value): index(child, path + '/' + str(n))
    index(document, '')
    def expand(value, active=()):
        if isinstance(value, dict):
            identifier = value.get('HandleId', value.get('HandleRefId'))
            if identifier is not None:
                if identifier in active: raise ValueError('Cyclic device value handle')
                return expand(definitions[identifier], active + (identifier,))
            return {key: expand(child, active) for key, child in value.items()}
        if isinstance(value, list): return [expand(child, active) for child in value]
        return value
    result = expand(document)
    result['Data']['RootChunk']['aliasTopology'] = sorted(sorted(paths) for paths in uses.values() if len(paths) > 1)
    return result


def main():
    from build_icon import main as compile_icon
    compile_icon()
    from compile_body import main as compile_body
    compile_body()
    preview = PROJECT / 'generated/love-actually-preview'
    subprocess.run([sys.executable, str(HERE / 'build.py')], cwd=ROOT, check=True)
    raw, archive = preview / 'source/raw', preview / 'native-binaries'
    # Localization and cloned controllers have their own authored source inputs.
    stage_native_inputs(PROJECT / 'source/raw/mod/gq004', raw / 'mod/gq004')
    schema = json.loads((ROOT / 'red-schema.json').read_text())
    writer = resolve_tool('wolvenkit')
    directories = sorted({p.parent for p in (raw / 'mod/gq004').rglob('*.json')})

    def convert(directory):
        relative = directory.relative_to(raw)
        inputs = preview / 'native-inputs' / relative
        inputs.mkdir(parents=True, exist_ok=True)
        sources = sorted(directory.glob('*.json'))
        target = archive / relative
        readback = preview / 'native-readback' / relative
        for obsolete in inputs.glob('*.json'):
            if obsolete.name not in {p.name for p in sources}: obsolete.unlink()
        for source in sources:
            shutil.copyfile(source, inputs / source.name)
        target.mkdir(parents=True, exist_ok=True)
        readback.mkdir(parents=True, exist_ok=True)
        log = preview / ('convert-' + '-'.join(relative.parts) + '.log')
        with log.open('w') as stream:
            subprocess.run([str(writer), 'cr2w', str(inputs), '-d', '-o', str(target), '-v', 'Minimal'], stdout=stream, stderr=subprocess.STDOUT, check=True)
            subprocess.run([str(writer), 'cr2w', str(target), '-s', '-o', str(readback), '-v', 'Minimal'], stdout=stream, stderr=subprocess.STDOUT, check=True)
        rows = []
        for source in sources:
            binary = target / source.name.removesuffix('.json')
            if binary.read_bytes()[:4] != b'CR2W': raise ValueError(str(binary))
            expected = json.loads(source.read_text(encoding='utf-8'))
            actual = json.loads((readback / source.name).read_text(encoding='utf-8'))
            if binary.suffix == '.ent':
                expected, actual = device_values(expected), device_values(actual)
                # The archive serializer emits independent inline values; WKit's
                # entity writer shares identical PS values between normal and
                # compiled component copies. Existing authored aliases stay strict.
                coalesced = 0
                if not expected['Data']['RootChunk']['aliasTopology']:
                    coalesced = len(actual['Data']['RootChunk']['aliasTopology'])
                    actual['Data']['RootChunk']['aliasTopology'] = []
            result = verify_document(expected, actual, schema)
            if binary.suffix == '.ent': result['reader_coalesced_value_handles'] = coalesced
            result.update(resource=str(binary.relative_to(archive)).replace('\\', '/'),
                          sha256=hashlib.sha256(binary.read_bytes()).hexdigest())
            rows.append(result)
        return rows

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [row for group in pool.map(convert, directories) for row in group]
    report = dict(ok=all(r['ok'] for r in results), resources=results,
                  validation='All authored values and array lengths; constructor defaults disclosed; no in-game claim.')
    (preview / 'native-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    if not report['ok']:
        for row in results:
            if not row['ok']: print(row['resource'], row['errors'][:3])
        raise RuntimeError('Native readback failed; source binaries not published')
    for row in results:
        relative = Path(row['resource'])
        for source, destination in ((archive / relative, PROJECT / 'source/archive' / relative),
                                     (raw / (str(relative) + '.json'), PROJECT / 'source/raw' / (str(relative) + '.json'))):
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
    print(f'Published {len(results)} verified native GQ004 resources')


def stage_native_inputs(source, destination):
    """Keep compiler-owned journal localization; copy only authored inputs."""
    generated = Path('localization/en-us/onscreens/gq004.json.json')
    for folder in ('localization', 'devices', 'ui'):
        for path in (source / folder).rglob('*.json'):
            relative = path.relative_to(source)
            if relative == generated:
                continue
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)


if __name__ == '__main__':
    main()
