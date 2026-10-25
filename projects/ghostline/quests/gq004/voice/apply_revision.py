"""Apply the explicitly approved second dialogue pass, preserving prior takes."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import wave

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent


def main():
    review = json.loads((HERE / 'dialogue-review-02.json').read_text(encoding='utf-8'))
    if review['status'] != 'user_reviewed':
        raise ValueError('Replacement takes require an explicit listening selection')
    candidate = ROOT / review['candidate_root']
    report = json.loads((candidate / 'velvet-a/render-report.json').read_text(encoding='utf-8'))
    records = {r['line_key']: r for r in report['candidates']}
    replacements = {}
    for path in candidate.glob('*_manifest.json'):
        for line in json.loads(path.read_text(encoding='utf-8'))['spoken_lines']:
            record = records[line['key']]
            wav = candidate / 'velvet-a' / record['wav']
            digest = hashlib.sha256(wav.read_bytes()).hexdigest()
            if digest != record['sha256'] or digest != review['selected_sha256'][line['key']]:
                raise ValueError('Approved candidate changed: ' + line['key'])
            with wave.open(str(wav)) as stream:
                line['duration_ms'] = round(stream.getnframes() / stream.getframerate() * 1000)
            destination = HERE / 'source' / Path(line['audio_path'].replace('\\', '/')).with_suffix('.wav').name
            backup = candidate / 'previous-source' / destination.name
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copyfile(destination, backup)
            shutil.copyfile(wav, destination)
            replacements[line['key']] = line
    for path in [*sorted((HERE.parent / 'script').glob('*_manifest.json')),
                 HERE / 'selected-manifest.json', HERE / 'velvet-a.selected.json']:
        manifest = json.loads(path.read_text(encoding='utf-8'))
        for line in manifest['spoken_lines']:
            if line['key'] in replacements:
                selected = replacements[line['key']]
                # Keep runtime beat, lipsync and phone metadata on the original.
                line.update(text=selected['text'], duration_ms=selected['duration_ms'])
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Applied {len(replacements)} user-selected replacement takes; previous sources preserved')


if __name__ == '__main__':
    main()
