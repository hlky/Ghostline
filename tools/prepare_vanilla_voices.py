"""Cache vanilla reference options and audition full-reference voice clones.

Run from the repository root with the activated DinoML toolchain. Existing
reference codes/embeddings are reused only when their input fingerprints match.
"""
import hashlib
import html
import json
import re
import struct
import subprocess
import wave
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'generated-voices/vanilla-library'
TWINS = REPO / 'generated-voices/french-twins'
BASE = Path('X:/checkpoints/Qwen/Qwen3-TTS-12Hz-1.7B-Base')
VOICE = REPO / 'tools/ghostline-voice/target/release/ghostline-voice.exe'
WKIT = Path('H:/WolvenKit.Console-8.17.4/WolvenKit.CLI.exe')
ART = TWINS / 'artifacts'
ROSTER = [('V Female', 'V', 'female'), ('V Male', 'V', 'male')]
ROSTER += [(name, name, 'female') for name in
           ['Judy', 'Panam', 'Johnny', 'Jackie', 'Viktor', 'Takemura',
            'River', 'Kerry', 'Reed', 'Songbird']]
INSTRUCTION = ('Match the reference speaker\'s voice, accent, and natural speaking style. '
               'Speak conversationally, with clear consonants and restrained confidence.')
TARGET = 'We have everything we need. Give me a minute, and I will find a way inside.'


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(path):
    stat = path.stat()
    return dict(path=str(path), size=stat.st_size, modified_ns=stat.st_mtime_ns)


def string_id(key):
    value = 0xcbf29ce484222325
    for byte in key.encode('utf-8'):
        value = ((value ^ byte) * 0x100000001b3) & ((1 << 64) - 1)
    return str(value)


def run(*args):
    result = subprocess.run(list(map(str, args)), cwd=REPO, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout[-4000:] + result.stderr[-4000:])


def search(actor):
    path = ROOT / 'search' / f'{actor.lower()}.json'
    if path.exists():
        cached = json.loads(path.read_text(encoding='utf-8'))
        if cached.get('_decoded_utf8'):
            return cached
    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=Retry(total=4, backoff_factor=1)))
    response = session.get('https://sounddb.zhincore.eu/v1/search/subtitles',
                           params={'q': 'actor:' + actor, 'per_page': 1000}, timeout=60)
    response.raise_for_status()
    data = json.loads(response.content.decode('utf-8'))
    if data.get('queryErrors') or data.get('syntaxErrors'):
        raise ValueError(data)
    data['_decoded_utf8'] = True
    save(path, data)
    return data


