"""Compare neutral V references with fixed text, seeds and sampling controls."""
import html
import json
import re
import wave
from functools import lru_cache
from pathlib import Path

import numpy as np
import prepare_vanilla_voices as shared

ROOT = shared.ROOT / 'v-neutral'
IDS = ['1927363080697278468', '1944418147795714048', '1927363080764387332',
       '1927363080563060740', '1947701449755156480', '1939027027790270464']
INSTRUCTION = ("Keep V's dry, casual, matter-of-fact delivery. Follow the reference's natural "
               "pitch, roughness, contractions and uneven pauses. Stay relaxed; do not add "
               "anger, pain, or exaggerated toughness.")
METHODS = [('full', 'Full reference', 'single', None),
           ('instruction', 'Full + V instruction', 'single', INSTRUCTION),
           ('mean', 'Full + mean embedding', 'mean', None),
           ('concat', 'Full + concat embedding', 'concat', None)]


@lru_cache(maxsize=1)
def phoneme_dictionary():
    dictionary = ROOT / 'cmudict.dict'
    if not dictionary.exists():
        response = shared.requests.get(
            'https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict', timeout=60)
        response.raise_for_status()
        dictionary.write_bytes(response.content)
    lexicon = {}
    for line in dictionary.read_text(encoding='utf-8').splitlines():
        fields = line.split()
        if len(fields) > 1 and not fields[0].startswith(';;;'):
            word = re.sub(r'\(\d+\)$', '', fields[0])
            lexicon.setdefault(word, set()).update(re.sub(r'\d', '', p) for p in fields[1:])
    return lexicon, shared.digest(dictionary)


