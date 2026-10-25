"""Compile audio-bound preview lipsync without promoting audition WAVs."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import wave

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
QUEST = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))


def gender_variants(document: dict, lines: list[dict], batch: str) -> dict[str, list[str]]:
    """Name male V clips correctly and share Velvet's take across player genders."""
    animations = {row['name']: row for row in document['animations']}
    result = {}
    for line in lines:
        suffix = f"{int(line['string_id']):016X}"
        female, male = 'f_' + suffix, 'm_' + suffix
        if batch == 'male':
            if female in animations:
                if male in animations:
                    raise ValueError(f'Duplicate male lipsync variant: {male}')
                animation = animations.pop(female)
                animation['name'] = male
                animations[male] = animation
            if male not in animations:
                raise ValueError(f'Missing compiled lipsync: {male}')
            result[line['key']] = [male]
        else:
            if female not in animations:
                raise ValueError(f'Missing compiled lipsync: {female}')
            result[line['key']] = [female]
            if batch == 'velvet-a':
                if male not in animations:
                    animation = copy.deepcopy(animations[female])
                    animation['name'] = male
                    document['animations'].append(animation)
                    animations[male] = animation
                result[line['key']].append(male)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', choices=['female', 'male', 'velvet-a'], required=True)
    parser.add_argument('--candidate-root', type=Path, default=ROOT / 'generated-voices/gq004')
    parser.add_argument('--manifest-directory', type=Path, default=QUEST / 'script')
    parser.add_argument('--extra-python-path', type=Path)
    parser.add_argument('--donor-glb', type=Path, required=True)
    parser.add_argument('--source', required=True)
    parser.add_argument('--device', default='auto')
    args = parser.parse_args()
    if args.device == 'cpu':
        # G2P uses many tiny NumPy matrix products; large BLAS pools stall this batch.
        os.environ['OPENBLAS_NUM_THREADS'] = '1'
        os.environ['MKL_NUM_THREADS'] = '4'
        os.environ['OMP_NUM_THREADS'] = '4'
    if args.extra_python_path:
        # Keep the selected PyTorch environment ahead of optional phonemizer packages.
        sys.path.append(str(args.extra_python_path.resolve()))
    import nltk
    nltk_directory = args.candidate_root / 'lipsync/nltk-data'
    nltk.data.path.insert(0, str(nltk_directory))
    for package, kind in [('cmudict', 'corpora'), ('averaged_perceptron_tagger', 'taggers'), ('averaged_perceptron_tagger_eng', 'taggers')]:
        try:
            nltk.data.find(f'{kind}/{package}')
        except LookupError:
            if not nltk.download(package, download_dir=str(nltk_directory), quiet=True):
                raise RuntimeError(f'Could not download phonemizer data: {package}')
    from compile_lipsync_manifest import build_parser, compile_manifest
    if args.device == 'cpu':
        import torch
        torch.set_num_threads(4)
    source = args.candidate_root / args.batch
    report = json.loads((source / 'render-report.json').read_text(encoding='utf-8'))
    candidates = {row['line_key']: row for row in report['candidates'] if row['version'] == 0}
    output = args.candidate_root / 'lipsync' / args.batch
    output.mkdir(parents=True, exist_ok=True)
    lines, inputs = [], []
    for path in sorted(args.manifest_directory.glob('*_manifest.json')):
        manifest = json.loads(path.read_text(encoding='utf-8'))
        for original in manifest['spoken_lines']:
            if original['key'] not in candidates:
                continue
            line = dict(original)
            candidate = candidates[line['key']]
            wav = source / candidate['wav']
            digest = hashlib.sha256(wav.read_bytes()).hexdigest()
            if digest != candidate['sha256']:
                raise ValueError(f'Candidate audio changed: {wav}')
            if args.batch == 'male':
                line['audio_path'] = line['male_audio_path']
            basename = line['audio_path'].replace('\\', '/').split('/')[-1].replace('.wem', '.wav')
            destination = output / 'audio' / basename
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(wav, destination)
            with wave.open(str(wav)) as stream:
                line['duration_ms'] = round(stream.getnframes() / stream.getframerate() * 1000)
            lines.append(line)
            inputs.append(dict(key=line['key'], string_id=line['string_id'], wav=str(wav), sha256=digest, duration_ms=line['duration_ms']))
    if not lines:
        raise ValueError('No candidate lines found')
    manifest_path = output / 'candidate-manifest.json'
    manifest_path.write_text(json.dumps(dict(spoken_lines=lines, choice_lines=[]), indent=2) + '\n', encoding='utf-8')
    options = build_parser().parse_args([
        str(manifest_path), str(output / 'audio'), str(args.donor_glb),
        str(output / 'gq004.anims.glb'), '--source', args.source,
        '--reports', str(output / 'alignments'), '--device', args.device,
        '--clear-donor-controls', '--neutral-skeleton',
    ])
    compile_manifest(options)
    from lipsync_glb import read_glb, write_glb
    document, chunks = read_glb(output / 'gq004.anims.glb')
    variants = gender_variants(document, lines, args.batch)
    write_glb(output / 'gq004.anims.glb', document, chunks)
    receipt = dict(schema_version=1, status='unreviewed_candidate_lipsync', batch=args.batch,
                   inputs=inputs, glb=str(output / 'gq004.anims.glb'),
                   donor_glb=str(args.donor_glb.resolve()), source_animation=args.source,
                   animation_variants=variants)
    (output / 'inputs.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(f'Compiled {len(lines)} audio-bound candidate clips: {output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
