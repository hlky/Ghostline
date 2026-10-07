# Quest reference inputs

`ign-index-snapshot.json` is the checked input for the offline quest-reference
generator. It retains IGN index titles and URLs only; it contains no walkthrough
article prose. The journal export supplies the quest descriptions and structure.

The snapshot was reconstructed on 2026-09-05 from `ign-link-map.json` at repository
revision `29bdc504cad11fa5e7bcb3e435b93f83eb5f376b` (original file SHA-256
`7392c4a62d81e6e851f0ec62c4bffb002b52a7a95363fea7eee0dd428dacca85`). For each
category, reconstruction combined matched `ign_title`/`ign_url` pairs with
`unmatched_index_links`, deduplicated exact title/URL pairs, and sorted those
pairs. It retained 79 main-job, 94 side-job, and 95 gig links. No network request
was made. The original fetch date is unknown; this reconstruction cannot recover
links that the previous generator discarded, and is not a current IGN scrape.

The local journal input used for this regeneration is `H:\projects\quest.json`,
SHA-256 `b39930c6cdee37f985fd489a511f34dfe0865a00b69ff37a441da307dc41fb28`.
It is an external game-data export, not a checked repository input. Reproducing
the same reference requires the same export; its content hash in the generated
link map detects a different input. `ign-link-map.json` now records the journal,
snapshot, and generator paths and SHA-256 hashes on each run.

Run from the repository root:

```powershell
py -B tools/build_quest_reference.py --quest-json H:\projects\quest.json
```

This uses the checked snapshot without importing network dependencies. To use a
different export or snapshot, supply `--quest-json` or `--index-snapshot`.
`--refresh-indexes` explicitly fetches current IGN index links and replaces the
snapshot before generating the reference; review the snapshot diff when using it.
Keep provenance with a refreshed snapshot instead of presenting its links as the
original reconstruction.
