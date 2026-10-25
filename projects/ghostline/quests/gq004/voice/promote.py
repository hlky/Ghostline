"""Promote the current user-reviewed full-reference batch with SHA-256 checks."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import subprocess
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools'))
from build_voice_selection_csv import report_rows


def main():
    lines = [line for path in sorted((HERE.parent / 'script').glob('*_manifest.json'))
             for line in json.loads(path.read_text(encoding='utf-8'))['spoken_lines']]
    for batch in ('female', 'male', 'velvet-a'):
        selected = [dict(line) for line in lines if (line['speaker'] == 'V') == (batch != 'velvet-a')]
        if batch == 'male':
            for line in selected:
                line['audio_path'] = line['male_audio_path']
        manifest = dict(spoken_lines=selected, choice_lines=[])
        path = HERE / f'{batch}.selected.json'
        path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        rows = report_rows(manifest, ROOT / f'generated-voices/gq004/{batch}/render-report.json')
        for row in rows:
            row['selected'] = 'yes' if row['take'] == '0' else ''
        selection = HERE / f'{batch}.selection.csv'
        with selection.open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        subprocess.run([sys.executable, str(ROOT / 'tools/promote_voice_selections.py'),
                        '--manifest', str(path), '--csv', str(selection), '--output-dir', str(HERE / 'source'),
                        '--receipt', str(HERE / f'{batch}.selection-receipt.json')], cwd=ROOT, check=True)
    (HERE / 'review.json').write_text(json.dumps(dict(status='user_reviewed', date='2026-10-25',
        evidence='User: I have listened they sound good', takes='current version00, all three batches',
        conditioning='ghostline-voice full-reference'), indent=2) + '\n', encoding='utf-8')
    all_manifest = HERE / 'selected-manifest.json'
    all_manifest.write_text(json.dumps(dict(spoken_lines=lines, choice_lines=[]), indent=2) + '\n', encoding='utf-8')
    if (HERE / 'dialogue-review-02.json').is_file():
        from apply_revision import main as apply_revision
        apply_revision()


if __name__ == '__main__':
    main()