def select(name, actor, variant, data):
    candidates = []
    for item in data['items']:
        voice = item.get(variant) or {}
        text = voice.get('text') or (item.get('female') or {}).get('text', '')
        # SoundDB contains some UTF-8 punctuation previously decoded as CP1252.
        # Retain the raw search response; repair only a reversible mojibake form.
        if any(marker in text for marker in ('\u00e2\u20ac', '\u00c3', '\u00c2')):
            try:
                text = text.encode('cp1252').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        depot = (voice.get('vo') or {}).get('main', '').replace('\\', '/')
        duration = voice.get('duration', 0)
        scenes = [s for s in (item.get('scenes') or {}).values() if actor in s.get('actors', [])]
        spoken = any(n.get('expression') == 'Vo_Expression_Spoken'
                     for s in scenes for n in s.get('nodes', {}).values())
        if not (spoken and '/vo/' in depot and 5 <= duration <= 8.5
                and 45 <= len(text) <= 145 and '<' not in text and '[' not in text):
            continue
        if actor == 'V' and not Path(depot).name.startswith('v_'):
            continue
        candidates.append(dict(speaker=name, actor=actor, player_variant=variant,
                               string_id=item['id'], transcript=text, depot=depot,
                               advertised_duration_s=duration,
                               source_url='https://sounddb.redmodding.org/subtitles/' + item['id']))
    candidates.sort(key=lambda c: (abs(c['advertised_duration_s'] - 7), c['string_id']))
    chosen = []
    seen = set()
    for row in candidates:
        if row['transcript'] in seen:
            continue
        chosen.append(row)
        seen.add(row['transcript'])
        if len(chosen) == 3:
            return chosen
    raise ValueError(f'{name}: only {len(chosen)} eligible references')


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    actors = list(dict.fromkeys(actor for _, actor, _ in ROSTER))
    with ThreadPoolExecutor(max_workers=4) as pool:
        searches = dict(zip(actors, pool.map(search, actors)))
    rows = [row for name, actor, variant in ROSTER
            for row in select(name, actor, variant, searches[actor])]
    save(ROOT / 'selected-references.json', rows)
    print(f'Selected {len(rows)} references for {len(ROSTER)} voices.', flush=True)
    for prefix, archive in [('base', 'content'), ('ep1', 'ep1')]:
        depots = [r['depot'] for r in rows if r['depot'].startswith(prefix + '/')]
        if depots and any(not (ROOT / 'wem' / p).is_file() for p in depots):
            pattern = '(' + '|'.join(re.escape(Path(p).name) for p in depots) + ')$'
            run(WKIT, 'unbundle', f'H:/Cyberpunk 2077/archive/pc/{archive}/lang_en_voice.archive',
                '-o', ROOT / 'wem', '-r', pattern, '-v', 'quiet')
    if any(not (ROOT / 'ogg' / Path(r['depot']).with_suffix('.Ogg')).is_file() for r in rows):
        (ROOT / 'ogg').mkdir(parents=True, exist_ok=True)
        run(WKIT, 'export', ROOT / 'wem', '-o', ROOT / 'ogg',
            '--gamepath', 'H:/Cyberpunk 2077', '-v', 'quiet')
    pending = []
    pipeline_identity = dict(checkpoints=[identity(BASE / 'model.safetensors'),
                                         identity(BASE / 'speech_tokenizer/model.safetensors')],
                             artifacts=[identity(p) for artifact in
                                        ['base_speaker_encoder_mel4096', 'tokenizer_encoder_dynamic_s240000']
                                        for p in sorted((ART / artifact).rglob('*')) if p.is_file()])
    for row in rows:
        stem = Path(row['depot']).stem
        wav = ROOT / 'references' / (stem + '.wav')
        ogg = ROOT / 'ogg' / Path(row['depot']).with_suffix('.Ogg')
        if not wav.exists():
            wav.parent.mkdir(parents=True, exist_ok=True)
            run('ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', ogg,
                '-ar', '24000', '-ac', '1', '-c:a', 'pcm_s16le', wav)
        with wave.open(str(wav)) as source:
            row['duration_s'] = source.getnframes() / source.getframerate()
            assert source.getframerate() == 24000 and source.getnchannels() == 1
            assert 1920 <= source.getnframes() <= 240000
        row.update(wav=str(wav), wav_sha256=digest(wav),
                   embedding=str(ROOT / 'embeddings' / (stem + '.safetensors')),
                   codes=str(ROOT / 'codes' / (stem + '.json')))
        fingerprint = dict(wav_sha256=row['wav_sha256'], pipeline=pipeline_identity)
        receipt = ROOT / 'cache' / (stem + '.json')
        if not (receipt.exists() and json.loads(receipt.read_text()) == fingerprint
                and Path(row['embedding']).exists() and Path(row['codes']).exists()):
            pending.append((row, receipt, fingerprint))
    if pending:
        run(VOICE, 'extract-embeddings', '--checkpoint', BASE / 'model.safetensors',
            '--speaker-artifact', ART / 'base_speaker_encoder_mel4096',
            '--reference', *[r['wav'] for r, _, _ in pending], '--output-dir', ROOT / 'embeddings')
    for number, (row, receipt, fingerprint) in enumerate(pending, 1):
        run(VOICE, 'encode-reference', '--checkpoint', BASE / 'speech_tokenizer/model.safetensors',
            '--encoder-artifact', ART / 'tokenizer_encoder_dynamic_s240000',
            '--reference', row['wav'], '--output', row['codes'])
        save(receipt, fingerprint)
        print(f'Cached {number}/{len(pending)}: {row["speaker"]}', flush=True)
    for row in rows:
        codes = json.loads(Path(row['codes']).read_text(encoding='utf-8'))
        with wave.open(row['wav']) as source:
            assert codes['frame_count'] == (source.getnframes() + 1919) // 1920
        assert codes['code_groups'] == 16
        assert len(codes['values']) == codes['frame_count'] * 16
        assert all(0 <= value < 2048 for value in codes['values'])
        data = Path(row['embedding']).read_bytes()
        header = json.loads(data[8:8 + struct.unpack('<Q', data[:8])[0]])
        assert any(v.get('shape') == [2048] and v.get('dtype') == 'F32'
                   for v in header.values() if isinstance(v, dict))
        row.update(codes_sha256=digest(Path(row['codes'])),
                   embedding_sha256=digest(Path(row['embedding'])))
    save(ROOT / 'generation-recipe.json', dict(
        schema_version=1, method='Full + Instruction', checkpoint=str(BASE), language='English',
        reference_prompts=str(ROOT / 'reference-prompts.json'),
        index=str(ROOT / 'voice-production.json'), instruction=INSTRUCTION,
        generation_artifact=str(ART / 'base_generation_p256_f288'),
        decoder_artifact=str(ART / 'tokenizer_decoder_f256'), seed_base=12000,
        versions=1, max_frames=120, temperature=0.95, top_k=50, top_p=0.98,
        repetition_penalty=1.0, subtalker_temperature=0.9, subtalker_top_k=50,
        subtalker_top_p=1.0))
    save(ROOT / 'catalog.json', dict(schema_version=1, model=BASE.name,
         instruction=INSTRUCTION, review_status='reference choices awaiting listening review', references=rows))
    sources = {}
    prompts = {}
    lines = []
    for row in rows:
        option = sum(r['speaker'] == row['speaker'] for r in rows[:rows.index(row)]) + 1
        speaker = row['speaker'] + f' Reference {option}'
        key = re.sub('[^a-z0-9]+', '_', speaker.lower())
        sources[speaker] = dict(mode='speaker_embedding', source=row['embedding'])
        prompts[speaker] = dict(text=row['transcript'], codes=row['codes'])
        lines.append(dict(key=key, string_id=string_id(key),
                          speaker=speaker, addressee='Listener', text=TARGET,
                          audio_path=f'mod\\vanilla_audition\\localization\\en-us\\vo\\{key}.wem', duration_ms=7000))
        row['audition_key'] = key
    save(ROOT / 'audition-manifest.json', dict(spoken_lines=lines))
    save(ROOT / 'reference-prompts.json', prompts)
    save(ROOT / 'voice-production.json', dict(schema_version=1, quest='vanilla_audition',
         spoken_line_count=len(lines), voice_sources=sources,
         manifests=[dict(id='vanilla_audition', file='audition-manifest.json', delivery='audition',
                         runtime_status='not_integrated', line_count=len(lines), speakers=sorted(sources))]))
    run(VOICE, 'validate', '--index', ROOT / 'voice-production.json')
    print('Rendering Full + Instruction auditions.', flush=True)
    run(VOICE, 'render-local', '--index', ROOT / 'voice-production.json', '--checkpoint', BASE,
        '--generation-artifact', ART / 'base_generation_p256_f288',
        '--decoder-artifact', ART / 'tokenizer_decoder_f256', '--reference-prompts', ROOT / 'reference-prompts.json',
        '--instruction', INSTRUCTION, '--output', ROOT / 'samples', '--versions', '1',
        '--seed-base', '12000', '--max-frames', '120')
    report = json.loads((ROOT / 'samples/render-report.json').read_text())
    assert len(report['candidates']) == len(rows)
    for c in report['candidates']:
        assert digest(ROOT / 'samples' / c['wav']) == c['sha256']
    save(ROOT / 'catalog.json', dict(schema_version=1, model=BASE.name, instruction=INSTRUCTION,
         review_status='reference choices awaiting listening review', references=rows))
    markup = ['<!doctype html><meta charset="utf-8"><title>Vanilla voice library</title>',
              '<style>body{font:16px system-ui;background:#11151d;color:#edf1f7;max-width:1150px;margin:32px auto}table{width:100%}td{padding:12px;vertical-align:top}audio{width:100%}a{color:#9dcaff}</style>',
              '<h1>Vanilla voices — Full + Instruction</h1><p>Three reference choices per voice. References need listening review; existing V embeddings remain available.</p>',
              '<p>Target: ' + html.escape(TARGET) + '</p>']
    for name, _, _ in ROSTER:
        markup.append('<h2>' + html.escape(name) + '</h2><table><tr>')
        for row in [r for r in rows if r['speaker'] == name]:
            ref = Path(row['wav']).relative_to(ROOT).as_posix()
            sample = 'samples/vanilla_audition/' + row['audition_key'] + '-version00.wav'
            markup.append(f'<td><p>{html.escape(row["transcript"])}</p><p>Reference ({row["duration_s"]:.2f}s)</p><audio controls preload="none" src="{ref}"></audio><p>Generated</p><audio controls preload="none" src="{sample}"></audio></td>')
        markup.append('</tr></table>')
    (ROOT / 'comparison.html').write_text('\n'.join(markup), encoding='utf-8')
    print(f'Complete: {len(rows)} cached reference pairs and verified auditions.', flush=True)


if __name__ == '__main__':
    main()
