"""Second neutral reference audition after user listening feedback."""
import prepare_neutral_npcs as workflow
import json
from pathlib import Path

workflow.ROOT = workflow.shared.ROOT / 'npc-revision2'
workflow.SELECTIONS = {
    # Songbird's q303_06_paradise conversation, avoiding the rejected coffee clip.
    'Songbird': ['3497061915993182208', '3497181714744217600'],
    'Kerry': ['1380775665492160512', '1804358115924860928'],
    'Panam': ['1664847311733911552', '1834318768515108864'],
}
workflow.ACCENT_INSTRUCTIONS = {}


def add_original_exports():
    root = workflow.ROOT
    page = root / 'comparison.html'
    markup = page.read_text(encoding='utf-8')
    for row in json.loads((root / 'catalog.json').read_text(encoding='utf-8'))['references']:
        original = 'ogg/' + Path(row['depot']).with_suffix('.Ogg').as_posix()
        marker = '<p>Reference</p><audio controls preload="none" src="' + Path(row['wav']).relative_to(root).as_posix() + '"></audio>'
        if 'src="' + original + '"' not in markup:
            markup = markup.replace(marker, marker.replace('<p>Reference</p>', '<p>Model reference — 24 kHz</p>') +
                         '<p>Original exported audio — before resampling</p><audio controls preload="none" src="' + original + '"></audio>')
        prior_sample = '../npc-neutral/samples/full/vanilla_audition/' + row['key'] + '-version00.wav'
        new_sample = '<p>Full reference — no instruction</p><audio controls preload="none" src="samples/full/vanilla_audition/' + row['key'] + '-version00.wav"></audio>'
        if 'src="' + prior_sample + '"' not in markup:
            markup = markup.replace(new_sample, new_sample +
                         '<p>Previous reference result — same text and seed</p><audio controls preload="none" src="' + prior_sample + '"></audio>')
    page.write_text(markup, encoding='utf-8')
    prior = workflow.shared.ROOT / 'npc-neutral/comparison.html'
    markup = prior.read_text(encoding='utf-8')
    if 'id="revision2"' not in markup:
        markup = markup.replace('<h1>', '<p id="revision2"><a href="../npc-revision2/comparison.html">New Songbird, Kerry and Panam reference comparisons</a></p><h1>', 1)
        prior.write_text(markup, encoding='utf-8')

if __name__ == '__main__':
    workflow.main()
    add_original_exports()
