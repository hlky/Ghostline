"""Prepare conversational NPC references and optional accent auditions."""
import html
import json
import re
import wave
from pathlib import Path

import numpy as np
import prepare_vanilla_voices as shared
from compare_v_references import phoneme_coverage

ROOT = shared.ROOT / 'npc-neutral'
SELECTIONS = {
    'Judy': ['1947785877336580096', '1944449961339895808'],
    'Panam': ['1705580412252508160', '1976297277084004352'],
    'Johnny': ['1955027583274602496', '3362307319563395072'],
    'Jackie': ['1628830076146479104', '1660749876914311168'],
    'Viktor': ['2009733986011078656', '1720034429371994112'],
    'Takemura': ['2037552315492753408', '2018919758379376640'],
    'River': ['1940238472842448896', '1940245564756201472'],
    'Kerry': ['1938689005456060416', '1938722775592726528'],
    'Reed': ['2889753876754354176', '3339213164162826240'],
    'Songbird': ['3233133047726571540', '3495402713838362624'],
    'Placide': ['1969066731232841728', '1561891919229161472'],
}
ACCENT_INSTRUCTIONS = {
    'Placide': ("Preserve the reference speaker's Haitian Creole-influenced English accent, "
                "low resonant tone and deliberate rhythm. Keep the delivery natural and calm; "
                "do not exaggerate the accent."),
    'Takemura': ("Preserve the reference speaker's Japanese-accented English and measured syllable timing. "
                 "Match the reference's natural pitch and tone. Keep the delivery calm; do not exaggerate the accent."),
}
TARGET = shared.TARGET.replace('I will', "I'll")


def validate_report(directory):
    report = json.loads((directory / 'render-report.json').read_text(encoding='utf-8'))
    for candidate in report['candidates']:
        path = directory / candidate['wav']
        assert shared.digest(path) == candidate['sha256']
        with wave.open(str(path)) as source:
            assert source.getframerate() == 24000 and source.getnchannels() == 1 and source.getsampwidth() == 2
            audio = np.frombuffer(source.readframes(source.getnframes()), dtype='<i2')
        assert 0 < len(audio) < 120 * 1920 and np.any(audio)
        assert not np.any((audio == -32768) | (audio == 32767))
    return report


