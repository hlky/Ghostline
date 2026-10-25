"""Rerender the four V methods changing only 'I will' to 'I'll'."""
import html
import json
import re
import wave

import numpy as np
import prepare_vanilla_voices as shared
from compare_v_references import ROOT


def main():
    destination = ROOT / 'contraction'
    destination.mkdir(exist_ok=True)
    previous = json.loads((ROOT / 'experiment.json').read_text(encoding='utf-8'))
    inputs = json.loads((ROOT / 'inputs.json').read_text(encoding='utf-8'))
    manifest = json.loads((ROOT / 'audition-manifest.json').read_text(encoding='utf-8'))
    target = previous['target_text'].replace('I will', "I'll")
    assert target != previous['target_text']
    for line in manifest['spoken_lines']:
        assert line['text'] == previous['target_text']
        line['text'] = target
    shared.save(destination / 'audition-manifest.json', manifest)
    index = json.loads((ROOT / 'voice-production.json').read_text(encoding='utf-8'))
    shared.save(destination / 'voice-production.json', index)
    shared.run(shared.VOICE, 'validate', '--index', destination / 'voice-production.json')
    shared.save(ROOT / 'preferred-method.json', dict(method='full', status='tentative',
                selected_by='user listening feedback', feedback='So far full reference sounds best.',
                date='2026-10-12', instruction=None))
    reports = {}
    sampling_args = [value for key, value in previous['sampling'].items()
                     for value in ['--' + key.replace('_', '-'), str(value)]]
    for method, info in previous['methods'].items():
        print('Rendering contracted text: ' + info['label'], flush=True)
        overrides = [value for variant, reference in inputs.items() for value in
                     ['--embedding', 'V ' + variant.title() + ' Reference 1=' + reference[info['embedding']]]]
        shared.run(shared.VOICE, 'render-local', '--index', destination / 'voice-production.json',
                   '--checkpoint', previous['checkpoint'], '--generation-artifact', previous['generation_artifact'],
                   '--decoder-artifact', previous['decoder_artifact'], '--reference-prompts', ROOT / 'reference-prompts.json',
                   '--output', destination / 'samples' / method, '--versions', '1',
                   '--seed-base', previous['seed_base'], '--max-frames', previous['max_frames'], *overrides, *sampling_args,
                   *(['--instruction', info['instruction']] if info['instruction'] else []))
        report = json.loads((destination / 'samples' / method / 'render-report.json').read_text(encoding='utf-8'))
        for candidate in report['candidates']:
            assert candidate['seed'] == previous['expected_seeds'][candidate['line_key']]
            path = destination / 'samples' / method / candidate['wav']
            assert shared.digest(path) == candidate['sha256']
            with wave.open(str(path)) as source:
                assert source.getframerate() == 24000 and source.getnchannels() == 1 and source.getsampwidth() == 2
                audio = np.frombuffer(source.readframes(source.getnframes()), dtype='<i2')
            assert 0 < len(audio) < previous['max_frames'] * 1920 and np.any(audio)
            assert not np.any((audio == -32768) | (audio == 32767))
        reports[method] = dict(**{k: info[k] for k in ['label', 'embedding', 'instruction']}, report=report)
    shared.save(destination / 'experiment.json',
                {**previous, 'methods': reports, 'original_target_text': previous['target_text'], 'target_text': target,
                 'controls': "Only target text changes: I will -> I'll. References, embeddings, instructions, per-voice seeds and sampling are unchanged."})
    page = ['<!doctype html><meta charset="utf-8"><title>V contraction comparison</title>',
            '<style>body{font:16px system-ui;background:#11151d;color:#edf1f7;max-width:1400px;margin:32px auto}table{width:100%;table-layout:fixed}td,th{padding:12px;vertical-align:top}audio{width:100%}a{color:#9dcaff}</style>',
            '<h1>V — I will versus I\'ll</h1><p>Full reference is the tentative preference. Only the spoken text changes; each method retains the same reference, embedding, instruction, seed and sampling.</p>',
            '<p>New text: ' + html.escape(target) + '</p>']
    for variant in inputs:
        page.append('<h2>V ' + variant.title() + '</h2><table><tr>' + ''.join('<th>' + info['label'] + '</th>' for info in reports.values()) + '</tr><tr>')
        for method in reports:
            file = f'vanilla_audition/v_{variant}_reference_1-version00.wav'
            page.append(f'<td><p>I will — original</p><audio controls preload="none" src="../samples/{method}/{file}"></audio><p>I\'ll — new</p><audio controls preload="none" src="samples/{method}/{file}"></audio></td>')
        page.append('</tr></table>')
    markup = '\n'.join(page)
    assert all((destination / p).is_file() for p in re.findall(r'src="([^"]+)"', markup))
    (destination / 'comparison.html').write_text(markup, encoding='utf-8')
    original = ROOT / 'comparison.html'
    markup = original.read_text(encoding='utf-8')
    if 'id="contraction-comparison"' not in markup:
        markup = markup.replace('<h1>', '<p id="contraction-comparison"><a href="contraction/comparison.html">New: compare I will versus I\'ll across all four methods</a>. Tentative preference: full reference.</p><h1>', 1)
        original.write_text(markup, encoding='utf-8')
    print('Complete: eight contracted-text auditions; original samples preserved.', flush=True)


if __name__ == '__main__':
    main()
