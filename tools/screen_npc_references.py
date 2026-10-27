"""Stage source clips for gameplay/provenance and signal screening before cloning."""
import argparse
import json

import prepare_neutral_npcs as workflow

ROOT = workflow.shared.ROOT / 'npc-screened'
SELECTIONS = {
    'Songbird': ['3273933107471863812', '3273933107471863824',
                '2983635373759942656', '2983636822774534144'],
    'Kerry': ['1807175567395217412', '1834734088295673856'],
    'Panam': ['1896726949659815948', '1896726950012137500'],
}
original_search = workflow.shared.search


def expanded_search(actor):
    data = original_search(actor)
    items = {i['id']: i for i in data['items']}
    for path in sorted((workflow.shared.ROOT / 'search').glob(actor.lower() + '-*.json')):
        for item in json.loads(path.read_text(encoding='utf-8')).get('items', []):
            items[item['id']] = item
    return {**data, 'items': list(items.values())}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--decode-only', action='store_true')
    args = parser.parse_args()
    workflow.ROOT = ROOT
    workflow.SELECTIONS = SELECTIONS
    workflow.ACCENT_INSTRUCTIONS = {}
    workflow.shared.search = expanded_search
    workflow.main(prepare_only=args.decode_only)
