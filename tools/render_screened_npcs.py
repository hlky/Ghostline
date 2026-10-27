"""Render six full-reference auditions from screened, scene-linked sources."""
import html
import json
import re
import wave
import argparse
from pathlib import Path

import numpy as np
import prepare_vanilla_voices as shared

ROOT = shared.ROOT / 'npc-screened'


def main(prepare_only=False, actors=None):
    reachability = json.loads((ROOT / 'scene-reachability.json').read_text(encoding='utf-8'))
    assert all(v['reachable_from_scene_start'] for scene in reachability.values()
               for v in scene['target_sections'].values())
    candidates = {r['string_id']: r for r in json.loads((ROOT / 'decoded-candidates.json').read_text(encoding='utf-8'))}
    groups = {'Songbird': [['3273933107471863812', '3273933107471863824'],
                          ['2983635373759942656', '2983636822774534144']],
              'Kerry': [['1807175567395217412'], ['1834734088295673856']],
              'Panam': [['1896726949659815948'], ['1896726949659815960']]}
    if actors:
        groups = {actor: options for actor, options in groups.items() if actor in actors}
    rows = []
    for actor, options in groups.items():
        for number, ids in enumerate(options, 1):
            source = [candidates[sid] for sid in ids]
            if len(source) > 1:
                wav = ROOT / 'references' / f'{actor.lower()}-lab-{number}.wav'
                with wave.open(str(wav), 'wb') as out:
                    out.setparams((1, 2, 24000, 0, 'NONE', 'not compressed'))
                    for clip in source:
                        with wave.open(clip['wav']) as inp:
                            out.writeframes(inp.readframes(inp.getnframes()))
            else:
                wav = Path(source[0]['wav'])
            with wave.open(str(wav)) as audio:
                samples = audio.getnframes()
                assert 1920 <= samples <= 240000
            rows.append(dict(actor=actor, speaker=actor + f' Reference {number}',
                             key=actor.lower() + f'_reference_{number}', sources=source,
                             transcript=' '.join(c['transcript'] for c in source), wav=str(wav),
                             wav_sha256=shared.digest(wav), samples=samples, duration_s=samples / 24000,
                             embedding=str(ROOT / 'embeddings' / (wav.stem + '.safetensors')),
                             codes=str(ROOT / 'codes' / (wav.stem + '.json'))))
    pending = [r for r in rows if not Path(r['embedding']).exists()]
    if pending:
        print(f'Extracting {len(pending)} matching embeddings.', flush=True)
        shared.run(shared.VOICE, 'extract-embeddings', '--checkpoint', shared.BASE / 'model.safetensors',
                   '--speaker-artifact', shared.ART / 'base_speaker_encoder_mel4096',
                   '--reference', *[r['wav'] for r in pending], '--output-dir', ROOT / 'embeddings')
    for row in rows:
        if not Path(row['codes']).exists():
            shared.run(shared.VOICE, 'encode-reference', '--checkpoint', shared.BASE / 'speech_tokenizer/model.safetensors',
                       '--encoder-artifact', shared.ART / 'tokenizer_encoder_dynamic_s240000',
                       '--reference', row['wav'], '--output', row['codes'])
        code = json.loads(Path(row['codes']).read_text(encoding='utf-8'))
        assert code['frame_count'] == (row['samples'] + 1919) // 1920 and code['code_groups'] == 16
        row['codes_sha256'] = shared.digest(Path(row['codes']))
        row['embedding_sha256'] = shared.digest(Path(row['embedding']))
        print('Cached ' + row['speaker'], flush=True)
    if prepare_only:
        shared.save(ROOT / 'prepared-references.json', rows)
        return
    original = shared.ROOT / 'npc-revision2'
    index = json.loads((original / 'voice-production.json').read_text(encoding='utf-8'))
    manifest = json.loads((original / 'audition-manifest.json').read_text(encoding='utf-8'))
    # Retain original key, text and seed namespace for each option.
    index['voice_sources'] = {r['speaker']: {'mode': 'speaker_embedding', 'source': r['embedding']} for r in rows}
    shared.save(ROOT / 'voice-production.json', index)
    shared.save(ROOT / 'audition-manifest.json', manifest)
    shared.save(ROOT / 'reference-prompts.json', {r['speaker']: {'text': r['transcript'], 'codes': r['codes']} for r in rows})
    shared.save(ROOT / 'catalog.json', {'references': rows, 'method': 'full_reference', 'instruction': None,
                                      'review_status': 'Source-screened; awaiting user audition preference'})
    shared.run(shared.VOICE, 'validate', '--index', ROOT / 'voice-production.json')
    print('Rendering six full-reference auditions, no instructions.', flush=True)
    shared.run(shared.VOICE, 'render-local', '--index', ROOT / 'voice-production.json', '--checkpoint', shared.BASE,
               '--generation-artifact', shared.ART / 'base_generation_p256_f288',
               '--decoder-artifact', shared.ART / 'tokenizer_decoder_f256',
               '--reference-prompts', ROOT / 'reference-prompts.json', '--output', ROOT / 'samples/full',
               '--versions', '1', '--seed-base', '12000', '--max-frames', '120')
    report = json.loads((ROOT / 'samples/full/render-report.json').read_text(encoding='utf-8'))
    previous = json.loads((original / 'samples/full/render-report.json').read_text(encoding='utf-8'))
    for candidate in report['candidates']:
        old = next(c for c in previous['candidates'] if c['line_key'] == candidate['line_key'])
        assert candidate['seed'] == old['seed']
        path = ROOT / 'samples/full' / candidate['wav']
        assert shared.digest(path) == candidate['sha256']
        with wave.open(str(path)) as w:
            assert w.getframerate() == 24000 and w.getnchannels() == 1 and w.getsampwidth() == 2
            audio = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2')
        assert 0 < len(audio) < 120 * 1920 and np.any(audio)
        assert not np.any((audio == -32768) | (audio == 32767))
    page = ['<!doctype html><meta charset="utf-8"><title>Screened NPC references</title>',
            '<style>body{font:16px system-ui;background:#11151d;color:#edf1f7;max-width:1200px;margin:32px auto}table{width:100%;table-layout:fixed}td{padding:12px;vertical-align:top}audio{width:100%}a{color:#9dcaff}</style>',
            '<h1>Songbird, Kerry and Panam — screened gameplay sources</h1>',
            '<p>Same spoken text, per-option seeds and full-reference settings; no instruction or corrective EQ.</p>',
            '<p>Source contexts: Firestarter lab setup before the crisis; Off the Leash terrace conversation; Riders on the Storm shelter conversation.</p>',
            '<p><a href="scene-reachability.json">Game scene connections</a> · <a href="signal-screen.json">Source frequency screening</a></p>']
    for actor in groups:
        page.append('<h2>' + actor + '</h2><table><tr>')
        for row in [r for r in rows if r['actor'] == actor]:
            page.append('<td><p>' + html.escape(row['transcript']) + '</p>')
            for source in row['sources']:
                src = 'ogg/' + Path(source['depot']).with_suffix('.Ogg').as_posix()
                page.append('<p>Original game export</p><audio controls preload="none" src="' + src + '"></audio>')
            page.append('<p>Model reference</p><audio controls preload="none" src="' + Path(row['wav']).relative_to(ROOT).as_posix() + '"></audio>')
            file = f'vanilla_audition/{row["key"]}-version00.wav'
            page.append(f'<p>New full-reference result</p><audio controls preload="none" src="samples/full/{file}"></audio>')
            page.append(f'<p>Previous result — same text and seed</p><audio controls preload="none" src="../npc-revision2/samples/full/{file}"></audio></td>')
        page.append('</tr></table>')
    markup = '\n'.join(page)
    assert all((ROOT / p).exists() for p in re.findall(r'src="([^"]+)"', markup))
    (ROOT / 'comparison.html').write_text(markup, encoding='utf-8')
    shared.save(ROOT / 'experiment.json', {'target_text': manifest['spoken_lines'][0]['text'], 'seed_base': 12000,
                'method': 'full_reference', 'instruction': None, 'checkpoint': str(shared.BASE),
                'generation_artifact': str(shared.ART / 'base_generation_p256_f288'),
                'decoder_artifact': str(shared.ART / 'tokenizer_decoder_f256'), 'max_frames': 120, 'report': report})
    print('Complete: six verified auditions with unchanged text and seeds.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--actor', action='append')
    options = parser.parse_args()
    main(options.prepare_only, options.actor)