def main(prepare_only=False):
    ROOT.mkdir(exist_ok=True)
    rows = []
    for actor, ids in SELECTIONS.items():
        items = {i['id']: i for i in shared.search(actor)['items']}
        for number, sid in enumerate(ids, 1):
            item = items[sid]
            voice = item['female']
            text = voice['text']
            depot = voice['vo']['main'].replace('\\', '/')
            assert '<' not in text and '/vo/' in depot
            assert any(actor in s.get('actors', []) and
                       any(n.get('expression') == 'Vo_Expression_Spoken' for n in s.get('nodes', {}).values())
                       for s in item.get('scenes', {}).values())
            rows.append(dict(actor=actor, speaker=actor + f' Reference {number}',
                        key=actor.lower() + f'_reference_{number}', string_id=sid,
                        transcript=text, depot=depot, scene_paths=list(item.get('scenes', {})),
                        source_url='https://sounddb.redmodding.org/subtitles/' + sid,
                        selection_status='Selected for conversational context; awaiting audio listening review',
                        phoneme_coverage=phoneme_coverage([text])))
    shared.save(ROOT / 'selection.json', rows)
    print(f'Selected {len(rows)} conversational references for {len(SELECTIONS)} NPCs.', flush=True)
    for prefix, archive in [('base', 'content'), ('ep1', 'ep1')]:
        depots = [r['depot'] for r in rows if r['depot'].startswith(prefix + '/')]
        if any(not (ROOT / 'wem' / p).exists() for p in depots):
            pattern = '(' + '|'.join(re.escape(Path(p).name) for p in depots) + ')$'
            shared.run(shared.WKIT, 'unbundle', f'H:/Cyberpunk 2077/archive/pc/{archive}/lang_en_voice.archive',
                       '-o', ROOT / 'wem', '-r', pattern, '-v', 'quiet')
    if any(not (ROOT / 'ogg' / Path(r['depot']).with_suffix('.Ogg')).exists() for r in rows):
        (ROOT / 'ogg').mkdir(exist_ok=True)
        shared.run(shared.WKIT, 'export', ROOT / 'wem', '-o', ROOT / 'ogg',
                   '--gamepath', 'H:/Cyberpunk 2077', '-v', 'quiet')
    pipeline = {'models': [shared.identity(shared.BASE / 'model.safetensors'),
                           shared.identity(shared.BASE / 'speech_tokenizer/model.safetensors')],
                'artifacts': [shared.identity(p) for name in
                              ['base_speaker_encoder_mel4096', 'tokenizer_encoder_dynamic_s240000']
                              for p in sorted((shared.ART / name).rglob('*')) if p.is_file()]}
    pending = []
    for row in rows:
        stem = Path(row['depot']).stem
        wav = ROOT / 'references' / (stem + '.wav')
        wav.parent.mkdir(exist_ok=True)
        if not wav.exists():
            shared.run('ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                       '-i', ROOT / 'ogg' / Path(row['depot']).with_suffix('.Ogg'),
                       '-ar', '24000', '-ac', '1', '-c:a', 'pcm_s16le', wav)
        with wave.open(str(wav)) as source:
            row['samples'] = source.getnframes()
            row['duration_s'] = source.getnframes() / 24000
            assert source.getframerate() == 24000 and source.getnchannels() == 1
            assert 1920 <= source.getnframes() <= 240000
        row.update(wav=str(wav), wav_sha256=shared.digest(wav),
                   embedding=str(ROOT / 'embeddings' / (stem + '.safetensors')),
                   codes=str(ROOT / 'codes' / (stem + '.json')))
        receipt = ROOT / 'cache' / (stem + '.json')
        fingerprint = dict(wav_sha256=row['wav_sha256'], pipeline=pipeline)
        if not (receipt.exists() and json.loads(receipt.read_text(encoding='utf-8')) == fingerprint
                and Path(row['codes']).exists() and Path(row['embedding']).exists()):
            pending.append((row, receipt, fingerprint))
    if prepare_only:
        shared.save(ROOT / 'decoded-candidates.json', rows)
        print(f'Decoded {len(rows)} candidates for source-audio screening.', flush=True)
        return
    if pending:
        shared.run(shared.VOICE, 'extract-embeddings', '--checkpoint', shared.BASE / 'model.safetensors',
                   '--speaker-artifact', shared.ART / 'base_speaker_encoder_mel4096',
                   '--reference', *[r['wav'] for r, _, _ in pending], '--output-dir', ROOT / 'embeddings')
    for number, (row, receipt, fingerprint) in enumerate(pending, 1):
        shared.run(shared.VOICE, 'encode-reference', '--checkpoint', shared.BASE / 'speech_tokenizer/model.safetensors',
                   '--encoder-artifact', shared.ART / 'tokenizer_encoder_dynamic_s240000',
                   '--reference', row['wav'], '--output', row['codes'])
        shared.save(receipt, fingerprint)
        print(f'Cached {number}/{len(pending)}: {row["actor"]}', flush=True)
    sources, prompts, lines = {}, {}, []
    for row in rows:
        codes = json.loads(Path(row['codes']).read_text(encoding='utf-8'))
        assert codes['frame_count'] == (row['samples'] + 1919) // 1920 and codes['code_groups'] == 16
        assert len(codes['values']) == codes['frame_count'] * 16
        row.update(codes_sha256=shared.digest(Path(row['codes'])),
                   embedding_sha256=shared.digest(Path(row['embedding'])))
        sources[row['speaker']] = dict(mode='speaker_embedding', source=row['embedding'])
        prompts[row['speaker']] = dict(text=row['transcript'], codes=row['codes'])
        lines.append(dict(key=row['key'], string_id=shared.string_id(row['key']), speaker=row['speaker'],
                          addressee='Listener', text=TARGET, duration_ms=7000,
                          audio_path=f'mod\\vanilla_audition\\localization\\en-us\\vo\\{row["key"]}.wem'))
    shared.save(ROOT / 'catalog.json', dict(references=rows, default_method='full_reference',
                default_instruction=None, accent_instructions=ACCENT_INSTRUCTIONS, target_text=TARGET,
                review_status='awaiting listening review'))
    shared.save(ROOT / 'reference-prompts.json', prompts)
    shared.save(ROOT / 'audition-manifest.json', dict(spoken_lines=lines))
    shared.save(ROOT / 'voice-production.json', dict(schema_version=1, quest='vanilla_audition',
                spoken_line_count=len(lines), voice_sources=sources,
                manifests=[dict(id='vanilla_audition', file='audition-manifest.json', delivery='audition',
                                runtime_status='not_integrated', line_count=len(lines), speakers=sorted(sources))]))
    shared.run(shared.VOICE, 'validate', '--index', ROOT / 'voice-production.json')
    args = [shared.VOICE, 'render-local', '--index', ROOT / 'voice-production.json', '--checkpoint', shared.BASE,
            '--generation-artifact', shared.ART / 'base_generation_p256_f288',
            '--decoder-artifact', shared.ART / 'tokenizer_decoder_f256',
            '--reference-prompts', ROOT / 'reference-prompts.json', '--versions', '1',
            '--seed-base', '12000', '--max-frames', '120']
    print(f'Rendering {len(rows)} full-reference auditions without instructions.', flush=True)
    shared.run(*args, '--output', ROOT / 'samples/full')
    full = validate_report(ROOT / 'samples/full')
    for actor, instruction in ACCENT_INSTRUCTIONS.items():
        print('Comparing accent guidance for ' + actor, flush=True)
        shared.run(*args, '--output', ROOT / 'samples' / (actor.lower() + '-accent'),
                   '--instruction', instruction, '--speaker', actor + ' Reference 1', '--speaker', actor + ' Reference 2')
        report = validate_report(ROOT / 'samples' / (actor.lower() + '-accent'))
        for c in report['candidates']:
            assert c['seed'] == next(r['seed'] for r in full['candidates'] if r['line_key'] == c['line_key'])
    page = ['<!doctype html><meta charset="utf-8"><title>Neutral NPC references</title>',
            '<style>body{font:16px system-ui;background:#11151d;color:#edf1f7;max-width:1150px;margin:32px auto}table{width:100%;table-layout:fixed}td{padding:12px;vertical-align:top}audio{width:100%}a{color:#9dcaff}</style>',
            '<h1>NPCs — conversational references</h1><p>Full reference without instructions is the default. Two new reference candidates per NPC; listening review determines the selection.</p>',
            '<p>Target: ' + html.escape(TARGET) + '</p>',
            '<p><a href="../v-neutral/contraction/comparison.html">Both Vs: selected full reference with contracted text</a></p>']
    for actor in SELECTIONS:
        page.append('<h2>' + actor + '</h2><table><tr>')
        for row in [r for r in rows if r['actor'] == actor]:
            page.append('<td><p>' + html.escape(row['transcript']) + '</p><p>Reference</p><audio controls preload="none" src="' + Path(row['wav']).relative_to(ROOT).as_posix() + '"></audio>')
            page.append(f'<p>Full reference — no instruction</p><audio controls preload="none" src="samples/full/vanilla_audition/{row["key"]}-version00.wav"></audio>')
            if actor in ACCENT_INSTRUCTIONS:
                page.append(f'<p>Full reference + accent guidance</p><audio controls preload="none" src="samples/{actor.lower()}-accent/vanilla_audition/{row["key"]}-version00.wav"></audio>')
            page.append('</td>')
        page.append('</tr></table>')
        if actor in ACCENT_INSTRUCTIONS:
            page.append('<p>Accent instruction: ' + html.escape(ACCENT_INSTRUCTIONS[actor]) + '</p>')
    markup = '\n'.join(page)
    assert all((ROOT / p).exists() for p in re.findall(r'src="([^"]+)"', markup))
    (ROOT / 'comparison.html').write_text(markup, encoding='utf-8')
    original = shared.ROOT / 'comparison.html'
    markup = original.read_text(encoding='utf-8')
    if 'id="neutral-npc-comparison"' not in markup:
        markup = markup.replace('<h1>', '<p id="neutral-npc-comparison"><a href="npc-neutral/comparison.html">New neutral NPC references, including Placide</a></p><h1>', 1)
        original.write_text(markup, encoding='utf-8')
    print(f'Complete: {len(rows)} cached reference pairs and {len(rows) + 2 * len(ACCENT_INSTRUCTIONS)} validated auditions.', flush=True)


if __name__ == '__main__':
    main()
