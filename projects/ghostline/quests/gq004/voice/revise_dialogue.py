"""Render reviewable dialogue revisions without replacing approved source takes."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent
REVISIONS = {
    'gq004_01_velvet_job': "Somebody stole Heartbreaker Protocol. I built it to break emotional-conditioning loops. The Claws turned it into a weapon. Now they're selling it.",
    'gq004_01_velvet_route': "Three Claws, two access points. Recover my code and its signing key from the first. Then use the second to shut down the stolen copies. Keep both boxes intact.",
    'gq004_02_velvet_arrive': "That's the operation. Recovery point first. Keep it intact; I need the code, not a smoking case.",
    'gq004_02_velvet_recovery': "Copy the prototype and its signing key. That key lets us shut down the stolen copies.",
    'gq004_02_velvet_patch': "Good. Upload my fix at the second access point. It'll shut down the stolen copies and give the guards a few seconds of optical trouble.",
    'gq004_02_velvet_brand': "Fits in the menu. Very professional.",
    'gq004_02_velvet_success': "Fix accepted. Stolen copies shut down. Oh, look. Hearts. And the bows survived compilation.",
    'gq004_02_velvet_exit': "The guards' optics will recover. The people they sold this to get their emotions back. Now get clear.",
    'gq004_02_velvet_retry': "Link dropped. Nothing committed. Reconnect when you're ready.",
    'gq004_03_velvet_close': "Don't sound so brave. They suit you.",
}


def main():
    output = ROOT / 'generated-voices/gq004/dialogue-review-02'
    output.mkdir(parents=True, exist_ok=True)
    config = json.loads((HERE / 'toolchain.json').read_text(encoding='utf-8'))
    index = json.loads((HERE.parent / 'script/voice-production.json').read_text(encoding='utf-8'))
    entries = []
    allowed = {'key', 'string_id', 'speaker', 'addressee', 'text', 'audio_path',
               'male_audio_path', 'duration_ms', 'beat', 'condition'}
    for entry in index['manifests']:
        manifest = json.loads((HERE.parent / 'script' / entry['file']).read_text(encoding='utf-8'))
        lines = [{k: v for k, v in line.items() if k in allowed}
                 for line in manifest['spoken_lines'] if line['key'] in REVISIONS]
        for line in lines:
            line['text'] = REVISIONS[line['key']]
        (output / entry['file']).write_text(json.dumps(dict(spoken_lines=lines, choice_lines=[]), indent=2) + '\n', encoding='utf-8')
        entries.append(dict(entry, line_count=len(lines), speakers=['Velvet']))
    index.update(manifests=entries, spoken_line_count=len(REVISIONS))
    index_path = output / 'voice-production.json'
    index_path.write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
    prompts = output / 'reference-prompts.json'
    prompts.write_text(json.dumps({'Velvet': dict(text=config['velvet_reference_text'],
        codes=str(ROOT / 'generated-voices/gq004/reference-codes/velvet.json'))}, indent=2) + '\n', encoding='utf-8')
    command = [str(ROOT / 'tools/ghostline-voice/target/release/ghostline-voice.exe'),
        'render-local', '--index', str(index_path), '--checkpoint', config['checkpoint'],
        '--generation-artifact', config['generation_artifact'], '--decoder-artifact', config['decoder_artifact'],
        '--speaker', 'Velvet', '--embedding', f"Velvet={ROOT / 'generated-voices/gq004/embeddings/velvet.safetensors'}",
        '--reference-prompts', str(prompts), '--versions', '1', '--seed-base', '4025',
        '--output', str(output / 'velvet-a')]
    subprocess.run(command, cwd=ROOT, env=dict(os.environ,
        DINOML_NATIVE_LIBRARY_DIR=config['native_library_directory']), check=True)


if __name__ == '__main__':
    main()