def phoneme_coverage(texts):
    lexicon, dictionary_sha256 = phoneme_dictionary()
    standard = set('AA AE AH AO AW AY B CH D DH EH ER EY F G HH IH IY JH K L M N NG OW OY P R S SH T TH UH UW V W Y Z ZH'.split())
    phones, unknown = set(), set()
    for text in texts:
        for word in re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower()):
            if word not in lexicon:
                unknown.add(word)
            phones.update(lexicon.get(word, set()))
    return dict(estimated_phones=sorted(phones & standard), missing=sorted(standard - phones),
                unknown_words=sorted(unknown), dictionary_sha256=dictionary_sha256,
                caveat='Dictionary estimate from transcripts; pronunciation and actual acoustic coverage may differ.')


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    data = json.loads((shared.ROOT / 'search/v.json').read_text(encoding='utf-8'))
    items = {item['id']: item for item in data['items']}
    rows = []
    for variant in ['female', 'male']:
        for sid in IDS:
            item = items[sid]
            voice = item[variant]
            depot = voice['vo']['main'].replace('\\', '/')
            assert '/vo/' in depot and depot.startswith('base/')
            assert any(s.get('actors') == ['V'] or 'V' in s.get('actors', [])
                       for s in item.get('scenes', {}).values())
            text = voice.get('text') or item['female']['text']
            assert '<' not in text
            rows.append(dict(speaker='V ' + variant.title(), variant=variant, string_id=sid,
                             transcript=text, depot=depot,
                             scene_paths=list(item.get('scenes', {})),
                             selection_reason='Everyday conversational topics in default Judy/Kerry/River scenes; Spoken expression, no injury/combat scenes.',
                             source_url='https://sounddb.redmodding.org/subtitles/' + sid))
    shared.save(ROOT / 'reference-selection.json', rows)
    print('Selected six conversational references per V.', flush=True)
    if any(not (ROOT / 'wem' / r['depot']).exists() for r in rows):
        pattern = '(' + '|'.join(re.escape(Path(r['depot']).name) for r in rows) + ')$'
        shared.run(shared.WKIT, 'unbundle', 'H:/Cyberpunk 2077/archive/pc/content/lang_en_voice.archive',
                   '-o', ROOT / 'wem', '-r', pattern, '-v', 'quiet')
    if any(not (ROOT / 'ogg' / Path(r['depot']).with_suffix('.Ogg')).exists() for r in rows):
        (ROOT / 'ogg').mkdir(exist_ok=True)
        shared.run(shared.WKIT, 'export', ROOT / 'wem', '-o', ROOT / 'ogg',
                   '--gamepath', 'H:/Cyberpunk 2077', '-v', 'quiet')
    for row in rows:
        stem = Path(row['depot']).stem
        wav = ROOT / 'references' / (stem + '.wav')
        wav.parent.mkdir(exist_ok=True)
        if not wav.exists():
            shared.run('ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                       '-i', ROOT / 'ogg' / Path(row['depot']).with_suffix('.Ogg'),
                       '-ar', '24000', '-ac', '1', '-c:a', 'pcm_s16le', wav)
        with wave.open(str(wav)) as source:
            row['duration_s'] = source.getnframes() / 24000
            assert source.getframerate() == 24000 and source.getnchannels() == 1
            assert 1920 <= source.getnframes() <= 240000
        row.update(wav=str(wav), wav_sha256=shared.digest(wav),
                   embedding=str(ROOT / 'embeddings' / (stem + '.safetensors')))
    inputs = {}
    for variant in ['female', 'male']:
        selected = [r for r in rows if r['variant'] == variant]
        concat = ROOT / 'references' / f'v-{variant}-concat.wav'
        with wave.open(str(concat), 'wb') as output:
            output.setparams((1, 2, 24000, 0, 'NONE', 'not compressed'))
            for row in selected:
                with wave.open(row['wav']) as source:
                    output.writeframes(source.readframes(source.getnframes()))
        duration = sum(r['duration_s'] for r in selected)
        assert 30 <= duration <= 43
        inputs[variant] = dict(clips=selected, primary=selected[0], concat_wav=str(concat),
                               concat_duration_s=duration, phoneme_coverage=phoneme_coverage(r['transcript'] for r in selected),
                               single=selected[0]['embedding'],
                               mean=str(ROOT / 'embeddings' / f'v-{variant}-mean.safetensors'),
                               concat=str(ROOT / 'embeddings' / f'v-{variant}-concat.safetensors'),
                               codes=str(ROOT / 'codes' / f'v-{variant}.json'))
    refs = [r['wav'] for r in rows] + [i['concat_wav'] for i in inputs.values()]
    if any(not (ROOT / 'embeddings' / (Path(p).stem + '.safetensors')).exists() for p in refs):
        print('Extracting 12 individual and two concatenated embeddings.', flush=True)
        shared.run(shared.VOICE, 'extract-embeddings', '--checkpoint', shared.BASE / 'model.safetensors',
                   '--speaker-artifact', shared.ART / 'base_speaker_encoder_mel4096',
                   '--reference', *refs, '--output-dir', ROOT / 'embeddings')
    prompts, lines, sources = {}, [], {}
    old_report = json.loads((shared.ROOT / 'samples/render-report.json').read_text(encoding='utf-8'))
    expected_seeds = {}
    for variant, info in inputs.items():
        shared.run(shared.VOICE, 'merge-embeddings', '--input',
                   *[r['embedding'] for r in info['clips']], '--output', info['mean'])
        if not Path(info['codes']).exists():
            shared.run(shared.VOICE, 'encode-reference', '--checkpoint', shared.BASE / 'speech_tokenizer/model.safetensors',
                       '--encoder-artifact', shared.ART / 'tokenizer_encoder_dynamic_s240000',
                       '--reference', info['primary']['wav'], '--output', info['codes'])
        speaker = 'V ' + variant.title() + ' Reference 1'
        key = 'v_' + variant + '_reference_1'
        previous = next(c for c in old_report['candidates'] if c['line_key'] == key)
        expected_seeds[key] = previous['seed']
        info['baseline'] = dict(wav=str(shared.ROOT / 'samples' / previous['wav']), seed=previous['seed'])
        prompts[speaker] = dict(text=info['primary']['transcript'], codes=info['codes'])
        sources[speaker] = dict(mode='speaker_embedding', source=info['single'])
        lines.append(dict(key=key, string_id=shared.string_id(key), speaker=speaker, addressee='Listener',
                          text=shared.TARGET, audio_path=f'mod\\vanilla_audition\\localization\\en-us\\vo\\{key}.wem', duration_ms=7000))
    shared.save(ROOT / 'inputs.json', inputs)
    shared.save(ROOT / 'reference-prompts.json', prompts)
    shared.save(ROOT / 'audition-manifest.json', dict(spoken_lines=lines))
    shared.save(ROOT / 'voice-production.json', dict(schema_version=1, quest='vanilla_audition', spoken_line_count=2,
                voice_sources=sources, manifests=[dict(id='vanilla_audition', file='audition-manifest.json',
                delivery='audition', runtime_status='not_integrated', line_count=2, speakers=sorted(sources))]))
    shared.run(shared.VOICE, 'validate', '--index', ROOT / 'voice-production.json')
    reports = {}
    for method, label, embedding, instruction in METHODS:
        print('Rendering ' + label, flush=True)
        overrides = [value for variant, info in inputs.items()
                     for value in ['--embedding', 'V ' + variant.title() + ' Reference 1=' + info[embedding]]]
        shared.run(shared.VOICE, 'render-local', '--index', ROOT / 'voice-production.json', '--checkpoint', shared.BASE,
                   '--generation-artifact', shared.ART / 'base_generation_p256_f288',
                   '--decoder-artifact', shared.ART / 'tokenizer_decoder_f256',
                   '--reference-prompts', ROOT / 'reference-prompts.json', '--output', ROOT / 'samples' / method,
                   '--versions', '1', '--seed-base', '12000', '--max-frames', '120', *overrides,
                   *(['--instruction', instruction] if instruction else []))
        report = json.loads((ROOT / 'samples' / method / 'render-report.json').read_text(encoding='utf-8'))
        for candidate in report['candidates']:
            assert candidate['seed'] == expected_seeds[candidate['line_key']]
            path = ROOT / 'samples' / method / candidate['wav']
            assert shared.digest(path) == candidate['sha256']
            with wave.open(str(path)) as source:
                assert source.getframerate() == 24000 and source.getnchannels() == 1 and source.getsampwidth() == 2
                audio = np.frombuffer(source.readframes(source.getnframes()), dtype='<i2')
            assert 0 < len(audio) < 120 * 1920 and np.any(audio)
            assert not np.any((audio == -32768) | (audio == 32767))
        reports[method] = dict(label=label, embedding=embedding, instruction=instruction, report=report)
        shared.save(ROOT / 'experiment.json', dict(target_text=shared.TARGET, seed_base=12000,
                    expected_seeds=expected_seeds, methods=reports,
                    controls='Same primary reference codes/transcript, target, per-voice seed, checkpoint, artifacts and sampling. Mean/concat change only embedding; instruction changes only delivery guidance.'))
    page = ['<!doctype html><meta charset="utf-8"><title>V neutral reference comparison</title>',
            '<style>body{font:16px system-ui;background:#11151d;color:#edf1f7;max-width:1400px;margin:32px auto}table{width:100%;table-layout:fixed}td,th{padding:12px;vertical-align:top}audio{width:100%}a{color:#9dcaff}details{margin:16px 0}</style>',
            '<h1>V — neutral references, four methods</h1>',
            '<p>Target: ' + html.escape(shared.TARGET) + '</p>',
            '<p>Each voice keeps its previous Reference 1 seed, shared across all four methods. Mean and concat change the embedding only; full audio conditioning always uses the same primary clip.</p>',
            '<p>V-specific instruction: ' + html.escape(INSTRUCTION) + '</p>']
    for variant, info in inputs.items():
        primary = info['primary']
        page += ['<h2>V ' + variant.title() + '</h2>',
                 '<p>Primary reference: ' + html.escape(primary['transcript']) + '</p>',
                 '<audio controls preload="none" src="' + Path(primary['wav']).relative_to(ROOT).as_posix() + '"></audio>',
                 '<table><tr>' + ''.join('<th>' + label + '</th>' for _, label, _, _ in METHODS) + '</tr><tr>']
        for method, _, _, _ in METHODS:
            page.append(f'<td><audio controls preload="none" src="samples/{method}/vanilla_audition/v_{variant}_reference_1-version00.wav"></audio></td>')
        baseline = Path(info['baseline']['wav']).relative_to(shared.ROOT).as_posix()
        page += ['</tr></table><p>Previous reference + generic instruction (same target and seed):</p>',
                 '<audio controls preload="none" src="../' + baseline + '"></audio>',
                 f'<details><summary>Six reference clips — {info["concat_duration_s"]:.2f}s; estimated {len(info["phoneme_coverage"]["estimated_phones"])}/39 English phonemes</summary>']
        for row in info['clips']:
            page += ['<p>' + html.escape(row['transcript']) + '</p><audio controls preload="none" src="' + Path(row['wav']).relative_to(ROOT).as_posix() + '"></audio>']
        page += ['<p>Concatenated reference:</p><audio controls preload="none" src="' + Path(info['concat_wav']).relative_to(ROOT).as_posix() + '"></audio></details>']
    (ROOT / 'comparison.html').write_text('\n'.join(page), encoding='utf-8')
    print('Complete: eight verified auditions with unchanged text and seeds.', flush=True)


if __name__ == '__main__':
    main()
