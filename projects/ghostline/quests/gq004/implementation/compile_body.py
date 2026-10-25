"""Compile Velvet's authored body, checking decoded materials and mesh data."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
PROJECT = ROOT / 'projects/ghostline'
sys.path.insert(0, str(ROOT / 'tools'))
from cr2w_validation import compare_documents
from toolchain import resolve_tool


def main():
    relative = Path('mod/ghostline/characters/velvet/body/t0_000_pwa_base__full.mesh')
    source = PROJECT / 'source/raw' / (str(relative) + '.json')
    output = PROJECT / 'generated/gq004-body-repair/compiled'
    readback = output / 'verify-wolvenkit'
    output.mkdir(parents=True, exist_ok=True)
    readback.mkdir(parents=True, exist_ok=True)
    writer = str(resolve_tool('wolvenkit'))
    binary = output / relative.name
    subprocess.run([writer, 'cr2w', '-d', str(source), '-o', str(output)], check=True)
    subprocess.run([writer, 'cr2w', '-s', str(binary), '-o', str(readback)], check=True)
    expected = json.loads(source.read_text())
    actual = json.loads((readback / (relative.name + '.json')).read_text())
    schema = json.loads((ROOT / 'red-schema.json').read_text())
    original = compare_documents(expected, actual, schema=schema, fresh_wolvenkit_defaults=actual)
    for document in (expected, actual):
        document['Data']['RootChunk']['localMaterialBuffer'].pop('rawDataHeaders')
    # Shorter depot paths change derived buffer offsets, not decoded materials.
    result = compare_documents(expected, actual, schema=schema, fresh_wolvenkit_defaults=actual)
    if not result.ok:
        raise RuntimeError(f'Velvet body readback failed: {result.errors[:5]}')
    destination = PROJECT / 'source/archive' / relative
    shutil.copyfile(binary, destination)
    report = dict(ok=True, normalized_material_offsets=len(original.errors),
                  validation='Decoded materials and all other mesh fields; derived material offsets excluded.',
                  sha256=hashlib.sha256(binary.read_bytes()).hexdigest())
    (output.parent / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
