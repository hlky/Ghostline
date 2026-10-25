"""Cook the audio-bound, reviewed facial clips into a quest-owned animset."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
sys.path.insert(0, str(ROOT / 'tools'))
from lipsync_glb import read_glb, write_glb


def selected_glb(path, exclude=()):
    document, chunks = read_glb(path)
    receipt = json.loads((path.parent / 'inputs.json').read_text())
    names = {name for variants in receipt['animation_variants'].values() for name in variants}
    names.difference_update(exclude)
    document['animations'] = [a for a in document['animations'] if a['name'] in names]
    if {a['name'] for a in document['animations']} != names:
        raise ValueError('Missing reviewed lipsync clips')
    return document, chunks


def merge(paths, replacement_names=()):
    document, chunks = selected_glb(paths[0], replacement_names)
    document = copy.deepcopy(document)
    payload = bytearray(chunks[0][1])
    names = {a['name'] for a in document['animations']}
    for index, path in enumerate(paths[1:], start=1):
        other, extra = selected_glb(path, replacement_names if index < 3 else ())
        if ([n.get('name') for n in document['nodes']] != [n.get('name') for n in other['nodes']]
            or document['skins'][0]['extras']['trackNames'] != other['skins'][0]['extras']['trackNames']
            or document['skins'][0]['extras']['boneNames'] != other['skins'][0]['extras']['boneNames']):
            raise ValueError('Facial skeleton/track contracts differ')
        if len(extra) != 1 or extra[0][0] != chunks[0][0]:
            raise ValueError('Expected a single binary buffer')
        payload.extend(b'\0' * (-len(payload) % 4))
        byte_offset, view_offset, accessor_offset = len(payload), len(document['bufferViews']), len(document['accessors'])
        for view in other['bufferViews']:
            view = copy.deepcopy(view)
            view['byteOffset'] = view.get('byteOffset', 0) + byte_offset
            document['bufferViews'].append(view)
        for accessor in other['accessors']:
            accessor = copy.deepcopy(accessor)
            if 'sparse' in accessor:
                raise ValueError('Sparse accessor relocation is not supported')
            if 'bufferView' in accessor:
                accessor['bufferView'] += view_offset
            document['accessors'].append(accessor)
        for animation in other['animations']:
            animation = copy.deepcopy(animation)
            if animation['name'] in names:
                raise ValueError('Duplicate animation name: ' + animation['name'])
            names.add(animation['name'])
            for sampler in animation['samplers']:
                sampler['input'] += accessor_offset
                sampler['output'] += accessor_offset
            document['animations'].append(animation)
        payload.extend(extra[0][1])
    document['buffers'][0]['byteLength'] = len(payload)
    return document, [(chunks[0][0], bytes(payload))]


def main():
    candidate = ROOT / 'generated-voices/gq004/lipsync'
    receipts = [candidate / batch / 'inputs.json' for batch in ('female', 'male', 'velvet-a')]
    paths = [p.parent / 'gq004.anims.glb' for p in receipts]
    replaced = set()
    review_path = Path(__file__).parent / 'dialogue-review-02.json'
    if review_path.exists():
        review = json.loads(review_path.read_text(encoding='utf-8'))
        if review['status'] != 'user_reviewed':
            raise ValueError('Unreviewed revision cannot replace runtime facial clips')
        receipt = ROOT / review['candidate_root'] / 'lipsync/velvet-a/inputs.json'
        data = json.loads(receipt.read_text(encoding='utf-8'))
        replaced = {name for names in data['animation_variants'].values() for name in names}
        for row in data['inputs']:
            if row['sha256'] != review['selected_sha256'][row['key']]:
                raise ValueError('Facial clip is not bound to the selected revised take')
            selected = Path(__file__).parent / 'source' / (row['key'] + '.wav')
            if hashlib.sha256(selected.read_bytes()).hexdigest() != row['sha256']:
                raise ValueError('Promoted source differs from revised facial input')
        receipts.append(receipt)
        paths.append(receipt.parent / 'gq004.anims.glb')
    # A changed source take invalidates its existing facial alignment.
    for receipt_path in receipts:
        receipt = json.loads(receipt_path.read_text())
        for row in receipt['inputs']:
            if hashlib.sha256(Path(row['wav']).read_bytes()).hexdigest() != row['sha256']:
                raise ValueError('Lipsync audio hash mismatch: ' + row['key'])
    output = ROOT / 'projects/ghostline/generated/gq004-lipsync'
    output.mkdir(parents=True, exist_ok=True)
    document, chunks = merge(paths, replaced)
    # Keep one neutral skeletal basis across the female/male donor exports;
    # retain each take's facial curves and measured duration.
    from lipsync_compiler import build_neutral_skeletal_channels
    durations = {}
    for receipt_path in receipts:
        receipt = json.loads(receipt_path.read_text())
        for row in receipt['inputs']:
            for name in receipt['animation_variants'][row['key']]:
                durations[name] = row['duration_ms'] / 1000
    for animation in document['animations']:
        build_neutral_skeletal_channels(document, chunks, animation['name'], durations[animation['name']])
    write_glb(output / 'gq004.anims.glb', document, chunks)
    donor = ROOT / 'generated/lipsync-corpus/cache/extracted/voice/base/localization/en-us/lipsync/base/quest/main_quests/part1/q112/scenes/q112_07a_parade_gameplay_and_combat_routines/civ_low_f_47_afam_50.anims'
    shutil.copyfile(donor, output / 'gq004.anims')
    subprocess.run([str(ROOT / 'tools/WolvenKit.AnimImport/bin/Release/net8.0/WolvenKit.AnimImport.exe'),
                    'K:/Cyberpunk 2077', str(output / 'gq004.anims.glb'), str(output)], check=True, cwd=ROOT)
    destination = ROOT / 'projects/ghostline/source/archive/base/localization/en-us/lipsync/mod/gq004/gq004.anims'
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(output / 'gq004.anims', destination)
    (output / 'receipt.json').write_text(json.dumps(dict(clips=len(document['animations']),
        sha256=hashlib.sha256(destination.read_bytes()).hexdigest(), output=str(destination),
        audio_hashes_verified=True), indent=2) + '\n')


if __name__ == '__main__':
    main()
